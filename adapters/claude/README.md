# Claude Code adapter

The coordinator follows `delivery/execution.md` and selects a `delivery-fast`, `delivery-standard`, or `delivery-deep` worker with the shared role path. The profiles' Haiku/Sonnet/Opus defaults are recorded in `delivery/model-routing.json`. Legacy role names remain available with baseline models for direct invocation; automatic routing uses tier workers.

Per-invocation model selection, agent frontmatter, and account/organization settings affect the effective model. Verify what the runtime reports and disclose substitutions or unsupported controls. The user's main-session model is preserved.

See [command equivalents](../../README.md#start-or-migrate-a-project) and [official Claude subagent configuration](https://code.claude.com/docs/en/sub-agents#choose-a-model).


For non-trivial work, Claude must dispatch the workers required by `delivery/dispatch.md`. It does not wait for acknowledgement between routine internal phases.
