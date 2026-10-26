# Core Model

## Purpose

This file is the terminology source of truth for the skill.

All writing and governance work uses five canonical objects:

1. **Artifact Brief**
2. **Claim Record**
3. **Evidence Profile**
4. **Narrative Decision**
5. **Boundary Record**

Other references may apply these objects but must not redefine them.

---

## 1. Artifact Brief

The Artifact Brief defines what is being produced and what the reader must be able to conclude.

Minimum fields:

```text
Artifact type:
Audience:
Reader decision or understanding goal:
Title / rubric / adopted scope:
Primary contribution:
Section or chapter responsibility:
Upstream facts already established:
Downstream handoff:
In scope:
Out of scope:
Canonical sources by domain:
Terminology source:
Output language and form:
```

### Primary contribution

The primary contribution is the project object, research action, or system result that the artifact is principally responsible for establishing.

Derive it jointly from:

- binding competition, contractual, or policy obligations;
- the adopted project scope and title;
- explicit project-owner intent;
- the approved document architecture.

Binding external obligations cannot be overridden by narrative convenience. Project-owner intent resolves discretionary emphasis within those obligations. If authoritative inputs conflict materially, stop and request a decision.

The most detailed repository module or easiest demonstration does not become the primary contribution automatically.

---

## 2. Claim Record

A Claim Record represents one material conclusion the artifact asks the reader to accept.

Minimum fields:

```text
Claim ID:
Claim statement:
Claim Type:
Object:
Scope:
State or strength:
Section responsibility:
Required proof:
Claim Lineage anchors:
Decision owner, when applicable:
```

### Claim Type

Claim Type answers:

> What kind of conclusion is this, and what proof obligation applies?

Use exactly these top-level types:

- **Research** — a method, model, analysis, or scientific/algorithmic result;
- **Engineering** — a system mechanism, implementation, runtime behavior, integration, reliability, deployment, or delivery result;
- **Product/Application** — a user-visible capability, organizational use, expected value, or observed real-context outcome.

A claim can depend on more than one type, but one type should own the primary proof responsibility. Split compound claims when ownership is unclear.

### Claim Lineage

Claim Lineage answers:

> Where is the same underlying claim restated across the artifact?

A lineage may include:

- body prose;
- tables and matrices;
- headings;
- figure and table captions;
- introductions;
- summaries;
- conclusions;
- executive summaries.

Claim Type and Claim Lineage are different dimensions.

Example:

```text
Claim Type: Research
Authoritative claim: The skill-mapping method achieved F1 = 0.92 on the frozen test set.
Claim Lineage:
- experiment paragraph
- result table
- chapter summary
- final conclusion
```

A local correction is incomplete until all material lineage occurrences preserve the same scope and evidence boundary.

---

## 3. Evidence Profile

An Evidence Profile records what supports a Claim Record and what the evidence can actually prove.

Minimum fields:

```text
Evidence source:
Source authority:
Evidence type:
Evidence state:
Direct fact or inference:
Stable or transient:
Protocol / environment / version:
Supported scope:
Unsupported extension:
Delegated target, if any:
Evidence-pointer quality:
Conflict or uncertainty:
```

### Evidence type

Use these evidence types:

- Requirement or policy
- Design
- Code or schema
- Automated test
- Runtime
- Experiment
- Application
- External authority

Claim-type-specific fields are defined in `claim-evidence-contracts.md`.

### Evidence state

Use these evidence states:

- **Traceable**
- **Present but unlinked**
- **Not found in inspected scope**
- **Inaccessible**
- **Confirmed absent**
- **Conflicting**

Evidence type and evidence state are independent.

---

## 4. Narrative Decision

A Narrative Decision determines what happens to a claim or source fact in the artifact.

Allowed primary treatments:

- **Keep** — retain as supported, relevant, necessary, and correctly placed.
- **Substantiate** — connect or obtain the required evidence.
- **Narrow** — reduce the claim to the supported scope.
- **Reframe** — preserve the fact but express its project or reader meaning.
- **Move** — relocate to another section, appendix, evidence package, or internal record.
- **Compress** — retain only the minimum necessary qualification.
- **Restructure** — change the argument or section organization.
- **Delete** — remove from the formal artifact.

A secondary action may preserve evidence or define follow-up work, but the primary treatment must state what happens to the formal artifact now.

Every Narrative Decision should record:

```text
Primary treatment:
Destination:
Reason:
Secondary evidence action, if any:
Affected Claim Lineage:
```

---

## 5. Boundary Record

Create a Boundary Record only when a limitation, uncertainty, incomplete state, or scope restriction must remain to keep a claim accurate.

Minimum fields:

```text
Claim affected:
Boundary:
Why omission would mislead:
Minimum wording:
Authoritative home:
Other lineage occurrences to narrow or cross-reference:
```

A necessary boundary should be authoritative, not ubiquitous.

Do not create Boundary Records for every internal defect. A negative fact must first pass the Claim Necessity Test in `decision-rules.md`.

---

## 6. Relationship among the five objects

```text
Artifact Brief
  -> identifies the reader decision and primary contribution
  -> creates Claim Records

Claim Record
  -> selects the proof obligation by Claim Type
  -> links all restatements through Claim Lineage
  -> receives one or more Evidence Profiles

Evidence Profile
  -> establishes supported scope and uncertainty
  -> informs the Narrative Decision

Narrative Decision
  -> determines wording, placement, evidence follow-up, or deletion
  -> may create a Boundary Record

Boundary Record
  -> preserves the minimum necessary limitation
  -> controls all related Claim Lineage occurrences
```

---

## 7. Role separation

The five working roles use the model differently:

| Role | Primary object |
|---|---|
| Investigator | Evidence Profile |
| Analyst | Claim Record + Evidence Profile |
| Editor | Artifact Brief + Narrative Decision |
| Writer | Approved Claim Records + Narrative Decisions |
| Auditor | All five objects, checked independently |

Working objects are internal unless the user explicitly requests an evidence matrix, audit report, or acceptance contract.

---

## 8. Core invariants

1. Artifact purpose outranks source structure.
2. Claim Type determines proof obligation.
3. Claim Lineage controls consistency across surfaces.
4. Evidence remains within its proof boundary.
5. Observer uncertainty is not project failure.
6. Strong state language must carry scope.
7. Internal identifiers require semantic projection before ordinary prose.
8. Negative facts enter the artifact only when necessary to preserve accuracy.
9. Primary contribution follows title, rubric, adopted scope, and owner intent.
10. Strategic decisions remain human-owned.
