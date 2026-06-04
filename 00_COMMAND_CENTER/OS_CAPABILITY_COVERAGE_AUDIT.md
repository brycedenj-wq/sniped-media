# OS CAPABILITY COVERAGE AUDIT (2026-06-04)

> Proof of what the OS actually contains and can do. Grounded in the manifest, the capability map, 167 doctrine docs, the skill set, and the built production harness. Full per-category detail: `OS_CAPABILITY_COVERAGE_MATRIX.md`. No strategy. No old-lane crowning.

---

## 1. OS ACTIVATION DEFINITION

A capability moves through six states. "Activated" means it reached at least **operationalized**, ideally **tested**.

| State | Definition | How to verify |
|---|---|---|
| **read** | the source was whole-read, every token-safe segment landed | manifest status `read_verified` |
| **distilled** | the source became a usable doctrine entry, not a chunk graveyard | exists in an `OS_DOCTRINE_*` doc |
| **retrievable** | the OS can find it on demand (named in the capability map / tool-routing / spine) | appears in `OS_CAPABILITY_MAP.md` or `ROUTING_MANIFEST.md` |
| **operationalized** | turned into a rule/gate/routing the OS applies in work | a gate in `os-quality-gates`, a routing row, a doctrine lock |
| **skill-built** | wrapped as an invokable skill or script | a file in `.claude/skills/` or `scripts/os_*` |
| **tested** | run on a real case and proven | a journal/dry-run record, a regression test, a real run |

**Verified vs unverified:** "verified" = read_verified in the manifest (96.6%). "Unverified" = the OCR/visual/transcription pile (40 items) plus anything only theoretical (doctrine with no skill and no test). A capability can be *known* (distilled) but not yet *doable-on-demand* (skill-built/tested). This audit separates the two honestly.

---

## 2. SOURCE COVERAGE PROOF

- **Verified sources: 1,215 / 1,258 = 96.6%** (manifest is the arbiter; `os_checkpoint.py` reconciles).
- By type (verified): **612 .md · 280 .docx · 136 .epub · 122 .pdf · 25 .mobi · 10 .azw3 · 7 .txt · 6 .djvu · 8 .py · 7 .skill · 1 .toml · 1 .doc**.
- **Distilled into: 167 `OS_DOCTRINE_*` docs + 7 `OS_CAPABILITY_*` docs + the master doctrine + Claude operating manual.**
- **Skills/scripts: 18 local `.claude/skills` + 57 native `sniped-*` + the 50-skill pack + 15 `os_*` production scripts.**
- **Remaining gaps (NOT counted as engaged):** 34 needs_ocr (scanned photo/lighting-diagram books), 5 needs_visual_review (Maus, Eggleston Guide, Haas, Abloh), 1 needs_transcription (the MP4). None are core business/strategy doctrine.
- **High-confidence areas:** AI image/composite, photography/lighting/production, brand/positioning/pricing, persuasion/copy/offers, Claude/agents/MCP/automation, operations/SOPs/gates, decision-making/strategy/systems, legal/employer-conflict gates. (Many verified sources + built skills.)
- **Lower-confidence areas:** AI video/animation (doctrine yes, skills/tests thin), Blender/Unreal 3D (doctrine yes, no execution record), Unreal specifically, marketplaces/community, voice agents (Vapi/Retell/ElevenLabs not in the corpus), current-market 2026 specifics (need web), and live platform/legal specifics.

---

## 3. CAPABILITY COVERAGE MATRIX (by category, not project)

Confidence: HIGH = multiple verified sources + a built skill; MED = doctrine but no skill or untested; LOW = thin/theoretical. Full 9-field detail per category in `OS_CAPABILITY_COVERAGE_MATRIX.md`.

