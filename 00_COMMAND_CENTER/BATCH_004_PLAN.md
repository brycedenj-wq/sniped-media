# BATCH_004 · SNIPED OS Depth-Fill · Extraction Plan

**Date drafted:** 2026-05-16
**Status:** PLAN ONLY · no extraction or chunking performed yet
**Batch theme:** SNIPED OS depth-fill · close the operating-state gaps left by BATCH_001's sampled-only coverage, plus pull in two deferred conversational sources and the previously-unread Aesthetic Statement.

**Source folder (already in place):** sources live across `~/AI-Brain-Refinery/raw/` root + `raw/00_BRIEF/` + `raw/10_REFERENCE/`. No file relocation needed for this batch · all sources are SNIPED-internal docs already in their canonical operating-folder locations.

---

## Why this batch · the gap it closes

After BATCH_001 + BATCH_002 + BATCH_003 (361 chunks across 3 batches), the corpus has comprehensive canon coverage (Tier 1 + Tier 2 books) and substantial operating-state coverage. But several SNIPED OS docs were SAMPLED only in BATCH_001 (head-only or first-few-sections), and a few high-value docs were deferred or missed entirely. BATCH_004 closes these specific gaps:

- **2 chat threads** that were captured as placeholder chunks only in BATCH_001 (chat thread + Gemini thread)
- **1 widely-referenced doc not in BATCH_001** (Aesthetic_Statement_v1.docx)
- **3 SAMPLED .md files** with substantial unprocessed content (100Q_AUDIT Sections 8+, STRATEGIC_PRINCIPLES Sections 5-12, SNIPED_OS_V1_SYNTHESIS Sections 6-14)
- **2 SAMPLED .docx files** with the remaining Parts unprocessed (Offer_Stack Parts VIII-XIII, Platform_Stack Parts VII-XIII)

The strategic value: BATCH_004 completes BJ's own operating system in chunk form, which makes the entire corpus self-referential (any future agent can answer 'what did BJ decide about X?' from the chunks rather than needing to re-read source docs).

---

## Source coverage matrix

### Selected (8 files · located, sized, format-verified)

| # | Priority | Source filename + path | Size | Format | What's needed | Extraction tool |
|--:|:--------:|------------------------|-----:|--------|---------------|------------------|
| 1 | P1 | `chat Sniped MAster thread.docx` (root) | 280 KB | docx | Full re-extract (BATCH_001 had placeholder only) | textutil or pandoc |
| 2 | P1 | `Gemini Sniped MAster thread.docx` (root) | 202 KB | docx | Full re-extract (BATCH_001 had placeholder only) | textutil or pandoc |
| 3 | P1 | `Aesthetic_Statement_v1.docx` (root) | 11 KB | docx | Fresh extract (not in BATCH_001) | textutil or pandoc |
| 4 | P2 | `00_BRIEF/100Q_AUDIT_OPTIMIZATIONS_2026-05-13.md` | 56 KB | md | Already plain text · target Sections 8-13 + CLOSING + CONSOLIDATED TOP MOVES + CROSS-REFERENCES | none (read in-place) |
| 5 | P2 | `10_REFERENCE/STRATEGIC_PRINCIPLES.md` | 70 KB | md | Already plain text · target Sections 5 through 12 (skip 4a-4k overlap with BATCH_003) | none (read in-place) |
| 6 | P2 | `00_BRIEF/SNIPED_OS_V1_SYNTHESIS_2026-05-12.md` | 70 KB | md | Already plain text · target Sections 6-14 + Appendices A/B | none (read in-place) |
| 7 | P3 | `The_Offer_Stack.docx` (root) | 55 KB | docx | Full re-extract · target Parts VIII-XIII (Brand Psychology + Platform Selection + Launch Mechanics + Scaling Winners + Growth Levels + Operator Sequence) | textutil or pandoc |
| 8 | P3 | `The_Platform_Stack.docx` (root) | 58 KB | docx | Full re-extract · target Parts VII-XIII (Meta architecture full stack + Setup Sequence) | textutil or pandoc |

**Total source size:** 802 KB across 8 files. Most of the .md files are already plain text (no extraction needed); .docx files extract quickly.

### Verified file presence and md5 uniqueness
- All 8 files confirmed present at the listed paths via direct stat
- All 5 docx files have unique md5s (no cross-file duplication within this batch)
- Md5s do NOT overlap with BATCH_002 or BATCH_003 source files (these are SNIPED-internal docs, structurally distinct from canon books)

