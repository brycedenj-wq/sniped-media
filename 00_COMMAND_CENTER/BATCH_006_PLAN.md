# BATCH_006 plan · operator-engine skill layer (two-pass split) · 2026-05-18 · rev 2

Plan only. No extraction, no chunking, no master-file updates, no source moves. Authorization required before any execution.

**Two-pass split locked.** This revision splits the originally-scoped BATCH_006 into two focused batches:

- **BATCH_006 (this plan)** · the operator-engine skill layer · SNIPED skills + 50-skill prompt pack + minimum supporting prompt-workflow / tool-workflow / automation docs that make the skill layer coherent.
- **BATCH_007 (deferred · see §11)** · operator doctrine + SOPs + working drafts + outreach + delivery + content + commercial singletons.

**Theme for BATCH_006:** install the reusable skill layer · prompts, tool workflows, automation patterns, operator-engine primitives. Nothing else.

**Sources scoped to 3 folders in `~/AI-Brain-Refinery/raw/`:**
- `_skills/` · 50 SNIPED skill packs + 1 build-queue meta-doc
- `Claude_AI_Skills_50_Upload_Ready (1)/` · 50-skill prompt pack
- `10_REFERENCE/_intake_2026-05-18/` · Claude / AI operating docs + 2 automation blueprints + REMOTION

**Total file candidates surveyed:** 108 files across the 3 folders.
**Recommended BATCH_006 inclusion set:** 108 files.
**Defer / exclude from this batch:** see §3 (deferred to BATCH_007 = ~50 files in 9 other folders, plus 5 in-folder items at `10_REFERENCE/_intake_2026-05-18/` that are sniped-media web codebase / unlabeled / BATCH_008 territory).
**Estimated chunk yield:** 100-125 chunks · target 115 (1-chunk-per-SKILL for the 100 skill packs · 1-3 chunks for the larger supporting docs).

---

## 1 · Full source candidate inventory

### 1.1 · `raw/_skills/` · 51 files (228 KB · 2,404 total lines)

50 `sniped-*/SKILL.md` files at avg 48 lines · structured frontmatter (`name`, `description`) + INVOKE WHEN + MANDATORY READING + OUTPUT + REFUSE. Plus 1 meta-doc `SKILL_BUILD_QUEUE.md` (9.2 KB · prioritized build order with 28-of-50 status).

| # | Skill folder | Lines |
|--:|---|---:|
| 0 | SKILL_BUILD_QUEUE.md (meta) | ~230 |
| 1 | sniped-ai-image-tool-pick | 35-50 |
| 2 | sniped-ai-photographer-market | 35-50 |
| 3 | sniped-ai-sentiment | 35-50 |
| 4 | sniped-analog-premium | 35-50 |
| 5 | sniped-art-series | 35-50 |
| 6 | sniped-assistant-task-routing | 45 |
| 7 | sniped-blockbuster-strategy | 35-50 |
| 8 | sniped-canonical-truths | 30 |
| 9 | sniped-caption-writer | 162 |
| 10 | sniped-capture-to-delivery | 35-50 |
| 11 | sniped-company-of-one | 35-50 |
| 12 | sniped-direction-stack | 35 |
| 13 | sniped-discovery-to-close | 35-50 |
| 14 | sniped-evoto-skin-pass | 35-50 |
| 15 | sniped-execution-prioritization | 35-50 |
| 16 | sniped-hero-composite-ceiling | 35-50 |
| 17 | sniped-hero-composite-lite | 35-50 |
| 18 | sniped-higgsfield-pipeline | 35-50 |
| 19 | sniped-hit-mechanics | 35-50 |
| 20 | sniped-hospitality-layer | 35-50 |
| 21 | sniped-lean-audit | 35-50 |
| 22 | sniped-leverage-logic | 35-50 |
| 23 | sniped-lighting-vault | 35-50 |
| 24 | sniped-luxury-edit | 135 |
| 25 | sniped-monday-cockpit | 35-50 |
| 26 | sniped-new-luxury | 35-50 |
| 27 | sniped-notion-crm-update | 35-50 |
| 28 | sniped-partnership-protocol | 35-50 |
| 29 | sniped-perennial-seller | 35-50 |
| 30 | sniped-photo-theory | 35-50 |
| 31 | sniped-pixieset-gallery | 35-50 |
| 32 | sniped-positioning-phrases | 35-50 |
| 33 | sniped-post-delivery | 35-50 |
| 34 | sniped-post-shoot-same-day | 35-50 |
| 35 | sniped-pre-shoot-prep | 35-50 |
| 36 | sniped-pricing-decision | 35-50 |
| 37 | sniped-production-os | 29 |
| 38 | sniped-retoucher-onboarding | 35-50 |
| 39 | sniped-reverse-roadmap | 35-50 |
| 40 | sniped-seedream-prompt | 35-50 |
| 41 | sniped-shoot-day-reset | 35-50 |
| 42 | sniped-shoot-day-strategic-free | 35-50 |
| 43 | sniped-status-psychology | 35-50 |
| 44 | sniped-strategic-implications | 35-50 |
| 45 | sniped-trust-equation | 35-50 |
| 46 | sniped-trust-mechanics | 35-50 |
| 47 | sniped-udemy-ai-accelerants | 28 |
| 48 | sniped-udemy-lightroom-rails | 28 |
| 49 | sniped-vib-outreach | 150 |
| 50 | sniped-wwp-positioning | 35-50 |

