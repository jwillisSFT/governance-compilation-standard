# Contributing

Contributions that critically test the specification are especially welcome.

## Good contribution types

- specification defect or ambiguity;
- authority-expansion counterexample;
- CTC or region model that cannot be represented;
- proof or counterexample for a listed proof obligation;
- independent implementation report;
- projection semantic-equivalence result;
- conformance test or negative fixture;
- empirical study design/result;
- accessibility, contestability, or domain-profile improvement.

## Normative changes

Normative changes should identify affected requirement IDs. New normative statements must receive stable IDs before release.

Use RFC-style uppercase keywords only when the statement is intended to be normative. Avoid using **MUST**, **SHALL**, **SHOULD**, or **MAY** casually in informative prose.

## Pull requests

A pull request should state:

- change class;
- specification sections affected;
- requirement IDs affected;
- compatibility impact;
- new/updated tests;
- evidence or rationale;
- unresolved questions.

## Independence and implementation neutrality

Do not introduce a dependency on AGCP, proprietary SFT code, private build systems, customer configuration, credentials, cryptographic secrets, or non-public assessment methods into the core specification.

Implementation-specific examples are welcome when they are clearly identified as informative and do not redefine the technology-neutral normative semantics.

## Research claims

Label evidence at its actual level. Do not present finite testing as proof, package conformance as deployment non-bypassability, technical conformance as legal compliance, or authenticated evidence as necessarily true evidence.
