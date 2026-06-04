#!/usr/bin/env python3
"""os-completion-verify: blocks a 'done' claim unless the manifest supports it.
Usage: python3 os_completion_verify.py [scope_substring]
Exit 0 = the scope is fully read_verified (safe to claim done).
Exit 1 = pending items exist in scope (NOT done); lists them."""
import csv, os, sys
CC=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAN=os.path.join(CC,"OS_ENGAGEMENT_MANIFEST.csv")
scope=sys.argv[1] if len(sys.argv)>1 else ""
rows=[r for r in csv.DictReader(open(MAN)) if r["class"]=="source"]
if scope: rows=[r for r in rows if scope.lower() in r["path"].lower()]
pending=[r for r in rows if not r["status"].startswith("read_verified")]
hard=[r for r in pending if r["status"] in ("not_read","partial_read_only","read_low_confidence")]
print(f"scope='{scope or 'ALL'}' | rows={len(rows)} | verified={len(rows)-len(pending)} | pending={len(pending)} (hard-unread={len(hard)})")
if hard:
    print("NOT DONE , unread/partial in scope:")
    for r in hard[:15]: print(f"  [{r['status']}] {os.path.basename(r['path'])[:60]}")
    sys.exit(1)
if pending:
    print(f"OK to claim done for READING; note {len(pending)} flagged-pending (ocr/visual/transcription) , disclose them.")
sys.exit(0)
