# PROMPT_TEMPLATES_DEEP mini-batch plan · 2026-05-19

Plan only. No extraction, no chunking, no master-file updates, no BATCH_008 start, no commit. Stops after this plan is written.

This mini-batch extracts durable prompt-craft patterns from 8 AI-Edge prompt-template PDFs (6 unique after dedupe). It is the 6th and final 2026-05-19 mini-batch and the prompt-craft CONTENT layer that the N8N_AUTOMATION_SYSTEMS Cluster B prompt-engineer agent consumes. It extends the BATCH_006 `prompt-engineering` domain.

---

## 0 · Headline

- **Sources:** 8 PDFs (~10.4 MB each · 2 pages each) · ALL CONFIRMED on disk. md5 confirms 2 true-duplicate pairs -> **6 unique templates.**
- **Extraction method:** `pdftotext -layout` (text layer is STRONG · 296-450 words per PDF · NO OCR needed). Extract the 6 UNIQUE PDFs only; skip the 2 duplicate `-2` copies. Strip the promo header/footer line ("Join My AI & Automation Community / skool.com/the-ai-edge").
- **Estimated yield:** 10-15 chunks · target ~12.
- **Domains:** prompt-engineering (primary/bulk), ai-tooling, operator-process (automation-blueprint available if needed). ALL EXIST. No NEW domains.
- **Provenance:** "The AI Edge" prompt-technique cheat sheets · the same course whose books are queued for BATCH_008 and whose templates produced the N8N workflows. Cross-reference BATCH_008, do not merge.

---

## 1 · Source files confirmed on disk + duplicate detection

8 PDFs in `raw/10_REFERENCE/_intake_2026-05-19/prompt_templates/`. Byte size + md5 below.

| File | Bytes | md5 (first 12) | Pages | Dedupe verdict |
|---|---:|---|---:|---|
| Prompt Template - Combining Techniques-2.pdf | 10,364,835 | 0f54f23559... | 2 | DUPLICATE of -3 · EXCLUDE |
| Prompt Template - Combining Techniques-3.pdf | 10,364,835 | 0f54f23559... | 2 | CANONICAL (keep) |
| Prompt Template - In Context-2.pdf | 10,361,462 | e3d42d1ba8... | 2 | UNIQUE (keep) |
| Prompt Template - Problem Decomposition.pdf | 10,363,348 | f6a5b498e2... | 2 | UNIQUE (keep) |
| Prompt Template - Self Criticism (Advanced)-2.pdf | 10,361,550 | d62b67512e... | 2 | DUPLICATE of -3 · EXCLUDE |
| Prompt Template - Self Criticism (Advanced)-3.pdf | 10,361,550 | d62b67512e... | 2 | CANONICAL (keep) |
| Prompt Template - Self Criticism (Basic)-3.pdf | 10,360,554 | 542f744a0f... | 2 | UNIQUE (keep) |
| Prompt Template - Thought Generation-2.pdf | 10,362,278 | 1bfcc8c4d0... | 2 | UNIQUE (keep) |

**Duplicate pairs (md5-confirmed identical, not just same size):**
1. `Combining Techniques-2.pdf` == `Combining Techniques-3.pdf` (md5 `0f54f23559...`). Chunk `-3` as canonical; exclude `-2`.
2. `Self Criticism (Advanced)-2.pdf` == `Self Criticism (Advanced)-3.pdf` (md5 `d62b67512e...`). Chunk `-3` as canonical; exclude `-2`.

**Result: 8 staged PDFs -> 6 unique intellectual sources.** The `-2`/`-3` suffixes are duplicate copies, not different content; they are NOT separate intellectual sources. Do NOT over-chunk them.

Staged in commit `215ffce`. None extracted or chunked.

---

## 2 · Per-template category (filename + text peek)

A read-only `pdftotext` peek (to stdout · no files written) confirmed each template's content. All are AI-Edge cheat sheets: a technique name, then worked business-prompt examples tagged with technique abbreviations.

| # | Unique template | Techniques covered (abbrev) | Sample examples |
|--:|---|---|---|
| 1 | In Context Learning | Few-shot prompting (provide examples, then ask) | content creation, customer service, data analysis |
| 2 | Thought Generation | CoT (Chain of Thought), ThoT (Thread of Thought) | step-by-step logical reasoning, campaign planning, supply-chain problem-solving |
| 3 | Problem Decomposition | LtM (Least-to-Most), PaS (Plan-and-Solve), PoTh (Plan-of-Thought / structured steps) | marketing strategy, customer-feedback analysis, product launch, workflow optimisation |
| 4 | Self-Criticism (Basic) | SE (Self-Evaluation), SR (Self-Refine), COVE (Chain-of-Verification) | product-launch review, sales-pitch refinement, report cross-check |
| 5 | Self-Criticism (Advanced) | S2A (System 2 Attention), RaR (Rephrase and Respond), RE2 (Re-reading) | retention strategy, partnership email, annual-report summary |
| 6 | Combining Techniques (Advanced) | chaining CoT + Problem Decomposition + Self-Criticism in one multi-step prompt | comprehensive marketing plan, customer-feedback improvement plan |

