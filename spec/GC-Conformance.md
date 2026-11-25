# GC-Conformance — Conformance Model

**Status:** Normative, v0.1.0

## 1. Conformance is bounded

A conforming implementation MUST state the object and boundary of conformance. The phrase "Governance Compilation compliant" without a conformance object/profile/scope is insufficient for v0.1.0.

## 2. Conformance objects

Supported object classes include:

- process;
- GIR;
- compiler/transformation capability;
- compiler qualification;
- package/manifest;
- validation process;
- repository/lifecycle store;
- activation mechanism;
- runtime consumer;
- operating protocol;
- projection/adapter;
- deployment non-bypassability claim.

Conformance of one object MUST NOT be represented as whole-lifecycle conformance.

## 3. Required conformance-claim content

A conformance claim MUST identify, as applicable:

- specification/version;
- conformance object;
- implementation/product/organization and version;
- applicable profile(s);
- scope and jurisdiction/domain;
- automation level;
- assurance level/evidence basis;
- consequence/risk class if used;
- compiler/configuration identity if material;
- packages/classes covered;
- validation methods;
- assessor/assessment relationship;
- effective period;
- exclusions/limitations/unresolved findings;
- compensating controls;
- invalidation/reassessment conditions;
- contestability profile where applicable;
- cryptographic trust profile where material; and
- deployment evidence basis for any non-bypassability claim.

## 4. Partial and conditional conformance

Partial conformance MAY be claimed for a declared subset. It MUST NOT be presented as full-lifecycle conformance.

Conditional conformance MUST identify the external dependency/condition, accepting authority where relevant, evidence, and invalidation trigger.

A mandatory core invariant MUST NOT be waived merely by calling the implementation partially conformant.

## 5. Assessment forms

A conformance claim SHOULD distinguish producer self-attestation, second-party assessment, independent internal assessment, independent external assessment, formal-analysis evidence, and continuing operational assurance. These labels describe evidence/independence; they do not imply absolute correctness.

## 6. Legal-compliance limitation

Conformance MUST NOT be represented as a general legal opinion, regulatory approval, or guarantee of lawful/ethical outcomes. A conforming process can faithfully operationalize defective, disputed, or unlawful source governance.
