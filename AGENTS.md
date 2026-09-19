# Codex delivery-team adapter

Read `WORKFLOW.md` and `delivery/manifest.json` before delivery work. They are the provider-neutral source; load only the role or operation procedure needed for the current phase.

Use `$spin-up-team`, `$adopt-team`, `$migrate-v1`, `$resume-work`, `$sync-team`, `$retro`, or `$big-guns` for named operations. Use `$delivery-team` to route general work.

Follow the shared gates, evidence standards, and approval boundaries exactly. Make routine implementation choices within an approved design; ask only when a material ambiguity affects scope, acceptance, architecture, safety, or an external side effect.

For automatic task routing, follow `delivery/execution.md` and select a native `.codex/agents/delivery-<tier>.toml` worker, passing the shared role path. These standalone profiles set model and reasoning effort for spawned agents. Select another tier profile to escalate; profile settings can override spawn settings. Preserve the user's main-session model. If custom agents/model selection are unavailable, follow the shared workflow on a capable available model and disclose the limitation.
