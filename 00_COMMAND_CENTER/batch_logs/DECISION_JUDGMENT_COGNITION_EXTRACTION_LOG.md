# DECISION_JUDGMENT_COGNITION extraction log · 2026-05-25

## Sources

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `thinking_fast_and_slow_kahneman.txt` | Thinking, Fast and Slow | Daniel Kahneman | mobi | `raw/03_TIER_2_CANON_BOOKS/decision_judgment/Daniel Kahneman - Thinking, Fast and Slow (2011, Farrar, Straus and Giroux) - libgen.li.mobi` | 190,774 |
| `noise_kahneman_sibony_sunstein.txt` | Noise: A Flaw in Human Judgment | Daniel Kahneman, Olivier Sibony, Cass R. Sunstein | pdf | `raw/03_TIER_2_CANON_BOOKS/decision_judgment/Sunstein, Cass R._ Sibony, Olivier_ Kahneman, Daniel - Noise_ A Flaw in Human Judgment (2021, Little, Brown and Company) - libgen.li.pdf` | 133,394 |

## Method

- **Tools:** `ebook-convert` (Thinking, Fast and Slow mobi) + `pdftotext` (Noise pdf). Both already on PATH.
- **No OCR. No new dependencies.** Both source files were read-only (not modified · mtimes unchanged).
- **Output:** `01_KNOWLEDGE_BASE/batches/decision_judgment_cognition_extracted/` (2 .txt · 324,168 words total).
- **Source selection:** the 2 net-new cognition-register sources from the DECISION_JUDGMENT_PLAN's recommended FIRST sub-lane (DECISION_JUDGMENT_COGNITION). Content sanity confirmed before chunking (System 1/2, anchoring, base rates, prospect theory in Kahneman; noise vs bias, level/pattern/occasion noise, decision hygiene, mediating assessments in Noise).
- **Script:** `scripts/extract_decision_judgment_cognition.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded / deferred (0 chunks · 0 extraction)

- **DECISION_JUDGMENT_CROWDS sub-lane (deferred):** The Righteous Mind, The Coddling of the American Mind (Haidt), The True Believer (Hoffer), The Crowd (Le Bon) · NOT extracted.
- **DECISION_JUDGMENT_MEANING sub-lane (deferred):** Man's Search for Meaning (Frankl), Games People Play (Berne) · NOT extracted.
- **STORYTELLING_NARRATIVE (separate future lane):** The Anatomy of Story (Truby), The Hero with a Thousand Faces (Campbell), Save the Cat! (Snyder) · NOT extracted.
- **BROKEN:** The Denial of Death (Becker · djvu, unsupported) + Story (McKee · 53MB scanned pdf, 0 extractable text) · re-acquire · NOT extracted.
- **Predictably Irrational (Ariely):** already canonical in PERSUASION_RECOVERY (not in this folder) · NOT re-chunked.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked · held SPIRITUAL_FOUNDATION anchor.
- **Every already-canonical persuasion/positioning/operator/classical source, and CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** NOT extracted.

## Scope-guard note (2 sources · ~324,168 words)

Per the operator's scope guard, the lane is **representative cognition / judgment pattern extraction, NOT a chapter-by-chapter psychology summary** · 12 curated chunks (incl. 1 synthesis · per-source Thinking, Fast and Slow 8 [7 + synthesis] / Noise 4), not a chapter walk of two dense ~150-190K-word books.

## Result

- Sources in: 2 · extracted out: 2 · failures: 0.
- Ready for chunking (completed in the same ship · see `DECISION_JUDGMENT_COGNITION_COMPLETE.md`).
