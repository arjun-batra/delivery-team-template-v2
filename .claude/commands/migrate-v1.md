---
description: "Upgrade an existing project from delivery-team-template v1 to the current v2 workflow. Usage: /migrate-v1"
---

Read `WORKFLOW.md` and `CLAUDE.md`. This command has the same outcome and approval boundaries as Codex `$migrate-v1`.

1. Establish the installed v1 baseline from `.claude/template-version`, root `VERSION`, or Git history. If it cannot be established, stop and ask the user; do not guess.
2. Fetch the current template into a platform-appropriate temporary workspace and create a three-way migration preview.
3. Preserve project-owned content: `README.md`, existing `docs/` artifacts, source, tests, configuration, and unknown files in managed directories.
4. After approval, update only managed workflow assets: `WORKFLOW.md`, `AGENTS.md`, `CLAUDE.md`, `.agents/skills/`, template-owned `.claude/agents/` and `.claude/commands/`, `.claudeignore`, `.github/workflows/audit.yml`, and `scripts/audit_template.py`. Create `docs/delivery-state.md` only if absent.
5. Do not copy root `VERSION`, `CHANGELOG.md`, or `adapters/` from the template. Write the adopted template version to `.claude/template-version`.
6. Run the workflow audit and project checks, report conflicts and results, then request approval before committing or opening a pull request.

Restart Claude Code if it does not recognize the updated commands or agents.
