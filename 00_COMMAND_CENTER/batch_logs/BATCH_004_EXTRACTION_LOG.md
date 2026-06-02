# BATCH_004_SNIPED_OS_DEPTH_FILL · Extraction Log

**Date:** 2026-05-18
**Source:** 8 SNIPED-internal docs across `raw/`, `raw/00_BRIEF/`, `raw/10_REFERENCE/`
**Destination:** `01_KNOWLEDGE_BASE/batches/batch_004_extracted/`

## Tooling

All tools previously installed (BATCH_002). No new tooling.

| Tool | Version path | Purpose |
|------|----|---------|
| pandoc | `/opt/homebrew/bin/pandoc` (3.9.0.2) | docx → markdown |
| python3 shutil.copy2 | stdlib | md → md (verbatim copy) |

## Outcome

- **Files successfully extracted:** 8 (5 docx via pandoc, 3 md via copy)
- **Files failed:** 0
- **Files skipped as duplicates:** 0
- **Files deferred:** 0
- **OCR required:** 0
- **Total extracted text:** 1.05 MB across 8 markdown files
- **Cleanup applied:** 0 files (all extractions came out usable as-is)

## Per-file results

| # | Source path | Output | Size | Method | Notes |
|--:|-------------|--------|-----:|--------|-------|
| 1 | `chat Sniped MAster thread.docx` (root) | `chat_sniped_master_thread.md` | 412 KB | pandoc | clean · 280 KB source → 412 KB markdown (formatting expansion). Discrepancy flagged below. |
| 2 | `Gemini Sniped MAster thread.docx` (root) | `gemini_sniped_master_thread.md` | 238 KB | pandoc | clean · 202 KB source → 238 KB markdown. Discrepancy flagged below. |
| 3 | `Aesthetic_Statement_v1.docx` (root) | `aesthetic_statement_v1.md` | 4 KB | pandoc | clean · small high-density doc · 75 lines markdown |
| 4 | `00_BRIEF/100Q_AUDIT_OPTIMIZATIONS_2026-05-13.md` | `100q_audit_optimizations.md` | 57 KB | copy | clean · already plain markdown · 696 lines, 13 SECTIONS + CLOSING + CONSOLIDATED + CROSS-REFERENCES |
| 5 | `10_REFERENCE/STRATEGIC_PRINCIPLES.md` | `strategic_principles.md` | 70 KB | copy | clean · already plain markdown · 855 lines, 12 main sections + subsections. Sections 4a-4k explicitly skipped during chunking (BATCH_003 dedupe). |
| 6 | `00_BRIEF/SNIPED_OS_V1_SYNTHESIS_2026-05-12.md` | `sniped_os_v1_synthesis.md` | 70 KB | copy | clean · already plain markdown · 1144 lines, 14 sections + Appendix A/B |
| 7 | `The_Offer_Stack.docx` (root) | `offer_stack_full.md` | 102 KB | pandoc | clean · full extraction · Parts I-VII covered in BATCH_001 explicitly skipped during chunking |
| 8 | `The_Platform_Stack.docx` (root) | `platform_stack_full.md` | 118 KB | pandoc | clean · full extraction · Parts I-VI covered in BATCH_001 explicitly skipped during chunking |

## Cleanup applied

None. All 8 files extracted clean enough for direct chunking without intermediate cleanup. Pandoc anchor artifacts present in markdown output (`[]{#fragment-id}` navigation anchors) but tolerable for chunking purposes.

## Decisions and notes

1. **File-size discrepancies flagged (per BATCH_004_PLAN.md risk #1-#2).**
   - `chat Sniped MAster thread.docx`: BATCH_001 source index reports 407 KB; actual source file is 280 KB; markdown output is 412 KB (markdown formatting expansion from docx).
   - `Gemini Sniped MAster thread.docx`: BATCH_001 source index reports 237 KB; actual source file is 202 KB; markdown output is 238 KB.
   - **Disposition:** flag-and-proceed per plan. Content scope appears sufficient for chunking purposes; if user later identifies missing content, can re-extract from an archive copy. The 412 KB markdown for chat thread is the largest extracted-text-per-source in this batch.

2. **Dedupe discipline applied at chunking phase, not extraction phase.**
   - Offer_Stack and Platform_Stack were FULLY extracted (all 13 Parts each) but the chunking script explicitly skipped Parts I-VII (Offer) and I-VI (Platform) to avoid duplicating BATCH_001 chunks. This preserves the full extracted text for future reference while preventing chunk duplication.
   - STRATEGIC_PRINCIPLES Sections 4a-4k (book summaries for BATCH_003 sources) were skipped during chunking. The full text remains in the extracted file; the chunking pipeline simply did not chunk those subsections.

3. **MD files copied verbatim, not re-processed.**
   - 100Q_AUDIT, STRATEGIC_PRINCIPLES, SNIPED_OS_V1_SYNTHESIS were already plain markdown in raw/. They were copied to `batch_004_extracted/` for archival consistency but not transformed in any way. The originals in raw/ remain canonical.

4. **Aesthetic_Statement_v1 is the smallest source in any batch so far (4 KB markdown).** It produced 6 chunks · highest chunk density per byte in the corpus. Confirms the plan estimate that small high-doctrine files yield disproportionate chunk value.

5. **No PDFs in this batch.** No OCR considerations. All 8 sources were docx or md.

6. **Em-dash compliance preserved.** All extracted text passes through markdown faithfully; no em-dashes were introduced. The locked global rule held.

## Files in `01_KNOWLEDGE_BASE/batches/batch_004_extracted/` (final)

```
       4,102  aesthetic_statement_v1.md
      56,587  100q_audit_optimizations.md
      70,118  strategic_principles.md
      69,932  sniped_os_v1_synthesis.md
     412,284  chat_sniped_master_thread.md
     238,202  gemini_sniped_master_thread.md
     102,197  offer_stack_full.md
     117,758  platform_stack_full.md
```

**Total: 8 files · 1.05 MB extracted text · 0 failures · 0 cleanup needed · 0 OCR · 0 deferred · 0 duplicates extraction-time. Dedupe-discipline applied at chunking phase.**

## Next step

Extraction phase complete. Chunking pipeline already executed (see `scripts/write_batch_004_chunks.py`), producing 96 chunks in `01_KNOWLEDGE_BASE/batches/BATCH_004_CHUNKS.jsonl`. Companion summary, source index, and complete-log files follow.
