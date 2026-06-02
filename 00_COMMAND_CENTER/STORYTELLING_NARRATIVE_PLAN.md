# STORYTELLING_NARRATIVE mini-batch · plan only · 2026-05-25

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document inventories the storytelling/narrative candidate files, probes extractability, runs an authoritative already-chunked overlap check, recommends a batch architecture, names the first lane, and stops. Nothing is extracted or chunked here.

## Operator decision (LOCKED 2026-05-25): Option 2 SELECTED

The operator selected **Option 2** as the source set for the STORYTELLING_NARRATIVE lane: **4 clean sources** as one curated mini-batch.

- **INCLUDE (4 · SELECTED):** The Anatomy of Story (John Truby) · The Hero with a Thousand Faces (Joseph Campbell) · Save the Cat! (Blake Snyder) · **The Visual Story (Bruce Block)**.
- **The Visual Story is locked IN** because visual narrative structure (contrast/affinity, the visual components, visual intensity, controlling the visual story across a sequence) is directly relevant to BJ's visual/operator work · it is the visual-craft companion to the three written-story books.
- **DEFER:** Story (Robert McKee) · broken scanned PDF · 0 words · no OCR · re-acquire.
- **EXCLUDE:** Building a StoryBrand (already canonical · BATCH_009 · cross-reference only) · life story.docx (personal note · out-of-scope) · the KJV Bible (held/excluded/not chunked) · all other literary/brand/media/canonical sources.

This selection locks §5 Option 2 and the §6 INCLUDE set (Block confirmed IN, not optional). Everything else in this plan stands. Extraction/chunking still requires a separate authorized ship step.

## 0. Verified starting state

