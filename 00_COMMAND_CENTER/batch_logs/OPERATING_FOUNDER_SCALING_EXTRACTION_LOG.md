# OPERATING_FOUNDER_SCALING extraction log · 2026-05-25

## Sources

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `blitzscaling_hoffman_yeh.txt` | Blitzscaling | Reid Hoffman and Chris Yeh | epub | `raw/02_TIER_1_CANON_BOOKS/operating_founder/[Blitzscaling] Reid Hoffman, Chris Yeh, Bill Gates - Blitzscaling_ ... (2018, Currency) - libgen.li.epub` | 86,784 |
| `amp_it_up_slootman.txt` | Amp It Up | Frank Slootman | pdf | `raw/02_TIER_1_CANON_BOOKS/operating_founder/Amp It Up{Frank Slootman}(2022, Wiley){112881352} libgen.li.pdf` | 49,597 |

## Method

- **Tools:** `ebook-convert` (Blitzscaling epub) + `pdftotext` (Amp It Up pdf). Both already on PATH.
- **No OCR. No new dependencies.** Both source files were read-only (not modified · 2026-05-16 mtimes unchanged).
- **Output:** `01_KNOWLEDGE_BASE/batches/operating_founder_scaling_extracted/` (2 .txt · 136,381 words total).
- **Script:** `scripts/extract_operating_founder_scaling.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded / deferred (0 chunks · 0 extraction)

- **OPERATING_FOUNDER_STARTUP sources (already canonical):** The Lean Startup, The Hard Thing About Hard Things, The Founder's Dilemmas · NOT extracted.
- **Deferred to OPERATING_FOUNDER_OPERATIONS:** The Goal (Goldratt), Reengineering the Corporation (Hammer/Champy), The E-Myth Revisited (Gerber), Built to Sell (Warrillow) · NOT extracted.
- **BROKEN:** Traction (Weinberg/Mares) · 0-byte empty epub · re-acquire · NOT extracted.
- **OUT-OF-SCOPE / misfiled in the folder:** The 88 Laws of the Masculine Mindset (Winters · self-help) + Moonwalk (Michael Jackson · music memoir) · NOT operating-founder · NOT extracted.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked. Held separately as a SPIRITUAL_FOUNDATION anchor.
- **Every already-canonical founder/operator/strategy/classical/history source, every network_distribution / sales_positioning / decision_judgment / brand-canon / Tier-2 source, and CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** NOT extracted.

## Scope-guard note (2 hypergrowth/intensity books)

The 2 sources total ~136,381 words. Per the operator's scope guard, the lane is **representative scaling / operator-tempo pattern extraction, NOT a chapter-by-chapter summary** · 11 curated chunks (incl. 1 synthesis · per-source Blitzscaling 6 / Amp It Up 5), not a chapter walk.

## Result

- Sources in: 2 · extracted out: 2 · failures: 0.
- Ready for chunking (completed in the same ship · see `OPERATING_FOUNDER_SCALING_COMPLETE.md`).
