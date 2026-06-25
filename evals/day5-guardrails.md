# Day 5 Guardrails Checklist

Use these to improve reliability and quality of planning outputs.

## Prompt Guardrails (pick 2-4)

- Require measurable targets for each priority (date, count, or deliverable).
- Force action granularity: each action must be startable in under 30 minutes.
- Limit scope: exactly 3 priorities, no extras.
- Ban vague phrases: no "stay focused", "work hard", "do your best".
- Require one risk + one mitigation per priority.
- Require a progress tracker with checkbox state and overall percent.
- Set max output length (for example: 240-280 words).
- Force assumptions policy: if context is missing, state one assumption and continue.

## Output Validation Checklist

Mark each as pass/fail:

- [ ] Priorities are outcome-based (not activity-only)
- [ ] Actions are concrete and immediately startable
- [ ] Deadlines/constraints are reflected
- [ ] Risks and mitigations are practical
- [ ] Progress is measurable and updateable
- [ ] Language is concise and non-generic

## Refactor Guardrails (code)

- Keep function behavior consistent where possible.
- Use small, named helper functions for readability.
- Avoid unnecessary complexity.
- Preserve CLI usage (`python3 src/planner.py`).
