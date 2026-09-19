# QA

Derive tests from FR/NFR and increment acceptance criteria. Run regression, real-entry-point, and relevant end-to-end checks; record environment, commands, result, evidence, and bugs in `docs/test-report.md`. For nondeterministic systems, test invariants, use controlled fixtures/recordings where possible, and distinguish deterministic assertions from evaluated behavior. Verify migrations, deployment artifacts, and automation safely and idempotently when applicable. Return PASS or actionable bugs; escalate after three fix cycles.

On every test/retest pass, follow `delivery/documentation.md`: replace stale results, check documented user/setup instructions against observed behavior, and report material documentation defects.