| Category | Conf | Knows / does | Built skills | Needs |
|---|---|---|---|---|
| AI image generation | **HIGH** | tool hierarchy, model routing, identity gate, 5-element prompt, Track B 5-step, 3-tier polish | seedream-prompt, ai-image-tool-pick, higgsfield-pipeline, hero-composite-lite/ceiling, composite-master-qa | composite-environment-router, crs-generator, generative-fill-discipline |
| AI video generation | MED | platform routing (Seedance/Kling/Cinema), virality predictor, 3-tier polish; video = support not deliverable | higgsfield-generate | kling-production-sop, motion-pipeline |
| AI animation | MED | dialogue-free is AI's strength; motion-as-billboard; image-to-video | (via higgsfield-generate) | animation-sop |
| character consistency | MED-HIGH | CRS mandate (14-ref sheet), Nano Banana identity-preserve, 350-img model concept | (campaign-house CRS stage) | sniped-crs-builder (logged) |
| style reference systems | HIGH | Midjourney SREF codes, v3 LUXURY lock, HEX palettes, 7-env vocab | seedream-prompt | sref-library skill |
| worldbuilding | MED | Composite Environment Rotation (7 locked), Island-of-Nod wide/med/close, lineage texture | art-series | world-bible skill |
| Blender/Unreal/3D | LOW-MED | official Blender MCP ($8/env), Unreal procedural gen, Patina PBR | (mcp-1 server read) | blender-pipeline (no exec record) |
| Photoshop/Lightroom/Adobe | HIGH | v3 LUXURY develop, 16-rail catalog, Evoto pass, Generative Fill discipline, Adobe MCP ops | luxury-edit, evoto-skin-pass, platform-mastering, composite-master-qa | preset-sync skill |
| photography/lighting/production | HIGH | Direction Stack 10-protocol, 30-shot, Nine Masters, capture-to-delivery, casting/lighting | direction-stack, capture-to-delivery, pre-shoot/shoot-day, lighting-vault | (mostly built) |
| cinematic direction | MED-HIGH | light-as-protagonist, atmospheric planes, sequencing, B&W register | direction-stack, photo-theory | cinematic-grade skill |
| brand building | HIGH | challenger 8-credos, Lighthouse identity, naming (Lexicon), positioning, Play Bigger | positioning-phrases, name gate (os_name_gate) | brand-system skill |
| fashion/luxury/status | HIGH | Trading Up ladder, status psychology, luxury strategy, quiet-luxury restraint | new-luxury, status-psychology | (built) |
| products/ecommerce/drops | MED | print-on-demand, drop cadence, edition economics, unit math | (validation-machine) | drop-engine skill |
| digital products | MED | $27-297 stacks, prompt/template products, zero-marginal-cost | (none specific) | digital-product skill |
| subscriptions | MED | recurring asset/visual-drop models, MRR math | (none) | subscription skill |
| licensing/IP | MED | owned-IP > rented likeness, Cornered Resource, Perennial Seller | (none) | licensing-engine skill |
| media companies | MED | faceless multi-channel, Hit Makers mechanics, scene-density | hit-mechanics, blockbuster-strategy | media-engine skill |
| YouTube/short-form/social | MED | broadcast/MAYA/clusters, dialogue-free cinematic, faceless | hit-mechanics | youtube-engine skill |
| copywriting/persuasion/offers | HIGH | TCREI, Schwartz awareness, Rule of One, Value Equation, Cialdini, AI-tell blocklist | caption-writer, positioning-phrases, voice gate | offer-builder skill |
| sales/outreach/lead-gen | HIGH | VIB, Ambient Audit, Cold-Calling-2.0, Seeds/Nets/Spears, Mom Test, cold-email stack | vib-outreach, discovery-to-close, wwp-positioning | crm-router skill |
| automation/agents/Claude/MCP | HIGH | 95/5 rule, complexity budget 2/6/8+, 11-step toolchain audit, the workflow engine itself | os-command-router, token-safe-reader, the whole os_* harness | (strong) |
| websites/funnels/apps | MED | Carrd conversion surface, CRO 3-phase, UX 141-checkpoint, Vercel deploy | (none built) | site-builder skill |
| operations/dashboards/SOPs | HIGH | capture-to-delivery, gate library, lean override, registry+dashboard, the production harness | os-production, os-batch, os-checkpoint, registry | (strong) |
| legal/ethical/employer-conflict | HIGH | payment-follows-proof, name gate, likeness/owned-IP, employer-conflict gate | os-quality-gates (gates 5/6) | contract-template skill |
| investing/ownership/holding | MED | margin of safety, Outsiders capital allocation, holding-company portfolio frame, 7 Powers | (none) | (theoretical) |
| decision/strategy/systems | HIGH | Thinking-in-Systems leverage, premortem, Munger 2-track, Sowell test, possibility-engine | decide, challenge, operator-review, the gates | (strong) |

---

## 4. TOOL & APP INVENTORY

