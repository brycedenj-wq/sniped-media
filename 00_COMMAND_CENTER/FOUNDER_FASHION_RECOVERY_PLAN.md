# FOUNDER_FASHION_RECOVERY mini-batch · plan only · 2026-05-24

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document plans a two-source recovery mini-batch around the recovered Grace: A Memoir (Coddington) and Total Recall (Schwarzenegger) and stops. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `bf55169 save ORIGINAL_SOURCE_COMPLETION_AUDIT checkpoint`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,501 (reconciled · header = sum of `.batches[].chunk_count` = sum of jsonl line counts).
- **Canonical sets:** 10 numbered batches + 23 mini-batches · 62 official domains (75 combined keys).
- **ORIGINAL_SOURCE_COMPLETION_AUDIT:** committed (`bf55169`) · this lane is step 1 of its recommended final sequence.
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate sources located in raw/

| Source | Author | Exact path |
|---|---|---|
| Grace: A Memoir | Grace Coddington | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/Grace Coddington - Grace_ A Memoir (2012, Random House) - libgen.li_RECOVERED.epub` |
| Total Recall: My Unbelievably True Life Story | Arnold Schwarzenegger | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/Schwarzenegger, Arnold - Total Recall- My Unbelievably True Life Story (2012, Simon & Schuster) - libgen.li_RECOVERED.epub` |

Both staged in the authorized RECOVERY_STAGING_PASS (`_RECOVERED` suffix · copy-not-move).

## 2. Source quality / stub / scan check (read-only)

| Attribute | Grace (Coddington) | Total Recall (Schwarzenegger) |
|---|---|---|
| File type | EPUB document | EPUB document |
| Size | 103,023,863 bytes (~103 MB · image-rich) | 8,868,448 bytes (~8.9 MB) |
| Text extractable | YES · ebook-convert to /tmp succeeded | YES · ebook-convert to /tmp succeeded |
| Word count | 82,009 words | 242,002 words |
| Stub / scan? | NO · full text (the large size is embedded photography/illustrations, but the prose extracts cleanly) | NO · full-length memoir |

**Verdict: both usable.** Clean, full-text epubs. Extraction tooling already on PATH (`ebook-convert` / calibre · no OCR · no new dependency). Grace's 103 MB is image weight; the extracted text is a normal ~82K-word memoir.

## 3. Old bad original exclusion

Both recovered files sit beside their old broken originals (0-byte stubs), which are EXCLUDED and left untouched:
- Grace old: `Coddington, Grace - Grace_ A Memoir (2012, Random House Publishing Group) - libgen.li.epub` · **0 bytes** (stub).
- Total Recall old: `Petre, Peter_Schwarzenegger, Arnold - Total recall_ ... (2012, Simon & Schuster) - libgen.li.epub` · **0 bytes** (stub).
The ship will extract ONLY the two `_RECOVERED.epub` files. The 0-byte stubs remain in place (preserved per the staging rules · do not hand-delete raw originals outside an authorized cleanup pass).

## 4. Already-chunked overlap check

- **Grace / Coddington already chunked:** NO · 0 `*_CHUNKS.jsonl` matches. **Net-new title.**
- **Total Recall / Schwarzenegger already chunked:** NO · 0 matches. **Net-new title.**
- **Thematic neighbors (for distinguishing · not duplication):**
  - **BIOGRAPHY_FOUNDER_MEDIA (22 chunks):** D.V. (Diana Vreeland), No Filter (Instagram), Losing My Virginity (Branson), Grinding It Out (Kroc), That Will Never Work (Netflix/Randolph), Made in Japan (Sony/Morita). **D.V. / Vreeland is the direct fashion-media-editor neighbor to Coddington** (both legendary Vogue-world tastemakers); Coddington is a distinct person and title, told from the creative-director's eye rather than the editor-in-chief's.
  - **FOUNDER_SECOND_TIER (20 chunks):** Sam Walton, Elon Musk, Super Pumped (Uber), The Airbnb Story, Titan (Rockefeller), The Fish That Ate the Whale, Pour Your Heart Into It (Schultz). **Total Recall is the operator/career-arc memoir neighbor** (relentless drive, platform-jumping, self-built public figure) but Schwarzenegger appears nowhere yet and is a distinct, first-person arc (bodybuilding to film to politics to business).
