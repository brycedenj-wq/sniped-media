# BATCH_008 plan · AI / tech / automation / agency / operating-edge canon · 2026-05-22

Plan only. No staging, extraction, chunking, master-file updates, OCR, or commits. This plan defines BATCH_008 so a later authorized extraction session can run the locked 7-step SOP (extract → chunk → validate → ship → consolidate → session-save) without re-deriving scope.

**Source universe:** `~/AI-Brain-Refinery/raw/` (already staged · the 2026-05-18 + earlier passes). No new staging is required for the core set · all core sources are already in `raw/`.
**Theme:** the AI / tech / automation / agency / operating-edge canon · the originally-reserved BATCH_008 held back through the 7 numbered batches and 9 mini-batches. The strategic / economic / philosophical WHY behind AI adoption (the 12 ai_tech canon books) plus the practical operator/agency HOW (the AI Edge course + operator-authored AI docs).

---

## 0 · Verified starting state (this session)

- Latest commit: `94283a2 save session after literary lane consolidation`
- Total chunks: 995 · 7 numbered batches + 9 mini-batches
- Official domains: 60
- Working tree: clean
- BATCH_008: NOT started (no `BATCH_008_CHUNKS.jsonl`, no `batch_008_extracted/`, no `BATCH_008_COMPLETE.md`, no prior `BATCH_008_PLAN.md`)
- Recovery follow-ups still flagged and OUT of BATCH_008 scope: Beloved, Maus I, Jonathan Livingston Seagull, Maus II, Russian-author mobi

---

## 1 · Candidate source locations (located in current docs + raw/)

BATCH_008 candidates live in four `raw/` locations, cross-referenced against the documented BATCH_008 definition in `MASTER_INDEX.md`, `ACTIVE_KNOWLEDGE_STATE.md`, `NEW_INTAKE_ACK_2026-05-19.md` §5, and `STAGING_PLAN_2026-05-19_INTAKE.md` §5 (row 11):

| Location | What it holds | Role |
|---|---|---|
| `raw/02_TIER_1_CANON_BOOKS/ai_tech/` | 12 AI/tech canon books | CORE · Cluster A |
| `raw/05_AI_EDGE_COURSE/` | Finding Your Edge.pdf + COURSE WORK 1 thru 2.docx | CORE · Cluster B |
| `raw/08_AI_TECH/ai_history_case_studies/` | AI CHANGED EVERYTHING.docx + sniped_os_knowledge_dump.docx | CORE · Cluster B |
| `raw/10_REFERENCE/_intake_2026-05-18/` | youtube skool doc.docx (+ several BATCH_006-chunked Claude Code docs · excluded) | CORE (youtube skool only) · Cluster B |
| `raw/` root + `raw/99_VAULT/` | loose, not-yet-chunked AI/Claude operator docs | DISCOVERED EXTRAS · operator decision (§4.3) |

---

## 2 · Inventory by folder, filename, file type, extraction method

### 2.1 · Cluster A · the 12 ai_tech canon books (`raw/02_TIER_1_CANON_BOOKS/ai_tech/`)

Format mix: 9 epub + 2 pdf + 1 mobi. All text-bearing · no OCR risk.

| # | Author · Title (year) | Type | Size | Extraction method |
|--:|---|---|---:|---|
| 1 | Christopher Steiner · Automate This (2012) | epub | 539 KB | stdlib zipfile + HTML-strip |
| 2 | Davenport & Kirby · Only Humans Need Apply (2016) | epub | 1,346 KB | stdlib zipfile + HTML-strip |
| 3 | Agrawal/Gans/Goldfarb · Power and Prediction (2022) | epub | 4,905 KB | stdlib zipfile + HTML-strip |
| 4 | Agrawal/Gans/Goldfarb · Prediction Machines (2018) | epub | 2,520 KB | stdlib zipfile + HTML-strip |
| 5 | Balaji Srinivasan · The Network State | pdf | 6,086 KB | pdftotext -layout |
| 6 | Chris Dixon · Read Write Own (2024) | epub | 4,579 KB | stdlib zipfile + HTML-strip |
| 7 | Daugherty & Wilson · Human + Machine (2018) | epub | 1,421 KB | stdlib zipfile + HTML-strip |
| 8 | Brynjolfsson & McAfee · The Second Machine Age (2014) | mobi | 1,045 KB | ebook-convert → temp txt → read → remove |
| 9 | Ethan Mollick · Co-Intelligence (2024) | epub | 3,170 KB | stdlib zipfile + HTML-strip |
| 10 | Lakhani & Iansiti · Competing in the Age of AI (2020) | epub | 6,229 KB | stdlib zipfile + HTML-strip |
| 11 | Max Tegmark · Life 3.0 (2017) | pdf | 5,234 KB | pdftotext -layout |
| 12 | Suleyman & Bhaskar · The Coming Wave (2023) | epub | 1,737 KB | stdlib zipfile + HTML-strip |

