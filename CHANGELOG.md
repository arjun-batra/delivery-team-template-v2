# Changelog

All notable changes to the delivery-team-template are recorded here. Any template change bumps `VERSION` and adds an entry here — no silent template edits.

## v2.1.0

Added same-name Codex skills for every Claude delivery command (`$spin-up-team`, `$adopt-team`, `$resume-work`, `$sync-team`, `$retro`, and `$big-guns`). Consolidated provider-neutral policy in `WORKFLOW.md`, added a compact delivery-state navigation index, template structural audit, safer CI defaults, and parity documentation.

## v2.0.0

Split the delivery process into provider-neutral `WORKFLOW.md` and separate Claude Code/Codex adapters. Added root `AGENTS.md` and a repository-scoped Codex delivery skill, removed automatic `git push` approval, and made the template safe to evolve without duplicating the workflow in bootstrapping commands.

## v1.7

pm, tech-lead, and lite-mode `lead` now route to model opus instead of sonnet (discovery/requirements and architecture/design work benefit from the extra reasoning depth); designer/dev/qa/reviewer stay sonnet, release stays haiku. Updated `.claude/agents/{pm,tech-lead,lead}.md` frontmatter, `.claude/orchestrator-checklist.md`'s reference table and example calls, and CLAUDE.md's orchestrator model-enforcement rule and lite-mode note.

## v1.6

Retro-driven (urmilsloa, v0.1.0): a theme shipped "complete" through 5 QA/reviewer passes and a full closure audit without ever being rendered in a browser — added a Non-negotiable barring source/static checks for rendering/layout/accessibility/editability claims (live-artifact evidence required; "can't verify here" halts and routes to the user, never a silent deferral). Reviewer's diff-scoped pass now also re-reads the prior increment's disclosed-but-unresolved limitations and logs them as findings after 2 consecutive mentions, instead of waiting for closure (one project's CI-never-ran gap sat disclosed for 5 increments before being logged). tech-lead now self-checks FR/NFR-to-AC coverage and flags environment-incompatible NFRs to the user once at GATE 3, instead of each increment rediscovering the same gaps independently.

## v1.5

Retro-driven (stock-advisory-analysis, v0.1.0): increment status now lives ONLY in increment-plan.md's `### INC-N` heading — 31 stale-status findings in one project traced to prose duplicated across 5+ docs. dev/qa must run every check the project's CI runs, not just the test suite. Executable artifacts (SQL/IaC/deploy scripts) must be executed, and double-applied where re-runnability matters, before qa passes or reviewer clears. dev mirrors the most recently reviewed sibling object instead of the design's illustrative sample. Artifact owners may read their own archive for hygiene, and may never archive a non-RESOLVED entry.

## v1.4

Add `big-guns` deep-analysis agent (manual-only, model-inherit, `[DEEP]` findings into review log).

## v1.3

Add `/retro` closure loop for mining project friction into template edits. Add `VERSION`/`CHANGELOG.md` versioning with `/sync-team` reporting vX -> vY. Add LLM-project rules: prompts/model params as config (dev, reviewer, tech-lead), nondeterministic-output QA (property assertions + golden set + fixtures), structured logging.

## v1.2

Add `docs/code-map.md` as a living one-page mental model owned by tech-lead/lead, refreshed on structural change. Require dev to write a short build plan before coding. Add reviewer's 6th pass: structure audit (dependency direction, oversized files, duplicated logic, stale code-map).

## v1.1

Token-efficiency optimizations: per-agent model routing (opus for pm/tech-lead, sonnet for dev/qa/reviewer/designer, haiku for release), diff-scoped reviewer audits, lite mode for small tools, document hygiene/archiving rules, `/resume-work` and `/adopt-team` commands.

## v1.0

Initial multi-agent delivery team: pm, tech-lead, designer, dev, qa, reviewer, release agents; phased pipeline with user gates; vertical-slice increments; git workflow and non-negotiables.
