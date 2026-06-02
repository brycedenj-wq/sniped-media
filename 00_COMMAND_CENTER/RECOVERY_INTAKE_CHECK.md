# RECOVERY_INTAKE_CHECK · newly downloaded recovery files · 2026-05-24

**Status:** REPORT ONLY. Read-only verification of the files BJ downloaded from the recovery list. No extraction, no chunking, no master-file changes, no file moves/renames/deletes, no OCR, no installs.

## 0. Current corpus state (verified)

- **Head commit:** `364b8c9 plan DEEP_FINANCE_EXPANSION mini-batch`
- **Repo working tree:** clean (the new files are NOT in the repo · see below).
- **Total chunks:** 1,403 · **numbered batches:** 10 · **mini-batches:** 18 · **official domains:** 62.

## 1. Where the files landed

BJ moved the files into the **source universe**, `~/Downloads/    SNIPED_OS/` (4 leading spaces · the canonical SNIPED OS source folder per AGENTS.md), **not** into `raw/`. That folder is OUTSIDE the git repo, so the new files do **not** appear in `git status` and are **not** yet staged. They sit beside the old broken originals (which are still present). Staging into `raw/` is a separate, operator-authorized step (SOP step 3-4) and was NOT performed here.

- **New files detected (intended recovery downloads):** 14
- **Matched to recovery targets:** 14 of 15 (the Russian-author mobi was not downloaded)
- **recovered_usable:** 11 · **still_broken:** 3 · **already_canonical / duplicate-of-canonical:** 0
- Also present: incomplete-download cruft (`.part` files + a 0-byte `Maus II.cbr`) · ignore/cleanup.

## 2. Full verification table (read-only checks)

All paths are under `~/Downloads/    SNIPED_OS/`. Word counts via pdftotext (pdf) or ebook-convert (epub/azw3) to /tmp, then deleted. No file modified.

| # | New file | Matched target | Type | Size | Words | Status | Problem (if any) |
|---|---|---|---|---|---:|---|---|
| 1 | `Confessions-of-an-Advertising-Man-by-Ogilvy-David-Parker-Alan-z-lib.org_.pdf` | Confessions of an Advertising Man (Ogilvy) | pdf | 0.7 MB | 42,924 | **recovered_usable** | text layer present (42 pp, reflowed edition) |
| 2 | `[Vintage] Dannen, Fredric - Hit Men_ ... (2011) - libgen.li.azw3` | Hit Men (Dannen) | azw3 | 2.4 MB | 152,952 | **recovered_usable** | replaces old scanned PDF |
| 3 | `Rensin, David - The Mailroom_ ... (2007) - libgen.li.epub` | The Mailroom (Rensin) | epub | 0.5 MB | 169,850 | **recovered_usable** | replaces old djvu |
| 4 | `Dan Ariely - Predictably Irrational, Revised and Expanded ... (2009) - libgen.li.epub` | Predictably Irrational (Ariely) | epub | 0.6 MB | 107,959 | **recovered_usable** | replaces old djvu · revised/expanded ed |
| 5 | `The Adweek Copywriting Handbook ... {Sugarman, Joseph}(2024) ... libgen.li.azw3` | The Adweek Copywriting Handbook (Sugarman) | azw3 | 4.4 MB | 107,745 | **recovered_usable** | was absent · now present |
| 6 | `Gary C Halbert - The Boron Letters (2013) - libgen.li.epub` | The Boron Letters (Halbert) | epub | 0.1 MB | 43,043 | **recovered_usable** | was absent · now present |
| 7 | `Grace Coddington - Grace_ A Memoir (2012, Random House) - libgen.li.epub` | Grace: A Memoir (Coddington) | epub | 103 MB | 82,009 | **recovered_usable** | replaces old 0-byte stub · large (image-rich) but text extracts |
| 8 | `Seth A. Klarman - Margin of Safety_ ... (1991) - libgen.li.epub` | Margin of Safety (Klarman) | epub | 0.6 MB | 72,828 | **recovered_usable** | replaces old scanned PDF · **re-opens DEEP_FINANCE inclusion (see 6)** |
| 9 | `Schwarzenegger, Arnold - Total Recall- ... (2012) - libgen.li.epub` | Total Recall (Schwarzenegger) | epub | 8.9 MB | 242,002 | **recovered_usable** | replaces old 0-byte stub |
| 10 | `Toni Morrison - Beloved (Vintage International) - libgen.li.azw3` | Beloved (Morrison) | azw3 | 0.7 MB | 97,915 | **recovered_usable** | replaces old 4-page stub PDF · full text · Morrison-as-author already in LITERARY_CANON_BLACK (author overlap, NOT a duplicate title) |
| 11 | ` Bach, Richard - Jonathan Livingston Seagull (2010, Avon Books) - libgen.li.epub` | Jonathan Livingston Seagull (Bach) | epub | 0.04 MB | 8,977 | **recovered_usable** | replaces old djvu · low word count is correct (short fable) |
| 12 | `John Caples, David Ogilvy - Tested Advertising Methods (4th Ed.) - libgen.li.pdf` | Tested Advertising Methods (Caples) | pdf | 54.8 MB | 0 (164 pp) | **still_broken** | scanned / image-only · would need OCR · re-download as epub |
| 13 | `[Maus Series _1] Art Spiegelman - Maus I ... (1986) - libgen.li.epub` | Maus I (Spiegelman) | epub | 109 MB | 0 | **still_broken** | image-only graphic novel (epub of scans) · not text material |
| 14 | `[Maus Series _2] Art Spiegelman - Maus II ... (1992) - libgen.li.epub` | Maus II (Spiegelman) | epub | 81 MB | 0 | **still_broken** | image-only graphic novel (epub of scans) · not text material |
| - | (not downloaded) | Russian-author mobi (`Шерман, Алекси`) | - | - | - | **skip** | still absent · unidentified · hold until BJ clarifies |

