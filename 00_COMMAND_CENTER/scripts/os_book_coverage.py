#!/usr/bin/env python3
"""
os_book_coverage.py , cheap LOCAL book-layer coverage audit (no re-reads, no spend).

Answers: were books certified to the segment-ledger standard, or only extracted/chunked?
Builds OS_BOOK_COVERAGE_LEDGER.csv classifying every book by what PROOF exists.
Rule: chunks are NOT coverage proof unless they carry offsets/segment ledger (they do not).
"""
import csv, os, glob, json, re, math
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)
MF = os.path.join(ROOT, "OS_ENGAGEMENT_MANIFEST.csv")
LEDGER = os.path.join(ROOT, "OS_BOOK_COVERAGE_LEDGER.csv")
BOOK_EXT = {'.epub', '.mobi', '.azw3', '.pdf', '.djvu', '.doc'}
SEGW = 6700

def wc(r):
    try: return int(r['words']) if r['words'] else 0
    except: return 0
def norm(s):
    s = os.path.basename(s or '').lower()
    s = re.sub(r'\.(epub|mobi|azw3|pdf|djvu|doc|txt|md)$', '', s)
    s = re.sub(r'(_extracted|_download|_docx)$', '', s)
    return re.sub(r'[^a-z0-9]', '', s)

rows = list(csv.DictReader(open(MF)))

# chunk coverage: which source_files have chunks, and do chunks carry offsets?
chunk_n = Counter(); chunk_has_offset = False
for f in glob.glob(os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/*CHUNKS*.jsonl")):
    for line in open(f):
        line = line.strip()
        if not line: continue
        try:
            d = json.loads(line)
        except: continue
        sf = norm(d.get('source_file') or d.get('source_title') or '')
        if sf: chunk_n[sf] += 1
        if any(k in d for k in ('start', 'end', 'offset', 'char_start', 'segment')): chunk_has_offset = True

# extracted texts (the real content units, with words)
ext = {norm(r['path']): r for r in rows if '_extracted/' in (r['path'] or '') and (r['ext'] or '').lower() == '.txt'}

# start-here certified twins (coverage proof exists)
cert_twins = set()
shl = os.path.join(ROOT, "OS_STARTHERE_CERT_LEDGER.csv")
if os.path.exists(shl):
    for r in csv.reader(open(shl)):
        if r and ('certified' in (r[4] if len(r) > 4 else '')): cert_twins.add(norm(r[0]))

# segment ledgers present (coverage proof)
seg_ledgers = {norm(d) for d in (os.listdir(os.path.join(ROOT, "_segments")) if os.path.isdir(os.path.join(ROOT, "_segments")) else [])}

books = [r for r in rows if (r['ext'] or '').lower() in BOOK_EXT]
# UNIT OF COVERAGE = the extracted text (has the words; shares slugs with chunks).
ext_rows = [r for r in rows if '_extracted/' in (r['path'] or '') and (r['ext'] or '').lower() == '.txt']
out = []
for r in ext_rows:
    st = norm(r['path']); words = wc(r); segs = math.ceil(words / SEGW) if words else 0
    chunks = chunk_n.get(st, 0)
    has_ledger = st in seg_ledgers; twin_cert = st in cert_twins
    if has_ledger or twin_cert: bucket = 'coverage_proven'
    elif chunks > 0: bucket = 'chunked_not_certified'        # concept-chunks only, NO coverage proof
    else: bucket = 'extracted_only_provisional'              # extracted, not even chunked
    needs_reread = (segs > 2 and bucket != 'coverage_proven')
    out.append({'extracted': os.path.basename(r['path']), 'words': words, 'segments_equiv': segs,
                'chunk_count': chunks, 'has_segment_ledger': 'yes' if has_ledger else 'no',
                'twin_certified': 'yes' if twin_cert else 'no',
                'needs_reread': 'yes' if needs_reread else 'no', 'bucket': bucket})
with open(LEDGER, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

# source-file (format) summary , the 667 epub/pdf/etc
src_status = Counter(b['status'] for b in books)
src_ext = Counter((b['ext'] or '').lower() for b in books)
stem_formats = defaultdict(set)
for b in books: stem_formats[norm(b['path'])].add((b['ext'] or '').lower())
multi_format = sum(1 for k, v in stem_formats.items() if len(v) > 1)

bc = Counter(o['bucket'] for o in out); bv = Counter()
for o in out: bv[o['bucket']] += o['words']
totv = sum(bv.values()) or 1
print("=== SOURCE FILES (formats: epub/pdf/mobi/azw3/djvu) ===")
print(f"  count {len(books)} | by ext {dict(src_ext)}")
print(f"  status {dict(src_status)} | multi-format titles (dedupe): {multi_format}")
print(f"\n=== COVERAGE UNIT = EXTRACTED TEXTS ({len(out)}, {sum(o['words'] for o in out):,} words) ===")
print(f"chunks carry offsets/coverage: {chunk_has_offset}  => chunks are {'PROOF' if chunk_has_offset else 'NOT coverage proof (concept-distillation only)'}")
print(f"extracted texts WITH a segment ledger: {sum(1 for o in out if o['has_segment_ledger']=='yes')}")
print(f"avg chunks per extracted text: {sum(o['chunk_count'] for o in out)/max(1,len(out)):.1f} (concept-chunks)")
print("\nBUCKET                       files    word-volume")
for k in ['coverage_proven', 'chunked_not_certified', 'extracted_only_provisional']:
    print(f"  {k:<28} {bc.get(k,0):>4}   {bv.get(k,0):>12,} ({bv.get(k,0)/totv*100:4.1f}%)")
print(f"  needs_reread (>2 seg, unproven): {sum(1 for o in out if o['needs_reread']=='yes')} files, "
      f"{sum(o['words'] for o in out if o['needs_reread']=='yes'):,} words")
print(f"\nPENDING (source files, not extracted): ocr {src_status.get('needs_ocr',0)} | visual {src_status.get('needs_visual_review',0)} | not_read {src_status.get('not_read',0)} | dup {src_status.get('duplicate',0)}")
print(f"ledger -> {LEDGER}")
