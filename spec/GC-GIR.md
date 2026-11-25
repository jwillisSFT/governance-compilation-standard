# GC-GIR — Governance Intermediate Representation

**Status:** Normative, v0.1.0

## 1. Purpose

The GIR is the canonical technology-neutral governance model from which target-specific artifacts can be projected. Implementations MAY use another internal representation, but an implementation claiming the v0.1 GIR interchange profile MUST be able to serialize/deserialize the normative semantics represented by the v0.1 schemas without silent loss.

## 2. Conceptual model

For transition-governance analysis, the complete GIR Governance Model can be represented abstractly as:

```text
GM_GIR = <G_*, CI, SI, A_P, S, M, K, R>
```

where:

- `G_*` — governance sources, requirements, interpretations, authority/provenance, and scope semantics;
- `CI` — constitutional invariants;
- `SI` — system invariants;
- `A_P` — authority-bounded Permitted Action Set;
- `S` — Governance-Defined Action Regions;
- `M` — region-to-contract mapping;
- `K` — Complete Transition Contracts;
- `R` — additional resolution/profile semantics, including composition, evidence, projection, and lifecycle rules.

The tuple is a reference abstraction, not a requirement that implementations use tuple storage.

## 3. Identity and versioning

Every GIR document MUST have a stable identifier, version, specification version, creation timestamp, and declared scope.

References between GIR objects MUST use stable identifiers. An implementation MUST NOT use display names as the sole semantic identity of objects that participate in traceability or authority decisions.

## 4. Source and requirement linkage

Each governance requirement MUST reference at least one source or authorized interpretation record. A derived requirement MAY reference multiple sources and MUST identify the derivation/interpretation provenance necessary for review.

## 5. Authority semantics

Authority assertions MUST be bound to provenance sufficient to answer:

```text
Who/what holds the authority?
What authority is asserted?
For what scope/action/target?
Under which delegation/office/instrument?
During what validity period?
What revokes or supersedes it?
```

Authority provenance MUST be separable from ordinary data provenance.

## 6. Permitted Action Set

The GIR MUST represent the authority-defined action boundary separately from current authorization predicates.

Action definitions SHOULD use typed parameters and bounded target semantics. An apparently narrow action primitive MUST NOT conceal arbitrary authority through an unconstrained parameter when that would defeat the declared action boundary.

## 7. Regions and mappings

A Governance-Defined Action Region MUST identify its predicate/treatment signature, provenance/version, status, and relation to the Permitted Action Set. Region overlap MAY be valid; overlap MUST be handled through explicit applicability/composition semantics rather than implementation ordering accidents.

Every action/context in a profile that requires transition governance MUST either resolve to applicable governance treatment or result in an explicit unknown/indeterminate/refusal status.

## 8. Complete Transition Contracts

Each required CTC MUST contain the six core components defined by `GC-Transition-Governance.md`. References to evidence types, authority predicates, invariants, target states, and closure semantics MUST be resolvable within the package/profile or through declared external dependencies.

## 9. Evidence semantics

Evidence requirements SHOULD distinguish, as applicable:

- evidence type;
- producing source/interface;
- subject/target binding;
- authenticity/integrity;
- freshness/time window;
- anti-replay property;
- qualification/trust basis;
- independence/corroboration requirement;
- required versus advisory status; and
- invalidation conditions.

Authentication of an evidence object MUST NOT be interpreted as establishing that its content is true unless the applicable evidence profile separately establishes the relevant observation/trust claim.

## 10. Decision and failure semantics

The GIR MUST support explicit refusal/indeterminate/escalation outcomes. Missing mandatory information MUST NOT default to permission unless the applicable governance explicitly authorizes that behavior.

## 11. Canonicalization and deterministic serialization

The v0.1 JSON profile uses ordinary JSON for interchange. A profile that uses signatures/digests over canonical content MUST specify a deterministic canonicalization/serialization method. The Core does not select a cryptographic canonicalization algorithm.

## 12. Extensions

Extensions MUST be namespace-identifiable and MUST NOT alter the meaning of a core field. A consumer that does not understand a mandatory extension MUST refuse or declare incompatibility rather than silently ignore semantics that could affect authority, evidence, target state, or closure.