### 2.2 · Cluster B · AI Edge course + operator/agency AI docs

| # | File | Folder | Type | Size | Extraction method |
|--:|---|---|---|---:|---|
| 13 | Finding Your Edge.pdf | `05_AI_EDGE_COURSE/` | pdf | 541 KB | pdftotext -layout |
| 14 | COURSE WORK 1 thru 2.docx | `05_AI_EDGE_COURSE/` | docx | 61 KB | pandoc -f docx -t plain |
| 15 | AI CHANGED EVERYTHING.docx | `08_AI_TECH/ai_history_case_studies/` | docx | 65 KB | pandoc -f docx -t plain |
| 16 | sniped_os_knowledge_dump.docx | `08_AI_TECH/ai_history_case_studies/` | docx | 27 KB | pandoc -f docx -t plain |
| 17 | youtube skool doc.docx | `10_REFERENCE/_intake_2026-05-18/` | docx | 916 KB | pandoc -f docx -t plain |

**Core total: 17 sources** (12 books + 5 course/operator docs). All already staged in `raw/`. All previously confirmed NOT chunked in any prior batch (grep of `MASTER_CHUNK_MAP.json` source_files: 0 references for sniped_os_knowledge_dump, AI CHANGED EVERYTHING, Finding Your Edge, COURSE WORK, Co-Intelligence, Network State, youtube skool).

**Tooling on PATH (already verified in prior batches):** pdftotext, ebook-convert (calibre), pandoc, unzip, python3 stdlib (zipfile, xml.etree). No new dependencies. No OCR.

---

## 3 · Duplicates · legacy · binaries · videos · OCR-risk · stub flags

| Item | Finding | Action |
|---|---|---|
| `claude_for_small_business_organized.docx` + `_legacy/claude for small business.docx` | Already chunked in the B2B_POSITIONING_CLAUDE_OPERATOR mini-batch (2 source refs in MAP) | EXCLUDE both · do not re-chunk |
| Claude Code Superpowers / Plugin / Built an AI SaaS / REMOTION / ai-ops-dashboard-prd | Already chunked in BATCH_006 (in `_intake_2026-05-18/`) | EXCLUDE · do not re-chunk |
| The Second Machine Age (`.mobi`, labeled "Brilliance Audio on MP3-CD") | Filename implies an audiobook edition · 1,045 KB suggests real text, but the label is a stub risk | PRE-FLIGHT PEEK at extraction time · if it is an audiobook-companion stub (sparse text), defer and flag for an ebook re-acquisition |
| `ai after ramon.docx` + `ai after ramon copy.docx` (raw/ root · 531 KB each) | Byte-identical duplicate pair (discovered-extras set) | If the operator includes them: dedupe to ONE · skip the `copy` |
| `document.pdf` (raw/_intake_2026-05-18 · 3,771 KB, generic name) | Unknown content · possible scanned/image PDF (OCR risk) | DEFER pending pre-flight peek · do not include blind |
| `index.html` (raw/_intake_2026-05-18 · 46 KB) | Likely a saved web page · uncertain value | DEFER pending pre-flight peek |
| Videos | None in the candidate set | n/a · the 8 photographer `.mp4` films are a separate BLOCKED transcription lane, not BATCH_008 |
| OCR-risk in core set | None · all 17 core sources are text-bearing (epub/pdf/mobi/docx) | No OCR needed for the core set |
| Junk scan (`.part`, `~$`, 0-byte, `.DS_Store`) across all candidate dirs | 0 results | clean |

---

## 4 · Recommended inclusion vs defer / exclude

### 4.1 · INCLUDE (core BATCH_008 · 17 sources)
All 12 ai_tech books + Finding Your Edge.pdf + COURSE WORK 1 thru 2.docx + AI CHANGED EVERYTHING.docx + sniped_os_knowledge_dump.docx + youtube skool doc.docx. This is the documented BATCH_008 definition.

### 4.2 · EXCLUDE (already chunked)
- claude_for_small_business (organized + legacy) · B2B_POSITIONING_CLAUDE_OPERATOR.
- Claude Code Superpowers, Claude Code Plugin, Built an AI SaaS, REMOTION, AI Ops Dashboard PRD · BATCH_006.

### 4.3 · DISCOVERED EXTRAS (operator decision · NOT auto-included)
While locating candidates, these loose AI/Claude operator docs were found in `raw/` root + `99_VAULT/`, none yet chunked. They fit the AI theme but are NOT in the documented BATCH_008 definition, so this plan does not silently fold them in. Operator picks one of: (a) add to BATCH_008, (b) hold for a separate `CLAUDE_OPERATOR_DOCS` mini-batch, (c) defer.

