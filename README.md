# Cursor

Vishal's Personal Cursor Projects

## Cursor Skill Builder

A lightweight 7-day practice project to sharpen prompt engineering and Cursor workflows.

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

## Project Structure

- `prompts/` - reusable prompt frameworks and daily exercises
- `examples/` - saved prompt outputs and reflections
- `src/` - small tool you improve over the week
- `evals/` - test inputs and quality scoring (starting Day 4)

## This Week Roadmap

- Day 1: baseline prompting + first GitHub publish
- Day 2: reusable prompt framework
- Day 3: Cursor workflow drills
- Day 4: output evaluation
- Day 5: guardrails and refactor
- Day 6: GitHub polish
- Day 7: demo and reflection
