# BATCH_003_TIER_2_CANON_BOOKS · Extraction Log

**Date:** 2026-05-16
**Source:** `raw/03_TIER_2_CANON_BOOKS/` (10 files, moved into folder from raw/ root before extraction)
**Destination:** `01_KNOWLEDGE_BASE/batches/batch_003_extracted/`

## Tooling

All tools previously installed for BATCH_002. No new tooling required.

| Tool | Version path | Purpose |
|------|----|---------|
| pandoc | `/opt/homebrew/bin/pandoc` (3.9.0.2) | epub → markdown |
| pdftotext | `/opt/homebrew/bin/pdftotext` (poppler 26.04.0) | pdf → text |

## Outcome

- **Files successfully extracted:** 10
- **Files failed:** 0
- **Files skipped as duplicates:** 0 (all md5s unique vs BATCH_002)
- **Files deferred:** 0
- **OCR required:** 0
- **Total extracted text:** 4.91 MB across 8 markdown + 2 text files
- **Cleanup applied:** 0 files (all extractions came out usable as-is)

## Per-file results

| # | Source filename | Output | Size | Method | Notes |
|--:|-------------|--------|-----:|--------|-------|
| 1 | `Blair Enns - The Win Without Pitching Manifesto (2010, RockBench Publishing Corp) - libgen.li.epub` | `wwp_manifesto_enns.md` | 134 KB | pandoc | clean · 12 proclamations cleanly headed in TOC |
| 2 | `Blair Enns - Pricing Creativity_ A Guide to Profit Beyond the Billable Hour (2018, RockBench Publishing Corp.) - libgen.li.epub` | `pricing_creativity_enns.md` | 384 KB | pandoc | clean · Principles + Rules + Tips structure preserved |
| 3 | `Will Guidara - Unreasonable Hospitality_ The Remarkable Power of Giving People More Than They Expect (2022, Optimism Press) - libgen.li.pdf` | `unreasonable_hospitality_guidara.txt` | 489 KB | pdftotext -layout | clean · text-bearing PDF (verified pre-extraction); 20 chapters cleanly delineated |
| 4 | `Alain De Botton - Status Anxiety (2005, Vintage) - libgen.li.epub` | `status_anxiety_de_botton.md` | 384 KB | pandoc | clean · 5 Causes / 5 Solutions structure preserved; pandoc anchor artifacts as expected |
| 5 | `Simler, Kevin _ Hanson, Robin - The Elephant in the Brain_ Hidden Motives in Everyday Life (2017, Oxford University Press) - libgen.li.epub` | `elephant_in_the_brain_simler_hanson.md` | 1.07 MB | pandoc | clean · largest extraction in batch; OUP epub structure clean |
| 6 | `[Company of One] Jarvis, Paul - Company of one why staying small is the next big thing for business (2018_2019, Penguin Books Ltd_Penguin Business) - libgen.li.epub` | `company_of_one_jarvis.md` | 440 KB | pandoc | clean · 13 chapters with clean heading anchors |
| 7 | `Holiday, Ryan - Perennial seller_ the art of making and marketing work that lasts (2017, Penguin Publishing Group_Portfolio_Penguin) - libgen.li.epub` | `perennial_seller_holiday.md` | 454 KB | pandoc | clean · 4 Parts (Creative / Positioning / Marketing / Platform) plus conclusion preserved |
| 8 | `Naval Ravikant, Eric Jorgenson, Jack Butcher, Tim Ferriss - The Almanack of Naval Ravikant_ A Guide to Wealth and Happiness (2020) - libgen.li.pdf` | `almanack_naval_ravikant.txt` | 286 KB | pdftotext -layout | clean · curated-quote layout preserved; pull-quote arrows (↓) visible but tolerable; no cleanup applied |
| 9 | `Elberse, Anita - Blockbusters_ Hit-making, Risk-taking, and the Big Business of Entertainment (2013, Henry Holt and Co.) - libgen.li.epub` | `blockbusters_elberse.md` | 680 KB | pandoc | clean · chapter structure intact |
| 10 | `Sax, David - The Revenge of Analog_ Real Things and Why They Matter (2016, PublicAffairs) - libgen.li.epub` | `revenge_of_analog_sax.md` | 710 KB | pandoc | clean · per-category chapter structure preserved |

## Cleanup applied

None. All 10 files extracted clean enough for direct chunking without intermediate cleanup.

The Naval PDF, which the BATCH_003 plan flagged as a possible cleanup candidate (curated quote layout with sidebars and pull-quotes), came out usable as-is. The pull-quote arrow characters (↓) and page numbers are visible in the text but don't interfere with semantic content or chunking. Skipped optional cleanup to avoid introducing changes for cosmetic-only improvement.

## Decisions and notes

1. **No duplicate checks needed mid-batch.** Md5 cross-check against BATCH_002 done pre-extraction during planning phase; all 10 files confirmed unique. No risk of duplicating BATCH_002 content.

2. **Pandoc anchor artifacts preserved.** EPUB → markdown output includes `[]{#fragment-id}` navigation anchors and `{.calibre1}` style markers consistent with BATCH_002 convention. Preserved as-is for source-traceability; downstream chunkers can strip via regex if clean prose output is needed.

3. **Two PDFs verified text-bearing pre-extraction.** Both Naval and Guidara PDFs returned clean prose from a 3-page pdftotext sample during the BATCH_003 planning phase. Full extraction confirmed: no OCR needed for either.

4. **All 10 files moved into `raw/03_TIER_2_CANON_BOOKS/` before extraction.** Per user decision during planning phase, files were relocated from `raw/` root into a dedicated batch folder mirroring the BATCH_002 convention. This produces a clean batch folder for log reference and prevents future re-flagging of the same files for other batches.

5. **Schein deferred.** Michael Schein's Hype Handbook was on the BATCH_002 next-batch recommendation but not present in `raw/`. Per user decision, BATCH_003 proceeded with the 10 available books; Schein can be added later as a top-up or in BATCH_004.

## Files in `01_KNOWLEDGE_BASE/batches/batch_003_extracted/` (final)

```
     137,104  wwp_manifesto_enns.md
     392,859  pricing_creativity_enns.md
     500,815  unreasonable_hospitality_guidara.txt
     393,384  status_anxiety_de_botton.md
   1,090,988  elephant_in_the_brain_simler_hanson.md
     450,676  company_of_one_jarvis.md
     464,721  perennial_seller_holiday.md
     292,581  almanack_naval_ravikant.txt
     695,786  blockbusters_elberse.md
     726,694  revenge_of_analog_sax.md
```

**Total: 10 files · 4.91 MB extracted text · 0 failures · 0 cleanup needed · 0 OCR · 0 deferred · 0 duplicates.**

## Next step

Extraction phase complete. Chunking pipeline already executed (see `scripts/write_batch_003_chunks.py`), producing 103 chunks in `01_KNOWLEDGE_BASE/batches/BATCH_003_CHUNKS.jsonl`. Companion summary, index, and complete-log files written in parallel.
