# ChatGPT Codex adapter

Codex discovers root `AGENTS.md` automatically. Repository skills live in `.agents/skills/` and provide the same named delivery operations as Claude commands.

| Claude Code | ChatGPT Codex |
|---|---|
| `/spin-up-team` | `$spin-up-team` |
| `/adopt-team` | `$adopt-team` |
| `/resume-work` | `$resume-work` |
| `/sync-team` | `$sync-team` |
| `/retro` | `$retro` |
| `/big-guns` | `$big-guns` |

Use `$delivery-team` for general routing. Skills preserve the shared workflow, artifacts, user gates, and approval rules while leaving task creation, models, worktrees, and permissions to the active Codex environment.

A skill is discovered from `.agents/skills/`; restart Codex if newly added skills do not appear.
