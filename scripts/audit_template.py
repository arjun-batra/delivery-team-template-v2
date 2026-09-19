#!/usr/bin/env python3
"""Validate either the delivery template or its installed workflow assets."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    "spin-up-team", "adopt-team", "migrate-v1", "resume-work",
    "sync-team", "retro", "big-guns",
)
CORE_REQUIRED = (
    "AGENTS.md", "CLAUDE.md", "WORKFLOW.md",
    "docs/delivery-state.md", ".github/workflows/audit.yml",
    ".agents/skills/delivery-team/SKILL.md",
)
TEMPLATE_ONLY = (
    "README.md", "CHANGELOG.md", "VERSION",
    "adapters/codex/README.md", "adapters/claude/README.md",
)
errors = []

for relative in CORE_REQUIRED:
    if not (ROOT / relative).is_file():
        errors.append(f"missing required workflow file: {relative}")

for skill in SKILLS:
    skill_path = ROOT / ".agents" / "skills" / skill / "SKILL.md"
    command_path = ROOT / ".claude" / "commands" / f"{skill}.md"
    if not skill_path.is_file():
        errors.append(f"missing Codex skill: {skill_path.relative_to(ROOT)}")
    elif not re.search(
        rf"(?m)^name: {re.escape(skill)}$",
        skill_path.read_text(encoding="utf-8"),
    ):
        errors.append(f"skill name does not match folder: {skill_path.relative_to(ROOT)}")
    if not command_path.is_file():
        errors.append(f"missing Claude command: {command_path.relative_to(ROOT)}")

is_template = all((ROOT / relative).is_file() for relative in TEMPLATE_ONLY)
if is_template:
    version = (ROOT / "VERSION").read_text(encoding="utf-8")
    if not re.fullmatch(r"\d+\.\d+\.\d+\n?", version):
        errors.append("VERSION must use semantic versioning (MAJOR.MINOR.PATCH)")
    for relative, marker in (
        ("README.md", "$migrate-v1"),
        ("CLAUDE.md", "$migrate-v1"),
        ("adapters/codex/README.md", "$migrate-v1"),
    ):
        if marker not in (ROOT / relative).read_text(encoding="utf-8"):
            errors.append(f"{relative} is missing parity marker: {marker}")

if errors:
    print("Delivery workflow audit failed:", *errors, sep="\n- ")
    sys.exit(1)

mode = "template" if is_template else "installed workflow"
print(f"Delivery workflow audit passed ({mode}): {len(SKILLS)} command-parity skills found.")