### 1.2 · `raw/Claude_AI_Skills_50_Upload_Ready (1)/` · 50 SKILL.md files (236 KB · 2,697 total lines)

Avg 54 lines · YAML frontmatter (multi-line `description: |`) + Purpose + When to Use + Instructions + Workflow + Output Format + Constraints. Each is a self-contained framework prompt.

Files (alphabetical): `ai-agent-architecture-wat`, `ai-code-website-build-pipeline`, `ai-video-production-pipeline`, `bad-strategy-audit`, `business-entity-credit-architecture`, `business-resilience-audit`, `calm-authority-voice-calibration`, `cognitive-bias-audit`, `cold-email-campaign-architecture`, `comparative-advantage-resource-allocation`, `consultative-selling-system`, `copywriting-rule-of-one-awareness-staging`, `counter-positioning-diagnosis`, `create-destroy-strategy-stress-test`, `creative-resistance-turning-pro`, `customer-segment-slicing`, `economic-incentive-policy-analysis`, `epms-site-analysis`, `fermi-estimation`, `framework-orchestrator`, `freelance-platform-optimization`, `hoshin-kanri-goal-alignment`, `industry-dynamics-assessment`, `lean-transformation-diagnostic`, `linkedin-growth-lead-generation`, `market-evaluation-scorecard`, `meta-business-infrastructure-setup`, `mom-test-customer-conversation`, `munger-two-track-decision-analysis`, `negotiation-leverage-black-swan`, `photography-business-system`, `premortem-analysis`, `preset-sync-export-photo-editing`, `professional-portrait-direction`, `prompt-engineering-tcrei`, `pyramid-structured-communication`, `revenue-growth-diagnostic`, `second-brain-code-para`, `server-farm-commissioning`, `seven-powers-strategic-position-assessment`, `shadow-test-pre-launch-validation`, `signal-noise-forecasting-bayesian`, `social-media-content-strategy`, `strategy-kernel-development`, `success-message-design`, `superforecasting-workflow`, `system-analysis-intervention-design`, `tactical-negotiation-ackerman-empathy`, `value-stream-improvement-pdca`, `video-editing-assembly-line`.

### 1.3 · `raw/10_REFERENCE/_intake_2026-05-18/` · minimum supporting prompt-workflow / tool-workflow / automation docs

INCLUDE for BATCH_006 (these are the primitives that make the skill layer coherent):

| # | File | Size | Why this batch |
|--:|---|---:|---|
| 1 | `CLAUDE CODE SUPERPOWERS.docx` | 48 KB | Claude Code productivity primitives · directly improves how the SKILL.md files are invoked. Tool workflow. |
| 2 | `CLAUDE CODE PLUGIN.docx` | 32 KB | Claude Code plugin patterns · tool workflow for skill-pack delivery. |
| 3 | `ai-ops-dashboard-prd.md` | 20 KB | AI-ops dashboard PRD · architectural pattern for orchestrating skill invocations at scale. Operator-engine primitive. |
| 4 | `Built an AI SaaS in 20 min.docx` | 68 KB | Rapid-build pattern for AI tooling · automation primitive. |
| 5 | `REMOTION.docx` | 28 KB | Remotion video automation pipeline · automation pattern. Pairs with `sniped-video-philosophy` work (deferred to B7) but the framework itself is a primitive. |
| 6 | `automations/AI Content Strategy Generator - Lead Magnet.json` | JSON | Automation blueprint · directly executable workflow. |
| 7 | `automations/Blueprint - ElevenLabs Agent That Calls & Qualifies Leads.json` | JSON | ElevenLabs voice-agent blueprint · directly executable workflow. |

