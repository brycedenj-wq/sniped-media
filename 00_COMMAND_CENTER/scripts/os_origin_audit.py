#!/usr/bin/env python3
"""
os_origin_audit.py , prove the 'derivative' classification before dismissing files.

A derivative is only safely dismissed if hash AND origin show it is derived from a
source that IS in the read queue / verified. md5 proves identity, not derivation.
This classifies each large derivative as:
  confirmed_derivative      , extraction/consolidation artifact in a known derivative dir
  duplicate_mirror          , md5 matches another row (exact copy; the original covers it)
  possible_misclassified_source , real content not represented elsewhere -> REQUEUE
  unknown                   , can't tell locally -> REQUEUE for a 1-segment spot read
Plus the deeper flag: extracted book text whose SOURCE book is NOT read_verified, or
whose true size (now visible) means the 'verified' book was never proven at full coverage.

  report          print breakdown + requeue list + per-file confidence
"""
import csv, re, os, sys
from collections import Counter, defaultdict

MF = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "OS_ENGAGEMENT_MANIFEST.csv")
DERIV_DIR = re.compile(r'(01_KNOWLEDGE_BASE|/batches/|_extracted/|/outputs/|/indexes/)', re.I)
DERIV_NAME = re.compile(r'(MASTER_INDEX|CHUNK|_chunks|chunk_map|consolidat|_INDEX\b|BATCH_\d)', re.I)
DOWNLOADS = re.compile(r'Downloads/\s*SNIPED_OS', re.I)
DOCISH = {'.md', '.docx', '.txt', '.html', '.htm', '.rtf', '.epub', '.pdf', '.mobi', '.azw3'}


def wc(r):
    try: return int(r['words']) if r['words'] else 0
    except: return 0
def stem(r):
    t = (r['title'] or os.path.basename(r['path'] or '')).lower()
    return re.sub(r'\.(txt|md|docx|epub|mobi|azw3|pdf|djvu)$', '', t)


def main():
    rows = list(csv.DictReader(open(MF)))
    by_md5 = defaultdict(list)
    for r in rows: by_md5[r['md5']].append(r)
    sources = [r for r in rows if (r['class'] or '').lower() == 'source']
    src_stems = {stem(r): r for r in sources}
    src_verified_stems = {stem(r) for r in sources if r['status'] == 'read_verified'}

    deriv = [r for r in rows if (r['class'] or '').lower() in ('derivative', 'mirror', 'old export') and wc(r) >= 20000]
    out = Counter(); requeue = []; book_gap = []
    per_file = []
    for r in deriv:
        p = r['path'] or ''; w = wc(r); md5 = r['md5']
        dup = len([x for x in by_md5[md5] if x is not r]) > 0
        verdict = conf = None
        if dup and any((x['class'] or '').lower() == 'source' for x in by_md5[md5] if x is not r):
            verdict, conf = 'duplicate_mirror', 0.95
        elif DERIV_DIR.search(p) or DERIV_NAME.search(r['title'] or p):
            verdict, conf = 'confirmed_derivative', 0.9
            # deeper check: is this an extracted BOOK whose source is NOT verified?
            if '_extracted/' in p:
                st = stem(r)
                # match a source book by stem overlap
                covered = any(st in s or s in st for s in src_verified_stems) or st in src_verified_stems
                if not covered:
                    book_gap.append((w, p))
        elif DOWNLOADS.search(p) and (os.path.splitext(p)[1].lower() in DOCISH):
            verdict, conf = 'possible_misclassified_source', 0.5
            requeue.append((w, p))
        else:
            verdict, conf = 'unknown', 0.4
            requeue.append((w, p))
        out[verdict] += 1
        per_file.append((verdict, conf, w, p))

    print("=== ORIGIN AUDIT , 331 large derivatives (>=20k words) ===\n")
    for k in ['confirmed_derivative', 'duplicate_mirror', 'possible_misclassified_source', 'unknown']:
        print(f"  {k:<32} {out.get(k,0)}")
    print(f"\n  total: {len(deriv)}")
    print(f"\n=== MUST RE-ENTER READ QUEUE (possible source / unknown): {len(requeue)} ===")
    for w, p in sorted(requeue, reverse=True)[:25]:
        print(f"  {w:>8,}w  {p.replace('/Users/sniper/','~/')[:78]}")
    if len(requeue) > 25: print(f"  ... +{len(requeue)-25} more")
    print(f"\n=== DEEPER FLAG: extracted BOOK text whose source is NOT verified: {len(book_gap)} ===")
    for w, p in sorted(book_gap, reverse=True)[:15]:
        print(f"  {w:>8,}w  {os.path.basename(p)}")
    bg_vol = sum(w for w, _ in book_gap)
    print(f"  book-extraction content not provably verified: {bg_vol:,} words")
    print(f"\n=== confidence summary ===")
    avg = sum(c for _, c, _, _ in per_file) / len(per_file)
    print(f"  mean origin-confidence across 331: {avg:.2f}")
    print(f"  high-confidence dismissable (>=0.9): {sum(1 for v,c,_,_ in per_file if c>=0.9)}")
    print(f"  must-act (requeue): {len(requeue)}  |  deeper book-coverage flag: {len(book_gap)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
