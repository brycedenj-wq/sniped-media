# OS METHODOLOGY AUDIT (2026-06-04)

> Verifying that the verification process itself was valid. `read_verified` only ever proved a read did not truncate , it never proved a MESSY source was read with full segment coverage and distilled as a messy corpus. This audit weights coverage by CONTENT VOLUME, not file count, because file count hides the problem.

## Headline
- **By file count, 96.2% "verified" , by CONTENT VOLUME, only ~23% has methodology-appropriate proven coverage.**
- **5 files hold 76.6% of all measured verified content (3,122,870 words, ~470 token-safe segments) and have ZERO coverage ledger.** They were marked `read_verified` and almost certainly characterized, not fully read.
- The manifest never had a per-file coverage / read-method / file-type column, so full-coverage of any messy file was never provable. That gap is the root cause.

## 1. Corpus type breakdown (read_verified, by volume)
| type | files | % files | words | % volume |
|---|---|---|---|---|
| book_clean (epub/pdf/mobi/azw3/djvu) | 377 | 29.1% | (no wordcount recorded) | n/a |
| docish_clean (small authored .md/.docx) | 865 | 66.7% | 905,040 | 22.2% |
| docish_messy_single (1-segment messy) | 34 | 2.6% | 42,218 | 1.0% |
| code_config | 16 | 1.2% | 7,541 | 0.2% |
| **rawdump_unverified (giants)** | **5** | **0.4%** | **3,122,870** | **76.6%** |

## 2. Clean books/docs vs messy raw dumps
- Clean/appropriate by count: 377 books + 865 small docs + 34 single-segment messy + 16 code = **1,292 files**.
- Messy multi-segment raw dumps: **5 files** , but they are **76.6% of all measured content**. The corpus is a few enormous dumps wrapped in a cloud of small clean docs.

## 3. How many raw dumps were FULLY read (proven)?
- **Zero proven.** No segment-coverage ledger exists for the 5 giants. `series_2_intake.md` alone is ~178 segments; there is no record that all 178 landed. They were distilled into `OS_DOCTRINE_INTAKE_series_*` docs, but distillation-from-characterization is not full coverage.

## 4. How many were silently sampled/partial but marked verified?
- **The 5 giants** were marked `read_verified` with no coverage evidence , i.e. silently assumed full. Now re-statused to `rawdump_unverified`. (The one explicitly-partial file is the new "new hot shit .docx", already `partial_read_only`.)

## 5. Derivatives needing review (concern #6)
- 2,515 rows are class derivative / mirror / old-export and were removed from the read queue.
- **331 are LARGE (>=20k words).** They carry an md5 (proves identity) but **no content-ORIGIN proof** (md5 does not prove a file is a derivative of another). Some may be real source material wrongly dismissed. These need an origin-verification pass before staying dismissed.

## 6. Files that need re-read (priority queue)
1. `series_2_intake.md` (1.19M w, ~178 seg)
2. `series_3_intake.md` (919k w, ~138 seg)
3. `world building characters etc.docx` (422k w, ~64 seg)
4. `series_5_intake.md` (378k w, ~57 seg)
5. `series_1_intake.md` (216k w, ~33 seg)
- Then: origin-verify the 331 large derivatives (cheap , hash-compare + 1-segment spot read each).

## 7. Corrected confidence score
- **File-count "non-truncating read": 96.2%** (true, but measures the wrong thing).
- **Content-volume methodology-PROVEN coverage: ~23%.** The dominant 77% of measured content (the 5 giants) is characterized, not verified.
- Books (377) have no recorded word count, so their volume is asserted, not measured , lower-risk (clean linear text via token-safe segments) but not volume-proven either.
- **Honest statement going forward:** "1,210 files had a non-truncating read; ~23% of measured content is methodology-proven; ~470 segments across 5 giant raw dumps are unproven and queued for a full raw-dump-protocol read; 331 large derivatives await origin verification."

## 8. New protocol for messy sources (RAW-DUMP FULL-READ PROTOCOL)
A raw dump is NOT done until every segment is read or it is explicitly marked partial. Steps:
1. **Classify by type** (book_clean / docish_clean / rawdump) via `os_methodology_audit.py`.
2. **Boilerplate strip** , ad-reads, "use code X", sponsor segments, repeated CTAs.
3. **Timestamp + marker cleanup** , strip `0:00`, "From your search", "Sync to video time".
4. **Repeated-line dedupe** , collapse duplicate lines (this corpus had 8.6% dup lines).
5. **Segment + coverage proof** , re-wrap to ~180 char lines, segment <=40k chars, read EVERY segment, record segments_total and segments_read (got==total).
6. **Capability extraction** , skills/gates/workflows/tool-routes/money-patterns, not just notes.
7. **New vs reinforcing doctrine split** , label each finding REINFORCES or FRESH.
8. **Skill/gate/workflow harvest** , log candidates to the capability map.
- **New manifest columns (to add):** `file_type`, `read_method` (full/characterized/partial), `segments_total`, `segments_read`, `coverage_pct`. Until added, `rawdump_unverified` status carries the flag.
- **New dashboard categories (concern #7):** split `read_verified` into `read_verified_clean_doc` vs `read_verified_raw_dump` (only the latter requires the segment ledger). `os_methodology_audit.py report` already produces this split on demand.

## 9. Files needing re-audit
- The 5 giants (full raw-dump-protocol read).
- The 331 large derivatives (origin verification).
- A one-time word-count backfill for the 377 books so volume math includes them.

## 10. Are previous strategy answers safe, limited, or stale?
- **Production / the campaign-house build (Phases 0-3): SAFE.** It rests on code + 90 passing tests, not on corpus reads. Independent of this methodology gap.
- **Strategy / doctrine answers: LIMITED.** They synthesized from a corpus whose 77%-by-volume (the 5 giants) was characterized, not fully read. They are hypotheses, not verified conclusions , which is exactly why the standing guardrails (proof decides, don't crown a lane, possibility-engine) already apply. Do not harden any strategy claim that leans on the intake giants until they pass the raw-dump protocol.
- **The "96.6% engaged" claim: STALE / methodology-inflated.** Restate it per Section 7. The dashboard is only trustworthy when methodology matches file type.

## New rule (locked)
A messy file is not a lesser file. A raw dump is not auto-low-value. A transcript pile is not "done" unless every segment was read or it is explicitly marked partial. A derivative is not dismissed unless content-hash AND content-origin prove it derivative. A scrape is not useless until read enough to know what is inside. `read_verified` now means clean-doc-or-fully-covered only; messy multi-segment sources carry `rawdump_unverified` until the protocol is run.