DEFER from this folder:
- `astro claude websites 3x faster.docx` (3.0 MB) · sniped-media web-codebase territory · separate workspace
- `youtube skool doc.docx` (920 KB) · likely course-transcript dump · BATCH_008 territory
- `document.pdf` · unlabeled · operator decision needed
- `index.html` · web-codebase territory

---

## 2 · Source categorization (BATCH_006 reduced to 4 buckets)

### A · SNIPED skills (51 files · `raw/_skills/`)
The SNIPED-internal skill packs · 50 `sniped-*/SKILL.md` files + 1 `SKILL_BUILD_QUEUE.md` meta-doc. This IS the operator engine. Each skill is a self-contained invocation pattern with frontmatter, INVOKE WHEN trigger conditions, MANDATORY READING references, OUTPUT spec, and REFUSE rules.

### B · 50-skill prompt pack (50 files · `raw/Claude_AI_Skills_50_Upload_Ready (1)/`)
External / framework-based prompt packs (TCREI, premortem, fermi, mom-test, hoshin-kanri, signal-noise-bayesian, etc.) and ops-engineering routines. Designed for upload as a Claude skill bundle. Each is a self-contained framework prompt.

### C · Claude / AI tool workflows (4 files)
- `CLAUDE CODE SUPERPOWERS.docx`
- `CLAUDE CODE PLUGIN.docx`
- `ai-ops-dashboard-prd.md`
- `Built an AI SaaS in 20 min.docx`

### D · Automation blueprints + framework primitives (3 files)
- `REMOTION.docx`
- `automations/AI Content Strategy Generator - Lead Magnet.json`
- `automations/Blueprint - ElevenLabs Agent That Calls & Qualifies Leads.json`

---

## 3 · Defer list (everything moving to BATCH_007 or out-of-scope)

### 3.1 · Deferred to BATCH_007 (operator doctrine + SOPs + working drafts)

| Source surface | Count | Notes |
|---|---:|---|
| `raw/00_BRIEF/` locked doctrine NEW | 11 files + 2 templates | CANONICAL_TRUTHS, THE_SPINE, THE_LINEAGE_DOCTRINE, OPERATING_LOCKS_2026-05-12, THE_OPERATOR_CODED_DEFINITION, LEAN_EXECUTION_AUDIT, MONDAY_COCKPIT, SATURDAY_BUILD_BRIEF, SYSTEM_FINAL_STATUS, OPERATOR_QUESTIONS_2026-05-13, PARTNERSHIP_PROTOCOL, recurring_checklists, templates/monthly_constraint_audit, templates/weekly_review |
| `raw/05_PRODUCTION/` SOPs NEW | 13 files | casting_call_doctrine_v1, ch02_mimi_production_brief_v1, chapter_intake_v1, checklist_post_shoot_same_day, checklist_pre_shoot_day_of, composite_environment_rotation_v1, lightroom_operating_system, preset_library, retoucher_training_notes, SOP_capture_to_delivery, SOP_reset_shoot_day, SOP_strategic_free, track_b_frame_walkthrough |
| `raw/03_OUTREACH/` NEW | 7 files | `SOP_assistant_v3.docx` as canonical (operator decision · use v3 if newer/more complete) · `SOP_assistant.md` deferred legacy unless dedupe proves unique material. Other includes: linkedin_comment_doctrine_v1, SOP_discovery_call, SOP_discovery_to_close, SOP_VIB_production, VIB_caption_library, VIB_figma_spec |
| `raw/06_DELIVERY/` | 11 files | SOP_post_delivery, pixieset_config, 9 email templates |
| `raw/07_CONTENT/` | 7 files | audience_engine, caption_templates, cultural_documentation_thesis, hook_library, linkedin_pov_bank, sniped_content_philosophy (with `legacy-language-sweep-pending` tag for affected chunks), sniped_video_philosophy |
| Commercial / network singletons | 3 files | `01_OFFERS/delivery_architecture_v2.md`, `04_CRM/notion_crm_schemas.md`, `13_NETWORK/access_and_community_architecture.md` |

**BATCH_007 estimated scope:** ~52 files · ~115-130 chunks (per the earlier P2+P3+P4 math).

### 3.2 · Deferred to other batches / mini-batches (not BATCH_006 or BATCH_007)

