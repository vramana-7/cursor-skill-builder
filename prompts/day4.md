# Day 4 - Output Evaluation (60 minutes)

Goal: Measure output quality with a repeatable rubric, then improve the prompt deliberately.

## Inputs

- Prompt template: `prompts/template.md`
- Rubric: `evals/day4-rubric.md`
- Output log: `examples/day4-output.md`

## Step 1 (20 min): Generate baseline output

1. Run `prompts/template.md` with your weekly context.
2. Save the output as "Baseline Output" in `examples/day4-output.md`.

## Step 2 (20 min): Score baseline output

Using `evals/day4-rubric.md`, score each criterion (1-5):
- Specificity
- Actionability
- Constraint Fit
- Clarity
- Risk Awareness
- Progress Measurability

Record the total score and 2-3 short observations.

## Step 3 (15 min): Improve one prompt element

Change exactly one part of `prompts/template.md`:
- output format, or
- constraints, or
- success criteria

Rerun the prompt and save as "Improved Output".

## Step 4 (5 min): Rescore and compare

Score the improved output with the same rubric.
Document score change and one lesson learned.

## Suggested Commit

```bash
git add .
git commit -m "Complete Day 4 output evaluation with rubric scoring"
git push
```
