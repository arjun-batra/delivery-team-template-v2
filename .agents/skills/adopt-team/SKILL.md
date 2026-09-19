---
name: adopt-team
description: Adopt this delivery workflow into an existing project and reverse-document the system before changing it.
---

# Adopt a delivery team

Install only template workflow files: `WORKFLOW.md`, `AGENTS.md`, `.agents/`, `.claude/`, `.claudeignore`, `.github/workflows/audit.yml`, and `scripts/audit_template.py`. Do not overwrite project `README.md`, `docs/`, source, tests, or configuration. Preview the diff and request approval before applying or committing changes.

Then make no production-code changes: document intended requirements, as-built design and code map, QA baseline, and review findings. Present non-security debt for user triage; record accepted debt with rationale. Use the normal gates for all later changes.
