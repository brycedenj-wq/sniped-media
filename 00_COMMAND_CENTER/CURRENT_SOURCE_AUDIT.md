# CURRENT SOURCE AUDIT · raw/ vs official corpus · 2026-05-23

**Purpose:** a read-only audit comparing everything staged in `raw/` against what is already official in the `*_CHUNKS.jsonl` files and `MASTER_CHUNK_MAP.json`. No extraction, chunking, consolidation, or master-file changes were performed.

## 0. Verified locked state

- **Head commit:** `5504be4 save session after EDGE_AND_OPERATING_DISCIPLINE consolidation`
- **Working tree:** clean before this audit.
- **Total official chunks:** 1,311 (header = sum of `.batches[].chunk_count` = sum of jsonl line counts).
- **Canonical sets:** 10 numbered batches + 13 mini-batches · 60 official domains.
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted (`1211da5`). Identity optionality guardrails ACTIVE.

## 1. Methodology + caveat

Matching is **heuristic**: raw filenames are matched against official `source_title` + `author` + `source_file` tokens (the official `source_file` values are normalized extracted names, so author/title token overlap is the signal). A raw book file is counted PROCESSED when its filename shares >=2 distinctive title tokens with an official record, or >=1 title token plus an author-surname match. The named special-attention items were checked individually (exact). Counts for book-format files are precise to within the heuristic's error band; md/docx are classified at category level. Numbers are estimates where noted.

## 2. raw/ inventory

- **Total raw files:** 765
- **Book-format (pdf/epub/mobi/azw3/djvu/lit/cbr):** 302
- **md / docx / txt content:** 379 (mostly SNIPED-authored OS docs, art-series studies, playbooks, operational notes)
- **Other (png/mp4/json/csv/xmp/sh/py/xlsx/zip/pptx/html/ds_store):** 84 (not chunk sources)

**Top raw folders by file count:** 02_TIER_1_CANON_BOOKS (123) · 03_TIER_2_CANON_BOOKS (107) · 10_REFERENCE (74) · 05_PRODUCTION (54) · Claude_AI_Skills_50_Upload_Ready (51) · _skills (51) · 03_OUTREACH (43) · 00_BRIEF (34) · 14_WEB (23) · 09_ART_SERIES (19) · 99_VAULT (17).

**Original master grab list:** there is no separately-labeled "245 list" on disk, but `00_COMMAND_CENTER/DOWNLOADS_INVENTORY_2026-05-18.txt` (2,737 lines) is a full `find` listing of the original `~/Downloads/    SNIPED_OS/` universe. `raw/` is a curated 765-file mirror of that universe (temp files, `.tif`, `.crdownload`, `.DS_Store`, and duplicate scratch copies from the original tree were not all staged).

## 3. Official corpus inventory

- **Batch jsonl files:** 23 · **total chunks:** 1,311
- **Distinct `source_title` (+ BATCH_001 `source`):** 427 · **distinct authors:** 113 · **distinct `source_file`:** 317
- **batch_ids (23):** BATCH_001 (106) · BATCH_002_TIER_1_CANON_BOOKS (152) · BATCH_003_TIER_2_CANON_BOOKS (103) · BATCH_004_SNIPED_OS_DEPTH_FILL (96) · BATCH_005 (161) · BATCH_006 (114) · BATCH_007 (128) · BATCH_008 (120) · BATCH_009 (76) · BATCH_009_EXPANSION (22) · BATCH_010 (45) · INTELLECTUAL_ARTIST_FRAME (7) · PERSONAL_OPERATING_CODE (9) · B2B_POSITIONING_CLAUDE_OPERATOR (8) · OPPORTUNITY_MANAGEMENT_TEMPLATES (4) · N8N_AUTOMATION_SYSTEMS (18) · PROMPT_TEMPLATES_DEEP (12) · LITERARY_CANON_BLACK (28) · LITERARY_CANON_DYSTOPIAN (17) · LITERARY_CANON_GENERAL (32) · CLAUDE_OPERATOR_DOCS (26) · CULTURE_AND_STATUS (16) · EDGE_AND_OPERATING_DISCIPLINE (11).

