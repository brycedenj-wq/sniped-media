# SKILL_REGISTRY.md (2026-06-08)

Complete registry of all **76 skills** on disk. Every skill is registered: ACTIVE (auto-routed when its domain matches), REFERENCE (relevant, loaded on demand only, kept out of auto-injection to avoid context bloat), or EXCLUDED (registered but never auto-routed on production tasks). **0 dead skills, 0 unregistered.**

Conventions (to keep this readable, not a 76x13 wall):
- **Path:** `.claude/skills/<name>/SKILL.md` for all.
- **Trigger phrases / activation conditions:** the `match` array of the skill's domain in `OS_ACTIVATION_INDEX.json` (the router fires on word-boundary match).
- **Required inputs / output type:** defined inside each skill's own SKILL.md.
- Status: ACTIVE / REFERENCE / EXPLICIT (explicit-trigger only) / EXCLUDED. Priority: P1 core, P2 supporting, P3 occasional.

---

## 1. film/video
| skill | status | pri | purpose | gates / standards | reason |
|---|---|---|---|---|---|
| cinema-worldbuilder | ACTIVE | P1 | Seedance motion-prompt director, 5 cinema modes | REAL_FILM_PRODUCTION_OS; diegetic audio | core motion grammar |
| kling-production-sop | ACTIVE | P1 | route + QA-gate an AI motion clip | kling motion QA; credit preflight | gates every clip |
| banana-pro-director | ACTIVE | P1 | image asset builder (base->sheet->plate) | the lock is the look | builds locked refs |
| os-face-lock | ACTIVE | P1 | lock one face across stills/motion | face-lock motion-ready gate | identity continuity |
| os-world-bible | ACTIVE | P1 | lock world rules + continuity | world continuity gate | world consistency |
| os-vision-reject-gate | ACTIVE | P1 | per-frame slop/hands/skin reject | vision reject | catches uncanny |
| watch | ACTIVE | P1 | actually watch the cut (frames+transcript) | /watch pass | Stage 11 |
| sniped-crs-builder | ACTIVE | P2 | character reference system for original chars | face-lock | non-real character lock |
| sniped-direction-stack | REFERENCE | P2 | 5-question shoot calibration | brief gates | pre-production |
| sniped-lighting-vault | REFERENCE | P3 | lighting/posing vault (26 PDFs) | - | lighting lookup |
| sniped-higgsfield-pipeline | REFERENCE | P2 | Higgsfield content-factory orchestration | - | velocity pipeline |
| sniped-seedream-prompt | REFERENCE | P2 | Seedream image prompt builder | - | alt image engine |
| sniped-ai-image-tool-pick | REFERENCE | P2 | route to the right image tool | - | tool selection |
| sniped-status-psychology | REFERENCE | P3 | founder-buyer emotional layer | STORY_GATE | brand-film emotion |
| sniped-hospitality-layer | REFERENCE | P3 | client-experience moments | - | warmth design |
| sniped-hit-mechanics | REFERENCE | P3 | distribution mechanics | - | reach planning |
| composite-master-qa | REFERENCE | P2 | composite physics QA | composite 6-axis | if compositing |
| platform-mastering | REFERENCE | P2 | per-surface export masters | skin-drift | export stage |

