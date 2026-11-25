# Conformance and Assessment Guide

This guide operationalizes `spec/GC-Conformance.md` for public review.

## 1. Claim template

A bounded claim should take the form:

> Subject **I**, version **v**, conforms to Governance Compilation Open Specification **0.1.0** for conformance object **O**, profile(s) **P**, domain/scope **D**, under evidence/assurance basis **A**, subject to exclusions **X**, limitations **L**, and invalidation conditions **Y**.

## 2. Do not collapse conformance objects

A schema-valid GIR is not a conforming compiler. A conforming compiler is not evidence that a particular package is valid. A valid package is not evidence that activation is authorized. A correct runtime decision is not evidence that all bypass routes are closed. A deployment non-bypassability assessment is not proof that the originating governance is correct.

## 3. Recommended v0.1 assessment sequence

1. structural/schema checks;
2. referential-integrity checks;
3. authority-space and region/mapping checks;
4. CTC well-formedness and satisfiability analysis;
5. composition/no-silent-weakening analysis;
6. invariant and reachability analysis;
7. projection differential/semantic tests;
8. package integrity/lifecycle tests;
9. runtime commitment/freshness tests;
10. target-state/closure tests;
11. deployment route/bypass analysis where claimed;
12. claim-scope and limitation review.

## 4. Evidence levels

Assessment reports should label evidence as developer test, independent test, bounded analysis, machine-checked result, implementation conformance, operational observation, or another clearly defined class. Avoid labels such as "verified" without naming what was verified and by which method.

## 5. v0.1 certification status

There is no official Governance Compilation certification body or accredited certification program in v0.1.0. Third parties may perform independent assessments but should describe them accurately as assessments against this draft specification rather than official certification.
