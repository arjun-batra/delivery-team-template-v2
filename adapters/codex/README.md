# ChatGPT Codex adapter

Repository skills in `.agents/skills/` preserve the [same operation names](../../README.md#start-or-migrate-a-project) with `$` replacing Claude's `/`. Use `$delivery-team` for general routing.

The coordinator follows `delivery/execution.md`. Native standalone profiles in `.codex/agents/` bind the fast, standard, and deep workers to the models in `delivery/model-routing.json`. Pass a shared role path and compact task brief; changing tier means selecting another profile for the remaining work. No global configuration or permission changes are required.

This requires a Codex runtime supporting standalone custom-agent TOML files and access to the selected models. Reload/restart if profiles are not discovered. Profile model/effort settings take precedence over spawn defaults. Verify runtime metadata where possible; report missing controls and use the capable current model instead of claiming a switch. These files do not change a plain ChatGPT chat's model or the user's main-session model.

Configuration format: [official Codex subagent documentation](https://developers.openai.com/es-419/docs/agent-configuration/subagents).
