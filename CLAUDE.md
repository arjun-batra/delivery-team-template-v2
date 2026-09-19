# Claude delivery-team adapter

Read `WORKFLOW.md` and `delivery/manifest.json` before delivery work. They are the provider-neutral source; load only the role or operation procedure needed for the current phase.

Claude commands and Codex skills have identical names with `/` replaced by `$`: `spin-up-team`, `adopt-team`, `migrate-v1`, `resume-work`, `sync-team`, `retro`, and `big-guns`. Claude role adapters in `.claude/agents/` point to the same shared role procedures used by Codex.

Follow the shared gates, evidence standards, and approval boundaries exactly. Ask only for material ambiguity or an external side effect.