## 2. photo/composite
| skill | status | pri | purpose | gates / standards | reason |
|---|---|---|---|---|---|
| sniped-direction-stack | ACTIVE | P1 | shoot calibration / intake | brief | pre-pro |
| model-casting-protocol | ACTIVE | P1 | find/select/communicate/lock models; handle model disputes | release (never-relax); brand-final-wins | casting + talent issues |
| sniped-hero-composite-ceiling | ACTIVE | P1 | full Track B ceiling composite | composite QA | portfolio anchor |
| sniped-hero-composite-lite | ACTIVE | P2 | 45-min lite composite | composite QA | daily IG |
| composite-master-qa | ACTIVE | P1 | composite physics gate | 6-axis + proof crops | believability |
| os-face-lock | ACTIVE | P1 | identity anchor | face-lock | same subject |
| platform-mastering | ACTIVE | P1 | per-surface masters | skin-drift | export |
| sniped-ai-image-tool-pick | ACTIVE | P2 | image tool routing | - | pick engine |
| sniped-seedream-prompt | ACTIVE | P2 | Seedream plate prompt | - | plate gen |
| banana-pro-director | ACTIVE | P2 | Higgsfield image assets | lock | char/plate |
| os-vision-reject-gate | ACTIVE | P1 | reject gate | vision reject | pre-ship |
| sniped-pre-shoot-prep | REFERENCE | P2 | day-of checklist | - | shoot prep |
| sniped-shoot-day-reset | REFERENCE | P2 | paid Reset shoot SOP | - | shoot day |
| sniped-shoot-day-strategic-free | REFERENCE | P2 | free/cultural-doc shoot SOP | - | trade shoot |
| sniped-post-shoot-same-day | REFERENCE | P2 | same-day ingest+backup | - | data safety |
| sniped-capture-to-delivery | REFERENCE | P1 | full RAW->gallery pipeline | - | end-to-end |
| sniped-pixieset-gallery | REFERENCE | P2 | client delivery gallery | - | delivery |
| sniped-crs-builder | REFERENCE | P2 | original character system | - | char lock |
| sniped-photo-theory | REFERENCE | P3 | Berger/Dyer photo theory | - | framing/copy |
| sniped-art-series | REFERENCE | P3 | art-lane direction | - | art lane |
| sniped-lighting-vault | REFERENCE | P3 | lighting vault | - | lighting |

## 3. editing/retouching
| skill | status | pri | purpose | gates / standards | reason |
|---|---|---|---|---|---|
| sniped-luxury-edit | ACTIVE | P1 | locked v3 Lightroom develop | identity-untouched | hero/select develop |
| sniped-evoto-skin-pass | ACTIVE | P1 | locked Evoto skin pass | skin-drift | skin retouch |
| sniped-capture-to-delivery | ACTIVE | P2 | cull+mask+retouch tree | - | pipeline |
| os-vision-reject-gate | ACTIVE | P1 | reject gate | vision reject | pre-ship |
| composite-master-qa | ACTIVE | P2 | composite QA | 6-axis | if composited |
| platform-mastering | ACTIVE | P2 | export masters | skin-drift | export |
| sniped-udemy-lightroom-rails | REFERENCE | P3 | 16 Lightroom rails reference | - | technique lookup |
| sniped-retoucher-onboarding | REFERENCE | P3 | retoucher hire training (Phase B gated) | - | hire only |

## 4. brand/campaign
| skill | status | pri | purpose | gates / standards | reason |
|---|---|---|---|---|---|
| os-world-bible | ACTIVE | P1 | campaign world continuity | continuity | one world |
| sniped-higgsfield-pipeline | ACTIVE | P2 | content factory | - | volume |
| sniped-canonical-truths | ACTIVE | P1 | strategic spine check | no-crown | on-strategy |
| sniped-caption-writer | ACTIVE | P2 | on-voice captions | voice gate | copy |
| platform-mastering | ACTIVE | P2 | per-surface masters | skin-drift | export |
| os-vision-reject-gate | ACTIVE | P1 | reject gate | vision reject | pre-ship |
| brand-validation-machine | REFERENCE | P2 | validate a brand concept go/no-go | proof-first | clothing-brand test |
| sniped-art-series, sniped-hit-mechanics, sniped-blockbuster-strategy, sniped-perennial-seller, sniped-trust-mechanics, sniped-hospitality-layer, sniped-status-psychology | REFERENCE | P3 | brand frames (art, distribution, authority, hospitality, psychology) | - | load per need |