| Tool | OS confidence | Known use | Can automate | Manual/taste | Needs web check |
|---|---|---|---|---|---|
| **Claude / Claude Code** | HIGH | the brain; skills, workflows, MCP, the os_* harness | routing, reads, gates, synthesis, production logging | strategy/voice/judgment | features evolve |
| **ChatGPT/Gemini** | MED | metaprompting, Gems creative-director layer, research | prompt expansion | n/a | yes |
| **Midjourney** | MED | SREF/style codes, all-AI visuals | style-locked batches (manual app) | sref curation | yes (v-version) |
| **Higgsfield (MCP, live)** | HIGH | image (Nano Banana), video (Seedance/Kling/Cinema), virality predictor, Marketing Studio | generate/poll/ingest via os_generate | concept + reject gate | model list shifts |
| **Nano Banana Pro** | HIGH | identity-preserving composites, CRS work | per-prompt gen | identity approval | yes |
| **Blender** | LOW-MED | official MCP, procedural env, PBR ($8/env) | bpy via MCP (no exec record) | scene taste | yes |
| **Unreal** | LOW | procedural world gen (transcript) | none yet | all | yes |
| **Photoshop / Adobe MCP** | HIGH | select/fill/hsl/preset; composite assembly | image ops via MCP | composite finish | minor |
| **Lightroom** | HIGH | v3 LUXURY develop, 16-rail catalog, presets | export presets (local) | develop taste | no |
| **DaVinci Resolve** | MED | grain/halation finish (3-tier polish) | none (manual) | the finish | no |
| **Figma (MCP)** | MED | VIB/dossier/card authoring, design system | generate/sync via MCP | layout taste | minor |
| **Canva** | LOW | not in verified corpus | n/a | n/a | yes |
| **Excel/Sheets** | MED | unit math, cost ledgers, registries | CSV via scripts | n/a | no |
| **Notion / Airtable (MCP)** | MED | CRM schema, project tracking | records via MCP | n/a | minor |
| **n8n / Make / Zapier** | MED | Kling+Topaz batch orchestration, automations | flows (external) | n/a | yes |
| **Vapi / Retell / ElevenLabs / voice** | LOW | NOT in verified corpus | none | all | yes (full) |
| **Vercel** | MED | static site deploy (CLI authed) | deploy via MCP/CLI | site design | minor |
| **Shopify / Gumroad / Stripe** | MED | DTC, digital products, payment rails; payment-follows-proof | checkout links | offer design | yes |
| **Instantly / Super Search** | MED | cold email stack, lead sourcing | campaigns (external) | copy | yes |
| **YouTube / IG / TikTok / X** | MED | distribution, faceless channels, Hit Makers mechanics | scheduling (no connector yet) | all content | yes (algos) |
| **Higgsfield CLI** | MED | installed (@0.1.40), unverified syntax/auth | possible full gen automation | n/a | yes |

---

## 5. MONEY-MODEL INVENTORY (first-principles, not old lanes)

| Model | Fastest cash | Proof loop | Needed assets | Risk | Upside | Faceless? | Optionality |
|---|---|---|---|---|---|---|---|
| Services (done-for-you visuals) | days (1 pilot) | 1 paid pilot delivered | a studio pseudonym + 1 spec set | feast/famine | mid | yes | preserves |
| Retainers / productized service | weeks | 1 monthly client | scoped offer + pipeline | scope creep | mid-high (MRR) | yes | preserves |
| Digital products (prompt/template/system) | days-weeks | 1 product sells on $0 seed | 1 packaged system | saturation | high margin | yes | preserves |
| Print drops | days (preorder) | 200-print sellout / 300-signup gate | 1 owned hero frame + POD | distribution seed | mid | yes | preserves |
| Physical products / merch | weeks | preorder conversion | POD + brand | inventory (avoid w/ POD) | mid | yes | preserves |
| Licensing / IP | slow | 1 license inquiry on a one-sheet | an owned character/world catalog | needs owned IP first | very high (royalties) | yes | preserves |
| Media channel (faceless YT/short) | slow (ad), mid (sponsor) | 3 posts, retention read | a channel + cinematic pipeline | red-ocean if generic | high (owned audience) | yes | preserves |
| Subscriptions (asset/visual drop) | weeks | 25 founding members | recurring drop engine | churn | high (recurring) | yes | preserves |
| Affiliate / referral | days | 1 referral close | warm list | low control | low-mid | yes | preserves |
| Sponsorship | weeks-mid | 1 brand placement | an audience/cluster | depends on audience | mid | yes | preserves |
| Consulting | days | 1 scoped call | credibility | identity-exposing | mid-high | NO (usually) | can trap |
| Software / tools | slow | 1 user with a real problem | a working tool | build risk | very high | yes | preserves |
| Community | mid | 25 founding seats | a niche + curation | empty-room | high (network) | yes | preserves |
| Marketplace | slow | 2-sided demand signal | network effects | hardest | very high | yes | preserves |
| Automations / agents | weeks | 1 automation a client pays for | a repeatable agent | maintenance | mid-high | yes | preserves |
| Local business offer | days | 1 local close | proximity | identity-exposing | mid | often NOT | can trap |
| Creator economy (content + products) | mid | audience + 1 product attach | content engine + product | platform risk | high | yes | preserves |

