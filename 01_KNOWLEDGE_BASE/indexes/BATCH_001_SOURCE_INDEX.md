# BATCH_001 · Source Index

Per-source coverage map for `BATCH_001_CHUNKS.jsonl`. Each row shows what was processed, how, and what was skipped or deferred.

Status legend:
- **FULL** = entire file read; chunks reflect comprehensive coverage
- **SAMPLED** = head/middle portions read; chunks cover sampled material; tail content deferred
- **DEFERRED** = placeholder chunk only; full extraction belongs in BATCH_002+
- **SKIPPED-DUPLICATE** = identified as canonical-duplicate via DUPLICATE_REVIEW.md; not processed

## The processed 25 (post-dedupe)

| # | Source path (relative to ~/AI-Brain-Refinery/raw/) | Type | Status | Chunks | Notes |
|--:|-----|------|--------|------:|-------|
| 1 | `99_VAULT/_intake_archive_2026-05-07/AI PHOTOGRAPHERS.docx` | docx | SAMPLED (head only) | 1 | YouTube transcript on AI portrait skin texture across Midjourney/Imagen/Reve/Flux. Full extraction in BATCH_002 if tactical AI workflow detail needed. |
| 2 | `chat Sniped MAster thread.docx` | docx | DEFERRED | 1 | 407 KB conversational ChatGPT thread. Placeholder chunk only. Sampling strategy noted. |
| 3 | `sniped figma.docx` | docx | SAMPLED (head only) | 1 | Tutorial transcript on Claude vs Codex vs Figma vs Google Stitch design workflow. |
| 4 | `Gemini Sniped MAster thread.docx` | docx | DEFERRED | 1 | 237 KB conversational Gemini thread. Placeholder chunk only. |
| 5 | `10_REFERENCE/lighting_pdfs/PHOTOGRAPHY MASTERCLASS.docx` | docx | SAMPLED (head only) | 1 | Udemy lighting course transcript. Foundational "seeing the light" content extracted; remaining technique-specific sections deferred. |
| 6 | `10_REFERENCE/STRATEGIC_PRINCIPLES.md` | md | SAMPLED (Sections 1-4 of 9) | 5 | Trust Equation, Hit Makers, Status Anxiety, Win Without Pitching, Pricing Creativity. Sections 5-9 (cross-source synthesis, decision-support routing, memory candidates) deferred. |
| 7 | `00_BRIEF/SNIPED_OS_V1_SYNTHESIS_2026-05-12.md` | md | SAMPLED (Sections 0-5 of unknown total) | 4 | 7-signature recognizability test, 10 aesthetic traps, composite environment rotation, hybrid AI stance. |
| 8 | `SNIPED_OS_OPERATING_BRIEF.md` | md | FULL | 9 | The spine document. Comprehensive coverage. |
| 9 | `The_Platform_Stack.docx` | docx | SAMPLED (Parts I-VI of XIII) | 4 | LinkedIn-as-business-community, profile storefront, content formats, hooks. Meta architecture (Parts VII-XIII) deferred. |
| 10 | `00_BRIEF/100Q_AUDIT_OPTIMIZATIONS_2026-05-13.md` | md | SAMPLED (Sections 1-7 of unknown total) | 4 | "Broke" vs runway reframe, time/cadence locks, pre-audience distribution, methodology disclosure on artifact. Remaining Q53+ deferred. |
| 11 | `The_Offer_Stack.docx` | docx | SAMPLED (Parts I-VII of XIII) | 5 | Three operating principles, 3 questions + 4 validation methods, 6-rung offer ladder, 5-question brand identity, AI services. Parts VIII-XIII (platform selection, launch mechanics, scaling, growth levels, operator sequence) deferred. |
| 12 | `The_Revenue_Stack.docx` | docx | FULL | 6 | Comprehensive coverage of all 12 parts. |
| 13 | `The_Attention_Stack.docx` | docx | FULL | 8 | Comprehensive coverage of all 12 parts + appendices. |
| 14 | `The_Production_Stack.docx` | docx | FULL | 5 | Six-layer stack + 7 working rules + moodboard + lighting setups + posing. |
| 15 | `00_BRIEF/PRODUCTION_OS.md` | md | FULL | 6 | Folder structure, naming, storage, photo pipeline, AI tool routing, content pipeline, delegation matrix. |
| 16 | `The_Outbound_Stack.docx` | docx | FULL | 7 | Sending architecture, ICP Waterfall, 3-email sequence, Workshop Funnel + Value-First Boomerang, AI personalization, Mom Test, benchmarks. |
| 17 | `00_BRIEF/EXECUTION_PRIORITIZATION.md` | md | FULL | 6 | What game am I playing, MVE, gating checklist, overcomplicating/overbuilding/underestimating audit, uncomfortable necessary actions, weekly time allocation. |
| 18 | `The_Copywriting_Stack.docx` | docx | FULL | 6 | Rule of One, 5 Stages of Awareness, Headline Formula + PAS, Sticky Research/VoC, Halbert process, Five Offers + features-to-benefits. |
| 19 | `00_BRIEF/REVERSE_ROADMAP.md` | md | FULL | 6 | Year-10 destination, dependency chain, 10 irreversible mistakes, attractive shortcuts, what compounds quietly, clarifying decision question. |
| 20 | `00_BRIEF/OPERATIONAL_BACKBONE.md` | md | FULL | 4 | 6 backbone loops, un-delegate-ables, 8 drift symptoms, condensation discipline. |
| 21 | `Study_AnnieLeibovitz.md` | md | FULL | 2 | Concept-first signature + 6 pillars; Leibovitz vs SNIPED borrowable + traps. |
| 22 | `05_PRODUCTION/chapter_rollout_doctrine_v1.md` | md | FULL | 5 | Universal chapter formula, caption convention, B&W Card dual-register rule, breath-day cadence, frame-earns-cover decision framework. |
| 23 | `The_Adobe_Stack_Manual.docx` | docx | FULL | 4 | Stack connections, Firefly prompt formula, Frame.io benchmarks, Adobe Express brand kit. |
| 24 | `03_OUTREACH/cold_email_doctrine_v1.md` | md | FULL | 3 | Loom audit front-end, SNIPED domain performance + voice rules, two-channel architecture. |
| 25 | `Study_ErnstHaas.md` | md | FULL | 2 | Color-as-music + abstraction signature; Haas vs SNIPED 3 borrowable moves. |

