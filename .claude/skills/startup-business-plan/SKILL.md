---
name: startup-business-plan
description: Creates an executable business plan for a startup idea, starting with a one-page plan and expanding only where needed, with every section ending in owners, dates and measurable actions. Use this whenever the user asks for a business plan, lean plan, one-page plan, business model, go-to-market plan, operating plan, or "how do I turn this idea into a business", including when they ask to simplify or tighten an existing plan.
---

# Startup business plan

Produce a plan the founder can act on next Monday. "Executable" means every section ends in a decision or an action with an owner, a date, and a way to tell whether it worked.

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

## Keep it simple

Long plans are rarely read and go stale quickly. Write the one-page plan first, confirm it with the user, then expand only the sections where the detail changes a decision. Plain language; no section the founder cannot explain aloud.

If `01-icp.md` does not exist, say so and either run `startup-icp` first or work from a provisional customer definition marked `[ASSUMPTION]`.

## Part 1: One-page plan

1. **Customer:** the beachhead segment from `01-icp.md`, in one line.
2. **Problem:** what it costs them today (time, money, risk).
3. **Solution:** what the product does, and what it deliberately does not do yet.
4. **Why us, why now.**
5. **Alternatives:** what they use today, and why they would switch.
6. **Business model:** who pays, for what, how much, how often.
7. **Go-to-market:** the first channel to try and the next 20 named prospects.
8. **Key numbers:** price, cost to acquire a customer, cost to serve one. Tag each as fact or assumption.
9. **Top three risks** and the test for each.
10. **90-day goals:** three at most, each measurable.

## Part 2: Expanded sections (as needed)

Expand only what the user asks for or what the one-pager leaves dangerously vague. For each, end with a short action table.

- **Market:** size built bottom-up (number of reachable customers × price), with sources. Avoid top-down "1% of a huge market" reasoning; it tells nobody anything about whether customers will buy.
- **Product:** the smallest version that delivers the paid-for outcome; what is built, what is manual behind the scenes, what is deferred.
- **Go-to-market:** channel, message, sales steps, expected conversion at each step as assumptions to test.
- **Operations:** what is needed to deliver, key suppliers, legal or regulatory requirements. Regulation is jurisdiction-specific; name the jurisdiction and recommend professional advice where it matters.
- **Team:** who does what now, the gaps, the next hire and what triggers it.
- **Money:** a summary only. The detail belongs to `startup-financial-model`.

## Part 3: Action plan

A single table for the next 90 days:

| Action | Owner | Due | Evidence it worked | Linked assumption |
|---|---|---|---|---|

Every top-three risk must have at least one action here. If an action has no measurable evidence, rewrite it until it does.

## Output

Write `ventures/<idea-slug>/02-business-plan.md`. Add new assumptions to `evidence-log.md`. Then suggest `startup-phased-roadmap` to stretch the 90-day plan into gated phases.
