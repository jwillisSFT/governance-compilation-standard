# GC-Profile-Model — Profiles and Extensions

**Status:** Normative profile framework, v0.1.0

## 1. Purpose

The core specification defines shared semantics without forcing every domain or consequence class to use identical assurance mechanisms. Profiles specialize the core while preserving its non-negotiable semantic separations.

## 2. Profile declaration

A profile MUST declare:

- profile ID/version/status;
- specification version(s) supported;
- applicability/scope;
- required core capabilities;
- added normative requirements;
- permitted optional features;
- evidence/assurance requirements;
- runtime/consumer dependencies;
- extension namespaces;
- compatibility rules;
- invalidation conditions; and
- known limitations.

## 3. Profile safety rule

A profile MUST NOT silently redefine a core term or weaken a core mandatory requirement. Any permitted variation MUST be explicitly identified by the core specification as profile-variable or be introduced through a versioned normative change to the core.

## 4. Rights-affecting / contestability profile

Where the governed domain requires contestability or redress, the profile SHOULD specify:

- who may challenge a source, interpretation, classification, authority determination, evidence item, rule, runtime fact, or outcome;
- challenge period/conditions;
- information available for review;
- competent reconsideration/correction authority;
- stay/suspension behavior;
- propagation of a successful challenge to requirements/models/packages/activation/related decisions; and
- remediation, recompilation, compensation, or other corrective action for consequences already produced.

The profile does not create a substantive right of appeal where the governing institution/law provides none; it represents such procedures where required.

## 5. Security/high-assurance profile

A profile relying on signatures/cryptographic attestations MUST identify signing authority, key custody, trust anchors, verification policy, rotation/expiry, compromise response, and revocation. The Core does not mandate a cryptographic suite or PKI.

## 6. Distributed-transition profile

A distributed-transition profile MAY define atomicity boundaries, sub-transitions, sagas, compensation, partial commit, irreversible effects, retries, composite evidence, recovery authority, and composite closure.

This profile is **experimental in v0.1.0**. Implementers MUST NOT imply that the core CTC semantics by themselves solve arbitrary distributed-transaction correctness.

## 7. Unknown extensions

A consumer MUST reject or declare incompatibility with an unknown mandatory extension whose semantics could alter authority, evidence, target-state, composition, or closure behavior. Unknown purely informative extensions MAY be ignored if the profile permits it.