## 4. Classification by status

### 1. OFFICIAL_PROCESSED
- **~159 of 302 book-format files** matched to official chunks (Tier-1/Tier-2 canon subsets chunked in BATCH_002/003, plus photography BATCH_005, AI/tech BATCH_008, advertising BATCH_009 + EXPANSION, lineage BATCH_010, literary canons, status pair, etc.).
- **The majority of the 379 md/docx/txt content files** were processed in the SNIPED-OS depth batches (BATCH_001, BATCH_004, BATCH_005, BATCH_006, BATCH_007) and the AI-Edge / literary / operator mini-batches (art-series studies, the brief docs, the playbooks, the operator-coded definition, etc.). Category-level estimate; not all individually re-matched.

### 2. STAGED_NOT_PROCESSED (the real backlog)
- **~137 book-format files** not yet chunked, clustered as:
  - **03_TIER_2_CANON_BOOKS: 68** · memoirs_biographies 17, decision_judgment 11, investing_finance 8, leadership_mgmt 8, consulting_service 7, fashion_luxury 7, systems_thinking 5, operator_engine_community 3, expertise_creativity 2.
  - **02_TIER_1_CANON_BOOKS: 28** · strategy_history 8, operating_founder 7, network_distribution 5, advertising 2, photography 2, sales_positioning 2, + Hit Makers + ArtOfWar.
  - **10_REFERENCE: 26** · mostly photography lighting-setup lecture PDFs (image-diagram heavy) + a Cartier-Bresson scan.
  - **raw root: 15** · loose canon (brand books: Watkins, Airey, Ries/Kotler, Wheeler, Meyerson, Neumeier; Company of One; Predictable Revenue; etc.).
- **5 deferred docx** (also HELD, see below): The_Operator_Playbook, GaryVee_Attention_Operating_System, Business_Operations_Playbook, Money_Wealth_Getting_Ahead, sniped_context_tools_only.

### 3. MISSING_NOT_FOUND (named, absent from raw/)
- **Maus II** · **Russian-author mobi** (`Шерман, Алекси` · absent) · **Sugarman** (*Adweek Copywriting Handbook*) · **Caples** (*Tested Advertising Methods*) · **Halbert** (*Boron Letters*).

### 4. BROKEN_OR_NEEDS_REACQUISITION
- **Broken format (no clean text · no OCR):** Maus I (`.cbr`), Predictably Irrational (`.djvu`), The Denial of Death (`.djvu`), The Book of Five Rings (`.djvu`), Creativity / Csikszentmihalyi (`.djvu`), The Mailroom (`.djvu`).
- **Bad content (present but unusable):** Beloved (staged PDF is a stub), Confessions of an Advertising Man (staged copy is a scan).
- All 8 confirmed 0 chunks. Re-acquire clean text editions.

### 5. DUPLICATE_OR_ALREADY_COVERED (intra-raw md5 duplicates)
- **document.pdf** (`10_REFERENCE/_intake_2026-05-18/`) = byte-identical to **This Is Marketing** (already chunked in BATCH_009).
- Same-file-two-locations pairs: **Predictable Revenue** (root + books/), **Cold Email Manifesto** (root + books/), **Hit Makers** (02_TIER_1 + root), **Eggleston's Guide** (02_TIER_1/photography + PHOTOGRPAHY GOLD), **Supreme Models** (culture/ + photography/ · chunked once in BATCH_010), **Short-Lighting** (lighting_pdfs `(1)` copy), **prompt template Self-Criticism/Combining** `-2`/`-3` copies (PROMPT_TEMPLATES_DEEP took one).

