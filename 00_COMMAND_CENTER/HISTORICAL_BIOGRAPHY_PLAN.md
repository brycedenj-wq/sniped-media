# HISTORICAL_BIOGRAPHY mini-batch · plan only · 2026-05-24

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document plans a two-source mini-batch around Ron Chernow's Grant and Washington: A Life and stops. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `8405815 save NON_BOOK_DOCS_COMPLETION_AUDIT checkpoint`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,531 (reconciled · header = sum of `.batches[].chunk_count` = sum of jsonl line counts).
- **Canonical sets:** 10 numbered batches + 25 mini-batches · 62 official domains (75 combined keys).
- **All RECOVERY_STAGING_PASS recovered sources processed.** ORIGINAL_SOURCE_COMPLETION_AUDIT (`bf55169`) named this the top remaining high-value book lane; NON_BOOK_DOCS_COMPLETION_AUDIT (`8405815`) recommended it first over a non-book intake.
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate sources located in raw/

| Source | Author | Exact path |
|---|---|---|
| Grant | Ron Chernow | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/Ron Chernow - Grant (2017, Penguin Publishing Group) - libgen.li.epub` |
| Washington: A Life | Ron Chernow | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/Ron Chernow - Washington_ A Life - libgen.li.pdf` |

Both are repo-local in `raw/` (staged earlier; not recovery `_RECOVERED` files, these were already present and clean).

## 2. Source quality / stub / scan check (read-only)

| Attribute | Grant (Chernow) | Washington: A Life (Chernow) |
|---|---|---|
| File type | EPUB document | PDF 1.5 · 945 pages · not encrypted |
| Size | 23.9 MB | 5.07 MB |
| Text extractable | YES · ebook-convert to /tmp succeeded | YES · pdftotext to /tmp succeeded (clean text layer, NOT a scan) |
| Word count | 477,789 words | 434,274 words |
| Stub / scan? | NO · full biography | NO · clean text PDF (a leading `rrrr...` cover-image artifact line precedes the real text; harmless) |

**Verdict: both usable.** Two full-length (~900-page) Chernow biographies, ~912,063 words combined. Grant via `ebook-convert`; Washington via `pdftotext` (text layer confirmed present, not image-only). No OCR, no new dependency. **Note:** these are the two largest single sources approached so far; chunking will be curated/selective (a representative pattern library, NOT exhaustive coverage), consistent with prior major-biography handling.

## 3. Already-chunked overlap check

- **Grant already chunked:** NO · 0 `*_CHUNKS.jsonl` matches. **Net-new title.**
- **Washington: A Life already chunked:** NO · 0 matches. **Net-new title.**
- **Author overlap (not duplicate):** Chernow appears in 1 jsonl (FOUNDER_SECOND_TIER) via **Titan: The Life of John D. Rockefeller** (3 chunks). Same author, distinct titles, **distinct register**: Titan reads Rockefeller as a business-empire builder (founder-psychology / capital / commercial-architecture); Grant and Washington are military-and-political-leadership lives → leadership / power / strategy. No duplication.
- **Thematic neighbors (for distinguishing):**
  - **FOUNDER_SECOND_TIER (20 chunks · founder-psychology 3, ethics 3, operator-doctrine 2, operator-process 2, systems-thinking 2, strategy 2, commercial-architecture 2, brand 2, capital 1, culture 1):** the company-building scale arcs (Walton, Musk, Uber, Airbnb, Titan, United Fruit, Schultz). Grant + Washington are the **public/military/political-leadership** cousins of those operator arcs, distinguished as institution-and-command leadership rather than company-building.
  - **BATCH_002 (Tier-1 canon · leadership 36) + BATCH_003 (leadership 4):** the existing `leadership` home (founder-mode, mood propagation, succession, multi-century leadership patterns). Grant + Washington extend `leadership` into military command and republican statecraft, the existing domain's natural deepening.
