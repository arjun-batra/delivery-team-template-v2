# Delivery Team Template v2

A reusable, provider-neutral delivery workflow for projects built with **Claude Code** or **ChatGPT Codex**. Use GitHub’s **Use this template** button to start a new repository; the project inherits the workflow and both adapters.

## What travels with a new project

- `WORKFLOW.md` — the canonical delivery policy: roles, durable artifacts, user gates, verification, and release rules.
- `AGENTS.md` and `.agents/skills/delivery-team/` — the Codex adapter.
- `CLAUDE.md` and `.claude/` — the Claude Code adapter and existing slash commands.
- `.github/workflows/audit.yml` — a portable starter audit.

## Start with Codex

Open the generated repository in Codex and say: “Use the delivery-team workflow to start a project: _[idea]_.” Codex reads `AGENTS.md`; the delivery-team skill gives it the reusable procedure. See [the Codex adapter](adapters/codex/README.md).

## Start with Claude Code

Open the generated repository in Claude Code and run `/spin-up-team <idea>`. See [the Claude adapter](adapters/claude/README.md).

## Working principles

The workflow is artifact-driven: requirements, design, increment status, test evidence, review findings, and runbooks live in `docs/`, not in transient chat. The user approves discovery, requirements, and design before implementation. Each merge is an end-to-end vertical slice.

## Safety and maintenance

The template never pre-approves `git push`. Agents must seek current approval for pushes, merges, deployments, and other external side effects. Update `WORKFLOW.md` before changing either adapter, bump `VERSION`, and record the change in `CHANGELOG.md`.
