# Sync workflow updates

Fetch the current template into a temporary workspace, compare manifest-managed workflow assets, and present a preview. Protect README, project docs, source, tests, configuration, and unknown files. After approval apply only managed assets, preserve local project adaptations explicitly, run the workflow audit and project checks, and request approval before external side effects.

Include the manifest's native `.codex/agents/` and Claude worker profiles in the preview. Preserve unknown files and local model overrides; merge only template-owned assets. Check that the installed runtime discovers the profiles and supports their configured models, or report the routing limitation. Never overwrite global provider settings.