| Source | Count | Defer reason |
|---|---:|---|
| `raw/00_BRIEF/BRAND_STRATEGY_2026-05-13/` 10 .md files | 10 | Reserved for a focused brand-strategy mini-batch · would dominate B7 with naming-decision text otherwise. |
| `raw/00_BRIEF/ACTIVE_THREADS.md` + `SESSION_LOG.md` + `CURRENT_STATE.md` + `cockpits/2026-W19_May04-May10.md` | 4 | Ephemeral live state · chunking creates immediate staleness. Read at session start instead. |
| `raw/02_CONTRACTS/` 3 legal docs | 3 | "Legal, lowest priority" per existing master notes. Future legal mini-batch. |
| `raw/03_OUTREACH/_sent_dms/` 12 specimens + `_README.md` | 13 | Sent specimens, not doctrine. |
| `raw/03_OUTREACH/_archive_v2_2026-05-07/*.docx` | 2 | Archived superseded versions. |
| `raw/03_OUTREACH/SOP_assistant.md` (440L) | 1 | DEFER LEGACY · supplanted by `SOP_assistant_v3.docx` per operator decision (rev 2). Revisit only if dedupe against v3 proves unique material. |
| `raw/05_PRODUCTION/sniped_operating_system_v1_legacy.md` | 1 | Explicit LEGACY in filename. |
| `raw/05_PRODUCTION/_preset_backups/*.xmp` + `_composite_references/*.png` | 19+ | Binary / visual. |
| `raw/02_TIER_1_CANON_BOOKS/ai_tech/` 12 books | 12 | BATCH_008 AI / tech canon territory. |
| `raw/08_AI_TECH/ai_history_case_studies/AI CHANGED EVERYTHING.docx` | 1 | BATCH_008 territory. |
| `raw/05_AI_EDGE_COURSE/Finding Your Edge.pdf` + `COURSE WORK 1 thru 2.docx` | 2 | BATCH_008 territory. |
| `raw/13_OPERATING_DISCIPLINE/` 3 PDF worksheets (ICP, Goals, Reflections) | 3 | DEFER to a future `EDGE_AND_OPERATING_DISCIPLINE` mini-batch (operator decision · rev 2). Unless clearly text-bearing and directly necessary, hold. Text density unverified · likely sparse PDF form labels. |
| `raw/10_REFERENCE/_intake_2026-05-18/astro claude websites 3x faster.docx` | 1 | sniped-media web codebase territory. |
| `raw/10_REFERENCE/_intake_2026-05-18/youtube skool doc.docx` | 1 | BATCH_008 territory. |
| `raw/10_REFERENCE/_intake_2026-05-18/document.pdf` + `index.html` | 2 | Unlabeled / web codebase. |
| `raw/99_VAULT/_intake_archive_2026-05-07/*` + `_intake_archive_2026-05-12/*` | 17 | Pre-curation source intake archives · most served as raw inputs to B1/B4 chunks. The rest are visual-heavy or low-signal craft tutorials. |
| `raw/08_BOOK/The_Direction_Stack_v_final_2026-05-12.pdf` | 1 | STILL BLOCKED · canonical confirmation pending. |
| `raw/_archive/chapter_cards/CH01_Yae_2026-05-13/*.png` | 5 | Binary PNG outputs. |

---

## 4 · Recommended inclusion set for BATCH_006

### Priority 1 · SNIPED skills (51 files · ~55 chunks)

- 50 `sniped-*/SKILL.md` files · 1 chunk each for the standard 28-50 line skills · 2 chunks each for the 3 longest (`sniped-caption-writer` 162L, `sniped-vib-outreach` 150L, `sniped-luxury-edit` 135L)
- 1 `SKILL_BUILD_QUEUE.md` · 1 chunk (the meta-doc · captures the build prioritization + skill-design discipline)

**Subtotal: 47 single-chunk skills + 3 double-chunk skills + 1 meta-doc chunk = ~54 chunks**

### Priority 2 · 50-skill prompt pack (50 files · ~50 chunks)

- 50 `*/SKILL.md` framework prompts · 1 chunk each (each is a single coherent prompt + workflow + output format)

**Subtotal: 50 chunks**

### Priority 3 · Claude / AI tool workflows (4 files · ~7 chunks)

| File | Est. chunks |
|---|---:|
| `CLAUDE CODE SUPERPOWERS.docx` (48 KB) | 2 |
| `CLAUDE CODE PLUGIN.docx` (32 KB) | 1 |
| `ai-ops-dashboard-prd.md` (20 KB) | 2 |
| `Built an AI SaaS in 20 min.docx` (68 KB) | 2 |
| **Subtotal** | **~7 chunks** |

### Priority 4 · Automation blueprints + framework primitives (3 files · ~3 chunks)

