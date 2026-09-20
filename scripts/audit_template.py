#!/usr/bin/env python3
"""Validate provider-neutral workflow structure and adapter linkage."""
import json
from pathlib import Path
import re
import sys
import tomllib
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def require(path):
    if not (ROOT/path).is_file(): errors.append(f"missing: {path}"); return False
    return True
for path in ("AGENTS.md","CLAUDE.md","WORKFLOW.md","docs/delivery-state.md","delivery/manifest.json","delivery/documentation.md","delivery/dispatch.md",".github/workflows/audit.yml",".agents/skills/delivery-team/SKILL.md"):
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
for agent,role in {"pm":"product","techlead":"technical-lead","tech-lead":"technical-lead","designer":"designer","dev":"developer","qa":"qa","reviewer":"reviewer","release":"release","big-guns":"deep-review"}.items():
    path=Path(".claude/agents")/(agent+".md"); procedure=manifest.get("roles",{}).get(role)
    if require(path) and procedure and procedure not in (ROOT/path).read_text(encoding="utf-8"):
        errors.append(f"Claude agent is not linked to shared role: {path}")
# Structural linkage only; factual freshness is checked by the increment reviewer.
for relative in ("WORKFLOW.md", "delivery/roles/developer.md", "delivery/roles/qa.md",
                 "delivery/roles/reviewer.md", "delivery/roles/technical-lead.md"):
    if require(relative) and "delivery/documentation.md" not in (ROOT/relative).read_text(encoding="utf-8"):
        errors.append(f"missing shared documentation standard link: {relative}")

# Validate native profiles against the shared map; no remote model calls.
for relative in ("delivery/execution.md", "delivery/worker.md", "delivery/model-routing.json", "delivery/dispatch.md"):
    require(relative)
for relative in ("WORKFLOW.md", "AGENTS.md", "CLAUDE.md", ".claude/orchestrator-checklist.md", ".agents/skills/delivery-team/SKILL.md"):
    if require(relative) and "delivery/execution.md" not in (ROOT/relative).read_text(encoding="utf-8"):
        errors.append(f"missing execution policy link: {relative}")
    if require(relative) and "delivery/dispatch.md" not in (ROOT/relative).read_text(encoding="utf-8"):
        errors.append(f"missing dispatch contract link: {relative}")
for relative in (".codex/agents/", ".claude/agents/", "delivery/", ".claude/orchestrator-checklist.md"):
    if relative not in manifest.get("managed_paths", []):
        errors.append(f"routing assets not managed for installation: {relative}")
try:
    routing = json.loads((ROOT/"delivery/model-routing.json").read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    errors.append(f"invalid model map: {exc}")
    routing = {}
if not isinstance(routing, dict) or routing.get("schema") != 1:
    errors.append("model map must be an object with schema 1")
    routing = {}
providers = routing.get("providers", {})
if not isinstance(providers, dict):
    errors.append("model providers must be an object")
    providers = {}
for provider in ("claude", "codex"):
    tiers = providers.get(provider, {})
    if not isinstance(tiers, dict) or set(tiers) != {"fast", "standard", "deep"}:
        errors.append(f"{provider} must define fast, standard, and deep tiers")
        tiers = {}
    for tier, expected in tiers.items():
        if not isinstance(expected, dict) or not isinstance(expected.get("model"), str) or not expected["model"].strip():
            errors.append(f"invalid model for {provider}/{tier}")
            continue
        name = f"delivery-{tier}"
        relative = f".{provider}/agents/{name}." + ("toml" if provider == "codex" else "md")
        if not require(relative):
            continue
        text = (ROOT/relative).read_text(encoding="utf-8")
        if provider == "codex":
            try:
                profile = tomllib.loads(text)
            except tomllib.TOMLDecodeError as exc:
                errors.append(f"invalid profile {relative}: {exc}")
                continue
            instructions = profile.get("developer_instructions", "")
            effort = expected.get("model_reasoning_effort")
            if not isinstance(effort, str) or not effort.strip() or profile.get("model_reasoning_effort") != effort:
                errors.append(f"reasoning effort mismatch: {relative}")
        else:
            frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
            if not frontmatter:
                errors.append(f"missing frontmatter: {relative}")
                continue
            profile = dict(re.findall(r"(?m)^([a-z_]+): ([^\r\n]+)$", frontmatter.group(1)))
            instructions = text[frontmatter.end():]
        if profile.get("name") != name or profile.get("model") != expected["model"]:
            errors.append(f"name/model mismatch: {relative}")
        if not profile.get("description") or "delivery/worker.md" not in instructions:
            errors.append(f"missing description/worker contract: {relative}")

if manifest.get("execution", {}).get("dispatch") != "delivery/dispatch.md":
    errors.append("manifest must declare the shared dispatch contract")

dispatch = (ROOT/"delivery/dispatch.md")
if dispatch.is_file():
    text = dispatch.read_text(encoding="utf-8")
    for required in ("delivery/roles/developer.md", "delivery/roles/qa.md", "delivery/roles/reviewer.md", "Do not use the same worker thread"):
        if required not in text:
            errors.append(f"dispatch contract is missing required worker rule: {required}")

is_template=all((ROOT/p).is_file() for p in ("README.md","CHANGELOG.md","VERSION","adapters/codex/README.md","adapters/claude/README.md"))
if is_template and not re.fullmatch(r"\d+\.\d+\.\d+\n?",(ROOT/"VERSION").read_text(encoding="utf-8")):
    errors.append("VERSION must use semantic versioning (MAJOR.MINOR.PATCH)")
if errors:
    print("Delivery workflow audit failed:",*errors,sep="\n- ");sys.exit(1)
print(f"Delivery workflow audit passed: {len(manifest.get('operations',{}))} linked operations and {len(manifest.get('roles',{}))} shared roles; native model profiles validated.")