### 6. HELD_FOR_FUTURE_LANE
- **memoirs_biographies cluster (17 staged book files)** → the **money / ownership lane** candidate (Branson, Schultz, Vreeland, Coddington, Arnold/Total Recall, etc.).
- **5 deferred docx** assigned: Operator_Playbook + GaryVee → content/distribution lane; Business_Operations_Playbook → business-ops/legal/finance lane; Money_Wealth_Getting_Ahead → money/ownership lane; sniped_context_tools_only → SNIPED-context (likely overlaps the chunked SNIPED OS Knowledge Dump).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY** · plan-only / NOT extracted · held until the operator writes the fresh current SNIPED brief.

### 7. OUT_OF_SCOPE_OR_SALVAGE
- **84 non-content files** (png/mp4/json/csv/xmp/sh/py/xlsx/zip/pptx/html/ds_store) · not chunk sources.
- **2 optional salvage scrapes:** `astro claude websites 3x faster.docx` (`10_REFERENCE/_intake_2026-05-18/`) · `MORE CLAUDE 5.docx` (`99_VAULT/_intake_archive_2026-05-12/`).
- **Operational md/docx** (CRM, contracts, cockpits, session logs, financial/legal placeholders) · not corpus material.

## 5. Headline counts

| Metric | Count |
|---|---:|
| Total raw files | 765 |
| Book-format raw files | 302 |
| Official batch jsonl files | 23 |
| Official chunks confirmed | 1,311 |
| Book-format OFFICIAL_PROCESSED (est.) | ~159 |
| Book-format STAGED_NOT_PROCESSED (est.) | ~137 |
| BROKEN_OR_NEEDS_REACQUISITION | 8 |
| MISSING_NOT_FOUND (named) | 5 |
| md/docx/txt content (mostly processed in OS depth batches) | 379 |
| Other (out-of-scope non-content) | 84 |

## 6. Top completed lanes (by chunk count)

BATCH_005 photography canon (161) · BATCH_002 Tier-1 canon (152) · BATCH_007 operator doctrine (128) · BATCH_008 AI/tech canon (120) · BATCH_006 (114) · BATCH_001 (106) · BATCH_003 Tier-2 canon (103) · BATCH_004 SNIPED-OS depth (96) · BATCH_009 advertising/copywriting (76) · BATCH_010 lineage + Black culture (45) · LITERARY_CANON_GENERAL (32) · LITERARY_CANON_BLACK (28) · CLAUDE_OPERATOR_DOCS (26) · BATCH_009_EXPANSION (22).

## 7. Top remaining lanes (staged clusters)

