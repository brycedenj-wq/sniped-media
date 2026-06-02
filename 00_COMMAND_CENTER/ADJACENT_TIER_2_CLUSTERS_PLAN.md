# ADJACENT_TIER_2_CLUSTERS mini-batch group · plan only · 2026-05-26

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document locates the candidates in the four remaining adjacent Tier-2 folders (leadership_mgmt, consulting_service, systems_thinking, expertise_creativity), probes extractability read-only, runs an authoritative already-chunked overlap check, classifies each candidate, recommends a grouped split architecture, names the first executable lane, and stops. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `afddf13 save session after FASHION_LUXURY_CULTURE consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,783 · 10 numbered batches + 43 mini-batches · 62 official domains (75 combined keys).
- **FASHION_LUXURY split complete** (FASHION_LUXURY_STRATEGY + FASHION_LUXURY_CULTURE both canonical) · **BRAND_CANON complete** · **TIER_2_GREENE_STRATEGY complete.**
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked (not in raw/, not tracked).

## 1. Candidate files located (verified · read-only `ls` / `stat`)

### 1a. leadership_mgmt (`raw/03_TIER_2_CANON_BOOKS/leadership_mgmt/` · 10 files)

| Source | Author | Format | Words (probe) | Status |
|---|---|---|--:|---|
| The Culture Code | Daniel Coyle | epub | 63,281 | CLEAN · NET-NEW |
| Leadership: In Turbulent Times | Doris Kearns Goodwin | epub | 195,517 | CLEAN · NET-NEW |
| Team of Rivals | Doris Kearns Goodwin | azw3 | 90,717 | CLEAN · NET-NEW |
| Extreme Ownership | Jocko Willink & Leif Babin | mobi | 84,758 | CLEAN · NET-NEW |
| The Dichotomy of Leadership | Jocko Willink & Leif Babin | epub | 96,028 | CLEAN · NET-NEW |
| Measure What Matters (OKRs) | John Doerr | epub | 71,642 | CLEAN · NET-NEW |
| Radical Candor | Kim Scott | epub | 93,384 | CLEAN · NET-NEW |
| Turn the Ship Around! | L. David Marquet | epub | 65,697 | CLEAN · NET-NEW |
| High Output Management | Andrew S. Grove | pdf | 68,084 | CLEAN · NET-NEW |
| Death by Meeting | Patrick Lencioni | txt | 1,131 | **SUMMARY STUB · EXCLUDE** (third-party abstract, not the full book) |

9 clean net-new books (~828,898 words). The `.txt` is a ~1,131-word third-party "Big Idea" summary (confirmed by reading it), NOT Lencioni's full text · exclude (re-acquire a clean epub if the full book is wanted).

### 1b. consulting_service (`raw/03_TIER_2_CANON_BOOKS/consulting_service/` · 7 files · all clean net-new)

| Source | Author | Format | Words (probe) | Status |
|---|---|---|--:|---|
| Value-Based Fees | Alan Weiss | pdf | 81,605 | CLEAN · NET-NEW |
| Million Dollar Consulting | Alan Weiss | pdf | 143,350 | CLEAN · NET-NEW |
| The McKinsey Way | Ethan M. Rasiel | pdf | 42,414 | CLEAN · NET-NEW |
| Managing the Professional Service Firm | David H. Maister | pdf | 126,173 | CLEAN · NET-NEW |
| Getting Naked | Patrick Lencioni | pdf | 47,421 | CLEAN · NET-NEW |
| The Advantage | Patrick Lencioni | pdf | 58,648 | CLEAN · NET-NEW |
| Flawless Consulting | Peter Block | epub | 107,028 | CLEAN · NET-NEW |

7 clean net-new books (~606,639 words). Note: Maister's *Managing the Professional Service Firm* is a different book from *The Trusted Advisor* (the latter is the source of the SNIPED Trust-Equation intel and is itself NOT chunked · net-new but not in these folders).

### 1c. systems_thinking (`raw/03_TIER_2_CANON_BOOKS/systems_thinking/` · 5 files · 4 distinct books)

| Source | Author | Format | Words (probe) | Status |
|---|---|---|--:|---|
| The Checklist Manifesto | Atul Gawande | epub | 56,799 | CLEAN · NET-NEW |
| Understanding Media (1994 · Extensions of Man) | Marshall McLuhan & Lewis Lapham | pdf | 121,372 | CLEAN · NET-NEW · **preferred copy** |
| Understanding media (1995, MIT · 15 MB) | Marshall McLuhan | pdf | 212,931 | CLEAN but OCR-inflated · **DUPLICATE TWIN · EXCLUDE** |
| Thinking in Systems: A Primer | Donella Meadows | pdf | 71,197 | CLEAN · NET-NEW |
| The Fifth Discipline | Peter M. Senge | pdf | 142,790 | CLEAN · NET-NEW |

4 distinct clean net-new books (~392,158 words using the cleaner 1994 McLuhan copy). The two McLuhan PDFs are the same book in two copies; recommend the 1994 Lapham/MIT 1 MB edition (cleaner text) and exclude the 15 MB 1995 twin (its 212,931-word count is inflated by OCR/double-text artifacts).

### 1d. expertise_creativity (`raw/03_TIER_2_CANON_BOOKS/expertise_creativity/` · 6 files · 4 clean distinct)

| Source | Author | Format | Words (probe) | Status |
|---|---|---|--:|---|
| Ways of Seeing | John Berger | epub | 22,532 | CLEAN · NET-NEW (short · illustrated essay) |
| The Creative Act: A Way of Being | Rick Rubin | epub | 47,357 | CLEAN · NET-NEW |
| Peak: Secrets from the New Science of Expertise | Anders Ericsson & Robert Pool | epub | 110,138 | CLEAN · NET-NEW |
| Talent Is Overrated | Geoff Colvin | pdf | 74,216 | CLEAN · NET-NEW |
| Dieter Rams: As Little Design as Possible | Sophie Lovell | epub | 0 | **BROKEN · image-only (71 MB monograph · 0 extractable text) · EXCLUDE** |
| Creativity: Flow and the Psychology of Discovery | Mihaly Csikszentmihalyi | djvu | 0 | **BROKEN · djvu unsupported · EXCLUDE (re-acquire epub)** |

4 clean net-new books (~254,243 words). Dieter Rams is an image-heavy design monograph with 0 extractable text (like Maus · exclude); Csikszentmihalyi's Creativity is the already-tracked broken `.djvu` (still-broken backlog · re-acquire a clean epub).

## 2. Source-quality / stub / scan / duplicate check (read-only `pdftotext` / `ebook-convert` probes to /tmp · temp deleted · mtimes unchanged)

- **24 clean, text-bearing net-new books** total across the four folders (~2.08M words combined).
- **Broken / excluded (3):** Death by Meeting (1,131-word summary stub), Dieter Rams (0 text · image-only), Creativity/Csikszentmihalyi (djvu · unsupported · already on the still-broken backlog).
- **Duplicate (1):** the two McLuhan *Understanding Media* PDFs are the same book; use the cleaner 1994 copy, exclude the 15 MB OCR-inflated twin.
- No OCR was run; no dependencies installed. `raw/` mtimes unchanged (May 15-18). At ship, sample each extracted .txt to confirm real book text before chunking.

## 3. Already-chunked overlap check (authoritative · by source_title / author across all 45 batch jsonls)

**All 24 clean candidate books are NET-NEW as sources (0 chunks each · verified).** Checked against OPERATING_FOUNDER (STARTUP/SCALING/OPERATIONS), BRAND_CANON, TIER_2_GREENE_STRATEGY, the full DECISION_JUDGMENT sequence, NETWORK_DISTRIBUTION, POSITIONING_DISRUPTION, HISTORICAL_BIOGRAPHY, MODERN_COMMAND_NAPOLEON, BATCH_002/003 (the Tier-1/Tier-2 canon), BATCH_005 (photography canon), and every other lane. No leadership / operator-doctrine / systems-thinking / consulting / expertise-adjacent lane already contains any of these 24 books.

**Adjacency findings (net-new books, conceptual overlap only · cross-reference, do NOT re-chunk the existing sources):**
- **Goodwin's Leadership / Team of Rivals (leadership-through-presidential-biography)** are adjacent to the already-canonical HISTORICAL_BIOGRAPHY (Grant + Washington / Chernow) and MODERN_COMMAND_NAPOLEON (Roberts) · net-new books, leadership register.
- **High Output Management (Grove)** is adjacent to OPERATING_FOUNDER_OPERATIONS (The Goal / Goldratt · operations-as-system) · net-new.
- **The McKinsey Way (problem-structuring)** is adjacent to DECISION_JUDGMENT_COGNITION (mental-models) and POSITIONING_DISRUPTION (The Mom Test / customer truth) · net-new.
- **Maister's Managing the Professional Service Firm** is adjacent to BATCH_003 (the SNIPED Trust-Equation intel from Maister's *The Trusted Advisor*, Guidara hospitality, Enns pricing) · net-new (different Maister book).
- **Peak (Ericsson) / Talent Is Overrated (Colvin)** (deliberate practice) are adjacent to TIER_2_GREENE_STRATEGY (Mastery / Greene · the apprenticeship-to-mastery arc) · net-new books, different authors.
- **Ways of Seeing (Berger)** is adjacent to BATCH_005 (the photography/aesthetics canon) and the SNIPED `intel_photo_theory` material (Berger's *The Suit and the Photograph* underpins the Direction Stack) · net-new as a chunked source · visual-perception register.
- **McLuhan's Understanding Media (media ecology)** is adjacent to MEDIA_BUSINESS / NETWORK_DISTRIBUTION and the distribution-mechanics intel · net-new.

## 4. Classification table

| Source | Cluster | Classification |
|---|---|---|
| The Culture Code, Leadership in Turbulent Times, Team of Rivals, Extreme Ownership, The Dichotomy of Leadership, Measure What Matters, Radical Candor, Turn the Ship Around!, High Output Management | leadership_mgmt | **net-new** (9) |
| Death by Meeting | leadership_mgmt | **broken / summary-stub** · exclude |
| Value-Based Fees, Million Dollar Consulting, The McKinsey Way, Managing the Professional Service Firm, Getting Naked, The Advantage, Flawless Consulting | consulting_service | **net-new** (7) |
| The Checklist Manifesto, Understanding Media (1994), Thinking in Systems, The Fifth Discipline | systems_thinking | **net-new** (4) |
| Understanding media (1995, 15 MB) | systems_thinking | **duplicate twin** · exclude |
| Ways of Seeing, The Creative Act, Peak, Talent Is Overrated | expertise_creativity | **net-new** (4) |
| Dieter Rams | expertise_creativity | **broken · image-only** · exclude |
| Creativity (Csikszentmihalyi) | expertise_creativity | **broken · djvu** · exclude / re-acquire |

## 5. Architecture recommendation: SPLIT into four register-appropriate sub-lanes (a grouped sequence)

The 24 clean books total **~2.08M words across four clearly distinct registers** · far too large and too heterogeneous for one mini-batch. Mirror the FASHION_LUXURY split and the OPERATING_FOUNDER (STARTUP / SCALING / OPERATIONS) and DECISION_JUDGMENT (COGNITION / CROWDS / MEANING) sequenced-sub-lane precedent. **Recommendation: four separate curated mini-batches, one per folder/register, each its own plan/ship/consolidate/session-save cycle**, grouped under the ADJACENT_TIER_2_CLUSTERS umbrella:

1. **LEADERSHIP_MGMT** · leadership_mgmt · 9 books · ~828,898 words · the leading-people / team-culture / management-system register.
2. **CONSULTING_SERVICE** · consulting_service · 7 books · ~606,639 words · the professional-services / consulting / client-craft / fee register.
3. **SYSTEMS_THINKING** · systems_thinking · 4 books · ~392,158 words · the systems-literacy / process / media-ecology register.
4. **EXPERTISE_CREATIVITY** · expertise_creativity · 4 books · ~254,243 words · the deliberate-practice / mastery / creative-craft / visual-perception register.

(Proposed batch_ids above are descriptive working names matching the folders; they are batch identifiers, NOT domains. The operator locks the final names at the first ship step. A `TIER_2_` prefix, e.g. `TIER_2_LEADERSHIP`, is an alternative consistent with the prior TIER_2_GREENE_STRATEGY naming.) A single mega-lane is NOT recommended.

## 6. Recommended first executable lane: CONSULTING_SERVICE

**Recommend CONSULTING_SERVICE as the first executable lane.** It is the most directly operator-relevant to BJ's CURRENT_OPERATOR_REALITY_BRIEF hypothesis space (which explicitly names *hybrid consulting / productized services*, *service-business automation*, and *documentation / SOP / reporting systems*) and to the brief's central question ("the highest-leverage business or offer that can emerge from BJ's real skills and ability to spot real-world pain"). The cluster covers how to package, price, structure, and deliver expertise as a solo/small practice (value-based fees, the problem-structuring method, managing a professional-services firm, client trust and loyalty, organizational health), which is the most actionable for a solo operator selling a service. It also deepens the existing Maister Trust-Equation / Enns pricing / Guidara hospitality intel.

**Equally-strong alternative first lane: LEADERSHIP_MGMT** (the largest, most canonical cluster) if the operator prefers leadership/management tooling first. SYSTEMS_THINKING and EXPERTISE_CREATIVITY are best sequenced after.

## 7. Include / defer / exclude set per cluster

| Cluster | INCLUDE (CORE · curated net-new) | EXCLUDE / DEFER |
|---|---|---|
| **LEADERSHIP_MGMT** | The Culture Code, Leadership in Turbulent Times, Team of Rivals, Extreme Ownership, The Dichotomy of Leadership, Measure What Matters, Radical Candor, Turn the Ship Around!, High Output Management (9) | Death by Meeting (1,131-word summary stub · re-acquire full book if wanted) |
| **CONSULTING_SERVICE** | Value-Based Fees, Million Dollar Consulting, The McKinsey Way, Managing the Professional Service Firm, Getting Naked, The Advantage, Flawless Consulting (7) | none |
| **SYSTEMS_THINKING** | The Checklist Manifesto, Understanding Media (1994 Lapham/MIT copy), Thinking in Systems, The Fifth Discipline (4) | the 15 MB 1995 McLuhan duplicate twin |
| **EXPERTISE_CREATIVITY** | Ways of Seeing, The Creative Act, Peak, Talent Is Overrated (4) | Dieter Rams (image-only · 0 text), Creativity/Csikszentmihalyi (djvu · re-acquire epub) |

Always excluded across all four lanes: the Bible (held SPIRITUAL_FOUNDATION anchor), CURRENT_IDENTITY / the held SNIPED-authored brand docs, and any already-canonical source.

## 8. Estimated chunk range per likely lane (curated · representative · NOT exhaustive)

| Lane | Books | ~Words | Target | Hard range | + synthesis |
|---|--:|--:|---|---|---|
| LEADERSHIP_MGMT | 9 | ~829K | ~15-17 | 13-18 | 1 optional |
| CONSULTING_SERVICE | 7 | ~607K | ~13-15 | 11-16 | 1 optional |
| SYSTEMS_THINKING | 4 | ~392K | ~11-13 | 9-14 | 1 optional |
| EXPERTISE_CREATIVITY | 4 | ~254K | ~10-12 | 8-13 | 1 optional |

Projected group total: **~49-57 chunks across 4 new mini-batches** (43 -> 47 mini-batches) · corpus ~1,783 -> ~1,832-1,840. Exact counts finalized at each ship/consolidation. Curated, not chapter-by-chapter.

## 9. Recommended domains per lane (EXISTING domains only · NO new domain · all verified present)

Verified to exist (current counts): `leadership` (55), `operator-doctrine` (126), `operator-process` (102), `systems-thinking` (54), `mental-models` (9), `decision-making` (18), `founder-psychology` (41), `strategy` (210), `commercial-architecture` (63), `culture` (68), `ethics` (55), `aesthetics` (85).

| Lane | Anchor | Secondary domains (existing only) |
|---|---|---|
| **LEADERSHIP_MGMT** | `leadership` | operator-process, operator-doctrine, culture, founder-psychology, ethics, strategy |
| **CONSULTING_SERVICE** | `operator-doctrine` | commercial-architecture, operator-process, ethics, mental-models, strategy, culture, founder-psychology |
| **SYSTEMS_THINKING** | `systems-thinking` | operator-process, mental-models, culture, operator-doctrine, strategy |
| **EXPERTISE_CREATIVITY** | `operator-doctrine` (deliberate practice / mastery) | `aesthetics` (strong · visual/creative craft), operator-process, mental-models, decision-making, culture |

Routing notes: leadership/team/ownership -> `leadership`; OKRs/output-systems/checklists/process -> `operator-process`; problem-structuring/diagnostics -> `mental-models`; fees/packaging/practice-economics -> `commercial-architecture`; client trust/loyalty/honesty -> `ethics`; org health/team culture/media-ecology -> `culture`; systems/feedback-loops/learning-organization -> `systems-thinking`; deliberate-practice/mastery/craft-philosophy -> `operator-doctrine`; visual perception/creative craft -> `aesthetics`; closing synthesis -> `operator-doctrine`.

### Domain issues to flag (important · tasks 12-15)

- **`creativity` DOES NOT EXIST and will NOT be created** (it is on the do-not-create list and is verified absent). All EXPERTISE_CREATIVITY creative/craft material routes to the existing `aesthetics` (85) and `operator-doctrine` (126). This is the same discipline applied to `taste` in BRAND_CANON (a token deliberately not created/used).
- **`systems` EXISTS as a thin domain (count 6) but is on the do-not-create list.** Systems-thinking material routes to the canonical, established `systems-thinking` (54), NOT to `systems`; this plan does not grow `systems`.
- **`management`, `consulting`, `service`, `expertise`, `innovation`, `productivity`, `business`, `self-help` do NOT exist and will NOT be created** (verified absent). Their material routes to the existing leadership / operator-doctrine / operator-process / commercial-architecture / mental-models / culture / ethics domains.
- **`mental-models` (9) and `decision-making` (18) are thin existing domains** · these lanes may reuse and grow them, NOT create anything new.
- **NO new domain will be created by any of the four lanes.** All planned domains pre-exist.

## 10. Connections (cross-references these lanes open · net-new books, conceptual ties only)

- **LEADERSHIP_MGMT <-> HISTORICAL_BIOGRAPHY (Grant/Washington) + MODERN_COMMAND_NAPOLEON + OPERATING_FOUNDER (the company-building arc) + TIER_2_GREENE_STRATEGY (power/human-nature):** the leadership/character register; Goodwin's presidential-leadership books extend the leadership-through-biography line. High Output Management ties to OPERATING_FOUNDER_OPERATIONS.
- **CONSULTING_SERVICE <-> BATCH_003 (Maister Trust Equation intel, Guidara hospitality, Enns pricing) + POSITIONING_DISRUPTION (The Mom Test) + the CURRENT_OPERATOR_REALITY_BRIEF hypothesis space (consulting / productized services / service-business automation):** the service-craft / pricing / client-trust register.
- **SYSTEMS_THINKING <-> OPERATING_FOUNDER_OPERATIONS (The Goal / constraints) + DECISION_JUDGMENT (mental-models) + the existing systems-thinking domain (origin LITERARY_CANON_DYSTOPIAN) + MEDIA_BUSINESS / NETWORK_DISTRIBUTION (McLuhan media ecology):** the systems-literacy / process register.
- **EXPERTISE_CREATIVITY <-> TIER_2_GREENE_STRATEGY (Mastery / deliberate practice) + STORYTELLING_NARRATIVE (aesthetics/craft) + BATCH_005 photography canon + `intel_photo_theory` (Berger / Ways of Seeing / The Suit and the Photograph):** the deliberate-practice / creative-craft / visual-perception register.
- **CURRENT_OPERATOR_REALITY_BRIEF + CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** the optionality guardrails and current-state anchor governing all four lanes.

## 11. Identity-optionality confirmation (task 18)

These lanes do NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks will frame the books as a **decision-support / pattern-library lens read against CURRENT_OPERATOR_REALITY_BRIEF**, applied to BJ's solo build-mode stage. It is **NOT a directive that BJ become a management guru, a consultant, a productivity influencer, a systems-theory account, a creativity coach, an expert-brand persona, or a corporate thought-leader.** The material is read as **operator tooling, diagnostic models, service craft, systems literacy, and creative skill-building.** Each lane's closing synthesis chunk will make the optionality discipline explicit. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted; the SNIPED-authored brand docs remain held.**

## 12. Bible exclusion (task 16)

**The KJV Bible was NOT touched, staged, or probed in this planning pass and will NOT be touched, staged, chunked, or included in any of the four lanes.** It is not present in `raw/` and not tracked in git · held separately as a reverent SPIRITUAL_FOUNDATION anchor in the source universe per NEW_SOURCE_INTAKE_PLAN.

## 13. Deliverables for each future ship (NOT created now · per-lane, mirroring the locked SOP)

For each of the four lanes `<LANE>` (e.g., CONSULTING_SERVICE first):
| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/<LANE>_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/<lane>_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/<LANE>_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/<LANE>_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/<LANE>_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/<LANE>_COMPLETE.md` |
| Extraction script | `scripts/extract_<lane>.py` |
| Chunk writer | `scripts/write_<lane>_chunks.py` |

