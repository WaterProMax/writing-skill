---
name: writing-skill
description: Use when generating a structured codebase knowledge base, drafting or revising formal project, competition, research, architecture, or engineering documents from repositories and evidence, or verifying and auditing technical documents against source code and evidence contracts. Unified integration of codebase-knowledge-base-generation, project-document-evidence-governance, and technical-doc-code-verification.
---

# Unified Technical Writing, Knowledge Base & Evidence Governance (`writing-skill`)

## Purpose

Transform multi-module repositories, experiments, runtime records, and internal evidence into structured knowledge bases, formal audience-facing documents, or code-verified revisions.

The skill follows three governing rules:

> **1. Evidence is a source of truth, not a source of narrative.** Repository directories and knowledge-base files (`01`..`07`) provide verifiable facts, never the chapter outline of a formal document.
>
> **2. Research, engineering, and product claims have different proof obligations and cannot substitute for one another.**
>
> **3. Every technical assertion must be verified line-by-line against source code, and revisions must be drop-in replacement text.**

The unified transformation is:

`codebase -> structured knowledge base (7+1) -> artifact brief -> claim record -> evidence profile -> narrative decision -> reader-facing artifact -> code & lineage verification`

Use `references/core-model.md` as the terminology source of truth.

---

## Operating modes

### Mode 1 — Knowledge-Base Generation (`codebase-knowledge-base-generation`)

Use when exploring a multi-module codebase (Java/Spring Boot + Vue + Go + Python) to generate a reusable local knowledge base (`docs/knowledge-base/`).

Always read:
- `references/codebase-knowledge-base-workflow.md`

Execute the 5-stage pipeline (`breadth-first explore -> parallel deep dive -> sync core read -> structured 7+1 output -> incremental edit`):
1. **Stage 1 (Explore, <=5 min)**: 1 Explore Agent maps 2-level directories, modules, configs (`pom.xml`, `package.json`, `go.mod`, `requirements.txt`, `Dockerfile`), docs, and line counts.
2. **Stage 2 (Parallel Background Agents)**: Launch 4+ agents (`run_in_background: true`, `read EVERY file`, `document: purpose, parameters, return types`) for (1) Backend Java Controllers/Services/pom, (2) Frontend Views/Components/Services/Store, (3) AI/Go/Python/SQL/eval scripts, and (4) Database Entities/Mappers/DTOs.
3. **Stage 3 (Sync Core Read)**: Without waiting, read `PROJECT_CONTEXT.md`/`AGENTS.md`, `功能模块.md`, `application.yml`, `ISSUES.md`, `TEST_REQUIREMENTS.md`, `API_ROUTE_MATRIX.md`, `AI_PROMPTS.md`, and core stores.
4. **Stage 4 (Structured `7 + 1` Output)**: Write `HOME.md` (role & module navigation) + `01-overview-architecture.md`, `02-frontend-analysis.md`, `03-backend-analysis.md`, `04-database-go-tools.md`, `05-business-flows-testing.md`, `06-ai-prompts-analysis.md`, `07-issues-configuration.md` with exact class/table/field names, line counts, issue statuses, cross-references, and tables.
5. **Stage 5 (Incremental Edit)**: Use targeted `edit` inserts as background agents return; never rewrite whole files or wait idly.

### Mode 2 — Evidence-Governed Writing (`project-document-evidence-governance` Writing Mode)

Use when drafting, rewriting, extending, or updating a formal artifact (competition proposal, research paper, architecture whitepaper, or engineering document).

Always read:
- `references/core-model.md`
- `references/writing-workflow.md`

Load conditionally:
- `references/claim-evidence-contracts.md` for material research, engineering, product, performance, validation, or acceptance claims;
- `references/decision-rules.md` when evidence is incomplete, conflicting, delegated, scope-sensitive, limitation-bearing, or spread across multiple surfaces;
- `references/narrative-projection.md` when producing or repairing reader-facing prose;
- `references/document-architecture.md` for whole-document structure, chapter responsibility, title/rubric alignment, or cross-layer argument design;
- `references/code-verification-workflow.md` when embedding concrete code/table/API facts or competition-specific descriptions;
- `references/examples.md` only when concrete failure signatures or rewrite patterns are useful.

