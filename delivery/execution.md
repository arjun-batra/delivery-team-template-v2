# Efficient execution and model routing

The coordinator reads this before planning or delegating. Minimize total effort per accepted increment, including retries and review. A smaller model or more agents is not automatically cheaper.

## Use only the agents needed

- Default to one coordinator performing the active role. Roles define responsibilities, not a requirement to spawn a team. Delegate for independent verification, separable parallel work, or a substantial search/log task that would crowd the main context.
- Keep at most two workers active by default, and one writer per artifact. No recursive delegation. Keep the QA and reviewer passes; prefer a separate reviewer context, and disclose when only self-review is available.
- Size increments as coherent, testable vertical slices. Avoid both tiny handoffs and oversized changes. Load only relevant role instructions, artifact sections, and affected contracts.
- Search paths/symbols before reading whole files. Use scripts for deterministic checks. Return summaries plus evidence paths, preserving exit codes and full logs outside the prompt.
- Reuse a worker for follow-up on the same task and model when supported. Do not broadcast histories or ask several agents to repeat the same analysis.

## Choose a model for each task

Use the active provider's mapping in `delivery/model-routing.json`; these are starting defaults, not a claim of globally lowest cost. Honor explicit user model choices, account availability, supported reasoning levels, and configured spending limits.

| Tier | Suitable work |
|---|---|
| fast | Targeted lookup, classifying logs, running known checks, mechanical documentation edits from verified facts |
| standard | Normal implementation/debugging, test design, requirements refinement, UX work, routine review and runbooks |
| deep | Ambiguous architecture, security-sensitive changes, data migration/deletion, complex concurrency, repeated reasoning failure, deep review |

Choose by task risk and ambiguity, not job title. High-risk tasks start at deep; never downgrade them to save tokens. A release role may delegate log collection to fast while retaining deployment judgment at standard/deep.

For each substantive task, the coordinator automatically selects `delivery-fast`, `delivery-standard`, or `delivery-deep`. Pass the appropriate shared role path and task brief. Native profiles bind the model; the runtime adapter explains selection mechanics. Do not spawn for a trivial action solely to change models.

A worker cannot promise to change its own running model. If the current tier cannot resolve a task after one failed reasoning/fix attempt, return a short escalation brief; the coordinator resumes the remaining work at the next capable tier. Reuse evidence and changes, never restart the investigation blindly. Do not escalate model size for a missing credential, network outage, or unavailable test environment. The existing three-cycle QA escalation remains the overall limit.

Select again for the next task; avoid model changes inside a coherent task. Check runtime-reported model metadata where available. If a model/profile is unsupported or substituted, report that once, use a verified capable supported model, and record the actual model or `unverified`. Never claim a switch based only on a prompt or config. If no capable option is available, pause only the affected work. Do not buy credits or switch providers implicitly.

## Compact task briefs and evidence

Give a worker: role path; goal and acceptance IDs; input paths/sections; allowed output paths; relevant constraints; checks and stop condition. Use a few lines, not the full conversation. Return outcome, changed paths, evidence, open risks, and next action; aim for 200 words unless substantive findings require more.

Run targeted checks during fixes. Before increment completion, retain the required full suite, CI-equivalent checks, and real-entry-point smoke test. QA may inspect and reuse evidence for the same code revision/diff, configuration, and environment; rerun checks affected by changes, missing coverage, or questionable evidence. Model changes alone do not invalidate test results.

Use the existing handoff for a compact execution note: tier/requested model, observed model or unverified, retries, and measured total usage/time if available. Do not estimate unavailable counters. Compare accepted work across similar increments using total tokens (including workers and retries), latency, and escaped defects. Tune mappings on measured results; no separate telemetry report is required.