Schema: the canonical 12-field JSONL · `chunk_id` pattern `<LANE>_NNN`. Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · curated · no new domain · the anchor per §9 · the do-not-create token list NOT created · the excluded/duplicate/broken sources 0 · already-canonical sources 0 · Bible 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality + not-a-directive guardrail in every chunk · quote discipline · em-dash sweep · curated-not-exhaustive).

## 14. Projected post-consolidation state (for reference · NOT applied now)

If all four lanes ship at mid-target and consolidate: 1,783 + ~49-57 = **~1,832-1,840 chunks** · 10 numbered batches + **47 mini-batches** · **62 domains (NO new domain** · growth across leadership / operator-doctrine / operator-process / systems-thinking / mental-models / decision-making / founder-psychology / strategy / commercial-architecture / culture / ethics / aesthetics). Exact counts finalized at ship/consolidation. After this group, the adjacent Tier-2 backlog is closed; remaining items: the optional operator-docs cleanup, the fresh current SNIPED brief / CURRENT_IDENTITY principle-only ship, the SPIRITUAL_FOUNDATION decision, and the broken-backlog re-acquisitions (Caples, Five Rings, Denial of Death, Creativity/Csikszentmihalyi, Story-McKee, Traction).

## 15. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,783.
- Did NOT modify any `raw/` or source file (read-only `ls` / `stat` / `file` / `pdftotext`+`ebook-convert`-to-/tmp · temp deleted · all mtimes unchanged · May 15-18).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created (and verified that `creativity` does not exist and must not be created; `systems` exists but will not be grown).
- No lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 16. Next step (operator decision · do not start without authorization)

Authorize the **CONSULTING_SERVICE** first lane (7 net-new professional-services books · `operator-doctrine` anchor · existing domains only · no new domain · target ~13-15 · the Death by Meeting summary stub, the McLuhan duplicate, Dieter Rams + Creativity/Csikszentmihalyi broken sources excluded · the Bible excluded · read decision-neutrally as operator tooling / service craft, NOT a directive that BJ become a consultant or expert-brand persona). Then ship -> consolidate -> session-save, then proceed to LEADERSHIP_MGMT, SYSTEMS_THINKING, and EXPERTISE_CREATIVITY as their own plan/ship/consolidate/save cycles. (Equally valid: start with LEADERSHIP_MGMT if the operator prefers the leadership cluster first.)
