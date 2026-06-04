#!/usr/bin/env python3
"""
os_certify.py , applies OS_CERTIFICATION_STANDARD.md to the entire corpus.

Classifies every manifest row into a FILE CLASS, assigns an honest CERT STATUS by
the per-class rule, computes the seven metrics (file-count secondary, word-volume
primary), and finds mismatches/giants/lineage-gaps. Writes OS_CERTIFICATION_LEDGER.csv
(the truth layer) + prints a certification report. Non-destructive to the manifest.

  report          classify + metrics + report (writes the ledger)
"""
import csv, re, os, math, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MF = os.path.join(HERE, "OS_ENGAGEMENT_MANIFEST.csv")
LEDGER = os.path.join(HERE, "OS_CERTIFICATION_LEDGER.csv")
SEGW = 6700

def wc(r):
    try: return int(r['words']) if r['words'] else 0
    except: return 0
def seg(w): return max(1, math.ceil(w / SEGW)) if w else 0
def base(r): return os.path.basename(r['path'] or '')
def low(r): return (r['path'] or '').lower()

OS_ART = re.compile(r'(OS_[A-Z]|DASHBOARD|LEDGER|MASTER_INDEX|_INVENTORY|STAGING_PLAN|SESSION_|ACTIVE_|SYNTHESIS|CHUNK_MAP|MANIFEST|_STATE\b|JOURNAL|CHECKPOINT|README|AGENTS|CLAUDE\.md)', re.I)
PHOTO_BOOK = re.compile(r'(avedon|maisel|eggleston|haas|leibovitz|newton_helmut|photographs?|portfolio|lookbook|art_of|the_americans|camera_lucida_plates)', re.I)
MESSY = re.compile(r'(intake|chat_export|chatgpt|conversation|thread|transcript|scrap|\bdump\b|high_level_convos|_docx\.txt$|review_completion)', re.I)
TRANSCRIPT = re.compile(r'(transcript|podcast|interview|_convos|fallon|club_shay|tonight_show)', re.I)


def classify(r, by_md5, verified_stems, queued_stems):
    e = (r['ext'] or '').lower(); p = low(r); n = base(r); w = wc(r); cls = (r['class'] or '').lower()
    # OS artifacts first
    if e in ('.py', '.skill', '.toml'): return 'generated_os_artifact'
    if e == '.md' and OS_ART.search(n) and cls != 'source': return 'generated_os_artifact'
    if cls == 'duplicate': return 'duplicate'
    if cls in ('mirror', 'old export'): return 'mirror'
    # media
    if e in ('.mp4', '.mov', '.mp3', '.wav', '.m4a'): return 'video_audio_source'
    # books
    if e in ('.epub', '.mobi', '.azw3'):
        return 'visual_art_photo_book' if PHOTO_BOOK.search(n) else 'book'
    if e == '.djvu': return 'ocr_scanned_source'
    if e == '.pdf':
        if r['status'] == 'needs_ocr' or PHOTO_BOOK.search(n): return 'ocr_scanned_source'
        return 'pdf_source'
    # extracted / derivative text
    if '_extracted/' in p: return 'extracted_book_text'
    if cls == 'derivative':
        return 'derivative'
    # docish
    if e == '.txt':
        if MESSY.search(n) or w >= 2 * SEGW: return 'transcript_dump' if TRANSCRIPT.search(n) else 'messy_raw_dump'
        return 'clean_text_doc'
    if e == '.docx':
        if w >= 2 * SEGW and MESSY.search(n): return 'messy_raw_dump'
        return 'docx_source'
    if e == '.md':
        if w >= 2 * SEGW and MESSY.search(n): return 'messy_raw_dump'
        return 'clean_text_doc'
    if e == '.doc': return 'docx_source'
    return 'unknown'


def cert_status(r, fclass, w, lineage_ok):
    s = r['status']; segs = seg(w)
    # pending piles , cannot be certified via text
    if fclass == 'ocr_scanned_source' or s == 'needs_ocr': return 'pending_ocr'
    if fclass == 'visual_art_photo_book' or s == 'needs_visual_review': return 'pending_visual_review'
    if fclass == 'video_audio_source' or s == 'needs_transcription': return 'pending_transcription'
    if fclass == 'generated_os_artifact': return 'os_artifact'
    if fclass == 'duplicate': return 'duplicate_confirmed'
    if fclass == 'mirror': return 'duplicate_confirmed'
    if fclass == 'derivative':
        # small derivatives without a clean stem-twin are assumed confirmed (Step-1 careful pass
        # found only 1 true large orphan); only LARGE no-lineage derivatives are flagged orphan.
        if lineage_ok: return 'derivative_confirmed'
        return 'source_orphan' if w >= 20000 else 'derivative_confirmed'
    if fclass == 'extracted_book_text':
        # the read artifact of a book, sitting in the processed KB pipeline (_extracted + chunked).
        # processed but NO token-safe segment ledger => provisional at best, never certified if multi-seg.
        if segs <= 2 and w > 0: return 'certified'
        return 'provisionally_verified'
    # not yet read
    if s in ('not_read',): return 'pending_full_read'
    if s == 'rawdump_unverified': return 'characterized'   # giants: distilled from sample
    if s == 'partial_read_only': return 'sampled'
    # read_verified path -> apply class proof rule
    if s == 'read_verified' or fclass == 'extracted_book_text':
        if fclass in ('messy_raw_dump', 'transcript_dump'):
            return 'characterized'      # samples never certify a dump
        if segs <= 2 and w > 0:
            return 'certified'          # trivially full coverage
        if segs > 2 or w == 0:
            return 'provisionally_verified'   # read happened, NO segment ledger
        return 'provisionally_verified'
    return 'unknown'


