# RECOVERY_STAGING_REPORT · staging the 11 usable recovered files into raw/ · 2026-05-24

**Status:** Authorized staging pass. The 11 usable recovered files were **copied** (not moved) from the source universe into their `raw/` destination folders, each with a `_RECOVERED` suffix so the old bad originals remain untouched beside them for comparison. No extraction, no chunking, no master-file changes, no modification/deletion of any existing file.

## 0. State

- **Head commit:** `f7fa4c7 revise DEEP_FINANCE_EXPANSION plan for recovered Margin of Safety`
- **Total chunks:** 1,403 (unchanged) · numbered batches 10 · mini-batches 18 · official domains 62.
- **Source of truth for routing:** the RECOVERY_INTAKE_CHECK proposed move map (`9814893`).

## 1. Destination-folder note (divergence from the task's "recommended folders")

The task listed `raw/04_LITERARY_CANON/` for Beloved and Jonathan Livingston Seagull. **That folder does NOT exist** in the repo. Per the rule ("if a destination folder does not exist, report it and stop before creating a new folder unless clearly aligned"), I did NOT create it. Instead I used the **RECOVERY_INTAKE_CHECK move map (the named source of truth)**, which places each literary book beside its old bad original in the existing tier-1 literary folders:
- Beloved → `raw/02_TIER_1_CANON_BOOKS/literary_canon_black/` (exists · holds the old Beloved stub PDF)
- Jonathan Livingston Seagull → `raw/02_TIER_1_CANON_BOOKS/literary_canon_general/` (exists · holds the old Seagull djvu)

All other destination folders existed and were used as listed.

## 2. Copied files (11) · source -> destination · verification

All sources are in `~/Downloads/    SNIPED_OS/`. All destinations are under `raw/`. Word counts via read-only pdftotext (pdf) / ebook-convert (epub/azw3) to /tmp, then deleted. Every copy verified: exists, correct type, non-trivial size, text extractable, title/author match.

| # | Title (author) | Dest folder | Staged filename (`_RECOVERED`) | Type | Size | Words | Verify | Old bad file still present? |
|---|---|---|---|---|---|---:|---|---|
| 1 | Confessions of an Advertising Man (Ogilvy) | `raw/02_TIER_1_CANON_BOOKS/advertising/` | `Confessions-of-an-Advertising-Man-by-Ogilvy-David-Parker-Alan-z-lib.org__RECOVERED.pdf` | pdf | 0.7 MB | 42,924 | OK | yes (old scanned 22.5 MB PDF) |
| 2 | The Adweek Copywriting Handbook (Sugarman) | `raw/02_TIER_1_CANON_BOOKS/advertising/` | `...{Sugarman, Joseph}(2024){112008782} libgen.li_RECOVERED.azw3` | azw3 | 4.4 MB | 107,745 | OK | n/a (was absent) |
| 3 | The Boron Letters (Halbert) | `raw/02_TIER_1_CANON_BOOKS/advertising/` | `Gary C Halbert - The Boron Letters (2013) - libgen.li_RECOVERED.epub` | epub | 0.1 MB | 43,043 | OK | n/a (was absent) |
| 4 | Predictably Irrational, Revised (Ariely) | `raw/03_TIER_2_CANON_BOOKS/persuasion_psych/` | `Dan Ariely - Predictably Irrational, Revised and Expanded Edition_ ... (2009, HarperCollins) - libgen.li_RECOVERED.epub` | epub | 0.6 MB | 107,959 | OK | yes (old djvu) |
| 5 | Hit Men (Dannen) | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` | `[Vintage] Dannen, Fredric - Hit Men_ ... (2011, ...Vintage eBooks) - libgen.li_RECOVERED.azw3` | azw3 | 2.4 MB | 152,952 | OK | yes (old scanned PDF) |
| 6 | The Mailroom (Rensin) | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` | `Rensin, David - The Mailroom_ ... (2007, Random House...) - libgen.li_RECOVERED.epub` | epub | 0.5 MB | 169,850 | OK | yes (old djvu) |
| 7 | Grace: A Memoir (Coddington) | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` | `Grace Coddington - Grace_ A Memoir (2012, Random House) - libgen.li_RECOVERED.epub` | epub | 103 MB | 82,009 | OK | yes (old 0-byte stub) |
| 8 | Total Recall (Schwarzenegger) | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` | `Schwarzenegger, Arnold - Total Recall- ... (2012, Simon & Schuster) - libgen.li_RECOVERED.epub` | epub | 8.9 MB | 242,002 | OK | yes (old 0-byte stub) |
| 9 | Margin of Safety (Klarman) | `raw/03_TIER_2_CANON_BOOKS/investing_finance/` | `Seth A. Klarman - Margin of Safety_ ... (1991, HarperCollins) - libgen.li_RECOVERED.epub` | epub | 0.6 MB | 72,828 | OK | yes (old scanned PDF) |
| 10 | Beloved (Morrison) | `raw/02_TIER_1_CANON_BOOKS/literary_canon_black/` | `Toni Morrison - Beloved (Vintage International) - libgen.li_RECOVERED.azw3` | azw3 | 0.7 MB | 97,915 | OK | yes (old 4-page stub PDF) |
| 11 | Jonathan Livingston Seagull (Bach) | `raw/02_TIER_1_CANON_BOOKS/literary_canon_general/` | ` Bach, Richard - Jonathan Livingston Seagull (2010, Avon Books) - libgen.li_RECOVERED.epub` | epub | 0.04 MB | 8,977 | OK | yes (old djvu) |

