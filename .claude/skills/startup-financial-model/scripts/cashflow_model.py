#!/usr/bin/env python3
"""Monthly cash-flow model with stage gates for an early-stage startup.

Usage:
    python cashflow_model.py assumptions.json --out <output-dir>
    python cashflow_model.py --example > assumptions.json

Reads a JSON assumptions file, simulates each scenario month by month, and
writes one CSV per scenario plus summary.md (KPIs and gate checks).
Standard library only. Currency is whatever the inputs use.

This is a simple recurring-revenue model: customers pay `arpa_monthly` every
month until they churn. It does not model tax, debt repayment, inventory,
or annual prepayments. State these limits when presenting results.
"""
import argparse
import csv
import json
import operator
import os
import sys

EXAMPLE = {
    "currency": "USD",
    "months": 24,
    "starting_cash": 50000,
    "arpa_monthly": 200,
    "gross_margin_pct": 75,
    "monthly_churn_pct": 3,
    "cac": 600,
    "collection_lag_months": 0,
    "team": [
        {"role": "Founder 1", "monthly_cost": 3000, "start_month": 1},
        {"role": "Engineer", "monthly_cost": 6000, "start_month": 7},
    ],
    "funding": [{"month": 7, "amount": 250000, "label": "Pre-seed"}],
    "phases": [
        {
            "name": "Problem validation",
            "start_month": 1,
            "end_month": 3,
            "new_customers_per_month": 0,
            "other_opex_monthly": 500,
            "gate": [{"metric": "cash", "op": ">=", "value": 30000}],
        },
        {
            "name": "MVP and first customers",
            "start_month": 4,
            "end_month": 12,
            "new_customers_per_month": 3,
            "other_opex_monthly": 1500,
            "gate": [
                {"metric": "customers", "op": ">=", "value": 20},
                {"metric": "runway_months", "op": ">=", "value": 9},
            ],
        },
        {
            "name": "Repeatable sales",
            "start_month": 13,
            "end_month": 24,
            "new_customers_per_month": 10,
            "other_opex_monthly": 4000,
            "gate": [
                {"metric": "mrr", "op": ">=", "value": 20000},
                {"metric": "ltv_cac", "op": ">=", "value": 3},
            ],
        },
    ],
    "scenarios": {
        "base": {},
        "downside": {"acquisition_mult": 0.5, "churn_mult": 1.5, "cac_mult": 1.3, "funding_mult": 0},
        "upside": {"acquisition_mult": 1.3, "churn_mult": 0.8},
    },
}

OPS = {">=": operator.ge, ">": operator.gt, "<=": operator.le, "<": operator.lt, "==": operator.eq}
INF = float("inf")


def phase_for(month, phases):
    for p in phases:
        if p["start_month"] <= month <= p["end_month"]:
            return p
    raise ValueError(f"Month {month} is not covered by any phase; phases must cover months 1..N without gaps.")


def simulate(a, sc):
    acq = sc.get("acquisition_mult", 1.0)
    churn = a["monthly_churn_pct"] / 100 * sc.get("churn_mult", 1.0)
    cac = a["cac"] * sc.get("cac_mult", 1.0)
    arpa = a["arpa_monthly"] * sc.get("price_mult", 1.0)
    fund_mult = sc.get("funding_mult", 1.0)
    gm = a["gross_margin_pct"] / 100
    lag = int(a.get("collection_lag_months", 0))

    rows, revenue_hist = [], []
    customers, cash = 0.0, float(a["starting_cash"])
    for m in range(1, a["months"] + 1):
        p = phase_for(m, a["phases"])
        new = p.get("new_customers_per_month", 0) * acq
        lost = customers * churn
        customers = customers + new - lost
        mrr = customers * arpa
        revenue_hist.append(mrr)
        cash_in = revenue_hist[m - 1 - lag] if m - 1 - lag >= 0 else 0.0
        cogs = mrr * (1 - gm)
        acquisition = new * cac
        payroll = sum(
            t["monthly_cost"] for t in a.get("team", [])
            if t.get("start_month", 1) <= m <= t.get("end_month", a["months"])
        )
        other = p.get("other_opex_monthly", 0)
        cash_out = cogs + acquisition + payroll + other
        funding = sum(f["amount"] for f in a.get("funding", []) if f["month"] == m) * fund_mult
        net_burn = cash_out - cash_in
        cash = cash + cash_in - cash_out + funding
        rows.append({
            "month": m, "phase": p["name"], "new_customers": new, "churned": lost,
            "customers": customers, "mrr": mrr, "cash_in": cash_in, "cogs": cogs,
            "acquisition_spend": acquisition, "payroll": payroll, "other_opex": other,
            "cash_out": cash_out, "net_burn": net_burn, "funding": funding, "cash": cash,
        })
    # Runway: cash divided by average net burn of the trailing 3 months.
    for i, r in enumerate(rows):
        window = rows[max(0, i - 2): i + 1]
        avg_burn = sum(w["net_burn"] for w in window) / len(window)
        r["runway_months"] = r["cash"] / avg_burn if avg_burn > 0 and r["cash"] > 0 else (INF if avg_burn <= 0 else 0.0)

    unit = {
        "gross_margin_pct": gm * 100,
        "ltv": arpa * gm / churn if churn > 0 else INF,
        "cac_payback_months": cac / (arpa * gm) if arpa * gm > 0 else INF,
    }
    unit["ltv_cac"] = unit["ltv"] / cac if cac > 0 else INF
    return rows, unit