- **Overlap risk + mitigation:** anchor each source on its own specifics. Grant → relentless persistence and clarity under pressure, total-war strategy, magnanimity at Appomattox, the honest man undone by misplaced trust (the Gilded-Age scandals), Reconstruction and moral courage. Washington → strategic patience (the Fabian strategy), command of a fragile coalition, and above all **the deliberate relinquishing of power** (resigning his commission, the two-term precedent). Kept complementary to FOUNDER_SECOND_TIER's business arcs.

## 4. One mini-batch or split?

**One curated mini-batch, no split.** Two Chernow biographies of foundational American leaders, same author, same historical-leadership register, both staged together. They belong together as the historical-biography lane. Precedent: the recovery lanes ran 2-3 sources per mini-batch. Per-source attribution preserved; Grant and Washington carry roughly equal weight (similar length). The combined size is large, so chunking is curated (a representative leadership/power pattern library), not exhaustive.

## 5. Recommended include / defer / exclude set

- **INCLUDE (2 · CORE):** Grant (Chernow) · `.epub`; Washington: A Life (Chernow) · `.pdf`.
- **DEFER:** none.
- **EXCLUDE (0 chunks):**
  - **Titan (Chernow · Rockefeller)** · already chunked in FOUNDER_SECOND_TIER · NOT re-chunked.
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor · not touched/staged/chunked).
  - Every other memoirs_biographies / canonical source already chunked (no re-chunking).

## 6. Recommended chunk target / range

- **Target:** ~14-18 chunks.
- **Range:** 10-20 (halt-and-report if outside).
- **Synthesis:** 1-2 closing synthesis chunks (the command-and-character + the relinquishing-of-power pattern + the optionality guardrail).
- **Provisional per-source split:** Grant ~7-8 + Washington ~7-8 + 1-2 synthesis. Rationale: two ~900-page lives warrant fuller-than-single-book coverage, but the lane stays curated (representative leadership patterns, not chapter-by-chapter). Both weighted roughly equally given comparable length.

## 7. Recommended domains (EXISTING domains only · NO new domain)

Verified against `MASTER_CHUNK_MAP.json.combined_domain_counts` (75 keys) before listing:

| Domain | Exists? | Count | Planned use in this lane |
|---|---|---:|---|
| `leadership` | YES | 40 | **Primary anchor.** Military command (Grant), command of a fragile coalition + republican leadership (Washington) · extends the existing BATCH_002/003 leadership home. |
| `power` | YES | 13 | **Co-anchor.** Washington's deliberate relinquishing of power (resigning the commission, the two-term precedent); Grant's command authority · the central historical-leadership lesson. |
| `strategy` | YES | 180 | Grant's total-war strategy and grasp of the whole theatre; Washington's Fabian strategic patience. |
| `operator-doctrine` | YES | 87 | The doctrine of persistence, clarity, delegation, and follow-through under pressure · plus the synthesis + optionality guardrail. |
| `operator-process` | YES | 76 | The working method · Grant's relentless logistics and plain orders; Washington's administrative discipline and institution-building. |
| `ethics` | YES | 41 | Character and integrity as leadership substance (routing the absent `character` domain here): Grant's magnanimity + the honest man undone by misplaced trust; Washington's restraint. |
| `culture` | YES | 54 | The founding-era / Civil-War / Reconstruction cultural context the leadership operated inside. |
| `founder-psychology` | YES (if warranted) | 31 | Only where a chunk is squarely about the leader's inner drive/psychology · used sparingly (links to the FOUNDER_SECOND_TIER cousins). |
| `systems-thinking` | YES (if warranted) | 45 | Only where warranted (Grant seeing the war as one system; Washington building durable institutions) · used sparingly. |

### Domain issue to flag (important)