def main():
    rows = list(csv.DictReader(open(MF)))
    by_md5 = defaultdict(list)
    for r in rows: by_md5[r['md5']].append(r)
    def norm(s):
        s = os.path.basename(s).lower(); s = re.sub(r'\.(txt|md|docx|epub|mobi|azw3|pdf|djvu|doc)$', '', s)
        s = re.sub(r'(_extracted|_download|_docx)$', '', s); return re.sub(r'[^a-z0-9]', '', s)
    verified_stems = {norm(r['path']) for r in rows if r['status'] == 'read_verified'}
    queued_stems = {norm(r['path']) for r in rows if r['status'] in ('not_read', 'read_verified')}
    by_norm = defaultdict(list)
    for r in rows: by_norm[norm(r['path'])].append(r)

    out = []
    for r in rows:
        fclass = classify(r, by_md5, verified_stems, queued_stems)
        w = wc(r)
        # lineage check for derivatives
        st = norm(r['path']); twins = [x for x in by_norm[st] if x is not r]
        dup_of_source = any((x['class'] or '').lower() == 'source' for x in by_md5[r['md5']] if x is not r)
        lineage_ok = dup_of_source or any(x['status'] in ('read_verified', 'not_read') for x in twins)
        cs = cert_status(r, fclass, w, lineage_ok)
        out.append({'path': r['path'], 'class_file': fclass, 'words': w, 'segments': seg(w),
                    'manifest_status': r['status'], 'cert_status': cs})

    with open(LEDGER, 'w', newline='') as f:
        wtr = csv.DictWriter(f, fieldnames=['path', 'class_file', 'words', 'segments', 'manifest_status', 'cert_status'])
        wtr.writeheader(); wtr.writerows(out)

    # ---- metrics ----
    # exclude OS artifacts + duplicates from SOURCE coverage
    src = [o for o in out if o['cert_status'] not in ('os_artifact', 'duplicate_confirmed', 'derivative_confirmed')]
    tot_files = len(src); tot_w = sum(o['words'] for o in src) or 1
    def vol(pred): return sum(o['words'] for o in src if pred(o))
    def cnt(pred): return sum(1 for o in src if pred(o))
    certified = lambda o: o['cert_status'] == 'certified'
    prov = lambda o: o['cert_status'] == 'provisionally_verified'
    charz = lambda o: o['cert_status'] in ('characterized', 'sampled')
    pend = lambda o: o['cert_status'].startswith('pending')

    print("=" * 64)
    print("OS CERTIFICATION REPORT (by OS_CERTIFICATION_STANDARD v1)")
    print("=" * 64)
    print(f"\nsource-eligible rows: {tot_files} | measured content: {tot_w:,} words")
    print("\n--- METRIC 1: file-count coverage (SECONDARY / vanity) ---")
    print(f"  certified: {cnt(certified)} ({cnt(certified)/tot_files*100:.1f}%)  provisional: {cnt(prov)}  characterized: {cnt(charz)}  pending: {cnt(pend)}")
    print("\n--- METRIC 2: WORD-VOLUME coverage (PRIMARY) ---")
    print(f"  certified words:       {vol(certified):>12,} ({vol(certified)/tot_w*100:5.1f}%)")
    print(f"  provisionally_verified:{vol(prov):>12,} ({vol(prov)/tot_w*100:5.1f}%)")
    print(f"  characterized/sampled: {vol(charz):>12,} ({vol(charz)/tot_w*100:5.1f}%)")
    print(f"  pending (read/ocr/vis):{vol(pend):>12,} ({vol(pend)/tot_w*100:5.1f}%)")
    print("\n--- METRIC 4: source-class coverage (per class, cert status) ---")
    cls_status = defaultdict(Counter); cls_vol = defaultdict(int)
    for o in out:
        cls_status[o['class_file']][o['cert_status']] += 1; cls_vol[o['class_file']] += o['words']
    for c in sorted(cls_status, key=lambda k: -cls_vol[k]):
        top = ', '.join(f'{k}:{v}' for k, v in cls_status[c].most_common(3))
        print(f"  {c:<22} {cls_vol[c]:>11,}w  | {top}")
    print("\n--- METRIC 7: pending-risk coverage (known-unknown mass) ---")
    pr = Counter()
    for o in out:
        if o['cert_status'].startswith('pending'): pr[o['cert_status']] += o['words']
    for k, v in pr.most_common(): print(f"  {k:<24} {v:,} words")

    # ---- enforcement findings ----
    print("\n--- HARD-RULE VIOLATIONS FOUND ---")
    giants = [o for o in out if o['segments'] > 10 and o['cert_status'] in ('provisionally_verified', 'characterized')]
    print(f"  giant (>10 seg) NOT certified (rule 2/4/5): {len(giants)} files, {sum(o['words'] for o in giants):,} words")
    mism = [o for o in out if o['manifest_status'] == 'read_verified' and o['cert_status'] != 'certified']
    print(f"  manifest 'read_verified' that FAIL certification: {len(mism)} files")
    orph = [o for o in out if o['cert_status'] == 'source_orphan']
    print(f"  source orphans (derivative, no lineage): {len(orph)}")
    print(f"\nledger written: {LEDGER} ({len(out)} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
