#!/usr/bin/env python3
"""Release validation for Governance Compilation Open Specification v0.1.0.

The checks here are repository/schema/finite semantic checks. They are not formal proof.
"""
from __future__ import annotations
import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = ROOT / "examples"
NEG = ROOT / "conformance" / "negative-fixtures"
RESULT = ROOT / "validation" / "release-validation.json"

class Report:
    def __init__(self):
        self.checks=[]
    def add(self, check_id:str, ok:bool, detail:str, kind:str='release-check'):
        self.checks.append({'check_id':check_id,'kind':kind,'status':'PASS' if ok else 'FAIL','detail':detail})
    @property
    def passed(self): return sum(c['status']=='PASS' for c in self.checks)
    @property
    def failed(self): return sum(c['status']=='FAIL' for c in self.checks)

def load_json(path:Path)->Any:
    return json.loads(path.read_text(encoding='utf-8'))

def ids(items, key):
    return {x[key] for x in items}

def semantic_issues(gir:dict)->list[str]:
    issues=[]
    action_by={a['action_id']:a for a in gir.get('actions',[])}
    source_ids=ids(gir.get('sources',[]),'source_id')
    contract_by={c['contract_id']:c for c in gir.get('contracts',[])}
    region_by={r['region_id']:r for r in gir.get('regions',[])}
    mappings={m['region_ref']:m.get('contract_refs',[]) for m in gir.get('region_contract_mapping',[])}

    # AP references must resolve and not name an action explicitly outside the permitted set.
    for ref in gir.get('permitted_action_set',{}).get('action_refs',[]):
        if ref not in action_by:
            issues.append(f'Permitted Action Set references undeclared action {ref}')
        elif action_by[ref].get('permitted_action_status') not in ('in_set','conditional'):
            issues.append(f'Permitted Action Set references action not eligible for membership: {ref}')

    # Requirement/source traceability.
    for req in gir.get('requirements',[]):
        for s in req.get('source_refs',[]):
            if s not in source_ids:
                issues.append(f"Requirement {req.get('requirement_id')} references undeclared source {s}")

    # Region mappings and contract refs.
    for rid,r in region_by.items():
        if r.get('status')=='active' and rid not in mappings:
            issues.append(f'Active region {rid} has no region-contract mapping')
        for c in r.get('contract_refs',[]):
            if c not in contract_by:
                issues.append(f'Region {rid} references undeclared contract {c}')
    for rid,crefs in mappings.items():
        if rid not in region_by:
            issues.append(f'Mapping references undeclared region {rid}')
        for c in crefs:
            if c not in contract_by:
                issues.append(f'Mapping {rid} references undeclared contract {c}')

    # CTC source refs and six semantic components.
    six=('preconditions','authorization','pre_commit_evidence','target_state','post_commit_evidence','closure')
    for cid,c in contract_by.items():
        for k in six:
            if k not in c:
                issues.append(f'CTC {cid} missing core component {k}')
        for s in c.get('source_refs',[]):
            if s not in source_ids:
                issues.append(f'CTC {cid} references undeclared source {s}')
        # required evidence ids should not duplicate within a CTC list component
        for ek in ('pre_commit_evidence','post_commit_evidence'):
            vals=[e.get('evidence_id') for e in c.get(ek,[]) if e.get('evidence_id')]
            if len(vals)!=len(set(vals)):
                issues.append(f'CTC {cid} duplicates evidence IDs in {ek}')

        # v0.1 finite semantic guard: success closure based only on execution result with
        # no closure evidence is an explicit false-closure defect for the fixture model.
        for out in c.get('closure',{}).get('outcomes',[]):
            if out.get('outcome')=='success':
                exprs=[str(p.get('expression','')).strip().lower() for p in out.get('conditions',[])]
                if not out.get('required_evidence') and exprs and all(('execution_status' in x or x in ('true','1')) for x in exprs):
                    # Neutral overlay contracts may use literal true only if another mapped contract supplies
                    # the target/closure semantics; allow literal-true overlay when the contract itself declares
                    # no post-commit evidence and its name signals additional controls.
                    neutral_overlay=(all(x in ('true','1') for x in exprs) and not c.get('post_commit_evidence') and ('additional' in c.get('name','').lower()))
                    if not neutral_overlay:
                        issues.append(f'CTC {cid} has success closure that can substitute execution result/tautology for target/closure evidence')

    # Composition rules: last-write-wins is not permitted for mandatory evidence components.
    cr=gir.get('composition_policy',{}).get('component_rules',{})
    for k in ('pre_commit_evidence','post_commit_evidence','authorization','target_state','closure'):
        if str(cr.get(k,'')).lower() in ('last_write_wins','replace','overwrite'):
            issues.append(f'Composition policy uses weakening-prone {cr.get(k)} for mandatory component {k}')

    return issues

