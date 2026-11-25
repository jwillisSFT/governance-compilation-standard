# GC Conformance Test Assertions

**Status:** v0.1.0 public-review assertions. These assertions do not constitute a certification scheme.

| ID | Area | Assertion | Target | Method |
|---|---|---|---|---|
| GC-TA-001 | Schema | Each published JSON Schema is a valid Draft 2020-12 schema. | all schemas | automated |
| GC-TA-002 | GIR | Each positive GIR example validates structurally against gir.schema.json. | positive examples | automated |
| GC-TA-003 | Package | Each positive package manifest validates structurally against package-manifest.schema.json. | positive examples | automated |
| GC-TA-004 | Authority | Every permitted action reference resolves to a declared action marked in_set or conditional. | positive GIR | automated semantic check |
| GC-TA-005 | Regions | Every active region contract reference resolves to a declared active CTC. | positive GIR | automated semantic check |
| GC-TA-006 | Mapping | Every active region has a region-contract mapping entry. | positive GIR | automated semantic check |
| GC-TA-007 | CTC | Each active CTC includes all six core semantic components. | positive GIR | schema + semantic check |
| GC-TA-008 | Traceability | Each governance requirement references at least one declared source. | positive GIR | automated semantic check |
| GC-TA-009 | Traceability | Each active CTC references at least one declared source. | positive GIR | automated semantic check |
| GC-TA-010 | Evidence | Required evidence IDs are unique within a CTC component/catalog context. | positive GIR | automated semantic check |
| GC-TA-011 | No silent weakening | A high-value overlay adding a required approval remains additive under union/conjunction composition. | financial example | bounded semantic check |
| GC-TA-012 | Authority expansion | Fixture with out-of-set action inserted into permitted set is detected. | negative fixture | automated semantic check |
| GC-TA-013 | Region coverage | Fixture removing a required region mapping is detected. | negative fixture | automated semantic check |
| GC-TA-014 | CTC | Fixture missing a required CTC component is rejected structurally. | negative fixture | schema validation |
| GC-TA-015 | Silent weakening | Fixture that replaces union_required evidence composition with last_write_wins is detected. | negative fixture | automated semantic check |
| GC-TA-016 | Commit freshness | Stale authorization fixture demonstrates that proposal-time approval cannot substitute for current approval. | negative vector | bounded semantic rule |
| GC-TA-017 | Closure | False-closure fixture is detected when success closure lacks required target evidence. | negative fixture | automated semantic check |
| GC-TA-018 | Projection | Unsound target projection granting undeclared action is classified as authority expansion. | negative vector | bounded semantic rule |
| GC-TA-019 | Profile | Core profile validates against profile.schema.json. | profile | automated |
| GC-TA-020 | Conformance claim | A conformance claim must include object, version, profiles, scope, evidence basis, limitations/exclusions, and invalidation conditions. | claim schema | schema |
| GC-TA-021 | Claim discipline | Package conformance is not accepted as evidence of deployment non-bypassability without deployment evidence references. | claim | automated semantic check |
| GC-TA-022 | Unknown extension | Unknown mandatory authority/evidence/closure extension causes incompatibility rather than ignore. | runtime consumer | implementation test |
| GC-TA-023 | Lifecycle | Activation of revoked/suspended package is refused. | runtime lifecycle | implementation test |
| GC-TA-024 | Evidence | Authenticated-but-stale evidence does not satisfy a freshness-sensitive requirement. | runtime evidence | implementation test |
| GC-TA-025 | Closure | Successful execution without required post-commit evidence does not produce successful closure. | runtime closure | implementation test |
| GC-TA-026 | Legal limitation | Conformance output does not claim legal compliance as a derived result. | claim/documentation | review |
| GC-TA-027 | Repository hygiene | Release contains no project-specific secrets or prohibited internal-development bleed terms. | repository | automated scan |
| GC-TA-028 | Identifiers | Normative requirement identifiers are unique. | requirements catalog | automated |
| GC-TA-029 | Formal | Formal property identifiers are unique. | property catalog | automated |
| GC-TA-030 | Manifest | Release manifest hashes all immutable release files except the manifest itself and the generated release-validation report. | release | automated |
