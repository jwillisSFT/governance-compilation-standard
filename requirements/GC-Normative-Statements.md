# GC Normative Requirements Catalog

**Release:** v0.1.0  
**Requirement count:** 215

This catalog provides stable identifiers for the principal normative statements in the v0.1.0 specification. The detailed specification modules control where additional context is necessary.

## SRC

- **`GC-SRC-001`** — Each compilation SHALL establish an identifiable authorized governance-source baseline.  
  Source: `GC-Core §3`
- **`GC-SRC-002`** — Each material source SHALL have a stable source identifier.  
  Source: `GC-Core §3`
- **`GC-SRC-003`** — Each material source SHALL record version or revision status where applicable.  
  Source: `GC-Core §3`
- **`GC-SRC-004`** — Each material source SHALL identify its issuing authority or authority basis.  
  Source: `GC-Core §3`
- **`GC-SRC-005`** — Each material source SHALL record declared applicability to the compilation scope.  
  Source: `GC-Core §3`
- **`GC-SRC-006`** — Each material source SHALL record effective, superseded, withdrawn, or equivalent lifecycle status.  
  Source: `GC-Core §3`
- **`GC-SRC-007`** — Each material source SHALL preserve provenance sufficient to identify origin and acquisition path.  
  Source: `GC-Core §3`
- **`GC-SRC-008`** — Explicitly excluded material sources SHALL be recorded when their exclusion affects scope or completeness claims.  
  Source: `GC-Core §3`
- **`GC-SRC-009`** — Disputed or unknown source applicability SHALL be represented as uncertainty, limitation, escalation, or refusal rather than silently resolved by the compiler.  
  Source: `GC-Core §3`
- **`GC-SRC-010`** — Source authorization for compilation SHALL NOT be represented as proof of legal validity, normative legitimacy, constitutionality, substantive correctness, or proportionality.  
  Source: `GC-Core §3`
## SCP

- **`GC-SCP-001`** — Each compilation SHALL declare the scope to which its normative and completeness claims apply.  
  Source: `GC-Core §4`
- **`GC-SCP-002`** — The declared scope SHALL identify the governed domain and target classes.  
  Source: `GC-Core §4`
- **`GC-SCP-003`** — The declared scope SHALL identify applicable organizations, tenants, or jurisdictional boundaries where material.  
  Source: `GC-Core §4`
- **`GC-SCP-004`** — The declared scope SHALL identify actors and authority relationships material to the governed actions.  
  Source: `GC-Core §4`
- **`GC-SCP-005`** — The declared scope SHALL identify effective period or temporal assumptions where material.  
  Source: `GC-Core §4`
- **`GC-SCP-006`** — The declared scope SHALL identify applicable constitutional and system invariants.  
  Source: `GC-Core §4`
- **`GC-SCP-007`** — The declared scope SHALL identify material threat/failure assumptions and exclusions.  
  Source: `GC-Core §4`
- **`GC-SCP-008`** — An implementation SHALL NOT make an unqualified completeness claim when the relevant scope boundary is undeclared.  
  Source: `GC-Core §4`
## INT

- **`GC-INT-001`** — Material interpretation decisions SHALL be attributable to an identified authority or authorized process.  
  Source: `GC-Core §5`
- **`GC-INT-002`** — An interpretation record SHALL identify the affected source or requirement.  
  Source: `GC-Core §5`
- **`GC-INT-003`** — An interpretation record SHALL record the selected interpretation and material scope.  
  Source: `GC-Core §5`
- **`GC-INT-004`** — An interpretation record SHOULD record alternatives considered when they materially affect authority or behavior.  
  Source: `GC-Core §5`
- **`GC-INT-005`** — An interpretation record SHALL record material assumptions and unresolved uncertainty.  
  Source: `GC-Core §5`
- **`GC-INT-006`** — AI- or tool-generated interpretation SHALL NOT become institutionally authoritative solely because it was generated automatically.  
  Source: `GC-Core §5`
- **`GC-INT-007`** — Irreducible ambiguity SHALL NOT be silently converted into deterministic semantics.  
  Source: `GC-Core §5`
- **`GC-INT-008`** — When ambiguity remains material, the implementation SHALL use authorized interpretation, bounded discretion, narrowed scope, indeterminate/escalation semantics, or refusal.  
  Source: `GC-Core §5`
- **`GC-INT-009`** — Interpretation changes SHALL be evaluated for downstream model/package impact.  
  Source: `GC-Core §5`
## TRC