| File | Size | Note · recommendation |
|---|---:|---|
| `claude cowork genius.docx` | 255 KB | Claude operator workflow · candidate · likely INCLUDE if expanding |
| `The_Claude_Stack (1).docx` | 56 KB | Claude tooling stack · candidate · likely INCLUDE if expanding · note the ` (1)` dedupe-suffix |
| `Claude_Operating_Manual.docx` | 18 KB | Claude operator doc · candidate · likely INCLUDE if expanding |
| `astro claude websites 3x faster.docx` | 3,042 KB | Claude Code web-build workflow · candidate · INCLUDE if expanding |
| `using ai x gumroad x digital products.docx` | 202 KB | AI productization · candidate · operator decision (could be BATCH_009 commercial) |
| `MORE CLAUDE 5.docx` (99_VAULT/_intake_archive_2026-05-12) | 497 KB | archived Claude doc · peek for staleness · operator decision |
| `ai after ramon.docx` (+ `copy`) | 531 KB | "after ramon" operator-transition doc · ambiguous (account-handover, not clearly AI-canon) · DEFER + peek · dedupe the pair |
| `document.pdf` | 3,771 KB | unknown · OCR risk · DEFER pending peek |
| `index.html` | 46 KB | saved web page · DEFER pending peek |

**Default recommendation:** ship the 17-source core BATCH_008 first; route the discovered extras to a follow-on `CLAUDE_OPERATOR_DOCS` mini-batch after a pre-flight peek, rather than inflating BATCH_008's scope. This keeps BATCH_008 thematically coherent (the AI canon + the AI Edge course) and matches the operator's standing scope discipline.

---

## 5 · Estimated chunk yield + target range

Two clusters, depth-chunked per the BATCH_005 canon-book pattern (short copyright-safe illustrative quotes only · in-copyright books).

| Cluster | Sources | Per-source estimate | Subtotal |
|---|---|---|---:|
| A · 12 ai_tech books | 12 | ~7-9 each | ~84-108 |
| B · AI Edge course + operator/agency docs | 5 | Finding Your Edge ~6-10 · COURSE WORK ~3-5 · AI CHANGED EVERYTHING ~3-5 · sniped_os_knowledge_dump ~3-5 · youtube skool ~5-8 | ~20-33 |
| Cross-source synthesis | n/a | the AI-canon thesis · operator-edge synthesis | ~3-5 |

**Target: ~110-120 chunks. Planning range: 100-135.** Consistent with the documented BATCH_008 estimate (100-130 in NEW_INTAKE_ACK §5 + STAGING_PLAN §5). This is the corpus's largest single batch since BATCH_005 · expect the extraction + chunk-write to run as the two clusters above for cleaner validation and rollback.

---

## 6 · Domain set (reuse existing · NO new domain recommended)

All BATCH_008 content maps onto existing domains. Proposed distribution (refined at chunk-write time):

| Domain | Where it comes from | Rough share |
|---|---|---|
| `strategy` | AI competitive/economic strategy (Prediction Machines, Power and Prediction, Competing in the Age of AI, The Coming Wave, Finding Your Edge) | high |
| `systems-thinking` | economic/institutional/algorithmic systems (Automate This, The Network State, Read Write Own, The Second Machine Age) · the domain introduced via LITERARY_CANON_DYSTOPIAN now does double duty | high |
| `ethics` | AI risk / safety / labor displacement (Life 3.0, The Coming Wave, Only Humans Need Apply, Human + Machine) | medium |
| `ai-tooling` | practical AI use (Co-Intelligence, AI Edge course, the operator docs) | medium |
| `operator-process` | the operator/agency workflow (Finding Your Edge, sniped_os_knowledge_dump, COURSE WORK, youtube skool) | medium |
| `commercial-architecture` | agency business model + productization (AI CHANGED EVERYTHING, Competing in the Age of AI) | medium |
| `client-application` | applying AI for client outcomes (the agency docs) | low |
| `prompt-engineering` | Co-Intelligence practical-prompting chapters · mostly already covered by PROMPT_TEMPLATES_DEEP · cross-reference, few new chunks | low |
| `automation-blueprint` | book-level references to automation · mostly covered by N8N_AUTOMATION_SYSTEMS · cross-reference, few new chunks | low |

### 7 · NEW domain flag
**Recommendation: introduce NO new domain.** The candidate gap is the "disruptive economics of AI" thesis shared by Prediction Machines / Power and Prediction / The Second Machine Age / The Coming Wave. It is adequately served by `strategy` + `systems-thinking` + `ethics`.

