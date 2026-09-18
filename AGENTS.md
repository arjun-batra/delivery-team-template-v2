# Codex Delivery Team Adapter

Read `WORKFLOW.md` before working. It is the shared workflow contract for this template.

## Operating mode

- Act as the delivery orchestrator unless a task explicitly assigns a different role.
- Keep user decisions at workflow gates; do not silently choose scope, product, or architecture trade-offs.
- Use `docs/` as durable project memory and update only the artifact owned by the active role.
- For substantial parallel work, assign bounded subtasks with the relevant artifact paths and acceptance criteria. Do not invent provider-specific agent names or model IDs.
- Before code changes, establish an approved requirement and design increment. Before a merge, require QA and review evidence.

## Codex conventions

- `AGENTS.md` is the repository instruction entry point. Repository skills live in `.agents/skills/`.
- Keep instructions concise; put reusable procedures in the delivery-team skill and project decisions in `docs/`.
- Ask before external writes such as pushes, pull requests, deployments, or account-setting changes.

## Starting work

For a new project, ask discovery questions in small batches and create `docs/idea-brief.md`. For an existing project, first document its intended behavior and current architecture before proposing changes.