Common structure across all 6: **Task** (what to do) -> **Prompt** (a structured, numbered instruction applying the technique). Each sheet carries a promo header/footer (skool.com/the-ai-edge) that is noise and will be stripped at extraction.

### Theme-coverage check (vs operator brief)

| Theme | Present? | Where |
|---|---|---|
| Prompt structure | Yes | the Task + numbered-Prompt scaffold across all 6 |
| System / input / action layers | Partial | the technique scaffolds layer instruction; no explicit "system/input/action" labels · framed as the instruction-layering pattern |
| Chain-of-thought / reasoning scaffolds | Yes | Thought Generation (CoT, ThoT) |
| Plan-and-solve | Yes | Problem Decomposition (PaS) |
| Self-criticism | Yes | 2 sheets (Basic SE/SR/COVE + Advanced S2A/RaR/RE2) |
| Decomposition | Yes | Problem Decomposition (LtM) |
| Guardrails | Yes | self-criticism / verification IS the guardrail layer (review before ship) |
| Reusable prompt templates | Yes | the entire mini-batch |
| Prompt-writing-agent substrate | Yes | these ARE what the N8N Cluster B agent produces/consumes |
| Support for N8N Prompt Engineer Agent | Yes | direct content-layer pairing |

---

## 3 · Extraction method

`pdftotext -layout` (Poppler · already on PATH). The text layer is STRONG and clean (296-450 words per 2-page PDF · confirmed in the peek), so NO OCR is needed.

- Extract ONLY the 6 unique PDFs (skip the 2 duplicate `-2` copies entirely).
- Strip the promo header/footer line ("Join My AI & Automation Community" + the skool.com URL) as noise; keep all substantive Task/Prompt content.
- Sanity floor: each extracted file must yield >= 100 words; if any comes back near-empty, mark it OCR-deferred (do NOT OCR now) and surface to the operator rather than chunking a weak text layer.

Output: one normalized `.txt` per unique template in `01_KNOWLEDGE_BASE/batches/prompt_templates_deep_extracted/`.

---

## 4 · Estimated chunk yield · 10-15 chunks · target ~12

Per-technique chunks (one per unique template · NOT per duplicate copy) plus cross-cutting synthesis chunks.

### Per-technique (6)

| # | Chunk | Domain |
|--:|---|---|
| 1 | In-Context Learning / few-shot prompting · examples-then-ask | prompt-engineering |
| 2 | Thought Generation · Chain-of-Thought + Thread-of-Thought reasoning scaffolds | prompt-engineering |
| 3 | Problem Decomposition · Least-to-Most + Plan-and-Solve + Plan-of-Thought | prompt-engineering |
| 4 | Self-Criticism (Basic) · Self-Evaluation + Self-Refine + Chain-of-Verification | prompt-engineering |
| 5 | Self-Criticism (Advanced) · System-2-Attention + Rephrase-and-Respond + Re-reading | prompt-engineering |
| 6 | Combining Techniques · chaining CoT + decomposition + self-criticism in one prompt | prompt-engineering |

### Cross-cutting synthesis (~6)

| # | Chunk | Domain |
|--:|---|---|
| 7 | The prompt-technique taxonomy · the full abbreviation map (few-shot, CoT, ThoT, LtM, PaS, PoTh, SE, SR, COVE, S2A, RaR, RE2) as a reference index | prompt-engineering |
| 8 | The Task + structured-Prompt template scaffold · the common reusable shape across all sheets | prompt-engineering |
| 9 | Self-criticism as a guardrail layer · verification/refinement before shipping output (Basic + Advanced synthesis) | prompt-engineering |
| 10 | The reasoning-scaffold family · when to use step-by-step (CoT) vs plan-first (PaS) vs least-to-most (LtM) | prompt-engineering |
| 11 | Prompt-writing-agent substrate · these templates ARE the content the N8N Cluster B deep-reasoning vs normal sub-agents produce (the bridge to N8N_AUTOMATION_SYSTEMS) | ai-tooling |
| 12 (optional) | Few-shot vs zero-shot economics · in-context examples as the cheapest quality lever | prompt-engineering |

