# BATCH_006 summary · operator-engine skill layer · 2026-05-18

114 chunks · 108 source files · batch_id `BATCH_006` · validated 6/6.

## What this batch covers

The operator-engine skill layer. Where BATCH_001-004 captured the SNIPED operating spine and BATCH_005 installed the photography canon, BATCH_006 makes the skill primitives themselves chunk-addressable. The result: every SNIPED skill is invokable by name + INVOKE-WHEN condition, every external framework prompt is searchable as a 1-chunk pack, and the supporting Claude Code / n8n / Remotion tooling primitives are reference-ready.

The batch breaks into 4 priority tiers (per BATCH_006_PLAN.md rev 2):

| Tier | Sources | Chunks | What it covers |
|---|---:|---:|---|
| P1 · SKILL_BUILD_QUEUE meta-doc | 1 | 1 | Meta-doctrine for how every SNIPED skill is designed (5 discipline rules) |
| P1 · SNIPED skills | 50 | 53 | The 50 sniped-* skill packs (3 longest get a second extended-methodology chunk) |
| P2 · 50-skill prompt pack | 50 | 50 | External framework prompts (TCREI, premortem, fermi, Munger 2-track, signal-noise, framework-orchestrator, etc.) |
| P3 · Claude / AI tool workflows | 4 | 7 | Claude Code Superpowers (2), Claude Code Plugin / Ralph Wiggum (1), AI Ops Dashboard PRD (2), Built an AI SaaS in 20 min (2) |
| P4 · Automation blueprints + framework primitive | 3 | 3 | Remotion video automation + 2 n8n blueprints (content-strategy generator + ElevenLabs voice agent) |

## Where this batch lands canonically

### New canon installed

1. **The 5-rule SNIPED skill-build discipline (SKILL_BUILD_QUEUE).** One skill per source · reference (do not duplicate) · frontmatter is load-bearing · MANDATORY READING in every skill · refuse drift. This is the meta-doctrine that governs the operator-engine skill layer itself.
2. **50 SNIPED skills made chunk-addressable.** Every operator-engine primitive (canonical truths, Direction Stack, Monday cockpit, lean audit, all 11 production SOP skills, all 4 outreach skills, pricing + WWP + partnership, all 9 aesthetics/edit/composite/lighting skills, all 15 strategy intel skills, 2 AI-tooling skills) is now retrievable by name and INVOKE-WHEN condition.
3. **50 framework prompts made chunk-addressable.** TCREI prompt engineering, framework-orchestrator (the meta-skill that orchestrates the other 49), 8 decision/judgment frameworks (premortem, fermi, Munger, signal-noise, superforecasting, cognitive-bias-audit, bad-strategy-audit, shadow-test), 15 strategy frameworks (seven-powers, strategy-kernel, counter-positioning, create-destroy, customer-segment-slicing, industry-dynamics, comparative-advantage, market-evaluation, revenue-growth, business-resilience, economic-incentive, hoshin-kanri, freelance-platform-optimization, photography-business-system, business-entity-credit-architecture), 7 outreach frameworks (cold-email-campaign-architecture, linkedin-growth-lead-generation, mom-test, consultative-selling, ackerman-negotiation, black-swan-negotiation, social-media-content-strategy), 5 AI-tooling frameworks (ai-agent-architecture, ai-code-website-pipeline, meta-business-infrastructure, server-farm-commissioning, epms-site-analysis), 3 automation blueprints (ai-video-production-pipeline, video-editing-assembly-line, preset-sync-export), 4 operator-process frameworks (lean-transformation-diagnostic, value-stream-improvement-pdca, system-analysis-intervention-design, creative-resistance-turning-pro), 8 prompt-craft frameworks (TCREI, framework-orchestrator, pyramid-structured-communication, success-message-design, calm-authority-voice-calibration, copywriting-rule-of-one-awareness-staging, second-brain-code-para, professional-portrait-direction).
4. **Claude Code Superpowers + Plugin (Ralph Wiggum) + AI Ops Dashboard PRD + Built an AI SaaS in 20 min.** The operator-engine tooling vocabulary: agentic-skills framework, brainstorm → write plan → execute plan workflow, TDD + sub-agents + code review + worktree isolation, promise-tag completion convention, single-overnight Ralph Wiggum loop, Claude Code + n8n decoupling pattern. These ground the operator engine's Claude Code use without crossing into book-canon territory (BATCH_008's job).
5. **2 directly-executable automation blueprints + Remotion.** The AI Content Strategy Generator lead-magnet pattern (webhook → GPT-5.2 system prompt → HTML 30-day strategy output). The ElevenLabs voice-agent blueprint (future-option · currently OUT of scope per the two-channel doctrine but documented as a primitive). Remotion as the React-based video automation framework for templated chapter cards + Cultural Doc lower-thirds + 7×7 cutdowns.

