---
name: writing-skill
description: Use when generating a structured codebase knowledge base, drafting or revising formal project, competition, research, architecture, or engineering documents from repositories and evidence, writing a limitations or boundary memo for one directory or toolchain without a whole-repo knowledge base, or verifying and auditing technical documents against source code and evidence contracts. Unified integration of codebase-knowledge-base-generation, project-document-evidence-governance, and technical-doc-code-verification.
---

# Unified Technical Writing, Knowledge Base & Evidence Governance (`writing-skill`)

## Purpose

Transform multi-module repositories, experiments, runtime records, and internal evidence into structured knowledge bases, formal audience-facing documents, or code-verified revisions.

Three governing rules:

> **1. Evidence is truth, not narrative.** Repo folders and KB files (`01`..`07`) supply verifiable facts, never the outline of a formal document.
> **2. Research, engineering, and product claims carry distinct proof obligations.**
> **3. Verify every technical assertion line-by-line against source code; revisions must be drop-in replacement text.**

The unified transformation for a **whole-repo** pass (Mode 4) is:

`codebase -> structured knowledge base (7+1) -> artifact brief -> claim record -> evidence profile -> narrative decision -> reader-facing artifact -> code & lineage verification`

**Stop at Scoped** when the deliverable is a boundary or limitations memo for **one directory or one toolchain**, and the user explicitly does not want a whole-repo knowledge base. That task is Mode 2, not this chain: do not enter Mode 1, and do not create `01`–`07`. See **Depth routing**.

Use `references/core-model.md` as the terminology source of truth.

---

## Operating modes

### Mode 1 — Knowledge-Base Generation (`codebase-knowledge-base-generation`)

Use when exploring a multi-module codebase to generate a reusable local Investigator index (default `docs/knowledge-base/`). Mode 1 output is **not** a second Canonical Wiki: `canonical_for` stays empty; if the target repo already has a Wiki, the index opening must point to it and declare non-replacement.

**Mode 1 reading set only** (do **not** load Deep-route references):
- `references/codebase-knowledge-base-workflow.md` (required)
- `references/core-model.md` — the five canonical objects only
- `references/decision-rules.md` — **§9 Claim Necessity Test** only
- Leave `examples.md` / `document-architecture.md` / `audit-workflow.md` for Mode 2/3

**Conflict priority** (one line, always):
`running code > Flyway/entities > generated OpenAPI > Wiki non-canonical prose > test notes > experiment directories`

**Red lines** (never violate). The four code-fact rules (listen, empty Controller, secrets and connection strings, Java property ≠ physical column) are **shared with Mode 2 and Mode 3**. Those modes load them from `references/code-verification-workflow.md` and do not enter Mode 1 to reach them.
- No passwords, connection strings, test-account secrets, or full JDBC URLs; no template percentages as metrics
- Do not call a CLI/batch a listening HTTP service without `ListenAndServe`/port bind; empty Controllers (0 handler methods) are **not** APIs
- Keep Java properties separate from physical columns (without `@TableField`, do not invent snake_case)
- Scan annotations/entries (`@RestController`/`@RequestMapping`/`go.mod`) repo-wide first, then split by directory ownership into **主产品进程** vs **独立工具/采集进程（如 `tools/**`）**. The `tools/**` path is an illustrative tree, not a required layout.
- Frontend API extraction must follow this repository's own local wrapper functions (e.g., custom wrapper functions such as `apiClient` / `request` / `schoolFetch`) in addition to raw `fetch(`/axios; unfollowed wrappers go to `未覆盖`, never “前端无某模块 API”. Those three names are examples of wrappers, not a required client API.
- Every static symbol table (Controller, entity, frontend API table) must open with: `本表仅证明符号/映射在源码中存在，不代表方法体分支、鉴权或运行时业务契约已验证`

