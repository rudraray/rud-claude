---
name: startup-fundraising
description: Develops fundraising options and a funding strategy matched to the startup's target market, stage, geography and business type, covering bootstrapping, customer-funded growth, grants, angels, accelerators, venture capital, crowdfunding, revenue-based financing and debt, plus how much to raise, what milestone it buys, and an investor target list and outreach plan. Use this whenever the user asks about fundraising, raising money, funding options, investors, grants, angels, VC, pre-seed or seed rounds, "how do I fund this", "how much should I raise", or whether to raise at all.
---

# Startup fundraising

Recommend how to fund the next phase, starting from the market the company serves and the kind of business it is, and say honestly when outside equity is the wrong tool.

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

## Why the target market drives the answer

Funding sources specialise. Investors and grant bodies choose by sector, customer type, geography and stage, and each expects a particular shape of return. A business that will not plausibly become very large is a poor fit for venture capital however good it is, and can be a good fit for grants, customer revenue, or lending. Matching the source to the market saves months of pitching the wrong people.

## Workflow

1. **Read** `00-idea-brief.md` (founder goals, geography), `01-icp.md` (market), `03-phased-roadmap.md` (current phase and next gate), `04-financial-model/` (cash need and timing). If the financial model is missing, the amount to raise can only be a rough range; say so.
2. **Confirm what you need to know**, asking only for gaps: country of incorporation and of the target market; sector; whether the founder will give up equity and control; how fast money is needed; existing investors or commitments.
3. **Classify the business** on the factors that determine fit:
   - Market type: B2B software, consumer, deep technology or science-based, hardware, regulated sector (health, finance, energy), social impact, local services.
   - Capital intensity and time to first revenue.
   - Realistic size if it works.
4. **Assess each funding route** against that profile. For each, give fit (strong / possible / poor), why, typical cost (dilution, repayment, time, obligations), and what the funder will expect to see:
   - Founder funds and revenue from customers (pre-sales, pilots, paid design partnerships, services income).
   - Grants and public innovation funding; research and development tax incentives.
   - Friends and family.
   - Angel investors and angel groups.
   - Accelerators and incubators.
   - Venture capital (pre-seed, seed).
   - Corporate or strategic investors (cross-check `05-partnerships.md`).
   - Equity or rewards crowdfunding.
   - Revenue-based financing, venture debt, bank or government-backed loans.
5. **Research specifics, with sources.** Programmes, eligibility, cheque sizes, and investor focus are specific to country and sector and change often. Use web search to find current ones, and cite page and date. Name an investor, fund, or programme only when you have a source showing it is active in this market and stage. Without search, describe the category and how to find members of it (portfolio pages of competitors' investors, government innovation agency sites, angel network directories) and mark the list `[UNKNOWN]`.
6. **Size the raise.** Amount = cash needed to reach the next gate that makes the company more fundable, from the downside scenario of the financial model, plus a buffer. State the milestone the money buys in one sentence. Explain the trade-off between raising more (dilution) and less (risk of running out before the gate).
7. **Recommend a sequence**, for example customer revenue and a grant now, angels after the first paying customers. Tie each step to a roadmap gate.
8. **Build the plan:**
   - Target list table: name or category, why they fit this market, source, route to a warm introduction, status.
   - Materials needed (from `startup-pitch`) and proof points still missing.
   - Timeline working back from the month cash runs low. Fundraising commonly takes several months; `[ASSUMPTION]` the duration unless the user has better information.
   - Weekly process: batch outreach so conversations run in parallel, track status, follow up.

## Be straightforward about

- Instruments and terms (priced equity, convertible notes, SAFE-style agreements, valuation caps, liquidation preferences) differ by country and have legal and tax consequences. Explain the concept when asked and recommend a lawyer for the actual documents. Do not quote "standard" valuations or dilution percentages without a current source.
- If the evidence so far would not convince an investor, say so, and point to the gate that would change that rather than polishing the story.

## Output

Write `ventures/<idea-slug>/06-fundraising.md`: Business profile, Funding routes table, Recommended sequence, Raise amount and use of funds, Target list, Timeline, Next actions. Log assumptions in `evidence-log.md`. Then suggest `startup-pitch`.