### Mode 3 — Code Verification & Governance Audit (`technical-doc-code-verification` + Governance Mode)

Use when verifying technical descriptions against actual source code, auditing claim-evidence alignment, or cleaning/repairing an existing artifact.

Always read:
- `references/core-model.md`
- `references/audit-workflow.md`
- `references/code-verification-workflow.md`

Load the conditional references from Mode 2 according to the issue under review. Do not load the full reference set mechanically.
- **Line-by-Line Code Verification (5 Steps)**: Split prose into atomic assertions -> query `docs/knowledge-base/` then `grep`/read actual code -> distinguish main online call chains from offline/auxiliary tools -> classify into 4 response tiers (`Exact match` / `Minor polish` / `Architecture misattribution` / `Exaggerated claim`) -> output `(1) original quote, (2) file path + key lines, (3) full drop-in replacement paragraph`.
- **Screen for the 4 Common Code Deviations**: (1) Misattributing System A's technology (e.g., RAG/ChromaDB) to System B; (2) Simplifying or omitting state enums / workflow steps; (3) Claiming synchronous output where code returns asynchronous status (e.g., `reportStatus: "pending"`); (4) Exaggerating AI boundaries (presenting AI candidate suggestions + engineering gates/validators as direct AI final decisions).

### Mode 4 — End-to-End Pipeline (KB -> Governed Writing -> Code & Lineage Audit)

1. Build or consult the `7 + 1` Knowledge Base (`references/codebase-knowledge-base-workflow.md`) as the Investigator fact store.
2. Draft the reader-facing artifact via `references/writing-workflow.md` without letting `01`..`07` file structure or `ISSUES.md` defect lists become the narrative outline.
3. Verify all technical assertions via `references/code-verification-workflow.md` and reconcile all Claim Lineages via `references/audit-workflow.md`.

---

## Depth routing

Choose the lightest route that preserves correctness.

| Depth | Use when | Typical references |
|---|---|---|
| **Lite** | Local paragraph repair or single-passage code verification; source authority and claim are clear | `core-model.md` + mode workflow + `narrative-projection.md` / `code-verification-workflow.md` |
| **Standard** | Substantive section, one material claim lineage, module KB extraction, or research/engineering/product explanation | Lite set + `claim-evidence-contracts.md` + `decision-rules.md` as needed |
| **Deep** | Full `7+1` KB, whole-document architecture, multi-source reconciliation, competition proposal, or final audit | Standard set + `document-architecture.md` + `codebase-knowledge-base-workflow.md` + `examples.md` |

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

- Start from reader need, artifact purpose, and section responsibility—not repository folders or knowledge-base numbering (`01`..`07`).
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
- In competition prose, explicitly name multi-layer technical mechanisms (e.g., Retrieval/Augmented/Generation), avoid hedging ("试图/尝试"), never overclaim AI boundaries, and deliver copy-pasteable paragraphs.
- Preserve the document's primary contribution as defined by the title, rubric, adopted scope, and owner intent.
- Reserve strategic emphasis and unsupported project decisions for the human owner.

---

## Output behavior

- **Mode 1 (Knowledge Base)**: Deliver `HOME.md` + `01`..`07` with concrete class/table/field names, line counts, issue statuses, cross-references, and tables.
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
- `references/code-verification-workflow.md` — line-by-line code verification, 4 deviation types, competition rules, and drop-in revision format
- `references/claim-evidence-contracts.md` — Research, Engineering, and Product/Application proof obligations
- `references/decision-rules.md` — evidence, scope, disclosure, severity, and treatment judgments
- `references/narrative-projection.md` — projection from internal structures to precise formal prose
- `references/document-architecture.md` — primary contribution, chapter roles, dependencies, and argument closure
- `references/examples.md` — concrete patterns and antipatterns
- `CHANGELOG.md` — version history and migration notes
