# Agent Model Enforcement Checklist

## Critical Rule

**The Orchestrator runs on Haiku 4.5; every subagent MUST be spawned with an explicit `model:` parameter matching the agent's configured model in `.claude/agents/<type>.md` frontmatter.**

This is non-negotiable. Violations result in underperforming agents and incomplete work. The urmilsloa project discovered INC-1 and INC-2 dev work was completed on Haiku 4.5 instead of configured Sonnet model — this checklist prevents that going forward.

## Agent Model Reference

| Agent | Model | Reason |
|-------|-------|--------|
| pm | `"opus"` | Product discovery requires nuanced judgment and long-form synthesis |
| tech-lead | `"opus"` | Architecture decisions need reasoning depth and system design thinking |
| lead (lite mode) | `"opus"` | Combined pm+tech-lead role requires full capability |
| designer | `"sonnet"` | UX/UI design decisions require aesthetic judgment and design systems thinking |
| dev | `"sonnet"` | Implementation of complex features requires code generation and debugging capability |
| qa | `"sonnet"` | Test design and regression analysis require comprehensive reasoning |
| reviewer | `"sonnet"` | Code review audits require consistency checking and architectural understanding across the codebase |
| release | `"haiku"` | Deployment orchestration is procedural; Haiku 4.5 is sufficient for runbook execution |
| big-guns | `inherit` | Deep audit agent inherits from parent session model; do not override |

## Correct vs. Incorrect Agent() Calls

### ✅ Correct

```python
Agent({
  description: "PM interviews user on project scope",
  prompt: "Interview the user about...",
  subagent_type: "pm",
  model: "opus"  # Explicit model parameter
})
```

```python
Agent({
  description: "Tech Lead designs system",
  prompt: "Design the system per requirements.md §3; files: src/core.py, src/api.py",
  subagent_type: "tech-lead",
  model: "opus"
})
```

```python
Agent({
  description: "Dev implements INC-1",
  prompt: "Implement INC-1 per design.md §4; files: src/handler.py",
  subagent_type: "dev",
  model: "sonnet"
})
```

### ❌ Incorrect

```python
Agent({
  description: "PM interviews user",
  prompt: "Interview..."
  subagent_type: "pm"
  // Missing model parameter — Haiku 4.5 will be used by default
})
```

```python
Agent({
  description: "QA tests increment",
  prompt: "Test INC-2...",
  subagent_type: "qa"
  // Missing model — QA will run on Haiku 4.5 instead of Sonnet, losing capability
})
```

## How to Verify

On every subagent spawn:

1. **Check the call**: Does the `Agent({...})` call include `model: "<correct_model>"`?
2. **Verify the model**: Does it match the `.claude/agents/<type>.md` frontmatter?
3. **Review commit footer**: Every commit with agent spawning work should show:
   ```
   Claude-Session: https://claude.ai/code/session_...
   ```
   and the model used MUST match the documented model for that agent type (visible in commit context/logs).

## History: Known Violations

### urmilsloa project
- **INC-1 dev work** (commit `abc123...`): dev agent spawned without model parameter; ran on Haiku 4.5 instead of Sonnet. Result: incomplete implementation, missing edge cases.
- **INC-2 dev work** (commit `def456...`): same violation; Haiku 4.5 dev agent, lost reasoning capability. Required rework.

**Lesson**: Explicit model parameter is not optional. Every orchestrator and agent spawn must enforce this.

## Orchestrator Checklist

- [ ] Before spawning any subagent, confirm `.claude/agents/<type>.md` has `model: <value>` in frontmatter
- [ ] Every `Agent({...})` call includes `model: "<correct_model_from_frontmatter>"`
- [ ] No exceptions for "quick" tasks — model enforcement applies universally
- [ ] On review: diff the code for any `Agent()` calls without explicit `model:` parameter
- [ ] Document violations in this file's History section so the pattern is visible

## References

- `.claude/agents/pm.md` — model frontmatter for pm agent
- `.claude/agents/tech-lead.md` — model frontmatter for tech-lead agent
- `.claude/agents/designer.md` — model frontmatter for designer agent
- `.claude/agents/dev.md` — model frontmatter for dev agent
- `.claude/agents/qa.md` — model frontmatter for qa agent
- `.claude/agents/reviewer.md` — model frontmatter for reviewer agent
- `.claude/agents/release.md` — model frontmatter for release agent
- `.claude/agents/big-guns.md` — model frontmatter for big-guns agent
- `CLAUDE.md` § Orchestrator rules — links back to this checklist
