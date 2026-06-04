#!/usr/bin/env python3
"""os_boot.py , prints the cold-start boot brief. Loads almost nothing: the active
mission, the cert summary, the next action, and the session-log tail. Run at SessionStart."""
import os, csv, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def head(path, n=999):
    p = os.path.join(ROOT, path)
    return open(p).read() if os.path.exists(p) else f"(missing: {path})"

def tail(path, n=5):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p): return f"(missing: {path})"
    return "\n".join(open(p).read().splitlines()[-n:])

print("=" * 60)
print("OS BOOT BRIEF , resume from disk, load nothing else yet")
print("=" * 60)

# active mission (first ## section of current-state)
cs = head("OS_CURRENT_STATE.md")
import re
m = re.search(r"## ACTIVE MISSION.*?\n(.*?)(?:\n##|\Z)", cs, re.DOTALL)
print("\nACTIVE MISSION:\n" + (m.group(1).strip() if m else "(set OS_CURRENT_STATE.md)"))

# cert summary
cl = os.path.join(ROOT, "OS_CERTIFICATION_LEDGER.csv")
if os.path.exists(cl):
    rows = list(csv.DictReader(open(cl)))
    from collections import Counter
    c = Counter(r.get("cert_status", "?") for r in rows)
    print(f"\nCERT LEDGER: {len(rows)} rows | " + " ".join(f"{k}={v}" for k, v in c.most_common(6)))
    print("  (word-volume truth in OS_CERTIFICATION_REPORT.md; file-count is vanity)")

print("\nNEXT ACTION:\n" + head("NEXT_ACTION.md"))
print("\nSESSION LOG (tail):\n" + tail("SESSION_LOG.md", 5))
print("\nTHEN: invoke os-command-router; pull doctrine/chunks only as needed; do not redo certified work.")
