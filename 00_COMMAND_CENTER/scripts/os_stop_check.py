#!/usr/bin/env python3
"""os-stop-check: Stop hook, warn-mode. On session/run end, checks the manifest/dashboard for a
CONTRADICTION (corruption or dashboard-out-of-sync). Warns ONCE per session (marker) via exit 2;
otherwise exits 0 silently. Never loops (marker), never blocks on a normal pending pile."""
import csv, os, sys, re, time
CC=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAN=os.path.join(CC,"OS_ENGAGEMENT_MANIFEST.csv"); DB=os.path.join(CC,"OS_ENGAGEMENT_DASHBOARD.md")
MARK="/tmp/os_stop_warned"
try:
    rows=list(csv.DictReader(open(MAN))); src=[r for r in rows if r["class"]=="source"]
    from collections import Counter
    sc=Counter(r["status"] for r in src); V=sc.get("read_verified",0)
    paths=[r["path"] for r in rows]
    dup=len(paths)-len(set(paths)); empty=sum(1 for r in src if not r["status"])
    # dashboard vs manifest verified mismatch
    db=open(DB).read(); m=re.search(r"\((\d+) / [\d,]+ verified", db)
    db_v=int(m.group(1)) if m else V
    issues=[]
    if dup: issues.append(f"{dup} duplicate manifest paths")
    if empty: issues.append(f"{empty} empty-status source rows")
    if abs(db_v-V)>0: issues.append(f"dashboard says {db_v} verified, manifest says {V} (run os_checkpoint.py --write)")
    if issues:
        # warn once per ~2h
        recent = os.path.exists(MARK) and (time.time()-os.path.getmtime(MARK) < 7200)
        if not recent:
            open(MARK,"w").write(str(time.time()))
            sys.stderr.write("[os-stop-check WARNING] completion/state contradiction: "+"; ".join(issues)+". Reconcile before claiming done.\n")
            sys.exit(2)
except Exception:
    pass
sys.exit(0)
