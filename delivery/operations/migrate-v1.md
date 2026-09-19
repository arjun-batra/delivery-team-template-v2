# Migrate a v1 delivery team

Establish a defensible installed v1 baseline from `.claude/template-version`, root `VERSION`, or Git history; otherwise stop and ask. Create a three-way preview against the current template. Preserve README, project docs, source, tests, configuration, and unknown files. After approval, update only manifest-managed workflow assets, create the state index only if absent, record the adopted version in `.claude/template-version`, run the workflow audit and project checks, and request approval before external side effects.
