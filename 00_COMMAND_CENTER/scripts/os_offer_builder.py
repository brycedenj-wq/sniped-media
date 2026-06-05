#!/usr/bin/env python3
"""
os_offer_builder.py , build a grand-slam offer + score it. Hormozi value equation + Blair Enns 3-option.

Doctrine (certified + Sprint 002): Hormozi $100M Offers (value = dream outcome x perceived likelihood /
(time delay x effort)), intel_pricing_logic, intel_wwp_proclamations, intel_status_psychology.

  os_offer_builder.py score --dream 1-5 --likelihood 1-5 --time 1-5 --effort 1-5   (5=best/least)
  os_offer_builder.py build --outcome "..." --tier reset|opkit|brand
"""
import sys, argparse
def score(d,l,t,e):
    t=max(1,t); e=max(1,e)
    val=(d*l)/(t*e)  # higher dream+likelihood, lower time+effort = higher value
    norm=round(val/ (25/1) *100,1)  # vs max 25/1
    print(f"VALUE EQUATION: (dream {d} x likelihood {l}) / (time {6-t} x effort {6-e}-inv) -> raw {round(val,2)}  score {norm}/100")
    levers=[]
    if d<4: levers.append("raise DREAM OUTCOME (sell the status/result, not the service)")
    if l<4: levers.append("raise PERCEIVED LIKELIHOOD (proof, guarantee, case study, risk-reversal)")
    if t<4: levers.append("cut TIME DELAY (faster first win; show speed-to-value)")
    if e<4: levers.append("cut EFFORT/SACRIFICE (done-for-you, remove client work)")
    print("  strongest levers:" if levers else "  offer is strong on all four axes")
    for x in levers: print("   -",x)
    return 0
def build(outcome,tier):
    floors={"reset":1500,"opkit":4000,"brand":12500}; f=floors.get(tier,1500)
    print(f"GRAND-SLAM OFFER , {tier} (floor ${f})")
    print(f"  Dream outcome: {outcome}")
    print( "  Stack (make the value obvious):")
    print( "   1 core deliverable (the result, named)")
    print( "   2 risk-reversal / guarantee (raises likelihood)")
    print( "   3 speed bonus (cuts time-delay: a fast first proof)")
    print( "   4 done-for-you (cuts effort: client does ~nothing)")
    print( "   5 scarcity (numbered / limited slots , status)")
    print(f"  Price on VALUE not cost; anchor high; floor ${f}; trade scope not price.")
    print( "  GATE: run os_pricing_gate.py check before quoting; os_client_fit_gate before pitching.")
    return 0
def main():
    ap=argparse.ArgumentParser(prog="os_offer_builder.py"); sub=ap.add_subparsers(dest="cmd")
    s=sub.add_parser("score"); [s.add_argument(f"--{x}",type=int,required=True) for x in ("dream","likelihood","time","effort")]
    b=sub.add_parser("build"); b.add_argument("--outcome",required=True); b.add_argument("--tier",default="reset")
    a=ap.parse_args()
    if a.cmd=="score": return score(a.dream,a.likelihood,a.time,a.effort)
    if a.cmd=="build": return build(a.outcome,a.tier)
    ap.print_help(); return 1
if __name__=="__main__": sys.exit(main())
