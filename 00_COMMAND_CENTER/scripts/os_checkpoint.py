#!/usr/bin/env python3
"""os-checkpoint: reconcile manifest -> rebuild engagement dashboard headline + audit taxonomy,
run consistency checks, print an OS-health snapshot. Deterministic, no model tokens.
Usage: python3 os_checkpoint.py [--write]   (--write updates the dashboard; default is dry-run)"""
import csv, os, sys, re
from collections import Counter
CC=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAN=os.path.join(CC,"OS_ENGAGEMENT_MANIFEST.csv")
DB=os.path.join(CC,"OS_ENGAGEMENT_DASHBOARD.md")
def main(write=False):
    rows=list(csv.DictReader(open(MAN)))
    src=[r for r in rows if r["class"]=="source"]
    TOT=len(src); sc=Counter(r["status"] for r in src); V=sc.get("read_verified",0)
    # consistency checks
    paths=[r["path"] for r in rows]
    dup=[p for p,c in Counter(paths).items() if c>1]
    nostat=[r for r in src if not r["status"]]
    issues=[]
    if dup: issues.append(f"{len(dup)} duplicate manifest path rows")
    if nostat: issues.append(f"{len(nostat)} source rows with empty status")
    # report
    print(f"=== OS CHECKPOINT ===")
    print(f"sources: {TOT} | VERIFIED: {V} ({V/TOT*100:.1f}%)")
    for k in sorted(sc): print(f"  {k}: {sc[k]}")
    pending=sc.get("needs_ocr",0)+sc.get("needs_visual_review",0)+sc.get("needs_transcription",0)
    print(f"pending pile (ocr+visual+transcription): {pending}")
    print(f"consistency: {'CLEAN' if not issues else 'ISSUES -> '+'; '.join(issues)}")
    if write:
        d=open(DB).read()
        d=re.sub(r"\| \*\*Percent of OS engaged \(VERIFIED only\)\*\* \| \*\*~[\d.]+%\*\*[^|]*\|",
                 f"| **Percent of OS engaged (VERIFIED only)** | **~{V/TOT*100:.1f}%** ({V} / {TOT:,} verified) |", d)
        for st in ["read_verified","read_low_confidence","partial_read_only","not_read","needs_ocr","needs_visual_review","needs_transcription"]:
            d=re.sub(rf"(\| \*\*{st}\*\* \| )\d+( \|)", rf"\g<1>{sc.get(st,0)}\g<2>", d)
        open(DB,"w").write(d)
        print("dashboard reconciled from manifest.")
    else:
        print("(dry-run; pass --write to reconcile the dashboard)")
    return 0 if not issues else 1
if __name__=="__main__":
    sys.exit(main("--write" in sys.argv))
