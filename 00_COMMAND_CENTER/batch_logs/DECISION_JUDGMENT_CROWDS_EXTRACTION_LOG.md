# DECISION_JUDGMENT_CROWDS extraction log · 2026-05-25

## Sources

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `righteous_mind_haidt.txt` | The Righteous Mind | Jonathan Haidt | azw3 | `raw/03_TIER_2_CANON_BOOKS/decision_judgment/Jonathan Haidt - The Righteous Mind_ ... (2012, Pantheon) - libgen.li.azw3` | 137,786 |
| `coddling_lukianoff_haidt.txt` | The Coddling of the American Mind | Greg Lukianoff and Jonathan Haidt | pdf | `raw/03_TIER_2_CANON_BOOKS/decision_judgment/Greg Lukianoff, Jonathan Haidt - The Coddling of the American Mind_ ... (2018, Penguin Press) - libgen.li.pdf` | 119,516 |
| `true_believer_hoffer.txt` | The True Believer | Eric Hoffer | epub | `raw/03_TIER_2_CANON_BOOKS/decision_judgment/Eric Hoffer - The true believer_ ... (1980, Time-Life Books) - libgen.li.epub` | 48,694 |
| `the_crowd_lebon.txt` | The Crowd | Gustave Le Bon | pdf | `raw/03_TIER_2_CANON_BOOKS/decision_judgment/Gustave Le Bon - The crowd_ a study of the popular mind (2001, Dover Publications) - libgen.li.pdf` | 56,662 |

## Method

- **Tools:** `ebook-convert` (The Righteous Mind azw3, The True Believer epub) + `pdftotext` (The Coddling of the American Mind pdf, The Crowd pdf). Both already on PATH.
- **No OCR. No new dependencies.** All four source files were read-only (not modified · mtimes unchanged).
- **Output:** `01_KNOWLEDGE_BASE/batches/decision_judgment_crowds_extracted/` (4 .txt · 362,658 words total).
- **Source selection:** the 4 net-new crowds/social-belief-register sources from the DECISION_JUDGMENT_PLAN's deferred DECISION_JUDGMENT_CROWDS sub-lane. Content sanity confirmed before chunking (moral foundations / elephant-and-rider in Haidt; great untruths / antifragility / safetyism in Coddling; mass movements / the frustrated / men of words in Hoffer; the crowd / contagion / prestige in Le Bon).
- **Script:** `scripts/extract_decision_judgment_crowds.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded / deferred (0 chunks · 0 extraction)

- **DECISION_JUDGMENT_COGNITION sub-lane (already canonical):** Thinking, Fast and Slow, Noise · NOT extracted.
- **DECISION_JUDGMENT_MEANING sub-lane (deferred):** Man's Search for Meaning (Frankl), Games People Play (Berne) · NOT extracted.
- **STORYTELLING_NARRATIVE (separate future lane):** The Anatomy of Story (Truby), The Hero with a Thousand Faces (Campbell), Save the Cat! (Snyder) · NOT extracted.
- **BROKEN:** The Denial of Death (Becker · djvu, unsupported) + Story (McKee · 53MB scanned pdf, 0 text) · re-acquire · NOT extracted.
- **Predictably Irrational (Ariely):** already canonical in PERSUASION_RECOVERY · NOT re-chunked.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked · held SPIRITUAL_FOUNDATION anchor.
- **Every already-canonical persuasion/positioning/operator/classical source, every storytelling/narrative source, and CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** NOT extracted.

## Sensitivity / scope-guard note (4 large, ideologically-charged sources · ~362,658 words)

Per the operator's scope guard, the lane is **representative crowds / moral-psychology / social-belief pattern extraction, NOT a chapter-by-chapter politics/culture-war summary** · 14 curated chunks (incl. 1 synthesis · per-source Righteous Mind 5 [4 + synthesis] / Coddling 4 / True Believer 3 / The Crowd 2). The material is held **descriptively** (to read and navigate group/belief/incentive dynamics) and explicitly **NOT as a manipulation playbook or a culture-war stance** · Le Bon's prestige/contagion mechanics (chunks 012, 013) are framed as defensive awareness, not a how-to. No political side is taken.

## Result

- Sources in: 4 · extracted out: 4 · failures: 0.
- Ready for chunking (completed in the same ship · see `DECISION_JUDGMENT_CROWDS_COMPLETE.md`).
