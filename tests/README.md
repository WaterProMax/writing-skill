# Skill Regression Tests

These tests protect the structural and behavioral integrity of the unified `writing-skill` (integrating `codebase-knowledge-base-generation`, `project-document-evidence-governance`, and `technical-doc-code-verification`). They are not runtime references and should not be loaded during normal writing, knowledge-base generation, or verification tasks.

## Static structure check

Run from the skill directory:

```bash
python3 tests/validate_structure.py
```

The script verifies:

- the unified runtime file set (`SKILL.md`, `CHANGELOG.md`, `README.md`, and all 10 `references/*.md` files);
- absence of legacy v0.4 runtime references;
- resolvable reference paths across all runtime markdown files;
- presence of the five canonical objects (`Artifact Brief`, `Claim Record`, `Evidence Profile`, `Narrative Decision`, `Boundary Record`);
- separation of `Claim Type` and `Claim Lineage`;
- inclusion of all 4 operating modes (`Mode 1` through `Mode 4`);
- bounded router and Lite-route load sizes;
- absence of version-history prose in `SKILL.md`.

## Behavioral regression cases

`regression-cases.yaml` contains 18 historical failure signatures covering both evidence governance and source-code verification:

- 13 governance regression cases from `project-document-evidence-governance` (proof substitution, target-as-result, orphan metrics, semantic subject ownership / global-subject saturation, Claim Lineage regression, boundary overexposure, primary contribution displacement, etc.);
- 5 code-verification and KB-bridge regression cases (cross-module RAG misattribution, state-enum simplification, sync-vs-async return mismatch, AI capability boundary exaggeration, and knowledge-base `01`..`07` structure leaking as a formal document outline).
