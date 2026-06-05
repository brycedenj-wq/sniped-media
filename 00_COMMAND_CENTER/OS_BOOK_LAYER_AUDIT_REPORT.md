# BOOK-LAYER CERTIFICATION AUDIT , REPORT (2026-06-04)

> Cheap, local, no re-reads. The question: were the books certified to the segment-ledger standard, or only extracted/chunked? **Answer, with proof: they were CHUNKED (concept-distilled), NOT certified.** Ledger: `OS_BOOK_COVERAGE_LEDGER.csv`.

## THE CLEAR ANSWER
- The KB chunks carry fields `concept / summary / usable_principle / direct_quotes` , and **NO `start/end/offset/segment` field.** A chunk is one distilled principle, not a text segment. **Average 4.7 chunks per book.** A 300k-word book represented by ~5 concept-chunks is distillation, not coverage.
- **Certified (segment-ledger coverage): ~0 classic books.** Only 19 extracted texts (5.6% by volume) have a ledger , and those are the start-here giants just processed, not the book canon.
- **The entire classic book layer = `chunked_not_certified` = 215 texts = 20.94M words = 93.6% by volume.** Provisional. Not certified. Not done to this standard.

## The 10 answers
1. **Total book count:** 667 source format-files (`.epub` 278, `.pdf` 310, `.mobi` 47, `.azw3` 19, `.djvu` 12, `.doc` 1) → ~240 distinct extracted-content books (**22,369,616 words**).
2. **Exact paths:** in `OS_ENGAGEMENT_MANIFEST.csv` (source files) + `OS_BOOK_COVERAGE_LEDGER.csv` (per extracted text).
3. **Have extracted text:** 240 extracted texts (the content units).
4. **Have chunks:** 215 (concept-chunked), avg 4.7 chunks each; 1,879 chunks total across 60 `*_CHUNKS.jsonl`.
5. **Real coverage proof:** **19 texts (1.25M words, 5.6%)** , and these are start-here giants, not the book canon. Classic books with coverage proof: effectively **0**.
6. **Only chunk/distillation evidence:** **215 texts (20.94M words, 93.6%)** , the real book layer.
7. **OCR / visual / scanned:** 66 source files `needs_ocr`, 5 `needs_visual_review` (cannot be certified via text , Hard Rule 6).
8. **Duplicates / alternate formats:** 6 manifest-flagged duplicates + multi-format titles (same book as epub+mobi+azw3); dedupe by title, certify once.
9. **Need a real re-read:** **191 extracted texts (21.0M words)** are >2 segments and unproven , a segment-ledger pass is the only path to certified for these.
10. **Status by file-count AND word-volume:**

| bucket | files | word-volume |
|---|---|---|
| coverage_proven (ledger/twin) | 19 | 1,246,695 (5.6%) |
| **chunked_not_certified (provisional)** | **215** | **20,943,721 (93.6%)** |
| extracted_only_provisional (not even chunked) | 6 | 179,200 (0.8%) |
| pending: needs_ocr | 66 src | (not extracted) |
| pending: needs_visual_review | 5 src | (images carry meaning) |
| pending: not_read source files | 213 src | (never extracted) |
| duplicate/alt-format | 6+ | (covered by twin) |

## VERDICT (per your taxonomy)
- **certified:** ~0 classic books (only start-here giants have ledgers).
- **chunked (provisional):** 215 texts / 20.94M words , the book canon. Usable as hypotheses with a `provisional` tag, never settled fact. Do NOT call these certified.
- **pending:** 66 OCR + 5 visual + 213 not-read source files.
- The 96.6%-"engaged" and any "books are done" claim was **chunking, mislabeled as coverage.** Confirmed.

## RECOMMENDED REPAIR PLAN (ranked by leverage / cost , do NOT execute yet)
**Principle: do NOT re-read 21M words wholesale.** Most are founder bios / classics with diluted per-word value already distilled into chunks. Spend only where doctrine actually leans.
1. **Cheapest, do first , dedupe + classify (local, $0):** collapse multi-format duplicates; confirm the 19 ledgered texts; tag all 215 chunked texts `provisional` in the manifest so nothing reads as certified. No reads.
2. **OCR the 66 scanned + visual-review the 5 (only if doctrine needs them):** triage which are SNIPED-relevant (photography/lighting canon) vs generic; OCR only the relevant subset, then ledger.
3. **Selective certification by doctrine-dependency (highest leverage):** identify the small set of books the active OS doctrine actually cites (photo theory, the few that feed certified doctrine). Re-read ONLY those under the segment-ledger protocol. Likely <20 books.
4. **Small books cheap win:** any extracted text ≤2 segments → certify with a 1-pass ledger (trivial, near-free).
5. **Leave the long tail provisional, labeled:** the bulk of bios/classics stay `chunked_not_certified` + `provisional`. They are reference, not law. Re-read only on demand when a task depends on one.
6. **Never bulk-workflow the 21M words** until steps 1-4 prove a specific, bounded subset is worth it. The audit says: targeted, not wholesale.

## What this changes on the dashboard
The book layer is restated honestly: **certified ~5.6% by volume (start-here giants), chunked-provisional 93.6%, plus OCR/visual/not-read pending.** No book canon is certified. See the cert-report delta.
