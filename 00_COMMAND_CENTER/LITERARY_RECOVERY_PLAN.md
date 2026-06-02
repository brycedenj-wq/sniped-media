# LITERARY_RECOVERY mini-batch · plan only · 2026-05-24

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document plans a two-source recovery mini-batch around the recovered Beloved (Morrison) and Jonathan Livingston Seagull (Bach) and stops. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `b757361 save session after FOUNDER_FASHION_RECOVERY consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,517 (reconciled · header = sum of `.batches[].chunk_count` = sum of jsonl line counts).
- **Canonical sets:** 10 numbered batches + 24 mini-batches · 62 official domains (75 combined keys).
- **ORIGINAL_SOURCE_COMPLETION_AUDIT:** committed (`bf55169`) · this lane is step 1-2 of its recommended final sequence (clears the last 2 clean recovery sources).
- **FOUNDER_FASHION_RECOVERY:** complete and canonical (`9d91490`).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate sources located in raw/

| Source | Author | Exact path |
|---|---|---|
| Beloved | Toni Morrison | `raw/02_TIER_1_CANON_BOOKS/literary_canon_black/Toni Morrison - Beloved (Vintage International) - libgen.li_RECOVERED.azw3` |
| Jonathan Livingston Seagull | Richard Bach | `raw/02_TIER_1_CANON_BOOKS/literary_canon_general/ Bach, Richard - Jonathan Livingston Seagull (2010, Avon Books) - libgen.li_RECOVERED.epub` |

Both staged in the authorized RECOVERY_STAGING_PASS (`_RECOVERED` suffix · copy-not-move).

## 2. Source quality / stub / scan check (read-only)

| Attribute | Beloved (Morrison) | Jonathan Livingston Seagull (Bach) |
|---|---|---|
| File type | Mobipocket/azw3 e-book ("Beloved", v8, codepage 65001) | EPUB document |
| Size | 683,018 bytes (~683 KB) | 43,376 bytes (~43 KB) |
| Text extractable | YES · ebook-convert to /tmp succeeded | YES · ebook-convert to /tmp succeeded |
| Word count | 97,915 words (full novel) | 8,977 words (short fable · correct length) |
| Stub / scan? | NO · full text (replaces the old 4-page PDF stub) | NO · full text (replaces the old djvu) |

**Verdict: both usable.** Clean, full-text e-books. Extraction tooling already on PATH (`ebook-convert` / calibre · no OCR · no new dependency). Seagull's small word count is correct (it is a novella-length fable, not a truncation).

## 3. Old bad original exclusion

Both recovered files sit beside their old broken originals, which are EXCLUDED and left untouched:
- Beloved old: `[Beloved Trilogy 1 ...] Beloved{Toni Morrison}(1987) ... libgen.li.pdf` · **PDF, 4 pages** (a stub/excerpt, NOT the full novel).
- Seagull old: `Richard Bach - Jonathan Livingston Seagull. (1973, Avon Books, N. Y.) - libgen.li.djvu` · **djvu** (unsupported format · no djvutxt on PATH).
The ship will extract ONLY the two `_RECOVERED` files. The stub PDF and djvu remain in place (preserved per the staging rules · do not hand-delete raw originals outside an authorized cleanup pass).

## 4. Already-chunked overlap check

- **Beloved already chunked:** NO · 0 `*_CHUNKS.jsonl` matches. **Net-new title.** (Morrison appears in LITERARY_CANON_BLACK via The Bluest Eye, 6 chunks · **author overlap, NOT a duplicate title** · Beloved was deferred at LITERARY_CANON_BLACK time because the staged PDF was a 4-page stub; it is now recovered.)
- **Jonathan Livingston Seagull already chunked:** NO · 0 matches. **Net-new title.** (Bach appears nowhere · Seagull was deferred at LITERARY_CANON_GENERAL time because the staged file was djvu; it is now recovered.)
- **Thematic neighbors (for distinguishing · not duplication):**
  - **LITERARY_CANON_BLACK (28 chunks · culture 13, lineage 8, aesthetics 5, operator-doctrine 2):** The Bluest Eye + The Color Purple + Their Eyes Were Watching God + Possessing the Secret of Joy + The Temple of My Familiar. **Beloved is the direct lineage neighbor** (Morrison, Black-lineage / ancestral-memory canon) · distinguished from The Bluest Eye (a distinct novel · Beloved's specific themes are rememory, the haunting weight of slavery, mother-love under bondage, and the cost of freedom).
  - **LITERARY_CANON_GENERAL (32 chunks · aesthetics 9, culture 9, operator-doctrine 7, ethics 4, lineage 3):** As a Man Thinketh, Lolita, Slaughterhouse-Five, The Kite Runner, The Prophet, Ulysses. **Seagull is the direct neighbor to As a Man Thinketh / The Prophet** (the philosophical-fable / self-transcendence register) · distinguished as a parable of mastery-through-practice and self-transcendence, held at the craft/cultural level.
  - **LITERARY_CANON_DYSTOPIAN (17 chunks · systems-thinking 8, ...):** the systemic-warning lane · only loosely adjacent.
- **Overlap risk + mitigation:** anchor each source on its own specifics. Beloved -> rememory / ancestral haunting / the moral weight of slavery / mother-love and the cost of freedom (distinct from The Bluest Eye's beauty-standard internalization). Seagull -> mastery through relentless practice, self-transcendence, the outcast-who-perfects-his-craft (distinct from As a Man Thinketh's thought-discipline). Keeps the lane complementary to the existing literary canons.

## 5. One mini-batch or split?

**One curated mini-batch, no split.** Both are recovered literary-canon works from the same RECOVERY_STAGING_PASS, both completing a previously-deferred slot in an existing literary lane (Beloved -> LITERARY_CANON_BLACK family; Seagull -> LITERARY_CANON_GENERAL family), and both route to the same existing literary-lane domains (culture / lineage / aesthetics / ethics / operator-doctrine). They differ sharply in register (a dense Black-lineage trauma novel vs a light philosophical fable), but the lane's job is identical: interpretive / cultural pattern-library extraction. Precedent: MEDIA_BUSINESS_RECOVERY + FOUNDER_FASHION_RECOVERY (2 books, one batch each). Per-source attribution preserved; Beloved (97,915 words) naturally carries more chunks than Seagull (8,977).

## 6. Recommended include / defer / exclude set

- **INCLUDE (2 · CORE):** Beloved (Morrison) · `_RECOVERED.azw3`; Jonathan Livingston Seagull (Bach) · `_RECOVERED.epub`.
- **DEFER:** none.
- **EXCLUDE (0 chunks):**
  - Old Beloved 4-page PDF stub + old Seagull djvu.
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor · not touched/staged/chunked).
  - Every other literary-canon source already chunked (no re-chunking · esp. the LITERARY_CANON_BLACK / _GENERAL / _DYSTOPIAN titles, including Morrison's The Bluest Eye).

## 7. Recommended chunk target / range

- **Target:** ~12-16 chunks.
- **Range:** 10-18 (halt-and-report if outside).
- **Synthesis:** 1-2 closing synthesis chunks (the lineage/memory + mastery/self-transcendence reading + the optionality guardrail).
- **Provisional per-source split:** Beloved ~8-9 + Seagull ~3-4 + 1-2 synthesis. Rationale: matches the per-title chunk weight in the existing literary lanes (The Bluest Eye 6, Their Eyes 7, Ulysses 6) and the word-count asymmetry (Beloved is ~11x Seagull).

## 8. Recommended domains (EXISTING domains only · NO new domain)

Verified against `MASTER_CHUNK_MAP.json.combined_domain_counts` (75 keys) before listing. **The existing literary lanes (LITERARY_CANON_BLACK / _GENERAL / _DYSTOPIAN) never used a `literary` domain** · they route to culture / lineage / aesthetics / ethics / operator-doctrine / systems-thinking. This lane follows that exact precedent.

| Domain | Exists? | Count | Planned use in this lane |
|---|---|---:|---|
| `culture` | YES | 49 | **Primary anchor (both).** The cultural weight and meaning of each work · matches the literary-lane anchor. |
| `lineage` | YES | 20 | **Beloved anchor.** Black lineage, ancestral memory / rememory, the inheritance of slavery · the Lineage-Doctrine spine (matches LITERARY_CANON_BLACK's routing). |
| `aesthetics` | YES | 71 | Morrison's prose and the haunted-house form; the fable's spare lyric form · craft-level reading. |
| `ethics` | YES | 39 | Beloved's moral weight (infanticide under slavery, the cost of freedom) · kept interpretive, not prescriptive. |
| `operator-doctrine` | YES | 84 | Seagull's mastery-through-practice / self-transcendence lesson + the synthesis chunk + the optionality guardrail (matches LITERARY_CANON_GENERAL's operator-doctrine reading of As a Man Thinketh / The Prophet). |
| `systems-thinking` | YES (if warranted) | 45 | Only if a Beloved chunk is squarely about slavery as a *system* (the institution's legacy) · used sparingly; the existing Black-lineage lane did not lean on it. |
| `mindset` | YES (if warranted) | 10 | Only if a Seagull chunk is squarely about the self-transcendence / growth mindset · available, used lightly. |

### Domain issue to flag (important)

- **`literary`, `identity`, `memory`, `trauma`, `freedom`, `myth` do NOT exist** in the corpus (ABSENT · the operator's "if it exists" conditions fail for memory/trauma/freedom/myth, and `literary`/`identity` are absent too). **None will be created.** Their material routes to the existing literary-lane domains: memory/trauma/freedom -> `culture` + `lineage` + `ethics`; identity -> `culture` + `lineage`; myth -> `culture` + `aesthetics` + `operator-doctrine`.
- **`culture`, `lineage`, `aesthetics`, `ethics`, `operator-doctrine` all exist** and are the lane's spine (exactly the domains the prior literary lanes used).
- **`systems-thinking` (45) and `mindset` (10) exist** and are available "if warranted" · used sparingly.
- **NO new domain will be created by default.** All planned domains pre-exist.

## 9. Connections (cross-references this lane opens)

- **LITERARY_CANON_BLACK:** the direct parent for Beloved · same Morrison / Black-lineage / `lineage` + `culture` cluster · Beloved completes the deferred Morrison-Beloved slot, distinguished from The Bluest Eye.
- **LITERARY_CANON_GENERAL:** the direct parent for Seagull · same philosophical-fable / `culture` + `aesthetics` + `operator-doctrine` register as As a Man Thinketh / The Prophet · Seagull completes the deferred djvu slot.
- **LITERARY_CANON_DYSTOPIAN:** loosely adjacent (the systemic-warning lane) · only if a Beloved systemic-legacy chunk warrants `systems-thinking`.
- **FOUNDER_FASHION_RECOVERY (and CULTURE_AND_STATUS / BATCH_010):** the taste / culture / status arcs · the literary works read as the humanistic-formation counterweight to the operator/founder pattern libraries.
- **CURRENT_OPERATOR_REALITY_BRIEF:** every chunk references the brief in `sniped_relevance` and holds the lane as interpretive / cultural decision-support only (the brief is the read-first anchor · NOT a chunked source).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** the optionality discipline governs this lane (see §10-11).

## 10. Identity-optionality confirmation

This lane does NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks frame the works as an **interpretive / cultural pattern-library lens read against CURRENT_OPERATOR_REALITY_BRIEF**, with the closing synthesis chunk(s) making the optionality discipline explicit. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 11. Literary recovery = interpretive / cultural pattern-library only (not a directive)

Beloved and Jonathan Livingston Seagull are held strictly as an **interpretive / cultural pattern-library layer**: the humanistic-formation and cultural-lineage reading that the existing literary lanes established (the cultural spine the operator/AI-build canon is read against). This is **NOT a directive that BJ turn the OS into literary criticism**, and **NOT a directive toward faith or self-help** · Seagull's self-transcendence parable is read at the cultural/craft level (alongside As a Man Thinketh / The Prophet), not as a belief system or a personal-development program, and Beloved is read as Black-lineage cultural canon, not as therapy. The `ethics` chunk(s) stay interpretive, not prescriptive. Photography remains one option among several.

## 12. Deliverables for the future ship (NOT created now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/LITERARY_RECOVERY_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/literary_recovery_extracted/` (2 normalized .txt) |
| Summary | `01_KNOWLEDGE_BASE/summaries/LITERARY_RECOVERY_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/LITERARY_RECOVERY_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/LITERARY_RECOVERY_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/LITERARY_RECOVERY_COMPLETE.md` |
| Extraction script | `scripts/extract_literary_recovery.py` |
| Chunk writer | `scripts/write_literary_recovery_chunks.py` |

