---
name: startup-financial-model
description: Builds a monthly cash-flow and financial model for a startup, aligned to the stage gates of its phased roadmap, with financial KPIs (runway, burn, MRR, gross margin, LTV/CAC, CAC payback, burn multiple) checked at each gate across base, downside and upside scenarios. Use this whenever the user asks for a financial model, cash flow forecast, projections, runway, burn rate, unit economics, break-even, "how much money do I need", "how long will my money last", or financial KPIs and targets per phase or milestone.
---

# Startup financial model

Build a cash-flow model whose time axis is the phased roadmap, so each stage gate has financial KPIs that either pass or fail.

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

- **Cash first.** Early companies die from running out of cash, not from low accounting profit. Model cash in and cash out by month.
- **Few drivers.** Six to ten input assumptions the founder can defend beat a hundred-row spreadsheet nobody can audit.
- **Every input is tagged.** Each driver is a `[FACT: source]` or an `[ASSUMPTION]` with reasoning. The founder supplies the numbers; do not fill gaps with "typical" benchmarks unless you can cite a source, and say so when a figure is your placeholder.
- **A projection is not a forecast.** The output shows what follows if the assumptions hold. Say this when presenting results.

## Workflow

1. **Read** `03-phased-roadmap.md` for phases, durations, and gate KPI names; `02-business-plan.md` for price and channel; `01-icp.md` for the customer. If the roadmap is missing, ask for phases or propose simple ones and mark them provisional.
2. **Collect the drivers.** Ask for whatever is missing, in one batch:
   - Starting cash; currency.
   - Price per customer per month (`arpa_monthly`). For one-off or usage pricing, see "Limits" below.
   - Gross margin: what share of revenue remains after the direct cost of serving a customer.
   - Monthly churn: share of customers lost each month.
   - Cost to acquire one customer (`cac`).
   - New customers per month in each phase.
   - Team: role, monthly cost, start month.
   - Other monthly costs per phase (tools, rent, legal).
   - Expected funding: month and amount. Treat unconfirmed funding as an assumption and exclude it in the downside scenario.
   - Payment delay in months, if customers pay late.
3. **Write** `ventures/<idea-slug>/04-financial-model/assumptions.json`. Get the format with:
   ```bash
   python scripts/cashflow_model.py --example
   ```
   Phases must cover months 1 to N with no gaps. Each phase's `gate` list holds criteria as `{"metric", "op", "value"}`. Available metrics: `customers`, `mrr`, `cash`, `net_burn`, `runway_months`, `gross_margin_pct`, `ltv`, `ltv_cac`, `cac_payback_months`, `burn_multiple`.
4. **Run the model** (the script is in this skill's folder):
   ```bash
   python scripts/cashflow_model.py ventures/<idea-slug>/04-financial-model/assumptions.json \
     --out ventures/<idea-slug>/04-financial-model
   ```
   It writes `cashflow_<scenario>.csv` and `summary.md` with the gate pass/fail table. Use the script rather than computing by hand so numbers are reproducible. Always include a downside scenario; the default example halves acquisition, raises churn and CAC, and removes funding.
5. **Interpret** in `ventures/<idea-slug>/04-financial-model/README.md`:
   - The driver table with fact/assumption tags.
   - Gate-by-gate results for each scenario.
   - The month cash runs out in the downside case, and the latest date by which fundraising must start. This is a judgement the founder should confirm; raising usually takes months, so starting when cash is nearly gone is too late.
   - Sensitivity: change one driver at a time (price, churn, CAC, acquisition rate), rerun, and report which one moves the gate results most. That driver is the assumption to test first.
   - How much funding is needed to reach the next gate with a buffer. Pass this figure to `startup-fundraising`.
6. If a gate fails in the base case, say so plainly and offer the levers (price, cost, timing, scope). Do not adjust assumptions to make gates pass without the user deciding to.

## KPI definitions (as the script computes them)

| KPI | Definition |
|---|---|
| MRR | customers × monthly price |
| Net burn | cash out − cash in for the month, excluding funding |
| Runway (months) | cash ÷ average net burn of the last three months |
| LTV | monthly price × gross margin ÷ monthly churn |
| LTV/CAC | LTV ÷ cost to acquire a customer |
| CAC payback (months) | CAC ÷ (monthly price × gross margin) |
| Burn multiple | net burn during the phase ÷ net new annualised revenue added in the phase; lower is better |

Which KPIs matter depends on the phase: before revenue, gates are about cash and runway; with first customers, about gross margin and retention; when scaling sales, about LTV/CAC, payback and burn multiple.

## Limits

The script models recurring monthly revenue only. It does not handle tax, debt repayment, inventory, annual prepayments, one-off sales, or marketplaces. For those, either approximate (for example convert one-off sales to a monthly equivalent and say so) or build a spreadsheet instead and state that the script was not used. This is planning support, not accounting or tax advice; recommend an accountant before the numbers go to investors or lenders.
