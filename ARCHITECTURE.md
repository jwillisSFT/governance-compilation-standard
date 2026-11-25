# Architecture Overview

Governance Compilation separates the creation of machine-evaluable governance from the runtime system that consumes it.

## Source-to-consequence chain

```text
Authorized governance sources
        |
        v
Interpretation + normalized requirements
        |
        v
Governance Intermediate Representation (GIR)
        |
        +--> authority model
        +--> Permitted Action Set
        +--> Governance-Defined Action Regions
        +--> Complete Transition Contracts
        +--> invariants + evidence semantics
        |
        v
Formal/analytical obligations
        |
        v
Target projection(s) + immutable package
        |
        v
Package validation + authoritative issuance
        |
        v
Controlled activation
        |
        v
Runtime consumer
        |
        v
Commit boundary
        |
        v
Target-state verification
        |
        v
Evidentiary closure
```

## Architectural rules

1. Source authority is not inferred from compiler output.
2. Computational capability does not imply action authority.
3. Membership in the Permitted Action Set does not itself authorize a concrete action.
4. Authorization is re-evaluated when the applicable profile requires commitment-boundary freshness.
5. A target projection cannot legitimately expand authority beyond the approved canonical model.
6. Mandatory obligations cannot disappear through composition without an explicitly authorized non-monotonic rule.
7. Evidence authenticity does not by itself establish truth of the evidence content.
8. Runtime success does not establish target-state verification or governance closure.
9. Package requirements do not establish deployment non-bypassability.
10. Conformance does not establish legal, ethical, policy, or safety correctness of the underlying governance.
