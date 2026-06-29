#!/usr/bin/env python3
"""
build_wave.py - wave-agnostic builder for a book-certification wave (002-E/F/G...).

Deterministic, no model, no spend. For the given wave it:
  1. reads BOOK_CANON_CERTIFICATION_LEDGER.csv -> rows where wave==WAVE and status_v2==DOCTRINE_EXTRACTION_SCHEDULED
  2. extracts each source's full text (pdftotext / ebook-convert), splits into ~45k-word parts
  3. writes per-part .txt under /tmp/<wavetmp>/parts/ and a map JSON (slug->src,parts,units)
  4. groups books into batches (<=5 books and <=10 parts each) and emits one Workflow script per batch
     into <control>/scripts/<wavetmp>-RN.js (durable; launch by absolute scriptPath)

Usage: python3 build_wave.py <WAVE e.g. 002-E> <control_dir_abspath>
Re-run safe: skips extraction for parts already present.
"""
import csv, os, sys, re, json, subprocess, tempfile, math

LEDGER = "/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/BOOK_CANON_CERTIFICATION_LEDGER.csv"
WORDS_PER_PART = 45000
MAX_BOOKS_PER_BATCH = 5
MAX_PARTS_PER_BATCH = 10

def slugify(title, used):
    s = title.lower()
    s = re.sub(r'\.(epub|mobi|azw3|pdf|djvu|doc|txt)$', '', s)
    s = re.sub(r'[^a-z0-9]+', '_', s).strip('_')[:40]
    base = s or "book"
    s = base; i = 1
    while s in used:
        i += 1; s = f"{base}_{i}"
    used.add(s); return s

