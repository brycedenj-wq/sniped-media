# CLASSICAL_STRATEGY extraction log · 2026-05-24

## Sources

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `the_prince_machiavelli.txt` | The Prince | Niccolo Machiavelli | pdf | `raw/02_TIER_1_CANON_BOOKS/strategy_history/Niccolo Machiavelli - The prince (2008, Hackett Pub. Co) - libgen.li.pdf` | 140,507 |
| `on_war_clausewitz.txt` | On War | Carl von Clausewitz | pdf | `raw/02_TIER_1_CANON_BOOKS/strategy_history/[Oxford World's Classics] Carl von Clausewitz, Beatrice Heuser - On War (2007, ...) - libgen.li.pdf` | 115,527 |
| `meditations_marcus_aurelius.txt` | Meditations | Marcus Aurelius | epub | `raw/02_TIER_1_CANON_BOOKS/strategy_history/Marcus Aurelius - Meditations - libgen.li.epub` | 154,648 |
| `landmark_caesar.txt` | The Landmark Julius Caesar (Web Essays) | Robert B. Strassler (ed.) | pdf | `raw/02_TIER_1_CANON_BOOKS/strategy_history/LandmarkCaesarWebEssays_5Jan2018.pdf` | 187,008 |

## Method

- **Tools:** `pdftotext` (The Prince, On War, Landmark Caesar) + `ebook-convert` (Meditations epub). Both already on PATH.
- **No OCR. No new dependencies.** All four source files were read-only (not modified).
- **Output:** `01_KNOWLEDGE_BASE/batches/classical_strategy_extracted/` (4 .txt · 597,690 words total).
- **Script:** `scripts/extract_classical_strategy.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded (0 chunks · 0 extraction)

- **Art of War (Sun Tzu):** already chunked in BATCH_002 (source_title "The Art of War") · NOT extracted.
- **The 48 Laws of Power + The 33 Strategies of War (Greene):** already chunked in BATCH_002 · NOT extracted.
- **The Book of Five Rings (Musashi):** `.djvu` (unsupported · no djvutxt) · NOT extracted.
- **Discourses on Livy (Machiavelli), Napoleon: A Life (Roberts), The Landmark Herodotus, The Landmark Thucydides, The Campaigns of Alexander (Arrian), Alexander logistics (Engels), the Greene trio (Laws of Human Nature / Mastery / 50th Law):** DEFERRED to subsequent classical lanes (CLASSICAL_HISTORY etc.) · NOT extracted here.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked. (Meditations is treated as a secular Stoic leadership/mindset text, not scripture; no faith lane created.)
- **Every operating_founder / network_distribution / sales_positioning / decision_judgment / brand-canon / Tier-2 source:** NOT extracted (this is only the first lane of the sequenced canon).

## Scope-guard note (large, dense classical sources)

Combined ~597,690 words across 4 dense classical texts. Per the operator's scope guard, the lane is **representative strategy/operator-pattern extraction, NOT exhaustive summary or political theory** · 18 curated chunks (Prince 4, On War 4, Meditations 4, Caesar 4, + 2 synthesis), not chapter-by-chapter coverage. The Landmark Caesar pdf is the freely-published Web Essays companion (interpretive essays + Caesar's own works framing), not the full printed volume; chunks draw on the essays' analysis of Caesar's command, clemency, risk-taking, and the Commentaries-as-self-narrative.

## Result

- Sources in: 4 · extracted out: 4 · failures: 0.
- Ready for chunking (completed in the same ship · see `CLASSICAL_STRATEGY_COMPLETE.md`).