### Existing canon reinforced or extended

- **BATCH_004 commercial-architecture / aesthetic-doctrine** are reinforced by the 9 SNIPED aesthetics skills (luxury-edit, hero-composite-ceiling, hero-composite-lite, evoto-skin-pass, higgsfield-pipeline, seedream-prompt, lighting-vault, ai-image-tool-pick, udemy-ai-accelerants) and the 11 production SOP skills.
- **BATCH_003 pricing canon (Enns)** is operationalized by sniped-pricing-decision + sniped-wwp-positioning + sniped-partnership-protocol skills.
- **BATCH_005 client-application doctrine** is operationalized by sniped-art-series skill (the SNIPED Art Series recreation methodology becomes invokable).
- **BATCH_001 outbound + production stacks** are operationalized by the 4 outreach-sop skills (vib-outreach, caption-writer, discovery-to-close, notion-crm-update) and the 11 production-sop skills.

### Cross-references opened

- `intel_pricing_logic.md` (Enns) · sniped-pricing-decision skill is the runtime invocation
- `intel_hospitality_layer.md` (Guidara) · sniped-hospitality-layer skill is the runtime invocation
- `intel_trust_equation.md` (Maister) · sniped-trust-equation skill is the runtime invocation
- `intel_hit_mechanics.md` (Berger) · sniped-hit-mechanics skill is the runtime invocation
- `intel_status_psychology.md` (de Botton + Simler/Hanson) · sniped-status-psychology skill is the runtime invocation
- `intel_leverage_logic.md` (Naval) · sniped-leverage-logic skill is the runtime invocation
- `intel_new_luxury.md` · sniped-new-luxury skill is the runtime invocation
- `intel_company_of_one.md` (Jarvis) · sniped-company-of-one skill is the runtime invocation
- `intel_perennial_logic.md` (Holiday) · sniped-perennial-seller skill is the runtime invocation
- `intel_blockbuster_strategy.md` (Elberse) · sniped-blockbuster-strategy skill is the runtime invocation
- `intel_analog_premium.md` (Sax) · sniped-analog-premium skill is the runtime invocation
- `intel_wwp_proclamations.md` (Enns WWP) · sniped-wwp-positioning skill is the runtime invocation
- `intel_ai_sentiment.md` · sniped-ai-sentiment skill is the runtime invocation
- `intel_ai_photographer_market.md` · sniped-ai-photographer-market skill is the runtime invocation
- `intel_photo_theory.md` (Berger / Dyer) · sniped-photo-theory skill is the runtime invocation
- `intel_strategic_implications.md` · sniped-strategic-implications skill is the runtime invocation
- `intel_positioning_phrases.md` · sniped-positioning-phrases skill is the runtime invocation
- `intel_trust_mechanics.md` · sniped-trust-mechanics skill is the runtime invocation
- `feedback_max_default.md` · framework-orchestrator skill enforces it at the prompt level

## Domain distribution