Optional, operator-decision-only: a single `ai-economics` domain could give those four books their own retrieval bucket. This plan does NOT recommend it (it would be the corpus's 61st domain for marginal routing benefit). Flagged only because the operator instruction requires surfacing any NEW-domain candidate. Default: reuse existing domains · no new domain.

---

## 8 · How BATCH_008 connects to the existing corpus

- **BATCH_006 operator skill layer:** B006 made the SNIPED skills + Claude Code / n8n / Remotion primitives chunk-addressable (the HOW of operating the engine). BATCH_008 supplies the WHY · the strategic / economic / philosophical canon behind AI adoption (Prediction Machines economics ↔ B006 automation primitives; Co-Intelligence practical-AI ↔ B006 Claude Code workflows). Do NOT re-chunk the B006-chunked `_intake_2026-05-18` Claude Code docs.
- **N8N_AUTOMATION_SYSTEMS:** B008's economics books (Prediction Machines, Power and Prediction) give the thesis for WHY automation creates value · N8N is the build layer that realizes it. The operator/agency docs (sniped_os_knowledge_dump, AI CHANGED EVERYTHING) likely describe the agency model the N8N workflows implement · cross-reference, do not duplicate.
- **PROMPT_TEMPLATES_DEEP:** Co-Intelligence's practical-AI-use chapters reinforce PTD's prompt craft · cross-reference; expect few NEW prompt-engineering chunks (PTD already owns that lane).
- **B2B_POSITIONING_CLAUDE_OPERATOR:** claude_for_small_business is already chunked there (EXCLUDED from B008). B008's "AI CHANGED EVERYTHING" macro thesis + the agency docs extend the commercial / B2B narrative · the market-level WHY behind the B2B demand the mini-batch captured at the buyer level.
- **OPPORTUNITY_MANAGEMENT_TEMPLATES:** the AI Edge course (Finding Your Edge) likely carries the opportunity / ICP / find-your-edge framing that OMT's hopper + business-case templates operationalize · cross-reference.
- **Future recovery batches:** BATCH_008 does NOT touch the flagged literary recovery items (Beloved, Maus I, Jonathan Livingston Seagull, Maus II, Russian-author mobi) · they remain flagged for separate re-acquisition. The queued BATCH_009 (advertising / copywriting) and BATCH_010 (lineage + Black culture) come after BATCH_008.

---

## 9 · Deliverables (defined here · produced only in the authorized extraction session)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/BATCH_008_CHUNKS.jsonl` |
| Extracted text dir | `01_KNOWLEDGE_BASE/batches/batch_008_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/BATCH_008_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/BATCH_008_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/BATCH_008_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/BATCH_008_COMPLETE.md` |
| Extractor script | `scripts/extract_batch_008.py` |
| Chunk-writer script | `scripts/write_batch_008_chunks.py` |

Schema: the canonical BATCH_003-onward 12-field schema (`chunk_id`, `batch_id`, `source_title`, `source_file`, `author`, `domain`, `concept`, `summary`, `usable_principle`, `sniped_relevance`, `direct_quotes`, `tags`). ID pattern `BATCH_008_NNN`. batch_id `BATCH_008`.

---

## 10 · Validation gates (at the authorized extraction session · per `jsonl-validation` SKILL)
JSONL parse (jq -c) · required 12 fields per line · chunk_id uniqueness · single batch_id `BATCH_008` · every source_file resolves under `batch_008_extracted/` · count. Plus: pre-flight stub peek on every source (the Beloved + Second Machine Age lesson), copyright-safe short quotes only, SNIPED-authored output em-dash clean (raw extracted text may retain source em-dashes), no new dependencies, no OCR.

---

## 11 · What this plan does NOT do
- No staging, copying, moving, renaming, or extraction.
- No chunking · no JSONL writes.
- No master-file updates (`MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`, `ACTIVE_KNOWLEDGE_STATE.md` untouched).
- No OCR · no new dependencies.
- No touching the recovery items (Beloved, Maus I, Jonathan Livingston Seagull, Maus II, Russian-author mobi).
- No commits.
- BATCH_008 not started.

Authorization required before any extraction. Stop here.

---

## 12 · Recommended next operation
Operator reviews this plan. On authorization, run the extraction session for the 17-source core in two clusters (A: 12 books · B: 5 course/operator docs), starting with a pre-flight peek on the Second Machine Age mobi and a stub check on each source. Decide the discovered-extras routing (§4.3) separately. Then follow the locked 7-step SOP through consolidation + session-save.

## 13 · Revision log
- **rev 1 (2026-05-22):** First BATCH_008 plan. 17 core sources located (12 ai_tech books + AI Edge course + 2 operator/agency docs + youtube skool doc), all already staged in raw/ and confirmed not previously chunked. EXCLUDE list: claude_for_small_business (B2B) + 5 Claude Code docs (B006). 9 discovered-extra loose AI/Claude docs surfaced as an operator decision. NO new domain recommended (`ai-economics` flagged optional only). Target ~110-120 chunks (range 100-135). Re-written cleanly after a Remote Control socket interruption left no file on disk; state verified intact (995 chunks · clean tree · head 94283a2).
