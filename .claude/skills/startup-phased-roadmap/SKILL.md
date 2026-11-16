---
name: startup-phased-roadmap
description: Breaks a startup plan into a simple phased roadmap with stage gates, where each phase has one goal, a time and money budget, and explicit pass / pivot / stop criteria before more is spent. Use this whenever the user asks for a phased approach, phases, milestones, roadmap, stage gates, MVP scope, "what should I do first", "keep it simple", or wants to simplify an over-ambitious plan into steps.
---

# Startup phased roadmap

Turn the plan into a small number of phases, each of which buys one piece of evidence. Money and effort for the next phase are released only when the gate is passed.

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

## Why gates

Founders usually fail by building too much before learning whether anyone wants it. A gate set in advance makes it possible to stop or change course without the decision being clouded by sunk cost.

## Workflow

1. Read `00-idea-brief.md`, `01-icp.md`, `02-business-plan.md`. Note the stage the venture is at today; start the roadmap there, not at phase 1 by default.
2. Draft the phases. Use the default set below, then merge, drop, or rename to fit. Three to five phases is the target; more than five usually means the plan is not simple yet.
3. For each phase fill in the template.
4. Check with the user that the gate criteria are numbers they accept as binding before work starts. Criteria agreed afterwards tend to move.

## Default phases

| Phase | Question it answers | Typical gate evidence |
|---|---|---|
| 1. Problem validation | Do the target customers have this problem badly enough? | Interviews completed; share reporting the problem unprompted; evidence they spend time or money on it |
| 2. Solution validation | Will they commit to this solution? | Signed pilots, letters of intent, pre-orders, or deposits |
| 3. MVP and first customers | Do they use it and pay? | Paying customers, usage, retention after the first period |
| 4. Repeatable sales | Can customers be acquired predictably at a sane cost? | Channel conversion, acquisition cost against customer value, payback period |
| 5. Scale | Does it hold with more spend and people? | Growth rate, margins, cash efficiency |

The thresholds are the founder's to set and depend on the market. Do not present any threshold as an industry standard unless you have a source; label proposed numbers `[ASSUMPTION]` with your reasoning.

## Phase template

```
### Phase N: <name>
Goal (one sentence):
Duration and deadline:
Budget (cash and founder time):
Must do (max 5 activities):
Explicitly not doing:
Gate criteria (measurable, 2 to 4):
  - Pass:   <metric and threshold>
  - Pivot:  <result that means change the customer, problem, or solution>
  - Stop:   <result that means end the project>
Decision date and who decides:
Financial KPIs for this gate: <names only; values come from startup-financial-model>
```

"Explicitly not doing" matters as much as "must do": it is where simplicity is enforced.

## Output

Write `ventures/<idea-slug>/03-phased-roadmap.md`: a one-table overview of all phases, then the template for each, then a "current phase" marker. Keep the gate KPI names consistent with what `startup-financial-model` computes (customers, mrr, cash, runway_months, gross_margin_pct, ltv_cac, cac_payback_months, burn_multiple) so the model can check them. Suggest running `startup-financial-model` next.