- **`GC-TRC-001`** — Governance requirements SHALL remain traceable to authorized source and interpretation provenance.  
  Source: `GC-Core §§5,9-11`
- **`GC-TRC-002`** — Traceability SHALL permit navigation from source to canonical model elements.  
  Source: `GC-Core §§5,9-11`
- **`GC-TRC-003`** — Traceability SHALL permit navigation from canonical model elements to source/interpretation basis.  
  Source: `GC-Core §§5,9-11`
- **`GC-TRC-004`** — Target artifacts SHALL remain traceable to the canonical model elements from which they were projected.  
  Source: `GC-Core §§5,9-11`
- **`GC-TRC-005`** — Validation evidence SHALL identify the model/package/object to which it applies.  
  Source: `GC-Core §§5,9-11`
- **`GC-TRC-006`** — Approval and issuance records SHALL bind to the exact model or package identity approved.  
  Source: `GC-Core §§5,9-11`
- **`GC-TRC-007`** — Activation records SHALL bind to the exact package identity and runtime scope activated.  
  Source: `GC-Core §§5,9-11`
- **`GC-TRC-008`** — Runtime evidence SHOULD identify the active package/governance version used for the decision.  
  Source: `GC-Core §§5,9-11`
## GIR

- **`GC-GIR-001`** — A GIR document SHALL have stable identity and version.  
  Source: `GC-GIR`
- **`GC-GIR-002`** — A GIR document SHALL identify the Governance Compilation specification version to which it claims conformance.  
  Source: `GC-GIR`
- **`GC-GIR-003`** — A GIR document SHALL identify its declared scope.  
  Source: `GC-GIR`
- **`GC-GIR-004`** — GIR cross-object references SHALL use stable identifiers rather than display names alone.  
  Source: `GC-GIR`
- **`GC-GIR-005`** — The GIR SHALL represent governance requirements and their source/interpretation linkage.  
  Source: `GC-GIR`
- **`GC-GIR-006`** — The GIR SHALL represent governed actions and typed targets/parameters sufficient for the declared authority boundary.  
  Source: `GC-GIR`
- **`GC-GIR-007`** — The GIR SHALL represent the Permitted Action Set separately from current authorization conditions.  
  Source: `GC-GIR`
- **`GC-GIR-008`** — The GIR SHALL represent applicable authority and authority provenance.  
  Source: `GC-GIR`
- **`GC-GIR-009`** — The GIR SHALL represent mandatory evidence semantics and trust conditions required by the profile.  
  Source: `GC-GIR`
- **`GC-GIR-010`** — The GIR SHALL represent applicable constitutional and system invariants.  
  Source: `GC-GIR`
- **`GC-GIR-011`** — The GIR SHALL represent explicit refusal, indeterminate, or escalation behavior where applicable.  
  Source: `GC-GIR`
- **`GC-GIR-012`** — The GIR SHALL represent temporal/lifecycle conditions that affect applicability or authority.  
  Source: `GC-GIR`
- **`GC-GIR-013`** — The GIR SHALL represent assumptions, limitations, profiles, and mandatory extensions.  
  Source: `GC-GIR`
- **`GC-GIR-014`** — An unknown mandatory GIR extension affecting authority, evidence, target-state, composition, or closure SHALL NOT be silently ignored.  
  Source: `GC-GIR`
- **`GC-GIR-015`** — An interchange implementation claiming GIR conformance SHALL preserve all mandatory core semantics through serialization/deserialization.  
  Source: `GC-GIR`
## AUT

- **`GC-AUT-001`** — Computational capability SHALL NOT be treated as evidence that an action is inside the Permitted Action Set.  
  Source: `GC-GIR §5-6; GC-Transition §1`
- **`GC-AUT-002`** — An action outside the active Permitted Action Set SHALL NOT become authorized solely because it can be proposed or executed.  
  Source: `GC-GIR §5-6; GC-Transition §1`
- **`GC-AUT-003`** — Membership in the Permitted Action Set SHALL NOT by itself authorize a concrete action.  
  Source: `GC-GIR §5-6; GC-Transition §1`
- **`GC-AUT-004`** — Current authorization SHALL be evaluated against applicable actor/principal authority, scope, target, state, time, evidence, and invariants as required by the profile.  
  Source: `GC-GIR §5-6; GC-Transition §1`
- **`GC-AUT-005`** — Authority assertions SHALL be bound to authority provenance.  
  Source: `GC-GIR §5-6; GC-Transition §1`
