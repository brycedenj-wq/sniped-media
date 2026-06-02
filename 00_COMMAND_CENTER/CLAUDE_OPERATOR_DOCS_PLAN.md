# CLAUDE_OPERATOR_DOCS mini-batch plan · loose AI/Claude operator docs · 2026-05-22

Plan only. No staging, extraction, chunking, master-file updates, OCR, or commits. This plan defines the CLAUDE_OPERATOR_DOCS mini-batch so a later authorized extraction session can run the locked SOP (extract → chunk → validate → ship → consolidate → session-save) without re-deriving scope.

**Source universe:** `~/AI-Brain-Refinery/raw/` (already staged). No new staging required.
**Theme:** extract useful operator signal from the loose AI/Claude docs discovered during BATCH_008 and deliberately excluded from its core scope. The unifying thread is *Claude-as-operating-system* (context architecture, workspaces, skills, co-work mode) and AI-applied-in-a-real-business, not the AI/tech canon (BATCH_008) and not the build primitives (BATCH_006).
**Naming:** `CLAUDE_OPERATOR_DOCS` (non-BATCH_NNN mini-batch slug · preserves numbered-batch slots for BATCH_009+). batch_id `CLAUDE_OPERATOR_DOCS`. ID pattern `CLAUDE_OPERATOR_DOCS_NNN`.

---

## 0 · Verified starting state (this session)

- Latest commit: `d8b4e5f save session after BATCH_008 consolidation`
- Total chunks: 1,115 · 8 numbered batches + 9 mini-batches · 60 official domains
- Working tree: clean
- BATCH_008 complete and canonical
- These 9 candidate docs are confirmed NOT chunked in any prior batch (the only MASTER_CHUNK_MAP.json references are the BATCH_008 `discovered_extras_operator_decision` exclusion note · 0 actual chunks)

---

## 1 · Candidate inventory (located + inspected · read-only peek)

10 files located (9 named candidates · the `ai after ramon` pair is two files). Each peeked read-only via pandoc/pdftotext to stdout (nothing written to disk).

| # | File | Path | Type | Size | Words (extracted) | Source-readable? |
|--:|---|---|---|---:|---:|---|
| 1 | `Claude_Operating_Manual.docx` | `raw/` | docx | 18 KB | 2,989 | YES · clean prose |
| 2 | `The_Claude_Stack (1).docx` | `raw/` | docx | 56 KB | 13,253 | YES · clean prose |
| 3 | `claude cowork genius.docx` | `raw/` | docx | 255 KB | 66,376 | YES · video transcript (timestamps) |
| 4 | `ai after ramon.docx` | `raw/` | docx | 531 KB | 137,068 | YES · video transcript (timestamps) |
| 5 | `ai after ramon copy.docx` | `raw/` | docx | 531 KB | 137,068 | YES · BYTE-IDENTICAL dup of #4 (md5 `4e9fd4f2…`) |
| 6 | `using ai x gumroad x digital products.docx` | `raw/` | docx | 202 KB | 55,649 | YES · structured layers + transcript |
| 7 | `astro claude websites 3x faster.docx` | `raw/10_REFERENCE/_intake_2026-05-18/` | docx | 3,042 KB | 853,149 | PARTIAL · web-page scrape (heavy boilerplate noise) |
| 8 | `MORE CLAUDE 5.docx` | `raw/99_VAULT/_intake_archive_2026-05-12/` | docx | 497 KB | 137,411 | PARTIAL · Anthropic Help Center / Release Notes scrape |
| 9 | `document.pdf` | `raw/10_REFERENCE/_intake_2026-05-18/` | pdf | 3,771 KB | 57,107 | YES · but it is a BOOK (see §3) |
| 10 | `index.html` | `raw/10_REFERENCE/_intake_2026-05-18/` | html | 46 KB | 0 | NO · JS app shell, 0 static text (see §3) |

Extraction methods (for the included set): `pandoc -f docx -t plain` for the docx files. No OCR. No new dependencies.

---

## 2 · Content classification (from the read-only peek)

