# BATCH_010 plan · lineage + Black culture canon · 2026-05-22

Plan only. No staging, extraction, chunking, master-file updates, OCR, or commits. This plan defines BATCH_010 so a later authorized extraction session can run the locked SOP (extract → chunk → validate → ship → consolidate → session-save) without re-deriving scope.

**Source universe:** `~/AI-Brain-Refinery/raw/` (already staged). No new staging required.
**Theme:** lineage, Black culture, cultural memory, hip-hop / business autobiography, mythmaking, voice, survival, status, identity, image-making, self-authorship, inheritance, hustle, public persona, and SNIPED's Lineage Doctrine. The primary-source music/culture layer that extends LITERARY_CANON_BLACK's literary foundation.

---

## 0 · Verified starting state (this session)

- Latest commit: `980cb2b save session after BATCH_009 consolidation`
- Total chunks: 1,217 · 9 numbered batches + 10 mini-batches · 60 official domains
- Working tree: clean
- BATCH_010: NOT started (no `BATCH_010_CHUNKS.jsonl`, no `batch_010_extracted/`, no `BATCH_010_COMPLETE.md`)
- **Overlap finding:** BATCH_002 (Tier 1) chunked the strategy/founder titles + two culture/music titles from this lane already · **The Tanning of America (Stoute · 7 chunks)** and **The Song Machine (3 chunks)**. Those are EXCLUDED (already canonical). The 7 books currently in `raw/02_TIER_1_CANON_BOOKS/culture/` are all net-new (verified: 0 chunks each in BATCH_002 and 0 source-refs in the map).

---

## 1 · Candidate source location

All candidates live in one folder: `raw/02_TIER_1_CANON_BOOKS/culture/` (7 books). No dedicated `lineage/` folder exists. The named "Reynolds" (Supreme Models) is cross-listed in both `culture/` and `photography/` (md5-identical · `e298253b...`) · chunk once.

**Out of scope (separate future lane, NOT BATCH_010):** `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` holds ~16 general founder / media biographies (Branson, Schultz ×2, Rockefeller, Walton, Vreeland, Coddington, Musk, Uber, ESPN, SNL, etc.) · these are not Black-culture/lineage primary sources and belong to a future memoir/biography batch.

---

## 2 · Inventory by folder, filename, type, extraction method (with read-only text-density peek)

All 7 are epub · extraction via stdlib zipfile + HTML-strip (proven) or ebook-convert. Word counts below are from a read-only composition peek (image count + approximate extractable words).

| # | Author · Title | Size | Images | Approx words | Method | Verdict |
|--:|---|---:|---:|---:|---|---|
| 1 | Dan Charnas · The Big Payback: The History of the Business of Hip-Hop (2010) | 708 KB | 33 | 255,158 | stdlib zipfile | CORE (richest) |
| 2 | Dan Charnas · Dilla Time: J Dilla (2022) | 32,217 KB | 59 | 161,195 | stdlib zipfile | CORE |
| 3 | Jay-Z · Decoded (2010) | 20,094 KB | 155 | 104,517 | stdlib zipfile | CORE |
| 4 | Gucci Mane · The Autobiography of Gucci Mane (2017) | 4,921 KB | 6 | 79,001 | stdlib zipfile | CORE |
| 5 | Rick Ross · Hurricanes: A Memoir (2019) | 29,744 KB | 46 | 69,393 | stdlib zipfile | CORE |
| 6 | Zack O'Malley Greenburg · Empire State of Mind: How Jay-Z Went from Street Corner to Corner Office (2011) | 315 KB | 42 | 58,450 | stdlib zipfile | CORE |
| 7 | Marcellas Reynolds · Supreme Models: Iconic Black Women Who Revolutionized Fashion (2019) | 120,159 KB | 244 | 31,803 | stdlib zipfile | CORE (LIGHT · image-heavy) |

**Tooling:** stdlib zipfile + HTML-strip (primary) · ebook-convert (fallback). No OCR. No new dependencies.

---

## 3 · Pre-flight source-quality / stub check (read-only · nothing written)

- **No stubs.** All 7 have substantial extractable text (Empire State of Mind 58k is the floor · all others 69k-255k).
- **Supreme Models is image-heavy** (244 images · 31,803 words of profiles/captions) · it is a visual coffee-table book straddling photography canon and Black culture. Workable but LIGHT coverage (the durable signal is the cultural-significance / Black-women-in-fashion / image-making angle, not deep text).
- **The large epub sizes are embedded images, not bloat** · Hurricanes (29 MB), Decoded (20 MB), Dilla Time (32 MB), Supreme Models (120 MB) all extract real prose; size is photo inserts.
- **No already-chunked overlap** · confirmed against BATCH_002 (Tanning of America + Song Machine were its only culture titles · both excluded here) and BATCH_005 (Supreme Models not chunked there despite the photography/ cross-listing).
- **Supreme Models dedupe** · the `culture/` and `photography/` copies are byte-identical (same md5) · chunk the `culture/` copy once.

