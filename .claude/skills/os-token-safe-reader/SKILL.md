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
