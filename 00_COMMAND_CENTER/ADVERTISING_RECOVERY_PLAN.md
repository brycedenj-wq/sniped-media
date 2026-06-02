# ADVERTISING_RECOVERY mini-batch · plan only · 2026-05-24

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no file moves, no OCR. The Bible is NOT touched. Stop after writing this plan.

## 0. Verified starting state

- **Head commit:** `e56441e save session after HIGH_LEVEL_CONVOS consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,455 · **numbered batches:** 10 · **mini-batches:** 20 · **official domains:** 62 (keys 75).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- The three recovered advertising sources are already staged in `raw/02_TIER_1_CANON_BOOKS/advertising/` (RECOVERY_STAGING_PASS · commit `105afa1`), so this lane is repo-local · no staging pass needed.

## 1. Theme

Advertising / copywriting canon recovery: the foundational craft of advertising the corpus was missing because these three were broken/missing at BATCH_009 time. Ogilvy's agency discipline + brand image, Sugarman's copy mechanics + psychological triggers, and Halbert's direct-response fundamentals + market-first thinking. Held as a decision-support and execution layer read against CURRENT_OPERATOR_REALITY_BRIEF.

## 2. Candidates located + inventory (3 recovered, in `raw/02_TIER_1_CANON_BOOKS/advertising/`)

| # | Title (author) | Recovered file | Format | Size | Words | Extraction |
|---|---|---|---|---|--:|---|
| 1 | Confessions of an Advertising Man (David Ogilvy) | `Confessions-of-an-Advertising-Man-by-Ogilvy-David-Parker-Alan-z-lib.org__RECOVERED.pdf` | pdf | 0.7 MB | 42,924 (42 pp) | pdftotext |
| 2 | The Adweek Copywriting Handbook (Joseph Sugarman) | `The Adweek Copywriting Handbook_ ... {Sugarman, Joseph}(2024)... libgen.li_RECOVERED.azw3` | azw3 | 4.4 MB | 107,745 | ebook-convert |
| 3 | The Boron Letters (Gary Halbert) | `Gary C Halbert - The Boron Letters (2013) - libgen.li_RECOVERED.epub` | epub | 0.1 MB | 43,043 | ebook-convert |

Combined ~193,712 words. All extractors on PATH (pdftotext, ebook-convert). No OCR, no new dependencies.

## 3. Pre-flight peek (read-only · to /tmp, deleted)

- **Confessions (recovered):** 42 pp · 42,924 words · clean text layer (a reflowed z-lib edition · the prose is complete). NOT a scan.
- **The Adweek Copywriting Handbook (recovered):** azw3 · 107,745 words · converts cleanly · NOT a stub.
- **The Boron Letters (recovered):** epub · 43,043 words · converts cleanly · NOT a stub.
- **No scans, stubs, duplicates, unsupported formats, or off-theme sources among the three.** All usable.

## 4. Old bad originals excluded (verified)

- **Old scanned Confessions** (`David Ogilvy_ Alan Parker - ... - libgen.li.pdf`, 22.5 MB, 107 pp): pdftotext yields **0 words** (still scanned/image-only) · EXCLUDED · contributes 0 · remains in raw/ untouched.
- **Hey, Whipple, Squeeze This** (`[Adweek Series] Luke Sullivan - ... .pdf`, 5.1 MB): a DIFFERENT book that merely shares the "Adweek" series label · NOT one of these three recovered sources · OUT OF SCOPE for this lane (a possible future advertising addition, not chunked here).

## 5. Caples remains broken and excluded

- **Tested Advertising Methods (John Caples):** the re-downloaded PDF is still scanned/image-only (0 extractable words · per RECOVERY_INTAKE_CHECK) · remains a recovery item · **EXCLUDED · contributes 0**. The direct-response lane proceeds with Sugarman + Halbert; Caples joins only once a clean epub is re-acquired.

## 6. Already-chunked overlap check

- **All three are net-new** (0 hits as source_title/source_file/author across every `*_CHUNKS.jsonl`). Confessions/Ogilvy = 0, Sugarman/Adweek = 0, Halbert/Boron = 0. Caples = 0 (excluded anyway).
- BATCH_009 + BATCH_009_EXPANSION chunked the advertising/copywriting canon (Hopkins, Schwartz, Bly, Whitman, Cialdini, Berger, Shotton, Sutherland, Godin, Trout, Dunford, Hormozi, Heath, Miller, etc.) but NOT Ogilvy's Confessions, Sugarman, or Halbert · these three were the broken/missing gaps. This lane completes the BATCH_009 advertising canon.

## 7. Enough for one mini-batch? YES · recommendation: INCLUDE the 3

Three dense, foundational advertising/copywriting canon books (~194K words) are ample for one curated mini-batch. INCLUDE all three. No split. Single `ADVERTISING_RECOVERY` mini-batch (the 21st mini-batch).

**Include:** Confessions (Ogilvy), The Adweek Copywriting Handbook (Sugarman), The Boron Letters (Halbert).
**Exclude (report-only · 0 chunks):** old scanned Confessions PDF, Caples (still scanned), Hey Whipple (different book, out of scope).

## 8. Estimated chunk yield + target range

- **Target:** ~14-18 chunks.
- **Hard range:** 10-22 (halt and surface if outside).
- **Indicative per-source allocation** (principle-level, content-faithful at chunk time):
  - Confessions (Ogilvy) 5-6 · The Adweek Copywriting Handbook (Sugarman) 5-6 · The Boron Letters (Halbert) 4-5 · cross-source synthesis 1.
- These are craft canon; extract durable principles, not exhaustive coverage.

## 9. Domain set (EXISTING domains only · NO new domain · `copywriting` anchors)

| Domain | Indicative weight | What it carries |
|---|---|---|
| copywriting (anchor) | heavy | the craft itself: headlines, first-sentence/slippery-slide, AIDA, editing, conversational copy |
| brand-psychology | medium | psychological triggers, emotion vs logic, curiosity seeds, why people buy (routes the "persuasion" content) |
| brand | medium | Ogilvy's brand image, long-term brand-building, reputation of the product |
| positioning | light-medium | the product's promise/claim, what the ad is really selling |
| offer-design | light-medium | the offer and its framing in direct response |
| sales-flow | light | the direct-response sequence, the ask, response mechanics |
| meta-advertising | light-medium | advertising-about-advertising: research discipline, what makes ads work, testing |
| commercial-architecture | light | agency economics, direct-response as a business (routes the "marketing" content) |
| content-strategy | light | the market/list-first thinking (Halbert's "starving crowd"), audience before message |
| strategy | light | the strategic frame around campaigns and positioning |
| operator-process | light (if warranted) | Ogilvy on running a creative shop, hiring/firing, discipline; Halbert's work ethic |
| ethics | light (if warranted) | Ogilvy on honesty in advertising / not making claims you would not want your family to see |

Final distribution is content-faithful at chunk time; `copywriting` / `brand-psychology` / `brand` are expected heaviest.

## 10. Domain verification + decision: `marketing` and `persuasion` do NOT exist

- **Verified existing (usable):** copywriting (20), positioning (16), sales-flow (15), offer-design (16), brand (36), brand-psychology (26), commercial-architecture (50), content-strategy (54), strategy (173), operator-process (72), ethics (34), meta-advertising (8).
- **`marketing` does NOT exist · `persuasion` does NOT exist** (verified · not in combined_domain_counts). Per the no-new-domain rule, they are **NOT created**. The "persuasion" content routes to **`brand-psychology`** (+ `copywriting`); the "marketing" content routes to **`commercial-architecture`** / **`strategy`** / **`content-strategy`**. **NO new domain is introduced.** (This mirrors the BATCH_009 decision, which also declined to add `advertising`/`persuasion` and routed to copywriting / meta-advertising / brand-psychology / sales-flow.)

## 11. Connections to existing lanes + the brief

- **BATCH_009 (+ EXPANSION):** the direct parent · the advertising/copywriting/persuasion/positioning canon and craft standard. ADVERTISING_RECOVERY completes it by adding the three foundational gaps (Ogilvy/Sugarman/Halbert) that were broken/missing at BATCH_009 time. Same `copywriting` / `brand-psychology` / `meta-advertising` cluster.
- **MONEY_OWNERSHIP:** copy and offers are how value is captured · advertising is the demand-capture craft over the owner-economics substrate (lighter connection).
- **HIGH_LEVEL_CONVOS:** the creator-economy / niche-audience-monetization / "provide value" threads echo Halbert's market-first thinking and Sugarman's copy mechanics in a conversational register.
- **CURRENT_OPERATOR_REALITY_BRIEF:** referenced in every chunk · the craft is decision-support + an execution layer for whatever BJ builds (he can write his own copy/positioning regardless of final direction), NOT a directive.
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** fully honored (see 13-14).

## 12. (covered in 11)

## 13. Identity optionality confirmation

This lane does NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction. SNIPED remains the live operator identity/container; SNIPED Media the existing photography company; BASEPLATE a possible historical rebrand asset. Every chunk frames the advertising/copywriting craft as decision-support + execution material read against CURRENT_OPERATOR_REALITY_BRIEF. Photography remains one option among several.

## 14. Advertising/copywriting is a decision-support + execution layer only

The craft is **NOT a directive that BJ become a copywriter or run an agency.** It is an execution layer (write better copy, sharper positioning, stronger offers for whatever he builds) and a decision-support lens, held against current reality. A closing synthesis chunk will make the optionality discipline explicit (mirroring the prior lanes' guardrail chunks).

## 15. Deliverables (created only when extraction/chunking is later authorized · NOT now)

- `01_KNOWLEDGE_BASE/batches/ADVERTISING_RECOVERY_CHUNKS.jsonl` (12-field canonical schema · batch_id `ADVERTISING_RECOVERY`)
- `01_KNOWLEDGE_BASE/batches/advertising_recovery_extracted/` (3 normalized .txt)
- `01_KNOWLEDGE_BASE/summaries/ADVERTISING_RECOVERY_SUMMARY.md`
- `01_KNOWLEDGE_BASE/indexes/ADVERTISING_RECOVERY_SOURCE_INDEX.md`
- `00_COMMAND_CENTER/batch_logs/ADVERTISING_RECOVERY_EXTRACTION_LOG.md`
- `00_COMMAND_CENTER/batch_logs/ADVERTISING_RECOVERY_COMPLETE.md`
- `scripts/extract_advertising_recovery.py`
- `scripts/write_advertising_recovery_chunks.py`

(This plan file `00_COMMAND_CENTER/ADVERTISING_RECOVERY_PLAN.md` is the only artifact written now.)

## 16-20. Scope guards for this planning pass

- **16. Do not extract.** Honored (the section-3 peeks went to /tmp and were deleted · the deliverable `advertising_recovery_extracted/` was NOT created).
- **17. Do not chunk.** Honored.
- **18. Do not update master files.** Honored.
- **19. Do not touch the Bible.** Honored · the KJV remains a held SPIRITUAL_FOUNDATION anchor, untouched and excluded.
- **20. Stop after writing the plan.** Honored. No commit (operator will review first).

## Execution sequence (when later authorized · the locked 7-step SOP, steps 5-7)

1. `scripts/extract_advertising_recovery.py` · pdftotext (Confessions recovered pdf) + ebook-convert (Sugarman azw3, Halbert epub) into `advertising_recovery_extracted/` (refuse to overwrite). Use the `_RECOVERED` files only; the old scanned Confessions pdf and Caples contribute 0. No OCR, no new dependency.
2. `scripts/write_advertising_recovery_chunks.py` · author 10-22 chunks (target ~14-18) · 12-field schema · batch_id `ADVERTISING_RECOVERY` · per-source attribution (Ogilvy / Sugarman / Halbert) · short illustrative quotes only (copyright-safe · in-copyright trade books) · em-dash clean · CURRENT_OPERATOR_REALITY_BRIEF referenced in every chunk · optionality guardrail in the closing chunk · existing domains only · `marketing`/`persuasion` NOT used.
3. Validate: 6 jsonl-validation checks + per-lane checks (exactly the 3 recovered sources resolve, NO new domain, old scanned Confessions + Caples 0, no already-chunked overlap with BATCH_009, brief not chunked, em-dash 0, quote discipline).
4. Ship commit, then a separate authorized master-consolidation (bumps existing domains · NO new domain), then session save. Each step gated and scoped.

## Open questions for the operator

1. **Chunk depth:** confirm ~14-18 (range 10-22), or signal a tighter cap if you want only the sharpest craft principles from the three.
2. **operator-process / ethics inclusion:** include the agency-running (Ogilvy) and honesty-in-advertising threads as `operator-process` / `ethics` chunks (default · if warranted), or keep the lane purely craft (copywriting/brand-psychology/brand)?
3. **Caples:** hold the direct-response lane as Sugarman + Halbert for now, or wait to re-acquire a clean Caples epub and add it before shipping?
