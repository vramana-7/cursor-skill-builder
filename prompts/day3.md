# Day 3 - Cursor Workflow Drills (60 minutes)

Goal: Build confidence using Cursor end-to-end: edit, run, verify, and commit quickly.

## Deliverables

- Complete 3 workflow drills
- Save outcomes in `examples/day3-output.md`
- Run `src/planner.py` once with your own context

## Drill 1 (15 min): Fast edit loop

1. Open `src/planner.py`
2. Ask Cursor to add one small feature (for example: include a "Top Risk" line)
3. Run:

```bash
python3 src/planner.py
```

4. Confirm the output changed as expected

## Drill 2 (20 min): Prompt-to-file workflow

1. Open `prompts/template.md`
2. Ask Cursor to tighten one constraint (word limit, format, or specificity)
3. Run the updated template with your weekly context
4. Save result to `examples/day3-output.md`

## Drill 3 (15 min): Review and commit workflow

1. Open Source Control
2. Review changed files and write a clear commit message
3. Commit via Cursor UI
4. Push/sync and verify on GitHub

## Reflection (10 min)

In `examples/day3-output.md`, note:
- which drill felt easiest
- which step caused friction
- one shortcut you will reuse daily

## Suggested Commit

```bash
git add .
git commit -m "Complete Day 3 Cursor workflow drills"
git push
```
