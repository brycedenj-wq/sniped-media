#!/usr/bin/env python3
"""
os_form_ingest.py , normalize a Tally OR Formspree CSV export into RESPONSES.csv.

Handles both exporters by header heuristics. Dedups by email. Never deletes.
  python3 os_form_ingest.py <export.csv> [--source private_link]
RESPONSES.csv schema: ts,email,method_interest_A,print_interest_C,intent,source
"""
import csv, sys, os, re, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.join(HERE, "RESPONSES.csv")
FIELDS = ["ts", "email", "method_interest_A", "print_interest_C", "intent", "source"]


def find(headers, *needles):
    for h in headers:
        hl = h.lower()
        if any(n in hl for n in needles):
            return h
    return None


def truthy(v):
    return str(v).strip().lower() in ("yes", "true", "1", "on", "checked", "x") or "breakdown" in str(v).lower() or "print" in str(v).lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export"); ap.add_argument("--source", default="private_link")
    a = ap.parse_args()
    rows = list(csv.DictReader(open(a.export, encoding="utf-8", errors="replace")))
    if not rows:
        print("  empty export"); return 0
    H = list(rows[0].keys())
    c_ts = find(H, "submitted", "date", "time", "created")
    c_email = find(H, "email", "e-mail")
    c_method = find(H, "breakdown", "built", "method", "how this")
    c_print = find(H, "print", "first frame", "limited")
    c_intent = find(H, "make", "intent", "what do you")
    c_source = find(H, "source")
    # load existing emails for dedup
    existing = set()
    if os.path.exists(DEST):
        for r in csv.DictReader(open(DEST)):
            existing.add((r.get("email") or "").strip().lower())
    new = []
    for r in rows:
        email = (r.get(c_email, "") if c_email else "").strip()
        if not email or email.lower() in existing:
            continue
        existing.add(email.lower())
        new.append({
            "ts": (r.get(c_ts, "") if c_ts else "").strip(),
            "email": email,
            "method_interest_A": "yes" if (c_method and truthy(r.get(c_method))) else "",
            "print_interest_C": "yes" if (c_print and truthy(r.get(c_print))) else "",
            "intent": (r.get(c_intent, "") if c_intent else "").strip()[:120],
            "source": (r.get(c_source, "") if c_source else "").strip() or a.source,
        })
    write_header = not os.path.exists(DEST) or os.path.getsize(DEST) == 0
    with open(DEST, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if write_header: w.writeheader()
        for r in new: w.writerow(r)
    print(f"  ingested {len(new)} new response(s) (dedup by email) -> {DEST}")
    print(f"  mapped columns: email={c_email} method={c_method} print={c_print} intent={c_intent} ts={c_ts}")
    if c_email is None: print("  WARNING: no email column detected , check the export header")
    return 0


if __name__ == "__main__":
    sys.exit(main())
