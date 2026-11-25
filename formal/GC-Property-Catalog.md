# GC Property Catalog

**Status:** Normative registry of proof/analysis obligations; the evidence status shown is the v0.1 release status, not a claim of universal proof.

## GC-PROP-001 — Authority-space closure

- **Class:** safety
- **Property:** No modeled or projected authorization path grants authority outside the approved Permitted Action Set.
- **Key assumptions:** Approved A_P is complete for the declared scope.
- **v0.1 status:** proof obligation; finite defect fixture
- **Evidence expected for a concrete profile:** bounded/exhaustive authority analysis or formal proof plus projection conformance

## GC-PROP-002 — Region coverage

- **Class:** coverage
- **Property:** Every action/context in the declared covered domain resolves to governance treatment or an explicit unknown/indeterminate/refusal disposition.
- **Key assumptions:** The covered action/context domain is finitely or otherwise precisely characterized.
- **v0.1 status:** analysis obligation; finite fixture
- **Evidence expected for a concrete profile:** coverage analysis over declared domain/profile

## GC-PROP-003 — Region-to-contract mapping completeness

- **Class:** coverage
- **Property:** Every applicable region requiring transition governance resolves to defined transition contract semantics.
- **Key assumptions:** Region applicability semantics are defined.
- **v0.1 status:** analysis obligation; finite fixture
- **Evidence expected for a concrete profile:** exhaustive mapping analysis within profile scope

## GC-PROP-004 — CTC well-formedness

- **Class:** structural
- **Property:** Each required CTC contains the six core semantic components and resolvable mandatory references.
- **Key assumptions:** The profile identifies required fields and reference domains.
- **v0.1 status:** structural conformance property
- **Evidence expected for a concrete profile:** schema/type validation plus semantic reference checks

## GC-PROP-005 — CTC satisfiability

- **Class:** existence
- **Property:** Relevant CTC predicates admit at least one valuation under declared assumptions where the contract is intended to be usable.
- **Key assumptions:** Predicate semantics and assumptions are explicit.
- **v0.1 status:** analysis obligation; finite witness search
- **Evidence expected for a concrete profile:** SAT/SMT/exhaustive finite analysis or justified alternative

## GC-PROP-006 — No silent weakening

- **Class:** composition
- **Property:** Composition does not silently discard mandatory obligations absent an explicit applicable authorized non-monotonic rule.
- **Key assumptions:** Composition operators and override semantics are declared.
- **v0.1 status:** proof obligation; restricted monotone argument; finite defect fixture
- **Evidence expected for a concrete profile:** proof or exhaustive bounded analysis for all permitted composition operators/override rules

## GC-PROP-007 — Invariant preservation

- **Class:** safety
- **Property:** Authorized governed transitions preserve applicable constitutional and system invariants.
- **Key assumptions:** Invariant predicates and transition semantics are defined.
- **v0.1 status:** proof obligation; finite example checks
- **Evidence expected for a concrete profile:** transition-system/model proof plus implementation evidence

## GC-PROP-008 — Authorization satisfiability

- **Class:** existence
- **Property:** Intended authorization classes contain admissible witnesses rather than being unintentionally impossible.
- **Key assumptions:** Authority/evidence predicates and assumptions are explicit.
- **v0.1 status:** analysis obligation; finite witness search
- **Evidence expected for a concrete profile:** profile-specific satisfiability analysis

## GC-PROP-009 — Target-state reachability

- **Class:** liveness
- **Property:** A legitimate governed transition can reach an acceptable target state where the profile intends success to be possible.
- **Key assumptions:** Transition/target semantics are defined.
- **v0.1 status:** reachability obligation; finite fixture
- **Evidence expected for a concrete profile:** model checking/reachability analysis

## GC-PROP-010 — Evidence-source capability

- **Class:** assurance
- **Property:** Required evidence types can be produced by declared admissible evidence sources under profile assumptions.
- **Key assumptions:** Evidence source interfaces and availability assumptions are declared.
- **v0.1 status:** assurance obligation; capability mapping
- **Evidence expected for a concrete profile:** source qualification, interface tests, operational availability evidence

## GC-PROP-011 — Successful closure reachability

- **Class:** liveness
- **Property:** Legitimate executions can reach successful evidentiary closure when the profile makes a meaningful success claim.
- **Key assumptions:** Target-state and closure semantics are defined.
- **v0.1 status:** reachability/nonvacuity obligation; finite witness
- **Evidence expected for a concrete profile:** transition and closure reachability analysis

## GC-PROP-012 — No unauthorized closure

- **Class:** safety
- **Property:** Successful closure cannot occur unless required authorization and closure conditions hold.
- **Key assumptions:** Closure outcome semantics are explicit.
- **v0.1 status:** safety obligation; finite fixture
- **Evidence expected for a concrete profile:** formal safety analysis plus implementation conformance testing

## GC-PROP-013 — Nonvacuity

- **Class:** meta-property
- **Property:** A safety result is not accepted merely because legitimate success states are unreachable.
- **Key assumptions:** The profile intends at least one legitimate successful behavior.
- **v0.1 status:** explicit analysis obligation
- **Evidence expected for a concrete profile:** positive witness paired with safety result

## GC-PROP-014 — Projection soundness

- **Class:** refinement
- **Property:** Target artifacts do not grant authority beyond or weaken mandatory semantics of the canonical approved model.
- **Key assumptions:** Source and target semantics and mapping are defined.
- **v0.1 status:** semantic-preservation proof obligation; finite projection defect fixture
- **Evidence expected for a concrete profile:** compiler/refinement proof, differential analysis, target conformance tests

## GC-PROP-015 — Closure-projection soundness

- **Class:** refinement
- **Property:** A target representation cannot claim successful closure under conditions weaker than the canonical model.
- **Key assumptions:** Canonical and target closure semantics are comparable.
- **v0.1 status:** semantic-preservation proof obligation; finite defect fixture
- **Evidence expected for a concrete profile:** projection/refinement analysis plus downstream conformance evidence

## GC-PROP-016 — Commit freshness

- **Class:** safety
- **Property:** A stale proposal-time authorization cannot commit after a material authority/evidence/state/governance change when the profile requires current eligibility.
- **Key assumptions:** The profile defines freshness-sensitive conditions and commit semantics.
- **v0.1 status:** interface proof/conformance obligation; stale-auth fixture
- **Evidence expected for a concrete profile:** atomic/fencing/revalidation proof and adversarial runtime testing

## GC-PROP-017 — Deployment non-bypassability

- **Class:** deployment assurance
- **Property:** Within the declared deployment boundary, every consequence-producing route for a governed effect is mediated by the required enforcement path or otherwise structurally unable to produce the effect.
- **Key assumptions:** Boundary/routes/identities/privileged paths are enumerated sufficiently for the claim.
- **v0.1 status:** deployment claim; not established by package semantics
- **Evidence expected for a concrete profile:** route coverage analysis, configuration/identity evidence, negative/adversarial testing, target-side observation
