# Codex adapter

Codex discovers the root `AGENTS.md` automatically. It supplies the shared workflow instructions and points to the repository skill at `.agents/skills/delivery-team/`.

Start a new project by asking Codex to use the delivery-team workflow with the project idea. For an existing repository, ask it to adopt the workflow and reverse-document the current system before implementing changes.

The adapter deliberately avoids fixed model names and provider-specific slash commands. Codex task creation, subagents, worktrees, and approvals remain controlled by the active Codex environment.