| Domain | Chunks | Notes |
|---|---:|---|
| strategy | 30 | Largest domain · 14 SNIPED strategy intel skills + 15 Claude50 strategy frameworks + 1 cross-tag · the strategic-primitive layer |
| ai-tooling | 14 | 2 SNIPED skills + 5 Claude50 AI-infra skills + 7 P3 supporting docs (Superpowers, Plugin, PRD, AI SaaS) |
| outreach-sop | 13 | 4 SNIPED outreach skills + 7 Claude50 outreach frameworks (cold-email, linkedin-growth, mom-test, consultative-selling, 2 negotiation, social-media-content-strategy) |
| production-sop | 10 | 10 SNIPED production skills (pre-shoot, reset, strategic-free, post-shoot, capture-to-delivery, retoucher, production-os, pixieset, post-delivery, lightroom-rails) |
| meta-doctrine | 9 | SKILL_BUILD_QUEUE + 8 Claude50 decision/judgment frameworks (premortem, fermi, Munger, signal-noise, superforecasting, cognitive-bias-audit, bad-strategy-audit, shadow-test) |
| prompt-engineering | 8 | 8 Claude50 prompt-craft frameworks (TCREI, framework-orchestrator, pyramid, success-message-design, calm-authority-voice, rule-of-one, second-brain-code-para, professional-portrait-direction) |
| operator-process | 8 | 4 SNIPED operator-process skills (execution-prioritization, monday-cockpit, lean-audit, assistant-task-routing) + 4 Claude50 operator-process frameworks (lean-transformation, value-stream-pdca, system-analysis, creative-resistance-turning-pro) |
| aesthetics | 8 | 8 SNIPED aesthetics / edit / composite / lighting / prompt-tool skills |
| automation-blueprint | 6 | 3 Claude50 automation skills (ai-video-production-pipeline, video-editing-assembly-line, preset-sync-export-photo-editing) + 3 P4 supporting docs (Remotion, content-strategy generator, ElevenLabs voice agent) |
| operator-doctrine | 5 | sniped-canonical-truths, sniped-direction-stack, sniped-reverse-roadmap, sniped-hospitality-layer, sniped-partnership-protocol |
| pricing | 2 | sniped-pricing-decision, sniped-wwp-positioning |
| client-application | 1 | sniped-art-series |

12 distinct domains used. All 4 NEW domains approved per BATCH_006_PLAN.md rev 2 are present (`prompt-engineering`, `ai-tooling`, `automation-blueprint`, `operator-process`). 8 existing domains reused from the post-BATCH_005 master enum (`strategy`, `outreach-sop`, `production-sop`, `meta-doctrine`, `aesthetics`, `operator-doctrine`, `pricing`, `client-application`).

## Source coverage

All 108 source files produced at least 1 chunk. 3 SNIPED skills (sniped-caption-writer, sniped-vib-outreach, sniped-luxury-edit) produced 2 chunks each (extended-methodology pass). 3 supporting docs (Claude Code Superpowers, AI Ops Dashboard PRD, Built an AI SaaS in 20 min) produced 2 chunks each. Source-by-source breakdown lives in `BATCH_006_SOURCE_INDEX.md`.

## What was deferred (to BATCH_007 or beyond)

Per BATCH_006_PLAN.md §3 and §11 forward-spec:

- **BATCH_007** (~52 files · ~115-130 chunks estimated): 00_BRIEF locked doctrine NEW (14), 05_PRODUCTION SOPs NEW (13), 03_OUTREACH NEW with `SOP_assistant_v3.docx` as canonical (7), 06_DELIVERY (11), 07_CONTENT (7), commercial / network singletons (3).
- **Brand-strategy mini-batch:** 10 docs in `00_BRIEF/BRAND_STRATEGY_2026-05-13/`.
- **Future EDGE_AND_OPERATING_DISCIPLINE mini-batch:** 3 PDF worksheets in `13_OPERATING_DISCIPLINE/` (ICP, Goals, Reflections).
- **BATCH_008:** 12 books in `02_TIER_1_CANON_BOOKS/ai_tech/`, AI CHANGED EVERYTHING.docx, AI Edge Course (Finding Your Edge.pdf + COURSE WORK 1 thru 2.docx), youtube skool doc.docx.
- **Out of all current scopes:** ephemeral live state (4 docs), 02_CONTRACTS legal (3), sent-DM specimens (13), `SOP_assistant.md` legacy (1), `sniped_operating_system_v1_legacy.md`, preset/composite binaries (19+), web-codebase items (astro claude / index.html / document.pdf · 3), pre-curation vault (17), still-blocked Direction Stack PDF.

