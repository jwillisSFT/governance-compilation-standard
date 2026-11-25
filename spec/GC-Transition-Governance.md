# GC-Transition-Governance — Regions, Complete Transition Contracts, Composition, and Closure

**Status:** Normative for the transition-governance profile, v0.1.0

## 1. Permitted Action Set

`A_P` defines the authority-bounded domain in which authorization can potentially exist. The model MUST distinguish action-space membership from current authorization.

Conceptually:

```text
Eligible(a,c) =
    InPermittedActionSet(a,c)
    AND AuthorizationSatisfied(a,c)
    AND InvariantsSatisfied(a,c)
```

This expression is a semantic dependency, not a claim that every implementation uses a Boolean evaluator.

## 2. Governance-Defined Action Regions

A region represents a governance-relevant subset of the action/context domain. Regions MAY be nested or overlapping. Specificity alone MUST NOT be treated as permission to weaken a more general mandatory obligation.

A region definition MUST include:

- stable ID/version;
- predicate or membership semantics;
- source/requirement provenance;
- treatment signature or mapping reference;
- status and applicability;
- priority/precedence only where explicitly authorized.

## 3. Action Mapping Bundle

The mapping layer MUST make it possible to determine which CTCs and invariants apply to an eligible action/context. Mapping gaps within a declared covered region MUST be detected or explicitly classified as indeterminate/refused.

## 4. Complete Transition Contract

A CTC has six required semantic components:

```text
K_i = <Pre_i, Auth_i, E_pre_i, T_i, E_post_i, L_i>
```

### 4.1 Pre-state semantics (`Pre_i`)

Conditions about the state/context that must hold before the transition can be considered.

### 4.2 Authorization semantics (`Auth_i`)

Conditions that establish current authority for the concrete transition. These MAY include actor/principal authority, delegation, approvals, separation of duties, target/scope, time, governance version, risk state, and other profile-specific predicates.

### 4.3 Required pre-commit evidence (`E_pre_i`)

Evidence that must be present and valid before commitment. Required evidence MUST remain required through composition unless an authorized rule explicitly substitutes/overrides it.

### 4.4 Target-state semantics (`T_i`)

The governed resulting-state conditions whose satisfaction is relevant to the transition outcome.

### 4.5 Required post-commit evidence (`E_post_i`)

Evidence required to evaluate target state or outcome after commitment.

### 4.6 Outcome-specific closure semantics (`L_i`)

Conditions/evidence under which the transition may be assigned an authorized terminal governance disposition.

A contract that is structurally well formed is not necessarily satisfiable or reachable.

## 5. Typed composition

Composition MUST be component-specific. An implementation MUST NOT treat all CTC components as one undifferentiated rule set.

For each component, the profile MUST define the permitted composition operator(s), conflict behavior, precedence/override semantics, and failure result.

### 5.1 No-silent-weakening obligation

A composition result MUST NOT silently discard or weaken a mandatory obligation unless the governance model contains an explicit, applicable, authorized non-monotonic rule permitting that effect.

For a purely monotone mandatory-obligation component, union/conjunction of mandatory requirements satisfies the restricted intuition that obligations are preserved. The general property is nevertheless a **proof/conformance obligation**, not a universal theorem for arbitrary policy algebras.

### 5.2 Non-monotonicity

Exception, substitution, precedence, waiver, or override semantics MUST identify:

- authorizing source/authority;
- affected component/obligation;
- scope;
- conditions;
- provenance;
- conflict resolution; and
- resulting evidence/traceability.

Specificity, file order, rule order, or last-write-wins behavior MUST NOT serve as an unmodeled authority to weaken governance.

## 6. Commitment-boundary validity

Authorization at proposal/evaluation time does not guarantee authorization at commitment. Where a relevant condition can change, a conforming runtime profile MUST require revalidation at the commit boundary or enforce an equivalent atomic/fencing/version condition that makes stale authorization unable to commit a changed transition.

## 7. Target-state verification

Target-state verification MUST be based on the applicable target semantics and qualified evidence. A successful API response or request dispatch MUST NOT automatically satisfy a target-state condition unless the governance explicitly defines that observation as sufficient.

## 8. Evidentiary closure

Closure MUST be outcome-specific. The profile MUST distinguish, where material, successful closure, resolved non-success closure, compensation, cancellation, expiration, failure, or other terminal branches.

No-unauthorized-closure is a safety obligation: a transition MUST NOT reach a successful closure disposition unless the applicable authorization and closure conditions hold.

Closure reachability/nonvacuity is a separate obligation: safety MUST NOT be accepted merely because legitimate success is impossible.

## 9. Probabilistic observations

A profile MAY use probabilistic, statistical, model-derived, or uncertain observations as evidence. It MUST nevertheless define deterministic governance semantics for how uncertainty is thresholded, escalated, corroborated, deferred, or classified. Probabilistic evidence does not create undeclared authority.
