# GC-Operating-Protocol — Package Exchange and Lifecycle Interoperability

**Status:** Normative protocol model, v0.1.0

## 1. Purpose

The operating protocol defines semantic operations among a package producer, repository, validator/assessor, issuance authority, activation authority, and runtime consumer. It does not mandate HTTP, REST, message queues, filesystem distribution, or another transport.

## 2. Protocol actors

A deployment MAY combine actors physically, but conformance evidence MUST preserve their logical responsibilities and authorities.

- **Producer** — emits candidate packages and manifests.
- **Repository** — stores immutable packages and lifecycle records.
- **Validator/Assessor** — evaluates a model/package/implementation under a declared profile.
- **Issuance Authority** — decides whether a validated package becomes authoritatively issued.
- **Activation Authority/Mechanism** — binds an issued package to a runtime scope.
- **Runtime Consumer** — evaluates governed proposals/actions using an active package.
- **Evidence/Status Source** — provides current authority, evidence, lifecycle, or target observations.

## 3. Semantic operations

Implementations claiming operating-protocol conformance MUST provide semantic equivalents for the operations they claim to support:

- `PublishCandidatePackage`
- `FetchPackage`
- `VerifyPackageIdentityIntegrity`
- `RecordValidationAttestation`
- `IssuePackage`
- `QueryPackageStatus`
- `ActivatePackage`
- `SuspendPackage`
- `RevokePackage`
- `SupersedePackage`
- `RollbackActivation`
- `ResolveActivePackage`
- `RecordRuntimeDecision`
- `RecordTargetVerification`
- `RecordClosure`

Transport-specific names MAY differ.

## 4. Required verification before consumption

Before treating a package as active governance, a consumer/activation mechanism MUST establish, according to profile:

1. exact package identity/integrity;
2. supported specification/profile semantics;
3. authoritative issuance status;
4. non-revoked/non-suspended status;
5. scope/target applicability;
6. effective/expiration time;
7. mandatory extension compatibility; and
8. required activation record/status.

A successful parse is not sufficient.

## 5. Protocol failure semantics

The operating profile MUST define behavior for at least:

- unknown package;
- digest/integrity mismatch;
- unsupported specification/profile;
- unknown mandatory extension;
- missing issuance/approval;
- revoked/suspended/superseded package;
- expired/not-yet-effective package;
- scope mismatch;
- stale lifecycle cache;
- unavailable status/evidence source;
- conflicting lifecycle records; and
- attempted downgrade to a weaker profile/version.

Mandatory failure conditions MUST result in refusal, indeterminate, or escalation semantics; they MUST NOT silently select a permissive fallback.

## 6. Status consistency and freshness

A consumer that caches lifecycle or authority state MUST define a freshness/consistency policy appropriate to the consequence class. A stale cache MUST NOT authorize commitment after a revocation or material lifecycle change where the profile requires current state.

## 7. Interoperability evidence

An interoperability result SHOULD record:

- producer and consumer versions;
- specification/profile versions;
- package identity;
- transport/protocol mapping;
- mandatory semantics exercised;
- positive/negative vectors;
- lifecycle changes tested;
- decision/target/closure observations;
- deviations and limitations.