Execute the 5-stage pipeline (details in the Mode 1 workflow):
1. **Stage 1 (Explore, <=5 min)**: map 2-level dirs, ownership, modules, configs, docs; line counts from **this run's** `wc`/tools only.
2. **Stage 2 (Parallel Background Agents)**: coverage declaration (enumerated symbols, files read, unread files; unread paths never in behavior prose). Scan repo-wide then split main product vs independent tool processes (e.g. a `tools/**` tree); follow this repository's frontend request wrappers.
3. **Stage 3 (Sync Core Read)**: read governance entry (`AGENTS.md` / Wiki map) first; apply **inventory invalidation** (missing → new path or Boundary; never treat a same-name history tree as current, e.g. `legacy-designs`). Spot-check issue status by **opening named source files** (note no process re-run); if unopened, write `未打开源码核对（仅保留手记原词）`.
4. **Stage 4 (`7 + 1` Output)**: `HOME.md` + `01`..`07` with symbol-table non-runtime disclaimers, verbatim issue statuses, and HOME modules derived from this repository's code or Wiki (never hard-code module names from another project; illustrative anti-pattern only: “用户系统/画像/简历”).
5. **Stage 5**: before background agents return, place `占位：后台探索尚未回传，以下仅为主会话已核对范围。` under `阶段 5 增补`; on return, delete the placeholder and merge only main-session-verified facts (never paste sub-agent default hosts/secrets, comment-inferred columns, or unverified method behavior).

### Mode 2 — Evidence-Governed Writing (`project-document-evidence-governance` Writing Mode)

Use when drafting, rewriting, extending, or updating a formal artifact (competition proposal, research paper, architecture whitepaper, engineering document, or a Scoped boundary/limitations memo for one directory or toolchain).

Always read:
- `references/core-model.md`
- `references/writing-workflow.md`

Load conditionally:
- `references/claim-evidence-contracts.md` for material research, engineering, product, performance, validation, or acceptance claims;
- `references/decision-rules.md` when evidence is incomplete, conflicting, delegated, scope-sensitive, limitation-bearing, or spread across multiple surfaces;
- `references/narrative-projection.md` when producing or repairing reader-facing prose;
- `references/document-architecture.md` for whole-document structure, chapter responsibility, title/rubric alignment, or cross-layer argument design;
- `references/code-verification-workflow.md` when embedding concrete code/table/API facts, writing a Scoped limitations memo, or competition-specific descriptions. This file holds the **Mode 2/3 code-fact red lines** (listen / empty Controller / secrets and connection strings / Java property ≠ physical column, plus 偏差 5). Do not load the Mode 1 workflow to reach them;
- `references/examples.md` only when concrete failure signatures or rewrite patterns are useful.

### Mode 3 — Code Verification & Governance Audit (`technical-doc-code-verification` + Governance Mode)

Use when verifying technical descriptions against actual source code, auditing claim-evidence alignment, or cleaning/repairing an existing artifact.

Always read:
- `references/core-model.md`
- `references/audit-workflow.md`
- `references/code-verification-workflow.md`

Load the conditional references from Mode 2 according to the issue under review. Do not load the full reference set mechanically.
- **Line-by-Line Verification (5 Steps)**: Split into atomic assertions -> query KB then read source -> separate online main chains from offline/auxiliary tools -> classify (`Exact match` / `Minor polish` / `Architecture misattribution` / `Exaggerated claim`) -> output `(1) quote, (2) file + lines, (3) drop-in replacement paragraph`.
- **5 Common Code Deviations**: (1) Cross-system tech misattribution (e.g., RAG/ChromaDB); (2) Omitted state enums/steps; (3) Sync claim vs async return (`reportStatus: "pending"`); (4) AI boundary exaggeration (ignoring engineering gates/validators); (5) Batch CLI client written as a long-lived HTTP service (needs `ListenAndServe` or an equivalent bind — not a directory name, a `net/http` import, or an unreferenced URL config).

### Mode 4 — End-to-End Pipeline (KB -> Governed Writing -> Code & Lineage Audit)

Do not start Mode 4 when **Scoped** applies (one directory or toolchain; user refused a whole-repo knowledge base).

1. Build or consult the `7 + 1` Knowledge Base (`references/codebase-knowledge-base-workflow.md`) as the Investigator fact store.
2. Draft the reader-facing artifact via `references/writing-workflow.md` without letting `01`..`07` file structure or `ISSUES.md` defect lists become the narrative outline.
3. Verify all technical assertions via `references/code-verification-workflow.md` and reconcile all Claim Lineages via `references/audit-workflow.md`.

