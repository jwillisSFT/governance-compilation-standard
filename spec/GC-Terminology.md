# GC-Terminology — Normative Terminology and Requirements Language

**Status:** Normative, v0.1.0

## 1. Requirements language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as normative requirements when, and only when, they appear in uppercase normative statements. Their use follows the established conventions of RFC 2119 and RFC 8174.

## 2. Core terms

**Authorized Governance Source (AGS)** — A source that has been identified as authoritative for a declared governance-compilation scope by an actor or institutional process possessing the authority to make that source selection. Authorization for compilation does not establish the source's legal validity, normative legitimacy, constitutionality, substantive correctness, proportionality, or immunity from challenge.

**Governance Requirement (GR)** — A traceable normative obligation, permission, prohibition, power, constraint, evidence requirement, lifecycle rule, or other operationally relevant requirement derived from or linked to an authorized governance source and any authorized interpretation decision.

**Governance Intermediate Representation (GIR)** — The canonical, technology-neutral model used to represent approved governance semantics before target-specific projection.

**Permitted Action Set (`A_P`)** — The authority-bounded set of actions or action instances for which institutional authorization can potentially exist within the declared scope. Membership does not mean that a specific action is currently authorized.

**Governance-Defined Action Region (GDAR)** — A governance-relevant subset or predicate over the permitted action/context domain for which a distinguishable governance treatment applies.

**Action Mapping Bundle (AMB)** — The bundle relating governed actions/regions to the transition contracts, invariants, evidence requirements, and related semantics that apply to them.

**Complete Transition Contract (CTC)** — A governance contract containing, at minimum, pre-state semantics, authorization semantics, required pre-commit evidence, target-state semantics, required post-commit evidence, and outcome-specific closure semantics.

**Constitutional Invariant (CI)** — A higher-order governance constraint whose amendment or override is controlled by an authority distinct from ordinary lower-level governance rules.

**System Invariant (SI)** — A required system/environment property that must hold for applicable transitions or states.

**Authority Provenance** — Evidence linking an authority assertion or decision to the role, office, delegation, or other authority relationship and ultimately to the originating institutional instrument/source that establishes the scope of authority.

**Evidence Requirement** — A typed requirement for evidence, including admissibility, source, target binding, freshness, anti-replay, independence, corroboration, or other trust conditions where applicable.

**Target-State Verification** — Evaluation of whether the governed post-commit state satisfies the applicable target-state semantics using qualified observations/evidence.

**Evidentiary Closure** — A governance-defined terminal disposition reached only when the applicable outcome-specific closure conditions and required closure evidence are satisfied.

**Governance Compiler** — A human, software, AI-assisted, organizational, or hybrid capability that transforms an approved governance model into one or more target artifacts while preserving required semantics and provenance.

**Compiled Governance Package (CGP)** — An immutable, identifiable bundle of machine-evaluable artifacts and associated manifest information produced from an approved governance model for a declared target/profile.

**Authoritative Issuance** — The controlled decision that a validated package is an approved governance artifact eligible for activation within its declared scope. Issuance and activation are distinct.

**Activation** — The controlled lifecycle transition that binds an authoritatively issued package to a defined runtime scope/effective period.

**Runtime Consumer** — A component/system that uses an active governance package to evaluate or constrain a concrete proposal/action. The consumer need not use any particular product or runtime architecture.

**Commit Boundary** — The consequence-producing boundary at which a governed action becomes operationally consequential and at which required current authority/state/evidence must remain valid.

**Structural Refusal** — A failure behavior that prevents authoritative generation, activation, commitment, or closure when mandatory requirements are not satisfied.

**Projection** — A transformation from canonical GIR semantics into a target-specific representation. Projection conformance requires preservation of the normative semantics within the declared target/profile.

**Proof Obligation** — A property that a profile, model, projection, implementation, or deployment is required to establish under declared assumptions and bounds. A proof obligation is not itself a completed proof.

**Conformance Claim** — A bounded statement identifying the specification version, conformance object, profile, scope, assurance basis, exclusions, limitations, evidence, and validity conditions of an asserted conformance result.

## 3. Non-equivalences

A conforming interpretation of this specification SHALL preserve the following non-equivalences:

```text
capability       != authority
source authority != substantive correctness
permitted        != currently authorized
authorized       != committed
committed        != verified
verified         != closed
authenticated evidence != necessarily true evidence
package requirement != deployment property
conformance      != legal compliance
```
