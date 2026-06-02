# ORIGINAL SOURCE COMPLETION AUDIT · original universe vs current corpus · 2026-05-24

**Purpose:** a read-only completion audit against the original source universe (the `~/Downloads/    SNIPED_OS/` grab captured in `DOWNLOADS_INVENTORY_2026-05-18.txt`) and the curated `raw/` mirror, so BJ knows exactly what remains and nothing is forgotten. **No extraction, chunking, consolidation, master-file change, or raw mutation was performed. The Bible was not touched.**

## 0. Current corpus state (verified live)

- **Head commit:** `05e67ca save session after PERSUASION_RECOVERY consolidation`
- **Working tree:** clean before this audit.
- **Total official chunks:** 1,501 (reconciled three ways · header = sum of `.batches[].chunk_count` = sum of all `*_CHUNKS.jsonl` line counts = 1,501).
- **Canonical sets:** 10 numbered batches + 23 mini-batches · 62 official domains (75 combined keys).
- **Complete + canonical recovery/expansion lanes:** PERSUASION_RECOVERY, ADVERTISING_RECOVERY, MEDIA_BUSINESS_RECOVERY, HIGH_LEVEL_CONVOS, DEEP_FINANCE_EXPANSION (plus MONEY_OWNERSHIP, BIOGRAPHY_FOUNDER_MEDIA, MEDIA_BUSINESS, FOUNDER_SECOND_TIER, ONWARD_TURNAROUND).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.

## 1. Methodology + uncertainty (read this before trusting any number)

Matching is **heuristic** and the gap numbers are **deliberately conservative-looking but inflated**:

- The original universe is a `find` listing (2,737 lines), not a clean title list. It contains **alternate-format twins** (the same book as both `.epub` and `.pdf`), **in-grab duplicate copies** (`... copy.docx`, `(1)`, `-2`), photography/reference PDFs, scratch files, and OS junk.
- `raw/` is a **curated mirror**: when a book was staged it was often kept in only one format, sometimes renamed (notably the `_RECOVERED` suffix), and the messy duplicates/scans were not all carried over.
- Official `source_file` values are **normalized extracted names** (e.g., `predictably_irrational_ariely.txt`), so "is this book chunked?" is judged by author + title token overlap, not by filename equality.

**Consequence:** an exact-basename diff between the original inventory and `raw/` **overcounts** what is missing (format twins and renames look "missing" though the content is staged or already chunked). Book-format counts are precise to within the heuristic's error band; md/docx are classified at the category level. Numbers below are estimates where marked. **When in doubt, the per-item named checks (sections 7-10) are exact and authoritative; the aggregate percentages (section 13) are directional.**

## 2. Original source universe inventory (DOWNLOADS_INVENTORY_2026-05-18.txt)

- **Total inventory lines:** 2,737 (full recursive `find` of `~/Downloads/    SNIPED_OS/`).
- **Book-format entries (pdf/epub/mobi/azw3/djvu):** 595 lines · **555 distinct basenames** (so ~40 in-grab duplicate copies).
- **By extension (original):** pdf 371 · epub 182 · mobi 28 · azw3 9 · djvu 5 (cbr/cbz/lit 0 in the original inventory; `.cbr`/`.lit` entered later in `raw/`).
- **Non-book content in the original grab:** docx 563 · md 84 · plus large media volumes (jpg 394 · png 257 · heic 162 · dng 150 · tif 88 · jpeg 75 · mp4 73) and operational files (xlsx 51 · zip 45 · csv 40). The media files are photography assets, not corpus sources.

**Reading:** the original grab was a large, messy ~555-distinct-book pile (with format twins and dup copies) plus a heavy photography-asset and operational-doc layer. `raw/` is the curated working subset of it.

## 3. Current raw/ inventory (live)

- **Total files:** 769 (777 including 8 `.DS_Store`).
- **Book-format (pdf/epub/mobi/azw3/djvu/cbr/lit):** **313 files · 310 distinct basenames.**
- **By extension:** md 285 · pdf 143 · epub 131 · docx 93 · png 37 · mobi 22 · azw3 9 · mp4 8 · json 8 · xmp 7 · djvu 6 · csv 5 · sh 3 · zip 2 · xlsx 2 · txt 2 · py 2 · pptx 1 · lit 1 · html 1 · cbr 1.