### NOT in this batch (intentionally · already covered or out-of-scope)

| Source | Status | Reason |
|--------|--------|--------|
| `SNIPED_OS_OPERATING_BRIEF.md` | FULL in BATCH_001 (9 chunks) | No re-processing needed |
| `The_Revenue_Stack.docx` | FULL in BATCH_001 (6 chunks) | No re-processing needed |
| `The_Attention_Stack.docx` | FULL in BATCH_001 (8 chunks) | No re-processing needed |
| `The_Outbound_Stack.docx` | FULL in BATCH_001 (7 chunks) | No re-processing needed |
| `The_Copywriting_Stack.docx` | FULL in BATCH_001 (6 chunks) | No re-processing needed |
| `The_Production_Stack.docx` | FULL in BATCH_001 (5 chunks) | No re-processing needed |
| `The_Adobe_Stack_Manual.docx` | FULL in BATCH_001 (4 chunks) | No re-processing needed |
| 7 remaining photographer Studies (Avedon, Eggleston, Shore, Herzog, Frank, Meyerowitz, Iturbide) | NOT YET in any batch | Defer to BATCH_005 photographer canon batch · this BATCH_004 stays focused on OS depth-fill |
| 9 `Art_Series_*.md` files | NOT YET in any batch | Same · defer to photographer batch |
| `08_BOOK/The_Direction_Stack_v_final_2026-05-12.pdf` (444 MB) | BLOCKED | Canonical confirmation still pending; out of scope until user resolves |
| STRATEGIC_PRINCIPLES Sections 4a-4k (book summaries) | OVERLAP with BATCH_003 | Sections 4a-4k summarize Enns ×2, Holiday, Guidara, Naval, Trading Up, Jarvis, Berger/Dyer, Elberse, Sax, Simler+Hanson · all directly chunked at depth in BATCH_003. Skip these subsections during chunking to avoid corpus duplication. |
| Section 4l-onward of STRATEGIC_PRINCIPLES (Trading Up · Silverstein/Fiske) | Partial gap | Trading Up was NOT chunked in BATCH_003 (the book is not in raw/). Section 4f-style synthesis chunk acceptable here as substitute. |

---

## Expected domains and concepts per file

### 1. chat Sniped MAster thread.docx (P1, 280 KB)
- **Format:** Conversational ChatGPT transcript across many sessions
- **Chunking strategy:** Thematic, not sequential. Skim for: locked decisions, "NEVER" markers, refusal patterns, voice tells, contradictions BJ resolved, ideas that got killed, frameworks that emerged
- **Expected domains:** doctrine-meta, mindset, drift-detection, decision-archaeology
- **High-signal targets:** the conversation moments where BJ articulated WHY (not just WHAT) — those are the chunks that survive
- **Estimated yield:** 10-20 chunks

### 2. Gemini Sniped MAster thread.docx (P1, 202 KB)
- **Format:** Conversational Gemini transcript
- **Chunking strategy:** Same as chat thread · thematic, looking for decision-archaeology
- **Specific value:** per BATCH_001 summary, this is "chronological excerpt sampling for thesis-genesis trail" · particularly look for the early articulations of the SNIPED meta-thesis
- **Expected domains:** doctrine-meta, thesis-evolution, mindset
- **Estimated yield:** 8-15 chunks

### 3. Aesthetic_Statement_v1.docx (P1, 11 KB)
- **Format:** Short locked-doctrine document
- **Chunking strategy:** Each major principle gets its own chunk (likely 4-7 principles total in such a small doc)
- **Expected domains:** aesthetics, visual-direction, brand
- **Specific value:** This is the locked aesthetic source referenced across nearly every SNIPED doc. Per BJ auto-memory feedback (2026-05-12), the canonical visual direction is "quiet luxury editorial restraint" · this doc is presumably where that decision is most fully articulated
- **Estimated yield:** 4-7 chunks