- **Overlap risk + mitigation:** anchor each source on its own first-person specifics. Grace → the creative-director's eye / editorial craft / taste as discipline (distinct from Vreeland's editor-in-chief authority). Total Recall → the multi-career reinvention arc / vision-and-reps / self-built brand (distinct from the company-building founders in FOUNDER_SECOND_TIER, since this is a personal operator arc, not a company history). Keeps the lane complementary, not duplicative.

## 5. One mini-batch or split?

**One curated mini-batch, no split.** Both are recovery memoirs from the same RECOVERY_STAGING_PASS, both in the BIOGRAPHY_FOUNDER_MEDIA family, and both are "operator / taste-maker / career-arc memoir" material that reads as decision-support pattern library. They differ in subject (fashion editorial vs bodybuilding/film/politics/business) but share the lane's job: how a singular operator builds a body of work, a public self, and a method over decades. Precedent: ADVERTISING_RECOVERY (3 books, one batch) and MEDIA_BUSINESS_RECOVERY (2 books, one batch). Per-source attribution preserved; Total Recall (242K words) naturally carries more chunks than Grace (82K).

## 6. Recommended include / defer / exclude set

- **INCLUDE (2 · CORE):** Grace: A Memoir (Coddington) · `_RECOVERED.epub`; Total Recall (Schwarzenegger) · `_RECOVERED.epub`.
- **DEFER:** none.
- **EXCLUDE (0 chunks):**
  - Old 0-byte Grace stub + old 0-byte Total Recall stub.
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor · not touched/staged/chunked).
  - Every other memoirs_biographies / canonical source already chunked (no re-chunking · esp. the BIOGRAPHY_FOUNDER_MEDIA + FOUNDER_SECOND_TIER + MEDIA_BUSINESS_RECOVERY titles; Grant + Washington / Chernow are the SEPARATE historical-biography lane, not this one).

## 7. Recommended chunk target / range

- **Target:** ~14-18 chunks.
- **Range:** 10-20 (halt-and-report if outside).
- **Synthesis:** 1-2 closing synthesis chunks (the taste-maker + operator-arc pattern + the optionality guardrail).
- **Provisional per-source split:** Grace ~6-7 + Total Recall ~7-9 + 1-2 synthesis. Rationale: matches the two-source recovery precedent (MEDIA_BUSINESS_RECOVERY = 15) and the word-count asymmetry (Total Recall is ~3x Grace).

## 8. Recommended domains (EXISTING domains only · NO new domain)

Verified against `MASTER_CHUNK_MAP.json.combined_domain_counts` (75 keys) before listing:

