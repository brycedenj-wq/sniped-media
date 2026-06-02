# MEDIA_BUSINESS mini-batch · PLAN

**Date planned:** 2026-05-23
**Status:** PLAN ONLY · not extracted, not chunked, master files untouched, not committed.
**Batch kind:** mini-batch (descriptive slug · the 16th mini-batch).

> **OPERATOR DECISIONS APPLIED (2026-05-23 · locked):**
> 1. **FLAG 0 RESOLVED.** `CURRENT_OPERATOR_REALITY_BRIEF.md` now exists and is committed (`ca5c4db`). It is a read-first current-state anchor, NOT chunked doctrine. MEDIA_BUSINESS must respect it (do not let stale SNIPED Media / BASEPLATE / photography-only assumptions override current reality).
> 2. **NEW domain `media-business` APPROVED** (the 62nd · registers at consolidation). `media`, `entertainment`, `programming` NOT created.
> 3. **3 CORE sources locked** (section 4): ESPN (Those Guys Have All the Fun), SNL (Live From New York), HBO (Tinderbox).
> 4. **Recovery/defer:** Hit Men (scanned) and The Mailroom (`.djvu`) remain recovery · not chunked.
> 5. **Exclude:** BIOGRAPHY_FOUNDER_MEDIA core, BATCH_010 culture, CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources, recovery/acquisition items.
> 6. **Identity optionality preserved** · media-business patterns are decision-support lenses only, NOT a directive that SNIPED becomes a media company · no final SNIPED / SNIPED Media / BASEPLATE direction.

---

## 0. Verified starting state

- **Head commit at planning:** `5f7c3f9` (BFM session save); the **`ca5c4db` CURRENT_OPERATOR_REALITY_BRIEF anchor** was committed immediately after (FLAG 0 resolved).
- **Working tree:** clean (only this plan uncommitted).
- **Total chunks:** 1,354 · 10 numbered batches + 15 mini-batches · 61 official domains (74 combined_domain_counts keys).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **No lane started:** no `MEDIA_BUSINESS_CHUNKS.jsonl`, no extracted dir, no COMPLETE marker.

### FLAG 0 · RESOLVED: CURRENT_OPERATOR_REALITY_BRIEF now exists
`00_COMMAND_CENTER/CURRENT_OPERATOR_REALITY_BRIEF.md` was created and committed (`ca5c4db`). It is the **read-first current-state anchor** (NOT chunked doctrine): SNIPED = BJ's active identity/container; SNIPED Media = the existing photography company; BASEPLATE = a possible historical rebrand asset, not the decided future; BJ = a solo field-engineer/data-center operator in ideation/build mode loading the backend before final brand/offer/company-architecture decisions. **MEDIA_BUSINESS respects it:** media-empire patterns are held as decision-support lenses against current reality, never as a directive, and they do not force the answer into photography, BASEPLATE, or a media company.

---

## 1. Goal + theme

Media-business infrastructure, attention networks, programming, talent systems, cultural institutions, entertainment economics, platform/story machinery, creative leadership, audience trust, distribution, and how media empires turn taste, access, talent, and timing into durable power. The source set is the media-business cluster deferred from BIOGRAPHY_FOUNDER_MEDIA (ESPN, SNL, HBO).

---

## 2. Candidate inventory (`raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/`)

| File | Subject | Type | Words | Status |
|---|---|---|--:|---|
| Those Guys Have All the Fun (Miller/Shales, 2011) | ESPN · the network's oral history | epub | 308,626 | net-new |
| Live From New York (Shales/Miller, 2003) | SNL · uncensored oral history | epub | 234,076 | net-new |
| Tinderbox (James Andrew Miller) | HBO · the channel's ruthless rise | mobi | (ebook-convert) | net-new |
| Hit Men (Fredric Dannen, 1991) | music-business power brokers | pdf | **0 (SCANNED)** | **BROKEN · recovery** |
| The Mailroom (David Rensin, 2003) | Hollywood agents from the bottom up | djvu | (blocked) | **BROKEN format · recovery** |

No other media-business sources elsewhere in raw/ (the "hollywood" matches are photography lighting PDFs and a Virgil Abloh design lecture txt · out of scope). The Abloh lecture is a creative-direction artifact, not media-business infrastructure · not included.