---

## 4 · Status pair decision (operator question)

**Recommendation: HOLD the Status pair (The Status Game · Storr, and Status and Culture · Marx) for a separate culture/status sub-lane · do NOT include in BATCH_010.**

Rationale: BATCH_010's coherence is Black-culture / hip-hop / lineage **primary sources** (memoir, autobiography, music-business history). The Status pair are **general status-sociology / taste-theory** secondary works · a distinct analytical lane. Folding them in would dilute the primary-source lineage focus, and they pair more naturally with the existing `status` domain (8 chunks · de Botton + Simler/Hanson from BATCH_003) in a future `CULTURE_AND_STATUS` mini-batch. They remain available and flagged. (If the operator prefers, Status and Culture · Marx · could fold in as a light theoretical lens for the image-making / fashion-status theme, but the default is HOLD.)

---

## 5 · Recommended inclusion vs defer / exclude

### 5.1 · INCLUDE (CORE · 7 books)
The Big Payback, Dilla Time, Decoded, The Autobiography of Gucci Mane, Hurricanes, Empire State of Mind, Supreme Models (light).

### 5.2 · HOLD (operator decision · separate future lane)
- The Status Game + Status and Culture → a future `CULTURE_AND_STATUS` mini-batch (or light fold-in · §4).
- `memoirs_biographies/` (~16 general founder/media biographies) → a future memoir/biography batch.

### 5.3 · EXCLUDE
- The Tanning of America (Stoute) + The Song Machine · already chunked in BATCH_002.

### 5.4 · No deferrals for format/stub
All 7 CORE books are clean epubs with real text · no OCR-blocked or format-blocked items in this lane.

---

## 6 · Estimated chunk yield + target range

CORE 7 books, chunked at primary-source depth (the durable cultural/operator signal per book), plus cross-source synthesis.

| Source | Estimate |
|---|---:|
| The Big Payback (Charnas) | ~8 |
| Dilla Time (Charnas) | ~7 |
| Decoded (Jay-Z) | ~6 |
| The Autobiography of Gucci Mane | ~6 |
| Hurricanes (Rick Ross) | ~5 |
| Empire State of Mind (Greenburg) | ~5 |
| Supreme Models (Reynolds · light) | ~3 |
| Cross-source synthesis | ~4-5 |

**Target: ~45-52 chunks. Planning range: 40-58.** Consistent with the documented BATCH_010 estimate (45-65) · slightly conservative because Supreme Models is light and the lane is 7 books (the +20-35 in the documented range assumed a folded-in literary subset, which is already chunked in LITERARY_CANON_BLACK).

---

## 7 · Domain set (existing-where-possible · NO new domain expected)

All from the operator-approved list, all pre-existing:

| Domain | Where it comes from |
|---|---|
| `lineage` (11) | inheritance, self-authorship, where-you-come-from, the Lineage Doctrine grounding (Decoded, Gucci Mane, Hurricanes, Supreme Models) |
| `culture` (30) | cultural memory, hip-hop as cultural force, scene/community (Big Payback, Dilla Time, all memoirs) |
| `aesthetics` (59) | craft, voice, rhythm, image-making, the made object (Dilla Time, Decoded, Supreme Models) |
| `brand` (21) | persona-construction, public image, name-as-asset (Hurricanes, Empire State of Mind, Gucci Mane) |
| `operator-doctrine` (52) | discipline, survival, transformation, work ethic, self-reinvention (Gucci Mane, Dilla Time) |
| `strategy` (141) | ownership, the come-up, business arc, leverage (Empire State of Mind, Big Payback) |
| `systems-thinking` (26) | the institutional dynamics of the music business · gatekeeping, ownership structures, exploitation/leverage (Big Payback) |
| `ethics` (23) | appropriation/exploitation in the industry, authenticity-vs-persona, the cost of the hustle (Big Payback, Hurricanes) |

### NEW-domain flag
**Recommendation: introduce NO new domain.** The eight existing domains fully cover the lineage/Black-culture/hip-hop material. If extraction reveals a genuine gap, halt and report rather than introduce one silently.

---

## 8 · How BATCH_010 connects to the corpus

