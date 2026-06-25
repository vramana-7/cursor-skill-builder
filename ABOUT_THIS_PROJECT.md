# About This Project

## Why This Exists

`cursor-skill-builder` is a 7-day execution project created to demonstrate how AI-assisted workflows can improve planning quality, consistency, and delivery discipline.

The intent was not to build a large product. The intent was to show repeatable problem-solving: start with a lightweight process, improve it daily, measure quality, and publish progress transparently.

## Context

This project was completed as a daily practice sprint and published in real time on GitHub.

The core challenge addressed:
- weekly planning outputs are often vague or inconsistent
- individuals and teams lose momentum without clear next actions
- process improvements are hard to prove without visible artifacts

## What Was Built

Over 7 days, this repository evolved from simple prompt experiments into a structured workflow with:
- reusable planning templates
- scoring rubrics and guardrails
- iterative refinements to a small local planning tool
- documentation for contribution and change tracking

Each day introduced a focused improvement and captured evidence in versioned files.

## Business and Team Impact

This work demonstrates capability in areas that matter to delivery-focused teams:
- **Execution rigor:** daily cadence from idea -> artifact -> commit -> publish
- **Quality mindset:** outputs were evaluated with rubrics, not just intuition
- **Operational clarity:** guardrails reduced ambiguity and made outputs more actionable
- **Knowledge sharing:** documentation was improved for onboarding and collaboration
- **Continuous improvement:** measurable gains were tracked across iterations

## Outcomes

- Completed and published a full 7-day improvement cycle
- Improved output quality score from baseline to higher-quality reruns using targeted prompt changes
- Established a reusable framework that can support personal productivity and team planning workflows

## Personal Goals

Through this project, I wanted to test and strengthen my ability to:
- self-direct and execute consistently
- blend technical tools with practical business outcomes
- prioritize measurable improvement over one-time output
- maintain strong documentation, communication, and delivery hygiene

## How To Use This

You can use this project in under 15 minutes for your own weekly planning.

### Option 1: Run the local planner script

From the repository root:

```bash
python3 src/planner.py
```

Paste a few weekly priorities (one per line), then press `Ctrl-D` to submit.

Example input:

```text
- Finalize QBR draft
- Rehearse customer demo
- Share weekly team update
```

Example output includes:
- Top Priorities
- Top Win
- Next Action
- Top Risk

### Option 2: Use the reusable prompt template

1. Open `prompts/template.md`
2. Replace placeholders with your context:
   - projects
   - deadlines
   - blockers
   - constraints
   - personal routines
3. Run the prompt in Cursor Chat
4. Save your output in a file like `examples/my-week-output.md`

### Option 3: Evaluate quality before you act

To avoid vague planning, score your output with:

- `evals/day4-rubric.md` (quality scoring)
- `evals/day5-guardrails.md` (actionability and safety checks)

This helps you improve the plan before execution.

## Next Steps

The next iteration would focus on:
- lightweight automation of output logging
- stronger progress analytics over time
- broader adoption patterns for team-level use

---

If you want a quick starting point, the most relevant files are:
- `README.md` (day-by-day execution record)
- `examples/` (evidence of output evolution)
- `evals/` (quality rubric and guardrails)
- `CHANGELOG.md` (progress narrative)
