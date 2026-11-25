# Replication Guidelines

A study or implementation report intended to support or challenge a Governance Compilation claim should preserve enough information for another team to reproduce the result.

## Minimum record

- specification release/commit;
- profile/version;
- source corpus or synthetic fixtures;
- declared scope/assumptions/exclusions;
- GIR/package artifacts;
- compiler/tool versions and configuration;
- formal model/tool/bounds where applicable;
- test vectors and expected outcomes;
- actual outcomes/witnesses/counterexamples;
- environment/dependency versions;
- analysis scripts/commands where publishable;
- deviations from the specification;
- unresolved findings;
- negative results.

## Claim discipline

Report exactly what the evidence establishes. A successful finite fixture is evidence of that fixture; a model-checking result is relative to the modeled abstraction and bounds; an implementation test is not a proof of institutional correctness; an operational pilot does not establish cross-domain generality.
