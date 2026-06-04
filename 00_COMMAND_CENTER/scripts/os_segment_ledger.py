#!/usr/bin/env python3
"""
os_segment_ledger.py , the coverage-proof primitive.

Turns a text file into a PARTITION of token-safe segments and a ledger that proves
100% coverage: segments are contiguous (start of seg N+1 == end of seg N), they
cover [0, total_chars] with no gap/overlap, and each carries a sha1 checksum.
A file is certifiable only when every segment is read AND the ledger validates.

  build <textfile> <doc_id>     re-wrap to ~180-char lines, segment <=40k chars,
                                write segments/<doc_id>/seg_NNN.txt + LEDGER.csv
  verify <doc_id>               validate the partition (contiguous, no gap, checksums)
  segments dir: 00_COMMAND_CENTER/_segments/<doc_id>/
"""
import os, sys, re, csv, hashlib, math

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEGDIR = os.path.join(ROOT, "_segments")
MAXCHARS = 40000
WRAP = 180


def rewrap(text):
    """Normalize to uniform short lines so segment sizing is predictable (the
    fix for the 25k-token read-cap bug: never segment by raw paragraph lines)."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 > WRAP:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w) if cur else w
    if cur: lines.append(cur)
    return "\n".join(lines)


def cmd_build(a):
    text = open(a.textfile, encoding="utf-8", errors="replace").read()
    norm = rewrap(text)
    total = len(norm)
    d = os.path.join(SEGDIR, a.doc_id)
    os.makedirs(d, exist_ok=True)
    # partition by char count on line boundaries, preserving norm EXACTLY
    # (last line carries no trailing newline so "".join(bodies) == norm).
    lines = norm.split("\n")
    segs, buf, start = [], "", 0
    for i, line in enumerate(lines):
        add = line + ("\n" if i < len(lines) - 1 else "")
        if buf and len(buf) + len(add) > MAXCHARS:
            segs.append((start, start + len(buf), buf)); start += len(buf); buf = add
        else:
            buf += add
    if buf or not segs: segs.append((start, start + len(buf), buf))
    # content-preservation proof: concatenated segments reconstruct the normalized text
    assert "".join(b for _, _, b in segs) == norm, "partition lost content"
    # write segments + ledger
    led = os.path.join(d, "LEDGER.csv")
    with open(led, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["doc_id", "seg_id", "start", "end", "chars", "sha1", "read"])
        for i, (s, e, body) in enumerate(segs, 1):
            sid = f"seg_{i:03d}"
            open(os.path.join(d, sid + ".txt"), "w").write(body)
            w.writerow([a.doc_id, sid, s, e, len(body), hashlib.sha1(body.encode()).hexdigest()[:12], "no"])
    print(f"  {a.doc_id}: {len(segs)} segment(s), {total:,} chars partitioned")
    print(f"  ledger: {led}")
    # immediate partition self-check
    ok = cover_check(segs, total)
    print(f"  partition coverage: {'VALID (contiguous, no gap)' if ok else 'INVALID'}")
    return 0 if ok else 1


def cover_check(segs, total):
    if not segs: return False
    if segs[0][0] != 0: return False
    for i in range(1, len(segs)):
        if segs[i][0] != segs[i - 1][1]: return False
    return segs[-1][1] == total


def cmd_verify(a):
    d = os.path.join(SEGDIR, a.doc_id); led = os.path.join(d, "LEDGER.csv")
    if not os.path.exists(led):
        print(f"  no ledger for {a.doc_id}"); return 1
    rows = list(csv.DictReader(open(led)))
    segs = [(int(r["start"]), int(r["end"]), None) for r in rows]
    total = segs[-1][1]
    # re-check checksums against files
    bad = 0
    for r in rows:
        body = open(os.path.join(d, r["seg_id"] + ".txt")).read()
        if hashlib.sha1(body.encode()).hexdigest()[:12] != r["sha1"]: bad += 1
    nread = sum(1 for r in rows if r["read"] == "yes")
    contiguous = cover_check(segs, total)
    full = contiguous and bad == 0 and nread == len(rows)
    print(f"  {a.doc_id}: segments={len(rows)} read={nread}/{len(rows)} checksum_bad={bad} contiguous={contiguous}")
    print(f"  COVERAGE: {'PROVEN (100%, all read, checksums ok)' if full else 'NOT PROVEN'}")
    return 0 if full else 1


def mark_read(doc_id, seg_ids):
    """Helper used by the batch runner after a segment is read."""
    d = os.path.join(SEGDIR, doc_id); led = os.path.join(d, "LEDGER.csv")
    rows = list(csv.DictReader(open(led)))
    for r in rows:
        if r["seg_id"] in seg_ids: r["read"] = "yes"
    with open(led, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)


def main():
    if len(sys.argv) < 2: print(__doc__); return 1
    import argparse
    p = argparse.ArgumentParser(); sub = p.add_subparsers(dest="cmd")
    b = sub.add_parser("build"); b.add_argument("textfile"); b.add_argument("doc_id")
    v = sub.add_parser("verify"); v.add_argument("doc_id")
    m = sub.add_parser("mark"); m.add_argument("doc_id"); m.add_argument("seg_ids", nargs="+")
    a = p.parse_args()
    if a.cmd == "build": return cmd_build(a)
    if a.cmd == "verify": return cmd_verify(a)
    if a.cmd == "mark": mark_read(a.doc_id, a.seg_ids); print("marked"); return 0
    print(__doc__); return 1


if __name__ == "__main__":
    sys.exit(main())
