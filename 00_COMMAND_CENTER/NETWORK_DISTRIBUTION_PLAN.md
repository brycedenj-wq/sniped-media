# NETWORK_DISTRIBUTION mini-batch · plan only · 2026-05-25

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document locates the network_distribution backlog, verifies extractability and already-chunked overlap, recommends a single curated lane, names the include/defer/exclude set, and stops. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `96992be save session after OPERATING_FOUNDER_OPERATIONS consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,649 · 10 numbered batches + 33 mini-batches · 62 official domains (75 combined keys).
- **Recovery program complete; classical block complete; historical-biography complete; the OPERATING_FOUNDER sequence COMPLETE** (STARTUP + SCALING + OPERATIONS). NETWORK_DISTRIBUTION is the next lane named in the ORIGINAL_SOURCE_COMPLETION_AUDIT remaining backlog.
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate files located in raw/ (verified)

**In the expected folder `raw/02_TIER_1_CANON_BOOKS/network_distribution/` (5 files):**

| Source | Author | Format | Words (probe) | Status |
|---|---|---|--:|---|
| The Inevitable: Understanding the 12 Technological Forces... | Kevin Kelly | epub | 108,050 | CLEAN |
| New Rules for the New Economy: 10 Radical Strategies for a Connected World | Kevin Kelly | pdf | 61,079 | CLEAN |
| The Long Tail (Revised): Why the Future of Business is Selling Less of More | Chris Anderson | epub | 75,305 | CLEAN |
| Free: The Future of a Radical Price (Abridged) | Chris Anderson | pdf | 74,656 | CLEAN |
| The Great Online Game (Not Boring) | Packy McCormick | pdf | 4,343 | CLEAN · SHORT essay (see note) |

**Adjacent network-effects book physically OUTSIDE the folder (in `raw/02_TIER_1_CANON_BOOKS/` root):**

| Source | Author | Format | Words (probe) | Status |
|---|---|---|--:|---|
| The Cold Start Problem: How to Start and Scale Network Effects | Andrew Chen | epub | 101,945 | CLEAN **but ALREADY CHUNKED (BATCH_002 · 5 chunks · `network-effects` domain)** · EXCLUDE |

Read-only `pdftotext` / `ebook-convert`-to-/tmp probes (temp deleted; all mtimes unchanged). **5 clean net-new sources in the folder · ~323,433 combined words** (excluding the already-canonical Cold Start Problem).

## 2. Source-quality / stub / scan check

- **5 clean, text-bearing net-new sources** (word counts above). The epubs (Inevitable, Long Tail) extract via `ebook-convert`; the pdfs (New Rules, Free, Great Online Game) via `pdftotext`. No OCR needed. Content sanity confirmed by first-page samples (FREE/Anderson title page; Long Tail TOC "THE RISE AND FALL OF THE HIT"; "Kevin Kelly -- New Rules for the New Economy"; "ALSO BY KEVIN KELLY Out of Control"; "The Great Online Game How to Win the Internet... Not Boring").
- **Note (The Great Online Game / McCormick):** this is a **single ~4,343-word essay/newsletter** (Packy McCormick's "Not Boring" piece), not a book; the 7.4 MB PDF is image/graphic-heavy. It is a high-signal synthesis essay on the network/status/online-economy thesis. **It contributes at most 1-2 chunks** and is best used as the contemporary capstone reading, NOT padded to book weight. At ship, sample each extracted .txt to confirm real text before chunking.
- **No broken/stub files** in the network_distribution folder. (Traction, the tactical 19-channels distribution book, is broken 0-byte and sits in `operating_founder/`, not here · see §5.)

## 3. Already-chunked overlap check (verified · authoritative by source_title / author / source_file)

A precise check (matching `source_title` + `author` + `source_file` fields, not incidental text mentions) across all 34 batch jsonls:

- **The Inevitable (Kelly):** 0 chunks as a source · **NET-NEW.**
- **New Rules for the New Economy (Kelly):** 0 chunks as a source · **NET-NEW.**
- **The Long Tail (Anderson):** 0 chunks as a source · **NET-NEW.** (The "Long Tail" / "Chris Anderson" substring hits in BATCH_001/003/CULTURE_AND_STATUS are incidental text mentions, NOT a chunked source.)
- **Free (Anderson):** 0 chunks as a source · **NET-NEW.**
- **The Great Online Game (McCormick):** 0 chunks as a source · **NET-NEW.**
- **The Cold Start Problem (Andrew Chen):** **ALREADY A SOURCE in BATCH_002** (5 chunks · `network-effects` domain · chunk ids batch-002-chunk-101..). **EXCLUDE** · do NOT re-chunk.

Cross-lane distinctness:
- **Distinct from OPERATING_FOUNDER_STARTUP / SCALING / OPERATIONS** (the build/scale/operate registers · Ries, Horowitz, Wasserman, Hoffman, Slootman, Goldratt, Hammer, Gerber, Warrillow) · no title overlap.
- **Distinct from ADVERTISING_RECOVERY** (Ogilvy, Sugarman, Halbert · copy craft) and **MEDIA_BUSINESS_RECOVERY** (Hit Men, The Mailroom · music/film institutions) · no title overlap; the Long Tail's media-distribution material is the economics of distribution, not the institutional histories.
- **Distinct from HIGH_LEVEL_CONVOS** (Earn Your Leisure transcripts) · no title overlap.
- **Distinct from BATCH_002's `network-effects` material** (Cold Start Problem) and from MEDIA_BUSINESS / strategy lanes · this is the network-economics / distribution-economics thesis register (Kelly's connected-economy + Anderson's distribution economics + McCormick's online-game synthesis), a coherent net-new lane.

## 4. Architecture recommendation: ONE curated mini-batch (no split, do NOT defer)

The 5 net-new sources form **one coherent register**: the economics of networks and distribution in a connected economy. Kelly (New Rules + The Inevitable) supplies the connected-world / network-economics and technological-forces thesis; Anderson (The Long Tail + Free) supplies the distribution economics (niche aggregation, the long tail, the economics of free/cross-subsidy); McCormick (The Great Online Game) is the contemporary synthesis capstone. ~323K words across 5 sources is a normal single-lane size for the corpus (comparable to OPERATING_FOUNDER_OPERATIONS's ~327K / 4 sources / 14 chunks). **No split is warranted** (it is one register, not four), and **no deferral is warranted** (the lane is complete and coherent on its own; it does NOT depend on Traction).

**On Traction (the deferral question, task 5):** Traction (Weinberg/Mares · the tactical "19 distribution channels" playbook) is a 0-byte broken epub in `operating_founder/`. It is a DIFFERENT sub-register (tactical channel-selection, not network/distribution economics). This lane does **NOT** need to wait for Traction. When Traction is re-acquired, it can seed a future tactical-distribution addendum (or fold into a NETWORK_DISTRIBUTION_TACTICS sub-lane) · noted, not blocking.

## 5. Recommended first (and only) lane: NETWORK_DISTRIBUTION (include / defer / exclude)

- **INCLUDE (5 · CORE · curated · the network/distribution-economics register):**
  - The Inevitable (Kevin Kelly) · epub · ~108,050 words.
  - New Rules for the New Economy (Kevin Kelly) · pdf · ~61,079 words.
  - The Long Tail (Chris Anderson) · epub · ~75,305 words.
  - Free (Chris Anderson · Abridged) · pdf · ~74,656 words.
  - The Great Online Game (Packy McCormick) · pdf · ~4,343 words · the short capstone essay (1-2 chunks).
  - Combined ~323,433 words · curated, not exhaustive.
- **DEFER:**
  - **Traction (Weinberg/Mares):** 0-byte broken epub in `operating_founder/` · re-acquire · a future tactical-distribution-channels addendum (different sub-register · not blocking).
- **EXCLUDE (0 chunks):**
  - **The Cold Start Problem (Andrew Chen):** ALREADY chunked in BATCH_002 (`network-effects`) · do NOT re-chunk.
  - **`raw/13_NETWORK/access_and_community_architecture.md`, `The_Platform_Stack.docx`, `raw/14_WEB/website-seo/references/platform-ranking.md`:** SNIPED-authored / operational docs (identity-side or website build kit), NOT books · out-of-scope for this book lane (the Stack docs are already represented via the SNIPED-OS depth batches; the 13_NETWORK md is identity/community-side, held).
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor).
  - Every already-canonical source and every other-cluster source (OPERATING_FOUNDER / ADVERTISING_RECOVERY / MEDIA_BUSINESS(_RECOVERY) / HIGH_LEVEL_CONVOS / the classical block / sales_positioning / decision_judgment / brand-canon / Tier-2). CURRENT_IDENTITY sources.

## 6. Recommended chunk target / range

- **Target:** ~15-17 chunks · **Range:** 13-19 (halt-and-report if outside).
- **Synthesis:** 1 closing synthesis chunk (the network/distribution-economics toolkit + the optionality guardrail).
- **Provisional per-source split:** The Inevitable ~4 · New Rules ~3 · The Long Tail ~3-4 · Free ~3 · The Great Online Game ~1-2 · + 1 synthesis. Curated/representative from ~323K words, NOT chapter-by-chapter (the McCormick essay is short and contributes 1-2 only).

## 7. Recommended domains (EXISTING domains only · NO new domain)

Verified to exist (current counts): `distribution` (9), `network-effects` (5), `strategy` (200), `commercial-architecture` (57), `systems-thinking` (50), `operator-doctrine` (107), `operator-process` (93), `media-business` (10), `culture` (58), `status` (15), `ethics` (49).

| Domain | Planned use in this lane |
|---|---|
| `distribution` (anchor) | The lane's through-line: how things spread and sell in a connected economy · the long tail (selling less of more), the economics of free / cross-subsidy as distribution, the aggregation of niche demand, abundance-driven distribution. |
| `network-effects` (existing · plural) | Kelly's network economics (increasing returns, the network as the unit of value, "follow the free"), the connected-world compounding dynamics, McCormick's online-game network framing. **Reuses the EXISTING `network-effects` domain (count 5, from BATCH_002); the forbidden singular `network-effect` is a DIFFERENT string and will NOT be created.** |
| `strategy` | The "10 radical strategies," the long-tail strategy, free-as-strategy, the strategic posture toward the connected economy. |
| `commercial-architecture` | Freemium / cross-subsidy / long-tail business-model architecture · the revenue/structure layer beneath the distribution thesis. |
| `systems-thinking` | Kelly's technological-forces systems view (the 12 forces · the connected world as an emergent system) · used where squarely systemic. |
| `operator-doctrine` | The disciplined synthesis (the closing chunk) and the optionality-guarded reading. |
| `media-business` (if warranted) | The Long Tail's media/content distribution economics (the niche-content/attention layer) · used only where clearly media-distribution, NOT padded. |
| `culture` / `status` (if warranted) | McCormick's "great online game" status/identity-in-public framing · used only if squarely present (likely 0-1). |
| `operator-process` / `ethics` (if warranted) | process-mechanics or a squarely-present moral dimension · used only where clearly warranted (likely 0-1). |

**Recommended anchor:** `distribution` (the lane's namesake and through-line), with `network-effects` + `strategy` the strong secondaries.

### Domain issues to flag (important)

- **`network-effects` (plural) ALREADY EXISTS** (count 5 · introduced by BATCH_002's The Cold Start Problem). It is a permitted existing domain and will be REUSED, not created. **The operator's forbidden list names `network-effect` (singular) · that is a different string and will NOT be created.** Network material routes to the existing plural `network-effects`.
- **`network`, `platform`, `platform-strategy`, `growth`, `marketing`, `startup`, `business` do NOT exist and will NOT be created** · network material -> `network-effects` / `strategy` / `systems-thinking`; platform/platform-strategy material -> `commercial-architecture` / `strategy`; growth material -> `strategy` / `operator-process`; marketing material -> `distribution` / `strategy` / `commercial-architecture`; startup/business material -> `operator-doctrine` / `commercial-architecture`.
- **`economics` does NOT exist** (ABSENT · verified). It will NOT be created · the free/long-tail/connected-economy economics route to `distribution` / `commercial-architecture` / `strategy` / `systems-thinking`.
- **NO new domain will be created by default.** All planned domains pre-exist.

## 8. Connections (cross-references this lane opens)

- **OPERATING_FOUNDER (STARTUP + SCALING + OPERATIONS):** the build/scale/operate registers · NETWORK_DISTRIBUTION is the how-it-reaches-and-compounds companion (how an offer spreads in a connected economy · same `strategy` / `commercial-architecture` family · the distribution layer beyond the build).
- **ADVERTISING_RECOVERY:** the message/copy craft · this is the structural distribution layer the message travels through (paid attention vs network/organic distribution).
- **MEDIA_BUSINESS_RECOVERY (+ MEDIA_BUSINESS):** the institutional attention/distribution machinery (ESPN/SNL/HBO, music/film) · the Long Tail's media-distribution economics reads against the institutional histories (`media-business` family).
- **HIGH_LEVEL_CONVOS:** the practical operator lessons on audience/creator-economy/media-ownership · this supplies the book-grade network/distribution economics beneath those transcripts.
- **BATCH_002 (The Cold Start Problem · `network-effects`):** the existing network-effects how-to-start-and-scale source · NETWORK_DISTRIBUTION is the distribution-economics companion that reuses (and modestly grows) the same `network-effects` domain.
- **CURRENT_OPERATOR_REALITY_BRIEF:** every chunk references the brief in `sniped_relevance` and holds the lane as decision-support only (the brief is the read-first anchor · NOT a chunked source).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** the optionality discipline governs this lane; CURRENT_IDENTITY remains plan-only / NOT extracted.

## 9. Identity-optionality confirmation

This lane does NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks frame the books as a **decision-support / pattern-library lens read against CURRENT_OPERATOR_REALITY_BRIEF**, with the closing synthesis chunk making the optionality discipline explicit. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 10. Network/distribution material = decision-support / pattern-library only (not a directive)

The Inevitable, New Rules for the New Economy, The Long Tail, Free, and The Great Online Game are held strictly as a **decision-support / pattern-library layer**: transferable patterns of how value spreads, compounds, and is distributed in a connected economy (network effects / increasing returns, niche aggregation / the long tail, the economics of free and cross-subsidy, the technological forces shaping distribution, the online "game" of building in public). It is **NOT a directive that BJ build a platform, a marketplace, a SaaS company, a media network, an agency, or a growth-hacking business**, and not a mandate to chase network-effects, "go viral," monetize via freemium, or productize attention. The methods are read as a transferable distribution/economics lens decoupled from the specific tech/platform context that produced them, applied to BJ's actual stage (a solo field-engineer in build-mode, loading the backend before final brand/offer/company-architecture decisions). Photography remains one option among several.

## 11. Deliverables for the future ship (NOT created now)

For the recommended lane (batch_id `NETWORK_DISTRIBUTION`):

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/NETWORK_DISTRIBUTION_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/network_distribution_extracted/` (5 normalized .txt) |
| Summary | `01_KNOWLEDGE_BASE/summaries/NETWORK_DISTRIBUTION_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/NETWORK_DISTRIBUTION_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/NETWORK_DISTRIBUTION_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/NETWORK_DISTRIBUTION_COMPLETE.md` |
| Extraction script | `scripts/extract_network_distribution.py` |
| Chunk writer | `scripts/write_network_distribution_chunks.py` |

