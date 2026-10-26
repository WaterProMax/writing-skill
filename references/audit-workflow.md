# Audit Workflow

## Purpose

Audit a completed or partial formal artifact before rewriting it.

The audit evaluates project claims, evidence, argument structure, and narrative projection—not the effort of the writer.

---

## Pass 0 — Reconstruct the Artifact Brief

Determine:

- artifact type;
- audience;
- reader decision;
- title, rubric, and adopted scope;
- primary contribution;
- chapter and section responsibilities;
- canonical sources;
- expected proof standard;
- requested audit depth.

If these materially conflict, record the conflict before judging prose.

---

## Pass 1 — Audit architecture and responsibility

Check:

- whether the document forms an argument rather than an asset catalog;
- whether primary contribution follows title, rubric, scope, and owner intent;
- whether chapter responsibilities are distinct;
- whether dependencies among problem, requirement, research, engineering, and application are explicit;
- whether downstream applications have displaced the central contribution;
- whether figures and tables reduce reasoning cost and carry appropriate evidence.

Use `document-architecture.md`.

---

## Pass 2 — Inventory Claim Records

Extract material claims and assign:

- Claim Type;
- object and scope;
- strong state, if any;
- section responsibility;
- known Claim Lineage surfaces.

Split compound claims.

Search especially for claims in:

- headings;
- table cells;
- captions;
- chapter introductions;
- summaries;
- conclusions.

Do not assume a qualification in one paragraph controls a broader standalone table or summary elsewhere.

---

## Pass 3 — Audit Evidence Profiles

For each material claim:

1. identify required proof from `claim-evidence-contracts.md`;
2. classify evidence type;
3. classify evidence state;
4. determine supported scope;
5. identify prohibited substitution;
6. verify delegated targets and pointer quality;
7. distinguish plan, target, result, and conclusion;
8. apply Metric Admissibility to research metrics;
9. distinguish expected Product/Application value from observed outcome.

High-risk failures include:

- code or runtime evidence used as algorithm performance;
- metrics used as engineering completion;
- target written as result;
- screenshot used as validity evidence;
- one run generalized without protocol;
- orphan metric;
- title-level contribution lacking a proof route.

---

## Pass 4 — Audit narrative projection

Use `narrative-projection.md`.

Check for:

- ambiguous “this/that/the above/the function/the chain” references;
- missing actors in engineering actions;
- grammatical subjects that do not match the nearest semantic owner;
- repeated project-wide subjects such as “本项目 / 本文 / 本研究 / 系统 / we / the project” at paragraph openings when a more specific method, process, actor, or data object exists;
- lexical synonym rotation that hides the same global-subject saturation rather than fixing semantic ownership;
- code constants or repository terms replacing project concepts;
- Q/R labels used as ordinary nouns;
- unnecessary English tokens in reader-facing prose;
- mechanical subsection symmetry;
- repeated conclusion formulas;
- transitions that provide glue but not logic;
- evidence-audit caveats or authoring instructions leaking into the artifact;
- paragraph-level abstraction jumps.

Treat these as projection failures first, not as isolated word-choice defects.

A repeated global subject is not automatically a defect. Flag it only when it masks a more informative semantic owner, flattens paragraph responsibility, or creates template-shaped rhythm. Use **Semantic-projection failure** as the root cause rather than inventing a lexical-repetition category.

---

## Pass 5 — Audit disclosure and Claim Lineage

Apply `decision-rules.md`.

For each negative or incomplete fact:

- identify the claim it qualifies;
- run the Claim Necessity Test;
- preserve a Boundary Record only when omission would mislead;
- choose one authoritative home;
- remove repeated defect inventories.

For each Claim Lineage:

- establish the authoritative form;
- compare all occurrences;
- repair broader summaries, captions, tables, or conclusions;
- recheck after edits.

---

## Pass 6 — Assign treatment and severity

For each material issue, record:

```text
Location:
Excerpt:
Affected claim:
Claim Type:
Evidence state:
Root cause:
Reader impact:
Primary treatment:
Secondary evidence action:
Affected Claim Lineage:
Boundary to preserve, if any:
Owner decision required, if any:
```

Assign P0/P1/P2 only after materiality analysis.

### Root-cause categories

Use the smallest useful set:

- Source gravity
- Coverage pressure
- Completion pressure
- Proof substitution
- Evidence-state overreach
- Section-role drift
- Primary-contribution displacement
- Semantic-projection failure
- Referential-integrity failure
- Claim-Lineage propagation failure
- Disclosure failure
- Decision-authority overreach

Do not create a new root-cause category for every surface symptom.

---

## Recommended output

Lead with an overall judgment, then use a concise issue table:

| Priority | Location | Claim Type | Root cause | Why it matters | Primary treatment | Evidence follow-up |
|---|---|---|---|---|---|---|

Add detail only where it changes the decision.

After the table, provide:

1. the few root causes responsible for most defects;
2. repair order;
3. boundaries that must survive repair and their authoritative homes;
4. owner decisions required;
5. evidence still needed for stronger claims;
6. unresolved delegated proof or source conflicts.

---

## Repair order

1. Correct false or materially unsupported claims.
2. Separate Research, Engineering, and Product/Application proof obligations.
3. Resolve target/result and expected/observed conflation.
4. Verify delegated proof and source conflicts.
5. Restore primary contribution and chapter responsibilities.
6. Reconcile material Claim Lineages.
7. Preserve required boundaries and remove repeated defect inventories.
8. Repair semantic projection, actors, semantic subject ownership, referents, terminology, and section structure.
9. Move source and reproducibility residue.
10. Polish language only after the structure is valid.

---

## Audit completion gate

Governance is complete when:

- every P0 issue is repaired or escalated;
- all material claims have a Claim Type and evidence judgment;
- evidence state is not rewritten as project failure;
- proof substitution is removed;
- plan, target, result, and conclusion are distinct;
- material metrics have valid contracts;
- Product/Application outcomes are not inferred from capability alone;
- delegated proof is valid or explicitly unresolved;
- primary contribution remains central;
- material Claim Lineages are consistent;
- necessary boundaries remain in one authoritative home;
- section responsibilities are restored;
- semantic projection assigns actions and claims to informative semantic owners rather than repeated global wrappers when possible;
- semantic projection no longer exposes internal ontology or drafting process;
- severity reflects reader impact rather than trigger words.
