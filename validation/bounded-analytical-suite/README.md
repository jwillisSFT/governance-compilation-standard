# Governance Compilation - Bounded Analytical Validation Suite

## Status

This is a **bounded executable analytical validation suite** for the Governance Compilation reference model. It is deliberately finite and dependency-free so that readers can reproduce the checks with ordinary Python.

It is **not** Alloy, SMT solving, TLA+, theorem proving, model checking, proof assistance, or a substitute for formal verification. Passing results establish only that the encoded properties hold for the enumerated fixtures and finite states represented by this suite.

## What it checks

The baseline fixture exercises finite checks corresponding to:

- authority-space closure;
- region coverage;
- region-to-contract mapping completeness;
- Complete Transition Contract structural well-formedness;
- bounded contract satisfiability by witness search;
- no-silent-weakening under union composition;
- a simple invariant-preservation condition;
- authorization satisfiability;
- target-state reachability in the finite transition function;
- evidence-source capability;
- successful-closure reachability;
- no-unauthorized-closure;
- nonvacuity;
- projection soundness; and
- closure-projection soundness.

The suite also injects deliberately defective variants for:

1. authority-boundary expansion;
2. missing region coverage;
3. contradictory/impossible contract conditions;
4. silent weakening during composition;
5. stale authorization caused by loss of policy-version revalidation;
6. false closure projection that drops required post-evidence; and
7. unsound projection that grants an unapproved action type.

## Run

```bash
python3 run_bounded_validation.py
```

The command writes `results.json` and exits nonzero if the baseline fails or an injected defect is not detected.

## Reproducibility boundary

The suite is useful for regression, example validation, teaching, specification discussion, and detecting contradictions in the finite fixture. It does **not** establish that:

- the Governance Compilation model is universally sound or complete;
- the checked properties hold for all possible governance models;
- a real compiler preserves the model;
- a deployed runtime is non-bypassable;
- evidence sources are trustworthy in operation; or
- Governance Compilation is empirically effective in production.

Those claims require separate formal, conformance, engineering, and empirical evidence.
