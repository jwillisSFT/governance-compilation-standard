# Assumptions and Analysis Bounds

A formal result is valid only within the declared analysis boundary.

At minimum, a proof profile SHOULD identify:

- specification/profile/model versions;
- action and target universe;
- actor/authority universe;
- source and invariant baseline;
- time model;
- state variables;
- evidence model;
- failure/attacker model;
- composition operators;
- external dependencies;
- solver/tool/version/configuration;
- finite bounds or abstraction relation;
- properties checked;
- witnesses/counterexamples retained; and
- known exclusions.

## Open-world warning

Governance-source completeness and real-world action completeness can be open-world problems. A finite proof over a declared modeled universe does not establish that an unknown applicable source, unmodeled action, alternate privileged route, or misclassified target cannot exist outside that universe.

## Legitimacy boundary

The formal model can establish properties of encoded authority relationships under assumptions. It cannot by itself prove that the underlying authority is morally legitimate, legally valid, constitutionally valid, socially beneficial, or otherwise substantively justified.
