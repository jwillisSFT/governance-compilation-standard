# GC Formal Reference Model

**Status:** Normative semantic reference with bounded claim status, v0.1.0

## 1. Purpose

This file states the mathematical/relational objects that profiles may formalize. It does not claim that the complete model has been machine-checked.

## 2. Scoped model

A proof or analysis claim is meaningful only relative to a declared scope:

```text
Sigma = <sources, jurisdictions, domains, systems, actors, authority,
         action/target space, lifecycle, threat/failure model,
         assumptions H, exclusions X>
```

Every formal claim MUST identify or reference the relevant `Sigma` or equivalent declared scope.

## 3. Canonical governance model

For transition-governance analysis:

```text
GM_GIR = <G_*, CI, SI, A_P, S, M, K, R>
```

where `G_*` includes source/requirement/interpretation/authority semantics; `CI` and `SI` are constitutional/system invariants; `A_P` is the Permitted Action Set; `S` is the set of Governance-Defined Action Regions; `M` maps applicable regions to contracts; `K` is the set of CTCs; and `R` contains additional profile/resolution/composition/projection semantics.

## 4. Eligibility

A generic dependency is:

```text
Eligible(a,c) = InAP(a,c)
             AND AuthSatisfied(a,c)
             AND InvariantsSatisfied(a,c)
```

Profiles MAY introduce additional mandatory conditions. This expression does not imply that every implementation uses a single Boolean function.

## 5. Region applicability

Let `S(a,c)` be the set of active regions whose predicates hold for action/context `(a,c)`. Mapping `M` resolves each applicable region to one or more transition contracts. The effective transition governance is obtained only through the profile's declared typed-composition rules.

## 6. Complete Transition Contract

```text
K_i = <Pre_i, Auth_i, E_pre_i, T_i, E_post_i, L_i>
```

The components are typed and MUST NOT be composed through an unspecified generic merge.

`ContractWellFormed(K_i)` does not imply `ContractSatisfiable(K_i)`.

`AuthorizationSatisfiable(K_i)` does not imply `TargetReachable(K_i)` or `ClosureReachable(K_i)`.

## 7. Commitment

Proposal-time eligibility does not establish commit-time eligibility. A profile that requires current eligibility at the consequence-producing boundary must establish an equivalent of:

```text
Commit(a,c_t) => Eligible(a,c_t)
```

where `c_t` is the authoritative context at commitment, not merely the proposal-time context.

## 8. Projection

A target projection `P` from canonical model `G` to target representation `T` is required to satisfy the profile's semantic-preservation claims. At minimum, authority must not expand:

```text
Authorized_T(a,c) => Authorized_G(a,c)
```

within the declared target/profile mapping.

Where target closure is represented:

```text
Closed_T(x) => Closed_G(x)
```

under the declared semantic relation.

These are proof obligations until established for a concrete projection.

## 9. Closure

Closure is outcome-specific. A generic successful-closure condition requires applicable target-state, post-commit evidence, and closure predicates. The exact relation is profile-defined.

A safety claim such as no-unauthorized-closure SHOULD be paired with a nonvacuity/reachability result when successful operation is intended.

## 10. Evidence-level rule

A mathematical expression defines a property to be established under declared assumptions. It is not by itself evidence that the property has been universally proved, implemented, or empirically demonstrated.
