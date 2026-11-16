---
name: startup-icp
description: Researches and defines the Ideal Customer Profile (ICP) for a startup idea, including segment options, a scored choice of beachhead segment, buyer and user personas, pains and triggers, where to find these customers, and a customer interview plan. Use this whenever the user asks about ICP, target customer, target market, customer segments, personas, beachhead market, "who should I sell to", "who is my customer", or customer discovery interviews, and before writing a business plan or pitch when no ICP exists yet.
---

# Startup ICP

Define who the first customers are, narrowly enough that the founder could list fifty of them by name.

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

## Why narrow

A broad ICP ("SMEs", "busy professionals") cannot be tested: there is no list to call, no shared pain, and no single message. The first ICP is a starting point chosen for learning speed, not a claim about the eventual market.

## Workflow

1. **Read** `00-idea-brief.md` and anything the user has from real conversations (notes, emails, survey results). Real customer words outrank reasoning.
2. **Generate 3 to 5 candidate segments.** For each: who they are (for B2B: industry, size, role of buyer and user; for consumer: situation and behaviour, not demographics alone), the job they are trying to get done, and how they solve it now.
3. **Score each candidate 1 to 5** on the criteria below and show the table. State which scores rest on evidence and which are guesses.
   - Pain intensity: is it a top-three problem for them?
   - Frequency: how often does it occur?
   - Budget and willingness to pay: do they already spend money or time on it?
   - Reachability: can the founder get in front of 20 of them this month?
   - Speed to decision: how long from first call to yes?
   - Founder fit: credibility or access the founder already has.
4. **Recommend one beachhead segment** and say what would make you change the recommendation.
5. **Write the profile** for that segment:
   - Firmographic or situational definition, with explicit exclusions ("not for...").
   - Buyer, user, and blocker: roles, what each cares about.
   - Trigger events that make them look for a solution now.
   - Current alternatives, including doing nothing and spreadsheets.
   - The measurable outcome they would pay for.
   - Where they gather: communities, events, publications, tools they already use.
   - Disqualifiers: signs a lead looks right but is not.
6. **Research, if tools allow.** Use web search to check segment size, existing spend, and competitors. Cite the page and date. If no search tool is available, list what to look up and mark the entries `[UNKNOWN]`.
7. **Interview plan.** Ten to fifteen conversations with the beachhead segment:
   - Where to find them and a short outreach message.
   - Questions about past behaviour ("tell me about the last time...", "what did you try?", "what did it cost?"), not opinions about the idea. People are polite about hypotheticals and honest about what they already did.
   - What result would confirm the segment, and what would rule it out. Decide this before the interviews.

## Output

Write `ventures/<idea-slug>/01-icp.md` with these sections: Candidate segments and scores, Chosen beachhead and why, Profile, Where to find them, Interview plan, Open questions. Add the key assumptions to `evidence-log.md`.

When the user brings back interview notes, update the scores and the profile, record what changed, and flag any downstream file that is now out of date.