1. **memoirs_biographies** (Tier-2 · 17) → money/ownership / founder-media lane.
2. **decision_judgment** (Tier-2 · 11) → a decision/judgment canon batch.
3. **strategy_history** (Tier-1 · 8) → Napoleon, Herodotus, Machiavelli, Marcus Aurelius, Caesar, Book of Five Rings (djvu).
4. **investing_finance** (Tier-2 · 8) + **leadership_mgmt** (Tier-2 · 8).
5. **consulting_service** (Tier-2 · 7) + **fashion_luxury** (Tier-2 · 7).
6. **10_REFERENCE lighting_pdfs** (~24 · photography lighting setups · image-diagram heavy · may be low-text).
7. **network_distribution** (Tier-1 · 5 · Kevin Kelly, Chris Anderson) + **operating_founder** (Tier-1 · 7 · Lean Startup, Hard Thing, Traction, Blitzscaling, Founder's Dilemmas, The Goal).

## 8. Top 20 recovery / re-acquisition priorities

1. Predictably Irrational (Ariely) · re-acquire epub/pdf (`.djvu`)
2. The Denial of Death (Becker) · re-acquire (`.djvu`)
3. The Book of Five Rings (Musashi) · re-acquire (`.djvu`)
4. Creativity (Csikszentmihalyi) · re-acquire (`.djvu`)
5. The Mailroom (Rensin) · re-acquire (`.djvu`)
6. Maus I (Spiegelman) · `.cbr` images · re-acquire text or future OCR
7. Beloved (Morrison) · staged PDF is a stub · re-acquire clean text
8. Confessions of an Advertising Man (Ogilvy) · scan · re-acquire text edition
9. Maus II (Spiegelman) · absent · acquire
10. Russian-author mobi (`Шерман, Алекси`) · absent · acquire/confirm
11. Sugarman · *Adweek Copywriting Handbook* · absent · acquire
12. Caples · *Tested Advertising Methods* · absent · acquire
13. Halbert · *The Boron Letters* · absent · acquire
14. Jonathan Livingston Seagull (Bach) · `.djvu` · re-acquire (note: literary lane is otherwise complete)
15. The Prophet (Gibran) · `.lit` present (content reached LITERARY_CANON_GENERAL) · re-acquire clean text only if a gap is found
16-20. (reserve · no further confirmed broken/missing canon items beyond the above)

## 9. Top 20 staged-not-processed priorities (book-format)

1. ArtOfWar.pdf (Sun Tzu · Tier-1 strategy)
2. Napoleon: A Life (Roberts · Tier-1 strategy_history)
3. The Landmark Herodotus (Tier-1 strategy_history)
4. The Prince (Machiavelli · Tier-1 strategy_history)
5. Meditations (Marcus Aurelius · Tier-1 strategy_history)
6. The Lean Startup (Ries · Tier-1 operating_founder)
7. The Hard Thing About Hard Things (Horowitz · Tier-1 operating_founder)
8. Traction (Weinberg/Mares · Tier-1 operating_founder)
9. Blitzscaling (Hoffman/Yeh · Tier-1 operating_founder)
10. The Founder's Dilemmas (Wasserman · Tier-1 operating_founder)
11. The Goal (Goldratt · Tier-1 operating_founder)
12. The Inevitable (Kevin Kelly · Tier-1 network_distribution)
13. The Long Tail (Chris Anderson · Tier-1 network_distribution)
14. Crossing the Chasm (Moore · Tier-1 sales_positioning)
15. The Mom Test (Fitzpatrick · Tier-1 sales_positioning)
16. Zero to One (Thiel · Tier-1 root)
17. Shoe Dog (Knight · Tier-1 root)
18. Steve Jobs (Isaacson · Tier-1 root)
19. The decision_judgment Tier-2 cluster (11 · e.g., Thinking Fast and Slow-adjacent, Becker djvu excluded)
20. The brand-canon loose set at raw root (Watkins, Airey, Ries/Kotler Positioning, Wheeler, Meyerson, Neumeier) → a future brand-canon batch (NOTE: identity-side · keep decision-neutral per optionality guardrails)

## 10. Recommended next 3 moves (operator decision · none started)

1. **Money / ownership lane** · the largest coherent staged cluster (memoirs_biographies 17 + Money_Wealth_Getting_Ahead.docx + relevant founder/wealth Tier-2). Plan per the locked 7-step SOP.
2. **Recovery / re-acquisition pass** · re-acquire clean text editions for the 8 broken + acquire the 5 missing (items 1-13 in section 8), then a small recovery batch.
3. **A strategy/decision canon batch** · Tier-1 strategy_history (8: Napoleon, Herodotus, Machiavelli, Marcus Aurelius, Caesar) + Tier-2 decision_judgment (11) + Tier-1 operating_founder (7) · a high-value classical-strategy + judgment lane.

The fresh current SNIPED brief + the CURRENT_IDENTITY_AND_BRAND_OPTIONALITY principle-only ship remain the identity-side option (held until the operator writes the brief). The brand-canon loose set is available but should stay decision-neutral under the active optionality guardrails.

## Constraints honored by this audit

- Did NOT extract, chunk, consolidate, or modify master files (MASTER_INDEX / MASTER_CHUNK_MAP / ACTIVE_KNOWLEDGE_STATE untouched).
- Did NOT modify any `raw/` source file or any existing batch jsonl.
- Did NOT start the money, recovery, brand, or identity lanes.
- No em-dashes. CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / not extracted.
- Wrote only `00_COMMAND_CENTER/CURRENT_SOURCE_AUDIT.md`. Not committed.
