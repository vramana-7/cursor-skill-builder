# Day 1 Output - Prompt Baseline

Date: 2026-06-22

## Weekly Context Used

Paste the exact context used for all 3 prompts:

```text
Current projects:
- Build a Day 1 demo repo to publish on GitHub (first public portfolio project)
- Prepare a 15-minute EBOU internal demo on AI workflow improvements
- Draft a one-page "Prompting Patterns" note for teammates

Deadlines this week:
- Day 1 repo and README polished by Wednesday evening
- EBOU demo dry run by Thursday at 3 PM
- Prompting note shared by Friday noon

Blockers:
- New to GitHub publishing flow (branch, remote, push)
- Need cleaner examples to make the repo look intentional
- Calendar is fragmented with short meeting blocks

Meetings/constraints:
- Mon: 10:00 standup, 1:00-2:00 team sync
- Tue: 11:30 partner call
- Wed: 9:00 roadmap review
- Thu: 2:00-3:00 prep block, 3:00 demo dry run
- Fri: lighter day, best focus window is 9:00-11:30

Personal goals:
- Gym Tuesday and Thursday mornings (7:00 AM)
- Grocery run Wednesday evening
- Sleep target: in bed by 11:00 PM on weekdays
- 20-minute evening walk at least 3 days this week
```

## Output 1 - Vague Prompt

Prompt used:

```text
Help me plan my week based on this context:
[PASTE WEEKLY CONTEXT]
```

Result:

```text
Here is a plan for your week:

1) Work on your GitHub Day 1 project and finish setup.
2) Get ready for your EBOU demo and practice.
3) Share your prompting patterns note with the team.
4) Fit in personal goals like gym and groceries.

Try to use your lighter focus blocks for deep work, especially Friday morning. Keep your evenings organized so you can also get groceries, walk, and sleep on time.
```

## Output 2 - Structured Prompt

Prompt used:

```text
You are a planning assistant.

Using the weekly context below, produce:
1) Top 3 priorities for this week
2) Next actions for each priority (2-3 actions each)
3) A short rationale (2-4 sentences) explaining why these priorities matter

Weekly context:
Current projects:
- Build a Day 1 demo repo to publish on GitHub (first public portfolio project)
- Prepare a 15-minute EBOU internal demo on AI workflow improvements
- Draft a one-page "Prompting Patterns" note for teammates

Deadlines this week:
- Day 1 repo and README polished by Wednesday evening
- EBOU demo dry run by Thursday at 3 PM
- Prompting note shared by Friday noon

Blockers:
- New to GitHub publishing flow (branch, remote, push)
- Need cleaner examples to make the repo look intentional
- Calendar is fragmented with short meeting blocks

Meetings/constraints:
- Mon: 10:00 standup, 1:00-2:00 team sync
- Tue: 11:30 partner call
- Wed: 9:00 roadmap review
- Thu: 2:00-3:00 prep block, 3:00 demo dry run
- Fri: lighter day, best focus window is 9:00-11:30

Personal goals:
- Gym Tuesday and Thursday mornings (7:00 AM)
- Grocery run Wednesday evening
- Sleep target: in bed by 11:00 PM on weekdays
- 20-minute evening walk at least 3 days this week
```

Result:

```text
1) Top 3 priorities for this week
- Publish the Day 1 GitHub project with clear examples and polished README by Wednesday evening.
- Deliver a confident EBOU demo dry run by Thursday 3 PM.
- Share a practical one-page "Prompting Patterns" note by Friday noon.

2) Next actions for each priority (2-3 actions each)
- Publish Day 1 project:
  - Complete `examples/day1-output.md` with realistic sample context and outputs.
  - Update README wording to clearly explain purpose and Day 1 flow.
  - Run git add/commit and push to a new GitHub repo.
- EBOU demo dry run:
  - Draft a 15-minute demo outline with 3 key workflow wins.
  - Build a small walkthrough script and rehearse once on Wednesday.
  - Reserve Thursday 2:00-3:00 for final polish before dry run.
- Prompting note:
  - Capture 3 reusable prompt patterns from Day 1 outputs.
  - Draft one page with examples and "when to use" guidance.
  - Share with team by Friday noon.

3) Short rationale
These priorities align portfolio growth, immediate work impact, and team enablement in one week. Shipping the GitHub repo creates visible progress, while the EBOU demo supports near-term performance. The prompting note turns personal learning into reusable value. Personal routines (gym, sleep, groceries) help maintain energy and consistency.
```

## Output 3 - Constrained Prompt

Prompt used:

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
Current projects:
- Build a Day 1 demo repo to publish on GitHub (first public portfolio project)
- Prepare a 15-minute EBOU internal demo on AI workflow improvements
- Draft a one-page "Prompting Patterns" note for teammates

Deadlines this week:
- Day 1 repo and README polished by Wednesday evening
- EBOU demo dry run by Thursday at 3 PM
- Prompting note shared by Friday noon

Blockers:
- New to GitHub publishing flow (branch, remote, push)
- Need cleaner examples to make the repo look intentional
- Calendar is fragmented with short meeting blocks

Meetings/constraints:
- Mon: 10:00 standup, 1:00-2:00 team sync
- Tue: 11:30 partner call
- Wed: 9:00 roadmap review
- Thu: 2:00-3:00 prep block, 3:00 demo dry run
- Fri: lighter day, best focus window is 9:00-11:30

Personal goals:
- Gym Tuesday and Thursday mornings (7:00 AM)
- Grocery run Wednesday evening
- Sleep target: in bed by 11:00 PM on weekdays
- 20-minute evening walk at least 3 days this week
```

Result:

```text
Priorities
1) Publish the Day 1 GitHub project by Wednesday evening.
   - Fill `examples/day1-output.md` with final prompt outputs.
   - Push repo to GitHub with a clean first commit.

2) Be ready for the Thursday EBOU dry run.
   - Draft a 15-minute talk track with 3 workflow wins.
   - Rehearse once on Wednesday and refine weak transitions.

3) Share the Prompting Patterns note by Friday noon.
   - Capture 3 patterns from this week with one example each.
   - Draft and share a one-page teammate-friendly version.

Rationale
This sequence ships your first public proof of work, then supports immediate team impact through the demo and note. It fits your fixed meetings and protects focused time. Personal routines (Tue/Thu gym, Wednesday groceries, weekday sleep target) keep execution steady.
```

## Reflection (Day 1)

- What improved from v1 to v3: Priorities became specific, outputs were shorter, and actions were immediately executable.
- Why it improved: The constraints forced concrete wording, realistic scope, and decision-making based on time limits.
- One prompt change to reuse in future: Always define output format + word limit + actionability constraints ("start in under 30 minutes").
