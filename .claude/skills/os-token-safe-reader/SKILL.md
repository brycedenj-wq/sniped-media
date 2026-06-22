---
name: os-token-safe-reader
description: Whole-read large files (books, PDFs, epubs, docx, transcripts) without hitting the 25k-token Read cap, with proven beginning-middle-end coverage. Use whenever engaging a source longer than ~15k words, or whenever "did we actually read the whole thing" matters. Prevents the fake-completion failure where word/line-sized segments silently error past the read cap.
---

# Token-Safe Reader + Extraction Audit

The Read tool errors (does not truncate) above ~25,000 tokens per call. Segmenting by words or lines lets epub/PDF conversions (few long paragraph-lines) overflow and fail silently. This skill is the proven fix.

## Engine
1. CONVERT to text if needed: pdftotext (PDF), ebook-convert / calibre (epub/mobi/azw3/djvu), textutil (docx). Flag <200-word output as needs_ocr (scanned/image-only).
2. RE-WRAP long lines to ~180 chars so line-based reading is uniform.
3. SEGMENT by CHARACTER count: <=40,000 chars (~10k tokens) per segment, never by raw line/word count.
4. READ each segment (haiku is fine), each reports OK or EMPTY.
5. GRADE: a file is read_verified ONLY when every segment landed (got == total, fail == 0). Otherwise partial_read_only -> targeted re-read.
6. CONSOLIDATE in <=12 books per sonnet shelf, or raise shelf count, to avoid the 1M-context gate. Run waves ONE at a time (concurrent waves drain the session cap mid-run).

## Status taxonomy
read_verified / read_low_confidence (18-25k tok borderline) / partial_read_only / needs_ocr / needs_visual_review / needs_transcription / conversion_failed / not_read. OCR/visual/video is a separate pending pile, never counted as engaged.

## Reference implementation
/tmp/token_segment.py (re-wrap + char-cap segmenter), the os-engagement re-read workflow pattern (per-book coverage tracking + N-shelf sonnet consolidation). Pairs with the extraction-audit-gate and capability-growth memory rules.


## Inputs
- Large source file path: PDF, epub, mobi, azw3, djvu, docx, or long transcript (>~15k words)
- Conversion tools available: pdftotext (PDF), ebook-convert/calibre (epub/mobi), textutil (docx)
- Target segment size: <=40,000 chars per segment (never raw line/word count)

## Outputs
- Converted plain-text version of the source (re-wrapped to ~180 chars/line)
- Per-segment read results: each segment reports OK or EMPTY
- Coverage status from taxonomy: read_verified / read_low_confidence / partial_read_only / needs_ocr / needs_visual_review / needs_transcription / conversion_failed / not_read
- Consolidated distillation (<=12 books per sonnet shelf) once all segments land
- Receipt: '<filename> · <N> segments · got=<N> fail=<F> · status=read_verified' OR 'status=partial_read_only · re-read segments [list]'

## Gates
- read_verified gate: file is only read_verified when every segment landed (got == total, fail == 0) -- any fail = partial_read_only, triggers targeted re-read
- OCR/visual gate: <200-word output after conversion = needs_ocr flag, never counted as engaged
- Shelf-size gate: <=12 books per sonnet shelf -- raise shelf count rather than cramming, never run concurrent waves (they drain session cap mid-run)
- Char-count segmentation gate: segments by character count only, never by raw line/word count (epub/PDF long-line overflow fails silently)

## Test
- case: Operator runs /os-token-safe-reader on a 180-page epub of a canon book (~90k words). Skill converts via ebook-convert, re-wraps to 180 chars/line, segments into ~22 character-capped chunks of <=40k chars each, reads each with haiku, logs OK/EMPTY per segment. All 22 land. Consolidates distillation in 2 sonnet shelves. Receipt: 'canon_book.epub · 22 segments · got=22 fail=0 · status=read_verified · distilled to 2 shelves.'
- expected failure: A scanned PDF (image-only) is passed to the skill. pdftotext returns <200 words. Skill flags: 'status=needs_ocr · output too short for text extraction; likely scanned/image-only. Do not count as engaged. Separate OCR pass required.' Refuses to mark it read_verified.


## INVOKE WHEN
- engaging a source longer than ~15k words
- did we actually read the whole thing / prove coverage
- read the next batch of books / whole-read this PDF
