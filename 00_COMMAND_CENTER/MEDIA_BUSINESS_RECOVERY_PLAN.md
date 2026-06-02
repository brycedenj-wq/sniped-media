# MEDIA_BUSINESS_RECOVERY mini-batch · plan only · 2026-05-24

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no file moves, no OCR. The Bible is NOT touched. Stop after writing this plan.

## 0. Verified starting state

- **Head commit:** `f8a01b5 save CURRENT_SOURCE_AUDIT_REFRESH checkpoint`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,471 · **numbered batches:** 10 · **mini-batches:** 21 · **official domains:** 62 (keys 75).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- The two recovered sources are already repo-local in `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` (RECOVERY_STAGING_PASS · `105afa1`), so this lane is repo-local · no staging pass needed.

## 1. Theme

Media-business recovery: the music-industry and Hollywood-agency institutions that extend the MEDIA_BUSINESS lane (which holds the ESPN / SNL / HBO oral histories). Hit Men (the music business · power brokers, promotion machinery, label economics, the dark side) and The Mailroom (Hollywood agency history from the bottom up · the agent's apprenticeship, talent representation, the agency as a talent-system institution). Held strictly as a pattern-library / decision-support lens read against CURRENT_OPERATOR_REALITY_BRIEF.

## 2. Candidates located + inventory (2 recovered, in `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/`)

| # | Title (author) | Recovered file | Format | Size | Words | Extraction |
|---|---|---|---|---|--:|---|
| 1 | Hit Men: Power Brokers and Fast Money Inside the Music Business (Fredric Dannen) | `[Vintage] Dannen, Fredric - Hit Men_ ... (2011, ...Vintage eBooks) - libgen.li_RECOVERED.azw3` | azw3 | 2.4 MB | 152,952 | ebook-convert |
| 2 | The Mailroom: Hollywood History from the Bottom Up (David Rensin) | `Rensin, David - The Mailroom_ ... (2007, Random House...) - libgen.li_RECOVERED.epub` | epub | 0.5 MB | 169,850 | ebook-convert |

Combined ~322,802 words. Both extractors on PATH (ebook-convert). No OCR, no new dependencies.

## 3. Pre-flight peek (read-only · ebook-convert to /tmp, deleted)

- **Hit Men (recovered azw3):** 152,952 words · converts cleanly · NOT a stub.
- **The Mailroom (recovered epub):** 169,850 words · converts cleanly · NOT a stub.
- **No scans, stubs, duplicates, unsupported formats, or off-theme sources among the two.** Both usable.

## 4. Old bad originals excluded (verified)

- **Old scanned Hit Men PDF** (` Fredric Dannen - Hit men_ ... (1991, Vintage Books) - libgen.li.pdf`, 216 pp): pdftotext yields **0 words** (scanned/image-only) · EXCLUDED · contributes 0 · remains in raw/ untouched.
- **Old Mailroom DjVu** (`David Rensin - The Mailroom -- ... (2003, Ballantine...) - libgen.li.djvu`): unsupported format (no djvutxt on PATH) · EXCLUDED · contributes 0 · remains in raw/ untouched.
- Use the `_RECOVERED` files only.

## 5. Already-chunked overlap check

- **Both are net-new** (0 hits as source_title/source_file/author across every `*_CHUNKS.jsonl`). Hit Men/Dannen = 0, Mailroom/Rensin = 0.
- MEDIA_BUSINESS currently holds three distinct institutions: ESPN (Those Guys Have All the Fun), SNL (Live From New York), HBO (Tinderbox). Hit Men (music industry) and The Mailroom (Hollywood agency) are **different institutions in the same family** · this recovery extends the lane, no content overlap. BATCH_010 (lineage + Black-music culture) is adjacent but distinct (Hit Men is an industry-power exposé, not an artist autobiography).

## 6. Enough for one mini-batch? YES · recommendation: INCLUDE the 2

Two dense media-institution books (~323K words) are ample for one curated mini-batch (the MEDIA_BUSINESS lane itself was 17 chunks from 3 oral histories). INCLUDE both. No split. Single `MEDIA_BUSINESS_RECOVERY` mini-batch (the 22nd mini-batch).

**Include:** Hit Men (Dannen), The Mailroom (Rensin).
**Exclude (report-only · 0 chunks):** old scanned Hit Men PDF, old Mailroom djvu.

## 7. Estimated chunk yield + target range

- **Target:** ~12-16 chunks.
- **Hard range:** 10-20 (halt and surface if outside).
- **Indicative per-source allocation** (principle-level, content-faithful at chunk time):
  - Hit Men (Dannen) 6-7 · The Mailroom (Rensin) 5-6 · cross-source synthesis 1-2.
- These are institution oral histories/exposes; extract durable patterns (gatekeeping, distribution power, talent systems, the dark side), not exhaustive coverage. Comparable to the MEDIA_BUSINESS ~6-chunks-per-book precedent.

## 8. Domain set (EXISTING domains only · NO new domain · `media-business` anchors)

| Domain | Indicative weight | What it carries |
|---|---|---|
| media-business (anchor) | heavy | the institutions, gatekeeping, distribution power, talent systems, how hits/careers are made |
| ethics | medium | payola / independent-promotion racket, artist exploitation, the "fast money" dark side |
| commercial-architecture | medium | label economics, the agency business model, deal/representation structures |
| culture | medium | the music-industry and Hollywood scenes and their cultures |
| operator-doctrine | light-medium | the mailroom apprenticeship grind, hustle, mentorship, paying dues |
| operator-process | light | how the machine runs (A&R, promotion, representation pipelines) |
| strategy | light | distribution and gatekeeping as power; controlling the chokepoint |
| founder-psychology | light | the ambition/drive of the power brokers and agents |
| content-strategy | light (if warranted) | hit-making, the pipeline from talent to audience |
| capital | light (if warranted) | the money flows / who profits in the industry |
| brand | light (if warranted) | label/agency/talent brand-building |

Final distribution is content-faithful at chunk time; `media-business` / `ethics` / `commercial-architecture` / `culture` are expected heaviest.

## 9. Domain verification + decision: all candidate domains exist · NO new domain

- **Verified existing (usable):** media-business (6), culture (48), commercial-architecture (51), strategy (174), brand (37), founder-psychology (28), operator-process (73), operator-doctrine (77), content-strategy (55), capital (21), ethics (35).
- **All 11 candidate domains pre-exist.** NO new domain is required or proposed. `media-business` anchors the lane (this is its recovery extension).

## 10. Connections to existing lanes + the brief

- **MEDIA_BUSINESS:** the direct parent · ESPN/SNL/HBO institutional oral histories. This recovery adds the music-industry (Hit Men) and Hollywood-agency (The Mailroom) institutions · same `media-business` anchor · the attention-network / talent-system / distribution patterns extended into music and film representation.
- **BIOGRAPHY_FOUNDER_MEDIA:** the founder/operator/media arcs · the power brokers and agents here are operators inside the media machine (the institutional layer above the individual founder arc).
- **HIGH_LEVEL_CONVOS:** the creator-economy / talent-equity / distribution threads (Malka/OWN, creator marketplace) echo the talent-representation and distribution-power patterns in their modern, creator-owned form.
- **ADVERTISING_RECOVERY (and BATCH_009):** media institutions distribute attention · the demand/attention craft reads against the gatekeeping/distribution machinery here.
- **CURRENT_OPERATOR_REALITY_BRIEF:** referenced in every chunk · the institution patterns are decision-support for how BJ reads media/talent/distribution power, NOT a directive.
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** fully honored (see 12-13).

## 11. (covered in 10)

## 12. Identity optionality confirmation

This lane does NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction. SNIPED remains the live operator identity/container; SNIPED Media the existing photography company; BASEPLATE a possible historical rebrand asset. Every chunk frames the media-business content as a pattern-library / decision-support LENS read against CURRENT_OPERATOR_REALITY_BRIEF. Photography remains one option among several.

## 13. Media-business recovery is a pattern-library / decision-support layer only

The institution patterns are **NOT a directive that BJ become a music, film, or media executive.** They are lenses on how gatekeeping, distribution power, talent systems, and the dark side of "fast money" industries work, held against current reality. The dark-side/ethics chunks (payola, artist exploitation) keep the patterns honest, not aspirational. A closing synthesis chunk will make the optionality discipline explicit (mirroring MEDIA_BUSINESS and the prior recovery lanes).

## 14. Deliverables (created only when extraction/chunking is later authorized · NOT now)

- `01_KNOWLEDGE_BASE/batches/MEDIA_BUSINESS_RECOVERY_CHUNKS.jsonl` (12-field canonical schema · batch_id `MEDIA_BUSINESS_RECOVERY`)
- `01_KNOWLEDGE_BASE/batches/media_business_recovery_extracted/` (2 normalized .txt)
- `01_KNOWLEDGE_BASE/summaries/MEDIA_BUSINESS_RECOVERY_SUMMARY.md`
- `01_KNOWLEDGE_BASE/indexes/MEDIA_BUSINESS_RECOVERY_SOURCE_INDEX.md`
- `00_COMMAND_CENTER/batch_logs/MEDIA_BUSINESS_RECOVERY_EXTRACTION_LOG.md`
- `00_COMMAND_CENTER/batch_logs/MEDIA_BUSINESS_RECOVERY_COMPLETE.md`
- `scripts/extract_media_business_recovery.py`
- `scripts/write_media_business_recovery_chunks.py`

(This plan file `00_COMMAND_CENTER/MEDIA_BUSINESS_RECOVERY_PLAN.md` is the only artifact written now.)

## 15-19. Scope guards for this planning pass

- **15. Do not extract.** Honored (the section-3 peeks went to /tmp and were deleted · the deliverable `media_business_recovery_extracted/` was NOT created).
- **16. Do not chunk.** Honored.
- **17. Do not update master files.** Honored.
- **18. Do not touch the Bible.** Honored · the KJV remains a held SPIRITUAL_FOUNDATION anchor, untouched and excluded.
- **19. Stop after writing the plan.** Honored. No commit (operator will review first).

## Execution sequence (when later authorized · the locked 7-step SOP, steps 5-7)

1. `scripts/extract_media_business_recovery.py` · ebook-convert (Hit Men azw3, The Mailroom epub) into `media_business_recovery_extracted/` (refuse to overwrite). Use the `_RECOVERED` files only; the old scanned Hit Men pdf and the old Mailroom djvu contribute 0. No OCR, no new dependency.
2. `scripts/write_media_business_recovery_chunks.py` · author 10-20 chunks (target ~12-16) · 12-field schema · batch_id `MEDIA_BUSINESS_RECOVERY` · per-source attribution (Dannen / Rensin) · short illustrative quotes only (copyright-safe · in-copyright trade books) · em-dash clean · CURRENT_OPERATOR_REALITY_BRIEF referenced in every chunk · optionality guardrail in the closing chunk · existing domains only · NO new domain.
3. Validate: 6 jsonl-validation checks + per-lane checks (exactly the 2 recovered sources resolve, NO new domain, old scanned Hit Men + old Mailroom djvu 0, no already-chunked overlap with MEDIA_BUSINESS/BATCH_010, brief not chunked, em-dash 0, quote discipline).
4. Ship commit, then a separate authorized master-consolidation (bumps existing domains · NO new domain), then session save. Each step gated and scoped.

## Open questions for the operator

1. **Chunk depth:** confirm ~12-16 (range 10-20), or signal a tighter cap if you want only the sharpest institution patterns from the two.
2. **ethics weight:** how heavily to chunk the dark-side material (Hit Men's payola/independent-promotion racket, artist exploitation) · default is ~2 ethics chunks that keep the patterns honest, not aspirational.
3. **capital / brand / content-strategy:** include the money-flow, label/agency-brand, and hit-making-pipeline threads as light single chunks (if warranted), or keep the lane tight on media-business / ethics / commercial-architecture / culture?
