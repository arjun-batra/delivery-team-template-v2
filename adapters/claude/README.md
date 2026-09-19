# Claude Code adapter

Claude Code uses `CLAUDE.md`, `.claude/agents/`, and `.claude/commands/`. These files provide Claude-specific mechanics; `WORKFLOW.md` is the cross-platform policy source.

The six named Claude commands have same-name Codex skill counterparts (replace `/` with `$`). When changing behavior, update `WORKFLOW.md` first, then preserve equivalent user-facing outcomes in both adapters.