## Skipped duplicates (per DUPLICATE_REVIEW.md)

| Path | Reason | Canonical kept |
|------|--------|----------------|
| `99_VAULT/_intake_archive_2026-05-07/PHOTOGRAPHY MASTERCLASS.docx` | byte-identical to canonical (md5 `f20d0e8e0079...`) | `10_REFERENCE/lighting_pdfs/PHOTOGRAPHY MASTERCLASS.docx` |

This was the only duplicate that overlapped with the original best-first 25. The dedupe replaced it with `Study_ErnstHaas.md` (next pri=1 file by inventory weight).

## Files referenced widely but NOT in the BATCH_001 set

Surfaced as worth pulling into BATCH_002:

- `Aesthetic_Statement_v1.docx` (10 KB · root) — referenced across nearly every doc as the locked aesthetic source. Not in best-first 25 because the inventory script weighted by size + explicit-high pattern; this file is small but load-bearing.
- `08_BOOK/The_Direction_Stack_v_final_2026-05-12.pdf` (444 MB) — the methodology IP itself. Held back pending duplicate confirmation (see `DUPLICATE_REVIEW.md` NEEDS_USER_CONFIRMATION section) and PDF extraction tooling decision.
- `09_ART_SERIES/` — folder shown empty in inventory; 9 root-level `Art_Series_*.md` files contain Bryce's interpretation of canon photographers.
- `04_CRM/notion_crm_schemas.md` — referenced repeatedly across operational docs; unread in BATCH_001.
- `02_CONTRACTS/` files (Collab Agreement, Reset MSA, Op Kit MSA) — referenced in operational chunks; unread.
- `06_DELIVERY/pixieset_config.md`, `SOP_post_delivery.md`, `email_templates/*.md` — referenced extensively in PRODUCTION_OS chunks; unread.

## Dedupe decisions still pending

Per `indexes/skip_duplicates.json`:

```
NEEDS_USER_CONFIRMATION:
  - 08_BOOK/The_Direction_Stack_v_final_2026-05-12.pdf (candidate canonical)
  - The Direction Stack_Final.pdf (candidate skip)
  - Reason: same byte size but not md5-verified at scan time
  - Path/version convention favors 08_BOOK version
```

Resolution before any BATCH that touches the book PDF.

## Redaction notes

