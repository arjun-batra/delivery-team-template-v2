---
name: delivery-team
description: Run a gated, artifact-driven software delivery workflow for a new project, an existing project, a change request, or project closure.
---

# Delivery Team Skill

Read `WORKFLOW.md` and `AGENTS.md` before acting.

## Routes

- **New project:** discovery → user gate → requirements → user gate → design/increment plan → user gate → increment loop.
- **Existing project:** reverse-document intended requirements and as-built design; establish a QA baseline; present debt for the user to triage before refactoring.
- **Change request:** update requirements, assess design/increment impact, obtain any needed approval, then resume the increment loop.
- **Closure:** perform the workflow closure checks and write a short retrospective.

Use focused role briefs that name exact files and acceptance criteria. Do not use this skill to bypass user gates or external-action approval.
