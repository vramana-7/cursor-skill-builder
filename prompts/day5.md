# Day 5 - Guardrails and Refactor (60 minutes)

Goal: make outputs safer and code easier to maintain.

## Inputs

- Guardrail checklist: `evals/day5-guardrails.md`
- Reusable prompt: `prompts/template.md`
- Script to refactor: `src/planner.py`
- Output log: `examples/day5-output.md`

## Step 1 (15 min): Apply prompt guardrails

1. Open `prompts/template.md`.
2. Add 2-3 guardrails from `evals/day5-guardrails.md`.
3. Run with weekly context and save output snapshot.

## Step 2 (20 min): Lightweight refactor in code

Refactor `src/planner.py` to improve readability without changing core behavior.
Suggested changes:
- split output sections into helper functions
- centralize fallback text/constants
- keep output format unchanged except intentional improvements

Run:

```bash
python3 src/planner.py
```

## Step 3 (15 min): Validate guardrails

Check whether generated output:
- avoids generic advice
- uses measurable targets
- includes risk + mitigation
- stays concise and scannable

Record pass/fail notes in `examples/day5-output.md`.

## Step 4 (10 min): Reflection + commit

Capture:
- what guardrail had biggest impact
- what refactor improved most
- one guardrail to keep permanently

## Suggested Commit

```bash
git add .
git commit -m "Complete Day 5 guardrails and planner refactor"
git push
```
