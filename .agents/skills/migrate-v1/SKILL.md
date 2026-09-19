---
name: migrate-v1
description: Upgrade an existing repository from delivery-team-template v1 to the current v2 workflow without overwriting project-owned content.
---

# Migrate a v1 delivery team

Read `AGENTS.md` and `WORKFLOW.md`. This operation has the same outcome and approval boundaries as Claude `/migrate-v1`.

1. Identify the installed template baseline from `.claude/template-version`, root `VERSION`, or Git history. If no defensible v1 baseline can be established, stop and ask the user; do not guess.
2. Fetch the current template into a platform-appropriate temporary workspace. Compare the installed workflow files against the v1 baseline and current template.
3. Present a migration preview. Treat `README.md`, existing `docs/` artifacts, source, tests, project configuration, and unrecognized files inside managed directories as project-owned. Do not delete or overwrite them silently.
4. After approval, update managed workflow assets: `WORKFLOW.md`, `AGENTS.md`, `CLAUDE.md`, `.agents/skills/`, template-owned `.claude/agents/` and `.claude/commands/`, `.claudeignore`, `.github/workflows/audit.yml`, and `scripts/audit_template.py`. Create `docs/delivery-state.md` only when it does not already exist.
5. Do not copy the template's root `VERSION`, `CHANGELOG.md`, or `adapters/` directory into the application. Record the adopted template version in `.claude/template-version`.
6. Run the workflow audit and the project's configured checks. Report conflicts and test results, then request approval before committing or opening a pull request.

Restart Codex after the migration if the new skills are not visible.
