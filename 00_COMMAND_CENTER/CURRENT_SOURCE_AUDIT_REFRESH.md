# CURRENT SOURCE AUDIT REFRESH · raw/ vs official corpus · 2026-05-24

**Purpose:** a read-only refresh of CURRENT_SOURCE_AUDIT.md (2026-05-23) after the MONEY_OWNERSHIP, BIOGRAPHY_FOUNDER_MEDIA, MEDIA_BUSINESS, FOUNDER_SECOND_TIER, ONWARD_TURNAROUND, DEEP_FINANCE_EXPANSION, HIGH_LEVEL_CONVOS, ADVERTISING_RECOVERY lanes and the recovery/re-acquisition + staging passes. No extraction, chunking, consolidation, master-file change, or raw mutation was performed. The Bible was not touched.

## 0. Verified locked state

- **Head commit:** `1f938a8 save session after ADVERTISING_RECOVERY consolidation`
- **Working tree:** clean before this audit.
- **Total official chunks:** 1,471 (reconciled three ways · header = sum of `.batches[].chunk_count` = sum of jsonl line counts).
- **Canonical sets:** 10 numbered batches + 21 mini-batches · 62 official domains (75 combined keys).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.

## 1. Headline counts (refresh vs the 2026-05-23 audit)

| Metric | 2026-05-23 audit | Now (2026-05-24) | Delta |
|---|---:|---:|---:|
| Total official chunks | 1,311 | 1,471 | +160 |
| Official batch jsonl files | 23 | 31 | +8 |
| Total raw files | 765 | 777 | +12 |
| Book-format raw files | 302 | 313 | +11 |
| Numbered batches + mini-batches | 10 + 13 | 10 + 21 | +8 mini |
| Official domains | 60 | 62 | +2 (`capital`, `media-business`) |

The +160 chunks and +8 mini-batches came from: MONEY_OWNERSHIP (21), BIOGRAPHY_FOUNDER_MEDIA (22), MEDIA_BUSINESS (17), FOUNDER_SECOND_TIER (20), ONWARD_TURNAROUND (12), DEEP_FINANCE_EXPANSION (27), HIGH_LEVEL_CONVOS (25), ADVERTISING_RECOVERY (16). The +12 raw files and +11 book-format are the 11 `_RECOVERED` books + `high_level_convos.docx` staged this run.

## 2. raw/ inventory

- **Total raw files:** 777
- **Book-format (pdf/epub/mobi/azw3/djvu/cbr/lit):** 313
- **By extension (top):** md 285 · pdf 143 · epub 131 · docx 93 · png 37 · mobi 22 · azw3 9 · ds_store 8 · mp4 8 · json 8 · xmp 7 · djvu 6 · csv 5 · cbr 1 · lit 1 · txt 2 · others (sh/py/zip/xlsx/pptx/html) ~11.
- **`_RECOVERED` book files staged:** 11 (the recovery intake · in advertising/, persuasion_psych/, memoirs_biographies/, investing_finance/, literary_canon_black/, literary_canon_general/).

## 3. Official corpus inventory

- **Batch jsonl files:** 31 · **total chunks:** 1,471.
- **batch_ids (31):** BATCH_001-010 (10) + 21 mini-batches (INTELLECTUAL_ARTIST_FRAME, PERSONAL_OPERATING_CODE, B2B_POSITIONING_CLAUDE_OPERATOR, OPPORTUNITY_MANAGEMENT_TEMPLATES, N8N_AUTOMATION_SYSTEMS, PROMPT_TEMPLATES_DEEP, LITERARY_CANON_BLACK, LITERARY_CANON_DYSTOPIAN, LITERARY_CANON_GENERAL, CLAUDE_OPERATOR_DOCS, CULTURE_AND_STATUS, BATCH_009_EXPANSION, EDGE_AND_OPERATING_DISCIPLINE, MONEY_OWNERSHIP, BIOGRAPHY_FOUNDER_MEDIA, MEDIA_BUSINESS, FOUNDER_SECOND_TIER, ONWARD_TURNAROUND, DEEP_FINANCE_EXPANSION, HIGH_LEVEL_CONVOS, ADVERTISING_RECOVERY).

## 4. Chunk reconciliation

**Confirmed 1,471 three ways:** header `total_chunks` = sum of `.batches[].chunk_count` = sum of all `*_CHUNKS.jsonl` line counts = 1,471.