| File | Est. chunks |
|---|---:|
| `REMOTION.docx` (28 KB) | 1 |
| `automations/AI Content Strategy Generator - Lead Magnet.json` | 1 |
| `automations/Blueprint - ElevenLabs Agent That Calls & Qualifies Leads.json` | 1 |
| **Subtotal** | **~3 chunks** |

### Inclusion-set rollup for BATCH_006

| Priority | Files | Estimated chunks |
|---|---:|---:|
| P1 · SNIPED skills (`_skills/`) | 51 | ~54 |
| P2 · 50-skill prompt pack | 50 | ~50 |
| P3 · Claude / AI tool workflows | 4 | ~7 |
| P4 · Automation blueprints + framework primitives | 3 | ~3 |
| **Total** | **108** | **~114** |

**Target landing zone: 100-125 chunks · center estimate ~115.** If extraction yields a denser-than-expected pass (e.g., some 50-skill packs naturally split into 2 chunks), the upper cap is 125. If looser (some short skills merge into thematic clusters), the lower cap is 100. Stay inside the range; do not let it drift past 125.

---

## 5 · Duplicates, stale versions, low-signal flags inside BATCH_006 scope

| Flag | File | Resolution |
|---|---|---|
| Already in BATCH_001-005 | none in BATCH_006 inclusion set | N/A · skill folders + intake-2026-05-18 are net-new surfaces |
| Frontmatter-only vs body | All 100 SKILL.md files | Extract frontmatter (`name`, `description`) into `source_title` + `concept` chunk fields; body becomes `summary` + `usable_principle`. Do NOT chunk the frontmatter as a separate chunk. |
| Description with multi-line YAML | `Claude_AI_Skills_*` 50-pack uses `description: |` blocks | Parse via stdlib YAML to capture multi-line description correctly. |
| JSON blueprints | 2 files | Treat each as 1 chunk · `concept` = blueprint name · `summary` = trigger + node list + key params · `usable_principle` = when to invoke. |

---

## 6 · Estimated chunk yield

**Target: 115 chunks · range 100-125.**

Math (skill-pack-dense, BATCH_006-shape):
- 100 skill-pack chunks (P1 + P2 dominant · ~87% of B6)
- ~7 tool-workflow chunks (P3)
- ~3 automation blueprint chunks (P4)

Sanity check vs prior batches:
- BATCH_005: 161 chunks / 32 sources · 5.0 chunks/source avg
- BATCH_004: 96 chunks / 8 sources · 12 chunks/source avg
- BATCH_003: 103 chunks / 10 books · 10.3 chunks/source
- BATCH_002: 152 chunks / 19 books · 8 chunks/source
- **BATCH_006 projection: ~115 chunks / 108 sources · 1.1 chunks/source avg** · this is the right shape because 100 of the 108 sources are 1-chunk skill packs.

---

## 7 · Extraction method by file type

| File type | Count in inclusion set | Method |
|---|---:|---|
| `.md` (plain markdown with YAML frontmatter) | 100 | Python frontmatter parser (stdlib `yaml` if available, else regex extraction) · pull `name` + `description` into chunk metadata · body becomes the chunk content. |
| `.md` (plain markdown, no frontmatter) | 1 (SKILL_BUILD_QUEUE) + 1 (ai-ops-dashboard-prd) | Direct read · single-pass chunking. |
| `.docx` (Word) | 4 | `pandoc -f docx -t markdown` per file. Same toolchain BATCH_005 used. Save extracted .md alongside in `batch_006_extracted/`. |
| `.json` (automation blueprint) | 2 | Parse as JSON, extract `name`, `description`, node summaries. Treat each blueprint as 1 chunk capturing trigger + workflow + key params. |
| `.pdf` | 0 | None in inclusion set (all PDFs deferred to other batches). |

**Tooling needed:** `pandoc` (already used for BATCH_005), Python stdlib `json` (no new deps). Optional: `PyYAML` for cleaner frontmatter parsing (Python stdlib alternative works via regex if PyYAML is not installed). No OCR. No Whisper. No new package installs.

**Frontmatter handling for skill packs:**
- `sniped-*/SKILL.md`: single-line `description:` followed by markdown body. Extract `description` into the chunk's `concept` field; preserve `name` as `source_title`. The body INVOKE WHEN / MANDATORY READING / OUTPUT / REFUSE sections concatenated into `summary`; the locked invocation rule into `usable_principle`; SNIPED context into `sniped_relevance`.
- `Claude_AI_Skills_50_Upload_Ready (1)/*/SKILL.md`: multi-line `description: |` block. Parse via YAML. Same field mapping otherwise.