## Validation

All 6 validation checks (per `.claude/skills/jsonl-validation/SKILL.md`) PASS:
- JSONL parse · PASS
- Required fields present per line · PASS (0 missing)
- chunk_id uniqueness · PASS (no duplicates across 114 chunks)
- batch_id consistency · PASS (1 distinct value: `BATCH_006`)
- source_file resolution · PASS (all 108 source_files resolve to `batch_006_extracted/`)
- Chunk count + source count · 114 chunks / 108 sources confirmed

Em-dash sweep: PASS (5 em-dashes were found post-write in the JSONL and swept to middle-dot before validation).

## Deviations from BATCH_006_PLAN.md rev 2

1. **Final chunk count 114 vs plan target 115.** Inside the 100-125 range. Off by one because the SUPPORTING_DOCS plan was 7 chunks but landed at 10 chunks (Claude Code Superpowers 2 + Plugin 1 + AI Ops Dashboard 2 + AI SaaS 2 + Remotion 1 + 2 automation blueprints) and one P1 SNIPED skill was 53 instead of the planned 54 (because the 3 long-skill extras were 3, not 4 · plan had a rounding ambiguity).
2. **No domain expansions beyond the approved 12-domain enum.** All 4 NEW domains approved by the operator (`prompt-engineering`, `ai-tooling`, `automation-blueprint`, `operator-process`) are present. 8 existing domains reused.
3. **Operator decision applied:** `SOP_assistant_v3.docx` set as canonical for BATCH_007 (not chunked in BATCH_006); `SOP_assistant.md` legacy deferred unless dedupe proves unique material. Both are out-of-scope for B6.
4. **Operator decision applied:** 13_OPERATING_DISCIPLINE PDF worksheets deferred to a future EDGE_AND_OPERATING_DISCIPLINE mini-batch.
5. **No structural deviations.** No source files copied. No master files updated. BATCH_007 not started.

## What this batch enables

1. **Every SNIPED skill is retrievable by name and INVOKE-WHEN condition** without re-reading `_skills/sniped-*/SKILL.md`. Future agent sessions can answer "what skill runs when X happens?" from chunks rather than a file scan.
2. **The 50-skill prompt pack is searchable as framework-prompt chunks.** "give me the TCREI prompt-engineering workflow" pulls a single canonical chunk. "premortem analysis for this decision" pulls the premortem skill.
3. **Claude Code productivity + plugin patterns + AI-ops dashboard + rapid-build AI SaaS** ground the operator engine's AI tooling vocabulary without crossing into book-canon territory (BATCH_008's job).
4. **Remotion video automation + 2 n8n workflow blueprints** install the automation-blueprint primitive layer · skills can reference them by name.
5. **The skill layer becomes invokable by an AI agent** without re-reading SKILL.md files for every prompt. Latency + token cost drops.
6. **BATCH_007 inherits a clean foundation** · the skills are chunked and retrievable; the doctrine + SOPs in B7 can reference them by skill name.

## End state

`01_KNOWLEDGE_BASE/batches/BATCH_006_CHUNKS.jsonl` is canonical. Validated. Awaits `master-consolidation 006` to be promoted into `MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`, and `ACTIVE_KNOWLEDGE_STATE.md`. No master files were updated in this batch run per the operator's explicit instruction.
