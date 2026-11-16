---
name: startup-validate
description: Entry point and coordinator for validating a startup idea end to end. Captures the idea brief, runs the other startup-* skills in the right order (ICP, business plan, phased roadmap, financial model, partnerships, fundraising, pitch, investor Q&A), tracks which assumptions are proven, and gives an honest go / pivot / stop verdict. Use this whenever the user says "validate my startup idea", "I have a business idea", "is this idea any good", "stress-test my startup", "where do I start with this venture", or wants a status check across their startup documents, even if they do not name a specific deliverable.
---

# Startup validate

Coordinate the validation of one startup idea. This skill owns the idea brief and the verdict; the other skills own the detailed documents.

## Shared workspace

All `startup-*` skills work on one folder per idea, `ventures/<idea-slug>/`, so each skill builds on the others instead of starting over. Before asking the user anything, read the files that already exist there and reuse what they say. If the folder or `00-idea-brief.md` is missing, collect the brief first (see `startup-validate`) or ask the few questions this skill needs.

| File | Owner skill |
|---|---|
| `00-idea-brief.md` | startup-validate |
| `01-icp.md` | startup-icp |
| `02-business-plan.md` | startup-business-plan |
| `03-phased-roadmap.md` | startup-phased-roadmap |
| `04-financial-model/` | startup-financial-model |
| `05-partnerships.md` | startup-partnerships |
| `06-fundraising.md` | startup-fundraising |
| `07-pitch.md` | startup-pitch |
| `08-investor-qa.md` | startup-investor-qa |
| `evidence-log.md` | all (append only) |

Write only your own file, plus new rows in `evidence-log.md`. If your work contradicts another file (for example the ICP no longer matches the plan), say so to the user and name the skill that should be rerun rather than silently editing it.

## Evidence rules

The point of this suite is to find out whether the idea is true, not to make it sound good. A plan built on invented numbers fails later and more expensively.

- Tag every material claim as `[FACT: source]`, `[ASSUMPTION]`, or `[UNKNOWN]`. A fact needs a source the user can check: something they told you, a document they supplied, or a page you actually retrieved.
- Do not invent statistics, market sizes, benchmarks, competitor details, investor names, or quotes. If you cannot source a number, write it as an assumption with the reasoning, or as unknown with the cheapest way to find out.
- Anything about funding programmes, investor activity, regulation, or pricing changes quickly. Look it up when a search tool is available and give the date; otherwise mark it as needing verification.
- Each `[ASSUMPTION]` that the plan depends on goes into `evidence-log.md` as a row: assumption, why it matters, how to test it, status (untested / supported / contradicted), evidence.
- If key context is missing, ask instead of guessing. Keep it to the questions that change the output.

## Step 1: Capture the idea brief

Create `ventures/<idea-slug>/00-idea-brief.md`. Ask only for what is missing, in one batch:

1. What is being built, in one sentence a stranger would understand.
2. Who has the problem, and how they deal with it today.
3. Why the founder, and why now.
4. Stage: idea, prototype, pilots, paying customers. Any numbers that exist (users, revenue, conversations held).
5. Team, location or target geography, money and time available.
6. What the founder wants out of this: venture-scale company, profitable small business, or undecided. This changes the fundraising and roadmap advice.

Write the brief in the founder's own facts. Leave gaps as `[UNKNOWN]` rather than filling them.

## Step 2: Run the suite in order

Each step uses the previous outputs. Skip a step the user does not want, but tell them what later steps will be weaker for it.

1. `startup-icp`: who exactly the customer is. Everything else depends on this.
2. `startup-business-plan`: the one-page-first plan.
3. `startup-phased-roadmap`: phases and stage gates.
4. `startup-financial-model`: cash flow and KPIs per gate.
5. `startup-partnerships`: who can shorten the path to customers.
6. `startup-fundraising`: how much, from whom, when.
7. `startup-pitch`: the investor narrative and deck outline.
8. `startup-investor-qa`: rehearsal for hard investor questions.

After each step, give a three-line summary: what was decided, the riskiest assumption it added, and the next step.

## Step 3: Verdict

When asked for a status or verdict, read every file in the folder and write a `## Verdict` section at the end of `00-idea-brief.md`:

- **Evidence scorecard:** count of assumptions supported, untested, and contradicted, from `evidence-log.md`.
- **The three riskiest untested assumptions**, each with the cheapest test and what result would change the plan.
- **Inconsistencies between documents** (for example the pitch claims a market the ICP file does not support).
- **Call:** proceed, proceed with changes, pivot, or stop. Give the reasons. A "not enough evidence yet" call is legitimate; say what evidence would settle it.

Do not soften a negative call. The founder is using this to avoid spending a year on something that does not work.