**Book-format by cluster (top):** memoirs_biographies 27 · 10_REFERENCE/lighting_pdfs 26 · raw root (loose canon) 22 · 02_TIER_1 root 19 · sales_positioning 16 · investing_finance 15 · strategy_history 14 · photography 14 · decision_judgment 13 · operating_founder 12 · ai_tech 12 · advertising 10 · persuasion_psych 9 · leadership_mgmt 9 · literary_canon_general 9 · fashion_luxury 8 · consulting_service 7 · culture 7 · expertise_creativity 6 · systems_thinking 5 · network_distribution 5.

**All files by top-level raw folder:** 02_TIER_1_CANON_BOOKS 127 · 03_TIER_2_CANON_BOOKS 113 · 10_REFERENCE 74 · 05_PRODUCTION 54 · _skills 51 · Claude_AI_Skills_50_Upload_Ready 50 · 03_OUTREACH 43 · 00_BRIEF 34 · 14_WEB 21 · 09_ART_SERIES 19 · 99_VAULT 17 · PHOTOGRPAHY GOLD 15 · 06_DELIVERY 11 · 07_CONTENT 8 · (plus loose root docx/md and small folders).

## 4. Official corpus inventory (live)

- **`*_CHUNKS.jsonl` files:** 33 · **total chunks:** 1,501.
- **Distinct `source_title`/`source`:** 472 · **distinct authors:** 156 · **distinct `source_file`:** 355.
- **batch_ids (33):** BATCH_001 (106) · BATCH_002 (152) · BATCH_003 (103) · BATCH_004 (96) · BATCH_005 (161) · BATCH_006 (114) · BATCH_007 (128) · BATCH_008 (120) · BATCH_009 (76) · BATCH_009_EXPANSION (22) · BATCH_010 (45) · INTELLECTUAL_ARTIST_FRAME (7) · PERSONAL_OPERATING_CODE (9) · B2B_POSITIONING_CLAUDE_OPERATOR (8) · OPPORTUNITY_MANAGEMENT_TEMPLATES (4) · N8N_AUTOMATION_SYSTEMS (18) · PROMPT_TEMPLATES_DEEP (12) · LITERARY_CANON_BLACK (28) · LITERARY_CANON_DYSTOPIAN (17) · LITERARY_CANON_GENERAL (32) · CLAUDE_OPERATOR_DOCS (26) · CULTURE_AND_STATUS (16) · EDGE_AND_OPERATING_DISCIPLINE (11) · MONEY_OWNERSHIP (21) · BIOGRAPHY_FOUNDER_MEDIA (22) · MEDIA_BUSINESS (17) · FOUNDER_SECOND_TIER (20) · ONWARD_TURNAROUND (12) · DEEP_FINANCE_EXPANSION (27) · HIGH_LEVEL_CONVOS (25) · ADVERTISING_RECOVERY (16) · MEDIA_BUSINESS_RECOVERY (15) · PERSUASION_RECOVERY (15).

## 5. Original universe vs current raw/ (set comparison · heuristic)

| Comparison (distinct book basenames) | Count |
|---|---:|
| Original universe distinct book basenames | 555 |
| Current raw/ distinct book basenames | 310 |
| Exact-basename intersection (in both) | 240 |
| Exact-basename only-in-original (apparent gap) | 315 |

**The 315 is NOT a "forgotten" list.** Inspection shows it is dominated by:
1. **Alternate-format twins** of staged titles (e.g., How to Get Dressed epub+pdf, Building a StoryBrand epub+pdf, Start With Why mobi+pdf, Good Strategy Bad Strategy two editions, Dale Carnegie mobi+pdf) · the content is staged in one format.
2. **Titles already chunked under a normalized name / different path** (e.g., Never Split the Difference → BATCH_009_EXPANSION; Supreme Models → BATCH_010; The Mom Test, Thinking Fast and Slow, The Creative Act, War of Art, Superforecasting · several of these are in the canon or staged elsewhere).
3. **A genuine unstaged tail** (see 6/7) · a real but modest set, notably a **fashion/styling sub-cluster** (Dressing the Man, The Chiffon Trenches, The little dictionary of fashion, The curated closet, Outfit Formulas, How to Get Dressed) and assorted business/strategy paperbacks (Good Strategy Bad Strategy, The Personal MBA, Start With Why, Basic Economics, Secrets of Sand Hill Road, That Will Never Work, Toyota Way, Signal and the Noise).