---

## Depth routing

Choose the lightest route that preserves correctness.

| Depth | Use when | Typical references |
|---|---|---|
| **Scoped** | Boundary or limitations for **one directory or one toolchain**, and the user explicitly does **not** want a whole-repo knowledge base | **Stop here.** Mode 2 only. Do **not** enter Mode 1. Do **not** create `HOME.md` or `01`–`07`. First write a file whitelist. Adjacent code may answer only “would this mis-attribute A’s tech to B?”. Read `core-model.md`, `writing-workflow.md`, `decision-rules.md` §9（子系统局限性备忘录）, and `code-verification-workflow.md` code-fact red lines（含偏差 5）. Do **not** load `codebase-knowledge-base-workflow.md`, `document-architecture.md`, or `examples.md`. Words such as 比赛 / 申报 do **not** promote this task to Deep. |
| **Lite** | Local paragraph repair or single-passage code verification; source authority and claim are clear | `core-model.md` + mode workflow + `narrative-projection.md` / `code-verification-workflow.md` |
| **Standard** | Substantive section, one material claim lineage, module KB extraction, or research/engineering/product explanation | Lite set + `claim-evidence-contracts.md` + `decision-rules.md` as needed |
| **Deep** | Whole-document architecture, multi-source reconciliation, a competition proposal whose chapter job is capability (not a single-subsystem Boundary), or final audit (Mode 2/3/4) | Standard set + `document-architecture.md` + `examples.md` (+ audit/code-verification as needed) |

**Scoped stop conditions** (apply before Mode 1, Mode 4, or Deep):

1. Deliverable is boundary/limitations, scope is one directory or one toolchain, and the user has refused a whole-repo knowledge base.
2. Do not build the `7+1` index “first so the memo has evidence.” Evidence is the whitelist plus opened lines in those files.
3. Do not describe that CLI or batch client as a listening service without a bind. That check is 偏差 5 in `code-verification-workflow.md`, not a Mode 1 stage.

Mode 1 uses its own reading set above — **never** expand Mode 1 into the Deep reference table. Scoped does not enter Mode 1.
Do not turn a local edit into a full governance exercise without a material reason.

---

## Required operating model

For substantive work, keep five roles distinct even when one agent performs all of them:

1. **Investigator** — builds/queries the knowledge base, inspects source code, and records source authority.
2. **Analyst** — determines `Claim Type`, code-truth alignment, proof obligation, and supported scope.
3. **Editor** — decides what belongs in the artifact and where (`Narrative Decision`, `Boundary Record`).
4. **Writer** — writes only from approved claims and evidence profiles.
5. **Auditor** — checks the completed artifact independently against source code and governance rules.

Repository inspection and final prose generation must not collapse into one undifferentiated pass.

---

## Core execution route

1. Establish the **Artifact Brief** (or execute the 5-stage KB workflow in Mode 1).
2. Create the material **Claim Records** and distinguish **Claim Type** from **Claim Lineage**.
3. Build the appropriate **Evidence Profile** for each claim (backed by code/KB/experiments).
4. Choose a **Narrative Decision** for each claim and source fact.
5. Create a **Boundary Record** only when a limitation must remain to keep a claim accurate.
6. Draft or repair the artifact at the reader's abstraction level.
7. Reconcile each material claim lineage and code assertion across prose, tables, figures, captions, summaries, and conclusions.

The five objects above are defined only in `references/core-model.md`.

---

## Non-negotiable invariants

