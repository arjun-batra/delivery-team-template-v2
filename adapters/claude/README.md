# Claude Code adapter

Claude Code uses `CLAUDE.md`, `.claude/agents/`, and `.claude/commands/`. These files preserve the existing Claude-facing commands while `WORKFLOW.md` is the cross-platform policy source.

When changing the workflow, edit `WORKFLOW.md` first and then update the adapter only where a Claude-specific instruction is required. Avoid embedding a second copy of the workflow in commands.
