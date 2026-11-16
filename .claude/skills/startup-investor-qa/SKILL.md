---
name: startup-investor-qa
description: Prepares a founder to answer hard investor and accelerator interview questions, by drafting short, specific, truthful answers from the venture's own evidence, exposing weak spots, and running mock interviews with follow-up questions and scoring. Covers a core bank of 14 questions (what are you building, walk through one customer, are people using it, how much are they paying, why you, aren't you just custom software, demo day goals, team roles, customers spoken to, how you sell, what is built, will first customers use it, where they need it most). Use this whenever the user wants to prepare for an investor meeting, accelerator or incubator interview, partner meeting, demo day Q&A, due-diligence call, or says "grill me", "mock interview", "what will investors ask", or "help me answer this investor question".
---

# Startup investor Q&A

Prepare the founder to answer direct investor questions in under a minute each, with specifics, and without claiming anything that is not true.

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

## What good answers have in common

Interviewers ask short questions to see whether the founder knows their business at the level of names and numbers. Strong answers:

- **Answer in the first sentence.** "Yes, 12 companies use it weekly" before any context. Background first sounds like avoidance.
- **Use a number or a name** where one exists: a customer, a price, a count, a date.
- **Tell the truth when the answer is weak.** "No one is paying yet. Three pilots start in March; two have agreed a price of X if the pilot hits Y." Interviewers probe weak answers, and an inflated one discovered later ends the conversation. The honest version plus a concrete next step is the strongest available answer.
- **Stop.** Twenty to forty seconds, then let them ask the next question.

Never help the founder imply traction, customers, revenue, or product that does not exist. If the true answer is "none yet", the work is to make the plan behind it credible, and to feed the gap back to the roadmap.

## Mode 1: Build the answer sheet

1. Read every file in the venture folder. Read `references/question-bank.md` for the 14 core questions: what each one tests, what a strong answer contains, the trap, the likely follow-ups, and which venture file holds the material.
2. For each question, draft the founder's answer:
   - First sentence: the direct answer.
   - Two or three supporting specifics, each traceable to a file or to something the user said.
   - Target length: 40 to 90 words spoken.
   - Where the facts are missing, do not draft around the hole. Write `NEEDS FOUNDER INPUT:` with the exact fact required, and ask the user.
3. Rate each answer on evidence: **Strong** (backed by facts), **Thin** (true but little evidence), **Gap** (no real answer yet).
4. For every Thin or Gap answer, give the honest version to use today and the action that would upgrade it, with the roadmap phase it belongs to.
5. Add likely follow-up questions under each answer with one-line responses.
6. If the user gives extra questions, or the audience suggests others (a grant panel, a corporate investor), add them in the same format.

## Mode 2: Mock interview

Run this when the user asks to practise, or after the answer sheet is done.

1. Tell the user the format: one question at a time, they answer as they would aloud, typed or dictated.
2. Ask the questions in mixed order, in the interviewer's blunt voice. Do not show the prepared answer first.
3. After each answer, ask one follow-up that presses on the weakest part ("You said 40 conversations. How many said they would pay?"), as an interviewer would. Interrupt long answers.
4. Then give brief feedback before the next question:
   - Did the first sentence answer the question?
   - Specific or vague? Quote the vague phrase.
   - Any claim not supported by the venture files. Flag it clearly; the founder may have newer facts, in which case update the files.
   - A tighter rewrite using only the founder's own facts.
5. Score each answer 1 to 5 on Direct, Specific, Credible, Brief. At the end, give a table of scores, the three answers to rework first, and facts the founder should memorise (customer count, price, conversations held, what is live).

## Output

Write `ventures/<idea-slug>/08-investor-qa.md`:

```
# Investor Q&A: <venture>
## Readiness summary        (count of Strong / Thin / Gap; top 3 gaps and the action for each)
## Numbers to know cold     (each with source)
## Answers
### <n>. <question>
Rating:
Answer:
Evidence:
If pressed:               (follow-ups and one-line responses)
To strengthen:            (action, phase)
## Mock interview log       (date, scores, what to rework)
```

Gaps found here are findings about the business, not about wording. Pass them to `startup-validate` or `startup-phased-roadmap` as actions.
