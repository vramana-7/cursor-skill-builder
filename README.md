# Cursor

Vishal's Personal Cursor Projects

## Cursor Skill Builder

A lightweight 7-day practice project to sharpen prompt engineering and Cursor workflows.

## About This Project

- What it does: turns weekly context into clear priorities, next actions, and concise rationale through prompt iterations.
- What I practiced: prompt design (vague vs structured vs constrained), Cursor workflow, and first GitHub publish flow.
- What's next: continue iterating daily and publish progress through Day 7.

## Current Progress

- Day 1: completed and published
- Day 2: completed and published
- Day 3: completed and published
- Day 4: completed and published
- Day 5-7: in progress

## Week Goal

Build a tiny but useful tool that turns your weekly context into:
- top 3 priorities
- clear next actions
- a short rationale

This repo starts with **Day 1** so you can practice immediately and publish your first GitHub project.

## Day 1 (60 minutes)

### 1) Prompt baseline exercise (20 min)
- Open `prompts/day1.md`
- Run the 3 prompt versions (vague, structured, constrained)
- Save outputs in `examples/day1-output.md`

### 2) Build a tiny local tool (20 min)
- Open `src/planner.py`
- Run:

```bash
python3 src/planner.py
```

- Paste your own weekly context when prompted

### 3) Reflect and tighten your prompt (10 min)
- Update `prompts/template.md` with one improvement
- Add one short note to `examples/day1-output.md`: what improved and why

### 4) First commit + GitHub push (10 min)
- Initialize branch if needed:

```bash
git add .
git commit -m "Initialize Day 1 prompt practice scaffold"
```

- Create a repository on GitHub named `cursor-skill-builder`
- Connect and push (replace `<your-username>`):

```bash
git branch -M main
git remote add origin https://github.com/<your-username>/cursor-skill-builder.git
git push -u origin main
```

## Day 2 (60 minutes)

### 1) Review Day 1 outputs (20 min)
- Identify what structure and constraints improved quality
- Note what was still too generic

### 2) Build reusable template (25 min)
- Open `prompts/template.md`
- Run it with your weekly context
- Save results to `examples/day2-output.md`

### 3) Tighten and rerun (10 min)
- Improve one part of the template (format, constraints, or success criteria)
- Run again and compare outputs

### 4) Commit + push (5 min)

```bash
git add .
git commit -m "Add Day 2 reusable prompt framework and outputs"
git push
```

## Day 3 (60 minutes)

### 1) Fast edit loop (15 min)
- Open `src/planner.py`
- Add one visible output improvement (for example: `Top Win`)
- Run `python3 src/planner.py` and verify the change

### 2) Prompt-to-file workflow (20 min)
- Open `prompts/template.md`
- Add a measurable progress tracker requirement
- Run the template and save output notes in `examples/day3-output.md`

### 3) Review + commit workflow (15 min)
- Review file changes in Source Control
- Commit with a clear message
- Push/sync and verify on GitHub

### 4) Reflection (10 min)
- Record easiest step, friction point, and one reusable shortcut in `examples/day3-output.md`

## Day 4 (60 minutes)

### 1) Generate baseline output (20 min)
- Run `prompts/template.md` with weekly context
- Save as baseline in `examples/day4-output.md`

### 2) Score baseline with rubric (20 min)
- Use `evals/day4-rubric.md`
- Score 6 categories (1-5 each) and total out of 30
- Record 2-3 observations

### 3) Improve one prompt element (15 min)
- Change exactly one part of the prompt (format, constraints, or success criteria)
- Rerun and save improved output in `examples/day4-output.md`

### 4) Rescore and compare (5 min)
- Score improved output with same rubric
- Document score delta and one lesson for Day 5

## Project Structure

- `prompts/` - reusable prompt frameworks and daily exercises
- `examples/` - saved prompt outputs and reflections
- `src/` - small tool you improve over the week
- `evals/` - test inputs and quality scoring (starting Day 4)

## This Week Roadmap

- Day 1: baseline prompting + first GitHub publish (done)
- Day 2: reusable prompt framework (done)
- Day 3: Cursor workflow drills (done)
- Day 4: output evaluation (done)
- Day 5: guardrails and refactor
- Day 6: GitHub polish
- Day 7: demo and reflection