- **`GC-AUT-006`** — Authority provenance SHALL identify the role, office, delegation, or institutional basis from which the asserted authority derives.  
  Source: `GC-GIR §5-6; GC-Transition §1`
- **`GC-AUT-007`** — Authority provenance SHALL identify scope and validity limits where applicable.  
  Source: `GC-GIR §5-6; GC-Transition §1`
- **`GC-AUT-008`** — Authority provenance SHALL represent revocation or supersession status where applicable.  
  Source: `GC-GIR §5-6; GC-Transition §1`
- **`GC-AUT-009`** — A revoked or expired authority SHALL NOT satisfy a current authorization condition.  
  Source: `GC-GIR §5-6; GC-Transition §1`
- **`GC-AUT-010`** — An authorization decision SHALL NOT silently broaden the Permitted Action Set.  
  Source: `GC-GIR §5-6; GC-Transition §1`
## REG

- **`GC-REG-001`** — Each Governance-Defined Action Region SHALL have stable identity and version.  
  Source: `GC-Transition §§2-3`
- **`GC-REG-002`** — Each region SHALL define membership or predicate semantics sufficient for deterministic applicability within the declared profile.  
  Source: `GC-Transition §§2-3`
- **`GC-REG-003`** — Region provenance SHALL identify the source/requirement basis for its governance treatment.  
  Source: `GC-Transition §§2-3`
- **`GC-REG-004`** — Region overlap MAY occur but SHALL be resolved through explicit applicability/composition semantics.  
  Source: `GC-Transition §§2-3`
- **`GC-REG-005`** — Region specificity SHALL NOT by itself authorize weakening a broader mandatory obligation.  
  Source: `GC-Transition §§2-3`
- **`GC-REG-006`** — Every covered action/context requiring transition governance SHALL resolve to treatment or an explicit unknown/indeterminate/refusal status.  
  Source: `GC-Transition §§2-3`
- **`GC-REG-007`** — Region-to-contract mapping gaps within a declared covered region SHALL be detected or explicitly classified.  
  Source: `GC-Transition §§2-3`
- **`GC-REG-008`** — Region changes SHALL trigger impact analysis of affected mappings/contracts/packages.  
  Source: `GC-Transition §§2-3`
## CTC

- **`GC-CTC-001`** — Each Complete Transition Contract SHALL contain pre-state semantics.  
  Source: `GC-Transition §4`
- **`GC-CTC-002`** — Each Complete Transition Contract SHALL contain current authorization semantics.  
  Source: `GC-Transition §4`
- **`GC-CTC-003`** — Each Complete Transition Contract SHALL contain required pre-commit evidence semantics.  
  Source: `GC-Transition §4`
- **`GC-CTC-004`** — Each Complete Transition Contract SHALL contain target-state semantics.  
  Source: `GC-Transition §4`
- **`GC-CTC-005`** — Each Complete Transition Contract SHALL contain required post-commit evidence semantics.  
  Source: `GC-Transition §4`
- **`GC-CTC-006`** — Each Complete Transition Contract SHALL contain outcome-specific closure semantics.  
  Source: `GC-Transition §4`
- **`GC-CTC-007`** — CTC references to authority, evidence, invariants, target states, or external dependencies SHALL be resolvable within the applicable package/profile boundary.  
  Source: `GC-Transition §4`
- **`GC-CTC-008`** — CTC structural well-formedness SHALL NOT be represented as proof of satisfiability.  
  Source: `GC-Transition §4`
- **`GC-CTC-009`** — CTC satisfiability SHALL NOT be represented as proof of target-state or closure reachability.  
  Source: `GC-Transition §4`
- **`GC-CTC-010`** — Mandatory pre-commit evidence SHALL remain mandatory through composition absent an explicitly authorized substitution/override.  
  Source: `GC-Transition §4`
- **`GC-CTC-011`** — CTC changes SHALL preserve source and version provenance.  
  Source: `GC-Transition §4`
- **`GC-CTC-012`** — Human judgment points within a CTC SHALL identify the authority responsible for that judgment or escalation.  
  Source: `GC-Transition §4`
## CMP

- **`GC-CMP-001`** — Composition SHALL be defined per CTC component rather than by one undifferentiated combining rule.  
  Source: `GC-Transition §5`
- **`GC-CMP-002`** — Each profile using composition SHALL define permitted composition operators and conflict behavior.  
  Source: `GC-Transition §5`
- **`GC-CMP-003`** — Composition SHALL NOT silently discard a mandatory obligation.  
  Source: `GC-Transition §5`
