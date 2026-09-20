# Delivery Team Template v2

A reusable, provider-neutral delivery workflow for projects built with **Claude Code** or **ChatGPT Codex**. Use GitHub’s **Use this template** button to start a new repository.

## What travels with a new project

- `WORKFLOW.md` — canonical policy for roles, artifacts, gates, verification, and approvals.
- `delivery/` — shared role/operation procedures, documentation standard, and execution policy.
- `.codex/agents/` — native Codex model-tier profiles.
- `AGENTS.md` and `.agents/skills/` — the ChatGPT Codex adapter.
- `CLAUDE.md` and `.claude/` — the Claude Code adapter.
- `docs/delivery-state.md` — compact navigation for a fresh session; authoritative facts remain in their owned artifacts.
- `.github/workflows/audit.yml` and `scripts/audit_template.py` — template and project checks.

## Start or migrate a project

| Operation | Claude Code | ChatGPT Codex |
|---|---|---|
| New project | `/spin-up-team <idea>` | `$spin-up-team <idea>` |
| Adopt an existing project | `/adopt-team` | `$adopt-team` |
| Migrate an existing v1 project | `/migrate-v1` | `$migrate-v1` |
| Resume work | `/resume-work` | `$resume-work` |
| Sync workflow updates | `/sync-team` | `$sync-team` |
| Retrospective | `/retro` | `$retro` |
| Deep review | `/big-guns [focus]` | `$big-guns [focus]` |

See [the Codex adapter](adapters/codex/README.md) and [the Claude adapter](adapters/claude/README.md).

## Working principles

The workflow is artifact-driven: requirements, design, increment status, test evidence, review findings, and runbooks live in `docs/`, not transient chat. The user approves discovery, requirements, and design before implementation. Each merge is an end-to-end vertical slice.

Documentation stays concise and human-readable through the [shared documentation standard](delivery/documentation.md). Each role refreshes affected artifacts on every pass; each increment closes with an automatic documentation reconciliation and reviewer check.

## Required subagent workflow

For non-trivial delivery work, the coordinator must spawn the shared-role workers defined in [the dispatch contract](delivery/dispatch.md): product/technical-design workers when needed, a developer for implementation, then separate QA and reviewer workers. The only coordinator-only exception is a trivial non-behavioral change. Codex and Claude report actual worker dispatch; they do not pause for routine internal handoffs or status acknowledgement.

## Efficient execution

One coordinator is the default. It selects fast, standard, or deep workers for the task using the [execution policy](delivery/execution.md) and [model map](delivery/model-routing.json), with compact handoffs and evidence reuse. Native profiles configure model selection for Claude Code and compatible Codex subagent runtimes. Plain ChatGPT chats or runtimes without these controls cannot enforce automatic switching; account overrides can also change the model. The shared workflow still applies.

Models are tunable defaults. Compare total usage, rework, latency, and quality before claiming savings. Configuration audits verify structure, not live model availability or model behavior. Python 3.11+ is required for the audit.

## Safety and maintenance

The template never pre-approves commits, pushes, pull requests, merges, deployments, or other external side effects. Update `WORKFLOW.md` before changing adapter behavior, then bump `VERSION` and add a `CHANGELOG.md` entry.
