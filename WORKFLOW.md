# Delivery Team Workflow

This is the provider-neutral contract. Runtime adapters may add provider mechanics, but may not weaken these gates, evidence, or approval rules. The authoritative operation and role procedures are indexed by `delivery/manifest.json`.

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

Read `docs/delivery-state.md` first. It is a navigation index; `docs/design/increment-plan.md` is the sole increment-status source. Decisions belong in their owner artifact.

## Gates

1. **Discovery:** establish users, outcome, scope, constraints, risks, and product/tool classification; obtain approval.
2. **Requirements:** record independently testable FR-NNN/NFR-NNN items; ask about material ambiguity in scope, acceptance, or architecture; obtain approval.
3. **Design:** map requirements to acceptance criteria and shippable vertical increments; identify unavailable verification environments; obtain approval.
4. **Increment loop:** plan, build, QA, and reviewer clearance for each increment. Expand review to related contracts when an interface changes. Reconcile affected documentation after every pass and complete the documentation closeout before marking an increment done.
5. **Closure:** end-to-end QA, full reviewer audit, product accounting, and release verification or dry run when applicable.

## Documentation

Follow `delivery/documentation.md` whenever creating or changing delivery artifacts. Write for a human reader: concise current facts, decisions, evidence, and next actions. Every role updates affected documents during its pass; the technical lead coordinates an automatic documentation closeout at each increment end, and the reviewer verifies it before clearance.

## Delivery rules

- Lite mode may combine product and technical-lead ownership and omit conditional design/release work, but never skips QA. Reviewer clearance is required before every merge; a full audit is additionally required at closure.
- A change request updates requirements, design impact, and affected increments before implementation.
- QA reports PASS or files bugs; after three fix cycles, escalate to the technical lead.
- Keep configuration out of source. For LLM work, prompts and model parameters are configuration.
- UI, accessibility, layout, editability, migrations, IaC, and deployment claims need appropriate live-artifact evidence.
- Before ready, run configured CI-equivalent checks, the full suite, and a real-entry-point smoke test.
- Keep active artifacts concise: current QA result/open bugs and open reviewer findings only. Archive resolved material outside ordinary task context.
- Commit code and changed documentation together after QA passes. Ask for current approval before commit, push, PR, merge, tag, deployment, visibility change, or another external side effect.
