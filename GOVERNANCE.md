# Governance of the Governance Compilation Open Specification

## 1. Purpose

This file governs changes to the versioned open specification. It does not govern independent implementations built from the specification.

## 2. Initial specification authority

During the pre-1.0 research and stabilization phase, **John M. Willis / Sustainable Future Tech, Inc.** serves as Specification Editor and release authority. This preserves a coherent reference baseline while public implementation, research, and standards feedback develops.

The editor is expected to publish the rationale for material normative changes and to preserve dissenting technical issues when they cannot be resolved immediately.

## 3. Change classes

Changes are classified as:

- **Editorial** — no normative semantic effect.
- **Clarification** — resolves ambiguity without intentionally changing the normative obligation.
- **Normative additive** — adds a requirement, object, property, profile, or behavior.
- **Normative breaking** — changes or removes an established semantic obligation.
- **Research/experimental** — explicitly non-normative material for evaluation.

## 4. Normative change requirements

A normative change proposal should include:

1. the affected requirement IDs and specification sections;
2. the problem or counterexample motivating the change;
3. proposed text or machine-readable change;
4. compatibility impact;
5. security/authority impact;
6. conformance-test impact;
7. evidence supporting the proposal; and
8. unresolved objections, if any.

Breaking changes require a release boundary and migration note.

## 5. Public review

Issues and pull requests may propose corrections, counterexamples, new profiles, formalizations, conformance tests, or independent implementation evidence. Acceptance means inclusion in the open specification; it does not assign authorship of unrelated inventions or waive patent rights.

## 6. Release approval

A release is approved when the Specification Editor:

- confirms the normative diff;
- confirms schema and validation checks;
- reviews open blocking issues;
- updates `VERSION`, `CHANGELOG.md`, and release notes; and
- records the release manifest.

## 7. Future governance transition

The project is intentionally structured so that governance can later transition to a multi-party technical steering process or formal standards-development organization. Such a transition requires an explicit governance revision, including treatment of voting/consensus, appeals, contributions, intellectual property, and release authority.

No future governance model is implied by this v0.1 file.
