#!/usr/bin/env python3
"""
os_form_score.py , score RESPONSES.csv into a keep/kill/scale verdict per rail.
Counts method (A), print (C), both, by source, and intent patterns. Writes SCORE.md.
  python3 os_form_score.py [--days 7]
NOT validation until the link was actually shared. Counts only.
"""
import csv, os, sys, re, argparse
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "RESPONSES.csv")
OUT = os.path.join(HERE, "SCORE.md")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--days", type=int, default=7); a = ap.parse_args()
    rows = list(csv.DictReader(open(SRC))) if os.path.exists(SRC) else []
    n = len(rows)
    A = sum(1 for r in rows if r.get("method_interest_A") == "yes")
    C = sum(1 for r in rows if r.get("print_interest_C") == "yes")
    both = sum(1 for r in rows if r.get("method_interest_A") == "yes" and r.get("print_interest_C") == "yes")
    by_source = Counter((r.get("source") or "?") for r in rows)
    intents = [r.get("intent", "").strip() for r in rows if r.get("intent", "").strip()]
    # crude intent clustering by keyword
    kw = Counter()
    for it in intents:
        for w in re.findall(r"[a-z]{4,}", it.lower()):
            if w not in ("that", "this", "with", "make", "your", "from", "have", "want"):
                kw[w] += 1

    def verdict(count, kill_at_zero=True, keep_thr=1, scale_thr=25):
        if count >= scale_thr: return "SCALE"
        if count >= keep_thr: return "KEEP"
        return "KILL-WATCH"
    vA = verdict(A, scale_thr=25)
    vC = "SCALE" if C >= 300 else ("KEEP" if C >= 1 else "KILL-WATCH")

    lines = [f"# FORM SCORE ({n} responses)", "",
             f"- **Rail A (method): {A}** , verdict **{vA}** (keep>=1 / scale>=25)",
             f"- **Rail C (print): {C}** , verdict **{vC}** (keep>=1 / scale>=300 before any run)",
             f"- both A+C: {both} | A-only: {A-both} | C-only: {C-both}",
             f"- by source: {dict(by_source)}",
             f"- intent patterns (top): {dict(kw.most_common(8)) if kw else 'none yet'}",
             "",
             "RULE: not validation until the link was shared with real people. No rail crowned on early signal.",
             "Thresholds: A keep>=1 on $0 in 7d, scale>=25. C keep>=1, scale>=300 (then validation-before-manufacture gate)."]
    open(OUT, "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    print(f"\n  -> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