### 4. 100Q_AUDIT_OPTIMIZATIONS Sections 8+ (P2, ~30 KB of unprocessed text)
- **Structure confirmed:** 13 SECTIONS total · Sections 1-7 sampled in BATCH_001
- **Remaining:** Section 8 (BRAND AND NAME), 9 (BUSINESS MODEL), 10 (RISK AND SLIPPAGE), 11 (PERSONAL STAKES), 12 (2026 WIN CONDITION), 13 (FINAL LOCK) + CLOSING + CONSOLIDATED TOP MOVES + CROSS-REFERENCES
- **Expected domains:** offer-design (Section 9), risk-management (Section 10), mindset (Section 11), goals (Section 12), doctrine-meta (Section 13), operational-locks (CLOSING + CONSOLIDATED)
- **Specific value:** Section 13 FINAL LOCK + CLOSING + CONSOLIDATED TOP MOVES are the actionable distillation of the entire 100Q audit · highest-signal chunks in this file
- **Estimated yield:** 20-35 chunks

### 5. STRATEGIC_PRINCIPLES Sections 5-12 (P2, ~25 KB of unprocessed text, EXCLUDING 4a-4k which overlap BATCH_003)
- **Structure confirmed:** 12 main sections (with subsection structure)
- **BATCH_001 sampled:** Sections 1-4 (Trust Equation, Hit Makers, Status Anxiety, WWP — chunked) PLUS subsections 4a-4k (book summaries for sources now in BATCH_003)
- **Remaining for BATCH_004 (DEDUPE-AWARE):**
  - Section 5 (the second "5" · "Cross-source synthesis for SNIPED")
  - Section 6 (Operational implications mapped to 3 engines)
  - Section 7 (Anti-patterns and contradictions)
  - Section 8 (Decision-support routing)
  - Section 9 (Memory file candidates)
  - Section 10 (Final integrated principle)
  - Section 11 (Reading sequence + future intelligence pulls)
  - Section 12 (Sources processed · date order · low chunk value, likely skip)
- **Specific value:** Sections 5-9 are the synthesis layer that maps the canonical book principles ONTO SNIPED's specific 3-engine architecture. This is meta-doctrine that adds value beyond what's in any individual book chunk (B2 or B3).
- **Expected domains:** doctrine-meta, decision-support, cross-source-synthesis, anti-patterns
- **Estimated yield:** 18-30 chunks (high signal density per byte)

### 6. SNIPED_OS_V1_SYNTHESIS Sections 6-14 + Appendices (P2, ~50 KB of unprocessed text)
- **Structure confirmed:** 14 main sections + 2 appendices
- **BATCH_001 sampled:** Sections 0-5 (Core Thesis, Visual Identity, Composite Workflow, Lightroom Philosophy, Brand/Positioning, Content OS)
- **Remaining for BATCH_004:**
  - Section 6 · The Commercial Architecture (very high value · maps to offer ladder + pricing)
  - Section 7 · Contradictions and Duplicated Ideas (meta-doctrine value)
  - Section 8 · Missing Systems / Underdeveloped Frameworks (gap-surface)
  - Section 9 · Latent Systems Already Emerging
  - Section 10 · Where SNIPED Drifts Into Generic Creator Behavior (anti-pattern surface)
  - Section 11 · Where SNIPED is Culturally Distinctive (the moat surfaces) (high-signal)
  - Section 12 · The Unified Mental Model
  - Section 13 · Recommendations (top 10, prioritized)
  - Section 14 · Closing
  - Appendix A · Files referenced
  - Appendix B · Files NOT read (gap-surface metadata; likely low chunk value)
- **Expected domains:** doctrine-meta, commercial-architecture, anti-patterns, moat-surfaces, mental-models, recommendations
- **Specific value:** Section 11 "Where SNIPED is Culturally Distinctive" is the explicit articulation of the moat · highest-value section in this doc. Section 7 (contradictions) and Section 8 (missing systems) help with future-batch planning.
- **Estimated yield:** 20-35 chunks

### 7. The_Offer_Stack Parts VIII-XIII (P3, ~25 KB of remaining text)
- **Structure confirmed via textutil probe:** Parts I-XIII total
- **BATCH_001 sampled:** Parts I-VII (Operating Principle, Finding the Offer, Offer Ladder, Digital Products, Physical Products, AI Services, Brand Identity Architecture)
- **Remaining for BATCH_004:**
  - Part VIII · Brand Psychology and Positioning
  - Part IX · Platform Selection for Digital Products
  - Part X · Launch Mechanics
  - Part XI · Scaling Winners
  - Part XII · Growth Levels
  - Part XIII · The Operator Sequence
