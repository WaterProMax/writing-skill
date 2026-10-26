# Changelog

## 1.0.3 — Scoped limitations memos and Mode 2/3 code-fact red lines (`writing-skill`)

Based on the Grok scoped trial on `Lenquest/KariosArc` (PR #21, subsystem / scoped limitations guidance **6/10**). This score is separate from whole-repo Mode 1 (7/10 on PR #19, 8/10 on PR #20). v1.0.1 and v1.0.2 Mode 1 fixes stay in force. This release teaches a teammate who owns one backend module to stop at **Scoped + Mode 2** instead of building `01`–`07`.

### Fixed / Added

1. **Scoped depth** — `SKILL.md` depth table and stop conditions: when the deliverable is a boundary or limitations memo for one directory or one toolchain, and the user explicitly does not want a whole-repo knowledge base, do not enter Mode 1, do not create `01`–`07`, write a file whitelist first, and open adjacent code only to answer “would this mis-attribute A’s tech to B?”. Words such as 比赛 / 申报 do not promote that task to Deep. Mode 2’s Phase 0 carries the same stop.
2. **Mode 2/3 code-fact red lines, including 偏差 5** — Listen / empty Controller / secrets and connection strings / Java property ≠ physical column are loadable from `references/code-verification-workflow.md` without entering Mode 1. Mode 1 still states them in its own red lines. 偏差 5: do not write a batch CLI client as a long-lived HTTP service unless the entrypoint has `ListenAndServe` or an equivalent bind. A directory name, a `net/http` import, or an unreferenced URL config is not a bind.
3. **`decision-rules.md` §9「子系统局限性备忘录」** — One row per entrypoint (process shape, default flags, write targets, gates). Do not merge dry-run defaults across entrypoints. Concentrate can-write / cannot-write in one Boundary section. Experiment scores default to Delete unless this section’s Claim Type is Research and the protocol is complete.
4. **Competition-doc style yields on Boundary** — When the chapter’s job is Boundary, do not fill RAG’s three layers, drop hedges, or retitle as capability marketing to widen claims. 偏差 4 and §9 outrank `code-verification-workflow.md`（特殊处理：比赛文档）. The priority is written in that section, in §9, and in the `SKILL.md` invariants.
5. **Infrastructure defaults in formal prose** — Cite source line number and category (loopback / public address / empty DSN). Do not copy host, IP, secret, or JDBC URL into the body.
6. **Regression** — `tests/regression-cases.yaml` case `scoped_cli_module_boundary`: input 「为单体仓库中的一个 CLI 模块写申报边界」. Failure signatures: producing `01`–`07`, writing the CLI as a listen service, or turning adjacent experiment scores into that CLI’s product metrics.

### Migration

Existing Mode 1 indexes are unchanged. A new limitations memo for one module should start at Scoped, not by re-running Mode 1.

---

## 1.0.2 — Mode 1 precision & verification gates from KariosArc retest (`writing-skill`)

Based on the second Grok Mode 1 trial on `Lenquest/KariosArc` (PR #20, `docs/writing-skill-test-v101/TEST_REPORT.md`, score **8/10**). Closes the 5 remaining extraction and verification gaps identified in the retest:

### Fixed / Added (Mode 1)

1. **Repo-wide entry scan before directory-ownership split** — Scan `@RestController` / `@RequestMapping` / `go.mod` across the entire repository first, then split by directory ownership into **主产品进程** vs **独立工具/采集进程（如 `tools/**`）**, preventing missed tool processes while keeping tool endpoints out of main-product API tables.
2. **Frontend API wrapper follow-through** — Extracting API literals must first identify and follow local request wrappers (`schoolFetch(`, `request(`, `apiClient`) in addition to raw `fetch(` / `axios`; unfollowed wrapper calls must be listed under `未覆盖`, and negative claims like “前端无某模块 API” are strictly forbidden.
3. **Stage 5 fixed placeholder & return-draft verification gate** — Before background agents return, `## 阶段 5 增补` uses the exact placeholder `占位：后台探索尚未回传，以下仅为主会话已核对范围。`; once returned, remove the placeholder and filter out any sub-agent default hosts/secrets, comment-inferred column names, or method-body behavior descriptions not verified line-by-line by the main session.
4. **Explicit source-opening rule for issue spot-checks** — Spot-checking `ISSUES.md` / test notes is defined as opening the named source files to verify current implementation (noting no process re-run); if a source file was not opened, write `未打开源码核对（仅保留手记原词）` rather than “仍破损” or “已修复”.
5. **Non-runtime contract disclaimer on static symbol tables** — Every annotation/static-scan symbol table (Controller mappings, entities, frontend API paths) must carry the fixed header/opening disclaimer: `本表仅证明符号/映射在源码中存在，不代表方法体分支、鉴权或运行时业务契约已验证`.

---


## 1.0.1 — Mode 1 grounding fixes from KariosArc trial (`writing-skill`)

Based on the Grok Mode 1 trial on `Lenquest/KariosArc` (`docs/writing-skill-test/TEST_REPORT.md`, fact-grounding **7/10**). Hardens Investigator-index generation so agents do not copy stale skill snapshots or invent unread behavior.

### Fixed / Added (Mode 1)

1. **Inventory invalidation** — Stage 3 now requires: on missing sample paths, consult `AGENTS.md` / Wiki repository map, record the new path or a Boundary; **never** treat `legacy-designs` same-name history as current. Line counts must come from **this run's** `wc`/tools, never from skill examples.
2. **Conflict priority** — Documented in `SKILL.md` and Mode 1 workflow: `running code > Flyway/entities > generated OpenAPI > Wiki non-canonical prose > test notes > experiment directories`. Issue status is copied **verbatim** from notes, with ≥1 spot-check per status class; disagreements are dual-written.
3. **Mode 1 reading set** — Mode 1 only forces this workflow + `core-model.md` five objects + Claim Necessity (§9); `examples` / `document-architecture` / `audit-workflow` stay in Mode 2/3. Mode 1 must not expand into the Deep reference table.
4. **Stage 2 coverage declaration** — Replaces “read EVERY file”: agents must list enumerated symbols, files fully read, and unread files; unread paths must not appear in behavior sentences. Structured main-session extraction is allowed when parallel agents cannot return in-session.
5. **Stage 5 session model** — If background agents only return after the turn ends, ship a main-session coverage version first, then insert under the fixed heading `阶段 5 增补`.
6. **Red lines** — No secrets/JDBC URLs; no template percentages as metrics; no CLI-as-HTTP without listen evidence; empty Controllers are not APIs; Java properties ≠ physical columns without `@TableField`; `@Value` default ≠ YAML placeholder default.
7. **HOME placeholders** — Modules are derived from workspace views / Controller prefixes present in code or Wiki canonical pages; no hard-coded “用户系统/画像/简历”.
8. **Canonical Wiki coexistence** — Mode 1 output is an Investigator index with empty `canonical_for`; if a Wiki exists, the opening must point to it and declare non-replacement.

Also noted from the trial (directory ownership for third-party / experiment / full-chain notes; frontend stack detection allowing “无路由表”).

### Migration

Existing Mode 1 indexes remain valid as drafts. Re-runs should refresh line counts, re-apply inventory invalidation, and add Wiki pointer + coverage/未覆盖 sections where missing.

---

## 1.0.0 — Unified Technical Writing, Knowledge Base & Evidence Governance (`writing-skill`)

This release unifies three complementary skills from `Lenquest/KariosArc` into a single, conflict-free, four-mode technical writing and governance skill:

1. **`codebase-knowledge-base-generation`** (Mode 1 — Knowledge-Base Generation, preserved in full in `references/codebase-knowledge-base-workflow.md`)
   - 5-stage parallel repository exploration (`Explore Agent -> 4+ Background Module Agents -> Synchronous Core Reading -> Structured 7+1 Knowledge Base Output -> Incremental Edit`).
   - Produces `HOME.md` (role/module navigation index) + `01-overview-architecture.md` through `07-issues-configuration.md` with exact class/table/field names, line counts, issue fix statuses, and cross-layer links.
2. **`project-document-evidence-governance` (v0.5.1)** (Mode 2 — Evidence-Governed Writing & Mode 3 — Governance Audit, preserved in full across `references/core-model.md`, `writing-workflow.md`, `audit-workflow.md`, `claim-evidence-contracts.md`, `decision-rules.md`, `narrative-projection.md`, `document-architecture.md`, `examples.md`)
   - Enforces the five canonical working objects (`Artifact Brief`, `Claim Record`, `Evidence Profile`, `Narrative Decision`, `Boundary Record`) and separates `Claim Type` (`Research`, `Engineering`, `Product/Application`) from `Claim Lineage`.
   - Enforces nearest-semantic-owner grammatical subjects to eliminate global-subject saturation ("本项目 / 本文 / 本研究 / 系统").
3. **`technical-doc-code-verification`** (Mode 3 — Line-by-Line Code Verification, preserved in full in `references/code-verification-workflow.md`)
   - 5-step atomic assertion verification against the local knowledge base and actual source code.
   - Detects the 4 common code deviations (cross-module tech misattribution, state enum/step simplification, sync/async mismatch, and AI capability boundary exaggeration) and outputs `(1) original quote, (2) file + line evidence, (3) full drop-in replacement prose`.
4. **Unified End-to-End Pipeline (Mode 4)** & **Governance Bridge Rules**
   - Connects the `7+1` Knowledge Base as the Investigator's structured fact index while preventing repository folder taxonomy (`01`..`07`) or raw `ISSUES.md` defect lists from leaking into formal reader-facing outlines.

---

0.5.1 — Semantic subject ownership

- Added an explicit nearest-semantic-owner rule for reader-facing prose.
- Added detection of global-subject saturation when project-wide wrappers such as “本项目 / 本文 / 本研究 / 系统 / we / the project” repeatedly occupy paragraph openings while a more informative local subject exists.
- Clarified that the failure is semantic ownership collapse rather than simple lexical repetition.
- Prohibited synonym rotation as a cosmetic fix for repeated global subjects.
- Added Writing-mode prevention, Governance-mode audit checks, and a behavioral regression case for this failure signature.

## 0.5.0 — Structural consolidation

This release reorganizes the skill without adding a new policy domain.

### Changed

- Replaced the growing set of parallel first-class concepts with five canonical working objects:
  - Artifact Brief
  - Claim Record
  - Evidence Profile
  - Narrative Decision
  - Boundary Record
- Separated **Claim Type** from **Claim Lineage**.
- Reduced `SKILL.md` to a mode/depth router, invariant set, and output contract.
- Added conditional reference loading so local edits do not require the full governance stack.
- Consolidated research, engineering, and product/application proof obligations into one claim-evidence contract reference.
- Added an explicit Product/Application Evidence Contract.
- Unified Writing and Governance workflows around the same canonical objects.
- Moved title/primary-contribution gravity into document architecture.
- Moved actor ownership, referential clarity, bilingual projection, Q/R label isolation, and de-templating into narrative projection.
- Moved concrete examples such as Kappa, status constants, and index-heavy prose into the examples reference.
- Centralized evidence-state, scope, delegated proof, disclosure, severity, and treatment rules in one decision reference.
- Added a static topology validator with router and Lite-load budgets.
- Added 12 behavioral regression cases derived from historical document failures.

### Removed

The following v0.4 references were replaced by the consolidated structure:

- `root-principles.md`
- `writing-line.md`
- `governance-line.md`
- `calibration-rules.md`
- `document-architecture-principles.md`
- `patterns-and-antipatterns.md`
- `research-engineering-contracts.md`
- `formal-narrative-controls.md`

## 0.4.0 — Research and engineering separation

- Separated research/algorithm proof from engineering/system proof.
- Added baseline, acceptance-target, and metric-admissibility controls.
- Added actor ownership, referential clarity, bilingual projection, index-label isolation, and de-templating controls.
- Added primary-contribution gravity checks.

## 0.3.0 — Cross-surface evidence governance

- Added evidence-state calibration, delegated-proof verification, strong-state scope, evidence-pointer quality, claim-lineage consistency, and boundary placement controls.

Earlier versions established the repository-to-claim-to-narrative workflow, writing/governance modes, evidence admission control, and selective-disclosure rules.
