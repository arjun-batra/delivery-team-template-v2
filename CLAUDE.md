# Claude Code Delivery Adapter

Read `WORKFLOW.md` first. It is the provider-neutral source of truth. This file contains only Claude Code mechanics.

## Roles

| Claude agent | Workflow role |
|---|---|
| `pm` | Product |
| `tech-lead` | Technical lead |
| `lead` | Lite-mode product and technical lead |
| `designer` | Designer |
| `dev` | Developer |
| `qa` | QA |
| `reviewer` | Reviewer |
| `release` | Release |
| `big-guns` | Optional deep reviewer |

Use the agent definitions in `.claude/agents/`. The main thread orchestrates and enforces workflow gates; agents communicate through owned artifacts, not transient chat.

## Commands

Claude commands and Codex skills provide the same user-facing delivery operations:

| Claude Code | ChatGPT Codex |
|---|---|
| `/spin-up-team` | `$spin-up-team` |
| `/adopt-team` | `$adopt-team` |
| `/resume-work` | `$resume-work` |
| `/sync-team` | `$sync-team` |
| `/retro` | `$retro` |
| `/big-guns` | `$big-guns` |

Read only the artifacts relevant to the active phase. Every subagent brief names exact files and acceptance criteria; reference paths and sections instead of pasting document contents.

## Claude-specific constraints

- Pass the explicit model configured in the target agent’s frontmatter when spawning a Claude subagent. See `.claude/orchestrator-checklist.md`.
- `big-guns` is user-invoked only and appends `[DEEP]` findings to `docs/review-log.md`.
- A session restart may be needed after adding or changing Claude agents or commands.
