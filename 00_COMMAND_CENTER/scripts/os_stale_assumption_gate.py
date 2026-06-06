#!/usr/bin/env python3
"""
os_stale_assumption_gate.py , newest committed truth wins. Catch claims that match a known-corrected old
assumption and return the latest truth + source before the OS acts on yesterday's reality.

  os_stale_assumption_gate.py check "<claim or question>"   , is this a stale assumption? show latest truth
  os_stale_assumption_gate.py audit                          , open risks (ACTIVE_RISK, not yet corrected)
  os_stale_assumption_gate.py list                           , the whole ledger
  os_stale_assumption_gate.py topic <topic>                  , entries for a topic
"""
import os, sys, csv, re
HERE=os.path.dirname(os.path.abspath(__file__)); CMD=os.path.dirname(HERE)
LEDGER=os.path.join(CMD,"OS_STALE_ASSUMPTION_LEDGER.csv")

def rows():
    return list(csv.DictReader(open(LEDGER)))

STOP=set("is the a an it can be should of to in on do does has have been now still yet was were are".split())
def toks(s): return {w for w in re.sub(r"[^a-z0-9 ]"," ",s.lower()).split() if w not in STOP and len(w)>2}

def check(claim):
    R=rows(); ct=toks(claim)
    scored=[]
    for r in R:
        hay=toks(r["old_assumption"]+" "+r["topic"])
        ov=len(ct & hay)
        # boost if a distinctive topic word appears literally
        if r["topic"].split("_")[0] in claim.lower(): ov+=2
        if ov: scored.append((ov,r))
    scored.sort(key=lambda x:-x[0])
    print(f"STALE-ASSUMPTION CHECK: {claim}")
    if not scored:
        print("  no matching stale assumption in the ledger. Proceed, but verify against current state (os_current_state_boot.py).")
        return 0
    score,r=scored[0]
    blocked = r["status"]=="CORRECTED"
    print(f"  TOPIC          {r['topic']}")
    print(f"  OLD ASSUMPTION {r['old_assumption']}")
    print(f"  LATEST TRUTH   {r['latest_truth']}")
    print(f"  SOURCE         {r['source_file_or_commit']}")
    print(f"  STATUS         {r['status']}" + (f" (corrected {r['date_corrected']})" if r['date_corrected'] else ""))
    print(f"  ENFORCEMENT    {r['next_enforcement']}")
    if blocked:
        print(f"  VERDICT        BLOCKED , this is a stale assumption. Use LATEST TRUTH, not the old claim.")
        return 1
    print(f"  VERDICT        OPEN RISK , latest truth not yet locked into a refreshed artifact; act on latest truth and refresh the source.")
    return 1

def audit():
    R=[r for r in rows() if r["status"]!="CORRECTED"]
    print(f"OPEN STALE RISKS (not yet corrected): {len(R)}")
    for r in R:
        print(f"  [{r['status']}] {r['topic']} , latest: {r['latest_truth'][:90]}")
        print(f"      enforce: {r['next_enforcement']}")
    if not R: print("  none. every ledger entry is CORRECTED.")
    return 0

def listall():
    for r in rows():
        print(f"  [{r['status']:11s}] {r['topic']:18s} {r['old_assumption'][:60]} -> {r['latest_truth'][:60]}")
    return 0

def topic(t):
    R=[r for r in rows() if t.lower() in r["topic"].lower()]
    if not R: print(f"no ledger entry for topic: {t}"); return 1
    for r in R:
        print(f"[{r['status']}] {r['topic']}\n  old: {r['old_assumption']}\n  now: {r['latest_truth']}\n  src: {r['source_file_or_commit']}\n  enforce: {r['next_enforcement']}")
    return 0

if __name__=="__main__":
    a=sys.argv[1:]
    if not a: print(__doc__); sys.exit(1)
    if a[0]=="check" and len(a)>1: sys.exit(check(" ".join(a[1:])))
    if a[0]=="audit": sys.exit(audit())
    if a[0]=="list": sys.exit(listall())
    if a[0]=="topic" and len(a)>1: sys.exit(topic(a[1]))
    print(__doc__); sys.exit(1)