- **`GC-CMP-004`** — Any weakening, substitution, exception, waiver, or override of a mandatory obligation SHALL be explicitly modeled and authorized.  
  Source: `GC-Transition §5`
- **`GC-CMP-005`** — An authorized non-monotonic rule SHALL identify affected obligation, scope, conditions, provenance, and authorizing authority.  
  Source: `GC-Transition §5`
- **`GC-CMP-006`** — File order, rule order, last-write-wins behavior, or specificity alone SHALL NOT constitute authority to weaken governance.  
  Source: `GC-Transition §5`
- **`GC-CMP-007`** — Composition conflicts that cannot be resolved under declared rules SHALL produce an explicit indeterminate/refusal/escalation result.  
  Source: `GC-Transition §5`
- **`GC-CMP-008`** — Composition results SHOULD be reproducible under a declared canonicalization/equivalence criterion.  
  Source: `GC-Transition §5`
## EVD

- **`GC-EVD-001`** — Required evidence SHALL be typed or otherwise semantically identifiable.  
  Source: `GC-GIR §9; GC-Security §2`
- **`GC-EVD-002`** — Required evidence SHALL identify subject or target binding where material.  
  Source: `GC-GIR §9; GC-Security §2`
- **`GC-EVD-003`** — Required evidence SHALL identify freshness/validity conditions where material.  
  Source: `GC-GIR §9; GC-Security §2`
- **`GC-EVD-004`** — Required evidence SHALL identify admissible producing source/interface where the profile depends on source qualification.  
  Source: `GC-GIR §9; GC-Security §2`
- **`GC-EVD-005`** — Replay-sensitive evidence SHALL define anti-replay requirements.  
  Source: `GC-GIR §9; GC-Security §2`
- **`GC-EVD-006`** — An authenticated evidence object SHALL NOT be treated as necessarily true evidence content.  
  Source: `GC-GIR §9; GC-Security §2`
- **`GC-EVD-007`** — Evidence profiles SHOULD identify independence or corroboration requirements where material.  
  Source: `GC-GIR §9; GC-Security §2`
- **`GC-EVD-008`** — Evidence profiles SHOULD identify compromise/revocation assumptions for evidence sources.  
  Source: `GC-GIR §9; GC-Security §2`
- **`GC-EVD-009`** — Missing mandatory evidence SHALL NOT silently satisfy an authorization, target-state, or closure condition.  
  Source: `GC-GIR §9; GC-Security §2`
- **`GC-EVD-010`** — Evidence used for closure SHALL remain linked to the outcome/target to which it applies.  
  Source: `GC-GIR §9; GC-Security §2`
## PRJ

- **`GC-PRJ-001`** — A target projection SHALL preserve authority boundaries from the approved canonical model.  
  Source: `GC-Core §9`
- **`GC-PRJ-002`** — A target projection SHALL NOT grant authority outside the canonical Permitted Action Set.  
  Source: `GC-Core §9`
- **`GC-PRJ-003`** — A target projection SHALL preserve mandatory authorization conditions applicable to projected actions.  
  Source: `GC-Core §9`
- **`GC-PRJ-004`** — A target projection SHALL preserve mandatory invariant obligations.  
  Source: `GC-Core §9`
- **`GC-PRJ-005`** — A target projection SHALL preserve mandatory evidence obligations.  
  Source: `GC-Core §9`
- **`GC-PRJ-006`** — A target projection SHALL NOT claim closure under conditions weaker than the canonical closure semantics.  
  Source: `GC-Core §9`
- **`GC-PRJ-007`** — Projection limitations or unsupported semantics SHALL be declared rather than silently omitted.  
  Source: `GC-Core §9`
- **`GC-PRJ-008`** — A consumer that cannot represent a mandatory semantic feature SHALL refuse compatibility or require an explicitly approved profile transformation.  
  Source: `GC-Core §9`
## PKG

- **`GC-PKG-001`** — Each compiled governance package SHALL have stable immutable identity and version.  
  Source: `GC-Package §§1-3`
- **`GC-PKG-002`** — Each package SHALL include integrity metadata sufficient to bind lifecycle records to exact content.  
  Source: `GC-Package §§1-3`
- **`GC-PKG-003`** — Each package manifest SHALL identify the canonical model identity/version/digest.  
  Source: `GC-Package §§1-3`
- **`GC-PKG-004`** — Each package manifest SHALL identify the source-baseline identity.  
  Source: `GC-Package §§1-3`
