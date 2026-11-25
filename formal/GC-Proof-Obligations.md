# GC Proof and Analysis Obligations

## Claim vocabulary

A result SHOULD be labeled as one of:

- **Definition** — stipulated semantics.
- **Derived proposition** — follows from explicitly identified definitions/assumptions.
- **Proof sketch** — structured but not necessarily machine-checked argument.
- **Proof obligation** — property that must be established for a concrete profile/implementation.
- **Bounded executable check** — finite computational evidence over a declared fixture.
- **Machine-checked verification** — property established by an identified formal method/tool under declared assumptions.
- **Implementation conformance result** — evidence of implementation correspondence.
- **Operational/empirical evidence** — observation in a defined environment/population.

## Required discipline

1. A proof claim MUST identify the model/profile/version and assumptions.
2. A bounded check MUST identify the finite bound/fixture and MUST NOT be generalized beyond it without justification.
3. A solver result MUST distinguish `satisfied`, `unsatisfied`, `indeterminate`, and `not evaluated` where applicable.
4. A safety result SHOULD include a nonvacuity or positive witness when legitimate success is intended.
5. A projection proof MUST identify the semantic relation between source and target representations.
6. A deployment property such as non-bypassability MUST NOT be inferred from a package proof alone.

## Priority proof campaign for independent research

The recommended first machine-checked campaign is:

1. authority-space closure for a finite action/context domain;
2. complete region coverage/mapping;
3. CTC satisfiability;
4. no-silent-weakening for a declared composition algebra;
5. invariant preservation;
6. target and closure reachability;
7. no-unauthorized-closure paired with nonvacuity;
8. projection soundness for one concrete target language;
9. stale-authorization prevention across commitment;
10. refinement between a runtime consumer and canonical CTC semantics.
