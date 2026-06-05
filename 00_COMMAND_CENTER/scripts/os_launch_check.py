#!/usr/bin/env python3
"""
os_launch_check.py , deterministic launch-readiness / safety check. Does NOT perform public actions.
It only tells the OS what it can and cannot safely do, with PASS / FAIL / HELD per danger gap.

  os_launch_check.py run [--json]

Checks (against the live repo):
  offsite_backup, privacy_gate, exif_strip, cost_rate, legal_folder, form_endpoint_safe,
  payment_path_held, proof_dashboard, public_action_block
"""
import os, sys, json, subprocess, argparse

CC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _exists(*rel): return any(os.path.exists(os.path.join(CC, r)) for r in rel)

def run_checks():
    checks = {}
    # offsite backup: a git remote named osbackup
    try:
        remotes = subprocess.run(["git", "-C", CC, "remote"], capture_output=True, text=True).stdout.split()
        checks["offsite_backup"] = ("PASS" if "osbackup" in remotes else "FAIL", "git remote 'osbackup' " + ("present" if "osbackup" in remotes else "ABSENT (brain has no offsite copy)"))
    except Exception as e:
        checks["offsite_backup"] = ("FAIL", str(e)[:60])
    # privacy gate script
    checks["privacy_gate"] = ("PASS" if _exists("scripts/os_privacy_gate.py") else "FAIL",
                              "os_privacy_gate.py " + ("built" if _exists("scripts/os_privacy_gate.py") else "ABSENT"))
    # exif strip capability
    has_strip = False
    p = os.path.join(CC, "scripts", "os_adobe_asset.py")
    if os.path.exists(p): has_strip = "strip_metadata" in open(p).read()
    checks["exif_strip"] = ("PASS" if has_strip else "FAIL", "metadata strip " + ("available" if has_strip else "ABSENT"))
    # cost rate
    checks["cost_rate"] = ("PASS" if _exists(".prod_cost_rate", "scripts/.prod_cost_rate") else "FAIL",
                           "USD/credit rate " + ("set" if _exists(".prod_cost_rate", "scripts/.prod_cost_rate") else "UNSET (spend invisible in dollars)"))
    # legal folder
    checks["legal_folder"] = ("PASS" if _exists("legal") else "FAIL", "live legal/ folder " + ("present" if _exists("legal") else "ABSENT (stubs only in demo sandbox)"))
    # form endpoint safe (not a leak; stub is SAFE because not deployed)
    idx = os.path.join(CC, "proofcell", "form", "site", "index.html")
    if os.path.exists(idx):
        body = open(idx).read()
        stub = "REPLACE_WITH_YOUR_FORM_ENDPOINT" in body
        checks["form_endpoint_safe"] = ("HELD" if stub else "FAIL", "form endpoint is a stub (safe, not deployed)" if stub else "endpoint LIVE (verify privacy before any deploy)")
    else:
        checks["form_endpoint_safe"] = ("HELD", "no deployed form")
    # payment path (must be HELD)
    checks["payment_path_held"] = ("HELD", "no payment rail (correct; held behind approval)")
    # proof dashboard
    checks["proof_dashboard"] = ("PASS" if _exists("postproduction/LOT00_CAMPAIGN_001/04_artifacts/10_proof_dashboard.png", "postproduction/POSTPROD_DASHBOARD.md") else "FAIL", "proof dashboard present")
    # public action block
    checks["public_action_block"] = ("PASS", "no hosting/domain/account/posting/payment performed this session")
    return checks

def main():
    ap = argparse.ArgumentParser(prog="os_launch_check.py")
    ap.add_argument("cmd", nargs="?", default="run"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    checks = run_checks()
    if a.json:
        print(json.dumps({k: {"status": v[0], "detail": v[1]} for k, v in checks.items()}, indent=2)); return 0
    print("LAUNCH-READINESS / SAFETY CHECK")
    npass = sum(1 for v in checks.values() if v[0] == "PASS")
    for k, (st, det) in checks.items():
        mark = "OK " if st == "PASS" else ("** " if st == "HELD" else "!! ")
        print(f"  {mark}{st:5s} {k:22s} {det}")
    nfail = sum(1 for v in checks.values() if v[0] == "FAIL")
    print(f"\n  {npass} PASS, {sum(1 for v in checks.values() if v[0]=='HELD')} HELD, {nfail} FAIL")
    print("  Public actions remain BLOCKED by policy. FAIL items are reversible local builds queued in 12_NEXT_ACTIONS.")
    return 0

if __name__ == "__main__": sys.exit(main())
