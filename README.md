# Startup validation skills

Nine Claude skills that work together to validate a startup idea. Each writes one file into a shared folder, `ventures/<idea-slug>/`, and reads the others' files, so later steps build on earlier ones.

| Order | Skill | Produces |
|---|---|---|
| 0 | `startup-validate` | Idea brief, runs the sequence, go / pivot / stop verdict |
| 1 | `startup-icp` | Ideal customer profile, beachhead choice, interview plan |
| 2 | `startup-business-plan` | One-page plan first, then a 90-day action table |
| 3 | `startup-phased-roadmap` | Three to five phases with pass / pivot / stop gates |
| 4 | `startup-financial-model` | Monthly cash flow and KPIs checked at each gate |
| 5 | `startup-partnerships` | Scored partner candidates and partner briefs |
| 6 | `startup-fundraising` | Funding routes matched to the target market, raise size, target list |
| 7 | `startup-pitch` | One-liner, deck outline, ask, pitch plan |
| 8 | `startup-investor-qa` | Answer sheet for 14 core investor questions, mock interview |

All skills share one rule: claims are tagged as fact (with source), assumption, or unknown, and nothing is invented. Assumptions are tracked in `ventures/<idea-slug>/evidence-log.md`.

## Use

- **Claude Code:** the skills live in `.claude/skills/` and are available when Claude Code is opened in this repository. Start with "validate my startup idea: ...".
- **Claude apps:** packaged copies are in `dist/*.skill`.

## Financial model script

`startup-financial-model/scripts/cashflow_model.py` (Python standard library only):

```bash
python .claude/skills/startup-financial-model/scripts/cashflow_model.py --example > assumptions.json
python .claude/skills/startup-financial-model/scripts/cashflow_model.py assumptions.json --out out/
```

It models recurring monthly revenue only; tax, debt, inventory and one-off sales are not covered.

## Rebuilding packages

After editing a skill, repackage it with the `package_skill` script from Anthropic's skill-creator skill.
