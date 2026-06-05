#!/usr/bin/env python3
"""
os_client_fit_gate.py , screen a prospect before pitching. Good fit vs bad fit.

Doctrine: intel_trust_equation (T=(C+R+I)/self-orientation , low self-orientation = good), WWP
(sell expertise, refuse scope creep / race-to-bottom), intel_new_luxury (premium buyer), Mom Test
(real demand vs politeness), feedback_referral_handling, feedback_payment_follows_proof.

  os_client_fit_gate.py screen --lane in|out --budget yes|no|unknown --priceshop yes|no --decision yes|no --referral yes|no --outcome yes|no [--notes "..."]
  os_client_fit_gate.py rubric
"""
import sys, argparse
GOOD=["values the OUTCOME/status not the file count","in-lane (founder/operator/premium)","decision-maker","referral or warm","accepts proof-before-price","low self-orientation (asks about the work, not just discount)"]
BAD=["price-shopper / race-to-bottom","off-lane (wrong buyer)","not the decision-maker","scope-creep before paying","'just send me your rates' with no problem","wants identity/employer exposure","no budget + no urgency"]
def screen(a):
    score=0; flags=[]
    if a.lane=="in": score+=2
    else: flags.append("off-lane (-)")
    if a.budget=="yes": score+=1
    elif a.budget=="no": flags.append("no budget (-)")
    if a.priceshop=="yes": score-=2; flags.append("price-shopper (--)")
    if a.decision=="yes": score+=1
    else: flags.append("not decision-maker (-)")
    if a.referral=="yes": score+=1
    if a.outcome=="yes": score+=2
    else: flags.append("cares about price not outcome (-)")
    verdict = "FIT , pitch" if score>=4 else ("HOLD , qualify more (Mom Test: ask about the problem, not the sale)" if score>=1 else "PASS , decline cleanly, trade scope or refer out")
    print(f"CLIENT FIT: {verdict}  (score {score})")
    for f in flags: print("  !!",f)
    if verdict.startswith("PASS"): print("  decline script: 'This isn't the right fit for what you need , happy to point you to someone.' (WWP: refuse, protect positioning.)")
    if verdict.startswith("FIT"): print("  next: os_offer_builder build -> os_pricing_gate check -> discovery (diagnose before prescribe).")
    return 0
def main():
    ap=argparse.ArgumentParser(prog="os_client_fit_gate.py"); sub=ap.add_subparsers(dest="cmd")
    s=sub.add_parser("screen")
    for x,df in [("lane","unknown"),("budget","unknown"),("priceshop","no"),("decision","unknown"),("referral","no"),("outcome","unknown")]: s.add_argument(f"--{x}",default=df)
    s.add_argument("--notes",default=""); sub.add_parser("rubric")
    a=ap.parse_args()
    if a.cmd=="screen": return screen(a)
    if a.cmd=="rubric":
        print("GOOD FIT:"); [print("  +",g) for g in GOOD]; print("BAD FIT:"); [print("  -",b) for b in BAD]; return 0
    ap.print_help(); return 1
if __name__=="__main__": sys.exit(main())
