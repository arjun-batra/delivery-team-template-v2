---
description: "Start the shared delivery workflow for a new project. Usage: /spin-up-team <one-line idea>"
---

The user wants to start a project with: $ARGUMENTS

Read `WORKFLOW.md` and `CLAUDE.md`. This repository already contains the complete Claude adapter; do not scaffold or embed a duplicate workflow.

1. Invoke the PM agent with the user's idea. It conducts the discovery interview in small batches and writes `docs/idea-brief.md`.
2. Relay its gate-1 go/no-go summary to the user. Do not start requirements without explicit approval.
3. Continue through the requirements, design, increment, and closure gates in `WORKFLOW.md`.

For an existing repository, use `/adopt-team` rather than this command.
