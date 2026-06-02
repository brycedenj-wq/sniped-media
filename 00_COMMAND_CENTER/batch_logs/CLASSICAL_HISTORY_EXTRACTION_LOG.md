# CLASSICAL_HISTORY extraction log · 2026-05-24

## Sources

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `herodotus_histories.txt` | The Landmark Herodotus: The Histories | Herodotus (Robert B. Strassler, ed.) | epub | `raw/02_TIER_1_CANON_BOOKS/strategy_history/Herodotus, Robert B. Strassler[ed] - The Landmark Herodotus_ Histories (2007, 2009, Anchor Books) - libgen.li.epub` | 437,842 |
| `thucydides_peloponnesian_war.txt` | The Landmark Thucydides: The Peloponnesian War | Thucydides (Robert B. Strassler, ed.) | epub | `raw/02_TIER_1_CANON_BOOKS/strategy_history/Thucydides, Robert B. Strassler, Richard Crawley, Victor Davis H - The Landmark Thucydides_ ... (1998, Free Press) - libgen.li.epub` | 352,171 |
| `arrian_campaigns_of_alexander.txt` | The Campaigns of Alexander | Arrian | azw3 | `raw/02_TIER_1_CANON_BOOKS/strategy_history/[Classics] Arrian - The Campaigns of Alexander (2003, Penguin Books Ltd) - libgen.li.azw3` | 132,066 |
| `engels_macedonian_logistics.txt` | Alexander the Great and the Logistics of the Macedonian Army | Donald W. Engels | pdf | `raw/02_TIER_1_CANON_BOOKS/strategy_history/Donald W. Engels - Alexander the Great and the Logistics of the Macedonian Army (2020, University of California Press) [10.1525_9780520352162] - libgen.li.pdf` | 75,419 |

## Method

- **Tools:** `ebook-convert` (Herodotus epub, Thucydides epub, Arrian azw3) + `pdftotext` (Engels pdf). Both already on PATH.
- **No OCR. No new dependencies.** All four source files were read-only (not modified).
- **Engels 44 MB pdf** has a real text layer (75,419 words extracted cleanly); the file size is embedded maps/figures, not image-only scans. No OCR needed.
- **Output:** `01_KNOWLEDGE_BASE/batches/classical_history_extracted/` (4 .txt · 997,498 words total).
- **Script:** `scripts/extract_classical_history.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded / deferred (0 chunks · 0 extraction)

- **Napoleon: A Life (Andrew Roberts):** DEFERRED to a modern-command lane (HISTORICAL_BIOGRAPHY-adjacent) · a modern (2014) command biography, register-wise closer to Chernow's Grant/Washington than to ancient primary histories · NOT extracted.
- **Discourses on Livy (Machiavelli):** DEFERRED to a political-theory pass (CLASSICAL_STRATEGY-adjacent) · the republican-strategy companion to The Prince · belongs with the strategy treatises, NOT the histories · NOT extracted.
- **Art of War (Sun Tzu), The 48 Laws of Power + The 33 Strategies of War (Greene):** already chunked in BATCH_002 · NOT extracted.
- **The Book of Five Rings (Musashi):** `.djvu` (unsupported · no djvutxt) · NOT extracted (a CLASSICAL_STRATEGY exclusion, not part of this lane).
- **The Prince / On War / Meditations / Landmark Caesar:** already chunked in CLASSICAL_STRATEGY (`d1bb701`) · NOT extracted.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked. Held separately as a SPIRITUAL_FOUNDATION anchor.
- **Every operating_founder / network_distribution / sales_positioning / decision_judgment / brand-canon / Tier-2 source, and CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** NOT extracted (this is only the second lane of the sequenced canon).

## Scope-guard note (huge primary histories)

Combined ~997,498 words across 4 huge ancient histories (the two Landmark Greek histories alone are ~790,000 words). Per the operator's scope guard, the lane is **representative strategy / power / culture / logistics pattern extraction, NOT exhaustive history summary or ancient-world survey** · 18 curated chunks (Herodotus 4, Thucydides 5, Arrian 4, Engels 3, + 2 synthesis), not chapter-by-chapter retelling of the histories.

## Result

- Sources in: 4 · extracted out: 4 · failures: 0.
- Ready for chunking (completed in the same ship · see `CLASSICAL_HISTORY_COMPLETE.md`).
