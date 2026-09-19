#!/usr/bin/env python3
"""Validate provider-neutral workflow structure and adapter linkage."""
import json
from pathlib import Path
import re
import sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def require(path):
    if not (ROOT/path).is_file(): errors.append(f"missing: {path}"); return False
    return True
for path in ("AGENTS.md","CLAUDE.md","WORKFLOW.md","docs/delivery-state.md","delivery/manifest.json",".github/workflows/audit.yml",".agents/skills/delivery-team/SKILL.md"):
    require(path)
try:
    manifest=json.loads((ROOT/"delivery/manifest.json").read_text(encoding="utf-8"))
except (OSError,json.JSONDecodeError) as exc:
    errors.append(f"invalid manifest: {exc}"); manifest={}
for name,procedure in manifest.get("operations",{}).items():
    skill=Path(".agents/skills")/name/"SKILL.md"; command=Path(".claude/commands")/(name+".md")
    for adapter,label in ((skill,"Codex skill"),(command,"Claude command")):
        if require(adapter):
            body=(ROOT/adapter).read_text(encoding="utf-8")
            if procedure not in body: errors.append(f"{label} is not linked to shared procedure: {adapter}")
    if require(procedure) and require(skill):
        if not re.search(rf"(?m)^name: {re.escape(name)}$", (ROOT/skill).read_text(encoding="utf-8")):
            errors.append(f"skill name does not match folder: {skill}")
for role,procedure in manifest.get("roles",{}).items():
    require(procedure)
for agent,role in {"pm":"product","techlead":"technical-lead","designer":"designer","dev":"developer","qa":"qa","reviewer":"reviewer","release":"release","big-guns":"deep-review"}.items():
    path=Path(".claude/agents")/(agent+".md"); procedure=manifest.get("roles",{}).get(role)
    if require(path) and procedure and procedure not in (ROOT/path).read_text(encoding="utf-8"):
        errors.append(f"Claude agent is not linked to shared role: {path}")
is_template=all((ROOT/p).is_file() for p in ("README.md","CHANGELOG.md","VERSION"))
if is_template and not re.fullmatch(r"\d+\.\d+\.\d+\n?",(ROOT/"VERSION").read_text(encoding="utf-8")):
    errors.append("VERSION must use semantic versioning (MAJOR.MINOR.PATCH)")
if errors:
    print("Delivery workflow audit failed:",*errors,sep="\n- ");sys.exit(1)
print(f"Delivery workflow audit passed: {len(manifest.get('operations',{}))} linked operations and {len(manifest.get('roles',{}))} shared roles.")
