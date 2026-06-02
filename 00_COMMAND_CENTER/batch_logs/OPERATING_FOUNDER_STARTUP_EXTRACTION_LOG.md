# OPERATING_FOUNDER_STARTUP extraction log · 2026-05-25

## Sources

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `lean_startup_ries.txt` | The Lean Startup | Eric Ries | pdf | `raw/02_TIER_1_CANON_BOOKS/operating_founder/Eric Ries - The Lean Startup ... (2017_2011, Crown Business) - libgen.li.pdf` | 84,808 |
| `hard_thing_horowitz.txt` | The Hard Thing About Hard Things | Ben Horowitz | epub | `raw/02_TIER_1_CANON_BOOKS/operating_founder/Ben Horowitz - The Hard Thing About Hard Things_ ... (2014, HarperBusiness) - libgen.li.epub` | 78,703 |
| `founders_dilemmas_wasserman.txt` | The Founder's Dilemmas | Noam Wasserman | epub | `raw/02_TIER_1_CANON_BOOKS/operating_founder/[Kauffman Foundation Series ...] Noam Wasserman - The Founder's Dilemmas_ ... (2012, Princeton University Press) - libgen.li.epub` | 145,096 |

## Method

- **Tools:** `pdftotext` (The Lean Startup) + `ebook-convert` (Hard Thing epub, Founder's Dilemmas epub). Both already on PATH.
- **No OCR. No new dependencies.** All three source files were read-only (not modified · 2026-05-1x mtimes unchanged).
- **Output:** `01_KNOWLEDGE_BASE/batches/operating_founder_startup_extracted/` (3 .txt · 308,607 words total).
- **Script:** `scripts/extract_operating_founder_startup.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded / deferred (0 chunks · 0 extraction)

- **Deferred to subsequent OPERATING_FOUNDER sub-lanes:**
  - **OPERATING_FOUNDER_SCALING:** Blitzscaling (Hoffman/Yeh), Amp It Up (Slootman) · NOT extracted.
  - **OPERATING_FOUNDER_OPERATIONS:** The Goal (Goldratt), Reengineering the Corporation (Hammer/Champy), The E-Myth Revisited (Gerber), Built to Sell (Warrillow) · NOT extracted.
- **BROKEN:** Traction (Weinberg/Mares) · 0-byte empty epub · re-acquire · NOT extracted.
- **OUT-OF-SCOPE / misfiled in the folder:** The 88 Laws of the Masculine Mindset (John Winters · self-help) + Moonwalk (Michael Jackson · music memoir) · NOT operating-founder · NOT extracted.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked. Held separately as a SPIRITUAL_FOUNDATION anchor.
- **Every already-canonical founder/operator/strategy/classical/history source, every network_distribution / sales_positioning / decision_judgment / brand-canon / Tier-2 source, and CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** NOT extracted.

## Scope-guard note (3 dense how-to books)

The 3 sources total ~308,607 words. Per the operator's scope guard, the lane is **representative operating-founder pattern extraction, NOT a chapter-by-chapter startup-book summary** · 15 curated chunks (incl. 1 synthesis · per-source 5/5/5), not a chapter walk.

## Result

- Sources in: 3 · extracted out: 3 · failures: 0.
- Ready for chunking (completed in the same ship · see `OPERATING_FOUNDER_STARTUP_COMPLETE.md`).
