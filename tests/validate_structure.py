#!/usr/bin/env python3
"""Static checks for the unified technical-writing, knowledge-base, and evidence-governance skill."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "references"

EXPECTED_REFERENCES = {
    "audit-workflow.md",
    "claim-evidence-contracts.md",
    "code-verification-workflow.md",
    "codebase-knowledge-base-workflow.md",
    "core-model.md",
    "decision-rules.md",
    "document-architecture.md",
    "examples.md",
    "narrative-projection.md",
    "writing-workflow.md",
}

LEGACY_REFERENCES = {
    "root-principles.md",
    "writing-line.md",
    "governance-line.md",
    "calibration-rules.md",
    "document-architecture-principles.md",
    "patterns-and-antipatterns.md",
    "research-engineering-contracts.md",
    "formal-narrative-controls.md",
}

CANONICAL_OBJECTS = {
    "Artifact Brief",
    "Claim Record",
    "Evidence Profile",
    "Narrative Decision",
    "Boundary Record",
}

REQUIRED_MODES = {
    "Mode 1",
    "Mode 2",
    "Mode 3",
    "Mode 4",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    skill = ROOT / "SKILL.md"
    changelog = ROOT / "CHANGELOG.md"
    readme = ROOT / "README.md"
    if not skill.exists() or not changelog.exists() or not readme.exists():
        fail("SKILL.md, README.md, and CHANGELOG.md must exist")

    actual_refs = {path.name for path in REFS.glob("*.md")}
    if actual_refs != EXPECTED_REFERENCES:
        fail(
            "reference set mismatch: "
            f"missing={sorted(EXPECTED_REFERENCES - actual_refs)}, "
            f"extra={sorted(actual_refs - EXPECTED_REFERENCES)}"
        )

    if actual_refs & LEGACY_REFERENCES:
        fail(f"legacy references still present: {sorted(actual_refs & LEGACY_REFERENCES)}")

    runtime_files = [skill, *sorted(REFS.glob("*.md"))]
    runtime_text = "\n".join(path.read_text(encoding="utf-8") for path in runtime_files)

    for legacy in LEGACY_REFERENCES:
        if f"`references/{legacy}`" in runtime_text:
            fail(f"runtime content still references legacy file {legacy}")

    skill_text = skill.read_text(encoding="utf-8")
    if re.search(r"\bv0\.\d+\b", skill_text, flags=re.IGNORECASE):
        fail("version-history prose must live in CHANGELOG.md, not SKILL.md")

    # 1.0.3 adds a Scoped route and shared red-line pointers on the always-loaded router.
    if len(skill_text) > 20_000:
        fail(f"SKILL.md is too large for a unified router: {len(skill_text)} characters")

    missing_modes = sorted(m for m in REQUIRED_MODES if m not in skill_text)
    if missing_modes:
        fail(f"operating modes missing from SKILL.md: {missing_modes}")

    core_text = (REFS / "core-model.md").read_text(encoding="utf-8")
    missing_objects = sorted(obj for obj in CANONICAL_OBJECTS if obj not in core_text)
    if missing_objects:
        fail(f"canonical objects missing from core model: {missing_objects}")

    if "Claim Type" not in core_text or "Claim Lineage" not in core_text:
        fail("core model must separate Claim Type from Claim Lineage")

    for path in runtime_files:
        text = path.read_text(encoding="utf-8")
        for ref in re.findall(r"`(references/[^`]+\.md)`", text):
            if not (ROOT / ref).exists():
                fail(f"{path.name} points to missing reference {ref}")

    lite_writing_size = sum(
        path.stat().st_size
        for path in [skill, REFS / "core-model.md", REFS / "writing-workflow.md"]
    )
    lite_audit_size = sum(
        path.stat().st_size
        for path in [skill, REFS / "core-model.md", REFS / "audit-workflow.md"]
    )
    # Raised with the 1.0.3 Scoped route, which lives on the always-loaded router.
    if lite_writing_size > 36_000 or lite_audit_size > 36_000:
        fail(
            "Lite route exceeded budget: "
            f"writing={lite_writing_size}, audit={lite_audit_size}"
        )

    workflow_text = (REFS / "codebase-knowledge-base-workflow.md").read_text(encoding="utf-8")
    required_grounding = [
        "清单失效",
        "running code > Flyway/entities",
        "阶段 5 增补",
        "Claim Necessity",
        "canonical_for",
        "ListenAndServe",
        "@TableField",
        "独立工具/采集进程",
        "schoolFetch(",
        "占位：后台探索尚未回传，以下仅为主会话已核对范围。",
        "未打开源码核对（仅保留手记原词）",
        "本表仅证明符号/映射在源码中存在，不代表方法体分支、鉴权或运行时业务契约已验证",
    ]
    missing_grounding = [s for s in required_grounding if s not in workflow_text]
    if missing_grounding:
        fail(f"Mode 1 workflow missing grounding anchors: {missing_grounding}")

    if "要求 `read EVERY file`" in workflow_text or "read EVERY file`" in workflow_text:
        fail("Mode 1 workflow must not require literal 'read EVERY file'")

    if "用户系统/画像/简历" in workflow_text and "不要写死" not in workflow_text:
        fail("HOME example modules must be placeholderized")

    mode1_markers = [
        "Mode 1 reading set",
        "Conflict priority",
        "Red lines",
        "独立工具/采集进程",
        "schoolFetch(",
        "占位：后台探索尚未回传，以下仅为主会话已核对范围。",
        "未打开源码核对（仅保留手记原词）",
        "本表仅证明符号/映射在源码中存在，不代表方法体分支、鉴权或运行时业务契约已验证",
    ]
    missing_skill = [s for s in mode1_markers if s not in skill_text]
    if missing_skill:
        fail(f"SKILL.md Mode 1 grounding markers missing: {missing_skill}")

    if "running code > Flyway/entities" not in skill_text:
        fail("SKILL.md must state the source conflict order")

    if "**Scoped**" not in skill_text or "Do **not** enter Mode 1" not in skill_text:
        fail("SKILL.md must show a Scoped route that refuses Mode 1")
    if "would this mis-attribute A’s tech to B?" not in skill_text:
        fail("SKILL.md Scoped route must limit adjacent code to mis-attribution checks")
    if "promote this task to Deep" not in skill_text:
        fail("SKILL.md must stop 比赛/申报 from promoting a Boundary memo to Deep")

    verify_text = (REFS / "code-verification-workflow.md").read_text(encoding="utf-8")
    shared_red_lines = [
        "Mode 2/3 code-fact red lines",
        "ListenAndServe",
        "net/http",
        "Empty Controller",
        "JDBC",
        "@TableField",
        "loopback",
        "public address",
        "empty DSN",
        "偏差 5",
        "章节职责是 Boundary 时，本节约让路",
        "偏差 4",
    ]
    missing_red = [s for s in shared_red_lines if s not in verify_text]
    if missing_red:
        fail(f"code-verification-workflow.md missing Mode 2/3 red lines: {missing_red}")
    if "codebase-knowledge-base-workflow.md" not in verify_text:
        fail("code-verification red lines must say Mode 2/3 need not open the Mode 1 workflow")

    rules_text = (REFS / "decision-rules.md").read_text(encoding="utf-8")
    memo_markers = [
        "子系统局限性备忘录",
        "One row per entrypoint",
        "Do not merge dry-run defaults across entrypoints",
        "可以写 / 不能写",
        "Experiment scores default to Delete",
        "Competition-style yield",
        "loopback / public address / empty DSN",
    ]
    missing_memo = [s for s in memo_markers if s not in rules_text]
    if missing_memo:
        fail(f"decision-rules.md §9 memo markers missing: {missing_memo}")

    writing_text = (REFS / "writing-workflow.md").read_text(encoding="utf-8")
    if "Scoped" not in writing_text or "Do not enter Mode 1" not in writing_text:
        fail("writing-workflow Phase 0 must route Scoped and refuse Mode 1")

    cases_text = (ROOT / "tests" / "regression-cases.yaml").read_text(encoding="utf-8")
    for signature in (
        "scoped_cli_module_boundary",
        "为单体仓库中的一个 CLI 模块写申报边界",
        "producing `01`–`07`",
        "writing the CLI as a listen service",
        "turning adjacent experiment scores into that CLI’s product metrics",
    ):
        if signature not in cases_text:
            fail(f"regression case missing signature: {signature}")

    print("PASS: unified writing-skill structure is valid")
    print("PASS: Mode 1 grounding anchors present")
    print("PASS: Scoped route and Mode 2/3 code-fact red lines present")

    print(f"PASS: Lite writing load = {lite_writing_size} bytes")
    print(f"PASS: Lite audit load = {lite_audit_size} bytes")


if __name__ == "__main__":
    main()
