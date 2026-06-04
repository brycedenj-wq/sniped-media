# OS CERTIFICATION STANDARD v1 (2026-06-04)

> The verification framework, hard-reset. No more "engaged." A file/layer/doctrine is DONE only when the proof matches the file class. This is the law; `os_certify.py` enforces it; `OS_CERTIFICATION_LEDGER.csv` is the truth layer (the manifest `status` column is demoted to a raw read-signal).

## Why this exists
Repeated pattern: call it engaged -> find the metric weak -> patch -> a hidden class appears -> confidence drops. Root cause = the certification standard itself never matched file type. A 332k-word book and a 2k-word note both read "read_verified." This standard makes that impossible.

---

## 1. FILE CLASSES
`clean_text_doc` · `messy_raw_dump` · `transcript_dump` · `book` · `extracted_book_text` · `docx_source` · `pdf_source` · `ocr_scanned_source` · `visual_art_photo_book` · `video_audio_source` · `derivative` · `duplicate` · `mirror` · `generated_os_artifact`

## 2. PER-CLASS RULES
Notation: SEG = ceil(words/6700) ~ token-safe segments. LEDGER = a per-file record of segments_total and segments_read with offsets+checksums proving got==total.

| class | "read" means | "verified" means | proof required | countable in doctrine | allowed cert statuses |
|---|---|---|---|---|---|
| **clean_text_doc** | every segment read | got==total | SEG ledger (trivial if SEG<=2) | yes | certified / provisionally_verified |
| **messy_raw_dump** | boilerplate-strip + dedupe, THEN every segment read | 100% segment LEDGER (offsets+checksums) | full LEDGER; NEVER from samples | only the distilled doctrine that has LEDGER behind it | certified / characterized / sampled / pending_full_read |
| **transcript_dump** | timestamp-cleanup + dedupe, THEN every segment read | 100% segment LEDGER | full LEDGER; never from samples | only LEDGER-backed doctrine | certified / characterized / sampled / pending_full_read |
| **book** | full text read via its extracted twin | SEG coverage of the extracted text OR extraction-twin proof | extracted_twin + SEG LEDGER | yes if proof | certified / provisionally_verified / pending_full_read |
| **extracted_book_text** | the read artifact of its book; every segment read | SEG LEDGER | LEDGER | yes if proof | certified / provisionally_verified / pending_full_read |
| **docx_source** | converted text, every segment read | SEG LEDGER | LEDGER | yes if proof | certified / provisionally_verified / pending_full_read |
| **pdf_source** (text layer) | text-layer fully read | SEG LEDGER + confirmed text (not scanned) | LEDGER + text-presence check | yes if proof | certified / provisionally_verified / pending_full_read / pending_ocr |
| **ocr_scanned_source** | NOT readable as text | cannot be verified via extraction | OCR output + then SEG LEDGER | NO until OCR'd | pending_ocr |
| **visual_art_photo_book** | images carry meaning | cannot be verified via text | visual review record | NO via text | pending_visual_review |
| **video_audio_source** | spoken/au content | cannot be verified via text | transcription + then LEDGER | NO until transcribed | pending_transcription |
| **derivative** | n/a (not a source read) | dismissable only with SOURCE-LINEAGE proof (twin verified, or source queued not_read) | lineage proof (twin+md5/stem) | no (its source counts, not it) | derivative_confirmed / source_orphan |
| **duplicate** | n/a | md5 == another row | md5 + location | no | duplicate_confirmed |
| **mirror** | n/a | copy in another location of a counted file | md5/stem + location | no | duplicate_confirmed |
| **generated_os_artifact** | OS-authored (doctrine/dashboard/ledger/index/state) | n/a , not a source | author = OS | excluded from source coverage entirely | os_artifact |

## 3. METRICS (seven, never collapsed to one)
1. **file_count_coverage** , % files certified. SECONDARY (vanity metric; can hide giants).
2. **word_count_coverage** , % of content WORDS in certified files. PRIMARY.
3. **segment_coverage** , segments with a LEDGER / total segments.
4. **source_class_coverage** , per-class % certified (book, docx, raw_dump, … each reported separately).
5. **doctrine_confidence_coverage** , % of promoted doctrine whose source class is certified.
6. **capability_confidence_coverage** , % of capability claims backed by certified+tested sources.
7. **pending_risk_coverage** , word volume sitting in pending_* piles (the known-unknown mass).

## 4. HARD RULES (non-negotiable)
1. **No single percentage can represent the OS.** Always report all seven metrics.
2. **No giant file may hide inside file-count stats.** Word-volume is primary; any file >2 SEG is named.
3. **No derivative is dismissed without source-lineage proof.** md5 = identity, not derivation.
4. **No book is verified without SEG coverage OR extraction-twin proof.** A verified status alone is void.
5. **No raw dump / transcript is verified from distributed samples.** Samples = `characterized`, never `certified`.
6. **No visual / scanned / video source is counted as read via text extraction.** It is pending until OCR/visual/transcription.
7. **No doctrine is promoted without source-class confidence attached.** Every doctrine line carries its source's cert status.

## 5. STATUS TAXONOMY (the only allowed labels)
`certified` · `provisionally_verified` (read happened, no LEDGER) · `characterized` (distilled from partial/sample) · `sampled` · `pending_full_read` · `pending_ocr` · `pending_visual_review` · `pending_transcription` · `derivative_confirmed` · `duplicate_confirmed` · `source_orphan` · `unknown`.

- **certified** is reserved: clean_text_doc/book/docx/extracted with SEG<=2 (trivially full) OR any class with a true LEDGER.
- Multi-segment files with only a `read_verified` manifest status and no LEDGER are **provisionally_verified at best** , NOT certified.
- Raw dumps read from samples are **characterized**, never higher.

## 6. CERTIFICATION = (class rule satisfied) AND (proof artifact present) AND (status in allowed set). Anything else is a lower honest label. "Done" is illegal without certification for that class.
