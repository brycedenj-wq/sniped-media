# BOOK-LAYER CERTIFICATION AUDIT , PLAN (2026-06-04)

> NOT a re-read. A cheap, LOCAL check to answer one question: were the books certified like `start here` (segment-ledger coverage), or were they only CHUNKED (KB concept-distillation)? The honest prior, from the certification work: **chunked, not certified** , but prove it per book, then classify.

## The distinction that decides everything
- **start-here coverage** = `os_segment_ledger` partition (contiguous, checksummed) + every segment READ. That is certification.
- **KB chunking** = `batches/*_CHUNKS.jsonl` = concept-summaries (chunk_id, source_file, summary, principle). A book chunked into 30 concept-chunks does NOT prove all its text was read , chunking distills, it can skip. **Chunks are evidence, not coverage proof.**
So the default verdict is: the 25M-word book layer is `provisionally_verified` (chunked + read-claimed, NO segment ledger), not `certified`. This audit confirms per book and finds any exceptions.

## What to RUN (cheap, local, no spend , build `scripts/os_book_coverage.py`)
For every book (its `extracted_book_text` twin carries the real size):
1. `extracted_words`, `segments_equiv = ceil(words/6700)`.
2. `has_segment_ledger?` , does `_segments/<book>/LEDGER.csv` exist with full read? (Today: NO for all books , only start-here has ledgers.)
3. `chunk_count` for the book (grep `source_file` across `*_CHUNKS.jsonl`) and `chunk_coverage_estimate` = does the chunk set span the whole text? (compare chunk count to segments_equiv; chunks << segments ⇒ distilled, not covered).
4. `certified_twin?` , is this book's content also in a CERTIFIED folder (like start-here)? (twin coverage).
5. `class` , text-book / scanned (pending_ocr) / photo-art (pending_visual).

## Classification buckets (the output)
- **coverage-proven** , has a segment ledger OR a certified twin. (Today: only books whose content is in `start here`, e.g. the giants. Expect very few.)
- **extracted/chunked but NOT certified** , has extracted text + KB chunks, no ledger. (Expect: the bulk , ~the 25M-word layer. This is `provisionally_verified`, honestly.)
- **provisionally trusted** , same as above; usable as hypotheses with the `provisional` tag, never settled fact.
- **OCR / visual** , scanned PDFs / photo-art books (`pending_ocr` 44, `pending_visual_review` 14). Cannot be certified via text (Hard Rule 6).
- **needs re-read** , big text books where chunk-span is far below segments_equiv (chunking clearly skipped) AND no twin , these need a segment-ledger pass to ever be certified.

## The decision rule (per book)
- segment ledger present, full → **certified**.
- certified twin (start-here etc.) → **coverage-proven (twin)**.
- chunks span ≈ full text (chunk_count close to segments_equiv, contiguous source offsets) → candidate **promote-to-certified-via-chunk** (only if the chunker recorded offsets proving span; if it only has summaries, it does NOT qualify).
- else, text book → **provisional / needs-reread** (rank by word volume).
- scanned/photo → **pending_ocr / pending_visual**.

## Expected answer (state plainly after running)
Almost certainly: **the books were CHUNKED, not certified.** KB chunks are concept-distillations without coverage offsets, so they cannot prove full-text coverage under the standard. The book layer stays `provisionally_verified` until either (a) a future `os_book_coverage` run shows chunk-span actually tiles a given book, or (b) a segment-ledger re-read. This audit just makes that per-book and honest , it does NOT re-read.

## Order (when authorized , NOT now)
1. Build `scripts/os_book_coverage.py` (the local computation above). Cheap.
2. Run it → produce `OS_BOOK_COVERAGE_LEDGER.csv` (per book: words, segments_equiv, chunk_count, ledger?, twin?, bucket).
3. Report the 5 buckets by count AND word-volume (volume primary).
4. Only then decide which books (if any) warrant a segment-ledger re-read , ranked by volume, smallest-cost-highest-value first.

## Guardrails
No re-read in this plan. No strategy. The cert ledger remains the redo gate. The 25M-word book layer is NOT upgraded by this plan , it only gets classified honestly so we know what "certifying the books" would actually require.
