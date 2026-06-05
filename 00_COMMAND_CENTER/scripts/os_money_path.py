#!/usr/bin/env python3
"""
os_money_path.py , deterministic money-readiness scorer for a world/asset/offer.

Scores the fastest, safe path from a creative world to real revenue WITHOUT exposing identity,
hosting, or setting up payment prematurely. Rubric is explicit and weighted; output is a 0-100
score, a readiness band, the fastest money lane, and the blockers.

  os_money_path.py score --config world.json
  os_money_path.py rubric

config keys (all 0 or 1 unless noted):
  has_glyph, has_color_law, faceless_safe, identity_safe, asset_shippable (gate SHIP),
  has_physical_product, has_recurring_revenue, has_licensing_lane, has_service_lane,
  low_capital, fast_first_dollar, low_legal_risk, demand_proven (0/1; usually 0 until a loop runs)
"""
import sys, json, argparse

WEIGHTS = {
    "has_glyph": 8, "has_color_law": 6, "faceless_safe": 10, "identity_safe": 10,
    "asset_shippable": 12, "has_physical_product": 10, "has_recurring_revenue": 10,
    "has_licensing_lane": 8, "has_service_lane": 6, "low_capital": 6,
    "fast_first_dollar": 6, "low_legal_risk": 4, "demand_proven": 14,
}
def band(s):
    return ("READY-TO-TEST" if s >= 75 else "BUILD-THEN-TEST" if s >= 55 else "EARLY" if s >= 35 else "CONCEPT-ONLY")

def fastest_lane(cfg):
    lanes = []
    if cfg.get("has_physical_product"): lanes.append(("physical print/drop (numbered edition)", 9))
    if cfg.get("has_recurring_revenue"): lanes.append(("subscription archive (monthly drop)", 8))
    if cfg.get("has_licensing_lane"): lanes.append(("license the system/seal/look (B2B film/TV/brand)", 7))
    if cfg.get("has_service_lane"): lanes.append(("done-for-you campaign service", 6))
    lanes.sort(key=lambda x: -x[1])
    return lanes[0][0] if lanes else "no money lane defined (demote)"

def blockers(cfg):
    b = []
    if not cfg.get("identity_safe"): b.append("identity not safe (HARD: fix before any share)")
    if not cfg.get("asset_shippable"): b.append("no gate-SHIP asset yet")
    if not cfg.get("demand_proven"): b.append("demand unproven (run a private proof loop; no public launch)")
    if not cfg.get("low_legal_risk"): b.append("legal review needed before sale")
    if not (cfg.get("has_physical_product") or cfg.get("has_recurring_revenue") or cfg.get("has_licensing_lane") or cfg.get("has_service_lane")):
        b.append("no money lane defined")
    return b

def score(cfg):
    s = sum(w for k, w in WEIGHTS.items() if cfg.get(k))
    total = sum(WEIGHTS.values())
    pct = round(100 * s / total)
    return {"score": pct, "band": band(pct), "fastest_lane": fastest_lane(cfg),
            "blockers": blockers(cfg), "note": "demand_proven stays 0 until a real private proof loop runs; no public launch implied."}

def main():
    ap = argparse.ArgumentParser(prog="os_money_path.py"); sub = ap.add_subparsers(dest="cmd")
    sc = sub.add_parser("score"); sc.add_argument("--config", required=True)
    sub.add_parser("rubric")
    a = ap.parse_args()
    if a.cmd == "rubric":
        print(json.dumps(WEIGHTS, indent=2)); return 0
    if a.cmd == "score":
        cfg = json.load(open(a.config)); print(json.dumps(score(cfg), indent=2)); return 0
    ap.print_help(); return 0

if __name__ == "__main__": sys.exit(main())