- **`GC-PKG-005`** — Each package manifest SHALL identify compiler/version/configuration identity sufficient for the profile.  
  Source: `GC-Package §§1-3`
- **`GC-PKG-006`** — Each package manifest SHALL identify the target/runtime profile.  
  Source: `GC-Package §§1-3`
- **`GC-PKG-007`** — Each package manifest SHALL include an artifact inventory with integrity identifiers.  
  Source: `GC-Package §§1-3`
- **`GC-PKG-008`** — Each package manifest SHALL identify declared scope and invariant profile.  
  Source: `GC-Package §§1-3`
- **`GC-PKG-009`** — Each package manifest SHALL identify known exclusions, limitations, and unresolved build-time assumptions.  
  Source: `GC-Package §§1-3`
- **`GC-PKG-010`** — Mutable validation/approval/activation status SHOULD be represented in detached records bound to the immutable package identity.  
  Source: `GC-Package §§1-3`
- **`GC-PKG-011`** — Package validation SHALL be performed separately from canonical-model verification.  
  Source: `GC-Package §§1-3`
- **`GC-PKG-012`** — A package SHALL NOT be considered authoritatively issued solely because it is structurally valid or executable.  
  Source: `GC-Package §§1-3`
## ACT

- **`GC-ACT-001`** — Authoritative issuance SHALL be attributable to an authorized actor or process.  
  Source: `GC-Package §§3-7`
- **`GC-ACT-002`** — Activation SHALL be represented as a lifecycle transition distinct from issuance.  
  Source: `GC-Package §§3-7`
- **`GC-ACT-003`** — Activation SHALL verify exact package identity and integrity.  
  Source: `GC-Package §§3-7`
- **`GC-ACT-004`** — Activation SHALL verify applicable issuance/approval status.  
  Source: `GC-Package §§3-7`
- **`GC-ACT-005`** — Activation SHALL verify non-revoked/non-suspended lifecycle status.  
  Source: `GC-Package §§3-7`
- **`GC-ACT-006`** — Activation SHALL verify compatibility with required runtime/profile semantics.  
  Source: `GC-Package §§3-7`
- **`GC-ACT-007`** — Activation SHALL bind the package to a defined runtime scope.  
  Source: `GC-Package §§3-7`
- **`GC-ACT-008`** — Activation SHALL enforce effective/expiration timing when applicable.  
  Source: `GC-Package §§3-7`
- **`GC-ACT-009`** — Failure of a mandatory activation precondition SHALL cause structural refusal or a defined non-active status.  
  Source: `GC-Package §§3-7`
- **`GC-ACT-010`** — Supersession, suspension, revocation, and rollback SHALL be distinguishable lifecycle states/actions.  
  Source: `GC-Package §§3-7`
## RT

- **`GC-RT-001`** — A runtime consumer SHALL identify the active package/version used for a governance decision.  
  Source: `GC-Package §5-6; GC-Transition §6-8`
- **`GC-RT-002`** — A runtime consumer SHALL verify compatibility with mandatory semantics and extensions.  
  Source: `GC-Package §5-6; GC-Transition §6-8`
- **`GC-RT-003`** — A runtime consumer SHALL obtain required current authority, evidence, and state.  
  Source: `GC-Package §5-6; GC-Transition §6-8`
- **`GC-RT-004`** — A runtime consumer SHALL preserve scope, tenant, and jurisdiction boundaries represented by the active package/profile.  
  Source: `GC-Package §5-6; GC-Transition §6-8`
- **`GC-RT-005`** — A runtime consumer SHALL apply defined missing-information and indeterminate-result behavior.  
  Source: `GC-Package §5-6; GC-Transition §6-8`
- **`GC-RT-006`** — A runtime consumer SHALL bind a decision to the exact proposal/action and target evaluated.  
  Source: `GC-Package §5-6; GC-Transition §6-8`
- **`GC-RT-007`** — A runtime consumer SHALL preserve refusal, escalation, and hold semantics.  
  Source: `GC-Package §5-6; GC-Transition §6-8`
- **`GC-RT-008`** — Where eligibility can become stale before commitment, the runtime profile SHALL require commitment-boundary revalidation or equivalent atomic/fenced protection.  
  Source: `GC-Package §5-6; GC-Transition §6-8`
- **`GC-RT-009`** — Runtime authorization at evaluation time SHALL NOT be presumed valid at commitment when a relevant condition has changed.  
  Source: `GC-Package §5-6; GC-Transition §6-8`
