# Claude delivery-team adapter

Read `WORKFLOW.md`, `delivery/execution.md`, and `delivery/manifest.json` before delivery work. They are the provider-neutral source; load only the role or operation procedure needed for the current phase, plus `delivery/dispatch.md` for any delivery work.

Claude commands and Codex skills have identical names with `/` replaced by `$`: `spin-up-team`, `adopt-team`, `migrate-v1`, `resume-work`, `sync-team`, `retro`, and `big-guns`. Claude role adapters in `.claude/agents/` point to the same shared role procedures used by Codex.

Follow the shared gates, evidence standards, and approval boundaries exactly. Ask only for material ambiguity or an external side effect.

For non-trivial work, follow `delivery/dispatch.md` exactly: spawn the required `delivery-fast`, `delivery-standard`, or `delivery-deep` subagents with their shared role paths, wait for required QA/review results, and report actual spawned-worker evidence. Their model fields define the default; use the mapped per-invocation model when supported and verify the effective model where exposed. Account/organization overrides may change selection. Preserve the user's main-session model; report unsupported routing instead of claiming it happened.