- **Source conflict order**: `running code > Flyway/entities > generated OpenAPI > Wiki non-canonical prose > test notes > experiment directories`.
- Start from reader need, artifact purpose, and section role—not repo folders or KB numbering (`01`..`07`, which is an Investigator index layout, never a formal outline).
- Route every material claim to **Research**, **Engineering**, or **Product/Application** before judging evidence.
- Verify every concrete technical description (class/table/field names, state enums, sync/async flows, AI vs engineering gates) against actual source code; never rely on memory.
- Keep evidence type separate from evidence state.
- Do not use code, tests, fixtures, runtime traces, or screenshots to prove algorithmic performance.
- Do not use model metrics to prove orchestration, persistence, recovery, integration, deployment, or user-facing completion.
- Keep plan, acceptance target, measured result, and validated conclusion distinct.
- Require a valid task, reference truth, protocol, rationale, comparator, and interpretation before admitting a material metric.
- Bind strong words such as "complete", "validated", "integrated", or "production-ready" to an explicit object, layer, evidence level, and boundary.
- Verify any chapter, table, appendix, report, or evidence package that carries delegated proof responsibility.
- Use project concepts in ordinary prose; preserve exact code identifiers (`table_name` without quotes, `STATE_ENUM`) only where exact strings matter.
- Treat Q/R labels, task IDs, and stage numbers as navigation aids, not project concepts.
- Name concrete actors, objects, and conditions when describing engineering actions.
- Use the nearest semantic owner as the grammatical subject when one exists; reserve project-wide wrappers such as "本项目 / 本文 / 本研究 / 系统 / we / the project" for genuine framing, ownership, scope, or synthesis, and never mask global-subject saturation via synonym rotation.
- Keep necessary limitations accurate but give each material boundary one deliberate authoritative home.
- In competition prose whose chapter job is a **capability**, explicitly name multi-layer technical mechanisms (e.g., Retrieval/Augmented/Generation), avoid hedging ("试图/尝试"), never overclaim AI boundaries, and deliver copy-pasteable paragraphs. **When the chapter’s job is Boundary, that style yields:** do not fill RAG’s three layers, drop hedges, or retitle the section as capability marketing in order to widen claims. 偏差 4 and `decision-rules.md` §9 outrank the competition-document section; the priority is stated in `code-verification-workflow.md`.
- Preserve the document's primary contribution as defined by the title, rubric, adopted scope, and owner intent.
- Reserve strategic emphasis and unsupported project decisions for the human owner.

---

## Output behavior

- **Mode 1 (Knowledge Base)**: Deliver Investigator-index `HOME.md` + `01`..`07` (`canonical_for` empty; Wiki pointer if present) with concrete names, this-run line counts, verbatim issue statuses (+ spot-check notes), cross-references, and tables — respecting Mode 1 red lines.
- **Mode 2 (Writing)**: Deliver the requested artifact, not the investigation transcript. Keep rejected facts, source dumps, evidence ledgers, and drafting instructions outside formal prose unless explicitly requested.
- **Mode 3 (Verification & Governance)**: Diagnose before rewriting. Identify affected claims, code evidence (file + lines), claim type, evidence state, root cause, reader impact, and primary treatment, followed by **drop-in replacement paragraphs** or the P0/P1/P2 audit table.
- **Direct repair**: Make the smallest coherent repair that resolves the root cause, then recheck the affected claim lineage.

---

## Stop conditions

Stop and request a project-owner decision when:
- authoritative sources conflict on a material claim;
- title/rubric/owner intent does not establish the primary contribution;
- an acceptance target or strategic threshold lacks an authorized basis;
- a requested stronger claim requires evidence confirmed absent;
- a delegated proof target materially contradicts the referring claim;
- a project-level architecture, limitation, or innovation decision cannot be resolved from adopted sources.

Do not stop merely because an initial search did not find evidence. Classify the evidence state and perform targeted retrieval first.

---

## References

- `references/core-model.md` — canonical objects and terminology
- `references/writing-workflow.md` — preventive drafting workflow
- `references/audit-workflow.md` — post-writing audit and repair workflow
- `references/codebase-knowledge-base-workflow.md` — 5-stage parallel codebase exploration and `7 + 1` knowledge-base generation
- `references/code-verification-workflow.md` — Mode 2/3 code-fact red lines, line-by-line verification, 5 deviation types (including CLI ≠ listen), competition rules that yield on Boundary chapters, and drop-in revision format
- `references/claim-evidence-contracts.md` — Research, Engineering, and Product/Application proof obligations
- `references/decision-rules.md` — evidence, scope, disclosure, severity, and treatment judgments
- `references/narrative-projection.md` — projection from internal structures to precise formal prose
- `references/document-architecture.md` — primary contribution, chapter roles, dependencies, and argument closure
- `references/examples.md` — concrete patterns and antipatterns
- `CHANGELOG.md` — version history and migration notes