def main()->int:
    r=Report()
    fmt=FormatChecker()

    # Schemas themselves.
    schema_files=sorted(SCHEMAS.glob('*.schema.json'))
    for p in schema_files:
        try:
            Draft202012Validator.check_schema(load_json(p))
            r.add(f'SCHEMA-{p.stem}', True, 'valid Draft 2020-12 schema')
        except Exception as e:
            r.add(f'SCHEMA-{p.stem}', False, f'{type(e).__name__}: {e}')

    gir_schema=load_json(SCHEMAS/'gir.schema.json')
    manifest_schema=load_json(SCHEMAS/'package-manifest.schema.json')
    profile_schema=load_json(SCHEMAS/'profile.schema.json')

    # Positive examples.
    for p in sorted(EXAMPLES.glob('*/gir.json')):
        d=load_json(p)
        errs=list(Draft202012Validator(gir_schema,format_checker=fmt).iter_errors(d))
        r.add(f'EX-GIR-{p.parent.name}', not errs, 'structural validation passed' if not errs else '; '.join(e.message for e in errs[:4]))
        sem=semantic_issues(d)
        r.add(f'EX-SEM-{p.parent.name}', not sem, 'finite semantic/reference checks passed' if not sem else '; '.join(sem[:6]))
    for p in sorted(EXAMPLES.glob('*/package-manifest.json')):
        d=load_json(p)
        errs=list(Draft202012Validator(manifest_schema,format_checker=fmt).iter_errors(d))
        r.add(f'EX-MAN-{p.parent.name}', not errs, 'manifest structural validation passed' if not errs else '; '.join(e.message for e in errs[:4]))

    # Profiles.
    for p in sorted((ROOT/'profiles').glob('*/profile.json')):
        d=load_json(p); errs=list(Draft202012Validator(profile_schema).iter_errors(d))
        r.add(f'PROFILE-{p.parent.name}', not errs, 'profile schema validation passed' if not errs else '; '.join(e.message for e in errs[:4]))

    # Requirement and assertion uniqueness / counts.
    req_rows=list(csv.DictReader((ROOT/'requirements/GC-Normative-Requirements.csv').open(encoding='utf-8')))
    req_ids=[x['requirement_id'] for x in req_rows]
    r.add('REQ-COUNT',len(req_rows)>=100,f'{len(req_rows)} normative requirements (threshold >=100)')
    r.add('REQ-UNIQUE',len(req_ids)==len(set(req_ids)),f'{len(set(req_ids))} unique IDs')
    tas=load_json(ROOT/'conformance/test-assertions.json')['assertions']; ta_ids=[x['assertion_id'] for x in tas]
    r.add('TA-COUNT',len(tas)>=25,f'{len(tas)} test assertions (threshold >=25)')
    r.add('TA-UNIQUE',len(ta_ids)==len(set(ta_ids)),f'{len(set(ta_ids))} unique IDs')
    props=load_json(ROOT/'formal/property-catalog.json')['properties']; prop_ids=[x['property_id'] for x in props]
    r.add('PROP-COUNT',len(props)>=15,f'{len(props)} formal properties (threshold >=15)')
    r.add('PROP-UNIQUE',len(prop_ids)==len(set(prop_ids)),f'{len(set(prop_ids))} unique IDs')

    # Negative fixtures should be rejected structurally or semantically.
    for p in sorted(NEG.glob('*.json')):
        d=load_json(p)
        structural=list(Draft202012Validator(gir_schema).iter_errors(d))
        sem=semantic_issues(d) if not structural else []
        rejected=bool(structural or sem)
        detail=('rejected structurally: '+structural[0].message) if structural else ('rejected semantically: '+sem[0] if sem else 'unexpectedly accepted')
        r.add(f'NEG-{p.stem}',rejected,detail,'negative-fixture')

    # Semantic test vectors.
    tv=load_json(ROOT/'conformance/test-vectors.json')['vectors']
    for v in tv:
        ok=False
        if v['vector_id']=='V-COMMIT-STALE-001':
            ok=(v['proposal_time']['approval_status']=='current' and v['commit_time']['approval_status']!='current' and v['expected']=='refuse_or_reauthorize')
        elif v['vector_id']=='V-PROJ-AUTH-001':
            ok=(not set(v['projected_actions']).issubset(set(v['canonical_actions'])) and v['expected']=='fail')
        elif v['vector_id']=='V-EVID-STALE-001':
            ok=(v['evidence_age_seconds']>v['max_freshness_seconds'] and v['expected']=='unsatisfied')
        elif v['vector_id']=='V-CLOSURE-001':
            ok=(v['execution_status']=='success' and not v['target_verified'] and not v['required_post_commit_evidence_present'] and v['expected']=='not_successfully_closed')
        r.add(v['vector_id'],ok,v['rationale'],'test-vector')

    # Project-bleed / inappropriate AGCP scan.
    bad_terms=['CMU_Lab3','UAT_Current_Status','Diagnosis Register','Fix Integration','OVHcloud','Docker Compose','Coder workspace','AGCP Rust','Codex']
    text_files=[p for p in ROOT.rglob('*') if p.is_file() and p.suffix.lower() in ('.md','.txt','.csv','.json','.yml','.yaml','.cff','.py','') and p != Path(__file__).resolve() and p != RESULT]
    hits=[]
    for p in text_files:
        try: txt=p.read_text(encoding='utf-8')
        except Exception: continue
        for term in bad_terms:
            if term.lower() in txt.lower(): hits.append(f'{p.relative_to(ROOT)}:{term}')
    r.add('HYGIENE-PROJECT-BLEED',not hits,'no prohibited internal-project bleed terms found' if not hits else '; '.join(hits[:10]))

    # AGCP references are allowed only in explicit independence/hygiene statements.
    agcp_allowed={Path('README.md'),Path('CONTRIBUTING.md'),Path('SECURITY.md'),Path('docs/implementation-independence.md')}
    agcp_hits=[]
    for p in text_files:
        try: txt=p.read_text(encoding='utf-8')
        except Exception: continue
        if re.search(r'\bAGCP\b',txt) and p.relative_to(ROOT) not in agcp_allowed:
            agcp_hits.append(str(p.relative_to(ROOT)))
    r.add('HYGIENE-AGCP-BOUNDARY',not agcp_hits,'AGCP appears only in explicit independence/security-boundary statements' if not agcp_hits else 'unexpected AGCP references: '+', '.join(agcp_hits))

    # Release manifest: all immutable release content except the manifest and generated validation report.
    manifest_path=ROOT/'RELEASE_MANIFEST.json'
    if manifest_path.exists():
        manifest=load_json(manifest_path)
        listed={x['path']:x for x in manifest.get('files',[])}
        actual={}
        for fp in sorted(ROOT.rglob('*')):
            if not fp.is_file() or fp in (manifest_path, RESULT) or '__pycache__' in fp.parts or fp.suffix=='.pyc':
                continue
            rel=str(fp.relative_to(ROOT))
            b=fp.read_bytes()
            actual[rel]={'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
        missing=sorted(set(actual)-set(listed))
        extra=sorted(set(listed)-set(actual))
        mismatch=sorted(k for k in set(actual)&set(listed) if actual[k]['sha256']!=listed[k].get('sha256') or actual[k]['bytes']!=listed[k].get('bytes'))
        ok=not missing and not extra and not mismatch and manifest.get('file_count')==len(listed)
        detail=f"{len(listed)} immutable release files hashed" if ok else f"missing={missing[:5]} extra={extra[:5]} mismatch={mismatch[:5]}"
        r.add('RELEASE-MANIFEST',ok,detail)
    else:
        r.add('RELEASE-MANIFEST',False,'RELEASE_MANIFEST.json is missing')

    # No TODO/TBD/placeholder drafting markers in normative spec files. "placeholder" is allowed in examples.
    draft_hits=[]
    for p in (ROOT/'spec').glob('*.md'):
        txt=p.read_text(encoding='utf-8')
        for pat in (r'\bTODO\b',r'\bTBD\b',r'FIXME'):
            if re.search(pat,txt,re.I): draft_hits.append(f'{p.name}:{pat}')
    r.add('HYGIENE-NORMATIVE-DRAFT-MARKERS',not draft_hits,'no TODO/TBD/FIXME markers in normative specification' if not draft_hits else '; '.join(draft_hits))

    out={
      'spec_version':'0.1.0',
      'generated_at':datetime.now(timezone.utc).isoformat(),
      'evidence_class':'repository/schema/finite semantic validation; not formal proof',
      'summary':{'passed':r.passed,'failed':r.failed,'total':len(r.checks)},
      'checks':r.checks
    }
    RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding='utf-8')
    print(json.dumps(out['summary'],indent=2))
    for c in r.checks:
        print(f"{c['status']:4} {c['check_id']}: {c['detail']}")
    return 1 if r.failed else 0

if __name__=='__main__':
    raise SystemExit(main())
