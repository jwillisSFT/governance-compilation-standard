# GC-Evidence-and-Assurance — Evidence Roles, Assurance Claims, and Claim Boundaries

**Status:** Normative framework, v0.1.0

## 1. Evidence is typed by claim

A conforming assurance record MUST identify what claim an evidence item supports. Evidence serving one claim MUST NOT silently stand in for another claim.

The specification distinguishes at least:

- source/authenticity/provenance evidence;
- interpretation/approval evidence;
- model-verification evidence;
- compiler/toolchain qualification evidence;
- package/build provenance;
- package-validation evidence;
- authorization evidence;
- enforcement/commit evidence;
- target-state evidence;
- closure evidence; and
- continuing-assurance evidence.

## 2. Authentication is not truth

For evidence `e` produced by source `s`:

```text
Authentic(e,s) does not imply True(Content(e))
```

A profile that depends on evidence truth/accuracy MUST state the observation, source-qualification, independence, corroboration, or other assumptions that justify that claim.

## 3. Validation-evidence ladder

Claims SHOULD identify their evidence level. A useful progression is:

1. conceptual argument;
2. formal statement;
3. proof sketch;
4. bounded executable check;
5. machine-checked verification;
6. implementation conformance;
7. operational/empirical evidence.

A lower level MUST NOT be described as a higher level without additional evidence.

## 4. Validation status

A property/result SHOULD use explicit statuses such as:

- `satisfied`;
- `unsatisfied`;
- `indeterminate`;
- `not_applicable`;
- `not_evaluated`.

A tool's solver status MUST NOT automatically determine the institutional disposition of a governance package. The profile MUST define which actor/process is authorized to accept, reject, conditionally accept, or escalate a result.

## 5. Assurance case

For higher-consequence profiles, the assurance case SHOULD link:

```text
claim -> argument -> evidence -> assumptions/context -> limitations
```

The assurance case SHOULD make dependencies explicit enough that a change to a source, model, compiler, package, evidence source, runtime boundary, or deployment can identify affected claims.

## 6. Continuing assurance

Activation does not freeze the validity of governance. Profiles SHOULD define which changes in source status, authority, evidence source, target system, dependency, topology, or threat environment invalidate prior assurance and trigger review/revalidation.

## 7. Independence

An assurance profile MAY require independent review. Independence claims SHOULD identify organizational, financial, technical, and evidence-access relationships material to the assessment. Formal separation alone does not establish substantive independence.