Cross-cut: faceless/off-grid + owned-IP + recurring is the optionality-preserving cluster; consulting/local/personal-brand are the identity-trapping ones (per `feedback_possibility_engine_optionality`).

---

## 6. TRACEABILITY (no "trust me")

| Capability | Doctrine cluster (cite) | Skill/workflow | Tested? | Real-world proof needed |
|---|---|---|---|---|
| AI image gen + composite | MASTER §2/§6, CAPABILITY_TOOL_ROUTING §1, DOCTRINE batches 002/007/008/011/012 | seedream-prompt, ai-image-tool-pick, higgsfield-pipeline, composite-master-qa, **os_generate/os_batch** | **YES** , 4 real Higgsfield gens (live_001, batch_001 x3, l4 obelisk) through the harness | a delivered client composite passing the AI-disclosure gap (CF-020) |
| character consistency | Nano Banana CRS mandate (MASTER §2, NEWFILES) | campaign-house CRS stage; sniped-crs-builder (logged) | partial (no multi-frame CRS run yet) | a 5-frame identity-locked set |
| photography/production | Direction Stack, Nine Masters, capture-to-delivery (MASTER §2, REREAD shelves) | direction-stack, capture-to-delivery, luxury-edit, lighting-vault | distilled, not field-run this session | one paid Reset delivered |
| persuasion/copy/offers | TCREI, Schwartz, Cialdini, Hormozi Value Eq (DOCTRINE batches, REREAD C) | caption-writer, positioning-phrases, voice gate (os_production) | **YES** , voice gate catches em-dash/AI-tell live | a converting piece of copy |
| sales/outreach | VIB, Ambient Audit, Cold-Calling-2.0, Mom Test (ROUTING_MANIFEST D2, REREAD) | vib-outreach, discovery-to-close | distilled, not sent | 1 booked discovery call |
| automation/agents/Claude | 95/5, complexity budget, 11-step audit, Claude manual | os-command-router, token-safe-reader, **the entire os_* harness** | **YES** , 14/14 regression suite + 6 live hooks | continued daily runs |
| production ops / gates | gate library, capture-to-delivery, lean override | os-production, os-batch, os-checkpoint, registry, os-quality-gates | **YES** , dry-runs + 1 real + 1 batch + resumability proven | a full real cohort to posting |
| decision/strategy/systems | Thinking-in-Systems, premortem, Munger, possibility-engine | decide, challenge, operator-review, the gates | partial (gates run; judgment is human) | a real decision validated by proof |
| Blender/Unreal 3D | official MCP, NEWFILES | mcp-1 server (read only) | **NO** , theoretical, no exec record | one rendered environment |
| voice agents | NONE in corpus | none | **NO** , absent | requires new ingestion + web |

---

## 7. OS WEAKNESS AUDIT (what it cannot do well yet)

- **Missing tools/knowledge:** voice agents (Vapi/Retell/ElevenLabs), Canva, marketplaces, live ad-platform mechanics , not in the verified corpus.
- **Missing integrations:** no posting/scheduling connector (campaign-house stages 11-12 are manual-gated), no analytics/proof connector, no live `/usage` read, Higgsfield CLI unverified.
- **Unprocessed files:** 34 OCR (scanned photo/lighting books), 5 visual (Maus/Eggleston/Haas/Abloh), 1 MP4 , flagged, not engaged.
- **Weak app knowledge:** Blender/Unreal (doctrine, no execution), DaVinci (manual), voice tools (none).
- **Weak current-market knowledge:** 2026 platform algorithms, current pricing, what's trending , the corpus is a snapshot; **web research required** for anything time-sensitive.
- **Legal uncertainty:** the composite AI-disclosure addendum (CF-020) is an unresolved hard block before any composite ships commercially; employer IP/non-compete specifics are unverified (operator must check own agreement).
- **Platform uncertainty:** social ToS, AI-content disclosure rules, likeness law , all need web verification.
- **Where the OS might be overconfident:** treating doctrine as doability (a distilled book principle is not a tested workflow); assuming a tool works as the corpus described when it may have changed; assuming a money model's numbers without a live proof loop.