- **Head commit:** `e27b6ee save session after DECISION_JUDGMENT_MEANING consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,711 · 10 numbered batches + 38 mini-batches · 62 official domains (75 combined keys).
- **DECISION_JUDGMENT sequence COMPLETE** (COGNITION + CROWDS + MEANING). STORYTELLING_NARRATIVE was flagged by the DECISION_JUDGMENT_PLAN (`fd7f19b`) as the distinct narrative-craft register to plan separately.
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate files located in raw/ (verified)

### A. The operator's named set · `raw/03_TIER_2_CANON_BOOKS/decision_judgment/` (4 files)

| Source | Author | Format | Size | Words (probe) | Status |
|---|---|---|---|--:|---|
| The Anatomy of Story: 22 Steps to Becoming a Master Storyteller | John Truby | pdf | 7.1M | 126,225 | CLEAN |
| The Hero with a Thousand Faces | Joseph Campbell | epub | 5.3M | 142,098 | CLEAN |
| Save the Cat! The Last Book on Screenwriting You'll Ever Need | Blake Snyder | pdf | 10.1M | 59,787 | CLEAN |
| Story | Robert McKee | pdf | 56M | **0 (scanned/image-only)** | **BROKEN** |

### B. Discovered net-new on-register candidate · `raw/` top-level (1 file · NOT in the named set)

| Source | Author | Format | Size | Words (probe) | Status |
|---|---|---|---|--:|---|
| The Visual Story: Creating the Visual Structure of Film, TV and Digital Media | Bruce Block | pdf | (top-level) | 61,118 | CLEAN · NET-NEW |

**The Visual Story (Block)** was found by a full `raw/` sweep (the operator asked to "locate all storytelling/narrative candidate files in raw/"). It is the visual-structure craft companion to the three written-story books (contrast/affinity, the visual components, visual intensity, controlling the visual story). It is **directly in BJ's visual-operator/photography wheelhouse** and squarely on-register. It is outside the operator's named 4, so its inclusion is an explicit operator call (recommended · see §5).

Read-only `pdftotext` / `ebook-convert`-to-/tmp probes (temp deleted; all mtimes unchanged · Campbell still 2026-05-16). **3 clean named story books (~328,110 words) + 1 broken named (Story/McKee scanned) + 1 clean discovered (The Visual Story · 61,118 words).** Combined clean if Block included: ~389,228 words.

### C. "story"-substring false positives swept and rejected (NOT storytelling-craft sources)

- `raw/life story.docx` (1,458 words) · a short personal/relationship note ("Born and raised... Parents still cover your phone bill..."), **NOT a canon storytelling source** · OUT-OF-SCOPE (personal/operator material).
- Building a StoryBrand (Miller · epub top-level + mobi in `sales_positioning/`) · **already-canonical** (BATCH_009 · 4 chunks) · see §3.
- Competing Against Luck: The Story of Innovation (Christensen) · innovation/JTBD, "Story" incidental · adjacent to POSITIONING_DISRUPTION's Christensen · OUT-OF-SCOPE for this lane.
- The Big Payback (hip-hop business), The Mailroom (already MEDIA_BUSINESS_RECOVERY), Live From New York, Total Recall (already FOUNDER_FASHION_RECOVERY), No Filter (Instagram), The Airbnb Story, Turn the Ship Around · "story"/"history" in biography/media titles · OUT-OF-SCOPE.
- `Tim-Walker-Story-Teller` flip-through `.mp4` (photography folder) · video, no extractable text · OUT-OF-SCOPE.

## 2. Source-quality / stub / scan check

- **3 clean named story books** (Truby pdf 126,225w · Campbell epub 142,098w · Snyder pdf 59,787w) + **1 clean discovered** (Block pdf 61,118w). Real book text confirmed by content sampling. epubs via `ebook-convert`; pdfs via `pdftotext`. No OCR.
- **BROKEN (1 · DEFER):**
  - **Story (Robert McKee):** 56 MB pdf · `pdftotext` extracted **0 words** (scanned / image-only). Confirmed broken (matches the DECISION_JUDGMENT_PLAN finding). **Excluded unless a clean text edition is re-acquired. NO OCR.** Re-acquire a clean epub.
- At ship, sample each extracted .txt to confirm real book text before chunking.

## 3. Already-chunked overlap check (verified · authoritative by source_title / author / source_file across all 38 batch jsonls)

**All 4 candidate books (the named 3 clean + McKee) AND the discovered The Visual Story are NET-NEW as book sources** (0 chunks as a source):

- The Anatomy of Story / The Hero with a Thousand Faces / Save the Cat! / Story (McKee) · **net-new.**
- The Visual Story (Bruce Block) · **net-new** (0 chunks · verified).

**Cross-lane / adjacency findings (checked LITERARY_RECOVERY, LITERARY_CANON_BLACK/_DYSTOPIAN/_GENERAL, POSITIONING_DISRUPTION, DECISION_JUDGMENT_*, CULTURE_AND_STATUS, MEDIA_BUSINESS/_RECOVERY, and a corpus-wide concept/tag scan):**

- **The one meaningful adjacency: Building a StoryBrand (Donald Miller · 2017), already-canonical in BATCH_009 (chunks 069-072 · domains brand / copywriting / positioning).** StoryBrand is the **applied brand-message** framework (customer-is-hero, the SB7 framework, clarity-beats-cleverness). STORYTELLING_NARRATIVE's books (Truby / Campbell / Snyder / Block) are the **story-construction craft beneath it** (how a story is actually built, structurally and visually). **Distinct registers · DO NOT re-chunk StoryBrand · cross-reference it** (the craft layer under the applied marketing-narrative layer).
- The LITERARY_* lanes the operator listed as MODERNIST / SOUTHERN_GOTHIC / RUSSIAN **do not exist** (only LITERARY_CANON_BLACK, _DYSTOPIAN, _GENERAL, and LITERARY_RECOVERY exist). No overlap with the story-craft sources (those lanes hold literary *works*; this lane holds story-*craft method*).
- Scattered "narrative" (10) / "storytelling" (2) hits across BATCH_002/003/004, FOUNDER_FASHION_RECOVERY, LITERARY_CANON_BLACK are incidental concept/tag usage, **NOT** a story-craft lane and **NOT** these sources. No domain named `storytelling` or `narrative` exists.

## 4. Classification table

| Source | Classification |
|---|---|
| The Anatomy of Story (Truby) | **net-new** · deep story structure / the 22 steps / moral argument |
| The Hero with a Thousand Faces (Campbell) | **net-new** · the monomyth / departure-initiation-return as a cross-cultural pattern |
| Save the Cat! (Snyder) | **net-new** · practical screenwriting · logline / beat sheet / genres |
| The Visual Story (Block) | **net-new · discovered (outside named set)** · visual narrative structure · BJ-relevant |
| Story (McKee) | **broken / needs-reacquire** (scanned · 0 text) |
| Building a StoryBrand (Miller) | **already-canonical** (BATCH_009 · applied brand-message · cross-reference only) |
| life story.docx | **out-of-scope** (personal note) |

## 5. Architecture recommendation: ONE curated mini-batch (do NOT split · do NOT defer the whole lane)

The clean sources form **one coherent register: narrative/story-construction craft** (how stories are built · structurally, dramatically, and visually). Unlike the `decision_judgment` folder (which held 8 books across 3 distinct registers and rightly split into COGNITION / CROWDS / MEANING), this is a single craft register across 3-4 books / ~328-389K words. That is squarely in-band for the corpus's curated 2-4-book lanes (LITERARY_RECOVERY, HISTORICAL_BIOGRAPHY, POSITIONING_DISRUPTION). **A split (myth/story-structure vs screenwriting/practical) would over-fragment 3-4 books into two thin, artificially-divided lanes** (Campbell's monomyth, Truby's steps, and Snyder's beats are the same craft at different altitudes). **Whole-lane deferral is NOT warranted** (3-4 clean books are ready; only McKee is broken, and McKee is redundant with the clean set's structural coverage).

**Recommendation: a single curated STORYTELLING_NARRATIVE mini-batch.**

Two source-set options (operator's call at ship):
1. **Core (recommended floor): Campbell + Truby + Snyder** (the 3 clean named books · ~328,110 words). McKee excluded (broken). This satisfies the operator's named set exactly.
2. **Core + The Visual Story (recommended): Campbell + Truby + Snyder + Block** (4 clean books · ~389,228 words). Adds the visual-structure craft layer · **most directly useful to BJ as a photographer/visual operator** (the same compositional thinking he already applies to images, applied to sequenced visual narrative). Block is net-new and on-register; its only caveat is that it sits outside the operator's named 4, so adding it is an explicit operator authorization.

**Primary recommendation: Option 2 (include The Visual Story)** for the operator-relevance, with Option 1 as the clean fallback if the operator wants to hold strictly to the named set.

**OPERATOR DECISION (LOCKED 2026-05-25): Option 2 SELECTED** · the lane ships the 4 clean sources (Campbell + Truby + Snyder + Block). See the top-of-file decision block.

## 6. Recommended first (and only) lane: STORYTELLING_NARRATIVE (include / defer / exclude)

- **INCLUDE (CORE · curated · the narrative/story-construction craft register):**
  - The Hero with a Thousand Faces (Joseph Campbell) · epub · ~142,098 words.
  - The Anatomy of Story (John Truby) · pdf · ~126,225 words.
  - Save the Cat! (Blake Snyder) · pdf · ~59,787 words.
  - **The Visual Story (Bruce Block) · pdf · ~61,118 words · SELECTED IN (Option 2 · operator-locked 2026-05-25).**
- **DEFER (broken · re-acquire clean text · NO OCR):**
  - Story (Robert McKee) · scanned/image-only · re-acquire a clean epub, then a future addendum.
- **EXCLUDE (0 chunks):**
  - Building a StoryBrand (Miller) · already-canonical in BATCH_009 (cross-reference only).
  - life story.docx (personal note · out-of-scope), Competing Against Luck (innovation · out-of-scope), all "story"/"history" biography/media-business titles, the Tim Walker video.
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor).
  - Every already-canonical source and every other-cluster source. CURRENT_IDENTITY sources.

## 7. Recommended chunk target / range

- **Option 1 (3 books · ~328K words):** target **~13-15** chunks · range 11-17 (halt-and-report if outside).
- **Option 2 (4 books · ~389K words · recommended):** target **~15-17** chunks · range 13-19 (halt-and-report if outside).
- **Synthesis:** 1 closing synthesis chunk (the narrative-craft toolkit + the optionality guardrail).
- **Provisional per-source split (Option 2):** Campbell ~4-5 · Truby ~4-5 · Snyder ~3-4 · Block ~3 · + 1 synthesis. Curated/representative (NOT chapter-by-chapter): Campbell (the monomyth arc · the call / refusal / threshold / road of trials / the boon / the return · myth as a cross-cultural structural pattern); Truby (story as organic structure not formula · desire / need / weakness · the moral argument and character web · theme expressed through structure · revelation sequencing); Snyder (the logline / one-line · the beat sheet · genre as audience-promise · the "same but different" rule · the likability/"save the cat" beat); Block (the visual components · contrast and affinity · visual intensity · controlling the visual story across a sequence).

## 8. Recommended domains (EXISTING domains only · NO new domain)

Verified to exist (current counts): `aesthetics` (73), `culture` (62), `brand` (38), `media-business` (11), `operator-doctrine` (115), `strategy` (205), `operator-process` (100), `ethics` (51), `status` (16), `decision-making` (16), `mental-models` (8), `lineage` (22), `systems-thinking` (54).

| Domain | Planned use |
|---|---|
| `aesthetics` (anchor) | Story/visual structure as compositional craft: dramatic structure, beats, form, contrast/affinity, the made composition. The lane's namesake-craft home (and Block's visual-structure material lands squarely here). |
| `culture` | Campbell's monomyth as a cross-cultural pattern · story as cultural technology · the shared structures audiences already carry. |
| `brand` | Narrative-to-message: the customer-as-hero / clarity bridge (the StoryBrand adjacency, held as the craft beneath the applied frame). |
| `media-business` | Screenwriting / film / TV / digital as a media-industry craft (Snyder's Hollywood pitch/genre/market logic; Block's film/TV/digital-media frame). Grows from a thin 11. |
| `operator-doctrine` | The transferable narrative discipline + the closing synthesis. |
| `strategy` (if warranted) | Narrative as pitch / positioning / sequencing-of-reveal where it bears on a strategic message · used sparingly. |
| `operator-process` (if warranted) | The beat-sheet / 22-steps / visual-structure checklist as a repeatable construction process · used where squarely procedural. |
| `ethics` (if warranted) | Only if a squarely-present moral dimension appears (Truby's "moral argument") · likely 0-1; otherwise routed to operator-doctrine/aesthetics. |

**Recommended anchor:** `aesthetics` (the corpus's craft/form domain · story and visual structure are compositional craft), with `culture` (cross-cultural myth pattern), `brand` (narrative-to-message bridge), and `media-business` (the film/TV/digital craft context) the strong secondaries.

### Domain issues to flag (important)

- **`storytelling`, `narrative`, `screenwriting`, `mythology`, `myth`, `archetype`, `hero`, `religion`, `spirituality`, `self-help` do NOT exist and will NOT be created.** Verified absent in `combined_domain_counts`. Routing: story-structure/screenwriting-craft -> `aesthetics`; monomyth/cross-cultural pattern -> `culture`; narrative-as-message -> `brand`; film/TV/digital-media craft -> `media-business`; the synthesis/discipline -> `operator-doctrine`; pitch/positioning -> `strategy` (sparingly); construction-process -> `operator-process` (sparingly); moral-argument -> `ethics` (0-1, if squarely present).
- **`media-business` (11) is a thin existing domain** · this lane will reuse and grow it, NOT create anything new.
- **NO new domain will be created by default.** All planned domains pre-exist.

## 9. Connections (cross-references this lane opens)

- **BATCH_009 (Building a StoryBrand / Miller):** the applied brand-message layer · STORYTELLING_NARRATIVE is the story-construction craft beneath it (customer-as-hero traces to Campbell's hero; SB7 is a beat sheet for a brand message). Held as craft, not re-chunked.
- **POSITIONING_DISRUPTION (The Mom Test / Crossing the Chasm) + BATCH_009/_EXPANSION:** narrative is how positioning is communicated; the craft of structuring a clear message.
- **LITERARY_RECOVERY (Beloved / Jonathan Livingston Seagull) + LITERARY_CANON_BLACK/_DYSTOPIAN/_GENERAL:** the literary *works* this craft analyzes · the method (how stories are built) reads against the works (built stories).
- **MEDIA_BUSINESS_RECOVERY (Hit Men / The Mailroom) + MEDIA_BUSINESS (ESPN/SNL/HBO):** the film/music/TV industry that consumes and pays for narrative craft · Snyder's Hollywood context and Block's film/TV/digital-media frame sit against the business of media.
- **DECISION_JUDGMENT (Kahneman / Haidt):** story is how humans actually process and remember (the narrative fallacy, intuitions-first) · the cognitive substrate beneath why narrative works · held descriptively, not as a manipulation lever.
- **CULTURE_AND_STATUS (Storr) + BATCH_010 (lineage/status):** myth and hero-pattern as status/cultural narrative.
- **CURRENT_OPERATOR_REALITY_BRIEF:** every chunk references the brief in `sniped_relevance` and holds the lane as decision-support only (the brief is the read-first anchor · NOT a chunked source).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** the optionality discipline governs this lane; CURRENT_IDENTITY remains plan-only / NOT extracted.

## 10. Identity-optionality confirmation

This lane does NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks frame the books as a **decision-support / pattern-library lens read against CURRENT_OPERATOR_REALITY_BRIEF** · the closing synthesis chunk makes the optionality discipline explicit. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 11. Storytelling/narrative material = decision-support / pattern-library only (not a directive)

Truby, Campbell, Snyder, and Block are held strictly as a **decision-support / pattern-library layer**: transferable patterns of how narratives are structured (dramatic and visual) and why they land. It is **NOT a directive that BJ become a screenwriter, a myth-brand guru, a novelist, a film critic, a narrative consultant, or a self-help storyteller**, and not a mandate to turn the OS into screenwriting or narrative-coaching content. The methods are read as transferable craft (structure, sequencing of revelation, visual composition over time) for a solo field-engineer/visual operator in build-mode, loading the backend before final brand/offer/company-architecture decisions.

## 12. Campbell mythology/religion handling (cultural/narrative pattern only · NOT a faith lane)

**The Hero with a Thousand Faces is heavy on comparative myth and religion.** It will be held **strictly as cultural and narrative pattern study** · the monomyth as a recurring cross-cultural *story structure*, NOT as theology, faith, or spiritual instruction. **No `religion` / `spirituality` / `mythology` / `myth` / `archetype` / `hero` domain will be created**, and no faith/spirituality lane is opened. Campbell's religious examples are treated as narrative source material (how cultures have structured hero stories), routed to `culture` / `aesthetics`. The KJV Bible stays held separately as the SPIRITUAL_FOUNDATION anchor and is NOT pulled into this lane.

## 13. Deliverables for the future ship (NOT created now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/STORYTELLING_NARRATIVE_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/storytelling_narrative_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/STORYTELLING_NARRATIVE_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/STORYTELLING_NARRATIVE_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/STORYTELLING_NARRATIVE_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/STORYTELLING_NARRATIVE_COMPLETE.md` |
| Extraction script | `scripts/extract_storytelling_narrative.py` |
| Chunk writer | `scripts/write_storytelling_narrative_chunks.py` |