Treat the curated **raw/ (313 files · 310 distinct books)** as the working corpus; the processed/staged/broken breakdown below is the reliable view.

## 6. Headline estimates (heuristic · book-format)

| Metric | Count / estimate |
|---|---:|
| Original universe book-format entries | 595 (555 distinct) |
| Current raw/ book-format files | 313 (310 distinct) |
| Book-format OFFICIAL_PROCESSED (est.) | ~193 |
| Book-format STAGED_NOT_PROCESSED clean (est.) | ~107 |
| Broken / unsupported still in raw/ (est.) | ~12 |
| Known skip (image-only / unidentified) | 3-4 |
| Unknown / unclassified | low · ~5-10 (heuristic residue, mostly format twins) |

The ~193 processed carries forward the 2026-05-23 audit (~159 at 1,311 chunks) + the 2026-05-24 refresh (~190 at 1,471) + the 3 book-format sources chunked since the refresh (MEDIA_BUSINESS_RECOVERY: Hit Men + The Mailroom; PERSUASION_RECOVERY: Predictably Irrational). md/docx content (mostly SNIPED-authored OS docs, art-series studies, playbooks) was largely processed in the SNIPED-OS depth batches (BATCH_001/004/005/006/007) and the AI-Edge / literary / operator mini-batches.

## 7. Remaining KNOWN CLEAN / unprocessed sources (exact · authoritative)

These are present in `raw/`, text-clean, and NOT yet chunked · the real remaining work:

