# Delivery Team — Project Template

New project = new repo from this template. The multi-agent team (.claude/agents/),
workflow (CLAUDE.md), and git permissions (.claude/settings.json) travel with the repo —
so all commands work in any Claude Code session: Desktop, terminal, web, or mobile.

## Start a project
1. GitHub -> "Use this template" -> create your new repo
2. Open it in Claude Code (Desktop Code session on a clone, or Claude Code on the web — no local folder needed)
3. Type: /spin-up-team <your idea>
4. Answer PM's discovery questions; approve at the gates

## Resume work (fresh session, any device)
Open a Claude Code session in the repo and type: /resume-work
It reconstructs state from docs/ and git history, tells you exactly where things stand,
and continues the pipeline from that point after you confirm.

## Adopt into an EXISTING project
- Repo already has .claude/commands/adopt-team.md (template-born or previously adopted): type /adopt-team
- Machine with the user-level install: /adopt-team works in any repo
- First-time adoption from web/mobile (no command available anywhere): paste this bootstrap prompt:

  "Clone https://github.com/arjun-batra/delivery-team-template (shallow) to a temp dir, read
  .claude/commands/adopt-team.md from it, and follow those instructions exactly in this repo."

After the first adoption the commands live in the repo, so every later session on any device has them.

## Git behavior (built into CLAUDE.md)
- Branch per increment; every merge to main is a shippable end-to-end feature
- Commit when QA passes, merge when reviewer clears, release tag at closure

## Change requests
Open a Claude Code session in the repo: "Change request: <what you want>"
PM assesses -> requirements updated -> design updated -> loop resumes.

## Retrospectives and template versioning
- At Phase 4 closure (or on demand), run `/retro`: it mines this project's docs/git history for delivery friction and proposes template edits — see `docs/retro.md` after running.
- Any template change bumps `VERSION` and adds a `CHANGELOG.md` entry — no silent template edits.
- `/sync-team` reports "synced from vX -> vY" with the relevant CHANGELOG entries, and records the new version in `.claude/template-version`.

## Token efficiency
- Run the main session on Sonnet; escalate to Opus manually only for individual hard design decisions.
- One increment per session: end the session and use /resume-work fresh next time.
- Prefer /clear + /resume-work over /compact — compaction is itself a large paid summarization and lossier than the docs.
- Use /usage to monitor spend.