That is 11-12 mapped chunks. Range 10-15 leaves room to drop the optional 12 or merge 9+10. Target ~12. The 2 duplicate copies contribute 0 additional chunks.

---

## 5 · Approved domains / tags

All candidate domains ALREADY EXIST. No NEW domains. Counts at 906-chunk state:

| Domain | Current count | Use in this mini-batch |
|---|---:|---|
| prompt-engineering | 8 | primary on the 6 per-technique + taxonomy/structure/guardrail/family chunks (the bulk) · roughly doubles this BATCH_006 domain |
| ai-tooling | 18 | primary on the prompt-writing-agent-substrate / N8N-bridge chunk |
| operator-process | 32 | available as a secondary tag (prompt discipline as an operating practice); no primary expected |
| automation-blueprint | 17 | available as a secondary tag on the N8N-bridge chunk if needed; no primary expected |

**Recommended tag bank:** `prompt-engineering`, `prompt-template`, `few-shot`, `in-context-learning`, `chain-of-thought`, `cot`, `thread-of-thought`, `problem-decomposition`, `least-to-most`, `plan-and-solve`, `plan-of-thought`, `self-criticism`, `self-evaluation`, `self-refine`, `chain-of-verification`, `system-2-attention`, `rephrase-and-respond`, `re-reading`, `combining-techniques`, `reasoning-scaffold`, `prompt-guardrail`, `task-prompt-scaffold`, `prompt-writing-agent`, `n8n-bridge`, `the-ai-edge`, `ai-tooling-aging-risk`.

**Aging note:** the technique names are reasonably durable (CoT/few-shot/self-criticism are established craft), but the specific framing and the AI-Edge packaging age; carry `ai-tooling-aging-risk` + the 2026-05-19 source date. Summaries foreground the durable technique and treat the worked business examples as illustration.

---

## 6 · How this mini-batch connects to the rest of the corpus

### BATCH_006 operator skill layer
- Directly EXTENDS the BATCH_006 `prompt-engineering` domain (currently 8 chunks: TCREI, framework-orchestrator, pyramid-structured-communication, etc. · roughly doubles it). These templates are the technique-level complement to the B6 framework-level prompt packs.

### N8N_AUTOMATION_SYSTEMS Prompt Engineer Agent cluster
- This is the CONTENT layer for N8N Cluster B (chunks 003-005, 010 of N8N): the Master Prompt Agent routes to deep-reasoning vs normal model-tier sub-workflows that PRODUCE structured prompts · these templates are exactly the kind of structured output those sub-agents generate (the Combining-Techniques and Self-Criticism scaffolds in particular). Chunk 11 is the explicit bridge. N8N is the IMPLEMENTATION (the agent); PROMPT_TEMPLATES_DEEP is the CRAFT (the technique). Complementary · cross-reference, do not merge.

### Future BATCH_008 AI / tech canon (NOT started)
- These are AI-Edge-course TEMPLATES; the course books are queued for BATCH_008. Keep the technique cheat sheets here as a reusable prompt-craft mini-batch · cross-reference BATCH_008, do not merge. With this mini-batch, all of the AI Edge non-book artifacts (n8n workflows, opportunity templates, prompt templates) are chunked; only the AI Edge BOOKS remain for BATCH_008.

---

## 7 · Deliverables (produced in the EXTRACTION + CHUNK session · NOT now)

