# NETWORK_DISTRIBUTION extraction log · 2026-05-25

## Sources

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `the_inevitable_kelly.txt` | The Inevitable | Kevin Kelly | epub | `raw/02_TIER_1_CANON_BOOKS/network_distribution/Kevin Kelly - The Inevitable_ Understanding the 12 Technological Forces That Will Shape Our Future (2016, Viking) - libgen.li.epub` | 108,050 |
| `new_rules_kelly.txt` | New Rules for the New Economy | Kevin Kelly | pdf | `raw/02_TIER_1_CANON_BOOKS/network_distribution/Kevin Kelly - New Rules for the New Economy_ 10 Radical Strategies for a Connected World (1999) - libgen.li.pdf` | 61,078 |
| `long_tail_anderson.txt` | The Long Tail | Chris Anderson | epub | `raw/02_TIER_1_CANON_BOOKS/network_distribution/Chris Anderson - Long Tail, The, Revised and Updated Edition_ Why the Future of Business is Selling Less of More (2008, Hyperion) - libgen.li.epub` | 75,305 |
| `free_anderson.txt` | Free: The Future of a Radical Price | Chris Anderson | pdf | `raw/02_TIER_1_CANON_BOOKS/network_distribution/Chris Anderson - Free_ The Future of a Radical Price (Abridged) (2009, Random House Business Books) - libgen.li.pdf` | 74,656 |
| `great_online_game_mccormick.txt` | The Great Online Game | Packy McCormick | pdf | `raw/02_TIER_1_CANON_BOOKS/network_distribution/XcMwr2sETldxuEwaZeEw_The+Great+Online+Game+-+Not+Boring+by+Packy+McCormick.pdf` | 4,343 |

## Method

- **Tools:** `pdftotext` (New Rules, Free, The Great Online Game) + `ebook-convert` (The Inevitable, The Long Tail). Both already on PATH.
- **No OCR. No new dependencies.** All five source files were read-only (not modified · mtimes unchanged).
- **Output:** `01_KNOWLEDGE_BASE/batches/network_distribution_extracted/` (5 .txt · 323,432 words total).
- **Note (The Great Online Game / McCormick):** a single ~4,343-word essay/newsletter ("Not Boring"), not a book; the 7.4 MB PDF is graphic-heavy. Used as the contemporary capstone reading (1 chunk), NOT padded to book weight. Content sanity confirmed before chunking.
- **Script:** `scripts/extract_network_distribution.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded / deferred (0 chunks · 0 extraction)

- **The Cold Start Problem (Andrew Chen):** ALREADY chunked in BATCH_002 (`network-effects` · 5 chunks) · NOT extracted, NOT re-chunked.
- **BROKEN:** Traction (Weinberg/Mares) · 0-byte empty epub in `operating_founder/` · re-acquire · NOT extracted (a future tactical-distribution addendum, different sub-register).
- **SNIPED-authored / operational docs:** `raw/13_NETWORK/access_and_community_architecture.md`, `The_Platform_Stack.docx`, `raw/14_WEB/website-seo/references/platform-ranking.md` · NOT books · out-of-scope · NOT extracted.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked. Held separately as a SPIRITUAL_FOUNDATION anchor.
- **Every already-canonical network-effects / distribution / advertising / media-business / operator / strategy source, every operating_founder / sales_positioning / decision_judgment / brand-canon / Tier-2 source, and CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** NOT extracted.

## Scope-guard note (5 sources · ~323,432 words)

Per the operator's scope guard, the lane is **representative network / distribution-economics pattern extraction, NOT a chapter-by-chapter internet-economy summary** · 16 curated chunks (incl. 1 synthesis · per-source The Inevitable 5 [4 + synthesis] / The Long Tail 4 / New Rules 3 / Free 3 / The Great Online Game 1), not a chapter walk.

## Result

- Sources in: 5 · extracted out: 5 · failures: 0.
- Ready for chunking (completed in the same ship · see `NETWORK_DISTRIBUTION_COMPLETE.md`).