- **`GC-RT-010`** — Runtime evidence SHOULD bind decision time and commitment time where distinct.  
  Source: `GC-Package §5-6; GC-Transition §6-8`
- **`GC-RT-011`** — A runtime allow/permit decision SHALL NOT be treated as proof that the target state was achieved.  
  Source: `GC-Package §5-6; GC-Transition §6-8`
- **`GC-RT-012`** — A runtime receipt SHALL NOT by itself establish deployment non-bypassability.  
  Source: `GC-Package §5-6; GC-Transition §6-8`
## CLO

- **`GC-CLO-001`** — Target-state verification SHALL evaluate the applicable target-state semantics using qualified observation/evidence.  
  Source: `GC-Transition §§7-9`
- **`GC-CLO-002`** — Successful request dispatch or API response SHALL NOT automatically satisfy target-state semantics unless the governance explicitly defines it as sufficient.  
  Source: `GC-Transition §§7-9`
- **`GC-CLO-003`** — Closure SHALL be outcome-specific where terminal outcomes have different obligations.  
  Source: `GC-Transition §§7-9`
- **`GC-CLO-004`** — Successful closure SHALL require satisfaction of applicable authorization and closure conditions.  
  Source: `GC-Transition §§7-9`
- **`GC-CLO-005`** — Successful execution SHALL NOT be treated as governance closure without required closure evidence.  
  Source: `GC-Transition §§7-9`
- **`GC-CLO-006`** — Closure safety SHALL be paired with reachability/nonvacuity analysis when the profile makes a meaningful success claim.  
  Source: `GC-Transition §§7-9`
- **`GC-CLO-007`** — Probabilistic evidence SHALL be governed by explicit deterministic decision/escalation semantics.  
  Source: `GC-Transition §§7-9`
- **`GC-CLO-008`** — Closure evidence SHALL remain reconstructibly linked to the governed transition and outcome.  
  Source: `GC-Transition §§7-9`
## SEC

- **`GC-SEC-001`** — A security claim SHALL state material trust assumptions within its declared scope.  
  Source: `GC-Security`
- **`GC-SEC-002`** — Cryptographic authenticity SHALL NOT be generalized to truth, correctness, independence, freshness, or target binding without separate evidence.  
  Source: `GC-Security`
- **`GC-SEC-003`** — A profile relying on signed artifacts SHALL identify signing authority, key custody, trust anchors, verification policy, rotation/expiry, compromise response, and revocation.  
  Source: `GC-Security`
- **`GC-SEC-004`** — A package requirement for non-bypassable enforcement SHALL NOT be represented as deployment evidence of non-bypassability.  
  Source: `GC-Security`
- **`GC-SEC-005`** — A deployment non-bypassability claim SHALL identify the consequence-producing boundary assessed.  
  Source: `GC-Security`
- **`GC-SEC-006`** — A deployment non-bypassability claim SHALL include evidence addressing alternate privileged, administrative, maintenance, or direct target paths where material.  
  Source: `GC-Security`
- **`GC-SEC-007`** — A deployment non-bypassability claim SHALL identify configuration/topology/identity/dependency changes that invalidate the claim.  
  Source: `GC-Security`
- **`GC-SEC-008`** — Missing, stale, revoked, unverifiable, or incompatible mandatory security evidence SHALL NOT silently default to authorization.  
  Source: `GC-Security`
## CNF

- **`GC-CNF-001`** — A conformance claim SHALL identify the specification and exact version.  
  Source: `GC-Conformance`
- **`GC-CNF-002`** — A conformance claim SHALL identify the conformance object.  
  Source: `GC-Conformance`
- **`GC-CNF-003`** — A conformance claim SHALL identify applicable profiles.  
  Source: `GC-Conformance`
- **`GC-CNF-004`** — A conformance claim SHALL identify the bounded scope/domain/jurisdiction covered.  
  Source: `GC-Conformance`
- **`GC-CNF-005`** — A conformance claim SHALL identify the evidence/assurance basis.  
  Source: `GC-Conformance`
- **`GC-CNF-006`** — A conformance claim SHALL identify exclusions and known limitations.  
  Source: `GC-Conformance`
- **`GC-CNF-007`** — A conformance claim SHALL identify effective period or validity conditions where applicable.  
  Source: `GC-Conformance`
- **`GC-CNF-008`** — A conformance claim SHALL identify unresolved findings or compensating controls where material.  
  Source: `GC-Conformance`
- **`GC-CNF-009`** — Partial conformance SHALL NOT be presented as full-lifecycle conformance.  
  Source: `GC-Conformance`
