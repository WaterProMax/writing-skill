# Changelog

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
