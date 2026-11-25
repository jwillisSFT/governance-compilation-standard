# GC-Security — Security and Trust-Boundary Requirements

**Status:** Normative for security claims, v0.1.0

## 1. Threat model

Governance Compilation assumes that errors or attacks can occur in sources, interpretation, modeling, compiler/toolchain, package storage, activation, runtime state/evidence, and enforcement. Strong downstream enforcement can make upstream defects more consistently consequential; it does not remove the need for upstream assurance.

A security claim SHOULD state assumptions about at least:

- source authenticity/integrity;
- authority and delegation integrity;
- compiler/toolchain integrity;
- repository/package integrity;
- activation authority;
- runtime identity and state;
- evidence-source trust;
- enforcement-route coverage;
- administrative/maintenance paths;
- tenant/domain isolation; and
- dependency compromise.

## 2. Evidence trust

Cryptographic authenticity proves only the applicable authenticity/integrity claim. It MUST NOT be generalized to truth, correctness, independence, freshness, or target binding unless those properties are separately established.

Evidence-source profiles SHOULD address qualification, independence, protected observation, freshness, anti-replay, target binding, corroboration, compromise assumptions, and revocation.

## 3. Package protection

Profiles that claim package authenticity/integrity MUST define the protection and verification mechanisms and their trust assumptions. Signing MUST bind the exact package identity/content and SHOULD bind relevant profile/version metadata.

## 4. Non-bypassability

A package MAY require non-bypassable governance, but:

```text
PackageRequiresNonBypass does not imply DeploymentDemonstratesNonBypass
```

A deployment non-bypassability claim MUST be supported by evidence appropriate to the declared consequence-producing boundary. Relevant evidence MAY include route/interface inventory, credential/service-identity analysis, privileged/administrative paths, network/OS/orchestration/target enforcement configuration, alternate APIs/storage/database paths, emergency/maintenance interfaces, negative/adversarial tests, and target-side observation.

The claim MUST identify configuration/topology/identity/dependency changes that invalidate the evidence.

## 5. Fail behavior

Missing, stale, revoked, unverifiable, incompatible, or indeterminate mandatory security/authority evidence MUST result in the profile-defined safe failure behavior. The default MUST NOT silently become authorization.

## 6. Supply-chain separation

A valid package does not establish a qualified compiler; a qualified compiler does not establish a valid package; either one alone does not establish secure activation or runtime enforcement. Conformance claims MUST identify which object was assessed.
