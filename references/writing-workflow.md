# Writing Workflow

## Purpose

Produce formal project prose from evidence without allowing repository structure, internal work artifacts, or incomplete proof to determine the narrative.

This workflow applies the objects defined in `core-model.md`.

---

## Phase 0 — Route the task

Determine:

- Writing mode depth: Lite, Standard, or Deep;
- artifact type and audience;
- whether the task contains Research, Engineering, Product/Application, or mixed claims;
- which conditional references are required.

Do not load every reference by default.

---

## Phase 1 — Establish the Artifact Brief

Record the Artifact Brief internally.

For whole-document or chapter-level work, also verify:

- primary contribution;
- section responsibility;
- upstream and downstream dependency;
- whether the adopted outline is authoritative;
- whether title, rubric, and owner intent agree.

Use `document-architecture.md` when these questions are material.

Do not inspect the repository broadly before the brief is clear enough to guide retrieval.

---

## Phase 2 — Build Claim Records

Write a small set of intended claims before collecting evidence broadly.

For each material claim:

1. state what the reader should conclude;
2. assign Claim Type;
3. identify scope and any strong state word;
4. identify required proof;
5. record known Claim Lineage surfaces.

Split compound claims when research, engineering, or product proof obligations differ.

A heading is not a claim. “Backend architecture” is a topic; “long-running tasks can resume after process restart because task identity and dependency state are persisted” is a claim.

---

## Phase 3 — Build Evidence Profiles

Retrieve only evidence required by the Claim Records.

For each claim:

1. select the applicable contract from `claim-evidence-contracts.md`;
2. inspect canonical sources in authority order;
3. record evidence type and evidence state;
4. distinguish direct fact from inference;
5. record supported scope and unsupported extension;
6. verify delegated proof and pointer quality when relevant;
7. identify conflict or uncertainty without resolving it silently.

For Research claims, explicitly separate plan, acceptance target, measured result, and validated conclusion.

For Engineering claims, identify actor, condition, action, state/data effect, output, failure boundary, and verification.

For Product/Application claims, distinguish expected value from observed outcome.

---

## Phase 4 — Make Narrative Decisions

Apply `decision-rules.md`.

For each candidate claim or source fact:

- pass the admission gates;
- select Keep, Substantiate, Narrow, Reframe, Move, Compress, Restructure, or Delete;
- choose the destination;
- create a Boundary Record only when omission would mislead;
- assign one authoritative home to each required boundary.

At this phase, decide document structure from reader reasoning—not source order.

Use `document-architecture.md` when the route, chapter balance, primary contribution, or representation is in question.

---

## Phase 5 — Draft the reader-facing artifact

Write only from approved Claim Records, Evidence Profiles, Narrative Decisions, and Boundary Records.

Use `narrative-projection.md` to ensure:

- concrete subjects and referents;
- the nearest semantic owner normally serves as the grammatical subject;
- project-wide wrappers such as “本项目 / 本文 / the project / we” are reserved for genuine framing, ownership, scope, or synthesis rather than repeated paragraph openings;
- project terminology before code identifiers;
- meaningful transitions;
- visible structure shaped by the subject, not the internal checklist;
- no leakage of evidence ledgers, audit instructions, TODOs, or source-search limitations.

Preferred explanatory movement:

`problem -> constraint -> mechanism or method -> evidence -> conclusion or boundary`

The exact structure should vary with the subject.

Do not de-template prose by rotating synonyms for the same global subject. If “本项目 / 本文 / 本研究 / 系统” repeatedly occupy the same grammatical role, restore the actual method, process, actor, or data object as the semantic owner where appropriate.

---

## Phase 6 — Reconcile and audit

Before finalizing:

1. recheck each Claim Type against its proof contract;
2. verify strong-state scope;
3. verify delegated proof;
4. search all Claim Lineage surfaces;
5. confirm required boundaries remain in their authoritative homes;
6. check terminology, referential clarity, and semantic subject ownership;
7. confirm primary contribution has not been displaced;
8. remove source, debugging, and authoring-process residue;
9. ensure no target is written as a result and no engineering evidence is presented as research performance.

Use `audit-workflow.md` for a deep final pass.

---

## Internal working templates

### Artifact Brief

Use the canonical fields in `core-model.md`.

### Claim Record

```text
Claim ID:
Claim:
Claim Type:
Object and scope:
Required proof:
Strong-state scope, if any:
Claim Lineage:
```

### Evidence Profile

```text
Source:
Authority:
Evidence type:
Evidence state:
Direct fact or inference:
Supported scope:
Unsupported extension:
Delegated proof:
Pointer quality:
Conflict:
```

### Narrative Decision

```text
Primary treatment:
Destination:
Reason:
Secondary evidence action:
Affected lineage:
```

### Boundary Record

Use only when required by the Claim Necessity Test.

---

## Writing completion gate

A writing task is complete when:

- the Artifact Brief is clear enough for the requested scope;
- every material claim has a Claim Type and suitable evidence contract;
- evidence type and evidence state remain distinct;
- plan, target, result, and conclusion are not conflated;
- material metrics have an admissible measurement design;
- engineering mechanisms identify agency and behavior at the required depth;
- Product/Application claims distinguish expected value from observed outcome;
- strong state words carry supported scope;
- delegated proof is valid or explicitly unresolved outside the artifact;
- Claim Lineage occurrences are consistent;
- primary contribution remains aligned with title, rubric, scope, and owner intent;
- reader-facing prose uses specific semantic owners where available instead of saturating paragraphs with project-wide subjects;
- reader-facing prose is free of internal ontology and drafting residue;
- necessary boundaries remain once, in the correct place.

---

## Stop conditions

Use the stop conditions in `SKILL.md`.

Do not stop merely because current results are unavailable in a proposal. Define a valid acceptance contract when the project owner or rubric provides the necessary basis.