| Source | Author | Path | Format | Lane |
|---|---|---|---|---|
| Grace: A Memoir | Grace Coddington | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/...Grace_ A Memoir...libgen.li_RECOVERED.epub` | epub (recovered) | founder/fashion recovery |
| Total Recall | Arnold Schwarzenegger | `.../memoirs_biographies/Schwarzenegger, Arnold - Total Recall...libgen.li_RECOVERED.epub` | epub (recovered) | founder/fashion recovery (optional) |
| Beloved | Toni Morrison | `raw/02_TIER_1_CANON_BOOKS/literary_canon_black/Toni Morrison - Beloved...libgen.li_RECOVERED.azw3` | azw3 (recovered) | literary recovery |
| Jonathan Livingston Seagull | Richard Bach | `raw/02_TIER_1_CANON_BOOKS/literary_canon_general/ Bach, Richard - Jonathan Livingston Seagull (2010...)...libgen.li_RECOVERED.epub` | epub (recovered) | literary recovery (optional · lane complete) |
| Grant | Ron Chernow | `.../memoirs_biographies/Ron Chernow - Grant (2017, Penguin Publishing Group) - libgen.li.epub` | epub | historical-biography lane |
| Washington: A Life | Ron Chernow | `.../memoirs_biographies/Ron Chernow - Washington_ A Life - libgen.li.pdf` | pdf | historical-biography lane |

**Other clean staged-not-processed clusters identified by the audit (the larger canon backlog, all text-clean, NOT recovery):**
- **Tier-1 strategy_history (~8):** ArtOfWar, Napoleon: A Life (Roberts), The Landmark Herodotus, The Prince (Machiavelli), Meditations (Marcus Aurelius), Caesar · (The Book of Five Rings is djvu · broken, see 8).
- **Tier-1 operating_founder (~7):** The Lean Startup, The Hard Thing About Hard Things, Traction, Blitzscaling, The Founder's Dilemmas, The Goal.
- **Tier-1 network_distribution (~5):** The Inevitable, The Long Tail (Kevin Kelly, Chris Anderson).
- **Tier-1 sales_positioning (~16) + raw-root loose canon (~22):** Crossing the Chasm, The Mom Test, Zero to One, Shoe Dog, Steve Jobs, the brand-canon set (Watkins, Airey, Ries/Kotler Positioning, Wheeler, Meyerson, Neumeier · identity-side · keep decision-neutral under optionality guardrails).
- **Tier-2 decision_judgment (~13), leadership_mgmt (~9), consulting_service (~7), fashion_luxury (~8), systems_thinking (~5), expertise_creativity (~6).**
- **10_REFERENCE/lighting_pdfs (~26):** photography lighting-setup PDFs · image-diagram heavy · likely low extractable text · low priority.

## 8. Still-broken / re-acquire (exact · authoritative)

| Item | Author | Status | Where |
|---|---|---|---|
| Tested Advertising Methods | John Caples | scanned/image-only · **NOT in raw/** (re-download was never staged) | source universe only · re-acquire clean epub |
| The Book of Five Rings | Miyamoto Musashi | `.djvu` (unsupported · no djvutxt) · 0 text | `raw/02_TIER_1_CANON_BOOKS/strategy_history/...djvu` |
| The Denial of Death | Ernest Becker | `.djvu` (unsupported) · 0 text | `raw/.../...djvu` |
| Creativity (Flow and the Psychology of Discovery) | Mihaly Csikszentmihalyi | `.djvu` (unsupported) · 0 text | `raw/.../...djvu` |

**Superseded old originals still in raw/ (already replaced by a recovered file · 0 action needed, optional cleanup):** old Predictably Irrational `.djvu` (replaced by `_RECOVERED.epub`, processed in PERSUASION_RECOVERY), old The Mailroom `.djvu` (replaced by `_RECOVERED.epub`, processed in MEDIA_BUSINESS_RECOVERY), old Jonathan Livingston Seagull `.djvu` (replaced by `_RECOVERED.epub`, staged). These can be deleted in a future authorized cleanup pass; they contribute 0 and are harmless.

## 9. Skip (image-only / unidentified / low-value)

| Item | Reason |
|---|---|
| Maus I (`Maus I.cbr` in raw/ + image-only epub in source universe) | image-only graphic novel · not text-corpus material |
| Maus II (absent from raw/ · image-only epub in source universe) | image-only graphic novel · not text-corpus material |
| Russian-author mobi (`Шерман, Алекси ... libgen.li.mobi`) | present-but-unidentified in the source universe · NOT in raw/ · hold until BJ confirms title + relevance |

## 10. Duplicate ledger (if found)

- **In-grab duplicates in the original universe (~40 basenames appear 2+ times):** Grace: A Memoir (x4), Cold Email Manifesto (x3), Combo Prospecting (x3), Gap Selling (x3), Predictable Revenue (x3), plus ~2x copies of Unreasonable Hospitality, The Brand Gap, Elephant in the Brain, Revenge of Analog, Brand Naming, Almanack of Naval, Trading Up, Perennial Seller, Blockbusters, Building a StoryBrand, Hit Makers, The Trusted Advisor, and others. These were de-duplicated when curated into `raw/`.
- **Known intra-raw / already-covered duplicate (from prior audit · still valid):** `document.pdf` (10_REFERENCE/_intake_2026-05-18/) is byte-identical to This Is Marketing (already chunked in BATCH_009). A handful of same-file-two-locations pairs (Predictable Revenue, Cold Email Manifesto, Hit Makers, Eggleston's Guide, Supreme Models) were each chunked at most once.

## 11. Bible status

**The KJV Bible (`The-Holy-Bible-King-James-Version.pdf`) remains OUTSIDE `raw/`, UNCHUNKED, and held as a reverent SPIRITUAL_FOUNDATION anchor/reference in the source universe** per NEW_SOURCE_INTAKE_PLAN. Confirmed: not in `raw/`, not in any `*_CHUNKS.jsonl`. No faith/spiritual lane exists or was created.

## 12. Identity optionality status

ACTIVE and unchanged. No lane finalizes SNIPED / SNIPED Media / BASEPLATE direction. CURRENT_OPERATOR_REALITY_BRIEF is the read-first current-state anchor (NOT chunked); **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted** (`1211da5`), held until the operator writes the fresh current SNIPED brief. The capital/finance, founder-arc, media-business, advertising, and persuasion lanes are all decision-support / pattern-library lenses, not directives. Photography remains one option among several.

## 13. Percent-complete estimate (three ways · directional, per the section-1 caveat)

1. **All raw/ book-format files:** ~193 processed of 313 ≈ **~62%**. (The denominator includes ~26 low-text lighting PDFs and ~12 broken/superseded files; if those are excluded the rate rises · see #2.)
2. **Useful / high-value curated corpus** (exclude ~26 image-diagram lighting PDFs, ~12 broken/superseded, ~3-4 skip · denominator ~270): ~193 of ~270 ≈ **~70-72%**. This is the most meaningful number · roughly 75-80 high-value text books remain (the strategy/decision/operating-founder/brand/fashion clusters + the 6 named recovery/biography sources).
3. **Recovery cleanup:** of the 15 tracked recovery items, **11 were re-acquired clean** and **7 are processed** (Confessions, Sugarman, Halbert, Margin of Safety, Hit Men, The Mailroom, Predictably Irrational); **4 clean staged remain** (Grace, Total Recall, Beloved, Seagull); **4 are still-broken/skip** (Caples scanned, Maus I/II image-only, Russian-author unidentified). Re-acquisition ≈ **~73% done** (11/15); recovery-processing ≈ **~64% done** (7/11 usable).

## 14. Recommended final sequence to reach "books/docs complete"

A practical ordering (operator decision · none started · plan each per the locked 7-step SOP):

1. **Founder/fashion recovery mini-batch** · Grace + Total Recall (clean, staged, BIOGRAPHY_FOUNDER_MEDIA family). Clears 2 of the 4 remaining clean recovery sources.
2. **Literary recovery mini-batch** · Beloved + Jonathan Livingston Seagull (clean, staged · LITERARY_CANON_BLACK / _GENERAL). Clears the last 2 recovery sources · the recovery program then reads "complete except the 4 still-broken/skip."
3. **Historical-biography lane** · Grant + Washington (Chernow · clean, staged). Closes the deferred Chernow histories (Titan already chunked in FOUNDER_SECOND_TIER).
4. **Classical strategy / decision / operating-founder canon lane(s)** · the largest remaining high-value text backlog: Tier-1 strategy_history (Napoleon, Herodotus, Machiavelli, Marcus Aurelius, Caesar, ArtOfWar) + Tier-1 operating_founder (Lean Startup, Hard Thing, Traction, Blitzscaling, Founder's Dilemmas, The Goal) + Tier-2 decision_judgment. Split into coherent mini-batches.
5. **Remaining Tier-2 clusters** · leadership_mgmt, consulting_service, fashion_luxury, systems_thinking, expertise_creativity, network_distribution, sales_positioning + the raw-root brand-canon set (keep brand-canon decision-neutral under optionality guardrails).
6. **Re-acquisition pass** · get clean epub/text for Caples, The Book of Five Rings, The Denial of Death, Creativity (Csikszentmihalyi); confirm/identify the Russian-author mobi; then a small recovery batch.
7. **Final cleanup / skip ledger** · delete the 3 superseded old djvu originals (optional, authorized cleanup); formally mark Maus I/II and the Russian-author mobi as permanent skips; note the lighting_pdfs as low-text / low-priority.
8. **Identity-side (separate track, when BJ is ready):** the fresh current SNIPED brief + the held CURRENT_IDENTITY_AND_BRAND_OPTIONALITY principle-only ship. Independent of the books-complete sequence.

After steps 1-3 the recovery program is functionally closed; after steps 4-5 the high-value text corpus is essentially complete (>90%); steps 6-7 are cleanup.

## 15. Constraints honored by this audit

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,501.
- Did NOT modify any `raw/` or source file (read-only `find` / `wc` / `grep` / `ls` / inventory parsing only).
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- No new domain. No next lane started.
- Wrote only this report. Em-dash clean. Not committed (operator will review first).
