#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'RELEASE_MANIFEST.json'
EXCLUDE={OUT.resolve(), (ROOT/'validation/release-validation.json').resolve()}
files=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or p.resolve() in EXCLUDE:
        continue
    if '__pycache__' in p.parts or p.suffix=='.pyc':
        continue
    b=p.read_bytes()
    files.append({'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
out={'spec_version':'0.1.0','manifest_version':'1','hash_algorithm':'sha256','exclusions':['RELEASE_MANIFEST.json','validation/release-validation.json (generated validation evidence)'],'file_count':len(files),'files':files}
OUT.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(f'wrote {OUT} with {len(files)} entries')