- **Expected domains:** brand-psychology, platform-mechanics, launch-mechanics, scaling, growth-levels, operator-sequence
- **Estimated yield:** 8-12 chunks

### 8. The_Platform_Stack Parts VII-XIII (P3, ~30 KB of remaining text)
- **Structure confirmed via textutil probe:** Parts I-XIII total
- **BATCH_001 sampled:** Parts I-VI (LinkedIn-as-Business-Community + LinkedIn Profile/Content/Engagement/Outreach)
- **Remaining for BATCH_004:**
  - Part VII · Meta Identity and Security Architecture
  - Part VIII · Meta Business Suite
  - Part IX · Meta Commerce Architecture
  - Part X · Meta Lead Center
  - Part XI · Meta Advertising Fundamentals
  - Part XII · The Integrated Platform Play
  - Part XIII · The Setup Sequence
- **Expected domains:** meta-architecture, meta-advertising, integrated-platform, platform-setup
- **Specific value:** Meta full-stack architecture is currently entirely absent from the corpus · all chunks here will be NEW coverage, not overlap with BATCH_001's LinkedIn-focused chunks.
- **Estimated yield:** 10-15 chunks

---

## Estimated chunk yield (full batch)

| Source | Range | Mid-estimate |
|--------|------:|-------------:|
| chat Sniped MAster thread | 10-20 | 15 |
| Gemini Sniped MAster thread | 8-15 | 12 |
| Aesthetic_Statement_v1 | 4-7 | 6 |
| 100Q_AUDIT Sections 8+ | 20-35 | 27 |
| STRATEGIC_PRINCIPLES Sections 5-12 | 18-30 | 24 |
| SNIPED_OS_V1_SYNTHESIS Sections 6-14 + Appendices | 20-35 | 27 |
| The_Offer_Stack Parts VIII-XIII | 8-12 | 10 |
| The_Platform_Stack Parts VII-XIII | 10-15 | 12 |

**Estimated total:** 98-169 chunks. Mid-estimate: **133 chunks**. Conservative floor: 100, ceiling: 180.