Schema: the canonical 12-field JSONL · `batch_id` = `NETWORK_DISTRIBUTION` · `chunk_id` pattern `NETWORK_DISTRIBUTION_NNN`. Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · 5 sources · no new domain · `distribution` anchor · `network-effects` reused-not-created · `network`/`network-effect`[singular]/`platform`/`platform-strategy`/`growth`/`marketing`/`startup`/`business` NOT created · The Cold Start Problem 0 [already BATCH_002] · Traction deferred/broken · SNIPED-authored network/platform docs 0 · Bible 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality + not-a-directive guardrail in every chunk · quote discipline · em-dash sweep · curated-not-exhaustive).

## 12. Projected post-consolidation state (for reference · NOT applied now)

If the lane ships at the mid-target (~16) and consolidates: 1,649 + ~16 = ~1,665 chunks · 10 numbered batches + 34 mini-batches · 62 domains (NO new domain · bumps to `distribution` [anchor] / `network-effects` / `strategy` / `commercial-architecture` / `systems-thinking` / `operator-doctrine`, plus `media-business` / `culture` / `status` where warranted). Exact counts finalized at ship/consolidation time. Subsequent lanes: SALES_POSITIONING (post BATCH_009/EXPANSION overlap audit), DECISION_JUDGMENT, Tier-2 (incl the Greene trio), BRAND_CANON.

## 13. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,649.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `pdftotext`+`ebook-convert`-to-/tmp · temp deleted).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created (and the existing `network-effects` distinguished from the forbidden singular `network-effect`).
- No lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 14. Next step (operator decision · do not start without authorization)

Authorize the **NETWORK_DISTRIBUTION** lane (5 curated net-new sources · The Inevitable + New Rules for the New Economy + The Long Tail + Free + The Great Online Game · target ~15-17 · existing domains only · `distribution` anchor · `network-effects` reused-not-created · no new domain · network/network-effect[singular]/platform/platform-strategy/growth/marketing/startup/business NOT created · The Cold Start Problem excluded [already BATCH_002] · Traction deferred/broken · Bible excluded · curated, not exhaustive · decision-support not a directive), then commit the ship outputs, then consolidate. The Traction tactical-distribution addendum follows only after re-acquisition.