### Duplicate / already-canonical findings

- **Already-canonical chunks for any recovered title: 0** (checked all `*_CHUNKS.jsonl`). None duplicate an existing canonical source.
- **Author overlaps (not duplicates):** Morrison is already in LITERARY_CANON_BLACK (6 chunks · other works) · Beloved is a net-new title. Ogilvy = 0 chunks in corpus · Confessions is net-new.
- **The old broken originals still sit in the source universe beside the new files** (old Confessions scanned PDF, old Margin scanned PDF, old djvu Mailroom/Predictably Irrational/Seagull, old 0-byte Grace/Total Recall, old Beloved stub PDF, old Maus I.cbr). They are superseded by the recovered files but were NOT deleted (read-only pass).
- **Incomplete-download cruft to ignore/clean up:** `Coddington, Grace ... .part` (24.9 MB partial), `Maus II.cbr` (0 B), `Maus II.j93PR5Wn.cbr.part` (15.7 MB partial). These are abandoned partial downloads, not the clean files above.

## 3. Tally

- recovered_usable: **11**
- still_broken: **3** (Caples · scanned PDF; Maus I + Maus II · image-only epubs)
- wrong_source / duplicate / already_canonical: **0**
- missing (not downloaded): **1** (Russian-author mobi)

## 4. Ready to route (11 · usable · text confirmed)

Confessions of an Advertising Man · Hit Men · The Mailroom · Predictably Irrational · The Adweek Copywriting Handbook (Sugarman) · The Boron Letters (Halbert) · Grace: A Memoir · Margin of Safety · Total Recall · Beloved · Jonathan Livingston Seagull.

## 5. Still need redownload / re-acquire

- **Tested Advertising Methods (Caples):** the new PDF is still scanned/image-only (0 extractable words) · re-download a **clean epub** (the other half of the direct-response trio · Sugarman + Halbert are already usable).

## 6. Material change to the DEEP_FINANCE_EXPANSION plan