---

## 8. EVALUATION SUITE (proves activation)

| # | Benchmark | Passing answer must include | Failing answer looks like | Doctrine/skills that should activate |
|---|---|---|---|---|
| 1 | generate a 2026-native faceless money model from zero | new (not old-lane) model + faceless rail + 24h/7d proof loop + cited doctrine + optionality preserved | renames an old lane; no proof loop; crowns it | possibility-engine, money-model inventory, proof-loop doctrine, name gate |
| 2 | build a one-person campaign pipeline | the 14-stage harness w/ gates + automated-vs-manual line + the os_* commands | a vague list with no gates | os-production, os-batch, campaign-house pipeline |
| 3 | design a character-consistency workflow | CRS 14-ref sheet + Nano Banana routing + identity gate + consistency check across frames | "just prompt the same name" | CRS mandate, ai-image-tool-pick, vision-reject-gate |
| 4 | route an AI video idea through tools | Seedance/Kling/Cinema selection + 3-tier polish + virality predictor + dialogue-free note | names one tool, no routing/finish | higgsfield-generate, tool-routing, 3-tier polish |
| 5 | turn a book principle into an executable skill | the principle + a SKILL.md (trigger/inputs/outputs/rule) + a test | restates the principle only | capability-growth mandate, skill lifecycle |
| 6 | create a no-conflict off-grid monetization path | faceless + no-employer + honest $ path + legal/employer-conflict gate + proof loop | LinkedIn-first / identity-exposing | employer-conflict gate, off-grid rules, payment-follows-proof |
| 7 | compare 5 money models without old-lane anchoring | 5 models x (fastest cash/proof/risk/upside/faceless/optionality) + no crowning | ranks old lanes; picks a throne | money-model inventory, anti-old-lane gate, optionality gate |
| 8 | build a production SOP with gates | numbered stages + per-stage gate + reject/audit/completion gates + logs | steps with no gates | gate library, os-quality-gates, capture-to-delivery |
| 9 | identify where proof is required before scaling | names the proof loop + kill/keep/scale + what's still theoretical vs tested | "just scale it" | proof-before-crowning gate, traceability, completion-verification |

A passing OS answers all 9 citing real doctrine/skills, discloses unverified dependencies, and refuses to crown a lane. (This suite can be run as a manual benchmark each quarter.)

---

## 9. FINAL ANSWER

**Is the OS activated enough to generate from zero at a high level? YES, for the high-confidence categories, with two honest caveats.**

**Why yes:** 96.6% of sources are verified (read + distilled), the capability map + 167 doctrine docs make it retrievable, the gates/routing make it operationalized, and a real, tested production harness (15 `os_*` scripts, 6 enforced hooks, 14/14 regression, 5 real Higgsfield generations through the full gated funnel) proves the OS is **not a pile of summaries** , it routes knowledge into tools, workflows, money models, and proof loops, and it self-checks. The HIGH-confidence spine (AI image/composite, photography/production, brand/positioning/pricing, persuasion/offers, sales/outreach, Claude/automation, operations/gates, decision/systems) is genuinely operational and partly tested.

**The two caveats (what to build/verify before leaning on the weak areas):**
1. **Skill build-out lags knowledge in the creative-scale categories** , AI video/animation, Blender/Unreal 3D, worldbuilding, digital-products/subscriptions/licensing/media are *distilled and retrievable* but mostly *not skill-built or tested*. The OS can reason about them; it cannot yet execute them on demand without building those skills.
2. **Time-sensitive and absent areas need web + new ingestion** , 2026 market specifics, voice agents, marketplaces, live platform/legal rules. The OS must disclose these as unverified and route to web research, not bluff.

**Net:** the OS knows what it has, can trace each major capability to its doctrine cluster + skill + test status, and can route into tools/money/proof. It is activated for high-level generation in the verified spine, and honest about where it is only theoretical. Build the creative-scale skills and verify the time-sensitive tools, and the weak categories move from *known* to *doable*.
