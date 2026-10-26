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

    if len(skill_text) > 15_000:
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
    if lite_writing_size > 30_000 or lite_audit_size > 30_000:
        fail(
            "Lite route exceeded budget: "
            f"writing={lite_writing_size}, audit={lite_audit_size}"
        )

    print("PASS: unified writing-skill structure is valid")
    print(f"PASS: Lite writing load = {lite_writing_size} bytes")
    print(f"PASS: Lite audit load = {lite_audit_size} bytes")


if __name__ == "__main__":
    main()
