# Required subagent dispatch

This contract applies when the active runtime supports subagents. It gives Claude Code and Codex the same operational workflow. A role is a live worker assignment for non-trivial delivery work, not merely a documentation owner.

## Classify before acting

A **trivial change** is a spelling, formatting, or mechanical documentation correction with no behavior, public interface, configuration, schema, test, deployment, or acceptance-criterion impact. The coordinator may complete it alone and records why dispatch was not required.

Everything else is a **non-trivial increment**. The coordinator must spawn the required workers below. It may run independent read-only investigation in parallel, but assigns one writer per artifact and waits for the required result before continuing.

## Required workers

| Trigger | Dispatch |
|---|---|
| Requirements, scope, or user outcome needs creation or material revision | `delivery-standard` with `delivery/roles/product.md` |
| Architecture, increment plan, contracts, or configuration design needs creation or material revision | `delivery-standard` with `delivery/roles/technical-lead.md` |
| User-facing behavior or interface changes | `delivery-standard` with `delivery/roles/designer.md`, when design review is relevant |
| Any non-trivial implementation or fix | `delivery-standard` with `delivery/roles/developer.md` |
| Implementation/fix is ready for verification | a separate `delivery-standard` with `delivery/roles/qa.md` |
| QA passes and the increment is ready for merge or completion | a separate `delivery-standard` with `delivery/roles/reviewer.md` |
| High-risk architecture, security-sensitive change, migration/deletion, complex concurrency, or unresolved design disagreement | `delivery-deep` with `delivery/roles/deep-review.md` |
| Release or deployment work | `delivery-standard` with `delivery/roles/release.md`; use `delivery-fast` only for bounded evidence collection |

Do not use the same worker thread for implementation and required QA/review. QA and review stay mandatory even when their result is “no issues found.” The coordinator consolidates results and maintains the documentation closeout.

## Dispatch brief and autonomy

Every spawned worker receives: the shared role path, goal and acceptance IDs, relevant input paths/sections, allowed output paths, constraints, checks, and a stop condition. The coordinator reports each spawned worker's role, scope, result, and evidence in its handoff.

Do not pause for acknowledgement, status reporting, handoffs, or ordinary internal transitions. A clear request to implement a bounded change authorizes discovery, requirements refinement, and design updates needed to perform that change. Pause only for a material ambiguity affecting scope, acceptance, architecture, safety, cost, or an external side effect. New projects and material scope changes retain the user approvals in `WORKFLOW.md`.

If subagents, a requested profile, or a required model are unavailable, state that once, continue with the coordinator using the same role procedures, and record the limitation. Never claim that a worker was spawned when it was not.
