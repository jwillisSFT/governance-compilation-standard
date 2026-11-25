# GC-Package-and-Lifecycle — Package, Issuance, Activation, Runtime Consumption, and Change

**Status:** Normative, v0.1.0

## 1. Immutable package identity

A Compiled Governance Package MUST have stable identity/version and integrity metadata sufficient to bind validation, issuance, activation, revocation, supersession, and runtime evidence to the exact package content.

Mutable lifecycle facts SHOULD be represented in detached attestations/records that reference the immutable package identity rather than modifying the already approved package.

## 2. Package manifest

The manifest MUST identify or reference:

- specification/profile version;
- package ID/version;
- canonical model ID/version/digest;
- source-baseline identity;
- compiler identity/version/configuration identity;
- target/runtime profile;
- artifact inventory and digests;
- dependency versions where material;
- declared scope;
- invariant profile;
- known exclusions/limitations; and
- unresolved build-time assumptions.

Validation, approval, issuance, activation, revocation, and supersession records MAY be detached but MUST be cryptographically or structurally bound to the exact package identity according to the applicable profile.

## 3. Validation and issuance

Post-compilation validation MUST evaluate the generated package against the approved canonical model and target profile. Validation evidence MUST identify scope, methods, results, limitations, and unresolved findings.

Authoritative issuance MUST be performed by an actor/process whose authority is represented and MUST NOT be inferred merely from successful validation.

## 4. Activation

Activation MUST verify, as applicable:

- exact package identity/integrity;
- authoritative issuance/approval;
- non-revoked status;
- runtime/profile compatibility;
- target/scope binding;
- effective/expiration time;
- required residual-risk acceptance;
- required rollback/supersession relation; and
- mandatory activation evidence.

Failure of a mandatory activation condition MUST cause structural refusal or a profile-defined non-active status.

## 5. Runtime consumer contract

A conforming runtime consumer MUST:

1. identify the active package/version used for a decision;
2. verify compatibility with mandatory semantics/extensions;
3. obtain required current authority/evidence/state;
4. preserve scope/tenant/jurisdiction boundaries;
5. apply defined missing/indeterminate behavior;
6. bind the decision to the exact action/proposal/target evaluated;
7. perform required commitment-boundary revalidation or equivalent atomic protection;
8. preserve refusal/escalation/hold semantics;
9. generate required decision/commit evidence; and
10. expose enough provenance to reconstruct the applicable governance decision within the declared profile.

## 6. Runtime evidence

A runtime decision/receipt profile SHOULD bind:

- proposal/action identity;
- target identity;
- active package/version;
- applicable governance version;
- structured decision and obligations;
- authority/evidence references;
- canonical state/version reference;
- decision time and commit time;
- enforcement result;
- target-state result where available; and
- closure state/evidence where applicable.

A receipt is evidence about the represented event; it is not by itself proof that every bypass route was prevented.

## 7. Supersession, suspension, revocation, rollback

Lifecycle records MUST distinguish supersession, suspension, revocation, and rollback because they have different semantics. Runtime consumers MUST apply the active lifecycle state rather than assuming that the newest package found is authoritative.

## 8. Change impact

Material change MUST trigger impact analysis. The implementation SHALL identify which models, packages, proofs/analyses, approvals, activations, conformance claims, and runtime dependencies are invalidated or require re-establishment.