- **`character`, `statecraft`, `governance` do NOT exist** in the corpus (ABSENT · the operator's "if it exists" conditions fail). **None will be created.** Routing: **character -> `leadership` / `ethics` / `operator-doctrine`**; **statecraft -> `strategy` / `leadership` / `power`**; **governance -> `strategy` / `operator-process` / `power`**.
- **`power` DOES exist (13)** and is the correct co-anchor (the operator's "if it exists" condition passes).
- **`leadership` (40) is the primary anchor** · this lane is its natural deepening into military + political leadership.
- **NO new domain will be created by default.** All planned domains pre-exist.

## 8. Connections (cross-references this lane opens)

- **FOUNDER_SECOND_TIER:** the company-building scale arcs · Grant + Washington are the public/military/political-leadership cousins (and Chernow's Titan already lives there · same author, distinguished register).
- **ONWARD_TURNAROUND:** the turnaround/repair-after-crisis pattern · Grant's wartime turnaround of a failing Union command and Washington's repeated recovery from near-defeat read against the operator turnaround arc.
- **MEDIA_BUSINESS_RECOVERY (and the operator/power lanes):** institutions converting position into durable power · the historical-leadership lens on how power is built, wielded, and (in Washington's case) deliberately surrendered.
- **ORIGINAL_SOURCE_COMPLETION_AUDIT:** this lane is step 1 of its recommended final sequence now that recovery is complete (the top remaining high-value book lane).
- **CURRENT_OPERATOR_REALITY_BRIEF:** every chunk references the brief in `sniped_relevance` and holds the lane as decision-support only (the brief is the read-first anchor · NOT a chunked source).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** the optionality discipline governs this lane (see §9-10).

## 9. Identity-optionality confirmation

This lane does NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks frame the biographies as a **pattern-library / decision-support lens read against CURRENT_OPERATOR_REALITY_BRIEF**, with the closing synthesis chunk(s) making the optionality discipline explicit. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 10. Historical biography = pattern-library / decision-support only (not a directive)

Grant and Washington are held strictly as a **pattern-library / decision-support layer**: transferable patterns of leadership, persistence, strategic patience, character under pressure, and the disciplined handling (and relinquishing) of power. They are **NOT a directive that BJ become a political, military, or public-leadership figure**, and not an endorsement of any era's politics. The leadership/power lessons are decoupled from their historical-political context and read as operator patterns. The `ethics` chunks keep character interpretive, not hagiographic (Grant's scandals and naivety, the moral complexity of the founding era, are part of the honest reading). Photography remains one option among several.

## 11. Deliverables for the future ship (NOT created now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/HISTORICAL_BIOGRAPHY_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/historical_biography_extracted/` (2 normalized .txt) |
| Summary | `01_KNOWLEDGE_BASE/summaries/HISTORICAL_BIOGRAPHY_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/HISTORICAL_BIOGRAPHY_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/HISTORICAL_BIOGRAPHY_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/HISTORICAL_BIOGRAPHY_COMPLETE.md` |
| Extraction script | `scripts/extract_historical_biography.py` |
| Chunk writer | `scripts/write_historical_biography_chunks.py` |

Schema: the canonical 12-field JSONL (chunk_id, batch_id, source_title, source_file, author, domain, concept, summary, usable_principle, sniped_relevance, direct_quotes, tags) · `batch_id` = `HISTORICAL_BIOGRAPHY` · per-source attribution (both Chernow, distinguished by title). Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · no new domain · Titan 0 · Bible 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality guardrail in every chunk · quote discipline · em-dash sweep).

## 12. Projected post-consolidation state (for reference · NOT applied now)

If shipped at the mid-target (~16) and consolidated: 1,531 + ~16 = ~1,547 chunks · 10 numbered batches + 26 mini-batches · 62 domains (NO new domain · bumps to leadership / power / strategy / operator-doctrine / operator-process / ethics / culture, plus founder-psychology / systems-thinking where warranted). Exact counts finalized at ship/consolidation time.

## 13. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,531.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `pdfinfo` / `ebook-convert`-and-`pdftotext`-to-/tmp · temp deleted).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No next lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 14. Next step (operator decision · do not start without authorization)

Authorize the HISTORICAL_BIOGRAPHY extract + chunk + validate step (2 sources · Grant epub + Washington pdf · target ~14-18 · existing domains only · `leadership` + `power` anchor · no new domain · `character`/`statecraft`/`governance` NOT created · Titan / Bible excluded), then commit the ship outputs, then authorize master-consolidation.