**All 11 copied and verified usable (text extracts cleanly · titles/authors match intended targets).**

## 3. Collisions / renames

- **No collisions.** Each `_RECOVERED` filename is net-new in its destination folder (no existing file was overwritten · `cp` was guarded to skip if the destination already existed · none did).
- **Rename convention:** `_RECOVERED` appended to the stem before the extension (per rule 5), so the recovered file and the old bad original coexist and are easy to tell apart. Example: `... - libgen.li_RECOVERED.epub` beside the old `... - libgen.li.pdf` / `.djvu` / 0-byte `.epub`.
- **Disambiguation handled:** the source universe also contained bad/partial variants that were deliberately NOT staged: the old scanned `Margin of Safety ... .pdf`, the `Total recall ... .epub.part` (incomplete) and the 0-byte `Petre ... Total recall ... .epub`, the `Coddington, Grace ... .part`, and the unrelated `[Adweek Series] Luke Sullivan - Hey, Whipple, Squeeze This ... .pdf` (a different book). Only the clean recovered files were copied.

## 4. Old bad files preserved (copy, not move)

Confirmed every old bad original still sits in its raw/ folder beside the recovered copy (git shows 11 additions, 0 modifications, 0 deletions):
- advertising: old scanned `David Ogilvy_ Alan Parker - Confessions ... .pdf` retained.
- persuasion_psych: old `Predictably Irrational_ ... .djvu` retained.
- memoirs_biographies: old `Hit men_ ... .pdf`, `The Mailroom ... .djvu`, `Coddington, Grace ... .epub` (0-byte), `Petre ... Total recall ... .epub` (0-byte) retained.
- investing_finance: old scanned `Margin of Safety ... .pdf` retained.
- literary_canon_black: old `[Beloved Trilogy 1 ...] ... .pdf` (4-page stub) retained.
- literary_canon_general: old `Richard Bach - Jonathan Livingston Seagull. (1973...) ... .djvu` retained.

(These superseded originals can be removed in a later authorized cleanup; they are left in place per the staging rules.)

## 5. Still broken / not staged (do NOT stage)

- **Tested Advertising Methods (Caples)** · the re-downloaded PDF is still scanned/image-only (0 extractable words) · re-download a clean epub.
- **Maus I + Maus II** · image-only graphic-novel epubs (0 extractable text) · skip (not text material).
- **Russian-author mobi (`Шерман, Алекси`)** · still absent / unidentified · skip until BJ clarifies.

## 6. DEEP_FINANCE_EXPANSION readiness

**Confirmed: Margin of Safety now exists in `raw/03_TIER_2_CANON_BOOKS/investing_finance/` as a usable epub (`... - libgen.li_RECOVERED.epub` · 72,828 words).** All **8** DEEP_FINANCE_EXPANSION CORE sources are now present in repo-local `raw/` (the original 7 were already staged; Margin of Safety is now staged too). **DEEP_FINANCE_EXPANSION can ship entirely from repo-local raw sources** when the operator authorizes the extract/chunk step · no source-universe dependency remains for that lane. The extract script should point at the `..._RECOVERED.epub` for Margin of Safety (and may continue to use the already-staged paths for the other 7).

## 7. Confirmations

- **No extraction** · no `*_extracted/` dir created.
- **No chunking** · no `*_CHUNKS.jsonl` created · total_chunks unchanged at **1,403**.
- **No master-file updates** · MASTER_INDEX / MASTER_CHUNK_MAP / ACTIVE_KNOWLEDGE_STATE untouched.
- **No existing raw file modified or deleted** · git shows 11 untracked additions, 0 modified, 0 deleted.
- **Copy, not move** · the source-universe originals remain in `~/Downloads/    SNIPED_OS/`.
- **No OCR, no new dependencies.**
- **Source files (source universe) not modified/moved/renamed/deleted** · read-only checks only.
- Em-dash clean.

## 8. Next step (operator decision · not started)

With all 8 DEEP_FINANCE_EXPANSION sources staged in raw/, the lane is ready to ship (extract -> chunk -> validate) on authorization, per the revised `DEEP_FINANCE_EXPANSION_PLAN.md` (target ~25-31 chunks · capital anchors · no new domain · economics not created). The advertising-recovery (Confessions + Sugarman + Halbert), persuasion (Predictably Irrational), media-business-recovery (Hit Men + The Mailroom), founder/fashion (Grace + Total Recall), and literary-recovery (Beloved + Seagull) sources are also now staged for their respective future lanes.