---

## 3. Pre-flight peek · source quality

- **Net-new:** all 5 verified net-new (0 chunked source-refs). None overlap BIOGRAPHY_FOUNDER_MEDIA core (Vreeland/Instagram/Branson/Kroc/Netflix/Sony) or BATCH_010 culture sources.
- **Broken / recovery (report-only · 0 chunks):** Hit Men (scanned pdf · 0 words via pdftotext); The Mailroom (`.djvu` · blocked). Both remain recovery flags · re-acquire clean text editions.
- **mobi (needs `ebook-convert` · calibre on PATH · no OCR):** Tinderbox (HBO).
- **Large but real text:** Those Guys Have All the Fun (308,626 words) and Live From New York (234,076 words) are clean epub oral histories · very long.
- **Image-heavy:** none among the usable CORE.
- **Recovery/acquisition items:** untouched (reported only).

---

## DOMAIN DECISION (LOCKED · per requirement #6-7)

### 6. `media-business` did NOT exist as an official domain
Checked `combined_domain_counts`: `media-business`, `media`, `entertainment`, `programming` were all **MISSING**. `distribution` EXISTS (9); `culture` (42), `commercial-architecture` (40), `content-strategy` (51), `strategy` (164), `brand` (31), `founder-psychology` (22), `operator-process` (65), `systems-thinking` (37), `capital` (9) all exist.

### 7. DECISION: approve ONE new domain `media-business` (the 62nd)
**Operator approved exactly ONE new domain: `media-business`** (entertainment/media economics, programming, talent systems, networks, cultural institutions, attention/distribution at media-empire scale). On ship + consolidation the official domain count goes **61 to 62**. **`media`, `entertainment`, `programming` are NOT created** (too generic / redundant with content-strategy + the new media-business domain). This mirrors the deliberate single-new-domain approval used for `capital`. Any further candidate new domain at chunk time must halt and re-surface to the operator. No other new domain.

---

## 4. Recommended inclusion / defer / exclude

### INCLUDE · CORE · 3 sources (LOCKED)
- **Those Guys Have All the Fun** (ESPN), **Live From New York** (SNL), **Tinderbox** (HBO). All net-new, on-theme, the deferred media-business cluster. (Tinderbox needs `ebook-convert` from mobi.)

### DEFER / RECOVERY (report-only)
- **Hit Men** (scanned pdf · music-business power brokers) and **The Mailroom** (`.djvu` · Hollywood agents) · re-acquire clean editions, then a later media-business expansion.

### EXCLUDE
- BIOGRAPHY_FOUNDER_MEDIA core (already chunked) · BATCH_010 culture sources (already chunked) · the Virgil Abloh lecture txt (off-theme · creative-direction, not media-business) · CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources.

---

## 5. Estimated chunk yield

3 large oral histories, ~5-6 chunks each + 1-2 synthesis:

| Source | Chunks |
|---|--:|
| Those Guys Have All the Fun (ESPN) | 5-6 |
| Live From New York (SNL) | 5-6 |
| Tinderbox (HBO) | 4-5 |
| cross-source synthesis | 1-2 |

**Target: ~14-20 chunks. Acceptable range: 12-24.** ID pattern `MEDIA_BUSINESS_NNN`. 1-2 synthesis chunks.

---

## 6. Domain set (LOCKED)

**ONE new domain `media-business`** (anchor · operator-approved) + existing `culture`, `commercial-architecture`, `content-strategy`, `strategy`, `brand`, `founder-psychology`, `operator-process`, `systems-thinking`. `distribution` (existing · 9) may take the audience/distribution chunks. `capital` only if a genuinely capital/ownership chunk appears (light). **`media`, `entertainment`, `programming` are NOT created.**

Indicative distribution: media-business ~7 · culture ~3 · commercial-architecture ~3 · content-strategy ~2 · strategy ~2 · brand ~1 · founder-psychology ~1 · operator-process ~1. Finalized at chunk time.

---

## 7. NEW domain decision (LOCKED)

