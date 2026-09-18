# Delivery Team Workflow

This is the provider-neutral source of truth. Claude Code and Codex adapters implement it; neither may weaken its gates or safety rules.

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

Decisions belong in their owner’s artifact. Do not treat chat history as project memory.

## Gates

1. **Discovery:** establish users, outcome, scope, constraints, risks, and whether this is a small tool or a product. The user explicitly approves proceeding.
2. **Requirements:** write independently testable FR-NNN/NFR-NNN items. Ambiguity is a question, never an assumption. The user approves them.
3. **Design:** map every requirement to an acceptance criterion and ordered, end-to-end vertical increments. Identify verification that needs unavailable services or a browser before implementation starts. The user approves the plan.
4. **Increment loop:** developer plans and builds one increment; QA runs regression and real-entry-point checks; reviewer checks the changed scope and traceability. Resolve blockers before the next increment.
5. **Closure:** QA performs end-to-end verification; reviewer performs a full audit; requirements are accounted for; release verifies or dry-runs deployment when applicable.

`docs/design/increment-plan.md` is the only status source for increments. Every merge to `main` must be a working vertical slice.

## Non-negotiables

- Do not implement before the applicable user gate.
- Keep configurable values out of source code. For LLM projects, prompts and model parameters are configuration.
- UI, layout, accessibility, and editability claims require live-artifact evidence, not only source inspection.
- Execute artifacts that run outside tests (for example migrations, IaC, or deployment scripts) in an appropriate safe environment; re-run when idempotence matters.
- Run the checks configured by CI, the full test suite, and a real entry-point smoke test before declaring an increment ready.
- Keep docs synchronized with Git. A contradiction is a defect to resolve before proceeding.
- Never push, merge, deploy, change visibility, or otherwise create an external side effect without the user’s current approval.

## Change requests and retrospectives

Route a change through requirements, design, and affected increment planning before implementation. At closure, capture 3–5 evidence-backed delivery lessons in `docs/retro.md`; propose template changes separately from project-specific changes.