| Deliverable | Path | Notes |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/PROMPT_TEMPLATES_DEEP_CHUNKS.jsonl` | 10-15 chunks · batch_id `PROMPT_TEMPLATES_DEEP` · 12-field canonical schema |
| Extracted source dir | `01_KNOWLEDGE_BASE/batches/prompt_templates_deep_extracted/` | 6 normalized `.txt` (unique templates only · promo lines stripped) |
| Summary | `01_KNOWLEDGE_BASE/summaries/PROMPT_TEMPLATES_DEEP_SUMMARY.md` | what it covers · where it lands · dedupe record · cross-references |
| Source index | `01_KNOWLEDGE_BASE/indexes/PROMPT_TEMPLATES_DEEP_SOURCE_INDEX.md` | per-chunk concept + domain + source-template map + dedupe note |
| Extraction log | `00_COMMAND_CENTER/batch_logs/PROMPT_TEMPLATES_DEEP_EXTRACTION_LOG.md` | sources in / extracted out / duplicates excluded / failures |
| Completion marker | `00_COMMAND_CENTER/batch_logs/PROMPT_TEMPLATES_DEEP_COMPLETE.md` | status · validation summary · deviations |
| Extraction script | `scripts/extract_prompt_templates_deep.py` | NEEDED · `pdftotext -layout` on the 6 unique PDFs · promo-line strip · dedupe-skip the 2 `-2` copies. Mirror `scripts/extract_personal_operating_code.py`. |
| Chunk writer | `scripts/write_prompt_templates_deep_chunks.py` | NEEDED · hand-authored chunk emit + em-dash sweep via `chr(0x2014)`. Mirror `scripts/write_n8n_automation_systems_chunks.py`. |

### Schema decisions (recommended · finalized at chunk-write time)
- `batch_id`: `PROMPT_TEMPLATES_DEEP`
- `chunk_id` pattern: `PROMPT_TEMPLATES_DEEP_001` ... `_0NN`
- `source_title`: `Prompt Template · <technique> · The AI Edge` for per-technique chunks; `Prompt Templates Deep · cross-template pattern` for synthesis chunks
- `author`: `The AI Edge (prompt-technique templates)`
- `source_file`: normalized lowercase-snake-case `.txt` per UNIQUE template · `prompt_template_in_context.txt`, `prompt_template_thought_generation.txt`, `prompt_template_problem_decomposition.txt`, `prompt_template_self_criticism_basic.txt`, `prompt_template_self_criticism_advanced.txt`, `prompt_template_combining_techniques.txt`. Synthesis chunks cite the most representative template (each resolves on disk for jsonl-validation check 5).

---

## 8 · Explicit exclusions

| Material | Disposition |
|---|---|
| `Combining Techniques-2.pdf` | EXCLUDE · md5-identical duplicate of `-3` |
| `Self Criticism (Advanced)-2.pdf` | EXCLUDE · md5-identical duplicate of `-3` |
| Promo header/footer ("Join My AI & Automation Community" + skool.com URL) | STRIP at extraction · noise, not prompt-craft |
| The worked business examples | KEPT as illustration inside the relevant technique chunk; summaries foreground the durable technique, not the specific example |
| Literary intake sources | OUT OF SCOPE · not touched |
| The AI Edge course BOOKS | OUT OF SCOPE · queued for BATCH_008 |

---

## 9 · What this planning session does NOT do

- No extraction. The planning peek used `pdftotext` to stdout only · no extracted files written.
- No chunking. No JSONL writes.
- No master-file updates (`MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`, `ACTIVE_KNOWLEDGE_STATE.md` untouched).
- No script files written.
- No BATCH_008 start.
- No literary intake touched.
- No source files moved/renamed/deleted.
- No commit.

---

## 10 · Recommended next operation

Authorize the extraction + chunk session per the locked 7-step SOP (steps 5-6):
1. Run `scripts/extract_prompt_templates_deep.py` · `pdftotext -layout` on the 6 UNIQUE PDFs into `prompt_templates_deep_extracted/` (skip the 2 `-2` duplicates · strip promo lines).
2. Hand-author 10-15 chunks (target ~12) per the section 4 map · 1 chunk per unique technique, no duplicate chunks.
3. Run `jsonl-validation` (6 checks) + em-dash sweep.
4. Write summary + source index + logs + completion marker.
5. Stop after validation + reporting · await `master-consolidation` authorization.

After this mini-batch consolidates (target 906 -> ~916-921), the 2026-05-19 mini-batch sequence is COMPLETE. The next queued work per `STAGING_PLAN_2026-05-19_INTAKE.md` section 5 is the 3 literary-canon mini-batches (BLACK / DYSTOPIAN / GENERAL), then BATCH_008 AI/tech canon (the AI Edge books + ai_tech books).

---

## 11 · Revision log

- **rev 1 (2026-05-19 · this version):** First plan for the PROMPT_TEMPLATES_DEEP mini-batch. All 8 PDFs confirmed on disk. md5 dedupe confirmed 2 true-duplicate pairs (Combining Techniques -2/-3, Self Criticism Advanced -2/-3) -> 6 unique templates. Read-only pdftotext peek confirmed strong text layer (296-450 words/PDF · no OCR needed). Extraction method: pdftotext -layout on the 6 unique PDFs, promo-line strip, dedupe-skip the 2 copies. 10-15 chunk estimate · target ~12 · 1 chunk per unique technique (no over-chunking duplicates). All candidate domains (prompt-engineering, ai-tooling, operator-process, automation-blueprint) confirmed pre-existing · no NEW domains. Cross-references mapped to B6 prompt-engineering (extends it), N8N Cluster B prompt-engineer agent (the content the agent consumes), and future BATCH_008 (templates here, books there · keep separate).