| Domain | Exists? | Count | Planned use in this lane |
|---|---|---:|---|
| `founder-psychology` | YES | 29 | **Co-anchor (operator-arc).** Vision + relentless drive + reinvention + self-belief (Schwarzenegger); the editor's will and standards (Coddington). |
| `aesthetics` | YES | 69 | **Co-anchor (taste-making).** Coddington's visual eye, editorial image-making, the made photograph, art direction as craft. |
| `taste` | YES | 10 | Taste as a disciplined, trainable judgment (Coddington) · a natural existing-domain fit; used where a chunk is squarely about taste/curation. |
| `brand` | YES | 37 | The self-built public figure / personal brand (Schwarzenegger built "Arnold"); the Vogue/editorial brand world. |
| `culture` | YES | 49 | Fashion culture, celebrity/Hollywood culture, the cultural machines both operated inside. |
| `operator-process` | YES | 74 | The working method · Coddington's shoot/sitting process; Arnold's training-and-preparation method. |
| `operator-doctrine` | YES | 81 | Reps, preparation, follow-through, ownership · the synthesis + optionality guardrail. |
| `strategy` | YES | 178 | Career sequencing / platform-jumping (bodybuilding to film to politics to business as deliberate moves). |
| `media-business` | YES (if warranted) | 9 | The Vogue editorial machine + Hollywood as media institutions · used only where a chunk is squarely institutional. |
| `ethics` | YES (if warranted) | 38 | Where a memoir is honest about cost/contradiction (Arnold's public failings, the price of obsession) · kept honest, not aspirational. |

### Domain issue to flag (important)

- **`fashion` does NOT exist** in the corpus (ABSENT · the operator's "if it exists" condition fails). It will **NOT be created.** All fashion/styling material routes to `aesthetics` + `taste` + `culture` + `brand` (the same routing BIOGRAPHY_FOUNDER_MEDIA used for D.V./Vreeland · `fashion`/`fashion-luxury` were never registered; `fashion_luxury` is only a raw/ folder name).
- **`founder-psychology` and `aesthetics` both exist** and are the dual anchor.
- **NO new domain will be created by default.** All 10 candidate domains pre-exist.

## 9. Connections (cross-references this lane opens)

- **BIOGRAPHY_FOUNDER_MEDIA:** the direct parent · D.V. (Vreeland) is the fashion-media-editor neighbor to Coddington; the founder/media arcs (Branson, Kroc, Sony) are the operator-arc neighbors to Schwarzenegger · same `founder-psychology` / `aesthetics` / `culture` cluster.
- **FOUNDER_SECOND_TIER:** the company-building scale arcs · Total Recall is the *personal* operator-arc companion (a self, not a company), distinguished so it complements rather than duplicates.
- **MEDIA_BUSINESS_RECOVERY (and MEDIA_BUSINESS):** the institutions (Vogue editorial, Hollywood) that Coddington and Schwarzenegger operated inside · the `media-business` link where warranted.
- **CULTURE_AND_STATUS + BATCH_010:** taste, status, and cultural-capital theory read against two lived taste/status arcs.
- **CURRENT_OPERATOR_REALITY_BRIEF:** every chunk references the brief in `sniped_relevance` and holds the lane as decision-support only (the brief is the read-first anchor · NOT a chunked source).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** the optionality discipline governs this lane (see §10-11).

## 10. Identity-optionality confirmation

This lane does NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks frame the memoir patterns as a **pattern-library / decision-support lens read against CURRENT_OPERATOR_REALITY_BRIEF**, with the closing synthesis chunk(s) making the optionality discipline explicit. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 11. Founder/fashion recovery = pattern-library / decision-support only (not a directive)

Grace and Total Recall are held strictly as a **pattern-library / decision-support layer**: how a singular operator builds taste, a method, a public self, and a decades-long body of work. They are **NOT a directive that BJ become a fashion operator, a memoirist, or a celebrity/personal brand**, and not an endorsement of any one path (fashion editorial or platform-jumping fame). The taste/aesthetics material is a lens on disciplined judgment; the operator-arc material is a lens on reps and reinvention. The `ethics` chunk(s), where used, keep the arcs honest (cost, contradiction, public failings), not aspirational. Photography stays one option among several.

## 12. Deliverables for the future ship (NOT created now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/FOUNDER_FASHION_RECOVERY_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/founder_fashion_recovery_extracted/` (2 normalized .txt) |
| Summary | `01_KNOWLEDGE_BASE/summaries/FOUNDER_FASHION_RECOVERY_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/FOUNDER_FASHION_RECOVERY_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/FOUNDER_FASHION_RECOVERY_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/FOUNDER_FASHION_RECOVERY_COMPLETE.md` |
| Extraction script | `scripts/extract_founder_fashion_recovery.py` |
| Chunk writer | `scripts/write_founder_fashion_recovery_chunks.py` |

Schema: the canonical 12-field JSONL (chunk_id, batch_id, source_title, source_file, author, domain, concept, summary, usable_principle, sniped_relevance, direct_quotes, tags) · `batch_id` = `FOUNDER_FASHION_RECOVERY` · per-source attribution (Coddington / Schwarzenegger). Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · no new domain · old 0-byte stubs 0 · Bible 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality guardrail in every chunk · quote discipline · em-dash sweep).

## 13. Projected post-consolidation state (for reference · NOT applied now)

If shipped at the mid-target (~16) and consolidated: 1,501 + ~16 = ~1,517 chunks · 10 numbered batches + 24 mini-batches · 62 domains (NO new domain · bumps to founder-psychology / aesthetics / taste / brand / culture / operator-process / operator-doctrine / strategy, plus media-business / ethics where warranted). Exact counts finalized at ship/consolidation time.

## 14. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,501.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `ls` / `ebook-convert`-to-/tmp · temp deleted).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No next lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 15. Next step (operator decision · do not start without authorization)

Authorize the FOUNDER_FASHION_RECOVERY extract + chunk + validate step (2 sources · the `_RECOVERED.epub` files only · target ~14-18 · existing domains only · `founder-psychology` + `aesthetics` dual anchor · no new domain · `fashion` NOT created · old 0-byte stubs / Bible excluded), then commit the ship outputs, then authorize master-consolidation.