## 5. Processed vs staged-not-processed (book-format · heuristic estimate)

Same heuristic caveat as the original audit (filename/title-token matching · precise to within an error band).

- **Book-format OFFICIAL_PROCESSED (est.):** ~190 (the original ~159 + ~33 book-format sources chunked across the eight new lanes: ~5 MONEY_OWNERSHIP + 6 BIOGRAPHY_FOUNDER_MEDIA + 3 MEDIA_BUSINESS + 7 FOUNDER_SECOND_TIER + 1 ONWARD + 8 DEEP_FINANCE + 3 ADVERTISING_RECOVERY · HIGH_LEVEL_CONVOS was a docx, not book-format).
- **Book-format STAGED_NOT_PROCESSED (est.):** ~110 (the canon backlog: Tier-1 strategy_history [Napoleon, Herodotus, Machiavelli, Marcus Aurelius, Caesar, On War, Alexander-logistics], operating_founder [Lean Startup, Hard Thing, Traction, Blitzscaling, Founder's Dilemmas, The Goal], network_distribution, sales_positioning, Zero to One / Shoe Dog / Steve Jobs / The Elephant in the Brain / The Network State at root; Tier-2 decision_judgment, leadership_mgmt, consulting_service, fashion_luxury, systems_thinking; 10_REFERENCE lighting PDFs; the brand-canon loose set) PLUS the 7 newly-staged recovered books not yet chunked (see section 6).
- **BROKEN / SKIP / MISSING:** see section 6 (Caples scanned · Maus I/II image-only · old superseded scans/stubs · Russian-author present-but-unidentified).

## 6. Recovery status table (the 15 known recovery items · re-classified)

| Item (author) | Status now | Where | Notes |
|---|---|---|---|
| Confessions of an Advertising Man (Ogilvy) | **recovered_and_processed** | raw/advertising/ `_RECOVERED.pdf` | chunked in ADVERTISING_RECOVERY (6) |
| The Adweek Copywriting Handbook (Sugarman) | **recovered_and_processed** | raw/advertising/ `_RECOVERED.azw3` | chunked in ADVERTISING_RECOVERY (5) |
| The Boron Letters (Halbert) | **recovered_and_processed** | raw/advertising/ `_RECOVERED.epub` | chunked in ADVERTISING_RECOVERY (4) |
| Margin of Safety (Klarman) | **recovered_and_processed** | raw/investing_finance/ `_RECOVERED.epub` | chunked in DEEP_FINANCE_EXPANSION (4) |
| Hit Men (Dannen) | **recovered_staged_not_processed** | raw/memoirs_biographies/ `_RECOVERED.azw3` | media-business recovery lane |
| The Mailroom (Rensin) | **recovered_staged_not_processed** | raw/memoirs_biographies/ `_RECOVERED.epub` | media-business recovery lane |
| Predictably Irrational (Ariely) | **recovered_staged_not_processed** | raw/persuasion_psych/ `_RECOVERED.epub` | persuasion recovery lane |
| Grace: A Memoir (Coddington) | **recovered_staged_not_processed** | raw/memoirs_biographies/ `_RECOVERED.epub` | founder/fashion recovery lane |
| Total Recall (Schwarzenegger) | **recovered_staged_not_processed** | raw/memoirs_biographies/ `_RECOVERED.epub` | founder/fashion recovery lane (optional) |
| Beloved (Morrison) | **recovered_staged_not_processed** | raw/literary_canon_black/ `_RECOVERED.azw3` | literary recovery lane |
| Jonathan Livingston Seagull (Bach) | **recovered_staged_not_processed** | raw/literary_canon_general/ `_RECOVERED.epub` | literary recovery lane (optional) |
| Tested Advertising Methods (Caples) | **still_broken** | source universe (scanned pdf · NOT staged) | re-acquire a clean epub |
| Maus I (Spiegelman) | **skip** (image-only) | raw/literary_canon_general/ `Maus I.cbr` (old) + image-only epub in source universe | graphic novel · not text material |
| Maus II (Spiegelman) | **skip** (image-only) | image-only epub in source universe (not in raw/) | graphic novel · not text material |
| Russian-author mobi (`Шерман, Алекси`) | **skip** (present-but-unidentified) | source universe `[Part 1 ] Шерман, Алекси _ - libgen.li.mobi` | **CORRECTION:** present in the source universe (a Part 1 mobi), NOT absent · unidentified, unstaged, unchunked · hold until BJ identifies it |

### Confirmations against the task spec

- **recovered_and_processed includes Confessions, Sugarman, Halbert, Margin of Safety.** CONFIRMED (all 4 chunked).
- **recovered_staged_not_processed includes Hit Men, The Mailroom, Predictably Irrational, Grace, Total Recall, Beloved, Jonathan Livingston Seagull.** CONFIRMED (all 7 staged as `_RECOVERED` in raw/, 0 chunks).
- **still_broken / skip:** Caples (scanned · still_broken), Maus I (image-only · skip), Maus II (image-only · skip). CONFIRMED.
- **Russian-author:** the spec said "absent"; the refresh CORRECTS this to **present-but-unidentified in the source universe** (a Part 1 mobi) · still skip (unidentified, unstaged, unchunked).

## 7. Next-lane recommendations (from the staged backlog)

1. **Media-business recovery mini-batch** · Hit Men + The Mailroom (staged · MEDIA_BUSINESS family · music/Hollywood institutions).
2. **Persuasion recovery mini-batch** · Predictably Irrational (staged · BATCH_009 / persuasion-psych / behavioral-economics).
3. **Founder/fashion recovery mini-batch** · Grace + Total Recall (staged · BIOGRAPHY_FOUNDER_MEDIA family · taste-making / operator memoir).
4. **Literary recovery mini-batch** · Beloved (LITERARY_CANON_BLACK) + Jonathan Livingston Seagull (LITERARY_CANON_GENERAL) (staged).
5. **Historical-biography lane** · Grant + Washington (Chernow · already in raw/memoirs_biographies/, not yet processed).
6. **Fresh current SNIPED brief / CURRENT_IDENTITY principle-only ship** (identity-side · unlocks the held plan).
7. **SPIRITUAL_FOUNDATION decision for the held KJV Bible** (design a reverent track or keep holding as anchor · deliberate, unhurried).
8. **(Larger canon backlog, not recovery)** · the Tier-1 strategy/decision canon (Napoleon, Herodotus, Machiavelli, Marcus Aurelius, On War, Alexander-logistics, operating_founder set) and the Tier-2 decision_judgment / leadership_mgmt / fashion_luxury clusters remain the biggest staged-not-processed opportunity beyond recovery.

## 8. Top immediate recommendation

**Media-business recovery mini-batch (Hit Men + The Mailroom).** Two staged, text-clean sources that directly extend the existing MEDIA_BUSINESS lane (music-industry power/money + Hollywood talent-system), the most coherent and highest-value of the staged recovery pairs, with a clear existing-domain home (`media-business` + `commercial-architecture` + `culture` + `operator-process`) and no new-domain risk. The persuasion (Predictably Irrational) and founder/fashion (Grace + Total Recall) and literary (Beloved + Seagull) lanes follow naturally.

## 9. Still-broken / skip / missing list

- **Tested Advertising Methods (Caples):** scanned/image-only · re-acquire a clean epub (the only true still-broken recovery item; Sugarman + Halbert already carry the direct-response lane).
- **Maus I + Maus II:** image-only graphic novels (cbr / image epub) · skip · not text-corpus material.
- **Russian-author mobi (`Шерман, Алекси`):** present-but-unidentified in the source universe · skip until BJ confirms the title and relevance.

## 10. Bible status

**The KJV Bible (`The-Holy-Bible-King-James-Version.pdf`) remains OUTSIDE raw/ and UNCHUNKED.** Confirmed not in raw/, not in any `*_CHUNKS.jsonl`, held as a reverent SPIRITUAL_FOUNDATION anchor/reference in the source universe per NEW_SOURCE_INTAKE_PLAN. No faith/spiritual lane exists.

## 11. Identity optionality status

ACTIVE and unchanged. No lane finalizes SNIPED / SNIPED Media / BASEPLATE direction. CURRENT_OPERATOR_REALITY_BRIEF is the read-first anchor (not chunked); CURRENT_IDENTITY_AND_BRAND_OPTIONALITY is plan-only / not extracted. The capital/finance, founder-arc, media-business, hospitality, and advertising/copywriting lanes are all held as decision-support / execution / pattern-library lenses, not directives. Photography remains one option among several.

## 12. Constraints honored by this audit

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,471.
- Did NOT modify any raw/ or source file (read-only `find` / `wc` / `grep` / `ls`).
- Did NOT touch the Bible.
- No next lane started. No em-dashes. Wrote only this report. Not committed.