## 5. writing/copy
| skill | status | pri | purpose | gates / standards | reason |
|---|---|---|---|---|---|
| sniped-caption-writer | ACTIVE | P1 | platform captions in voice | voice gate | core copy |
| sniped-positioning-phrases | ACTIVE | P1 | copy through phrase bank + failure modes | positioning gate | on-brand check |
| sniped-status-psychology | ACTIVE | P2 | founder-buyer psychology in copy | - | persuasion |
| sniped-canonical-truths | ACTIVE | P2 | strategy spine for copy | no-crown | on-strategy |
| sniped-trust-mechanics, sniped-photo-theory, sniped-hit-mechanics, sniped-vib-outreach, operator-review | REFERENCE | P3 | authority/theory/outreach frames | - | load per need |

## 6. strategy/business
| skill | status | pri | purpose | gates / standards | reason |
|---|---|---|---|---|---|
| sniped-canonical-truths | ACTIVE | P1 | the 12 locked truths | no-crown | spine |
| sniped-leverage-logic | ACTIVE | P1 | labor/capital/code+media frame | no-crown | hire/tool calls |
| os-command-router | ACTIVE | P1 | classify mode + gates | all gates | routing |
| boardroom | ACTIVE | P2 | multi-expert decision board | proof-before-crowning | pressure a call |
| challenge | ACTIVE | P2 | pressure-test the direction | anti-anchoring | contradiction check |
| operator-review | ACTIVE | P2 | apply OS to an outside situation | proof-first | diagnosis |
| sniped-execution-prioritization | ACTIVE | P2 | prioritize competing items | - | what first |
| sniped-strategic-implications, sniped-reverse-roadmap, sniped-blockbuster-strategy, sniped-company-of-one, sniped-new-luxury, sniped-perennial-seller, sniped-ai-sentiment, sniped-ai-photographer-market, sniped-analog-premium, sniped-lean-audit, sniped-wwp-positioning | REFERENCE | P3 | strategy frames (books/doctrines) | no-crown | load per decision |

## 7. research
| skill | status | pri | purpose | gates / standards | reason |
|---|---|---|---|---|---|
| os-token-safe-reader | ACTIVE | P1 | whole-read large sources | coverage | reading books/PDFs |
| os-command-router | ACTIVE | P2 | classify + web routing | source-freshness | routing |
| deep-research (plugin) | ACTIVE-EXT | P1 | fan-out cited research | cite+date | the research engine (external) |
| sniped-udemy-ai-accelerants, operator-review, watch | REFERENCE | P3 | AI accelerants / diagnosis / video review | - | load per need |

## 8. negotiation/pricing
| skill | status | pri | purpose | gates / standards | reason |
|---|---|---|---|---|---|
| sniped-pricing-decision | ACTIVE | P1 | 3-option price architecture | floor-held | quotes |
| sniped-wwp-positioning | ACTIVE | P1 | Win Without Pitching proclamations | no-crown | positioning |
| sniped-trust-equation | ACTIVE | P2 | Maister trust diagnosis | - | stuck deals |
| sniped-discovery-to-close | ACTIVE | P2 | discovery->proposal->close | - | closing |
| sniped-vib-outreach | ACTIVE | P2 | VIB cold DM draft | voice | outreach |
| sniped-partnership-protocol | ACTIVE | P2 | partnership/collab eval | - | collabs |
| sniped-new-luxury, sniped-status-psychology, sniped-trust-mechanics, operator-review | REFERENCE | P3 | trade-up/psychology/trust frames | - | load per deal |

## 9. web/build
| skill | status | pri | purpose | gates / standards | reason |
|---|---|---|---|---|---|
| (none native) | - | - | served by external plugin skills | completion-verification | intentional: no native SNIPED web skill |
| update-config (plugin), vercel:* (plugin), figma:* (plugin) | REFERENCE-EXT | P2 | settings/deploy/design via plugins | responsive_check | external tooling |

