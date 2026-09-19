---
description: "Adopt the delivery workflow into an existing project. Usage: /adopt-team"
---

Read `WORKFLOW.md` and `CLAUDE.md`. This command has the same outcome and approval boundaries as Codex `$adopt-team`.

## Install safely

Fetch the template into a platform-appropriate temporary workspace. Preview the diff before copying only `WORKFLOW.md`, `AGENTS.md`, `.agents/`, `.claude/`, `.claudeignore`, `.github/workflows/audit.yml`, and `scripts/audit_template.py`.

Never overwrite `README.md`, `docs/`, source, tests, or project configuration. Request approval before applying the copy or making a commit.

## Adoption pass

Do not build or refactor production code. Reverse-document intended requirements, as-built design and code map, a QA baseline, and review findings. Present non-security debt to the user for fix-now versus accepted-debt triage. Record accepted debt with rationale. Future changes follow the ordinary user gates and increment workflow.
