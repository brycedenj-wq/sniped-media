#!/usr/bin/env python3
"""
os_methodology_audit.py , audit whether 'read_verified' methodology matched file type.

read_verified only ever proved the read did not truncate. It never proved that a
messy raw dump (transcript pile / scrape / chat export / huge compilation) was read
with FULL segment coverage and distilled as a messy corpus. This audit separates:
  - read_verified_clean   : books + small authored docs + code (methodology OK)
  - rawdump_unverified     : huge or external-capture dumps with NO coverage ledger
  - rawdump_review         : soft-signal compilations to be hand-classified
and reports coverage by FILE COUNT and by CONTENT VOLUME (the honest metric).

  report                 print the breakdown (no writes)
  downgrade --write      re-status the unambiguous messy files -> rawdump_unverified
"""
import csv, re, sys, math, os
from collections import Counter

MF = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "OS_ENGAGEMENT_MANIFEST.csv")
BOOK_EXT = {'.epub', '.mobi', '.azw3', '.pdf', '.djvu', '.doc'}
DOCISH = {'.md', '.docx', '.txt', '.html', '.htm', '.rtf'}
CODE = {'.py', '.skill', '.toml'}
HUGE = 200000  # words; a single file this big cannot be a clean doc
# external-capture signals = almost certainly a raw dump regardless of size
HARD_MESSY = re.compile(r'(chatgpt|chat[_ -]|gpt[-_]|claude|conversation|thread|transcript|scrap|\bdump\b|\braw\b|\bmessages?\b|session|youtube|reddit|tweet|substack|export\b|intake)', re.I)
# soft signals = could be OS-authored synthesis OR a compilation -> review, don't auto-downgrade
SOFT_MESSY = re.compile(r'(synthesis|master|research|compil|merged|combined|archive|backup|feed|timeline|notes?\b)', re.I)


def wc(r):
    try: return int(r['words']) if r['words'] else 0
    except: return 0


def name(r): return (r['title'] or r['path'] or '')


SEG_W = 6700           # words per token-safe segment (~40k chars)
MULTI = 2 * SEG_W      # >=2 segments => coverage proof actually matters
def segs(r): return max(1, math.ceil(wc(r) / SEG_W))
def klass(r):
    e = (r['ext'] or '').lower(); w = wc(r); n = name(r)
    if e in CODE: return 'code_config'
    if e in BOOK_EXT: return 'book_clean'
    if e in DOCISH:
        messy = bool(HARD_MESSY.search(n)) or (bool(SOFT_MESSY.search(n)) and w >= 20000)
        if w >= HUGE: return 'rawdump_unverified'           # huge => raw dump, coverage cannot be 1-pass
        if messy and w >= MULTI: return 'rawdump_review'     # multi-segment messy => verify coverage
        if messy: return 'docish_messy_single'              # single-segment messy => fully read, low risk
        return 'docish_clean'
    return 'other'


def load(): return list(csv.DictReader(open(MF)))


def report(rows):
    verified = [r for r in rows if r['status'] == 'read_verified']
    tot_w = sum(wc(r) for r in verified) or 1
    buckets = Counter(klass(r) for r in verified)
    vol = Counter()
    for r in verified: vol[klass(r)] += wc(r)
    print("=== METHODOLOGY AUDIT (read_verified files) ===")
    print(f"verified files: {len(verified)} | total content: {tot_w:,} words\n")
    print(f"{'type':<22}{'files':>7}{'% files':>9}{'words':>14}{'% volume':>10}")
    for k in ['book_clean', 'docish_clean', 'docish_messy_single', 'code_config', 'rawdump_review', 'rawdump_unverified', 'other']:
        f = buckets.get(k, 0); v = vol.get(k, 0)
        print(f"{k:<22}{f:>7}{f/len(verified)*100:>8.1f}%{v:>14,}{v/tot_w*100:>9.1f}%")
    clean_vol = vol['book_clean'] + vol['docish_clean'] + vol['code_config'] + vol['docish_messy_single']
    unproven_vol = vol['rawdump_unverified'] + vol['rawdump_review']
    print(f"\nMETHODOLOGY-VALID coverage (by volume): {clean_vol/tot_w*100:.1f}%")
    print(f"UNPROVEN raw-dump coverage (by volume): {unproven_vol/tot_w*100:.1f}%")
    print(f"  -> the file-count score hides this; {unproven_vol/tot_w*100:.0f}% of CONTENT is unproven.\n")
    print("=== rawdump_unverified (re-read queue, biggest first) ===")
    rd = sorted([r for r in verified if klass(r) == 'rawdump_unverified'], key=wc, reverse=True)
    for r in rd[:20]:
        print(f"  {wc(r):>9,} w  ~{math.ceil(wc(r)/6700):>4} seg  {name(r)[:52]}")
    print(f"  ... {len(rd)} files total")
    rv = [r for r in verified if klass(r) == 'rawdump_review']
    print(f"\n=== rawdump_review (hand-classify): {len(rv)} files ===")
    for r in sorted(rv, key=wc, reverse=True)[:10]:
        print(f"  {wc(r):>8,} w  {name(r)[:52]}")
    # derivative requeue risk
    deriv = [r for r in rows if (r['class'] or '').lower() in ('derivative', 'mirror', 'old export')]
    bigd = [r for r in deriv if wc(r) >= 20000]
    print(f"\n=== DERIVATIVE/MIRROR requeue risk ===")
    print(f"  derivative/mirror/old-export rows: {len(deriv)}; LARGE (>=20k w) needing ORIGIN proof: {len(bigd)}")
    return rd, rv, bigd


def downgrade(rows, write):
    changed = 0
    for r in rows:
        if r['status'] == 'read_verified' and klass(r) == 'rawdump_unverified':
            r['status'] = 'rawdump_unverified'; changed += 1
    print(f"  re-status read_verified -> rawdump_unverified: {changed} files")
    if write:
        with open(MF, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
        print(f"  manifest written.")
    else:
        print("  (dry-run; pass --write to apply)")
    return changed


def main():
    rows = load()
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'report'
    if cmd == 'report':
        report(rows)
    elif cmd == 'downgrade':
        report(rows)
        print()
        downgrade(rows, '--write' in sys.argv)
    else:
        print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main())
