#!/usr/bin/env python3
"""os-wave-lock: lifecycle for the workflow concurrency lock.
  acquire [runid]  - set lock (used by cost guard); refuses if a FRESH lock exists
  release          - clear lock on wave completion/failure/timeout (call when handling results)
  status           - show lock state + age
  clear            - manual override (force-remove)
Stale window: a lock older than MAX_AGE auto-clears (crash recovery)."""
import sys, os, time, json
LOCK="/tmp/os_wf.lock"; MAX_AGE=5400  # 90 min = longest plausible wave; auto-stale after
def age(): return time.time()-os.path.getmtime(LOCK) if os.path.exists(LOCK) else None
def main():
    cmd=sys.argv[1] if len(sys.argv)>1 else "status"
    a=age()
    if cmd=="acquire":
        if a is not None and a<MAX_AGE:
            print(f"BLOCK: wave in flight ({int(a)}s old). release/clear first."); return 2
        json.dump({"runid":sys.argv[2] if len(sys.argv)>2 else "?","ts":time.time()},open(LOCK,"w")); print("acquired"); return 0
    if cmd=="release":
        if os.path.exists(LOCK): os.remove(LOCK); print("released")
        else: print("no lock")
        return 0
    if cmd=="clear":
        if os.path.exists(LOCK): os.remove(LOCK); print("cleared (override)")
        else: print("no lock")
        return 0
    # status
    if a is None: print("lock: NONE (free)")
    elif a>=MAX_AGE: os.remove(LOCK); print(f"lock: STALE ({int(a)}s) -> auto-cleared")
    else: print(f"lock: HELD ({int(a)}s old, stale at {MAX_AGE}s)")
    return 0
sys.exit(main())
