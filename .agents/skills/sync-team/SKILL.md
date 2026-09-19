---
name: sync-team
description: Safely preview and sync workflow files from the delivery-team template without overwriting project content.
---

# Sync the delivery team

Fetch the upstream template into a platform-appropriate temporary workspace. Compare its workflow files with this repository before changing anything. Never overwrite `README.md`, `docs/`, source, tests, or project configuration.

Report the version jump and relevant changelog entries. Request approval before applying changes or committing. Record the adopted version in the adapter-local template-version file and remind the user that a restart may be needed for new skills or commands.