**Margin of Safety is now usable** (epub · 72,828 words). The committed `DEEP_FINANCE_EXPANSION_PLAN.md` (`364b8c9`) currently **excludes** it as scanned/recovery. This check **re-opens** its inclusion: the operator may want to add Margin of Safety as the **8th source** in DEEP_FINANCE_EXPANSION (raising the target band slightly). Flagged for an operator decision · the plan is not edited here.

## 7. "Do not worry about these"

- **Maus I + Maus II** · image-only graphic novels even as epub (0 extractable text) · not text-corpus material · skip (OCR is banned and low-value).
- **Russian-author mobi** · not downloaded · unidentified · skip until BJ confirms the title and why it belongs.
- **The `.part` / 0-byte cruft** (Grace `.part`, Maus II `.cbr` 0-byte + `.part`) · incomplete downloads · ignore (BJ can delete them at leisure).
- **Tested Advertising Methods** is not lost · Sugarman + Halbert carry the direct-response lane until a clean Caples arrives.

## 8. Proposed move map (DO NOT EXECUTE · for a future authorized staging pass)

Each usable file should be staged from the source universe into the matching `raw/` subfolder, replacing (or sitting beside, then superseding) the known bad original in that folder. Format preference satisfied (epub/azw3/clean-text PDF · no djvu/cbr/scanned).

| Recovered file (source universe) | Proposed raw/ destination | Replaces (bad original) | Future lane |
|---|---|---|---|
| Confessions ... z-lib.org_.pdf | `raw/02_TIER_1_CANON_BOOKS/advertising/` | old scanned Confessions PDF | advertising recovery (BATCH_009 family) |
| Adweek Copywriting Handbook (Sugarman) azw3 | `raw/02_TIER_1_CANON_BOOKS/advertising/` | (none · was absent) | advertising recovery (BATCH_009 family) |
| The Boron Letters (Halbert) epub | `raw/02_TIER_1_CANON_BOOKS/advertising/` | (none · was absent) | advertising recovery (BATCH_009 family) |
| Predictably Irrational (Revised) epub | `raw/03_TIER_2_CANON_BOOKS/persuasion_psych/` | old Predictably Irrational djvu | persuasion / decision recovery (BATCH_009 family) |
| Hit Men (Dannen) azw3 | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` | old Hit Men scanned PDF | media-business recovery (MEDIA_BUSINESS) |
| The Mailroom (Rensin) epub | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` | old The Mailroom djvu | media-business recovery (MEDIA_BUSINESS) |
| Grace: A Memoir epub | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` | old Grace 0-byte stub | founder-media / fashion-luxury |
| Total Recall epub | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` | old Total Recall 0-byte stub | founder / biography (optional) |
| Margin of Safety epub | `raw/03_TIER_2_CANON_BOOKS/investing_finance/` | old Margin of Safety scanned PDF | DEEP_FINANCE_EXPANSION (now eligible · see 6) |
| Beloved (Vintage Intl) azw3 | `raw/02_TIER_1_CANON_BOOKS/literary_canon_black/` | old Beloved 4-page stub PDF | literary recovery (LITERARY_CANON_BLACK-adjacent) |
| Jonathan Livingston Seagull (2010) epub | `raw/02_TIER_1_CANON_BOOKS/literary_canon_general/` | old Seagull djvu | literary recovery (optional · LITERARY_CANON_GENERAL-adjacent) |

**Recommendation on replacement:** stage the new good file into the raw/ subfolder, then remove the superseded bad original **in the same authorized staging pass** (do not hand-delete raw originals outside an authorized pass · AGENTS.md drift rule). Until then, the bad originals stay put.

**still_broken (do NOT route):** Tested Advertising Methods (re-download epub first), Maus I, Maus II.

## 9. Scope guards honored

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,403.
- Did NOT move, rename, delete, or modify any source file or raw file (read-only `file` / `wc -c` / `pdfinfo` / `pdftotext`-to-/tmp / `ebook-convert`-to-/tmp · temp deleted).
- Did NOT OCR and did NOT install anything.
- No CHUNKS.jsonl, no extracted dir, no COMPLETE marker created.
- Wrote only this report. Not committed (operator will review first).