def gate_results(a, rows, unit):
    out = []
    for p in a["phases"]:
        end = rows[p["end_month"] - 1]
        start_mrr = rows[p["start_month"] - 2]["mrr"] if p["start_month"] > 1 else 0.0
        burn = sum(r["net_burn"] for r in rows[p["start_month"] - 1: p["end_month"]])
        new_arr = (end["mrr"] - start_mrr) * 12
        metrics = dict(unit)
        metrics.update({k: end[k] for k in ("customers", "mrr", "cash", "net_burn", "runway_months")})
        # Burn multiple: net cash burned in the phase per unit of net new ARR. Lower is better.
        metrics["burn_multiple"] = burn / new_arr if new_arr > 0 and burn > 0 else (0.0 if burn <= 0 else INF)
        checks = []
        for g in p.get("gate", []):
            if g["metric"] not in metrics:
                raise ValueError(f"Unknown gate metric '{g['metric']}'. Available: {sorted(metrics)}")
            actual = metrics[g["metric"]]
            checks.append((g, actual, OPS[g["op"]](actual, g["value"])))
        out.append((p, checks))
    return out


def fmt(x):
    if x == INF:
        return "n/a (no burn or no churn)"
    return f"{x:,.1f}" if abs(x) < 100 else f"{x:,.0f}"


def summarise(name, a, rows, unit, gates):
    cur = a.get("currency", "")
    low = min(rows, key=lambda r: r["cash"])
    out_of_cash = next((r["month"] for r in rows if r["cash"] < 0), None)
    breakeven = next((r["month"] for r in rows if r["net_burn"] <= 0 and r["mrr"] > 0), None)
    L = [f"## Scenario: {name}", ""]
    L.append(f"- Ending cash (month {rows[-1]['month']}): {cur} {fmt(rows[-1]['cash'])}")
    L.append(f"- Lowest cash: {cur} {fmt(low['cash'])} in month {low['month']}")
    L.append(f"- Runs out of cash: {'month ' + str(out_of_cash) if out_of_cash else 'not within the model period'}")
    L.append(f"- First month with no net burn: {breakeven if breakeven else 'not within the model period'}")
    L.append(f"- Ending customers: {fmt(rows[-1]['customers'])}; ending MRR: {cur} {fmt(rows[-1]['mrr'])}")
    L.append(f"- LTV: {cur} {fmt(unit['ltv'])}; LTV/CAC: {fmt(unit['ltv_cac'])}; CAC payback: {fmt(unit['cac_payback_months'])} months")
    L += ["", "| Phase | Gate month | Metric | Target | Modelled | Result |", "|---|---|---|---|---|---|"]
    for p, checks in gates:
        if not checks:
            L.append(f"| {p['name']} | {p['end_month']} | (no gate set) | | | |")
        for g, actual, ok in checks:
            L.append(f"| {p['name']} | {p['end_month']} | {g['metric']} | {g['op']} {g['value']:,} | {fmt(actual)} | {'PASS' if ok else 'FAIL'} |")
    L.append("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("assumptions", nargs="?", help="Path to assumptions JSON")
    ap.add_argument("--out", default=".", help="Output directory")
    ap.add_argument("--example", action="store_true", help="Print an example assumptions file and exit")
    args = ap.parse_args()
    if args.example:
        json.dump(EXAMPLE, sys.stdout, indent=2)
        print()
        return
    if not args.assumptions:
        ap.error("assumptions file required (or use --example)")
    with open(args.assumptions) as f:
        a = json.load(f)
    os.makedirs(args.out, exist_ok=True)
    parts = [
        "# Financial model summary", "",
        "Outputs are projections computed from the assumptions file, not forecasts of what will happen.",
        "Not modelled: tax, debt repayment, inventory, annual prepayments.", "",
    ]
    for name, sc in (a.get("scenarios") or {"base": {}}).items():
        rows, unit = simulate(a, sc)
        with open(os.path.join(args.out, f"cashflow_{name}.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            for r in rows:
                w.writerow({k: (round(v, 2) if isinstance(v, float) and v != INF else v) for k, v in r.items()})
        parts.append(summarise(name, a, rows, unit, gate_results(a, rows, unit)))
    path = os.path.join(args.out, "summary.md")
    with open(path, "w") as f:
        f.write("\n".join(parts))
    print("\n".join(parts))
    print(f"Wrote {path} and one CSV per scenario to {args.out}")


if __name__ == "__main__":
    main()
