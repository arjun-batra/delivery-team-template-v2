# Adopt an existing project

Inspect the repository and Git history, then propose a protected installation preview. Preserve source, tests, project configuration, README, and existing docs; install only manifest-managed workflow assets after approval. Reverse-document current behavior into the owned delivery artifacts, create the state index only if absent, run the workflow audit and project checks, and request approval before external side effects.

Include the manifest's native `.codex/agents/` and Claude worker profiles in the preview. Preserve unknown files and local model overrides; merge only template-owned assets. Check that the installed runtime discovers the profiles and supports their configured models, or report the routing limitation. Never overwrite global provider settings.
