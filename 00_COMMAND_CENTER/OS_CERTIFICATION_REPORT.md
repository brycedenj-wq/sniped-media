# OS CERTIFICATION REPORT v1 (2026-06-04)

> The truth, by `OS_CERTIFICATION_STANDARD.md`, enforced by `scripts/os_certify.py`, recorded in `OS_CERTIFICATION_LEDGER.csv` (3,877 rows). No optimizing to look good. No protecting prior claims. "Engaged" is retired; only "certified by file class, with proof."

## The seven metrics (never collapsed to one)
| # | metric | value |
|---|---|---|
| 1 | file-count coverage (SECONDARY/vanity) | certified 840 / 1,746 = **48.1%** |
| 2 | **WORD-VOLUME coverage (PRIMARY)** | **certified 4.4%** · provisional 82.0% · characterized 13.0% · pending 0.6% |
| 3 | segment coverage (LEDGER / total) | **~0%** , no per-file segment ledger exists yet for any multi-segment file |
| 4 | source-class coverage | see table below |
| 5 | doctrine-confidence coverage | NOT YET COMPUTED , requires tagging each doctrine line with its source cert (action #9) |
| 6 | capability-confidence coverage | NOT YET COMPUTED , same (action #9) |
| 7 | pending-risk coverage | 195,001 measured words + 44 OCR + 14 visual + 1 video files (no wordcount) |

The 48.1% file-count vs 4.4% word-volume gap is the proof of Hard Rule 2: giants hide in file counts.

## Metric 4 , source-class coverage (cert status by class)
| class | volume | cert breakdown |
|---|---|---|
| extracted_book_text | 25,460,013 w | certified 225 (small), **provisionally_verified 223 (the big books, no ledger)** |
| derivative | 17,679,963 w | derivative_confirmed 1,291 (lineage proven) |
| messy_raw_dump | 2,889,973 w | **characterized 5** (the giants), pending 1 |
| docx_source | 1,261,787 w | provisionally_verified 279, pending 5 |
| clean_text_doc | 926,023 w | **certified 614**, pending 17 |
| book (epub/mobi) | 0 w (volume in extracted twin) | provisionally_verified 157, pending_ocr 2, pending_visual 2 |
| pdf_source | 0 w | provisionally_verified 117, unknown 3 |
| ocr_scanned_source | 0 w | **pending_ocr 44** |
| visual_art_photo_book | 0 w | **pending_visual_review 14** |
| video_audio_source | 0 w | **pending_transcription 1** |
| generated_os_artifact | 390,654 w | os_artifact 73 (excluded from source coverage) |

## What is TRULY CERTIFIED right now
- **4.4% of content volume (1,351,227 words).** That is: 614 small clean authored docs + 225 small (<=2 segment) book extractions. These have trivially-full coverage. Use freely.
- The **campaign-house build (Phases 0-3)** is certified by a different proof , 90 passing tests , and is independent of corpus reads. Safe.

## What is only PROVISIONALLY trusted (do not certify, do not harden)
- **82% of content volume (25.0M words):** the big book layer (founder bios, photography canon, strategy/finance classics) + 279 docx sources. They were read/processed into the KB but have **no segment ledger**. Treat as "probably read, unproven." Usable as hypotheses with a `provisional` flag attached, never as settled fact.

## What is CHARACTERIZED only (weakest, never certify from this)
- **13% of content volume (3.96M words):** the 5 giant raw dumps (`series_1/2/3/5_intake`, `world building characters`) + the new "hot shit" doc. Distilled from distributed samples. Hard Rule 5 forbids certifying these without a full LEDGER read.

## What must be RE-READ (ranked by volume + risk)
1. The **158 giant files >10 segments = 24.84M words** that fail certification (the big books + giants). This is the dominant unproven mass.
2. The 5 raw-dump giants specifically (3.12M words) , full-read protocol.
3. The ~8M-word `not_read` docx source pile surfaced in Step 1.

## What must be OCR'd / visually reviewed / transcribed (cannot be read as text , Hard Rule 6)
- **OCR: 44 scanned sources + 32 ocr-mirrors** (`pending_ocr`).
- **Visual review: 14 photo/art books + 1** (`pending_visual_review`) , images carry the meaning.
- **Transcription: 1 video/audio** (`pending_transcription`).

## What strategy answers can SAFELY use
- The 4.4% certified content + the test-backed campaign-house system. Anything provable by code/test.

## What strategy answers CANNOT safely rely on
- Any claim resting on the 82% provisional book layer or the 13% characterized giants , i.e. most intellectual doctrine (Hit Makers, founder lessons, photography theory, the intake synthesis). These remain HYPOTHESES until certified. This matches the standing guardrails (proof decides, don't crown). Do not promote any doctrine to "settled" while its source is provisional/characterized.

## Corrected NEXT 10 REPAIR ACTIONS (in order)
1. **Adopt this standard as OS law** , `cert_status` (ledger) is the truth layer; demote manifest `status` to a raw read-signal. (DONE this turn.)
2. **Build the segment-LEDGER primitive** , a per-file record (segments_total, segments_read, byte offsets, per-segment checksum) and bake it into the token-safe reader so every future read emits certifiable proof. Nothing can become `certified` without it.
3. **CHEAP, do first:** audit whether the 60 KB `*_CHUNKS.jsonl` fully cover each book (chunk offsets vs file length). Where chunks prove full coverage, promote book provisional -> certified WITHOUT re-reading. This could certify a large share of the 25M-word book layer for near-zero cost.
4. **Re-read the 5 raw-dump giants** under the full-read protocol (characterized -> certified). 3.12M words.
5. **Read the ~8M-word `not_read` docx/source pile** (Step-1 surfaced) under the right per-class protocol.
6. **OCR** the 44 scanned + 32 ocr-mirror sources, then ledger them.
7. **Visual-review** the 14 photo/art books + 1.
8. **Transcribe** the 1 video/audio source.
9. **Compute metrics 5 & 6** , tag every doctrine + capability claim with its source cert status; flag and freeze any doctrine resting on characterized/provisional sources.
10. **Re-run `os_certify` after every wave**; always report all seven metrics; never publish a single percentage again.

## The new rule (locked)
No more "engaged" claims. A file/layer/doctrine is DONE only when `os_certify` labels it `certified` for its class, with proof. Everything else carries its honest lower label.
