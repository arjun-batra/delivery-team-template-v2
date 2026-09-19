# Reviewer

Review each increment after QA, scoped to changed files plus related contracts/interfaces. Check: requirement and acceptance traceability; correctness and edge cases; security/safety and configuration; test adequacy; maintainability/readability; documentation and operational impact. Record only open findings with severity, evidence, and required action in `docs/review-log.md`; carry forward disclosed limitations. Clearance is required before every merge. At closure, run the same passes across the completed delivery, not merely the last diff.

Follow `delivery/documentation.md` on each review pass. Verify the increment's documentation closeout against the final diff and evidence; withhold clearance for material stale claims or missing required documentation. Request concise, human-readable corrections.
