# DECISION_JUDGMENT_MEANING extraction log · 2026-05-25

## Sources

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `mans_search_for_meaning_frankl.txt` | Man's Search for Meaning | Viktor E. Frankl | pdf | `raw/03_TIER_2_CANON_BOOKS/decision_judgment/Viktor E. Frankl - Man's search for meaning (2000, Beacon Press) - libgen.li.pdf` | 47,250 |
| `games_people_play_berne.txt` | Games People Play | Eric Berne | epub | `raw/03_TIER_2_CANON_BOOKS/decision_judgment/Eric Berne - Games People Play_ The Basic Handbook of Transactional Analysis. (1996, Ballantine Books) - libgen.li.epub` | 50,273 |

## Method

- **Tools:** `pdftotext` (Man's Search for Meaning pdf) + `ebook-convert` (Games People Play epub). Both already on PATH.
- **No OCR. No new dependencies.** Both source files were read-only (not modified · mtimes unchanged).
- **Output:** `01_KNOWLEDGE_BASE/batches/decision_judgment_meaning_extracted/` (2 .txt · 97,523 words total).
- **Source selection:** the 2 net-new meaning/interaction-register sources from the DECISION_JUDGMENT_PLAN's deferred DECISION_JUDGMENT_MEANING sub-lane (the last of the three DECISION_JUDGMENT sub-lanes). Content sanity confirmed before chunking (the last of the human freedoms / logotherapy / will to meaning / tragic optimism in Frankl; Parent/Adult/Child / transactional analysis / games / ulterior transactions / payoff in Berne).
- **Script:** `scripts/extract_decision_judgment_meaning.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Sensitivity note (2 philosophically/clinically adjacent sources)

These are handled with care per the operator's guardrails: **Frankl is treated with dignity, NOT reduced to hustle or motivation content** (the suffering/meaning material is framed soberly, grounded in his survival of the camps); **Berne is translated as interpersonal-pattern awareness, NOT armchair diagnosis or a tool for labeling people** (ego states and games are read as patterns to notice in interactions, including one's own). The lane does NOT become therapy, religion, self-help, or psychological diagnosis.

## Excluded / deferred (0 chunks · 0 extraction)

- **DECISION_JUDGMENT_COGNITION sub-lane (already canonical):** Thinking, Fast and Slow, Noise · NOT extracted.
- **DECISION_JUDGMENT_CROWDS sub-lane (already canonical):** The Righteous Mind, The Coddling of the American Mind, The True Believer, The Crowd · NOT extracted.
- **STORYTELLING_NARRATIVE (separate future lane):** The Anatomy of Story (Truby), The Hero with a Thousand Faces (Campbell), Save the Cat! (Snyder) · NOT extracted.
- **BROKEN:** The Denial of Death (Becker · djvu, unsupported) + Story (McKee · 53MB scanned pdf, 0 text) · re-acquire · NOT extracted.
- **Predictably Irrational (Ariely):** already canonical in PERSUASION_RECOVERY · NOT re-chunked.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked · held SPIRITUAL_FOUNDATION anchor.
- **Every already-canonical persuasion/positioning/operator/classical source, every storytelling/narrative source, and CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** NOT extracted.

## Scope-guard note (2 sources · ~97,523 words)

Per the operator's scope guard, the lane is **representative meaning / agency / interpersonal-pattern extraction, NOT a therapy summary or psychological diagnosis** · 9 curated chunks (incl. 1 synthesis · per-source Man's Search for Meaning 5 [4 + synthesis] / Games People Play 4), not a chapter walk.

## Result

- Sources in: 2 · extracted out: 2 · failures: 0.
- Ready for chunking (completed in the same ship · see `DECISION_JUDGMENT_MEANING_COMPLETE.md`).
