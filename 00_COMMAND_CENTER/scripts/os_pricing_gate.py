#!/usr/bin/env python3
"""
os_pricing_gate.py , price the value, not the cost. Enforces the SNIPED pricing doctrine on any quote.

Doctrine sources (certified): intel_pricing_logic (Blair Enns 3-option + premium-as-insurance),
intel_new_luxury, intel_status_psychology, intel_wwp_proclamations, feedback_referral_handling
(Reset floor $1,500, trade scope never price), feedback_payment_follows_proof.

  os_pricing_gate.py check --tier reset|opkit|brand|custom --price N [--basis value|cost] [--scope "..."]
  os_pricing_gate.py options --anchor N        , build the 3-option architecture around an anchor
  os_pricing_gate.py doctrine
"""
import sys, argparse
FLOORS = {"reset":1500, "opkit":4000, "brand":12500, "custom":1500}
RULES = [
 "Price the value and the meaning, not the cost (no cost-plus, no hourly).",
 "Three-option architecture; anchor high; the middle is the target.",
 "Premium tier framed as insurance (de-risk), not as a bigger expense.",
 "Reset floor holds at $1,500. Trade SCOPE, never price.",
 "Scarcity / numbered editions for status goods.",
 "Proof before price: do not raise the number before demand/proof exists.",
 "Status is signaled, not stated; the buyer pays to signal, not to get files.",
]
def check(tier, price, basis, scope):
    floor=FLOORS.get(tier,1500); v={}
    v["above_floor"]= "PASS" if price>=floor else f"FAIL(below {tier} floor ${floor}; trade scope down, do not drop price)"
    v["value_basis"]= "PASS" if basis=="value" else "FAIL(cost/hourly basis , reprice on outcome+meaning)"
    v["status_premium"]= "OK" if price>=floor else "raise via scope, hold the number"
    verdict = "HOLD-PRICE" if all(str(x).startswith(("PASS","OK")) for x in v.values()) else "REPRICE"
    print(f"PRICING GATE [{tier} ${price}, basis={basis}]: {verdict}")
    for k,val in v.items(): print(f"  {'OK ' if str(val).startswith(('PASS','OK')) else '!! '}{k}: {val}")
    if scope: print(f"  scope lever: if buyer resists ${price}, REDUCE deliverables ({scope}), keep the price.")
    print(f"  3-option anchor: run `os_pricing_gate.py options --anchor {max(price,floor)}`")
    return 0 if verdict=="HOLD-PRICE" else 1
def options(anchor):
    good=max(anchor,1500); better=round(good*2.4/100)*100; best=round(good*4.5/100)*100
    print("3-OPTION ARCHITECTURE (anchor high; middle is the target):")
    print(f"  BEST  (anchor)   ${best:>6}  , full world/system + scarcity + premium-as-insurance")
    print(f"  BETTER (target)  ${better:>6}  , the option you want them to pick")
    print(f"  GOOD  (floor)    ${good:>6}  , entry; trade scope to defend this number")
    print("  present BEST first (anchor), let BETTER look reasonable; never lead with GOOD.")
    return 0
def main():
    ap=argparse.ArgumentParser(prog="os_pricing_gate.py"); sub=ap.add_subparsers(dest="cmd")
    c=sub.add_parser("check"); c.add_argument("--tier",default="custom"); c.add_argument("--price",type=int,required=True); c.add_argument("--basis",default="value"); c.add_argument("--scope",default="")
    o=sub.add_parser("options"); o.add_argument("--anchor",type=int,required=True); sub.add_parser("doctrine")
    a=ap.parse_args()
    if a.cmd=="check": return check(a.tier,a.price,a.basis,a.scope)
    if a.cmd=="options": return options(a.anchor)
    if a.cmd=="doctrine":
        for r in RULES: print("  -",r); return 0
    ap.print_help(); return 1
if __name__=="__main__": sys.exit(main())
