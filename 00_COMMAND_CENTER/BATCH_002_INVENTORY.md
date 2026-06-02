# BATCH_002_TIER_1_CANON_BOOKS · Inventory

**Source:** `raw/02_TIER_1_CANON_BOOKS/`
**Generated:** 2026-05-15
**Total files:** 20
**Total size:** ~228 MB (dominated by one 184 MB PDF)

This batch supersedes the earlier `BATCH_002_PLAN.md` doctrine-completion scope. The new scope is the Tier-1 founder/strategy/cultural-business canon library.

---

## Tool availability check

| Format | Tool needed | Installed? |
|---|---|---|
| `.epub` | `pandoc` OR `ebook-convert` (Calibre) OR Python `ebooklib`+`beautifulsoup4` | **NO** · need to install |
| `.mobi` | `ebook-convert` (Calibre · mobi is Amazon-proprietary, very few alternatives) | **NO** · need to install Calibre |
| `.pdf` (text) | `pdftotext` (poppler) OR Python `pypdf`/`pymupdf` | **NO** · need to install |
| `.pdf` (scanned / large) | OCR via `tesseract` OR cloud (Azure Doc Intelligence, AWS Textract) | **NO** · case-by-case |
| `.docx` | `textutil` (macOS native) | **YES** |

**Recommendation before extraction:** install via Homebrew in one shot:
```
brew install pandoc poppler calibre
```
- `pandoc` → epub → markdown (cleanest output, structure preserved)
- `poppler` → `pdftotext` for the small Art of War PDF
- `calibre` → `ebook-convert` for the .mobi (Shoe Dog) AND for the massive Munger PDF as fallback

Calibre install is ~600 MB but it is the only reliable .mobi extractor. Acceptable one-time cost.

---

## Full inventory

| # | Filename | Ext | Size | Likely method | Process now? | Notes |
|--:|----------|-----|-----:|---------------|:---:|-------|
| 1 | Andrew Chen · The Cold Start Problem | epub | 4.1 MB | pandoc → md | YES | Founder/network-effects canon |
| 2 | Brad Stone · The Everything Store (Bezos/Amazon) | epub | 1.3 MB | pandoc → md | YES | Amazon operating culture |
| 3 | Charles T. Munger · Poor Charlie's Almanack | pdf | **184.6 MB** | **NEEDS USER DECISION** · likely SCANNED or image-heavy; OCR may be required | **DEFER** | Single file = 81% of batch size. Test text-extract first; if scanned, OCR is a separate workstream. |
| 4 | Colin Bryar + Bill Carr · Working Backwards | epub | 1.0 MB | pandoc → md | YES | Amazon mechanisms, PR/FAQ method |
| 5 | Derek Thompson · Hit Makers | epub | 3.5 MB | **SKIP-DUPLICATE** | NO | **Byte-identical to existing `raw/Derek Thompson - Hit Makers...epub` (md5 `29a7347d955bdb80...`)**. Already synthesized into BATCH_001 via `STRATEGIC_PRINCIPLES.md` Section 2. Drop from active processing; mark canonical = the root-level copy. |
| 6 | Ed Catmull · Creativity, Inc. (Pixar) | epub | 6.0 MB | pandoc → md | YES | Studio creative-leadership canon |
| 7 | Jack Weatherford · Genghis Khan | epub | 0.5 MB | pandoc → md | YES | Strategy / leadership / empire-building |
| 8 | James B. Stewart · DisneyWar | epub | 0.8 MB | pandoc → md | YES | Org politics, Eisner-era Disney |
| 9 | John Seabrook · The Song Machine | epub | 0.6 MB | pandoc → md | YES | Hit factory mechanics, music industry parallels |
| 10 | Peter Thiel · Zero to One | epub | 1.4 MB | pandoc → md | YES | Founder canon, monopoly thinking |
| 11 | Phil Knight · Shoe Dog | **mobi** | 0.8 MB | **ebook-convert (Calibre only)** | YES (after Calibre install) | Founder memoir, Nike origin |
| 12 | Robert Iger · The Ride of a Lifetime | epub | 18.1 MB | pandoc → md | YES | CEO playbook, post-Eisner Disney |
| 13 | Steve Stoute · The Tanning of America | epub | 0.3 MB | pandoc → md | YES | Hip-hop economics + cultural commerce |
| 14 | Walter Isaacson · Steve Jobs | epub | 1.9 MB | pandoc → md | YES | Founder canon |
| 15 | William N. Thorndike · The Outsiders | epub | 0.6 MB | pandoc → md | YES | Capital allocation, 8 unconventional CEOs |
| 16 | `[Alexander the Great 1] Freeman · Alexander the Great` | epub | 1.2 MB | pandoc → md | YES | Strategy / leadership / empire |
| 17 | Robert Greene · The 48 Laws of Power | epub | 0.7 MB | pandoc → md | YES | Power dynamics canon |
| 18 | Robert Greene · The 33 Strategies of War | epub | 1.1 MB | pandoc → md | YES | Strategy canon |
| 19 | `ArtOfWar.pdf` (Sun Tzu) | pdf | 0.4 MB | `pdftotext` (small, almost certainly text) | YES (after poppler install) | Likely public-domain text PDF; quick extract |
| 20 | `mostly Powerhouse-.docx` | docx | 0.2 MB | `textutil -convert txt` (already-available) | YES | Title suggests Iger-adjacent or operator notes; sample first to confirm scope |