def extract(src, ext):
    out = tempfile.NamedTemporaryFile(suffix=".txt", delete=False).name
    if ext.lower() == ".pdf":
        subprocess.run(["pdftotext","-enc","UTF-8",src,out], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.run(["ebook-convert",src,out], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    t = open(out, errors="ignore").read(); os.unlink(out); return t

def main():
    wave = sys.argv[1]
    control = sys.argv[2]
    wavetmp = "wave" + wave.lower().replace("-", "")
    tmpdir = f"/tmp/{wavetmp}/parts"
    os.makedirs(tmpdir, exist_ok=True)
    scripts_dir = os.path.join(control, "scripts"); os.makedirs(scripts_dir, exist_ok=True)

    rows = [r for r in csv.DictReader(open(LEDGER))
            if r["wave"].strip() == wave and r["status_v2"].strip() == "DOCTRINE_EXTRACTION_SCHEDULED"]
    print(f"{wave}: {len(rows)} scheduled books")
    used = set(); books = []
    for r in rows:
        title = r["title"].strip(); src = r["path"].strip(); ext = r["ext"].strip().lower()
        if not os.path.exists(src):
            print(f"  MISSING SRC, skip: {title[:50]}"); continue
        slug = slugify(title, used)
        # extract (or reuse if already split)
        existing = sorted([f for f in os.listdir(tmpdir) if f.startswith(slug + "_p")])
        if existing:
            units = []
            for f in existing:
                p = int(re.search(r'_p(\d+)\.txt$', f).group(1))
                fp = os.path.join(tmpdir, f); units.append({"part": p, "file": fp, "words": len(open(fp,errors='ignore').read().split())})
            units.sort(key=lambda u: u["part"])
            books.append({"slug": slug, "title": title, "src": src, "ext": ext, "parts": len(units), "units": units})
            print(f"  reuse {slug} ({len(units)} parts)"); continue
        try:
            txt = extract(src, ext); words = txt.split(); n = max(1, math.ceil(len(words)/WORDS_PER_PART))
            per = math.ceil(len(words)/n); units = []
            for i in range(n):
                chunk = " ".join(words[i*per:(i+1)*per])
                fp = os.path.join(tmpdir, f"{slug}_p{i+1}.txt"); open(fp,"w").write(chunk)
                units.append({"part": i+1, "file": fp, "words": len(chunk.split())})
            books.append({"slug": slug, "title": title, "src": src, "ext": ext, "parts": n, "units": units})
            print(f"  OK {slug:42s} words={len(words):>7} parts={n}")
        except Exception as e:
            print(f"  FAIL {slug}: {type(e).__name__}: {e}")

    # map
    json.dump(books, open(f"/tmp/{wavetmp}_map.json","w"), indent=0)
    json.dump(books, open(os.path.join(control, f"{wavetmp}_map.json"),"w"), indent=1)

    # batch grouping: greedy pack
    batches = []; cur = []; cur_parts = 0
    for b in sorted(books, key=lambda x: x["parts"]):
        if cur and (len(cur) >= MAX_BOOKS_PER_BATCH or cur_parts + b["parts"] > MAX_PARTS_PER_BATCH):
            batches.append(cur); cur = []; cur_parts = 0
        cur.append(b); cur_parts += b["parts"]
    if cur: batches.append(cur)

    # emit one JS per batch
    for idx, batch in enumerate(batches, 1):
        emit_js(wave, wavetmp, idx, batch, scripts_dir)
    plan = [{"batch": f"R{i+1}", "books": len(b), "parts": sum(x["parts"] for x in b),
             "slugs": [x["slug"] for x in b]} for i, b in enumerate(batches)]
    json.dump(plan, open(os.path.join(control, "batch_plan.json"),"w"), indent=1)
    print(f"\n{wave}: {len(books)} books -> {len(batches)} batches. scripts in {scripts_dir}")
    for p in plan: print(f"  {p['batch']}: {p['books']} books, {p['parts']} parts")

def emit_js(wave, wavetmp, idx, batch, scripts_dir):
    name = f"{wavetmp}-R{idx}"
    books_js = json.dumps([{"slug": b["slug"], "title": b["title"], "parts": b["parts"],
                            "units": [{"part": u["part"], "file": u["file"], "words": u["words"]} for u in b["units"]]}
                           for b in batch])
    js = '''export const meta = {
  name: '%(name)s',
  description: 'Wave %(wave)s: whole-read + segment-ledger certify books, extract 5-field doctrine, adversarially verify',
  phases: [
    { title: 'Read', detail: 'one reader per book-part, whole-read, segment ledger + doctrine observations' },
    { title: 'Certify', detail: 'synthesize the 5-field doctrine record per book' },
    { title: 'Verify', detail: 'adversarial verifier spot-checks the record against the real text' },
  ],
}

const BOOKS = %(books)s

const PART = {
  type: 'object', required: ['slug','part','words_seen','coverage_complete','segments','observations'],
  properties: {
    slug:{type:'string'}, part:{type:'integer'}, words_seen:{type:'integer'},
    coverage_complete:{type:'boolean'},
    segments:{type:'array',minItems:2,maxItems:12,items:{type:'object',required:['section','covers','key_claims'],properties:{section:{type:'string'},covers:{type:'string'},key_claims:{type:'array',items:{type:'string'},minItems:1,maxItems:4}}}},
    observations:{type:'array',items:{type:'string'},minItems:2,maxItems:8},
  },
}
const BOOK = {
  type:'object', required:['slug','segment_count','coverage_complete','operating_principles','patterns_to_steal','traps_to_avoid','applies_in_sniped','does_not_apply'],
  properties:{
    slug:{type:'string'}, segment_count:{type:'integer'}, coverage_complete:{type:'boolean'},
    operating_principles:{type:'array',items:{type:'string'},minItems:3,maxItems:7},
    patterns_to_steal:{type:'array',items:{type:'string'},minItems:2,maxItems:6},
    traps_to_avoid:{type:'array',items:{type:'string'},minItems:1,maxItems:5},
    applies_in_sniped:{type:'array',items:{type:'string'},minItems:1,maxItems:5},
    does_not_apply:{type:'array',items:{type:'string'},minItems:1,maxItems:4},
  },
}
const VERDICT = {
  type:'object', required:['slug','coverage_verdict','pass','evidence'],
  properties:{slug:{type:'string'},coverage_verdict:{type:'string',enum:['whole-read','partial','sampled']},pass:{type:'boolean'},evidence:{type:'string'},issues:{type:'array',items:{type:'string'}}},
}

const out = await pipeline(
  BOOKS,
  async (book) => {
    const parts = await parallel(book.units.map((u) => () => agent(
      `Certify a part of a book for the SNIPED OS by WHOLE-READING it. NEVER SAMPLE. This is part ${u.part} of ${book.parts} of "${book.title}".\\n` +
      `File: ${u.file} (about ${u.words} words). Read the ENTIRE file start to finish, paging with the Read tool offset/limit until EOF. Do not skim or summarize from prior knowledge.\\n` +
      `Emit a segment ledger for THIS part (sections with key_claims from the actual text) and 2-8 observations (operating principles, patterns to steal, traps). coverage_complete=true only if you read the whole part.`,
      { label: `read:${book.slug}#${u.part}`, phase: 'Read', schema: PART, model: 'sonnet' }
    )))
    return { book, parts: parts.filter(Boolean) }
  },
  async ({ book, parts }) => {
    const rec = await agent(
      `Synthesize the SNIPED doctrine record for "${book.title}" from its whole-read part ledgers (read in full across ${book.parts} part(s); do not re-read).\\n` +
      `Part ledgers:\\n${JSON.stringify(parts)}\\n\\n` +
      `Produce the 5-field record: operating_principles, patterns_to_steal (concrete moves to lift into SNIPED), traps_to_avoid, applies_in_sniped (specific skills/lanes/decisions), does_not_apply (where it misleads or does not fit a solo AI-augmented creative studio). segment_count = total across parts.`,
      { label: `certify:${book.slug}`, phase: 'Certify', schema: BOOK, model: 'sonnet' }
    )
    return { book, parts, rec }
  },
  async ({ book, parts, rec }) => {
    const files = book.units.map((u) => u.file).join(' , ')
    const v = await agent(
      `Adversarial verifier. Do not trust the readers. Confirm "${book.title}" was genuinely WHOLE-READ across all ${book.parts} part(s), not sampled.\\n` +
      `Part files to spot-check: ${files}\\n` +
      `Doctrine record:\\n${JSON.stringify(rec)}\\n\\n` +
      `Open 2-3 of the part files, read different regions (start/middle/end). Confirm claims appear in the text, the parts span the whole book, and the atoms are grounded not generic. If any part looks unread or atoms are vague, verdict=sampled/partial. pass=true only for a grounded whole-read.`,
      { label: `verify:${book.slug}`, phase: 'Verify', schema: VERDICT, model: 'sonnet' }
    )
    return { slug: book.slug, title: book.title, rec, verdict: v }
  }
)

const clean = out.filter(Boolean)
const passed = clean.filter((r) => r.verdict && r.verdict.pass && r.verdict.coverage_verdict === 'whole-read')
const failed = clean.filter((r) => !(r.verdict && r.verdict.pass && r.verdict.coverage_verdict === 'whole-read'))
log(`%(wave)s %(name)s certified+verified: ${passed.length}/${BOOKS.length}; needs-rework: ${failed.length}`)
return {
  passed: passed.map((r) => ({ slug: r.slug, title: r.title, verdict: r.verdict.coverage_verdict })),
  failed: failed.map((r) => ({ slug: r.slug, title: r.title, verdict: r.verdict && r.verdict.coverage_verdict, issues: r.verdict && r.verdict.issues })),
  records: clean.map((r) => ({ slug: r.slug, title: r.title, rec: r.rec, verdict: r.verdict })),
}
''' % {"name": name, "wave": wave, "books": books_js}
    open(os.path.join(scripts_dir, name + ".js"), "w").write(js)

if __name__ == "__main__":
    main()