## 10. ops/project management
| skill | status | pri | purpose | gates / standards | reason |
|---|---|---|---|---|---|
| sniped-monday-cockpit | ACTIVE | P2 | weekly cockpit | - | plan the week |
| sniped-notion-crm-update | ACTIVE | P2 | CRM update | schema | log leads/shoots |
| sniped-execution-prioritization | ACTIVE | P2 | prioritization | - | what first |
| sniped-post-delivery | ACTIVE | P2 | post-delivery SOP | - | follow-up |
| sniped-assistant-task-routing | ACTIVE | P3 | delegate to assistant | scope | delegation |
| sniped-production-os | ACTIVE | P2 | folder/naming/structure | - | structure Qs |
| sniped-lean-audit, sniped-hospitality-layer, sniped-retoucher-onboarding, session-save, os-engagement | REFERENCE | P3 | audits/hire/state/ingest | - | load per need |

## 11. QA/proofing
| skill | status | pri | purpose | gates / standards | reason |
|---|---|---|---|---|---|
| os-quality-gates | ACTIVE | P1 | the 11 OS gates | all | completion check |
| os-vision-reject-gate | ACTIVE | P1 | per-frame reject | vision reject | visual QA |
| composite-master-qa | ACTIVE | P1 | composite QA | 6-axis | believability |
| watch | ACTIVE | P1 | watch the cut | /watch | film QA |
| challenge | ACTIVE | P2 | red-team the direction | anti-anchoring | pressure-test |
| os-command-router, platform-mastering | REFERENCE | P2 | routing / export QA | - | load per need |
| emergency-drop-protocol | ACTIVE (cross-cutting) | P1 | time-boxed production mode; scope-cut not quality-cut; relax-vs-never gates; honest label; send/no-send | never-relax: identity/legal/vision-reject/brand-core/honest-label | auto-promoted on emergency triggers in ANY production domain |

## 12. utility/support
| skill | status | pri | purpose | gates / standards | reason |
|---|---|---|---|---|---|
| save | ACTIVE | P1 | persist a fact to memory | - | memory write |
| os-token-safe-reader | ACTIVE | P2 | whole-read large files | coverage | big reads |
| os-command-router | ACTIVE | P2 | classify any request | gates | routing |
| skill-template | REFERENCE | P3 | template for new skills | activation contract | building skills |
| session-save | EXCLUDED | P2 | snapshot session state | - | explicit-trigger; corpus/state op |
| os-engagement | EXCLUDED | P2 | corpus ingestion protocol | coverage | explicit-trigger |
| batch-extraction | EXCLUDED | P1 | corpus batch extraction | jsonl-validation | explicit-trigger (BATCH_NNN) |
| jsonl-validation | EXCLUDED | P1 | validate chunk JSONL | schema | explicit-trigger |
| master-consolidation | EXCLUDED | P1 | consolidate master index | - | explicit-trigger |
| source-inventory | EXCLUDED | P2 | inventory a source folder | count-first | explicit-trigger |
| staging-plan | EXCLUDED | P2 | staging plan for raw/ | - | explicit-trigger |

---

## Coverage summary
- Total skills on disk: **78** (added emergency-drop-protocol, model-casting-protocol 2026-06-08)
- ACTIVE (auto-route on domain match): **45**
- REFERENCE (load on demand): **33**
- INTENTIONALLY EXCLUDED from production routing: **8** (corpus/maintenance: batch-extraction, jsonl-validation, master-consolidation, source-inventory, staging-plan, os-engagement, session-save, skill-template)
- UNREGISTERED / DEAD: **0**
- DEPRECATED: 0 · MISSING-DEPENDENCY: 0

## Intentional exclusions (why omitted from auto-routing)
These are registered and runnable, but never auto-fire on creative/production tasks because they are corpus or session-maintenance operations that would only add noise: batch-extraction, jsonl-validation, master-consolidation, source-inventory, staging-plan, os-engagement, session-save, skill-template. Invoke them explicitly by name when doing corpus or OS-maintenance work.

## Routing gaps - status
- **Model casting:** CLOSED. `model-casting-protocol` built + active in photo_composite (triggers cover casting requests AND model disputes about usage/edits/flaking).
- **Emergency drop:** CLOSED. `emergency-drop-protocol` built; auto-promoted by `emergency_triggers` in the router, so it fires in any production domain under time pressure.
- **Web/build:** open by design; no native SNIPED skill, served by external vercel/figma plugins (intentional exclusion).
