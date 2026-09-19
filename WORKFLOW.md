# Delivery Team Workflow

This is the provider-neutral source of truth. Claude Code and ChatGPT Codex adapters implement this workflow; neither may weaken its gates, verification, or approval rules.

## Roles and artifacts

| Role | Owns |
|---|---|
| Product | `docs/idea-brief.md`, `docs/requirements.md`, `README.md` |
| Technical lead | `docs/design.md`, `docs/design/increment-plan.md`, `docs/code-map.md` |
| Designer | `docs/ux-spec.md` when there is a user-facing interface |
| Developer | production code, configuration, `docs/handoff.md` |
| QA | tests and `docs/test-report.md` |
| Reviewer | `docs/review-log.md` |
| Release | `docs/runbook.md` and deployment configuration |

Decisions belong in their owner’s artifact. A decision not recorded there did not happen.

## Context and state

Read `docs/delivery-state.md` first to locate the active phase and authoritative artifacts. Read only the documents relevant to that phase; reference requirement, acceptance-criterion, bug, and finding IDs rather than copying prose.

`docs/design/increment-plan.md` is the only status source for increments. `docs/delivery-state.md` is a navigation index: it must point to the source of truth and never restate increment completion, QA verdicts, or reviewer verdicts.

## Gates

1. **Discovery:** establish users, outcome, scope, constraints, risks, and whether this is a small tool or product. The user explicitly approves proceeding.
2. **Requirements:** write independently testable FR-NNN/NFR-NNN items. Ambiguity is a question, never an assumption. The user approves them.
3. **Design:** map every requirement to acceptance criteria and ordered, end-to-end vertical increments. Identify unavailable verification environments before implementation. The user approves the plan.
4. **Increment loop:** developer plans and builds one increment; QA runs regression and real-entry-point checks; reviewer checks changed scope and traceability. Resolve blockers before the next increment.
5. **Closure:** QA performs end-to-end verification; reviewer performs a full audit; product accounts for every requirement; release verifies or dry-runs deployment when applicable.

## Delivery rules

- A small tool may use lite mode: one lead owns product and technical-lead artifacts; designer and release remain conditional; reviewer runs at closure. A product uses the full roles above.
- Before Gate 3, verify every requirement claimed by an increment has a matching increment acceptance criterion. Route unavailable live-network, external-service, browser, or automation verification to the user once for a decision.
- Each increment is a shippable vertical slice. Developer writes a short build plan, implements, runs the configured checks, and writes a handoff.
- QA reports PASS or files bugs. After three fix cycles, escalate to the technical lead.
- Reviewer audits files changed since its last clearance, validates claimed FR/NFR traceability, and carries forward recurring disclosed limitations as findings.
- A change request updates requirements, design impact, and affected increments before implementation. Batch related changes where practical.
- At closure, write 3–5 evidence-backed delivery lessons in `docs/retro.md`; propose template changes separately from project changes.

## Verification and quality

- Keep configurable values out of source code. For LLM projects, prompts and model parameters are configuration.
- UI, layout, accessibility, and editability claims require live-artifact evidence, not only source inspection.
- Execute artifacts that run outside tests, such as migrations, IaC, and deployment scripts, in an appropriate safe environment; re-run where idempotence matters.
- Before declaring an increment ready, run CI-equivalent checks, the full suite, and a real entry-point smoke test.
- Keep docs synchronized with Git. A contradiction is a defect to resolve before proceeding.
- Keep active artifacts concise: QA retains the latest run and open bugs; reviewer retains open findings; owners archive only resolved entries in their own archives. Never use archives for ordinary task context.

## Git and approval rules

- Work on an increment branch when the project is not explicitly using the solo/low-stakes exception.
- Commit code and the documentation it changes together after QA passes. Merge only after reviewer clearance.
- Ask for current approval before any commit, push, pull request, merge, tag, deployment, visibility change, or other external side effect. No adapter may pre-approve these actions.
