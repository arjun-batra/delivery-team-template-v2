#!/usr/bin/env python3
"""Validate the delivery-team template's portable structure."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("spin-up-team", "adopt-team", "resume-work", "sync-team", "retro", "big-guns")
REQUIRED = (
    "AGENTS.md", "CLAUDE.md", "WORKFLOW.md", "README.md", "CHANGELOG.md", "VERSION",
    "docs/delivery-state.md", "adapters/codex/README.md", "adapters/claude/README.md",
    ".github/workflows/audit.yml", ".agents/skills/delivery-team/SKILL.md",
)
errors = []

for relative in REQUIRED:
    if not (ROOT / relative).is_file():
        errors.append(f"missing required file: {relative}")

for skill in SKILLS:
    path = ROOT / ".agents" / "skills" / skill / "SKILL.md"
    if not path.is_file():
        errors.append(f"missing Codex skill: {path.relative_to(ROOT)}")
        continue
    text = path.read_text(encoding="utf-8")
    if not re.search(rf"(?m)^name: {re.escape(skill)}$", text):
        errors.append(f"skill name does not match folder: {path.relative_to(ROOT)}")

version = (ROOT / "VERSION")
if version.is_file() and not re.fullmatch(r"\d+\.\d+\.\d+\n?", version.read_text(encoding="utf-8")):
    errors.append("VERSION must use semantic versioning (MAJOR.MINOR.PATCH)")

for relative, required_text in (
    ("WORKFLOW.md", "provider-neutral source of truth"),
    ("README.md", "$spin-up-team"),
    ("CLAUDE.md", "$spin-up-team"),
    ("adapters/codex/README.md", "$spin-up-team"),
):
    path = ROOT / relative
    if path.is_file() and required_text not in path.read_text(encoding="utf-8"):
        errors.append(f"{relative} is missing expected parity marker: {required_text}")

if errors:
    print("Template audit failed:", *errors, sep="\n- ")
    sys.exit(1)

print(f"Template audit passed: {len(SKILLS)} Codex command-parity skills found.")