- **Claude_Operating_Manual.docx** · HIGH signal. Self-describes as "synthesized from 160K+ lines of transcripts across 3 source files, all redundancy removed." Core thesis: *AI superiority is context architecture, not prompting skill; Claude is an operating system you configure, not a chatbot you ask.* Covers workspaces, CLAUDE.md, skills as reusable automation packages, sub-agents, MCP, website building. Dense, deduplicated operator doctrine.
- **The_Claude_Stack (1).docx** · HIGH signal and SNIPED-native. The fifth volume of the operator's own "Stack" series (Direction / Production / Revenue / Attention / Claude). It is *the operating layer underneath the other four* · context architecture, skills, commands, sub-agents, workspaces, AI-as-force-multiplier for a working photographer running a business at agency scale. (The ` (1)` suffix is a download-rename artifact; it is the only copy on disk.)
- **claude cowork genius.docx** · GOOD signal. Video transcript walking through Claude desktop's chat / co-work / code tabs and using co-work mode for real work instead of copy-paste chat. Practical ai-tooling. High word count but a single walkthrough · chunk selectively.
- **ai after ramon.docx** · GOOD signal. Video transcript from a founder ("last year my company did over $250M in aggregate revenue") on how they apply AI to make the business better, cheaper, faster, less risky, with real examples. AI-applied-in-a-real-business case study · client-application + strategy.
- **using ai x gumroad x digital products.docx** · MODERATE signal · weakest thematic fit. Structured (strategic / operational layers) on Amazon KDP + AI-assisted digital-product publishing + profit-first niches. This is AI-x-product-monetization more than Claude-operation; it overlaps future BATCH_009 / a monetization lane.
- **astro claude websites 3x faster.docx** · LOW signal as extracted. Despite the filename (build websites 3x faster with Claude + Astro), the extracted text is dominated by a scraped marketing landing page ("Super Carl, your AI Super Connector"). 853K words from a 3 MB docx is a boilerplate-noise red flag · the useful content (if any) is buried in scrape artifacts.
- **MORE CLAUDE 5.docx** · LOW durable signal + STALE. A scrape of Anthropic's Claude Help Center / Release Notes (April 2026 · "Claude Design," Opus 4.7). Release notes age fast, the doc is nav-boilerplate heavy, and it sits in the `99_VAULT/_intake_archive` (already archived).

---

## 3 · Duplicates · stale/legacy · low-signal · bad downloads · HTML artifacts · overlaps

| Item | Finding | Action |
|---|---|---|
| `ai after ramon copy.docx` | BYTE-IDENTICAL to `ai after ramon.docx` (same md5) | EXCLUDE the `copy` · chunk only one |
| `document.pdf` | NOT a Claude doc · it is **Seth Godin, "This is Marketing" (2018, Portfolio/Penguin)** · a full in-copyright marketing book hidden behind a generic filename | EXCLUDE from this mini-batch · REROUTE to BATCH_009 advertising/copywriting canon |
| `index.html` | "AI Ops Dashboard" · a JS app shell with 0 extractable static text · the build artifact of the AI Ops Dashboard PRD already chunked in BATCH_006 | EXCLUDE · not source-readable · overlaps BATCH_006 |
| `astro claude websites 3x faster.docx` | Web-page scrape · 853K words dominated by a "Super Carl" landing page · content does not match the filename | DEFER · needs careful manual review before any chunking · high noise risk |
| `MORE CLAUDE 5.docx` | Anthropic Help Center / release-notes scrape · stale, boilerplate-heavy, archived location | DEFER / EXCLUDE · low durable operator signal, high staleness |
| Overlap with BATCH_006 | B006 holds the Claude Code / skills primitives; these docs are operator-level Claude practice, not the same chunks | INCLUDE the unique operator signal · cross-reference, do not duplicate |
| Overlap with BATCH_008 | B008 is the AI/tech canon (books + course); these are practical Claude-operation docs | distinct · no overlap |

---

## 4 · Recommended include vs defer / exclude

### 4.1 · INCLUDE (core · 5 sources)
1. `Claude_Operating_Manual.docx` (HIGH)
2. `The_Claude_Stack (1).docx` (HIGH · SNIPED-native)
3. `claude cowork genius.docx` (GOOD · chunk selectively)
4. `ai after ramon.docx` (GOOD · chunk selectively · dedupe the `copy`)
5. `using ai x gumroad x digital products.docx` (LIGHT · 2-3 chunks · weakest fit · operator may veto to a monetization lane)

### 4.2 · DEFER (pending operator review · 0 chunks until cleared)
- `astro claude websites 3x faster.docx` · web-scrape noise · needs manual signal extraction first.
- `MORE CLAUDE 5.docx` · stale release-notes scrape · low durable value.

### 4.3 · EXCLUDE
- `ai after ramon copy.docx` · byte-identical duplicate.
- `document.pdf` · Seth Godin "This is Marketing" · wrong theme · REROUTE to BATCH_009.
- `index.html` · AI Ops Dashboard build artifact · 0 text · overlaps BATCH_006.

---

## 5 · Estimated chunk yield

| Source | Estimate |
|---|---:|
| Claude_Operating_Manual.docx | 5-7 |
| The_Claude_Stack (1).docx | 6-9 |
| claude cowork genius.docx | 4-6 |
| ai after ramon.docx | 4-6 |
| using ai x gumroad x digital products.docx (light) | 2-3 |
| Cross-source synthesis | 1-2 |

**Target: ~22-26 chunks. Planning range: 16-32.** A small, high-signal mini-batch (several sources are long transcripts that compress to a handful of distinct, durable concepts each).

---

## 6 · Domain set (existing domains only · NO new domain expected)

All from the operator-approved list, all pre-existing in the corpus:

| Domain | Where it comes from |
|---|---|
| `ai-tooling` | Claude-as-OS, context architecture, co-work mode, skills/MCP, the practical Claude stack |
| `operator-process` | workspace setup, the working practice of running AI as a force multiplier, daily operator habits |
| `meta-doctrine` | the "Claude is an operating system, not a chatbot" thesis · context-beats-prompting as a stance |
| `strategy` | AI-as-leverage / force-multiplier, the throughput-doubling argument, AI-applied-at-business-scale |
| `client-application` | AI applied in a real business (ai after ramon), productization (gumroad, light) |
| `prompt-engineering` | context-beats-prompting · only where it adds beyond PROMPT_TEMPLATES_DEEP (expect 0-1, lane stays owned by PTD) |
| `automation-blueprint` | skills/commands/sub-agent workflows where a concrete build is described (expect 0-2) |

**NO new domain.** If extraction reveals a genuine gap not covered by these, halt and report rather than introduce one silently.

---

## 7 · How this mini-batch connects to the corpus

- **BATCH_006 operator skill layer:** B006 made the SNIPED skills + Claude Code / n8n / Remotion primitives chunk-addressable (the build primitives). CLAUDE_OPERATOR_DOCS adds the *operator practice* layer on top: how to configure Claude as a workspace/OS, when to use co-work vs chat vs code, context architecture as the real lever. Cross-reference the B006 Claude Code chunks; do not duplicate them.
- **BATCH_008 AI/tech canon:** B008 is the strategic/economic/philosophical WHY (the books) + the agency HOW (the course). This mini-batch is the *day-to-day Claude-operation HOW* · the hands-on practice that sits below the canon. Co-Intelligence's "invite AI to the table" / Jagged Frontier (B008) is the principle; the Claude Operating Manual is the implementation.
- **N8N_AUTOMATION_SYSTEMS:** where these docs describe skills/commands/sub-agent automations, they are the Claude-side complement to the n8n build layer · cross-reference, do not duplicate.
- **PROMPT_TEMPLATES_DEEP:** the "context beats prompting" thesis reframes PTD's prompt craft (prompts matter, but context architecture matters more) · expect 0-1 prompt-engineering chunks · the lane stays owned by PTD.

---

## 8 · Deliverables (defined here · produced only in the authorized extraction session)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/CLAUDE_OPERATOR_DOCS_CHUNKS.jsonl` |
| Extracted text dir | `01_KNOWLEDGE_BASE/batches/claude_operator_docs_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/CLAUDE_OPERATOR_DOCS_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/CLAUDE_OPERATOR_DOCS_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/CLAUDE_OPERATOR_DOCS_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/CLAUDE_OPERATOR_DOCS_COMPLETE.md` |
| Extractor script | `scripts/extract_claude_operator_docs.py` |
| Chunk-writer script | `scripts/write_claude_operator_docs_chunks.py` |

Schema: the canonical 12-field schema (`chunk_id`, `batch_id`, `source_title`, `source_file`, `author`, `domain`, `concept`, `summary`, `usable_principle`, `sniped_relevance`, `direct_quotes`, `tags`). ID pattern `CLAUDE_OPERATOR_DOCS_NNN`. batch_id `CLAUDE_OPERATOR_DOCS`.

---

## 9 · Validation gates (at the authorized extraction session)
The 6 jsonl-validation checks (parse · 12 fields · chunk_id uniqueness · single batch_id `CLAUDE_OPERATOR_DOCS` · source_file resolution · count) plus: pre-flight stub/signal peek on every source, dedupe the `ai after ramon` pair, copyright-safe short quotes only, SNIPED-authored output em-dash clean, no new dependencies, no OCR, no new domain.

---

## 10 · What this plan does NOT do
- No staging, extraction, chunking, or master-file updates.
- No OCR · no new dependencies.
- No touching recovery items (Beloved, Maus I, Jonathan Livingston Seagull, Maus II, Russian-author mobi).
- No starting BATCH_009 (and `document.pdf` / "This is Marketing" is rerouted there, not chunked here).
- No commits.

Authorization required before any extraction. Stop here.

---

## 11 · Open operator decisions surfaced
1. **`using ai x gumroad x digital products.docx`** · include light (2-3 chunks) here, or route to a future monetization / BATCH_009 lane? Default: include light, flagged.
2. **`astro claude websites 3x faster.docx` + `MORE CLAUDE 5.docx`** · defer (recommended) or attempt salvage chunking despite the scrape noise / staleness? Default: defer.
3. **`document.pdf` ("This is Marketing")** · confirm reroute to BATCH_009 (recommended). It is a clean, valuable marketing canon book · just not a Claude doc.

---

## 12 · Revision log
- **rev 1 (2026-05-22):** First CLAUDE_OPERATOR_DOCS plan. 10 files inspected (9 candidates · 1 dup). INCLUDE 5 (Claude_Operating_Manual, The_Claude_Stack, claude cowork genius, ai after ramon, using ai x gumroad light). DEFER 2 (astro claude websites, MORE CLAUDE 5). EXCLUDE 3 (ai after ramon copy = dup; document.pdf = Seth Godin "This is Marketing", reroute to BATCH_009; index.html = AI Ops Dashboard artifact, overlaps B006). Target ~22-26 chunks (range 16-32). Existing domains only (ai-tooling, operator-process, meta-doctrine, strategy, client-application, prompt-engineering, automation-blueprint); no new domain. No extraction, chunking, master updates, or commits performed.
