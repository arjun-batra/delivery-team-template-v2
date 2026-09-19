# Delivery Team Template v2

A reusable, provider-neutral delivery workflow for projects built with **Claude Code** or **ChatGPT Codex**. Use GitHub’s **Use this template** button to start a new repository.

## What travels with a new project

- `WORKFLOW.md` — canonical policy for roles, artifacts, gates, verification, and approvals.
- `AGENTS.md` and `.agents/skills/` — the ChatGPT Codex adapter.
- `CLAUDE.md` and `.claude/` — the Claude Code adapter.
- `docs/delivery-state.md` — compact navigation for a fresh session; authoritative facts remain in their owned artifacts.
- `.github/workflows/audit.yml` and `scripts/audit_template.py` — template and project checks.

## Start a project

| Operation | Claude Code | ChatGPT Codex |
|---|---|---|
| New project | `/spin-up-team <idea>` | `$spin-up-team <idea>` |
| Adopt an existing project | `/adopt-team` | `$adopt-team` |
| Resume work | `/resume-work` | `$resume-work` |
| Sync workflow updates | `/sync-team` | `$sync-team` |
| Retrospective | `/retro` | `$retro` |
| Deep review | `/big-guns [focus]` | `$big-guns [focus]` |

See [the Codex adapter](adapters/codex/README.md) and [the Claude adapter](adapters/claude/README.md).

## Working principles

The workflow is artifact-driven: requirements, design, increment status, test evidence, review findings, and runbooks live in `docs/`, not transient chat. The user approves discovery, requirements, and design before implementation. Each merge is an end-to-end vertical slice.

## Safety and maintenance

The template never pre-approves commits, pushes, pull requests, merges, deployments, or other external side effects. Update `WORKFLOW.md` before changing adapter behavior, then bump `VERSION` and add a `CHANGELOG.md` entry.