Per the user's extraction rule "Redact secrets/API keys/tokens/passwords/private credentials":
- **No redactions performed in this batch.** None of the 25 source files contained API keys, tokens, passwords, or private credentials in the sampled material.
- Email addresses in the corpus belong to BJ's domain infrastructure (`admin@snipedmedia.com`, `trysnipedmedia.com`, `snipedstudio.com`, `brycedenphoto.com`, `snipedproduction.com`, `snipedvisuals.com`) and are operationally meaningful (one is explicitly KILLED FROM COLD use). They are kept as-is per the operating logic that they exist in user's own SNIPED_OS public-facing infrastructure context.
- Personal names mentioned (Pearl, Larry Bernard, Rejuar, Bishop Peters, Tracy at Davis Law, Ramon, Miho, Hermine, Yae, Mimi, Jamie, Don) are operational network nodes the user has explicitly named in their own docs as part of business infrastructure. Kept as-is.

## Chunk ID range

`batch-001-chunk-001` through `batch-001-chunk-106`. Sequential, no gaps.

## Tag taxonomy used (full set)

Tags applied across the batch:
`positioning, identity, sniped, operator-coded, pricing, offer-ladder, reset, operator-kit, brand-system, outreach, vib, linkedin, direction-stack, sales-asset, methodology, ip, authority-asset, operations, stack, tooling, backend, offer-design, free-work, collab, community, access, aesthetics, visual-register, filter, strategy, three-engines, sniped-canon, canon, 12-truths, mindset, game-theory, wrong-game, metrics, mve, priorities, backbone-loops, gating, scaling, discipline, drift-detection, execution, action-bias, avoidance, time-budget, cadence, field-engineer, year-10, vision, destination-state, dependency-chain, milestones, timeline, irreversible, mistakes, shortcuts, refusals, compounding, long-game, decision-filter, clarifying-question, ai-tools, adobe, firefly, workflow, prompt-engineering, image-generation, frame-io, creative-review, benchmarks, adobe-express, brand-kit, templates, content-strategy, seven-laws, attention-economy, distribution, pac-framework, platforms, algorithms, validation-loop, organic-paid, r-and-d, 7x7-workflow, content-split, ai-cutdowns, hooks, copywriting, conversion, platform-arbitrage, attention, monetization, pebble-to-boulder, niche, sequencing, 9pm-window, maybe-filter, cynicism, rule-of-one, fundamentals, awareness-stages, schwartz, funnel, headline, pas-formula, structure, research, voc, sticky-research, halbert, writing-process, drafting, five-offers, benefits, features, cold-email, infrastructure, deliverability, icp, triggers, segmentation, sequences, email-architecture, workshop-funnel, value-first, boomerang, personalization, ai-usage, uncanny-valley, mom-test, discovery, fitzpatrick, troubleshooting, loom-audit, front-end-offer, domain-performance, voice-rules, two-channel, cannibalization, chapter-rollout, ig-cadence, captions, convention, b-w-cards, dual-register, breath-day, card-selection, bans, folder-structure, production, naming, storage, backup, pipeline, timing, editing, camp-b, routing, content-pipeline, outputs, bts, delegation, hiring, retoucher, weekly-rhythm, sacred, forever-bj, correctives, weekly-audit, condensation, tiers, maintenance, photography-business, 60-day-test, specialization, tier-anchor, rules, photography-pricing, finance, wage-separation, wealth-levels, cash-reserve, growth-levers, clv-cpa-cr, scaling-paths, premium, authority-pivot, six-layers, pre-production, working-rules, moodboard, alignment, brief, lighting, setups, modifiers, posing, seven-points, defaults, trust-equation, maister, hit-makers, thompson, status-anxiety, de-botton, premium-pricing, wwp, enns, proclamations, three-options, insurance, recognizability, hero-standard, traps, drift, cross-medium, composite, environments, ai-stance, hybrid, track-b, leibovitz, study, concept-first, borrows, haas, color, three-rules, validation, forms, third-layer, ladder, 6-rungs, brand, 5-questions, ai-services, outcomes, lego-brick, platform-setup, meta, four-buckets, commitment, profile, storefront, formats, reframe, runway, phase-b-trigger, time-lock, pre-audience, methodology-disclosure, ai-defense, sniped-moat, midjourney, skin-texture, design-workflow, figma, claude-codex, craft, meta (deferred-marker), deferred, chat-thread, batch-002`
