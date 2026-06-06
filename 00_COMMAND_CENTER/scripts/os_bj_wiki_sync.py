#!/usr/bin/env python3
"""
os_bj_wiki_sync.py , safe seam between the EXECUTION OS (AI-Brain-Refinery) and the SECOND BRAIN (BJ-WIKI).
Append-only + read-only. Never overwrites or deletes anything in BJ-WIKI. See OS_TO_BJ_WIKI_SYNC_PLAN.md.

  os_bj_wiki_sync.py status                      , paths + hot-cache age vs OS_CURRENT_STATE
  os_bj_wiki_sync.py log "<decision>" [commit]   , APPEND a dated decision line to BJ-WIKI/wiki/log.md
"""
import os, sys, datetime
WIKI=os.path.expanduser("~/Documents/BJ-WIKI")
HOT=os.path.join(WIKI,"_meta","hot-cache.md")
LOG=os.path.join(WIKI,"wiki","log.md")
CMD=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CUR=os.path.join(CMD,"OS_CURRENT_STATE.md")
def mtime(p):
    try: return datetime.datetime.fromtimestamp(os.path.getmtime(p))
    except: return None
def status():
    print("BJ-WIKI SYNC STATUS")
    print(f"  wiki present: {os.path.isdir(WIKI)}")
    print(f"  hot-cache: {HOT} ({'exists '+str(mtime(HOT)) if os.path.exists(HOT) else 'MISSING'})")
    print(f"  log: {LOG} ({'exists' if os.path.exists(LOG) else 'MISSING'})")
    print(f"  OS_CURRENT_STATE: {mtime(CUR)}")
    h,c=mtime(HOT),mtime(CUR)
    if h and c and h>c: print("  ! hot-cache is NEWER than OS_CURRENT_STATE , review for execution-relevant truth (newest wins)")
    elif h and c: print("  OS_CURRENT_STATE is current vs hot-cache")
    return 0
def log(decision, commit=""):
    if not os.path.isdir(os.path.dirname(LOG)):
        print(f"BJ-WIKI/wiki not found at {LOG}; cannot log"); return 1
    line=f"- {datetime.date.today().isoformat()} (OS): {decision}" + (f" [commit {commit}]" if commit else "") + "\n"
    with open(LOG,"a") as f: f.write(line)
    print(f"appended to {LOG}:\n  {line.strip()}")
    return 0
if __name__=="__main__":
    a=sys.argv[1:]
    if a and a[0]=="status": sys.exit(status())
    if len(a)>=2 and a[0]=="log": sys.exit(log(a[1], a[2] if len(a)>2 else ""))
    print(__doc__); sys.exit(1)
