# GC-Core — Governance Compilation Core Specification

**Status:** Normative, v0.1.0  
**Conformance class:** Core lifecycle and semantic requirements

## 1. Scope

GC-Core specifies the minimum technology-neutral semantics and lifecycle controls for transforming authorized human governance into bounded machine-evaluable governance artifacts and for preserving the relevant governance meaning through issuance, activation, runtime consumption, consequence verification, and closure.

It does not prescribe a programming language, solver, policy engine, ontology product, cloud platform, runtime control plane, or organizational structure.

## 2. Normative boundary

A conforming Core implementation SHALL preserve identifiable responsibility for:

1. governance-source qualification;
2. declared compilation scope;
3. interpretation and normalized requirements;
4. bidirectional traceability;
5. canonical governance modeling;
6. authority-bounded action semantics;
7. region and transition-contract semantics where the transition-governance profile is used;
8. model verification/analysis;
9. controlled transformation/projection;
10. package construction and post-compilation validation;
11. authoritative issuance;
12. activation and lifecycle state;
13. runtime-consumer compatibility;
14. commitment-boundary obligations;
15. target-state verification and closure where required; and
16. change/revalidation/invalidation.

These responsibilities MAY be implemented by combined components, but their inputs, outputs, decisions, authorities, and evidence SHALL remain distinguishable.

## 3. Authorized source baseline

An implementation MUST establish an identifiable source baseline before making a scoped completeness or compilation claim. Each material source MUST have identity, version/status, issuing authority, applicability information, provenance, and effective/supersession status sufficient for the declared profile.

A source's inclusion in an authorized baseline MUST NOT be represented as establishing legal or normative correctness beyond the authority determination actually made.

Unknown, disputed, excluded, or unavailable sources that materially limit a claim MUST be represented as scope limitations rather than silently treated as absent obligations.

## 4. Declared compilation scope

Each compilation MUST declare the boundary to which its requirements, analysis, completeness, package, and conformance claims apply. The scope SHALL identify, as applicable, source universe, jurisdictions, organizations/tenants, domains, actors and authority relations, governed actions/targets, lifecycle state, effective period, invariants, assumptions, threat/failure model, exclusions, and known limitations.

Unqualified completeness claims MUST NOT be made when the applicable boundary is not declared.

## 5. Interpretation and requirements

Material interpretation choices that affect machine behavior, authority, evidence, exceptions, applicability, timing, or closure MUST be attributable to an authorized decision process.

Where source text is irreducibly ambiguous or open-textured, the compilation process MUST NOT silently invent determinacy. It SHALL use an authorized interpretation, preserve bounded discretion/judgment, narrow the applicable scope, represent an indeterminate/escalation path, or refuse authoritative generation.

Requirements MUST remain traceable to source and interpretation provenance.

## 6. Canonical governance model

The canonical model MUST represent enough semantics to distinguish at least:

- sources and requirements;
- scope and applicability;
- actors and authority provenance;
- actions and targets;
- the authority-bounded permitted action space;
- conditions for current authorization;
- required evidence and trust conditions;
- system/constitutional invariants;
- decision/failure semantics;
- temporal and lifecycle conditions;
- target-state obligations where applicable;
- closure obligations where applicable; and
- assumptions, limitations, profiles, and extensions.

The GIR defined in `GC-GIR.md` is the v0.1 canonical interchange representation for these semantics.

## 7. Authority boundary

A conforming model MUST preserve the separation:

```text
Capability_m(a,c) does not imply InPermittedActionSet(a,c)
```

An action outside the active Permitted Action Set MUST NOT become authorized solely because an agent, user, model, workflow, or runtime component can formulate or execute it.

Membership in the Permitted Action Set establishes only potential eligibility. Current authorization MUST be evaluated under the applicable authority, context, evidence, state, time, and invariant conditions.

## 8. Pre-compilation and post-compilation validation

The approved canonical model MUST be evaluated separately from the generated package. A valid source model does not establish correct transformation, packaging, or projection; a correctly generated package does not establish that its source governance is substantively correct.

The applicable profile SHALL specify the required analyses and acceptable result statuses.

## 9. Transformation and projection

A compiler/projection MUST preserve the normative meaning declared by the canonical model within the target profile.

No target artifact MAY grant authority outside the approved canonical authority space.

No target artifact MAY weaken a mandatory authorization, invariant, evidence, target-state, or closure condition unless an explicitly modeled and authorized non-monotonic rule permits that effect.

Transformation provenance MUST bind the target artifact/package to the source model, compiler capability/version/configuration, target profile, and relevant dependencies.

## 10. Package, issuance, and activation

A package MUST have immutable identity and integrity information. Package validation, authoritative issuance, and activation MUST be represented as distinct lifecycle judgments.

A package MUST NOT become active merely because it exists, parses successfully, or has been stored in a repository.

Activation MUST bind an authoritatively issued package to a defined scope and MUST structurally refuse activation when a mandatory activation condition is unsatisfied.

## 11. Runtime consumption

A conforming runtime consumer MUST verify the package/version/profile it is using, obtain the current inputs required by the active governance semantics, preserve refusal/indeterminate behavior, and bind a decision to the proposal/action and target actually evaluated.

Where current authority, evidence, state, or other eligibility conditions can change between evaluation and commitment, the applicable runtime profile MUST define commitment-boundary revalidation or an equivalent atomic/fenced mechanism that prevents stale eligibility from authorizing a changed consequence.

## 12. Consequence and closure

If the profile defines target-state or closure requirements, a runtime allow/permit result MUST NOT be treated as evidence that the required target state was reached.

Successful execution MUST NOT be treated as governance closure unless the applicable closure conditions and required evidence are satisfied.

Closure semantics MUST be outcome-specific where success, compensated, cancelled, refused, failed, expired, or other terminal outcomes have different evidentiary obligations.

## 13. Change and invalidation

Material changes to sources, interpretations, authority, invariants, model semantics, compiler/toolchain, projection, profile, package, runtime interfaces, or evidence-source assumptions MUST be evaluated for impact. Affected validation/approval/conformance claims MUST be invalidated or re-established as required by the applicable profile.

## 14. Claim limits

Core conformance is a claim about the specified process/artifact/interface under a declared scope. It MUST NOT be represented as proving:

- legal compliance;
- ethical legitimacy;
- correctness of the originating governance;
- safety of all governed behavior;
- truth of all authenticated evidence;
- non-bypassability of a deployment absent deployment evidence; or
- universal correctness outside the tested/proved scope.

## 15. Normative requirement catalog

The individually traceable normative statements are indexed in `requirements/GC-Normative-Requirements.csv`. In a conflict between an identifier's catalog summary and the detailed normative specification, the detailed specification text controls for v0.1.0 and the discrepancy SHALL be treated as a specification defect.
