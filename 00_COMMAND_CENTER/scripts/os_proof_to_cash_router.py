#!/usr/bin/env python3
"""
os_proof_to_cash_router.py , given the proof you have NOW, route to the fastest CLEAN cash play.

Doctrine: feedback_payment_follows_proof, feedback_old_work_informs_proof_decides, intel_pricing_logic,
WWP, feedback_possibility_engine (don't crown a lane), safety floor (no identity exposure, payment
follows proof, faceless-safe). Clean = no identity exposure, no employer overlap, reversible, legit link.

  os_proof_to_cash_router.py route --assets "axis,deed,reset" [--days 3]
  os_proof_to_cash_router.py plan72        , the 72-hour money plan template (held for go)
"""
import sys, argparse
PLAYS = {
 "reset": ("Reset shoot $1,500 floor","ACTIVE","existing offer; book a real shoot via referral/warm; fastest legit cash; faceless-safe (you behind camera)"),
 "deed": ("DEED office campaign still as a paid brand asset","AMBER","strongest single still; sell as a campaign image / poster to a founder; needs a buyer + delivery"),
 "axis": ("AXIS world / campaign-film proof as a premium brand-film offer","AMBER","elite proof exists; sell the capability (one-person campaign house); price on value; needs one named buyer"),
 "opkit": ("Op Kit upsell to a delivered Reset client","AMBER","day-30 trigger; warm; higher tier"),
 "drop": ("numbered print/edition drop","HELD","validate demand before any manufacture; no checkout yet"),
}
def route(assets, days):
    have=[x.strip().lower() for x in assets.split(",") if x.strip()]
    print(f"PROOF-TO-CASH (assets: {', '.join(have)}; window {days}d)")
    ranked=[]
    for k in have:
        if k in PLAYS:
            name,st,note=PLAYS[k]; ranked.append((0 if st=="ACTIVE" else (1 if st=="AMBER" else 2),k,name,st,note))
    ranked.sort()
    for _,k,name,st,note in ranked:
        print(f"  [{st:6s}] {name}\n           {note}")
    print("\n  FASTEST CLEAN: the ACTIVE play first (Reset). AMBER plays need 1 buyer + a delivery surface.")
    print("  HELD always: no payment setup, no outreach send, no identity exposure (this router PLANS, it does not execute).")
    print("  payment when triggered: fastest legit link (Stripe/PayPal/Square link) , payment follows proof; entity cleanup later.")
    return 0
def plan72():
    print("72-HOUR MONEY PLAN (DRAFT , held for operator go; nothing executes):")
    print("  Day 1: pick ONE ACTIVE play (Reset). Build the offer (os_offer_builder) + price (os_pricing_gate). Draft 5 warm/referral DMs (NOT sent).")
    print("  Day 2: screen any responders (os_client_fit_gate). Book 1 discovery (diagnose before prescribe). Prep delivery surface (Pixieset).")
    print("  Day 3: close 1 Reset at floor+; take payment via fastest legit link ONLY on your explicit go. Log to CRM.")
    print("  Guardrails: faceless-safe, no employer overlap, no public posting, no payment rail set up without approval.")
    return 0
def main():
    ap=argparse.ArgumentParser(prog="os_proof_to_cash_router.py"); sub=ap.add_subparsers(dest="cmd")
    r=sub.add_parser("route"); r.add_argument("--assets",required=True); r.add_argument("--days",type=int,default=3); sub.add_parser("plan72")
    a=ap.parse_args()
    if a.cmd=="route": return route(a.assets,a.days)
    if a.cmd=="plan72": return plan72()
    ap.print_help(); return 1
if __name__=="__main__": sys.exit(main())
