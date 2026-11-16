---
name: startup-partnerships
description: Identifies and prioritises strategic partnerships for a startup (distribution and channel partners, technology and integration partners, design partners and pilot customers, suppliers, credibility partners), scores candidates, and prepares the value exchange, outreach message and pilot terms for each. Use this whenever the user asks about partnerships, strategic partners, alliances, channel or reseller strategy, integrations, co-marketing, design partners, "who should I partner with", or how to reach customers through another company.
---

# Startup partnerships

Find the few partners that shorten the path to the ICP or remove a risk in the current phase, and prepare an approach each one could say yes to.

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

- A partnership is worth pursuing only if it serves the current phase's gate in `03-phased-roadmap.md`. Large-company partnerships are slow; pursuing one too early can consume a whole phase.
- The partner must gain something specific. "Exposure" or "innovation" is not a reason for them to spend time.
- Two or three active partnership efforts is the limit for a small team.

## Workflow

1. **Read** `01-icp.md` (where customers gather, what tools they already use), `02-business-plan.md` (channel), `03-phased-roadmap.md` (current phase and gate).
2. **State the gap** the partnership should close, in one sentence: reach, credibility, missing capability, supply, or data.
3. **Map partner types** and keep those relevant to the gap:
   - Design partners: early customers who co-develop in return for influence or price.
   - Distribution: companies or communities that already have the ICP's attention (resellers, marketplaces, associations, consultants, agencies).
   - Technology: platforms the product must integrate with or build on.
   - Supply: providers of a critical input.
   - Credibility: institutions whose name lowers the buyer's perceived risk (universities, industry bodies, known customers).
4. **List candidates.** Name real organisations only if the user supplied them or you found them through search, with the source. Otherwise describe the type of organisation and how to find examples; do not guess names or contacts.
5. **Score each 1 to 5** and show the table:
   - Access to the ICP
   - What they gain (strength of their incentive)
   - Effort and time to a first result
   - Dependency risk (could they copy it, block it, or change terms?)
   - Fit with the current phase
6. **For the top two or three, write a partner brief:**
   - What we ask for, and what we give.
   - Who inside the partner benefits personally, and their likely objection.
   - The smallest first step: a pilot with a fixed length, one success measure, and a named owner on each side.
   - Terms to settle before starting: exclusivity, revenue share or fees, ownership of data and of anything built together, how either side exits. Recommend legal review before signing anything binding.
   - A short outreach message in plain language.
7. **Risks:** over-dependence on one partner, channel conflict with direct sales, and what the fallback is if the partner goes quiet.

## Output

Write `ventures/<idea-slug>/05-partnerships.md`: Gap, Candidate table with scores, Partner briefs, Risks, Next actions (owner, date). Add assumptions such as "partner X's customers match our ICP" to `evidence-log.md`. Revenue or cost effects of a partnership should be passed to `startup-financial-model`.
