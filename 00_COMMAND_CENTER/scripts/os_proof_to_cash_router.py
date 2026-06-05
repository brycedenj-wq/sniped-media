#!/usr/bin/env python3
"""
os_proof_to_cash_router.py , route current proof to the fastest CLEAN cash play.

STANDING ORDER (locked): ACTIVE DIRECTION = Prime Mover / one-person campaign house / AI-native
premium creative production / faceless private proof loops / world+IP systems / proof-to-cash WITHOUT
identity exposure. OLD SNIPED (Reset, Pixieset, local photo sessions, school photo, local-service
packages, op-kit/brand-system photo tiers) = ARCHIVE / FALLBACK ONLY. It is NOT selectable by default;
it appears only with --fallback or when the operator explicitly asks for fallback cashflow.

  os_proof_to_cash_router.py route --assets "axis,deed,world" [--days 3]
  os_proof_to_cash_router.py plan72
  os_proof_to_cash_router.py fallback     , show archived old-SNIPED cashflow (explicit only)
"""
import sys, argparse

# ACTIVE LANE , campaign-house / AI-native. These are the defaults.
ACTIVE = {
 "campaign_demo": ("Private campaign-house demo package","ACTIVE","take the proven AXIS/DEED capability -> a private, identity-safe demo that lands ONE paying brand; no public post, no face"),
 "spec_diagnostic": ("High-ticket diagnostic / paid spec","ACTIVE","sell the THINKING first: a paid Direction/world diagnostic or a spec frame; fastest clean cash that is on-lane and faceless"),
 "ai_campaign_pkg": ("AI-native premium campaign package","AMBER","stills+motion+kit for a brand/world; needs one named buyer + private delivery room"),
 "world_build": ("Premium world / campaign build","AMBER","full world for a brand; anchor high; needs a buyer + scope"),
 "brand_ip_system": ("Brand / world / IP system","AMBER","highest-ticket; ownable system; later-stage buyer"),
 "proof_loop": ("Private proof loop","ACTIVE","identity-safe demand validation before scaling price; keep/kill/scale on real signal"),
}
# FALLBACK , OLD SNIPED. Archived. Never default. Explicit only.
FALLBACK = {
 "reset": ("[FALLBACK] Reset photo shoot $1,500","FALLBACK","old local-service lane; cashflow only if operator explicitly asks; NOT the active direction"),
 "pixieset_delivery": ("[FALLBACK] Pixieset client gallery","FALLBACK","old delivery surface for the photo lane; use a private campaign-house room instead"),
 "local_photo": ("[FALLBACK] local photo packages / op-kit / brand-system shoots","FALLBACK","archived old SNIPED service tiers"),
}
def route(assets, days):
    have=[x.strip().lower() for x in assets.split(",") if x.strip()]
    print(f"PROOF-TO-CASH (ACTIVE LANE: campaign-house / AI-native; window {days}d)")
    print("  default money question: convert the Prime Mover campaign-house capability into paid work")
    print("  without exposing identity, posting publicly, or selling weak work.\n")
    blocked=[a for a in have if a in FALLBACK]
    if blocked:
        print(f"  ! BLOCKED from default routing (old SNIPED, fallback-only): {', '.join(blocked)} , run with `fallback` to see it.\n")
    for k,(name,st,note) in ACTIVE.items():
        print(f"  [{st:6s}] {name}\n           {note}")
    print("\n  FASTEST CLEAN (active): private campaign_demo or a paid spec_diagnostic , both faceless, on-lane.")
    print("  HELD always: no payment setup, no outreach sent, no identity exposure (this PLANS, never executes).")
    print("  payment when triggered: fastest legit link; payment follows proof; entity cleanup later.")
    return 0
def plan72():
    print("72-HOUR MONEY PLAN (ACTIVE LANE , draft, held for go; nothing executes):")
    print("  Day 1: package the campaign-house DEMO from existing proof (AXIS world + DEED) into a private, identity-safe demo. Build+price the offer (os_offer_builder / os_pricing_gate, anchor high).")
    print("  Day 2: identify 3-5 on-lane brands/founders who need premium world/campaign work (NOT local photo clients). Screen (os_client_fit_gate). Draft private outreach (faceless, unsent).")
    print("  Day 3: book 1 paid diagnostic OR send the private demo to 1 warm brand; take payment via fastest legit link ONLY on explicit go. Log to CRM.")
    print("  Guardrails: faceless-safe, no employer overlap, no public posting, no payment rail without approval.")
    print("  NOTE: old SNIPED Reset/Pixieset is NOT in this plan. It is fallback cashflow only, on explicit request.")
    return 0
def fallback():
    print("FALLBACK CASHFLOW (OLD SNIPED , ARCHIVED, explicit request only, NOT the active direction):")
    for k,(name,st,note) in FALLBACK.items(): print(f"  [{st}] {name} , {note}")
    print("  Use ONLY if the operator explicitly asks for fallback cashflow. Default route ignores these.")
    return 0
def main():
    ap=argparse.ArgumentParser(prog="os_proof_to_cash_router.py"); sub=ap.add_subparsers(dest="cmd")
    r=sub.add_parser("route"); r.add_argument("--assets",default="axis,deed,world"); r.add_argument("--days",type=int,default=3)
    sub.add_parser("plan72"); sub.add_parser("fallback")
    a=ap.parse_args()
    if a.cmd=="route": return route(a.assets,a.days)
    if a.cmd=="plan72": return plan72()
    if a.cmd=="fallback": return fallback()
    ap.print_help(); return 1
if __name__=="__main__": sys.exit(main())
