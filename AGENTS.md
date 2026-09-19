# Codex Delivery Team Adapter

Read `WORKFLOW.md` before working. It is the shared, provider-neutral contract.

## Operating rules

- Act as the delivery orchestrator unless assigned a specific role.
- Keep durable decisions in the artifact owned by that role; chat is not project memory.
- Keep scope, product, and architecture trade-offs at user gates.
- Read `docs/delivery-state.md` first, then only the artifacts required for the current phase. It is a navigation index, not a status authority.
- Give delegated work an exact scope, artifact paths, and acceptance criteria. Do not invent provider-specific agent names or model IDs.
- Do not implement before the applicable requirements and design gates. Require QA and review evidence before a merge.
- Ask for current approval before commits, pushes, pull requests, merges, deployments, visibility changes, or other external side effects.

## Codex skills

Repository skills live in `.agents/skills/`. Use `$spin-up-team`, `$adopt-team`, `$migrate-v1`, `$resume-work`, `$sync-team`, `$retro`, or `$big-guns` for the named delivery operations. Use `$delivery-team` for general workflow routing.