---

## 8 · Deliverables

| File | Path | Purpose |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/BATCH_006_CHUNKS.jsonl` | The canonical chunked output · ~115 lines |
| Extracted source tree | `01_KNOWLEDGE_BASE/batches/batch_006_extracted/` | All source content normalized to .md / .txt / .json (mirrors `_skills/`, `claude_ai_skills/`, `intake_2026-05-18/` subfolder names) |
| Extraction script | `scripts/extract_batch_006.py` | Reads inclusion-set manifest · runs pandoc on .docx · copies .md as-is · summarises .json blueprints · writes to `batch_006_extracted/` |
| Chunk writer | `scripts/write_batch_006_chunks.py` | Reads `batch_006_extracted/` · emits BATCH_006_CHUNKS.jsonl with the canonical 12-field schema |
| Summary | `01_KNOWLEDGE_BASE/summaries/BATCH_006_SUMMARY.md` | Narrative summary of what entered the brain and what the skill layer now enables |
| Source index | `01_KNOWLEDGE_BASE/indexes/BATCH_006_SOURCE_INDEX.md` | Per-file chunk-range table |
| Extraction log | `00_COMMAND_CENTER/batch_logs/BATCH_006_EXTRACTION_LOG.md` | Per-file extraction status (success/skip/issue) |
| Completion marker | `00_COMMAND_CENTER/batch_logs/BATCH_006_COMPLETE.md` | Headline numbers + validation summary + next-recommended-action |

Both scripts are NEW · pattern templates: `scripts/extract_batch_005.py` + `scripts/write_batch_005_chunks.py`. Reuse the json-line writer pattern, the pandoc subprocess pattern, the chunk_id pattern (`BATCH_006_001` through `BATCH_006_NNN`).

---

## 9 · Domain enum (operator-approved · rev 2)

Operator approved 4 new domains per rev-2 brief. BATCH_006 reuses existing domains where appropriate (from the post-BATCH_005 53-unique-domain enum) and adds the 4 approved new domains.

**Approved 12-domain enum for BATCH_006:**

| Domain | Status | Source pool | Expected chunks |
|---|---|---|---:|
| `operator-doctrine` | EXISTING (B5) | sniped-canonical-truths skill + selected sniped-* doctrine skills | ~12 |
| `prompt-engineering` | NEW (approved) | 50-skill pack framework prompts (TCREI, premortem, fermi, mom-test, etc.) | ~25 |
| `ai-tooling` | NEW (approved) | Claude Code Superpowers + Claude Code Plugin + ai-ops-dashboard-prd + Built an AI SaaS | ~7 |
| `automation-blueprint` | NEW (approved) | REMOTION + 2 JSON blueprints | ~3 |
| `operator-process` | NEW (approved) | sniped-monday-cockpit + sniped-execution-prioritization + sniped-lean-audit + sniped-assistant-task-routing + SKILL_BUILD_QUEUE meta-doc | ~7 |
| `aesthetics` | EXISTING (B5) | sniped-luxury-edit + sniped-hero-composite-* + sniped-evoto-skin-pass + sniped-higgsfield-pipeline + sniped-seedream-prompt + sniped-lighting-vault + sniped-ai-image-tool-pick | ~10 |
| `production-sop` | EXISTING / extended | sniped-pre-shoot-prep + sniped-shoot-day-reset + sniped-shoot-day-strategic-free + sniped-post-shoot-same-day + sniped-capture-to-delivery + sniped-retoucher-onboarding + sniped-production-os + sniped-pixieset-gallery + sniped-post-delivery + sniped-udemy-lightroom-rails | ~10 |
| `outreach-sop` | EXISTING / extended | sniped-vib-outreach + sniped-caption-writer + sniped-discovery-to-close + sniped-notion-crm-update + cold-email-campaign-architecture + linkedin-growth-lead-generation + mom-test-customer-conversation + consultative-selling-system + tactical-negotiation-ackerman-empathy + negotiation-leverage-black-swan | ~12 |
| `pricing` | EXISTING (B3) | sniped-pricing-decision + sniped-wwp-positioning + sniped-partnership-protocol | ~3 |
| `client-application` | EXISTING (B5) | sniped-discovery-to-close (cross-tag) + sniped-direction-stack + sniped-art-series | ~3 |
| `meta-doctrine` | EXISTING (B4 doctrine-meta extends) | SKILL_BUILD_QUEUE (cross-tag) + framework-orchestrator + signal-noise-forecasting-bayesian + munger-two-track-decision-analysis + bad-strategy-audit + premortem-analysis + cognitive-bias-audit | ~8 |
| `strategy` | EXISTING (B2) | sniped-strategic-implications + sniped-reverse-roadmap + sniped-blockbuster-strategy + sniped-perennial-seller + sniped-leverage-logic + sniped-new-luxury + sniped-company-of-one + sniped-trust-equation + sniped-hit-mechanics + sniped-trust-mechanics + sniped-status-psychology + sniped-hospitality-layer + sniped-ai-sentiment + sniped-ai-photographer-market + sniped-analog-premium + sniped-photo-theory + sniped-art-series + sniped-positioning-phrases + seven-powers-strategic-position-assessment + strategy-kernel-development + counter-positioning-diagnosis + create-destroy-strategy-stress-test + customer-segment-slicing + industry-dynamics-assessment + comparative-advantage-resource-allocation + market-evaluation-scorecard + revenue-growth-diagnostic + business-resilience-audit + lean-transformation-diagnostic + value-stream-improvement-pdca + hoshin-kanri-goal-alignment + shadow-test-pre-launch-validation + success-message-design + pyramid-structured-communication + calm-authority-voice-calibration + copywriting-rule-of-one-awareness-staging + social-media-content-strategy + creative-resistance-turning-pro + second-brain-code-para + freelance-platform-optimization + photography-business-system + professional-portrait-direction + preset-sync-export-photo-editing + business-entity-credit-architecture + economic-incentive-policy-analysis + server-farm-commissioning + epms-site-analysis + meta-business-infrastructure-setup + ai-agent-architecture-wat + ai-code-website-build-pipeline + ai-video-production-pipeline + video-editing-assembly-line + superforecasting-workflow + system-analysis-intervention-design + fermi-estimation | ~14 (cross-tag · most strategic skills will primarily land in `strategy` or `prompt-engineering` with `strategy` as secondary) |

The 4 NEW domains (`prompt-engineering`, `ai-tooling`, `automation-blueprint`, `operator-process`) are scoped to be additive · they extend the master enum, do not replace anything.

**Rounding note:** Sum exceeds 115 because some skill chunks will carry 2 domains via the tag-secondary route (e.g., a strategy framework that also teaches prompt-engineering). Primary-domain count will sum to ~115; tag cross-references add another ~25 secondary domain hits.

---

## 10 · Validation requirements

Per `.claude/skills/jsonl-validation/SKILL.md`, the 6-check gate before chunks become canonical:

| Check | Method |
|---|---|
| JSONL parse | `python3 -c "import json; [json.loads(l) for l in open('BATCH_006_CHUNKS.jsonl')]"` · 0 errors expected |
| Required fields present per line | `chunk_id`, `batch_id`, `source_title`, `source_file`, `author`, `domain`, `concept`, `summary`, `usable_principle`, `sniped_relevance`, `direct_quotes` (may be empty array), `tags` (may be empty array but field present) |
| chunk_id uniqueness | Python set check · 0 duplicates across ~115 chunks. Pattern: `BATCH_006_NNN`. |
| batch_id consistency | Single string value `BATCH_006` across all lines (canonical · matches B5 short-form pattern) |
| source_file resolution | Every `source_file` value must point to a file present under `01_KNOWLEDGE_BASE/batches/batch_006_extracted/` |
| Chunk count + source count | Report final tally; expected ~115 chunks across 108 unique source files |

Halt and surface to operator on any failure. Do not write to master files until all 6 PASS.

---

## 11 · BATCH_007 forward-spec (referenced from this plan · not authorized here)

BATCH_007 takes the deferred content from §3.1: operator doctrine + SOPs + working drafts + outreach + delivery + content + commercial singletons.

**BATCH_007 estimated scope:** ~52 files · ~115-130 chunks.

**BATCH_007 priority tiers (preview · final plan written in a separate BATCH_007_PLAN.md after BATCH_006 is consolidated):**

| Tier | Source surface | Files | Est. chunks |
|---|---|---:|---:|
| P1 · 00_BRIEF locked doctrine NEW | CANONICAL_TRUTHS, THE_SPINE, THE_LINEAGE_DOCTRINE, OPERATING_LOCKS, OPERATOR_CODED_DEFINITION, LEAN_EXECUTION_AUDIT, MONDAY_COCKPIT, SATURDAY_BUILD_BRIEF, SYSTEM_FINAL_STATUS, OPERATOR_QUESTIONS_2026-05-13, PARTNERSHIP_PROTOCOL, recurring_checklists, templates/×2 | 14 | ~36 |
| P2 · 05_PRODUCTION SOPs NEW | 13 production-process docs (casting / chapter intake / composite rotation / lightroom OS / preset library / retoucher training / capture-to-delivery / reset / strategic-free / track B / 2 checklists / ch02 brief) | 13 | ~26 |
| P3 · 03_OUTREACH NEW (excluding SOP_assistant.md legacy) | linkedin_comment_doctrine_v1 + SOP_assistant_v3.docx (canonical) + SOP_discovery_call + SOP_discovery_to_close + SOP_VIB_production + VIB_caption_library + VIB_figma_spec | 7 | ~13 |
| P4 · 06_DELIVERY | SOP_post_delivery + pixieset_config + 9 email templates (consolidated thematically) | 11 | ~7 |
| P5 · 07_CONTENT | sniped_content_philosophy (with legacy-language-sweep tag) + sniped_video_philosophy + audience_engine + caption_templates + cultural_documentation_thesis + hook_library + linkedin_pov_bank | 7 | ~22 |
| P6 · Commercial / network singletons | delivery_architecture_v2 + notion_crm_schemas + access_and_community_architecture | 3 | ~7 |
| **Total** | | **55** | **~111** |

**BATCH_007 written separately after BATCH_006 ships.** Not in scope for this plan.

---

## 12 · Extraction sequence (post-authorization · DO NOT EXECUTE NOW)

1. Operator authorizes BATCH_006 execution.
2. Run `scripts/extract_batch_006.py` to populate `01_KNOWLEDGE_BASE/batches/batch_006_extracted/` with normalized .md / .txt / .json content. Log per-file success/skip/issue in `BATCH_006_EXTRACTION_LOG.md`.
3. Run `scripts/write_batch_006_chunks.py` to emit `BATCH_006_CHUNKS.jsonl`.
4. Run the 6-check validation gate against the JSONL.
5. Write `BATCH_006_SUMMARY.md` + `BATCH_006_SOURCE_INDEX.md`.
6. Write `BATCH_006_COMPLETE.md` completion marker with headline numbers + validation summary + next-recommended-action.
7. STOP. Do not update master files. Operator authorizes `master-consolidation 006` in a separate session.
8. After BATCH_006 consolidation: revise `BATCH_007_PLAN.md` from the §11 forward-spec; execute on operator authorization.

---

## 13 · What this batch enables (post-consolidation)

1. **Every SNIPED skill is retrievable by name and INVOKE-WHEN condition** without re-reading `_skills/sniped-*/SKILL.md`. The operator engine becomes self-describing.
2. **The 50-skill prompt pack is searchable as framework-prompt chunks** · "give me the TCREI prompt-engineering workflow" pulls a single canonical chunk. "premortem analysis for this decision" pulls the premortem skill.
3. **Claude Code productivity + plugin patterns + AI-ops dashboard + rapid-build AI SaaS** ground the operator engine's AI tooling vocabulary without crossing into book-canon territory (BATCH_008's job).
4. **Remotion video automation + 2 JSON workflow blueprints** install the automation-blueprint primitive layer · skills can reference them by name.
5. **The skill layer becomes invokable by an AI agent** without re-reading SKILL.md files for every prompt. Latency + token cost drops.
6. **BATCH_007 inherits a clean foundation** · the skills are chunked and retrievable; the doctrine + SOPs in B7 can reference them by skill name.

---

## 14 · What this plan does NOT do

- No extraction. `batch_006_extracted/` is not created.
- No chunking. `BATCH_006_CHUNKS.jsonl` is not written.
- No master file updates. `MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`, `ACTIVE_KNOWLEDGE_STATE.md` untouched.
- No source moves. `raw/` is read-only this session.
- No commits.
- No new dependencies. `pandoc` and `python3` already used.
- No OCR. No Whisper. No external API calls.

Authorization required before any of the above. Stop here.

---

## 15 · Revision log

- **rev 1 (2026-05-18 earlier):** Single 175-chunk batch covering P1+P2+P3+P4+P5+P6.
- **rev 2 (2026-05-18 now):** Two-pass split applied. BATCH_006 = operator-engine skill layer only (~115 chunks across 108 sources). BATCH_007 forward-spec captures the deferred ~111 chunks across 55 sources. Operator decisions: `SOP_assistant_v3.docx` canonical (legacy `.md` deferred), 13_OPERATING_DISCIPLINE PDFs deferred to future `EDGE_AND_OPERATING_DISCIPLINE` mini-batch, 4 new domains approved (`prompt-engineering`, `ai-tooling`, `automation-blueprint`, `operator-process`).