- **LITERARY_CANON_BLACK:** LCB is the literary foundation of the Lineage Doctrine (Morrison, Hurston, Walker · cultural memory, voice, dignity); BATCH_010 is its music/culture extension (hip-hop autobiography, self-authorship, the come-up). Same `lineage` + `culture` domains, different register · the literary spine plus the popular-culture spine.
- **INTELLECTUAL_ARTIST_FRAME:** the MJ Moonwalk disciplined-artist frame extends directly to Dilla's craft discipline and Jay-Z's self-authorship · the intellectual-artist thread across genres.
- **BATCH_005 photography canon:** Supreme Models (Black women in fashion / image-making) and Decoded's visual self-presentation pair with the photography canon's image-making and representation lanes · cross-reference, do not duplicate (Supreme Models not chunked in B005).
- **BATCH_007 operator doctrine:** Gucci Mane's discipline/transformation and Jay-Z's ownership arc are primary-source backing for the locked operator doctrine (composure, self-reinvention, owning your work).
- **BATCH_009 commercial voice:** the come-up and persona-construction in these memoirs are the lived version of BATCH_009's positioning + brand + persuasion theory · the canon's principles enacted in real cultural careers.
- **SNIPED Lineage Doctrine (auto-memory + the locked doctrine):** this batch is the most direct primary-source grounding for the Lineage Doctrine's "document from inside the lineage" principle · the Black-founder / hip-hop / self-made-image lineages made canonical and chunk-addressable.

---

## 9 · Deliverables (defined here · produced only in the authorized extraction session)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/BATCH_010_CHUNKS.jsonl` |
| Extracted text dir | `01_KNOWLEDGE_BASE/batches/batch_010_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/BATCH_010_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/BATCH_010_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/BATCH_010_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/BATCH_010_COMPLETE.md` |
| Extractor script | `scripts/extract_batch_010.py` |
| Chunk-writer script | `scripts/write_batch_010_chunks.py` |

Schema: the canonical 12-field schema (`chunk_id`, `batch_id`, `source_title`, `source_file`, `author`, `domain`, `concept`, `summary`, `usable_principle`, `sniped_relevance`, `direct_quotes`, `tags`). ID pattern `BATCH_010_NNN`. batch_id `BATCH_010`.

---

## 10 · Validation gates (at the authorized extraction session)
The 6 jsonl-validation checks (parse · 12 fields · chunk_id uniqueness · single batch_id `BATCH_010` · source_file resolution · count) plus: pre-flight stub peek on every source, copyright-safe SHORT quotes only (all in-copyright trade books · memoirs especially · keep quotes to a sentence or two), SNIPED-authored output em-dash clean, no new dependencies, no OCR, no new domain without authorization.

---

## 11 · What this plan does NOT do
- No staging, extraction, chunking, or master-file updates.
- No OCR · no new dependencies.
- No touching recovery/acquisition items (Beloved, Maus I, Jonathan Livingston Seagull, Maus II, Russian-author mobi, Confessions text edition, Sugarman/Caples/Halbert, Predictably Irrational).
- No commits. BATCH_010 not started.

Authorization required before any extraction. Stop here.

---

## 12 · Open operator decisions surfaced
1. **Status pair** · HOLD for a future `CULTURE_AND_STATUS` sub-lane (recommended) or light fold-in of Status and Culture for the fashion/image-status theme? Default: HOLD.
2. **Supreme Models depth** · light (3 chunks · recommended, it is image-heavy) or fuller treatment of the Black-women-in-fashion lineage?
3. **memoirs_biographies/ folder** · spin a future general memoir/biography batch (Branson, Schultz, Rockefeller, Vreeland, Coddington, etc.)? Out of BATCH_010 scope.

---

## 13 · Revision log
- **rev 1 (2026-05-22):** First BATCH_010 plan. 7 net-new CORE books located in `culture/` (Big Payback, Dilla Time, Decoded, Gucci Mane, Hurricanes, Empire State of Mind, Supreme Models). Confirmed BATCH_002 already chunked Tanning of America + Song Machine (excluded). Read-only composition peek: all 7 have real text (58k-255k words); Supreme Models image-heavy (light coverage); large epub sizes are photo inserts. Status pair recommended HOLD for a future culture/status sub-lane. memoirs_biographies/ flagged as a separate future lane. Target ~45-52 chunks (range 40-58). Existing domains only (lineage, culture, aesthetics, brand, operator-doctrine, strategy, systems-thinking, ethics) · no new domain. No extraction, chunking, master updates, or commits performed.
