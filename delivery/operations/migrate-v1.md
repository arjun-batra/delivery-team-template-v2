# Migrate a v1 delivery team

Establish a defensible installed v1 baseline from `.claude/template-version`, root `VERSION`, or Git history; otherwise stop and ask. Create a three-way preview against the current template. Preserve README, project docs, source, tests, configuration, and unknown files. After approval, update only manifest-managed workflow assets, create the state index only if absent, record the adopted version in `.claude/template-version`, run the workflow audit and project checks, and request approval before external side effects.

Include the manifest's native `.codex/agents/` and Claude worker profiles in the preview. Preserve unknown files and local model overrides; merge only template-owned assets. Check that the installed runtime discovers the profiles and supports their configured models, or report the routing limitation. Never overwrite global provider settings.