Schema: the canonical 12-field JSONL · `chunk_id` pattern `STORYTELLING_NARRATIVE_NNN`. Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · 3 or 4 sources · no new domain · `aesthetics` anchor · storytelling/narrative/screenwriting/mythology/myth/archetype/hero/religion/spirituality/self-help NOT created · McKee 0 · Building a StoryBrand 0 [already BATCH_009] · life story.docx 0 · Bible 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality + not-a-directive + Campbell-cultural-not-faith guardrail in every chunk · quote discipline · em-dash sweep · curated-not-exhaustive).

## 14. Projected post-consolidation state (for reference · NOT applied now)

If the lane ships at the mid-target and consolidates: 1,711 + ~13-17 = **~1,724-1,728 chunks** · 10 numbered batches + **39 mini-batches** · **62 domains (NO new domain** · bumps to `aesthetics` [anchor] / `culture` / `brand` / `media-business` / `operator-doctrine`, plus `strategy` / `operator-process` / `ethics` where warranted). Exact counts finalized at ship/consolidation time. Subsequent lanes: Tier-2 clusters (incl the Greene trio: Laws of Human Nature / Mastery / 50th Law), BRAND_CANON, the optional operator-docs cleanup, the fresh current SNIPED brief / CURRENT_IDENTITY principle-only ship, the SPIRITUAL_FOUNDATION decision (KJV Bible), and the broken-backlog re-acquisitions (incl Story/McKee for a future STORYTELLING addendum).

## 15. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,711.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `pdftotext`+`ebook-convert`+`pandoc`-to-/tmp · temp deleted · all mtimes unchanged).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 16. Next step (operator decision · do not start without authorization)

Authorize the **STORYTELLING_NARRATIVE** lane ship. **Source set is LOCKED to Option 2** (Campbell + Truby + Snyder + The Visual Story/Block · 4 clean sources · target ~15-17). Existing domains only · `aesthetics` anchor · no new domain · storytelling/narrative/screenwriting/mythology/myth/archetype/hero/religion/spirituality/self-help NOT created · Story/McKee deferred (broken) · Building a StoryBrand excluded (already BATCH_009) · Campbell held as cultural/narrative pattern not faith · Bible excluded · curated, not exhaustive · decision-support, not a directive. Then commit the ship outputs, then consolidate, then session-save.
