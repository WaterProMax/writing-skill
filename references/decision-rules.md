# Decision Rules

## Purpose

This file is the single source of truth for evidence judgment, claim scope, delegated proof, disclosure, severity, and treatment.

It applies to both Writing and Governance modes.

---

## 1. Evidence type and proof boundary

| Evidence type | Can support | Cannot support by itself |
|---|---|---|
| Requirement or policy | Intended behavior, obligation, scope, constraint | Implementation or effectiveness |
| Design | Intended architecture or mechanism | Running behavior |
| Code or schema | Existence and shape of implementation | Runtime success or quality |
| Automated test | Behavior under defined test conditions | General user journey or real-world value |
| Runtime | Execution under stated environment and input | Generalized algorithm performance |
| Experiment | Performance under a defined protocol | System integration or production readiness |
| Application | Observed outcome in a real use context | Universal validity outside that context |
| External authority | Industry, policy, scientific, or standard fact within source scope | Project-specific implementation or performance |

Never silently promote one evidence type into a stronger conclusion.

---

## 2. Evidence-state taxonomy

| State | Meaning | Allowed judgment |
|---|---|---|
| **Traceable** | Appropriate evidence is present and directly locatable | Evaluate supported scope |
| **Present but unlinked** | Evidence appears to exist but is not connected to the claim | Repair traceability; do not call the claim false automatically |
| **Not found in inspected scope** | The current search did not locate sufficient evidence | Report search limitation outside the artifact; continue targeted retrieval |
| **Inaccessible** | Evidence may exist but cannot currently be inspected | State auditor limitation; do not convert it into project failure |
| **Confirmed absent** | Authoritative scope or owner confirms the required evidence does not exist | Narrow, omit, or obtain evidence before restoring the stronger claim |
| **Conflicting** | Authoritative sources disagree materially | Resolve, escalate, or narrow before stronger prose |

Never promote:

`not found -> confirmed absent`

or:

`inaccessible -> unsupported`

without additional basis.

---

## 3. Strong-state scope

High-strength words include:

- complete
- implemented
- validated
- verified
- integrated
- closed-loop
- available
- deployed
- official
- mature
- ready
- production-ready

Normalize every material use as:

`state word + object + layer/scope + evidence level + material boundary`

Relevant scopes include:

- architecture definition;
- implementation existence;
- runtime path;
- representative scenario;
- user-facing end-to-end journey;
- experiment coverage;
- application context;
- deployment;
- production readiness.

If a reasonable reader could infer a stronger scope than the evidence supports, narrow the sentence rather than appending defensive caveats.

---

## 4. Delegated-proof integrity

When a claim delegates proof to another chapter, table, figure, appendix, report, evidence package, or external source, verify:

1. target existence;
2. target identity and adopted version;
3. temporal consistency;
4. responsibility fit;
5. scope fit;
6. conflict state;
7. reader-accessible path.

Reference states:

- **Valid delegation**
- **Partial delegation**
- **Unresolved delegation**
- **Broken delegation**
- **Conflicting delegation**
- **Stale delegation**

A reference transfers proof responsibility; it does not discharge it.

---

## 5. Evidence-pointer quality

A pointer carrying formal proof responsibility should be:

- **Resolvable**
- **Stable**
- **Contextualized**
- **Interpretable**
- **Authority-compatible**

Examples:

| Pointer | Typical use |
|---|---|
| Versioned experiment report with protocol and results | Formal evidence |
| Evidence-index entry resolving to logs/results | Formal evidence |
| Persistent read-only runtime receipt with context | Potentially formal evidence |
| Raw task UUID without resolver | Investigator locator only |
| Screenshot filename without provenance | Weak pointer |
| Temporary URL or local path | Internal or reproducibility-only pointer |

Evidence may be present while the pointer remains inadequate.

---

## 6. Claim-Lineage consistency

For each material Claim Lineage:

1. establish the authoritative claim;
2. identify semantic anchors such as object, state, metric, outcome, and scope;
3. search all claim-bearing surfaces;
4. compare every occurrence with the authoritative form;
5. narrow, split, or substantiate inconsistent occurrences;
6. repeat the sweep after summaries, captions, or tables change.

Do not collapse:

- declared capability into observed execution;
- one run into general validation;
- implementation into user-journey completion;
- local validation into deployment;
- acceptance target into measured result.

Each table cell, caption, heading, and summary can mislead independently.

---

## 7. Main-text admission control

A source fact enters the main narrative only when it passes all four gates:

1. **Truth**
2. **Relevance**
3. **Audience value**
4. **Section responsibility**

Then choose the correct destination:

| Destination | Appropriate content |
|---|---|
| Main narrative | Stable facts necessary to establish the section’s claims |
| Table or figure | Structured relationships that reduce reasoning cost |
| Appendix or reproducibility note | Protocols, commands, versions, exact configurations |
| Evidence index | Raw results, logs, screenshots, receipts |
| Internal record | Debugging detail, unresolved conflicts, rejected evidence |

Being true is necessary but not sufficient for publication.

---

## 8. Stable and transient facts

Prefer stable project truth in formal prose:

- problem and scope;
- approved terminology;
- research method;
- system mechanism;
- measured result;
- enduring boundary.

Treat these as transient by default:

- commit hashes;
- one-time dates;
- task or run IDs;
- warning counts;
- local environment variables;
- temporary routes;
- fixtures, mocks, or seeds;
- one-run failures.

