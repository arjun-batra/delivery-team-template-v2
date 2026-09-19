---
description: "Preview and sync workflow files from the delivery-team template. Usage: /sync-team"
---

Read `WORKFLOW.md` and `CLAUDE.md`. This command has the same outcome and approval boundaries as Codex `$sync-team`.

Fetch the upstream template into a platform-appropriate temporary workspace. Compare the template workflow files with this repository and report the version jump and relevant changelog entries before changing anything.

Copy only workflow files. Never overwrite `README.md`, `docs/`, source, tests, or project configuration. Record the adopted version in `.claude/template-version`. Request approval before applying changes or making a commit. A session restart may be needed to load changed agents or commands.
