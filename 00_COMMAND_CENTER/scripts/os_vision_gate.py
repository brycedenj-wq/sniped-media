#!/usr/bin/env python3
"""os-vision-reject-gate (production-integrated). Enforces: no asset reaches 06_approved without a
VISION_GATE_LOG record. The visual scoring is done by the model (Reads the asset); this script
enforces the folder flow + the log.
Usage:
  os_vision_gate.py intake <project> <asset_path>          - copy to 05_vision_quarantine, print checklist
  os_vision_gate.py verdict <project> <asset> <SHIP|FIX|REJECT> "<scores>" - move + LOG (SHIP->approved, REJECT->rejected)
  os_vision_gate.py audit <project>                        - FAIL if any approved asset lacks a log record
  os_vision_gate.py <asset_path>                           - standalone checklist (no project)"""
import sys, os, csv, shutil, time
CC=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT=os.path.join(CC,"campaign_house")
RUBRIC=["slop","hands","skin","clothing","text","identity","brand","likeness","beat_source"]
def checklist(name):
    print(f"VISION REJECT-GATE for: {name}  (model Reads the asset and scores each; any hard-fail = REJECT)")
    for r in RUBRIC: print(f"  [ ] {r}")
    print("  Verdict: SHIP / FIX / REJECT. Owned character only, must beat an honest camera frame.")
def proj(p): return os.path.join(ROOT,p)
def logp(p): return os.path.join(proj(p),"10_logs","VISION_GATE_LOG.csv")
def main():
    a=sys.argv
    if len(a)==2 and os.path.exists(a[1]): checklist(os.path.basename(a[1])); return 0
    cmd=a[1] if len(a)>1 else "help"
    if cmd=="intake":
        project,asset=a[2],a[3]
        if not os.path.exists(asset): print("missing asset"); return 1
        q=os.path.join(proj(project),"05_vision_quarantine"); os.makedirs(q,exist_ok=True)
        dst=os.path.join(q,os.path.basename(asset)); shutil.copy2(asset,dst)
        print(f"intake -> {dst}"); checklist(os.path.basename(asset)); return 0
    if cmd=="verdict":
        project,asset,verdict=a[2],a[3],a[4].upper(); scores=a[5] if len(a)>5 else ""
        q=os.path.join(proj(project),"05_vision_quarantine",os.path.basename(asset))
        dest_dir="06_approved" if verdict=="SHIP" else "07_rejected"
        dd=os.path.join(proj(project),dest_dir); os.makedirs(dd,exist_ok=True)
        if os.path.exists(q): shutil.move(q,os.path.join(dd,os.path.basename(asset)))
        with open(logp(project),"a",newline="") as f:
            csv.writer(f).writerow([time.strftime("%Y-%m-%d %H:%M"),os.path.basename(asset),verdict]+
                                   ([scores] if scores else [""]* (len(RUBRIC))) + ["model"])
        print(f"verdict {verdict} logged -> {dest_dir}"); return 0
    if cmd=="audit":
        project=a[2]; ap=os.path.join(proj(project),"06_approved")
        logged=set()
        if os.path.exists(logp(project)):
            for row in csv.reader(open(logp(project))):
                if row and row[1]!="asset": logged.add(row[1])
        approved=[f for f in os.listdir(ap) if f!=".gitkeep"] if os.path.isdir(ap) else []
        orphan=[f for f in approved if f not in logged]
        if orphan: print(f"AUDIT FAIL: {len(orphan)} approved asset(s) with NO gate record: {orphan}"); return 1
        print(f"AUDIT PASS: {len(approved)} approved, all have gate records."); return 0
    print(__doc__); return 0
if __name__=="__main__": sys.exit(main())
