# Claude Code adapter

Claude Code uses `CLAUDE.md`, `.claude/agents/`, and `.claude/commands/`. These files provide Claude-specific mechanics; `WORKFLOW.md` is the cross-platform policy source.

The seven named Claude commands have same-name Codex skill counterparts (replace `/` with `$`). Use `/migrate-v1` when upgrading an existing v1 project; use `/adopt-team` only for first-time adoption. When changing behavior, update `WORKFLOW.md` first, then preserve equivalent user-facing outcomes in both adapters.
