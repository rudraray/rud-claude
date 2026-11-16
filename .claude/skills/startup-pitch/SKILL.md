---
name: startup-pitch
description: Creates the investor pitch and pitch plan for a startup, including the one-sentence and one-minute pitch, the narrative, a slide-by-slide deck outline with speaker notes, the ask and use of funds, a data-room checklist, and a meeting plan. Use this whenever the user asks for an investor pitch, pitch deck, elevator pitch, one-liner, investor memo, demo day pitch, accelerator application answers, or "help me pitch this". For rehearsing investor questions and answers, use startup-investor-qa.
---

# Startup pitch

Build a pitch that is specific, short, and true. Investors hear many pitches; what stands out is concrete evidence and a founder who is clear about what is not yet known.

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

## Principles

- **Only claim what the files support.** Every number in the pitch must trace to `evidence-log.md`, the financial model, or something the user states. If traction is thin, present what is real (conversations held, pilots agreed, what was learned) and the plan to get more. An exaggerated claim that collapses under one follow-up question costs more than a modest one.
- **Specific over grand.** "Invoice reconciliation for 10 to 50 person construction subcontractors" beats "an AI platform transforming finance".
- **Lead with the answer.** Each slide's title is its conclusion.

## Workflow

1. **Read all files in the venture folder.** List what is missing and how that weakens the pitch (no ICP: customer slide will be vague; no financial model: the ask cannot be justified).
2. **Confirm the audience and format:** angel, accelerator, seed fund, grant panel; live pitch, emailed deck, application form; time limit. Emailed decks need to stand alone; live decks need less text.
3. **Write the short forms first.** If these are not clear, slides will not fix it.
   - One sentence: what it is, for whom, and the outcome. No jargon, no "platform", no comparison to another company unless it helps a stranger understand.
   - One minute: problem, who has it, what you built, proof so far, why you, the ask.
4. **Draft the deck outline.** One idea per slide. For each slide give: title (the conclusion), the two to four points or the visual, the evidence with its source file, and speaker notes of a few sentences.

   | # | Slide | Must answer |
   |---|---|---|
   | 1 | Title | What you do, in one line |
   | 2 | Problem | Who hurts, how much, how they cope today |
   | 3 | Solution | What the product does for them; show it |
   | 4 | How it works / demo | One customer's use, start to finish |
   | 5 | Traction | What is real today: users, revenue, pilots, conversations |
   | 6 | Market | Bottom-up size, starting from the beachhead |
   | 7 | Business model | Who pays, how much, unit economics |
   | 8 | Go-to-market | How customers are won now and next |
   | 9 | Competition | Alternatives and why you win with this customer |
   | 10 | Team | Who does what and why this team |
   | 11 | Roadmap and financials | Phases, gates, key KPIs, runway |
   | 12 | Ask | Amount, what milestone it buys, by when |

   Reorder to put the strongest material early: lead with traction if there is any, with team if that is the edge. Drop slides that have nothing true to say rather than padding them.
5. **The ask.** Amount and use of funds come from `06-fundraising.md` and the financial model: "We are raising X to reach Y by Z." If those files do not exist, flag the ask as provisional.
6. **Pitch plan:**
   - Materials: deck, one-page summary, short demo, financial model, data-room checklist (incorporation documents, cap table, customer evidence, key contracts, model). Note which exist.
   - Meeting plan: two-minute opening, demo, where to pause for questions, what to ask the investor, the follow-up email with next step.
   - Rehearsal: time the pitch aloud; then run `startup-investor-qa`.
7. **Red-team pass.** Reread the draft as a sceptical investor and list the five weakest claims with what evidence would fix each. Give this list to the user; do not hide it.

## Output

Write `ventures/<idea-slug>/07-pitch.md`: One sentence, One minute, Deck outline with notes, Ask, Pitch plan, Weakest claims. If the user wants actual slides, build them with whatever presentation tool or skill is available, from this outline.
