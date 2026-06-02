# OPERATING_FOUNDER_OPERATIONS extraction log · 2026-05-25

## Sources

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `the_goal_goldratt.txt` | The Goal | Eliyahu M. Goldratt | pdf | `raw/02_TIER_1_CANON_BOOKS/operating_founder/ Eliyahu, Goldratt - The goal_ a process of ongoing improvement (2004, North River Press) - libgen.li.pdf` | 143,658 |
| `reengineering_hammer_champy.txt` | Reengineering the Corporation | Michael Hammer and James Champy | pdf | `raw/02_TIER_1_CANON_BOOKS/operating_founder/ Michael Hammer_ James Champy - Reengineering the corporation ... (2001, HarperBusiness) - libgen.li.pdf` | 79,110 |
| `emyth_revisited_gerber.txt` | The E-Myth Revisited | Michael E. Gerber | mobi | `raw/02_TIER_1_CANON_BOOKS/operating_founder/Michael E. Gerber - The E-Myth Revisited_ ... (1995, HarperCollins) - libgen.li.mobi` | 66,283 |
| `built_to_sell_warrillow.txt` | Built to Sell | John Warrillow | pdf | `raw/02_TIER_1_CANON_BOOKS/operating_founder/John Warrillow - Built to Sell_ Turn Your Business Into One You Can Sell (2010) - libgen.li.pdf` | 38,682 |

## Method

- **Tools:** `pdftotext` (The Goal, Reengineering, Built to Sell) + `ebook-convert` (The E-Myth Revisited mobi). Both already on PATH.
- **No OCR. No new dependencies.** All four source files were read-only (not modified · 2026-05-16/17 mtimes unchanged).
- **Output:** `01_KNOWLEDGE_BASE/batches/operating_founder_operations_extracted/` (4 .txt · 327,733 words total).
- **Note (The Goal / Built to Sell):** `file` reported low page-counts (a PDF-metadata quirk); both extracted full real text (The Goal = 143,658 words of the TOC manufacturing novel; Built to Sell = 38,682 words of the parable). Confirmed content sanity before chunking.
- **Script:** `scripts/extract_operating_founder_operations.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded / deferred (0 chunks · 0 extraction)

- **OPERATING_FOUNDER_STARTUP sources (already canonical):** The Lean Startup, The Hard Thing About Hard Things, The Founder's Dilemmas · NOT extracted.
- **OPERATING_FOUNDER_SCALING sources (already canonical):** Blitzscaling, Amp It Up · NOT extracted.
- **BROKEN:** Traction (Weinberg/Mares) · 0-byte empty epub · re-acquire · NOT extracted.
- **OUT-OF-SCOPE / misfiled in the folder:** The 88 Laws of the Masculine Mindset (Winters · self-help) + Moonwalk (Michael Jackson · music memoir) · NOT operating-founder · NOT extracted.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked. Held separately as a SPIRITUAL_FOUNDATION anchor.
- **Every already-canonical founder/operator/strategy/classical/history source, every network_distribution / sales_positioning / decision_judgment / brand-canon / Tier-2 source, and CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** NOT extracted.

## Scope-guard note (4 systems/process books)

The 4 sources total ~327,733 words. Per the operator's scope guard, the lane is **representative operations / operator-system pattern extraction, NOT a chapter-by-chapter business-book summary** · 14 curated chunks (incl. 1 synthesis · per-source The Goal 5 / Reengineering 3 / E-Myth 3 / Built to Sell 3), not a chapter walk.

## Result

- Sources in: 4 · extracted out: 4 · failures: 0.
- Ready for chunking (completed in the same ship · see `OPERATING_FOUNDER_OPERATIONS_COMPLETE.md`).