- **`GC-CNF-010`** — Conditional conformance SHALL identify the external condition/dependency and invalidation trigger.  
  Source: `GC-Conformance`
- **`GC-CNF-011`** — Conformance of one object SHALL NOT be represented as conformance of unrelated lifecycle objects.  
  Source: `GC-Conformance`
- **`GC-CNF-012`** — Conformance SHALL NOT be represented as a general legal opinion or guarantee of lawful, ethical, safe, or correct outcomes.  
  Source: `GC-Conformance`
## PRO

- **`GC-PRO-001`** — Each profile SHALL have stable identity, version, and status.  
  Source: `GC-Profile-Model`
- **`GC-PRO-002`** — Each profile SHALL identify supported specification version(s).  
  Source: `GC-Profile-Model`
- **`GC-PRO-003`** — Each profile SHALL declare applicability/scope and required core capabilities.  
  Source: `GC-Profile-Model`
- **`GC-PRO-004`** — Each profile SHALL identify added normative requirements and mandatory extensions.  
  Source: `GC-Profile-Model`
- **`GC-PRO-005`** — A profile SHALL NOT silently redefine a core term.  
  Source: `GC-Profile-Model`
- **`GC-PRO-006`** — A profile SHALL NOT weaken a core mandatory requirement unless the core explicitly defines that requirement as profile-variable.  
  Source: `GC-Profile-Model`
- **`GC-PRO-007`** — An unknown mandatory extension that can affect authority, evidence, composition, target state, or closure SHALL cause incompatibility/refusal rather than silent ignore.  
  Source: `GC-Profile-Model`
- **`GC-PRO-008`** — A rights-affecting profile SHOULD define contestability/redress semantics where required by the governing institution or law.  
  Source: `GC-Profile-Model`
- **`GC-PRO-009`** — A distributed-transition profile SHALL identify atomicity, compensation, partial-commit, recovery-authority, and composite-closure semantics that it claims to support.  
  Source: `GC-Profile-Model`
- **`GC-PRO-010`** — The v0.1 distributed-transition profile SHALL be represented as experimental rather than as a solved core property.  
  Source: `GC-Profile-Model`
## QUAL

- **`GC-QUAL-001`** — A compiler-qualification claim SHALL identify the actual human/software/AI-assisted/organizational capability being relied upon.  
  Source: `GC-Compiler-Qualification`
- **`GC-QUAL-002`** — A qualification claim SHALL identify the intended-use scope for which the capability is qualified.  
  Source: `GC-Compiler-Qualification`
- **`GC-QUAL-003`** — A qualification claim SHALL identify supported specification/profile versions and target projection classes.  
  Source: `GC-Compiler-Qualification`
- **`GC-QUAL-004`** — Qualification evidence SHOULD address semantic fidelity, traceability, diagnostics, provenance, reproducibility/equivalence, configuration control, security, and negative testing proportionate to intended use.  
  Source: `GC-Compiler-Qualification`
- **`GC-QUAL-005`** — Compiler qualification SHALL NOT be represented as package-specific validation.  
  Source: `GC-Compiler-Qualification`
- **`GC-QUAL-006`** — Package validation SHALL NOT be represented as proof that the compiler capability is generally qualified.  
  Source: `GC-Compiler-Qualification`
- **`GC-QUAL-007`** — AI-assisted compilation SHALL identify the role delegated to the probabilistic component and the control by which its output becomes authoritative.  
  Source: `GC-Compiler-Qualification`
- **`GC-QUAL-008`** — AI-generated interpretation SHALL NOT become authoritative solely because it was generated by an AI system.  
  Source: `GC-Compiler-Qualification`
- **`GC-QUAL-009`** — Where byte-identical reproducibility is not required or possible, the qualification profile SHALL define the equivalence criterion actually claimed.  
  Source: `GC-Compiler-Qualification`
- **`GC-QUAL-010`** — A qualification evidence package SHOULD identify dependencies and configuration baseline material to the claim.  
  Source: `GC-Compiler-Qualification`
- **`GC-QUAL-011`** — Material changes to compiler semantics, AI model/provider/configuration, dependencies, adapters, or build/security environment SHALL be assessed for requalification impact.  
  Source: `GC-Compiler-Qualification`
- **`GC-QUAL-012`** — A material change SHALL invalidate affected qualification claims until re-established.  
  Source: `GC-Compiler-Qualification`
## ASR

- **`GC-ASR-001`** — An assurance record SHALL identify the claim supported by each material evidence item.  
  Source: `GC-Evidence-and-Assurance`