Transient detail may belong in reproducibility or evidence records when it materially supports a claim.

---

## 9. Claim Necessity Test

Before retaining a negative or incomplete fact, ask:

1. Which explicit claim does it qualify?
2. Without it, would a reasonable reader infer a stronger capability?
3. Is the affected capability required by the artifact, rubric, or section responsibility?
4. Can the positive claim be narrowed safely?
5. If the boundary remains necessary, where should it live?
6. What is the minimum neutral wording?

Decision:

| Condition | Treatment |
|---|---|
| No affected claim, no stronger implication, no evaluation obligation | Keep the defect outside the main narrative |
| A narrower positive claim is fully supported | Narrow the claim; move defect detail |
| Omission would materially mislead | Create a Boundary Record |
| Genre is a readiness/defect report | Report the relevant defect at the requested depth |
| Detail is needed only for reproducibility | Move detail; keep the main conclusion concise |

Do not conceal a boundary necessary for accuracy. Do not publish an internal defect merely because it is true.

### 子系统局限性备忘录

Use this subsection when the artifact is a boundary or limitations memo for one directory or one toolchain inside a larger repository. Depth is **Scoped** (`SKILL.md`). Do not enter Mode 1. Do not create `01`–`07`.

1. **File whitelist first.** List the files that may support a sentence. Adjacent code may be opened only to answer “would this mis-attribute A’s tech to B?”. Do not grow a second product chapter from that read.
2. **One row per entrypoint.** Each row states process shape (CLI, batch, or listen), default flags, write targets, and gates. A listen shape requires `ListenAndServe` or an equivalent bind (`code-verification-workflow.md`, 偏差 5).
3. **Do not merge dry-run defaults across entrypoints.** If two commands default `-dry-run` differently, or one entrypoint bypasses dry-run, keep them on separate rows. A merged sentence such as “the tool defaults to dry-run” is a false Engineering claim.
4. **One Boundary section.** Concentrate can-write / cannot-write in a single section a reader can find as 「可以写 / 不能写」. Entrypoint sections keep a narrow positive sentence and point here. Do not repeat the defect inventory in every section (§10).
5. **Experiment scores default to Delete.** Keep a score only when this section’s Claim Type is **Research** and the Research contract is complete (task, reference truth, protocol, rationale, comparator, interpretation). A score from an adjacent experiment is not this module’s product metric.
6. **Infrastructure defaults.** In formal prose, cite the source line number and the category (loopback / public address / empty DSN). Do not copy host, IP, secret, or JDBC URL into the body. The same rule covers passwords and connection strings. Java property names are not physical columns without `@TableField`. These code-fact red lines live in `code-verification-workflow.md` and do not require the Mode 1 workflow.
7. **Search scope is not product failure.** “This search found no reader” states the observation scope. Do not write it as a product failure (see §11: auditor-access limitation versus project-level absence).

**Competition-style yield.** When the chapter’s job is Boundary, do not use “name all three RAG layers / drop hedges such as 试图 or 尝试 / retitle as capability marketing” to widen claims. 偏差 4 and this subsection outrank `code-verification-workflow.md`（特殊处理：比赛文档）. That competition section applies only when the chapter’s job is a capability statement.

---

## 10. Boundary placement

Every material Boundary Record should have one authoritative home.

Other sections should:

- state the narrower positive claim that is correct there;
- cross-reference the authoritative boundary when local understanding requires it;
- avoid repeating the full defect inventory.

Necessary disclosure should be authoritative, not ubiquitous.

---

## 11. Severity

Assign severity after root-cause and materiality analysis.

Evaluate:

- correctness impact;
- trust impact;
- reader decision impact;
- scope and salience;
- repair depth.

### P0 — Material correctness or trust failure

Examples:

- false performance or completion claim;
- research/engineering evidence substitution;
- target presented as result;
- hidden authoritative conflict;
- misleading omission of a necessary boundary;
- auditor-access limitation rewritten as project failure.

### P1 — Structural or argumentative failure

Examples:

- chapter-role drift;
- primary contribution displaced;
- repo-first organization;
- repeated abstraction mixing;
- important evidence present but unlinked;
- internal ontology replacing project ontology;
- repeated boundary exposure distorting the project story.

### P2 — Local expression or density defect

Examples:

- isolated ambiguous referent;
- local terminology drift;
- unnecessary identifier density;
- repeated transition;
- minor AI-writing fingerprint that does not alter the conclusion.

Category alone never determines severity.

---

## 12. Treatment selection

Allowed primary treatments are defined in `core-model.md`.

Common compound actions:

| Primary | Secondary | Use |
|---|---|---|
| Compress | Move | Keep a minimum boundary; preserve detail elsewhere |
| Narrow | Substantiate | Reduce the claim now; gather stronger evidence later |
| Reframe | Move | Express project meaning; relocate source identifiers |
| Keep | Substantiate | Claim is appropriate; evidence connection needs repair |
| Delete | Move | Remove residue while preserving internal history |

---

## 13. Decision sequence

Use this order:

```text
identify claim
-> determine Claim Type
-> identify required evidence
-> classify evidence type
-> classify evidence state
-> determine supported scope
-> verify delegated proof and pointer quality
-> reconcile Claim Lineage
-> test admission and disclosure necessity
-> choose Boundary Record if required
-> assess materiality
-> select Narrative Decision
```

Do not assign severity from a keyword and justify it afterward.