**Corpus impact:** Combined corpus after BATCH_004 will be 361 + ~133 = **~494 chunks** (range 461-541). The corpus will have substantial coverage across all three main families: SNIPED OS (B1 + B4 ≈ 240 chunks), canon books (B2 + B3 = 255 chunks), and self-referential doctrine-meta (concentrated in B4's chat threads + synthesis sections).

---

## Expected new domain coverage

BATCH_004 will likely introduce these previously-thin or absent domains:

| Domain | Expected new chunks | Source |
|--------|-------------------:|--------|
| **doctrine-meta** | 10-15 | Chat threads + STRATEGIC_PRINCIPLES synthesis + SYNTHESIS doc |
| **aesthetic-doctrine** | 4-7 | Aesthetic_Statement (currently the only `aesthetics` chunks are 9 photographer-study fragments in B1) |
| **meta-architecture** | 6-10 | Platform_Stack Parts VII-XIII |
| **meta-advertising** | 2-4 | Platform_Stack Part XI |
| **commercial-architecture** | 4-7 | SYNTHESIS Section 6 + 100Q Section 9 |
| **moat-surfaces** | 3-5 | SYNTHESIS Section 11 |
| **anti-patterns** | 3-5 | SYNTHESIS Section 7 + 10 + STRATEGIC_PRINCIPLES Section 7 |
| **decision-archaeology** | 5-10 | Chat thread + Gemini thread (NEW domain) |
| **brand-psychology** | 2-4 | Offer_Stack Part VIII |
| **launch-mechanics** | 2-3 | Offer_Stack Part X |
| **scaling** | 2-3 | Offer_Stack Part XI |
| **operational-locks** | 5-10 | 100Q FINAL LOCK + CLOSING + CONSOLIDATED TOP MOVES |

The corpus moves from ~38 unique domains today to ~50 unique domains after BATCH_004.

---

## Risks and missing items

### Confirmed risks

1. **Chat thread file-size discrepancy.** BATCH_001 source index reports `chat Sniped MAster thread.docx` as 407 KB; actual file is 280 KB. Possible explanations: (a) file was edited/trimmed between BATCH_001 and now, (b) BATCH_001 size report was inaccurate, (c) a different copy was being referenced. **Action:** flag in extraction log; proceed with extraction of the current file; note the discrepancy for user awareness in case content was lost in the trim.

2. **Gemini thread file-size discrepancy.** BATCH_001 source index reports 237 KB; actual file is 202 KB. Same as above. **Action:** same · flag, proceed, note.

3. **STRATEGIC_PRINCIPLES has duplicate "Section 5" headings.** Two `## 5 ·` sections exist in the source (one labeled "NEXT INFO GRABS · raw Reddit / photography corpus" at line 632; another labeled "Cross-source synthesis" at line 659). This is a source-doc numbering bug. **Action:** during chunking, disambiguate explicitly (refer to them as "Section 5 · NEXT INFO GRABS" and "Section 5 · Cross-source synthesis" in chunk concepts). Skip the NEXT INFO GRABS section if it's a low-signal aggregation list; chunk the synthesis section.

4. **STRATEGIC_PRINCIPLES Sections 4a-4k overlap with BATCH_003.** Subsections 4a-4k are summaries of Enns, Holiday, Guidara, Naval, Jarvis, Elberse, Sax, Simler+Hanson — all books directly chunked at depth in BATCH_003. **Action:** explicitly skip these subsections during chunking. The synthesis sections (5+) reference these books but synthesize across them; those synthesis chunks add value and should be chunked. The 1-page-per-book summaries do not.

5. **Conversational source chunking is qualitatively different.** Chat thread + Gemini thread are stream-of-consciousness, not structured. Sequential chunking will produce low-signal results. **Action:** chunk thematically by skimming for: locked decisions (markers like "decided", "locked", "NEVER", "always", "from now on"), refusal patterns (what got rejected and why), thesis-genesis moments (early articulations of the SNIPED meta-thesis). Expect lower chunk-per-byte ratio than structured docs.

6. **SNIPED_OS_V1_SYNTHESIS Appendix B is "Files NOT read in this synthesis."** This is a gap-surface metadata list, low chunk value. **Action:** skim for any high-signal entries; if none, skip the appendix entirely. Appendix A (Files referenced) is similarly low chunk value · skip both unless surprise-content emerges.

7. **Re-extraction of partially-sampled .docx files.** Offer_Stack and Platform_Stack were sampled with textutil in BATCH_001. A fresh extract with pandoc or textutil will produce the full content again — including the parts already chunked. **Action:** extract fresh into `01_KNOWLEDGE_BASE/batches/batch_004_extracted/`, then in the chunking script, EXPLICITLY skip Parts I-VII (Offer) / Parts I-VI (Platform) to avoid duplicating BATCH_001 chunks. Mark this discipline in the chunking script comments.

### Non-risks (verified clear)
- All 8 source files present at expected paths
- All .docx files have unique md5s (no cross-file duplication within BATCH_004)
- No md5 overlap with BATCH_002 or BATCH_003 sources
- All required tools already installed (textutil native to macOS; pandoc from BATCH_002 install)
- No OCR required (no PDFs in this batch)

### Pending user confirmation (no blocker for BATCH_004 extraction)
- Direction Stack PDF canonical decision remains outstanding · NOT a blocker for this batch (book is intentionally excluded)
- File-size discrepancies on chat threads · proceed with current files; user can verify content scope post-extraction if concerned

---

## Domain coverage projection (combined corpus after BATCH_004)

Current top-10 domains (3 batches, 361 chunks):

| Domain | Current | BATCH_004 expected adds | Projected new total |
|--------|--------:|------------------------:|--------------------:|
| strategy | 63 | +5 (100Q + SYNTHESIS) | ~68 |
| leadership | 40 | +2 (chat threads on team) | ~42 |
| operations | 18 | +5 (SYNTHESIS commercial architecture) | ~23 |
| content-strategy | 15 | +5 (100Q content sections) | ~20 |
| pricing | 14 | +3 (Offer Stack Part X + 100Q Section 9) | ~17 |
| founder-psychology | 13 | +5 (chat threads + 100Q Section 11) | ~18 |
| **aesthetics** | **9** | **+7 (Aesthetic_Statement)** | **~16 (substantial deepening)** |
| **doctrine-meta** | **~0** | **+12 (NEW · cross-batch synthesis chunks)** | **~12 (NEW domain)** |
| **decision-archaeology** | **~0** | **+8 (NEW · chat threads thematic mining)** | **~8 (NEW domain)** |
| **meta-architecture** | **~0** | **+8 (NEW · Platform_Stack Parts VII-XIII)** | **~8 (NEW domain)** |

**Net effect:** BATCH_004 will deepen 5-6 existing domains substantially AND introduce 4 new domains (doctrine-meta, decision-archaeology, meta-architecture, plus likely aesthetic-doctrine if it emerges as distinct from generic aesthetics).

---

## Chunking strategy notes (apply during chunking phase)

1. **Avoid duplication with prior batches.** Three specific anti-duplication disciplines:
   - Skip STRATEGIC_PRINCIPLES Sections 4a-4k (already in BATCH_003)
   - Skip Offer_Stack Parts I-VII (already in BATCH_001)
   - Skip Platform_Stack Parts I-VI (already in BATCH_001)

2. **Use BATCH_003 schema** (canonical going-forward): `chunk_id`, `batch_id`, `source_title`, `source_file`, `author`, `domain`, `concept`, `summary`, `usable_principle`, `sniped_relevance`, `direct_quotes`, `tags`. For self-authored SNIPED docs, `author` = "BJ / SNIPED Media" (or use a more precise attribution per doc if helpful).

3. **Conversational source chunking:** for chat thread + Gemini thread, search for explicit decision markers ("decided", "locked", "NEVER", "always do", "the rule is", "from now on", "killed", "refused"). Each marker is a chunk seed. Skim around it for context. Do NOT chunk sequentially — chunk thematically.

4. **Meta-doctrine chunks** (from STRATEGIC_PRINCIPLES synthesis sections + SYNTHESIS Section 7) should be tagged with `doctrine-meta` and cross-referenced to the BATCH_002/003 chunks they synthesize. Use the `sniped_relevance` field heavily — these are pre-translated decisions SNIPED has already made.

5. **The Aesthetic_Statement is small but high-value.** Aim for 4-7 chunks total. Each principle should be a standalone chunk with the direct quote preserved. Tag heavily with `quiet-luxury`, `visual-direction`, `aesthetics-doctrine`, `editorial-restraint`, `anti-cinematic`.

---

## Recommended next command for BATCH_004 extraction

When ready to proceed, execute:

```bash
python3 ~/AI-Brain-Refinery/scripts/extract_batch_004.py
```

(Script does not yet exist; will be created at extraction step, modeled on `scripts/extract_batch_003.py`. Key adaptations needed: handle `.docx` via textutil OR pandoc; for the `.md` files, copy into `batch_004_extracted/` rather than re-extracting; tag the partially-extracted Offer/Platform stacks for the chunker to skip Parts already covered.)

The extraction step will:
1. For 5 .docx files: extract via textutil (or pandoc · decide based on tactile quality after a quick comparison) to `01_KNOWLEDGE_BASE/batches/batch_004_extracted/<slug>.md`
2. For 3 .md files: copy verbatim to `01_KNOWLEDGE_BASE/batches/batch_004_extracted/<slug>.md` for archival consistency
3. Write extraction log to `00_COMMAND_CENTER/batch_logs/BATCH_004_EXTRACTION_LOG.md`

After extraction completes, the chunking pipeline (modeled on `scripts/write_batch_003_chunks.py`, organized into 8 clusters one per source) will produce `01_KNOWLEDGE_BASE/batches/BATCH_004_CHUNKS.jsonl` plus the three required companion files (summary, source index, completion log).

---

## Summary

- **Files selected for BATCH_004:** 8 (3 docx fresh-extract, 2 docx partial-re-extract, 3 md no-extract-needed)
- **Files excluded (out of scope this batch):** 7 photographer Studies + 9 Art_Series · defer to BATCH_005; Direction Stack PDF · still blocked
- **Total source size:** 802 KB (substantially smaller than canon-book batches because internal docs are dense markdown not narrative prose)
- **Estimated chunk yield:** 98-169 chunks (mid 133)
- **Estimated extraction time:** <2 minutes (all sources fast)
- **Estimated chunking time:** longest phase (8 clusters · conversational sources require careful thematic mining)
- **Major risks:** chat thread file-size discrepancy (flag-and-proceed), STRATEGIC_PRINCIPLES dedupe discipline (sections 4a-4k must be skipped), Offer/Platform Stack dedupe discipline (early Parts must be skipped)
- **Blocker:** none

Ready to proceed with extraction on user signal.