- **`GC-ASR-002`** — Evidence for one claim SHALL NOT silently substitute for evidence of a different claim.  
  Source: `GC-Evidence-and-Assurance`
- **`GC-ASR-003`** — Authenticated evidence SHALL NOT be treated as necessarily truthful/correct evidence content.  
  Source: `GC-Evidence-and-Assurance`
- **`GC-ASR-004`** — A profile depending on evidence accuracy SHALL identify the observation/source-qualification/corroboration assumptions supporting that claim.  
  Source: `GC-Evidence-and-Assurance`
- **`GC-ASR-005`** — Assurance results SHOULD identify their evidence level or method.  
  Source: `GC-Evidence-and-Assurance`
- **`GC-ASR-006`** — A bounded executable check SHALL NOT be described as machine-checked universal proof.  
  Source: `GC-Evidence-and-Assurance`
- **`GC-ASR-007`** — An implementation-conformance result SHALL NOT be described as empirical effectiveness without operational evidence.  
  Source: `GC-Evidence-and-Assurance`
- **`GC-ASR-008`** — Property results SHOULD distinguish satisfied, unsatisfied, indeterminate, not applicable, and not evaluated statuses where relevant.  
  Source: `GC-Evidence-and-Assurance`
- **`GC-ASR-009`** — A solver/tool result SHALL NOT automatically determine institutional package disposition unless the profile assigns that authority.  
  Source: `GC-Evidence-and-Assurance`
- **`GC-ASR-010`** — Higher-consequence assurance cases SHOULD link claims, arguments, evidence, assumptions/context, and limitations.  
  Source: `GC-Evidence-and-Assurance`
- **`GC-ASR-011`** — Continuing-assurance profiles SHOULD identify source/authority/evidence/deployment changes that invalidate prior claims.  
  Source: `GC-Evidence-and-Assurance`
- **`GC-ASR-012`** — An independence claim SHOULD identify material organizational, financial, technical, and evidence-access relationships.  
  Source: `GC-Evidence-and-Assurance`
## OPS

- **`GC-OPS-001`** — An operating-protocol conformance claim SHALL identify which semantic operations it supports.  
  Source: `GC-Operating-Protocol`
- **`GC-OPS-002`** — Logical producer, repository, validator, issuance, activation, runtime-consumer, and evidence/status responsibilities SHALL remain distinguishable even when implemented by combined components.  
  Source: `GC-Operating-Protocol`
- **`GC-OPS-003`** — Before active consumption, exact package identity/integrity SHALL be verified.  
  Source: `GC-Operating-Protocol`
- **`GC-OPS-004`** — Before active consumption, supported specification/profile semantics SHALL be verified.  
  Source: `GC-Operating-Protocol`
- **`GC-OPS-005`** — Before active consumption, authoritative issuance status SHALL be verified.  
  Source: `GC-Operating-Protocol`
- **`GC-OPS-006`** — Before active consumption, revoked/suspended status SHALL be evaluated.  
  Source: `GC-Operating-Protocol`
- **`GC-OPS-007`** — Before active consumption, scope/target applicability SHALL be evaluated.  
  Source: `GC-Operating-Protocol`
- **`GC-OPS-008`** — Before active consumption, effective/expiration timing SHALL be evaluated where applicable.  
  Source: `GC-Operating-Protocol`
- **`GC-OPS-009`** — Unknown mandatory extensions SHALL cause incompatibility/refusal rather than permissive fallback.  
  Source: `GC-Operating-Protocol`
- **`GC-OPS-010`** — Integrity mismatch, missing issuance, lifecycle invalidity, scope mismatch, or equivalent mandatory failure SHALL NOT silently select a permissive fallback.  
  Source: `GC-Operating-Protocol`
- **`GC-OPS-011`** — A consumer caching lifecycle or authority state SHALL define freshness/consistency behavior appropriate to the profile.  
  Source: `GC-Operating-Protocol`
- **`GC-OPS-012`** — A stale cache SHALL NOT authorize commitment after a material revocation/change when the profile requires current state.  
  Source: `GC-Operating-Protocol`
- **`GC-OPS-013`** — An interoperability result SHOULD identify producer/consumer versions, profile versions, package identity, operations/vectors exercised, results, deviations, and limitations.  
  Source: `GC-Operating-Protocol`

## Identifier policy

Published identifiers are never reused for a different semantic obligation. Withdrawn requirements remain reserved and are marked superseded/withdrawn in a future release.