Schema: the canonical 12-field JSONL (chunk_id, batch_id, source_title, source_file, author, domain, concept, summary, usable_principle, sniped_relevance, direct_quotes, tags) · `batch_id` = `LITERARY_RECOVERY` · per-source attribution (Morrison / Bach). Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · no new domain · old stub PDF + old djvu 0 · Bible 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality guardrail in every chunk · quote discipline · em-dash sweep).

## 13. Projected post-consolidation state (for reference · NOT applied now)

If shipped at the mid-target (~14) and consolidated: 1,517 + ~14 = ~1,531 chunks · 10 numbered batches + 25 mini-batches · 62 domains (NO new domain · bumps to culture / lineage / aesthetics / ethics / operator-doctrine, plus systems-thinking / mindset where warranted). Exact counts finalized at ship/consolidation time. This would close the recovered-literary slots and leave LITERARY_CANON_BLACK + _GENERAL effectively complete.

## 14. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,517.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `ls` / `ebook-convert`-to-/tmp · temp deleted).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No next lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 15. Next step (operator decision · do not start without authorization)

Authorize the LITERARY_RECOVERY extract + chunk + validate step (2 sources · the `_RECOVERED` files only · target ~12-16 · existing domains only · `culture` + `lineage` anchor · no new domain · `literary`/`identity`/`memory`/`trauma`/`freedom`/`myth` NOT created · old stub PDF / old djvu / Bible excluded), then commit the ship outputs, then authorize master-consolidation.
