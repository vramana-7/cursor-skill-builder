# Day 1 Prompt Baseline Exercise

Goal: Compare how prompt quality changes output quality.

## Instructions

1. Copy your weekly context into each prompt version.
2. Run all three prompts in Cursor Chat.
3. Save outputs in `examples/day1-output.md`.
4. Compare differences in clarity, actionability, and focus.

---

## Weekly Context Placeholder

Replace this with your real context before running prompts:

- Current projects:
- Deadlines this week:
- Blockers:
- Meetings/constraints:
- Personal goals:

---

## Prompt Version 1: Vague

```text
Help me plan my week based on this context:
[PASTE WEEKLY CONTEXT]
```

## Prompt Version 2: Structured

```text
You are a planning assistant.

Using the weekly context below, produce:
1) Top 3 priorities for this week
2) Next actions for each priority (2-3 actions each)
3) A short rationale (2-4 sentences) explaining why these priorities matter

Weekly context:
[PASTE WEEKLY CONTEXT]
```

## Prompt Version 3: Constrained

```text
You are a pragmatic weekly planning assistant.

Use the context below to produce exactly:
- 3 priorities (each must be outcome-focused and realistic this week)
- For each priority, 2 concrete next actions that can be started in under 30 minutes
- A rationale under 80 words total

Constraints:
- Keep total response under 220 words.
- Use simple language.
- Do not include generic advice.
- If context is missing, state one assumption clearly and continue.

Weekly context:
[PASTE WEEKLY CONTEXT]
```