`media-business`, `media`, `entertainment`, `programming` were all MISSING. **Operator approved exactly ONE new domain: `media-business`** (the 62nd · registers at consolidation · 61 to 62). `media`, `entertainment`, `programming` are NOT created. No other new domain · any candidate new domain at chunk time must halt and re-surface to the operator.

---

## 8. How this mini-batch connects to the corpus

- **CURRENT_OPERATOR_REALITY_BRIEF (NOT YET CREATED · see FLAG 0):** intended anchor for current reality (solo operator, ideation stage, Canon R6 Mark II) · this lane is media-business pattern-library held against that reality once written · reconcile when it exists.
- **BIOGRAPHY_FOUNDER_MEDIA:** the founder/operator arcs (incl. Instagram platform media) · MEDIA_BUSINESS is the institutional/infrastructure layer above the individual arc (how networks and channels are built and run).
- **BATCH_010 lineage + Black culture canon:** the Black-music/culture lineage · complementary; Hit Men (music business · recovery) would later bridge them.
- **BATCH_009 / BATCH_009_EXPANSION:** positioning/category/distribution theory · here enacted at media-empire scale (programming as category creation, distribution as the moat).
- **MONEY_OWNERSHIP:** the capital/ownership economics · media empires are capital + talent + distribution compounded (HBO/ESPN as ownership-of-attention).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** media-empire patterns are decision-support lenses, NOT a directive that SNIPED becomes a media company · optionality preserved.
- **Future SNIPED direction (without deciding it):** supplies institution-building and attention-network patterns the operator can draw from · reversible inputs.

---

## 9. This lane does NOT finalize brand direction

Confirmed. MEDIA_BUSINESS chunks media-business institutional histories as pattern-library / decision-support. It does **not** decide SNIPED, SNIPED Media, or BASEPLATE direction, does not commit the operator to building a media company, and does not prescribe a path. Per the active guardrails, `sniped_relevance` frames the patterns as lenses (how these institutions turned taste/access/talent/timing into durable power), with SNIPED's direction undecided and photography one option among several.

---

## 10. Deliverables (produced only at the authorized ship step · NOT now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/MEDIA_BUSINESS_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/media_business_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/MEDIA_BUSINESS_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/MEDIA_BUSINESS_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/MEDIA_BUSINESS_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/MEDIA_BUSINESS_COMPLETE.md` |
| Extract script | `scripts/extract_media_business.py` (epub via stdlib zipfile · mobi via ebook-convert for Tinderbox) |
| Chunk writer | `scripts/write_media_business_chunks.py` |

Schema: the canonical 12-field JSONL. `batch_id` = `MEDIA_BUSINESS`. source_file values resolve under `media_business_extracted/`. Copyright-safe quote discipline: in-copyright trade books · short illustrative lines only (target longest <= 14 words) · most chunks paraphrase. No OCR · ebook-convert (calibre) is on PATH for the one mobi (no new dependency).

---

## Constraints honored by this plan

- Did NOT extract, chunk, update master files, or commit.
- Did NOT modify any `raw/` source file · recovery/acquisition items reported only, untouched.
- No em-dashes.
- **No new domain created** · the `media-business` decision is flagged for the operator (requirement #7-9).
- Does not finalize SNIPED / SNIPED Media / BASEPLATE direction (optionality preserved).
- Surfaced the missing CURRENT_OPERATOR_REALITY_BRIEF rather than fabricating it.
- Stops at the plan.

## Open questions · ALL RESOLVED (2026-05-23)

1. **CURRENT_OPERATOR_REALITY_BRIEF:** RESOLVED · the brief now exists and is committed (`ca5c4db`) · read-first current-state anchor, not chunked doctrine · MEDIA_BUSINESS respects it.
2. **DOMAIN:** RESOLVED · approve ONE new domain `media-business` (the 62nd) · `media`/`entertainment`/`programming` NOT created.
3. **CORE:** RESOLVED · the 3 net-new books (ESPN, SNL, HBO/Tinderbox) · Tinderbox via ebook-convert from mobi.
4. **Recovery:** RESOLVED · Hit Men (scanned) + The Mailroom (djvu) stay recovery / deferred.
5. **Target band:** ~14-20 chunks (range 12-24).

Plan is ready to ship on authorization (extract -> chunk -> validate -> consolidate). The ship will register `media-business` as the 62nd official domain.
