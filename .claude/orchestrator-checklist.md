# Model routing

Use `delivery/execution.md`, `delivery/dispatch.md`, and `delivery/model-routing.json`. Dispatch the required role workers for non-trivial work; do not substitute the orchestrator for developer, QA, or reviewer. Select a tier for the actual task, then invoke its native worker with the shared role path. Verify effective model metadata when available; a configured model is not proof of runtime selection. Main-session model choice belongs to the user.
