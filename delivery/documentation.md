# Concise, current documentation

Apply this standard to every delivery artifact, including requirements, design, plans, handoffs, reports, README, UX specs, and runbooks.

## Write for people

- Lead with the outcome or decision. Use plain language, short paragraphs, descriptive headings, and stable IDs with a brief label.
- Keep only information needed to understand, use, verify, or continue the work. Omit narration, repeated context, boilerplate, empty sections, and copied tool logs.
- Give each fact one authoritative home. Link to exact sections, acceptance criteria, findings, or evidence instead of repeating them.
- Prefer a short paragraph or a few bullets; use a table only when comparison is clearer. Explain unfamiliar terms once.
- Keep evidence reproducible: command or check, environment when relevant, result, and a link to details. Concision must not remove acceptance criteria, material decisions, unresolved risks, or verification limits.
- Edit existing text in place. Remove obsolete instructions and broken references; retain significant decision rationale in its owner artifact or archive.

## Refresh after every pass

Before handing off, each role compares its affected artifacts with the current diff, approved decisions, and observed results, then updates them automatically within the authorized scope. This includes implementation, QA, review, and every fix/retest pass. Do not wait for a documentation reminder.

The owner remains accountable for the artifact; a coordinating agent may perform the owner role when no separate agent is available. Route changes outside your ownership to that role before handoff. Never rewrite approved requirements or acceptance criteria to make an implementation appear compliant; obtain the required change approval.

## Close each increment

The technical lead coordinates this closeout after the final fix/retest and before the increment is marked done:

1. Compare the actual increment diff and acceptance criteria with affected requirements, design/contracts, code map, UX spec, README, configuration/setup instructions, and runbook. Inspect only relevant sections; update changed behavior and instructions.
2. Reconcile the handoff, latest QA evidence/open bugs, and reviewer findings with the final implementation. A fix that changes behavior invalidates affected earlier evidence until rechecked.
3. Update the active increment entry in `docs/design/increment-plan.md`: concise delivered outcome, criterion IDs with evidence links, remaining blockers or limitations, and accurate status. Link to QA/review verdicts instead of duplicating them. Keep pending work pending; record an explicit approved deferral when applicable.
4. Refresh `docs/delivery-state.md` pointers and next owner/action without copying increment status. Remove stale TODOs, contradictory claims, duplicated text, and broken references from affected artifacts.
5. Reviewer checks accuracy, readability, and concision before clearance. In the existing increment entry, record one line: `Docs checked: <revision or diff scope>; updated <paths> / no changes needed; gaps <links or none>.` Do not create a separate report.

Any later fix reopens the affected checks. Missing required documentation or material contradictions block completion. Keep code and its documentation in the same delivery change.
