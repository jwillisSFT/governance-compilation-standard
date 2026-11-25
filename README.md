# Governance Compilation Open Specification

**Release:** v0.1.0 — Draft Public Review  
**Status:** pre-standard, implementation-neutral public specification  
**Repository:** `jwillisSFT/governance-compilation-standard`

Governance Compilation is a proposed engineering discipline for transforming authorized human governance into **bounded, traceable, machine-evaluable governance artifacts** while preserving authority, provenance, interpretation, assurance obligations, activation state, and downstream consequence semantics.

This repository is the versioned open-specification surface for that work. It is designed so that an independent team can implement, test, criticize, extend, or profile Governance Compilation **without using AGCP or any other proprietary runtime system**.

## Core principle

Computational capability does not create institutional authority.

Conceptually:

```text
Governance sources + invariants + authority model + governed-action semantics
    -> normalized governance model
    -> authority-bounded permitted action space
    -> governance-defined action regions
    -> complete transition contracts
    -> formal analysis and proof obligations
    -> validated machine-readable governance artifacts
    -> controlled issuance and activation
    -> runtime authorization and commitment
    -> target-state verification
    -> evidentiary closure
```

The specification preserves the distinction:

```text
permitted != authorized != committed != verified != closed
```

## What v0.1.0 contains

This release includes:

- a normative Core Specification;
- normative terminology and requirements language;
- a Governance Intermediate Representation (GIR) model;
- Permitted Action Set and Governance-Defined Action Region semantics;
- Complete Transition Contract (CTC) semantics;
- typed composition and no-silent-weakening requirements;
- evidence, target-state, and evidentiary-closure semantics;
- package, lifecycle, activation, and runtime-consumer requirements;
- profile and extension rules;
- security and trust-boundary requirements;
- more than 100 individually identified normative requirements;
- JSON Schema 2020-12 schemas;
- four machine-readable examples;
- a formal property catalog and proof-obligation registry;
- conformance objects, claims, assertions, and negative test fixtures;
- the bounded analytical validation suite used by the research monograph;
- repository validation tooling and CI configuration;
- public-review governance and contribution procedures; and
- an open research agenda.

## Status and claim discipline

v0.1.0 is a **Draft Public Review** release. It is not an adopted consensus standard, certification scheme, legal-compliance framework, completed formal-verification result, or production implementation.

The specification distinguishes:

- **normative requirement** — a requirement for conformance to a declared profile;
- **definition** — a stipulated semantic meaning;
- **proof obligation** — a property that a concrete profile or implementation must establish;
- **bounded analytical evidence** — executable evidence over a declared finite fixture;
- **implementation-conformance evidence** — evidence that an implementation realizes specified semantics; and
- **empirical evidence** — observed evidence from operational or experimental settings.

No lower evidence level is represented as establishing a higher one.

## Repository map

| Path | Purpose |
|---|---|
| `spec/` | Normative specification modules |
| `requirements/` | Traceable normative requirement catalog |
| `schemas/` | Technology-neutral JSON Schema representation |
| `formal/` | Formal reference model, properties, assumptions, proof obligations |
| `conformance/` | Conformance model, test assertions, fixtures |
| `profiles/` | Core and extension-profile definitions |
| `examples/` | Machine-readable worked examples |
| `validation/` | Bounded analytical validation and release evidence |
| `research/` | Open research problems and replication guidance |
| `docs/` | Informative architecture and book-to-spec crosswalks |
| `tools/` | Repository-validation tooling |

## Normative versus informative material

The files under `spec/` are normative except where a section is explicitly marked **Informative**. `requirements/GC-Normative-Requirements.csv` is the machine-readable requirements index. Schemas are normative for the v0.1 JSON interchange profile but do not require implementations to use JSON internally.

Examples, research material, diagrams, and explanatory documents are informative unless a profile explicitly incorporates them.

## Independence from runtime implementations

Governance Compilation ends its design-time lifecycle at controlled issuance/activation and defines the contract by which runtime consumers use compiled governance. A conforming implementation may use any runtime architecture that satisfies the declared consumer and deployment obligations.

AGCP is a separate runtime-governance reference realization in the broader Runtime Governance Engineering work. **AGCP is not required by this specification and this repository does not define AGCP source code, deployment configuration, cryptographic keys, or proprietary implementation details.**

## Quick start

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_repo.py
python validation/bounded-analytical-suite/run_bounded_validation.py
```

See `examples/README.md` for the example domains and `conformance/GC-Conformance.md` for how to state a bounded conformance claim.

## Research foundation

The principal research foundation is:

**John M. Willis, _Governance Compilation: A Reference Model for Translating Human Governance into Machine-Evaluable Controls_, Runtime Governance Engineering, Volume 3, First Edition, Sustainable Future Tech Publishing, 2026. ISBN 979-8-9971149-3-0.**

The book is informative with respect to this repository. For a particular repository release, the versioned specification controls claims of specification conformance.

## License and patent notice

See `LICENSE.md` and `NOTICE.md`. Copyright permission and patent rights are separate.

## Public review

v0.1.0 is intentionally suitable for critical review. Contributions are welcome that:

- identify ambiguity or internal inconsistency;
- produce counterexamples;
- test a proof obligation;
- propose an independent implementation;
- demonstrate semantic loss in a projection;
- improve interoperability or conformance testing; or
- provide empirical evidence that supports, narrows, or falsifies a claim.

See `CONTRIBUTING.md` and `GOVERNANCE.md`.