---

## Suspicious / flagged

- **Munger 184 MB PDF**: anomalously large for a single book PDF. Two likely explanations: (a) high-resolution image-scan of an illustrated edition (would need OCR), or (b) embedded color illustrations at high DPI on every page (still text-extractable but slow). Recommend a 5-page sample extract first to decide which path before committing to full extraction.
- **`mostly Powerhouse-.docx`**: filename pattern (`mostly Powerhouse-.docx`) is operator-shorthand, not a published book title. Suggests it's BJ's notes or excerpt rather than a canon source. Quick scope-check before treating as canon material.
- **`ArtOfWar.pdf`**: filename lacks the libgen pattern of every other file. Could be a public-domain PDF (PG/archive.org). Almost certainly text-extractable; just verify it isn't a scan.

---

## Within-batch + cross-batch duplicate analysis

- **Within batch:** zero byte-level duplicates.
- **Cross-batch:** 1 duplicate confirmed
  - `Derek Thompson - Hit Makers...epub` (BATCH_002) == `Derek Thompson - Hit Makers...epub` (existing in `raw/` root, was reference for BATCH_001)
  - md5: `29a7347d955bdb80...`
  - **Decision:** SKIP in BATCH_002. Already covered.

---

## Extraction plan summary

**Three workstreams:**

### A · Fast path · 16 books (pandoc + ebook-convert + textutil + pdftotext)
After installing `brew install pandoc poppler calibre`:
- 15 epub → `pandoc -f epub -t markdown` → `batches/batch_002_extracted/{slug}.md`
- 1 mobi (Shoe Dog) → `ebook-convert ... .txt` → same dir
- 1 small PDF (ArtOfWar) → `pdftotext -layout` → same dir
- 1 docx (Powerhouse) → `textutil -convert txt` → same dir
Estimated time: 20-40 min including install.

### B · Decision-gated · Munger PDF (184 MB)
Before committing:
1. Sample 5 pages with `pdftotext` → confirm text-extractable
2. If yes: extract full text, chunk by chapter
3. If no (scanned): OCR is a separate batch (cost decision · tesseract local vs cloud)
**Recommendation:** test-first, then propose path.

### C · Skip
- Hit Makers epub (BATCH_002 copy) — duplicate, already covered.

---

## Recommended order of operations

1. **Confirm tooling install** is acceptable (`brew install pandoc poppler calibre`)
2. **Test-extract Munger PDF first 5 pages** to decide path B
3. **Sample `mostly Powerhouse-.docx`** to verify it belongs in canon-books batch (might belong elsewhere)
4. **Process workstream A in parallel** (independent files, can run via shell loop)
5. **Verify each extracted file is non-empty + sensible** (not garbled, not encrypted)
6. **Generate BATCH_002 chunks** from extracted text following same JSONL schema as BATCH_001
7. **Move outputs to `01_KNOWLEDGE_BASE/batches/batch_002/`** per new workspace structure

Total expected chunks if all 18 processable books extract cleanly: ~120-180 chunks (6-10 per book is a reasonable target for canon distillation, matching BATCH_001's density per source).
