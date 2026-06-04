## SKILLS

Below is the consolidated, deduplicated, prioritized skill backlog for the SNIPED OS. Each entry is synthesized from the full capability digest across all 166 doctrine docs.

---

### Production + Composite

| Name | One-Line Purpose | Trigger | Inputs | Outputs | Extends/Replaces | Priority |
|---|---|---|---|---|---|---|
| `sniped-composite-modular-6part` | Runs the 6-part modular composite workflow SOP from plate to delivery | Any composite job enters queue | Subject TIFF, environment brief, chapter assignment | Composite PSD + gate checklist completed | Extends composite-master-qa | now |
| `sniped-composite-shadow-check` | Validates shadow physics (type, opacity, blur, gradient, mode, light coherence) before composite finalizes | Pre-delivery gate on any composite | Merged composite file | Pass/fail + fix list per shadow element | Part of composite-master-qa | now |
| `composite-master-qa` | 8-gate QA + 6-axis scorecard mandatory before client or deck entry | Every composite before delivery | Composite file, environment spec | Gate results, axis scores (each 8/10 min), client-ready verdict | Extends existing composite-master-qa (LOCKED 2026-06-02) | now |
| `sniped-generative-fill-discipline` | Triage tree for Generative Fill: 6-attempt cap, approved prompt patterns, variant selection, escalation routing | Any Generative Fill session opens | Subject region, environment brief | Approved fill or escalation directive | Replaces ad-hoc Firefly use | now |
| `sniped-over-processing-gate` | Pre-delivery gate: does output serve the photograph or mythology? Output must beat source visually | Before any image ships | Processed image vs. source RAW | Pass/fail + beat-source test result | Extends sniped-sprezzatura-check | now |
| `sniped-gesture-audit` | 3-question gate: specific gesture present, color serves gesture, trigger identifiable | Pre-delivery on any portrait composite | Final composite or hero image | Pass/fail + named gesture or block directive | New | now |
| `sniped-color-relationship-check` | Color family count, accent/trigger present, interaction vs. competition logic | Pre-finalization of composite | Final image or composite file | Pass/fail + fix list | New | now |
| `sniped-bliss-point-audit` | Confirms 3-4 visual hook moments per artifact before release | Before any Card, HERO, or composite publishes | Image or composite | Hook inventory (named moments) + pass/fail | New | now |
| `sniped-apparatus-audit` | Gate: body readable, lighting reveals, environment serves, negative-proof library checked | Pre-delivery on any chapter image | Hero or composite | Pass/fail per apparatus criterion | New | now |
| `sniped-composite-qa-gate` | Cutout boundary + identity preservation: edge quality, skin texture, world separation, tone restraint | Before any composite enters delivery pipeline | Composite PSD | Structured pass/fail checklist | Part of composite-master-qa | now |
| `sniped-generatives-audit` | Score composite or deliverable against Kelly 8 generatives; Embodiment + Authenticity required | Pre-publish on any major deliverable | Final image/composite | Generative score + pass/fail | New | now |
| `sniped-composite-subject-gate` | Protocol 01-06 checklist before Higgsfield or Adobe queue entry | Pre-generation gate | Source frame | Protocol compliance verdict | New | now |
| `sniped-composite-defense` | Barthes-grounded copyblock in 4 registers (casual/professional/academic/teaching) for hybrid-operator stance | When composite methodology needs defending in copy or DM | Composite image or chapter output | 4-register defense copy | New | soon |
| `sniped-hero-composite-lite` | Hero composite workflow with reference image sub-workflow + environment-specific library | Reset or Brand System shoot composite | Subject, environment choice, reference images | Composite PSD + environment library (3-5 per env) | Extends existing sniped-hero-composite-lite | now |
| `sniped-hero-composite-ceiling` | Ceiling-tier composite with DOF/lens match, perspective/camera-height, directional color bleed gates | Client-ready composite or portfolio anchor | High-res subject + environment plates | Ceiling-grade composite + 11-gate QA | Extends sniped-hero-composite-lite | soon |
| `sniped-environment-prebuild` | Pre-production loop: reference curation, prop sourcing, pre-viz, lighting simulation, generative fill test | Before any new composite environment chapter | Environment brief + chapter assignment | Pre-viz composite, prop list, lighting sim | New | soon |
| `sniped-rememory-environment-brief` | Composite environment briefing encoding cultural frequency, lineage marker, memory activation | Opening a new chapter environment | Chapter assignment, lineage anchor | Brief + rememory anchor doc | New | soon |
| `composite-environment-router` | 5-element prompt routing (WHAT/STYLE/LIGHTING/ENVIRONMENT/TECHNICAL) + model-task routing | Any AI image generation task | Job description + chapter assignment | Model selection + prompt scaffold | Extends sniped-seedream-prompt | now |
| `sniped-seedream-prompt` | HEX palette + camera cheat code + 7-environment rotation vocab; no subject generation | Track B composite plate generation | Chapter environment, color palette | Seedream prompt + plate output | Extends existing sniped-seedream-prompt | now |
| `block-environment-spec` | Locked Block visual spec (space type, depth cues, linear motif, tonal range, color scheme, shape) per named environment | Before any environment chapter shoot or composite | Environment name + chapter | Environment spec sheet | New; used by composite-environment-router | soon |
| `visual-structure-audit` | Block 7-component pass/fail per composite environment | Pre-delivery composite review | Composite + environment spec | Pass/fail + gap list | New | soon |
| `sniped-environment-line-audit` | Composite QA for competing line-types without hierarchy | Pre-delivery composite review | Composite image | Line-type conflict report + fix directive | New | soon |
| `sniped-display-intent` | Pre-shoot intention-to-display pipeline: Card vs. HERO vs. print vs. book decided before shutter | Planning any shoot | Shoot brief | Display intent doc | New | now |
| `sniped-three-level-eval` | Shore physical/depictive/mental evaluation gate; mental is tier-one criterion | Image selection + portfolio entry | Image set | Tier classification per image | New | now |
| `sniped-sequence-review` | Five-level image batch evaluation (individual/pair/series/section/thread) | Before any chapter or carousel publishes | Curated image set | Sequence manifest + gap flags | New | soon |
| `sniped-image-eval` | Freeman Six Qualities gate: scored pass/fail per dimension + display routing | Image selection gate | Candidate images | Scored gate results + routing directive | New | now |
| `photo-qa-gate` | 8-criterion 1-10 matrix; emotional weight + uniqueness must both clear 6 | Before any image ships publicly | Final image | Score card + ship/hold verdict | New | now |
| `sniped-sprezzatura-check` | Looks-less-processed-than-source + snapshot test | Before any image or composite ships | Processed image vs. source | Pass/fail + fix | Extends sniped-over-processing-gate | now |
| `platform-mastering` | Color + B&W per aspect ratio per safe area, contrast/sharpen/text applied; skin-drift measurement | After composite approval, before publish | Composite or hero image | Platform-ready masters per surface | Extends existing platform-mastering (LOCKED 2026-06-02) | now |
| `sniped-luxury-edit` | Environment-to-master assignment (Avedon/Eggleston/Leibovitz/Shore/Herzog/Frank/Meyerowitz/Haas/Iturbide); retouch depth by register | Post-cull, pre-delivery | Culled selects + register assignment | Retouch instructions + preset assignment | Extends existing sniped-luxury-edit | now |
| `lightroom-hero-preset-check` | SNIPED Hero Playbook QA: panel hierarchy + Three Pillars of Digital Depth + Evoto 85% gate | Before Lightroom export | Lightroom develop settings | Pass/fail + fix list | New | now |
| `sniped-lightroom-preset-audit` | Pre-export gate: preset, calibration, clarity, NR/grain conflict, export spec, cull compliance | Before any export | Lightroom catalog + export settings | Pass/fail + compliance report | New | now |
| `sniped-evoto-preset-library` | Per-shoot-type Evoto presets (Portfolio/Client Natural/Chapter Card B&W/HERO color) with 30-75% restraint thresholds | Before Evoto batch session | Shoot type + register | Preset selection + slider caps | New | now |
| `sniped-evoto-batch-grade` | Operationalizes Evoto AI Color Match: hero reference, environment preset, batch run, 3-image sample validation, TIFF export | Batch retouching session | Hero reference TIFF + batch folder | Validated batch TIFFs | New | now |
| `evoto-routing-decision-tree` | Studio-only scope gate; non-studio routes to composite | Before any Evoto session | Image context (studio vs. location) | Route directive: Evoto or composite | Extends existing evoto-routing-decision-tree | now |
| `sniped-capture-to-delivery` | v3 5-pass cull + v2 3-tier edit pipeline (8-12 Heroes/30-40 Selects/60-100 Proofs in 2-3.5 hr); Pixieset reset/upsell routing | Post-shoot processing | RAW files + shoot card | Tiered deliverable set + Pixieset gallery | Extends existing sniped-capture-to-delivery | now |
| `sniped-retoucher-onboarding` | 4-hour onboarding; BJ owns cull/labels/Hero promotion/preset/final approval; Retoucher owns preset apply/masks/Evoto/PS routing | New retoucher hire | Retoucher intake + SNIPED preset library | Onboarding protocol + performance contract | Extends existing sniped-retoucher-onboarding | soon |
| `sniped-posing-director` | Real-time on-set co-pilot: pose library lookup, micro-cue scripts, workflow timers, energy matching by founder type | During shoot, on-set | Shoot brief + subject type | Pose queue + direction scripts | Extends existing sniped-posing-director | now |
| `sniped-direction-stack-pre-shoot` | Rotation setup, anchor calibration cues, subject-type classification, operator briefing card | Day before any shoot | Shoot brief + subject profile | Pre-shoot briefing card | New | now |
| `sniped-on-set-diagnostic` | Real-time protocol-failure root-cause identification with Shore/Direction Stack cue options | Mid-shoot when direction stalls | Observable behavior pattern | Named protocol failure + correction cue | New | now |
| `sniped-presence-reject-gate` | Protocol 09 presence gate at selects: hero/supporting/placeholder/reject classification | Image selection | Selects folder | Classification per image; performing/absent = placeholder | New | now |
| `sniped-composite-prompt` | 6-part Nano Banana prompt with camera specs, lighting, constraint language per CRS + environment slot | Before any AI plate generation | CRS + environment assignment | Validated generation prompt | New | now |
| `sniped-crs-generator` | Character Reference Sheet for composite workflows: multi-angle prompt set locked to identity | Before any composite session | Subject identity anchors | CRS doc | New | now |
| `sniped-moodboard-brief` | 5-section structure (Model/Lighting/Location/Hair-Makeup/Wardrobe), working vs. presentation phase, AI as pre-viz only | Pre-production planning | Shoot brief | Moodboard brief doc + crew PDF | Extends moodboard-brief-generator | now |
| `sniped-golden-hour-operator-playbook` | W1-W4 timeline (Open shade/Pre-golden/Golden hero PROTECTED/Afterglow); H1-H5 fallback hierarchy | Outdoor shoot planning | Shoot date + location | Timed shoot schedule + fallback cascade | Extends existing sniped-golden-hour-operator-playbook | now |
| `sniped-bts-shot-list` | Mandatory BTS capture angles per shoot; resolves carousel attribution gap structurally | Every shoot plan | Shoot brief | BTS capture protocol | New | now |
| `sniped-shoot-day-reset` | Direction Stack diagnostic mandatory; no mid-shoot scope adds | Shoot day | Shoot brief + cast | Real-time direction reset protocol | Extends existing sniped-shoot-day-reset | now |
| `sniped-shoot-day-strategic-free` | 4-8 frames vs. 8-12 paid; explicit trade terms; refuse vague exposure | Free-shoot booking request | Booking inquiry | Scoped SOP with trade terms | Extends existing sniped-shoot-day-strategic-free | now |
| `sniped-pre-shoot-prep` | Day-before checklist: weather/gear/contingencies/casting confirms | Evening before shoot | Shoot brief + cast confirms | Completed prep checklist | Extends existing sniped-pre-shoot-prep | now |
| `sniped-casting-call-doctrine` | 24-hr confirm, wardrobe gate, two-strike removal, tier-2 standby, 48-hr MUA confirm | Casting process for any shoot | Casting form responses | Confirmed cast list + tier-2 standby | Extends existing sniped-casting-call-doctrine | now |
| `sniped-photo-artifact-route` | 5-destination taxonomy, 10-step develop base, reject gate, 9-preset export stack | Post-cull routing decision | Culled image set | Routed and exported artifacts | Extends existing sniped-photo-artifact-route | now |
| `sniped-art-series-frame` | Master wrapper for all 9 Art Series frame skills | Any Art Series chapter shoot | Chapter brief + master assignment | Routed to correct frame skill | Extends existing sniped-art-series-frame | now |
| `sniped-art-series-avedon` | 60% retouch ceiling, mask-drop gate, 15-20 min buffer post-final-shot | Avedon chapter shoot | Chapter brief | Shoot + retouch protocol | Extends existing sniped-art-series-avedon | soon |
| `sniped-art-series-leibovitz` | Concept-before-medium gate, 30-min pre-camera interview, one-sentence thesis lock | Leibovitz chapter shoot | Chapter brief | Thesis + shoot protocol | Extends existing sniped-art-series-leibovitz | soon |
| `sniped-art-series-iturbide` | B&W sealed exception, 40% retouch, subject collision, back-turned series | Iturbide chapter shoot | Chapter brief | Shoot + register protocol | Extends existing sniped-art-series-iturbide | soon |
| `sniped-air-test` | 4-question binary: air presence, identity hold, punctum detail, blind field gate | Before portfolio publish or case study entry | Hero or portfolio candidate image | Pass/fail per criterion | New | soon |
| `sniped-portrait-brief-generator` | Pre-shoot brief with air criteria + lineage context + punctum permission + blind-field direction | Pre-shoot planning | Subject profile + chapter | Shoot brief | New | soon |
| `sniped-avedon-authenticity-gate` | 3-question pre-delivery gate: environment serves presence, identity untouched, existential weight present | Pre-delivery on any hero | Hero image | Pass/fail + fix | New | soon |
| `sniped-composition-repertoire` | Freeman schema library (12 named schemas) with line-type and emotional register annotations | Composite environment planning | Environment spec | Schema selection + line-type assignment | New | later |
| `sniped-frame-decision` | Aspect ratio, dominant line-type, focal length, key selection, context contribution, figure-ground, beholder's share | Pre-shoot gate | Shoot brief + environment | Framing directive | New | later |
| `rawpy-batch-develop` | CR3 folder + XMP preset + operator gate; 75-85% Lightroom fidelity TIFFs + metadata JSON + integrity log | Phase 2 batch development (operator-approved) | CR3 RAW folder + preset | TIFF batch + integrity log | New | later |
| `kling-production-sop` | Multi-shot workflow: element checklist + 5-Part Cinematic Structure + two-pass protocol; Higgsfield vs. Kling Omni platform selection | Any video or motion project | Motion brief | Production SOP + asset checklist | New | soon |
| `sniped-video-philosophy` | Motion work briefing for 6 video formats; editor brief + "Never Happens" checklist + platform specs | Motion project planning | Motion brief | Editor brief + format specs | Extends existing sniped-video-philosophy | soon |
| `sniped-motion-pipeline` | Music-driven hero film/brand film: beat-mapping, LUT, AI plate slots; Lane A (Old Hollywood)/Lane B (clean product) | Brand film or chapter film production | Film brief | Production pipeline doc | Extends existing sniped-motion-pipeline | later |

---

### Outreach + Sales

| Name | One-Line Purpose | Trigger | Inputs | Outputs | Extends/Replaces | Priority |
|---|---|---|---|---|---|---|
| `sniped-vib-outreach` | Specific compliment + soft offer + subtle proof + single yes/no ask; 5 failure modes refused; protocol diagnosis gate mandatory before send | VIB DM batch prep | Prospect profile + visual gap assessment | Validated DM draft | Extends existing sniped-vib-outreach | now |
| `sniped-vib-dm-sequence` | Staged DM (mirror opener + label + pause + No-invitation frame + calibrated discovery Q) | VIB DM send | Prospect profile + thumbscrew map | Sequenced DM draft | Extends sniped-vib-outreach | now |
| `sniped-vib-gap-diagnosis` | Isolation of Section 9 (SOP_assistant.md); reusable for case study selection, authority positioning, editorial direction review | Pre-VIB or case study planning | Prospect profile or past engagement | Gap diagnosis + protocol number | Extends existing sniped-vib-gap-diagnosis | now |
| `sniped-thumbscrew-map` | Founder profiling: LinkedIn/IG signals, emotional void identification, mirror strategy, first-touch framing | Pre-VIB DM prep | Prospect LinkedIn/IG profile | Founder profile + first-touch strategy | New | now |
| `sniped-vib-onboarding-arc` | Know/Feel/Do model per tier transition | VIB tier-level change | Current VIB tier + engagement history | Tier transition protocol | New | soon |
| `sniped-conversion-waterfall` | 100 warm LA Tier 0 > 20 engaged > 4 free-offer > 1 paid calibration model | Quarterly outreach planning | Current pipeline state | Calibrated outreach targets | New | soon |
| `sniped-discovery-to-close` | Same-day reply, diagnostic Mom Test call, same-day follow-up, deposit booking; 15-min call structure + 9-step flow + objection handlers + Green/Yellow/Red sorting | Inbound inquiry received | Inquiry details + prospect profile | Discovery call outcome + next action | Extends existing sniped-discovery-to-close | now |
| `sniped-discovery-call-script` | Diagnosis-model sales call script; 5-7 discovery Qs; anti-pitch enforced | Discovery call prep | Prospect profile + gap diagnosis | Call script + objection prep | Extends sniped-discovery-to-close | now |
| `sniped-gap-discovery-protocol` | Keenan discovery checklist: current state (quantified), future state (3-part), intrinsic motivation, gap formula | Pre-VIB conversion call prep | Prospect current/future state data | Gap formula + call prep | New | now |
| `sniped-mom-test-intake` | Structured discovery: 3 big questions, Mom Test question set, bad data deflection, commitment/advancement checkpoint | Discovery call or VIB warm-up | Prospect conversation | Validated signals + commitment check | Extends mom-test-customer-conversation | now |
| `sniped-outreach-combo` | Timed COMBO artifact: LinkedIn comment + DM + Instantly email + voicemail, trigger-event hook baked in | Tier HOT target activation | Trigger event + prospect profile | COMBO sequence artifact | New | now |
| `sniped-trigger-scan` | Daily scan: CrunchBase, Google Alerts, LinkedIn Nav, 24-hr LA founder search; ranked 5-10 warm targets with trigger context | Daily prospecting session | ICP criteria + LA founder filters | Ranked warm target list with triggers | New | now |
| `sniped-outreach-sequence` | Generalized 3-email diagnostic-reframe-giveaway pattern | Cold email campaign | ICP segment + offer | 3-email sequence | Extends existing sniped-outreach-sequence | now |
| `sniped-outbound-c1-tech-ops` | End-to-end C1 loop: lead pull, tier tag, email sequence, Loom production, funnel tracking | C1 outreach campaign launch | ICP list + offer | Full C1 campaign | Extends existing sniped-outbound-c1-tech-ops | now |
| `sniped-cold-email-campaign-launch` | Campaign lifecycle (Week 0-1 templating, lead pull, Instantly setup, A/B split, Ren cadence) | Cold email campaign initiation | ICP criteria + offer | Campaign launch SOP | Extends existing sniped-cold-email-campaign-launch | now |
| `sniped-cold-email-doctrine` | Rule of one, awareness staging, subject-line discipline, deliverability | Cold email copy review | Draft email | Compliance report + rewrites | Extends existing sniped-cold-email-doctrine | now |
| `sniped-cold-email-infrastructure` | 4-step VIB outbound: visual gap verification, trigger-event sourcing, soft-ask micro-offer template, buying-committee waterfall | VIB cold outreach build | ICP segment | Validated outbound stack | New | now |
| `sniped-outreach-anatomy` | 5-part anatomy (hook + compliment + case study + CTA + signature) | Any cold outreach draft | Prospect profile + offer | Anatomically correct draft | New | now |
| `sniped-follow-up-sequence` | 4-touch arc (Day 0/3/6/9 breakup); Instantly or Notion CRM queue | Post-outreach follow-up | Prospect status + last touch | Follow-up sequence | Extends existing sniped-follow-up-rules | now |
| `sniped-follow-up-rules` | B2B cadence, stop thresholds, reply windows | Outreach cadence review | Campaign metrics | Cadence adjustment directive | Extends existing sniped-follow-up-rules | now |
| `sniped-hook-engine` | 5+ opening patterns by content type; hook_library.md | Any copy or outreach draft | Content type + audience | Hook variants | Extends existing sniped-hook-engine | now |
| `sniped-headline-forge` | Three Ogilvy variants per post/DM/caption: benefit+news+brand, ticket-on-meat specificity, emotional amplification | Any headline-writing task | Content brief | 3 headline variants | Extends sniped-headline-factory | now |
| `sniped-post-delivery` | Day-0 v2 delivery, Day-7 testimonial ask, Day-30 Op Kit pitch; full 9-template email lifecycle state machine | Post-shoot delivery | Delivery date + client record | Delivery email sequence | Extends existing sniped-post-delivery | now |
| `sniped-referral-drip-trigger` | Day-45 automated referral drip post-delivery; educational asset + soft invite + incentive | Day-45 post-delivery | Client delivery record | Referral drip sequence | New | now |
| `sniped-referral-activation-loop` | Week-2/4/6 post-delivery CRM workflow closing 83%-willing/29%-doing gap | Post-delivery follow-up | Delivery record | Referral request protocol | New | now |
| `sniped-referral-ask-menu` | Post-delivery referral ask generator; Hormozi 7-ask menu, top 2 context-appropriate options scripted | Post-testimonial milestone | Client testimonial + context | Scripted referral ask | New | now |
| `sniped-meeting-outcome-gate` | Post-conversation diagnostic against 8-case taxonomy; flags zombie leads, compliment traps, stall tactics | After every sales or VIB conversation | Conversation notes | Case classification + next action | New | now |
| `sniped-networking-opportunity` | 5-question filter (reciprocity/operator-coded fit/lane fit/trust transfer/time cost); 4+ YES = proceed | Any networking invitation | Invitation details | Accept/decline + next-action directive | Extends existing sniped-network-opportunity | now |
| `sniped-relationship-runway` | Cultivation timeline + touch-point sequence before ask | Pre-outreach relationship planning | VIB tier list | Cultivation calendar | New | soon |
| `sniped-sneezer-map` | Quarterly CRM workflow: map Tier 0 impressed contacts, evangelist credibility scores, story/tool equipped status, touchpoint dates | Quarterly CRM review | Tier 0 CRM | Sneezer tier list + enablement plan | New | soon |
| `sniped-loom-audit-production` | Protocol diagnosis tree, Higgsfield editorial portrait prompts, Descript assembly, QA checklist (6 points) | Loom production for cold outreach | Prospect profile | Loom video + QA checklist | Extends existing sniped-loom-audit-production | soon |
| `sniped-linkedin-pov-gen` | Angle + copy pairing for outreach warming | LinkedIn content planning | Topic + ICP | POV post draft | Extends existing sniped-linkedin-pov-gen | now |
| `sniped-scene-density-audit` | Weekly sub-agent sweep: DM tier distribution, cast repeat rate, collaboration density, LA cultural circle coverage | Weekly cadence | CRM + collaboration records | Scene-density health report | New | now |
| `sniped-intel-timing-brief` | Pre-pitch competitive intelligence scan of target's current state | Before any major pitch or VIB batch | Target profile | Current-state intelligence brief | New | soon |
| `sniped-converted-spy-tracker` | VIB network mapping by intel value, referral count, scenes opened, hub proximity | Quarterly VIB network review | Tier 0 CRM | Hub proximity map + activation priority | New | soon |

---

### Copy + Positioning

| Name | One-Line Purpose | Trigger | Inputs | Outputs | Extends/Replaces | Priority |
|---|---|---|---|---|---|---|
| `sniped-voice-test` | Raw copy in; pass/fail on Named/Sealed/Quiet/Lineage anchors + banned-word scan + em-dash scan + repair suggestions | Before any external copy ships | Draft copy | Pass/fail report + rewrites | Extends existing sniped-voice-test | now |
| `sniped-copy-audit` | 4 U's + 10-point gate + Motivating Sequence scoring for all positioning assets | Before any positioning asset ships | Draft copy | Score + pass/fail + rewrites | New | now |
| `sniped-copy-self-critique` | S2A + RaR + RE2 in sequence on copy assets; output: original + critique + revision | Before any LLM-generated copy ships | AI-generated copy | Critiqued + revised copy | New | now |
| `sniped-curse-of-knowledge-gate` | External artifact eval: jargon, buried lead, emotional hooks, story arc, identity appeal | Before any external artifact ships | Draft artifact | Pass/fail list + fixes | New | now |
| `sniped-success-checklist` | SUCCESs 6-axis score (Simple/Unexpected/Concrete/Credible/Emotional/Story) with weak-point fixes | Before Direction Stack chapters, VIB outreach, LinkedIn POV ship | Draft content | Score + fixes | New | now |
| `sniped-newspeak-gate` | Gate: could this describe a competitor without modification? Yes = flag for specificity re-injection | Before any positioning copy ships externally | Draft positioning copy | Pass/fail + specificity prompt | New | now |
| `sniped-language-drift-gate` | Diffs new positioning language vs. THE_SPINE.md + CANONICAL_TRUTHS.md; flags Commandment-revision patterns | Before any positioning change or major doc update | New positioning language | Diff report + drift flags | New | now |
| `sniped-proof-audit` | Input: image/caption/DM/case study. Claim = rejected. Proof = passes | Before any authority asset distributes | Draft artifact | Claim/proof classification per statement | New | now |
| `sniped-caption-architecture` | Two-level narrative (surface human interest + lineage subtext); load-bearing Hook (8 words) + Context (3-5 lines) + Deployment + CTA | Caption drafting at image selection | Image + lineage context | Caption draft + platform variants | Extends existing sniped-caption-writer | now |
| `sniped-reading-sequence-writer` | Notice > identity > relevance > support > details sequence; rejects features-first structure | Any copy or content artifact | Draft copy | Restructured copy | New | now |
| `sniped-caption-writer` | Hook (8 words) + Context (3-5 lines) + Deployment + CTA; platform-specific scaffolds | Caption production | Image + chapter context | Platform-ready captions | Extends existing sniped-caption-writer | now |
| `sniped-one-liner-generator` | Lineage-specific (5 lineages) + internal problem + aspirational identity; Grunt Test scored | Positioning or pitch prep | Lineage + ICP profile | Tested one-liner | New | now |
| `sniped-three-whys-drill` | Positioning interrogation until visceral emotional core surfaces | Positioning development | Current positioning language | Emotional core statement | New | now |
| `sniped-brand-adjective` | Compressed positioning drill; output: single locked adjective tested against ownable/product-true/vernacular criteria | Before any positioning finalization | Positioning brief | Single locked adjective | New | now |
| `sniped-ideation-volume` | 100+ variant sprint for positioning, caption, DM opener; write-hot-edit-cold cadence | Any copy brainstorm session | Brief or prompt | 100+ variants | New | now |
| `sniped-ganz-dm-builder` | Ganz Self-Us-Now (3-4 sentences); upgrades soft-opener VIB DM | VIB warm DM drafting | Prospect profile | DM draft | New | now |
| `sniped-storybrand-one-liner` | SB7-compliant one-liner (Character+Problem+Plan+Success) + Agreement Plan | Before any external messaging push | Positioning brief | SB7 one-liner + Agreement Plan | New | now |
| `sniped-manifestobuilder` | Apple five-step (tribe/villain/lineage/voice/rallying cry) + name-availability gate | Before major launch or positioning push | Positioning brief | Manifesto draft | New | soon |
| `sniped-case-study-builder` | Problem > methodology > outcome > testimonial > CTA; specificity enforced | Post-delivery case study production | Client engagement record | Case study artifact | New | now |
| `sniped-testimonial-extractor` | 5-question interview (Problem/Frustration/Differentiation/Moment of Realization/Transformed Life) | Post-delivery testimonial request | Client engagement | Testimonial copy + case study card | New | now |
| `sniped-content-sourcing-loop` | Hormozi four-bucket taxonomy (real-time/30-day/far-past/manufactured) | Content planning session | Content history + schedule | Content calendar feed | New | now |
| `sniped-story-case-study` | Smith 6-attribute template (time/place/character/obstacle/goal/events); outputs DM story + LinkedIn case study + Direction Stack chapter seed | Post-shoot case study | Shoot record + client outcome | 3-format case study outputs | New | now |
| `sniped-content-unit-check` | Hook/Retain/Reward + Give:Ask ratio evaluation for Chapter Cards, LinkedIn posts, Cultural Docs | Before any content piece publishes | Draft content | Pass/fail + ratio score | New | now |
| `sniped-awareness-stage-diagnosis` | Diagnoses Schwartz awareness stage (1-5) + sophistication; returns stage-matched rewrite | Before any cold copy writes | Prospect description + copy draft | Stage diagnosis + copy rewrite | New | now |
| `sniped-documentary-authority-audit` | Cultural Doc + Chapter Card captions: validates lineage specificity (names, locations, communities) vs. generic narrative drift | Before Cultural Doc or Card ships | Caption/copy draft | Pass/fail + specificity report | New | now |
| `sniped-intent-audit` | Does aesthetic serve intent or conceal it? Pass/fail before publish | Before any image or composite ships with caption | Image + caption | Pass/fail + fix | New | now |
| `sniped-testimony-format-check` | 4 criteria: inside-experience voice, specific detail, no savior framing, contradiction allowed | Before any testimonial or Cultural Doc ships | Draft testimony/doc | Pass/fail per criterion | New | now |
| `sniped-lineage-integrity-check` | Gate: inside-lineage documentation or external observation? Ambiguous = block | Before any Cultural Doc, Card, or case study ships | Draft content | Pass/fail + block/proceed directive | New | now |
| `sniped-inversion-audit` | Names dominant regime being inverted; pass/fail + inversion language | Before any positioning or copy publishes | Draft positioning | Inversion statement + pass/fail | New | soon |
| `sniped-em-dash-scan` | Scans all output for em-dashes (U+2014) before any ship; lifetime rule | Before any text output leaves OS | Any text artifact | Clean artifact or flagged violations | Standalone gate (all outputs) | now |

---

### Strategy + Decision

| Name | One-Line Purpose | Trigger | Inputs | Outputs | Extends/Replaces | Priority |
|---|---|---|---|---|---|---|
| `sniped-canonical-truths` | Loads and enforces 12 canonical truths across any OS decision | Session start or major decision | THE_SPINE.md + CANONICAL_TRUTHS.md | Canonical truth checklist | Extends existing sniped-canonical-truths | now |
| `sniped-execution-prioritization` | Ranks active threads by execution ROI; outputs single next action | Session start or decision paralysis | ACTIVE_THREADS.md + STANDING_ORDER | Ranked thread list + single next action | Extends sniped-os-execution-governor | now |
| `sniped-reverse-roadmap` | Decade-vision structural review; compare Year-10 state, check irreversible-mistakes list; output proceed/decline/reframe/defer | Major strategic decision | Decision description + Year-10 state | Proceed/decline/reframe/defer verdict | Extends existing sniped-reverse-roadmap | now |
| `sniped-decide` | Pressure-test any decision against full OS corpus + canonical truths + doctrines | Any threshold decision | Decision description | Decision analysis + recommendation | Extends existing sniped-decide | now |
| `boardroom` | Decision pressure-testing using canon thinkers as multi-expert advisors | High-stakes decisions | Decision description | Multi-expert analysis | Extends existing boardroom | now |
| `challenge` | Stress-test proposition against full OS corpus | Any major claim or strategy | Proposition | Stress-test result + counter-arguments | Extends existing challenge | now |
| `sniped-bad-strategy-audit` | Opportunity cost/gap diagnosis against Rumelt Kernel: diagnosis + guiding policy + coherent action | Before any new strategy or initiative | Proposed strategy | Kernel audit + gap report | New | now |
| `sniped-premortem` | Failure history written 12 months forward; triggers on timeline >30d or budget >500 | Before any commitment >30 days or >$500 | Project/initiative brief | Failure scenarios + mitigations | New | now |
| `sniped-outside-view-forecast` | Flyvbjerg reference-class anchoring before any timeline or budget estimate | Any planning session | Proposed timeline/budget | Reference-class-anchored estimate | New | now |
| `sniped-cognitive-bias-pre-decision-gate` | Pre-decision checklist against 25 Munger misjudgments + 17 CBT distortion patterns | Before major decisions | Decision description | Bias inventory + debiased framing | New | now |
| `sniped-boat-selector` | Structural growth/decline? deepens moat? lineage alignment? go/no-go | Before any new opportunity or lane | Opportunity description | Go/no-go + rationale | New | now |
| `sniped-opportunity-cascade-audit` | Gate: does proposed artifact generate 2+ downstream opportunities? | Before committing resources to any artifact | Proposed artifact or initiative | Cascade count + proceed/block | New | now |
| `sniped-enough-gate` | Checklist before scope expansion: does this increase baseline cost before prior proof? moves goalpost before confirmation? | Before any scope expansion | Proposed expansion | Pass/fail + rationale | New | now |
| `sniped-time-horizon-lock` | Explicit time-horizon declaration before any decision; prevents time-mismatch behavior | Before any strategic commitment | Decision description | Time-horizon declaration + pass/fail | New | now |
| `sniped-formlessness-check` | Pre-commitment gate: reversible? closes optionality? hands competitors fixed target? | Before any public commitment | Proposed commitment | Pass/fail + optionality analysis | New | now |
| `sniped-victory-stop` | Post-win checklist: overstepped original objective? acting on momentum not plan? | After any major win | Win description + original objective | Pass/fail + consolidate/stop directive | New | now |
| `sniped-culminating-point-audit` | Scene-depth vs. returns; deepen vs. transition decision | Quarterly or when lane feels flat | Lane metrics | Deepen/transition verdict | New | soon |
| `sniped-moat-audit` | Quarterly per-lane moat-widening vs. -narrowing; four institutional-imperative pathologies | Quarterly review | Lane descriptions + metrics | Moat direction per lane + pathology flags | New | soon |
| `sniped-lean-audit` | Monthly revenue tally, conversion %, constraint ID, Mirror Test, capacity compression | Monthly recurring | Revenue + conversion data | Constraint identification + Mirror Test result | Extends existing sniped-lean-audit | now |
| `sniped-monthly-constraint-audit` | Single-constraint ID, last Monday, 60 min; phase trigger gate | Monthly recurring | Current metrics + phase thresholds | Named binding constraint + phase verdict | Extends existing sniped-monthly-constraint-audit | now |
| `sniped-weekly-review` | 8-section template, 11-metric audit, 10-point drift check; SLA table | Weekly recurring | Weekly activity data | Completed review + drift flags | Extends existing sniped-weekly-review | now |
| `sniped-monday-cockpit` | 3 outcomes + cadence lock; no new strategy on Monday | Every Monday session | STANDING_ORDER + NEXT_ACTION | Weekly 3-outcome list + cadence confirmation | Extends existing sniped-monday-cockpit | now |
| `sniped-goal-set` | 90-min, three-goal max, hierarchy trace, three-scenario test, red-flag gate | Quarterly planning | Current state + OS direction | Three-goal card + red-flag inventory | New | now |
| `sniped-four-us-audit` | Score lane against 4 Us + 3D defensibility; breakthrough/viable/weak verdict | Before committing to any new lane | Lane description | 4U score + defensibility verdict | New | soon |
| `sniped-seven-thiel-audit` | Thiel 7-question stress-test (Engineering/Timing/Monopoly/People/Distribution/Durability/Secret) for go/no-go | Before any major lane commitment | Lane or initiative description | 7-question verdict | New | soon |
| `sniped-chasm-audit` | Moore 4-question showstopper before any ICP expansion | Before ICP expansion | Expansion proposal | 4-question verdict | New | soon |
| `sniped-canada-principle-audit` | 5-gate moat-dilution test before any new lane executes | Before new lane activation | Lane proposal | Pass/fail per gate | New | soon |
| `sniped-positioning-diagnostic` | Decision tree: fast yes+no = raise price / hesitant = fix positioning / no replies = fix targeting / awkward calls = fix structure | After any outreach or sales signal batch | Signal data | Named diagnosis + fix directive | New | now |
| `sniped-positioning-audit` | Dunford 6-component audit (competitive alternatives, unique attributes, value+proof, target characteristics, market category, optional trends) | Every 6 months | All positioning artifacts | Gap report + rewrite priorities | New | soon |
| `sniped-positioning-ceiling-audit` | Periodic audit of brand language vs. TAM ceiling risk; candidate reframes, larger-category options | Before any major positioning push | Current positioning language | Ceiling analysis + reframe candidates | New | later |
| `sniped-market-evaluation-scorecard` | 10-factor go/no-go: <50 walk, 50-75 mitigate, 75+ commit | Before any new market or vertical entry | Market description | Score + verdict | New | soon |
| `sniped-strategic-implications` | 10 corpus-validated decision frames; chassis-level decisions only | Major strategic choice | Decision description | Validated implication set | Extends existing sniped-strategic-implications | now |
| `sniped-operator-plan` | Weekly operator planning pulling Calendar + STANDING_ORDER + NEXT_ACTION | Weekly planning session | Calendar + OS state | Weekly operator plan | Extends existing sniped-operator-plan | now |
| `sniped-direction-stack` | Direction Stack diagnostic mandatory; conversation not form, no proxy | On-set or VIB discovery | Subject + context | Direction Stack protocol output | Extends existing sniped-direction-stack | now |
| `os-engagement` | Full-OS-read + distill discipline; 2,361 sources; coverage tracking | Major OS synthesis request | Source inventory | Coverage report + distilled doctrine | Extends existing os-engagement | now |
| `sniped-stuck-router` | 3-question diagnostic (capacity/productive avoidance/architecture temptation); hard rule: pick one door, run it | When scattered, stalled, or re-strategizing | Current state description | Single door diagnosis + action directive | Extends existing sniped-stuck-router | now |
| `sniped-execution-governor` | 12-step runtime dispatch, session-start/end protocol, 24 anti-patterns, 9 empire lanes | Session start | STANDING_ORDER + CURRENT_STATE | Dispatched next action | Extends existing sniped-os-execution-governor | now |
| `staging-plan` | Scan source folder, categorize by extension, propose chapter slots, flag overlaps, sequence mini-batches | Before any batch extraction or corpus update | Source folder | Staging plan + mini-batch sequence | Extends existing staging-plan | now |
| `source-inventory` | Track and categorize all OS source documents; gap tracking, canonical routing | Corpus maintenance | OS source folder | Source inventory + gap register | Extends existing source-inventory | now |
| `batch-extraction` | DOCX/EPUB/PDF/MOBI to normalized plaintext; 7-step locked SOP | Corpus ingestion | Source files | JSONL batches | Extends existing batch-extraction | now |
| `jsonl-validation` | Verify JSONL line count = chunk count = header count; schema complete; chunk_id unique | Post-extraction | JSONL files | Validation report + halt/proceed directive | Extends existing jsonl-validation | now |
| `master-consolidation` | Merges batches into MASTER_INDEX; P-tier stratification model | Post-validation | Validated JSONL batches | Updated MASTER_INDEX | Extends existing master-consolidation | now |
| `session-save` | End-of-session memory harvester: updates CURRENT_STATE.md, ACTIVE_THREADS.md, SESSION_LOG.md, memory files | Session end | Session outputs + decisions | Updated OS state files | Extends existing session-save | now |
| `operator-review` | SNIPED OS applied to outside situation or inbound proposal | Inbound opportunity or outside request | Situation description | OS-grounded analysis + recommendation | Extends existing operator-review | now |
| `sniped-project-ingestion` | Raw export immutable; no OS mutation without BJ approval; 8-field BRIEF_TEMPLATE validation + 3-gate checkboxes | New project intake | Project materials | Intake record + gate verdicts | Extends existing sniped-project-ingestion | now |
| `sniped-skill-intake` | 5-bucket classification: activate-now/convert-to-skill/reference-only/defer-until-tool/reject-bloat | Any new skill or workflow candidate | Candidate skill description | Classified bucket + action directive | Extends existing sniped-skill-intake | now |
| `sniped-ai-agent-architecture-wat` | Post-proof trigger, 6-9mo after 5+ client cycles; W-A-T decision | Phase B+ planning | Current proof state | WAT architecture recommendation | New | later |
| `sniped-proof-loop-review` | Weekly proof review; H1-H6 framework, Keep/Kill/Iterate, anti-hiding check | Weekly recurring | Proof log entries | Proof review output + next loop action | Extends existing sniped-proof-loop-review | now |
| `proof-log-validator` | Enforce REAL PROOF (money + named outcome + access) vs. FAKE INTEREST (praise, "send info," no door opened) | Any proof log entry | Proof log entry | Valid/invalid classification | Extends existing proof-log-validator | now |

---

### Pricing + Commercial

| Name | One-Line Purpose | Trigger | Inputs | Outputs | Extends/Replaces | Priority |
|---|---|---|---|---|---|---|
| `sniped-pricing-decision` | 3-option architecture, $1,500 floor hard, trade scope not price | Any pricing conversation | Scope + client context | 3-tier proposal structure | Extends existing sniped-pricing-decision | now |
| `sniped-choice-of-yeses-builder` | 3-option proposals using Weiss Column 3/distinct value-jump architecture; 10:1 ROI floor | Proposal creation | Client objectives + budget signals | 3-option proposal | New | now |
| `sniped-pricing-proposal` | 3-option proposal builder: anchor/target/floor + bundled value framing + round numbers + risk-transfer language | Any proposal | Scope + client profile | Formatted proposal | New | now |
| `sniped-pricing-defense-script` | Collapsing-middle rebuttal; floor non-negotiable | Pricing objection | Objection type | Defense script | Extends existing sniped-pricing-defense-script | now |
| `sniped-value-conversation` | Enns 4-step value conversation: Three-Year Question, desired future state, metrics, value | Pre-proposal call | Client context | Value conversation transcript + anchors | New | now |
| `sniped-anchor-audit` | Evaluates pricing conversations for anchor position, oral-price sequencing, senior decision-maker reach | Post-conversation review | Conversation notes | Anchor assessment + next action | New | now |
| `sniped-offer-architect` | Hormozi 5-step: problem catalog, solution list, delivery vehicle matrix, trim/stack, bundle naming via MAGIC formula, guarantee structure | New offer creation | Offer brief | Complete offer architecture | New | now |
| `sniped-offer-validation` | 3-5 day sprint (LinkedIn traction, community thread count, competitor gap mining, case study language) before production entry | Before any new offer launches | Offer concept | Validation sprint output + go/no-go | New | now |
| `sniped-guarantee-builder` | 14-type guarantee taxonomy with conditional clause + conversion-lift-vs-refund-rate math check | Offer finalization | Offer description | Guarantee clause | New | now |
| `sniped-mvpr-launch-gate` | Minimum-viable-profit gate before any new offering; cost, price floor, time-to-first-dollar | Before any new offer activates | Offer description | MVPr assessment + pass/fail | New | now |
| `sniped-reset-activation` | VIB diagnostic drafting, 3-5 shoot cap + 14-day cap management | Reset campaign activation | Pipeline state | Reset campaign SOP | Extends existing sniped-cash-now | now |
| `sniped-reset-to-brand-system` | Wedge-to-ladder distinction (Reset/Operator Kit/Brand System); VIB vs. warm-creatives split | Upsell planning | Client history + engagement | Ladder routing directive | Extends existing sniped-reset-to-brand-system | now |
| `sniped-money-urgency` | Speed-lever routing (escrow > warm lead > VIB queue > cold fresh); blocks discount triggers; $1,500 floor holds | Cash urgency situation | Current pipeline state | Speed-lever ranked action list | Extends existing sniped-money-urgency | now |
| `sniped-post-shoot-same-day` | SD to SSD to HDD to Lightroom to Notion before laptop closes | Post-shoot | Shoot output | Completed same-day protocol | Extends existing sniped-post-shoot-same-day | now |

---

### Production Operations + Workflow

| Name | One-Line Purpose | Trigger | Inputs | Outputs | Extends/Replaces | Priority |
|---|---|---|---|---|---|---|
| `sniped-production-os` | Folder lock, naming lock, storage tiering Hot/Warm/Cold, 5-pass cull, 12-15 min Hero cap | Any production session | Shoot output | Organized production folder + cull output | Extends existing sniped-production-os | now |
| `sniped-chapter-rollout` | Subject intake, post sequence + breathing calendar + HERO/Card briefs | Chapter launch planning | Subject profile + chapter assignment | Chapter rollout plan | Extends existing sniped-chapter-rollout | now |
| `sniped-chapter-card-audit` | Neumeier 5-anchor evaluation (Distinctiveness/Relevance/Memorability/Extendibility/Depth) | Before any Chapter Card ships | Card draft | 5-anchor score + pass/fail | New | now |
| `sniped-card-production` | Source image, Figma Card variant spec (masthead, wordmark, saturation params); 3-5 min/card | Card production session | Hero image + chapter assignment | B&W Card variants | Extends existing sniped-card-production | now |
| `sniped-rollout-executor` | Harvest sheet to grid layout to calendar; grid sequence rules (warm-glam alt, color motif beat, no 3-adjacent-blob) | Post-chapter-production | Completed chapter assets | Grid layout + content calendar | Extends existing sniped-rollout-executor | now |
| `sniped-audience-engine-phase-1` | Deploy first Reset outputs, assemble carousel, audit Phase 1 anti-patterns, decide weekly content | Phase 1 activation | Reset output + Chapter 1 assets | Phase 1 content plan | Extends existing sniped-audience-engine-phase-1 | now |
| `sniped-audience-multiplier` | 1-shoot-to-5-outputs routing + platform variant logic | Post-shoot content planning | Shoot assets | 5-output content plan | Extends existing sniped-audience-multiplier | now |
| `sniped-cultural-documentation-cadence` | Monthly 30-50 frame shoot + carousel + essay; quarterly thematic mini-essay; annual archive review; 5 ecosystems, 10-year horizon | Monthly/quarterly cadence | Lineage targets + schedule | Cultural Doc production plan | Extends existing sniped-cultural-documentation-cadence | now |
| `sniped-chapter-intake-routing` | Mode 1-4 decision (90-sec DM 80% default/expanded DM/13-question form/silent); three-word-to-environment mapping | New chapter subject inquiry | Inquiry type + context | Routing decision + intake mode | Extends existing sniped-chapter-intake-routing | now |
| `sniped-concept-intake` | 4-question filter (proof fit/register/lineage/environment); brief or vault routing | New concept or shoot idea | Concept description | Route: brief or vault | Extends existing sniped-concept-intake | now |
| `sniped-event-filter` | 4-question accept/decline; Day 0-30 post-event cadence | Event invitation | Event description | Accept/decline + post-event cadence | Extends existing sniped-event-filter | now |
| `sniped-business-idea-gate` | 3-question filter; lane classification; vault parking with reopen condition | New business idea | Idea description | Lane classification + vault/activate directive | Extends existing sniped-business-idea-gate | now |
| `sniped-product-idea-gate` | 5-step proof order check; seduction taxonomy; moat-dilution routing; /challenge gate | New product idea | Idea description | Proof-order position + route directive | Extends existing sniped-product-idea-gate | now |
| `sniped-acquisition-gate` | 4-question filter (refuse-list/saturation audit/Gap Map tier fit/proof-loop dependency) | Any new tool, channel, hire, or lane proposal | Proposal description | Pass/fail per gate | Extends existing sniped-acquisition-gate | now |
| `sniped-notion-crm-phase-1` | 9-step Phase 1 build (DBs 1-2 activation, Activities + Projects, 7/14/30-day gates) | CRM setup | Schema requirements | CRM build SOP | Extends existing sniped-notion-crm-phase-1 | now |
| `sniped-internal-tightness-tracker` | Dashboard mapping 10 required operating systems to completion + auto-flag blockers | Quarterly OS review | OS component inventory | Completion dashboard + blocker list | Extends existing sniped-internal-tightness-tracker | now |
| `sniped-ai-visibility-audit` | Domain baseline, Google Overviews/ChatGPT/Perplexity/Claude/Copilot citation report + schema markup gaps + monthly tracking | Monthly | Domain + OS content inventory | AI citation report + gap list | Extends existing sniped-ai-visibility-audit | soon |
| `sniped-article` | 10-step GEO/AEO engine: Answer Block, question H2s, claim-level evidence, FAQ schema | Article or Cultural Doc production | Topic + outline | Publication-ready article | Extends existing sniped-article | soon |
| `sniped-schema-markup-implementation` | Case study pages, citation-amplification loop, AI search indexing | Case study page build | Case study content | Schema-marked-up HTML | New | soon |
| `sniped-photoshop-source-audit` | 6-author whitelist + 5 auto-reject pattern gates as intake audit | Before any PS or LR tutorial resource is consumed | Tutorial source | Whitelist pass/fail + consume/reject | Extends existing sniped-photoshop-source-audit | now |
| `sniped-reject-gates-masking` | Binary reject gate for Photoshop masking techniques; 5 global locked anti-patterns | Before any masking workflow | Technique description | Approve/reject verdict | New | soon |
| `sniped-generative-expand` | Generative Fill expand protocol: target region, empty-prompt-first, 5 checkpoints, 6-attempt cap | Any Generative Fill session | Source image + fill region | Approved fill or escalation | New | soon |
| `sniped-pixieset-gallery-ops` | CSV staging, collection naming, sRGB export gate, PIN config, Order Delay 24-hr hold, boutique packaging, WHCC store routing | Gallery delivery | Shoot selects + client record | Pixieset gallery + delivery email | Extends existing sniped-pixieset-gallery | now |
| `sniped-carrd-conversion-surface` | Problem-Method-Offer order, 60-sec booking target | Carrd site review or update | Site draft | Conversion-optimized site copy | Extends existing sniped-carrd-conversion-surface | now |
| `sniped-baseplate-carrd-launch` | 10-section checklist, 11 scroll-sections, Calendly setup, mobile check, legal footer | Carrd site launch | Site content | Launch checklist + compliance report | Extends existing sniped-baseplate-carrd-launch | soon |
| `sniped-capability-dossier` | 12 master components (C1-C12), 8-page assembly, type system, palette, watermark v2+ | Capability dossier production | Client engagement records | Dossier PDF | Extends existing sniped-capability-dossier | soon |
| `sniped-outreach-dossier-pilot` | Week 1 bootstrap through Week 4 outreach sprint with call runbook + proof-log discipline | BASEPLATE pilot outreach | ICP list + dossier | Outreach sprint plan | Extends existing sniped-outreach-dossier-pilot | soon |
| `sniped-kots-sponsor-sequence` | Tier structure, inventory catalog, outreach flow, renewal recap | KOTS sponsorship campaign | Sponsor targets + tiers | Sponsor outreach + renewal SOP | Extends existing sniped-kots-sponsor-sequence | soon |
| `sniped-kots-institutional-reframe` | Institutional vs. founder frame; program-sourced stats; governance clarification | KOTS positioning or pitch | KOTS context | Institutional framing brief | Extends existing sniped-kots-institutional-reframe | soon |
| `heel-finishing-spec` | Acrylic heel finish (platform glass, refraction, specular edges, contact shadow, toe correction, cast shadow, re-grain); ~15 min | Brand System retouching with shoe detail | Composite or hero with visible heel | Finished heel layer in PSD | New | soon |
| `sniped-naming-evaluation` | 10-criterion scoring, tie-breaker on legibility/register/credibility/durability/phonetics | Any naming decision | Name candidates | Scored ranking + winner | Extends existing sniped-naming-evaluation | now |
| `sniped-naming-sprint` | Brief-lock > 100+ candidates > SMILE filter > SCRATCH check > trademark DIY screen | Naming project | Naming brief | Top candidate list + trademark check | Extends sniped-naming-evaluation | now |

---

### Intelligence + Research

| Name | One-Line Purpose | Trigger | Inputs | Outputs | Extends/Replaces | Priority |
|---|---|---|---|---|---|---|
| `sniped-trust-equation` | T=(C+R+I)/S per client; diagnose weakest variable; S-reduction actions | Any client or outreach relationship review | Relationship history | Trust score + weakest-variable diagnosis | Extends existing sniped-trust-equation | now |
| `sniped-trust-mechanics` | 8 trust signals, 5 anti-patterns, 3 authority loops | Authority or positioning design | Context description | Trust signal inventory + anti-pattern scan | Extends existing sniped-trust-mechanics | now |
| `sniped-status-psychology` | De Botton/Simler/Hanson: selectivity > availability; prestige vs. dominance | Pricing, copy, or positioning decision | Context description | Status signal recommendations | Extends existing sniped-status-psychology | now |
| `sniped-photo-theory` | Berger/Dyer: taken vs. made images; ambiguity of the photograph; anti-AI defense | Direction Stack methodology framing, captions, cultural doc | Context description | Photo-theory framing copy | Extends existing sniped-photo-theory | now |
| `sniped-wwp-positioning` | 12 Blair Enns proclamations; refusal is positioning | Positioning or sales-flow review | Context description | Proclamation checklist + violation flags | Extends existing sniped-wwp-positioning | now |
| `sniped-hit-mechanics` | 6 distribution mechanics (exposure/MAYA/story/broadcast/clusters/prophecy) | Content distribution planning | Content plan | Distribution mechanic selection | Extends existing sniped-hit-mechanics | soon |
| `sniped-perennial-seller` | Making work that lasts decades; Iron Maiden patience | Direction Stack book launch or product planning | Launch plan | Long-horizon validation | Extends existing sniped-perennial-seller | soon |
| `sniped-hospitality-layer` | Service = what was promised; hospitality = more than expected | Any client touchpoint design | Touchpoint description | Hospitality move inventory | Extends existing sniped-hospitality-layer | now |
| `sniped-leverage-logic` | Naval: 3 forms (labor/capital/code+media); question: should we add this surface or hire? | Resource allocation decision | Proposed action | Leverage classification + recommendation | Extends existing sniped-leverage-logic | now |
| `sniped-new-luxury` | Trading Up: technical-functional-emotional ladder; collapsing middle | Pricing, ICP refinement, lane positioning | Context description | Ladder analysis + positioning recommendation | Extends existing sniped-new-luxury | soon |
| `sniped-company-of-one` | Jarvis: right-size not scale; resilience over scale | Hire decisions, growth temptations | Proposed action | Scale-or-hold analysis | Extends existing sniped-company-of-one | soon |
| `sniped-blockbuster-strategy` | Elberse: bet big or don't bet; superstar economics | Book launch or named-client strategy decision | Context description | Blockbuster bet analysis | Extends existing sniped-blockbuster-strategy | soon |
| `sniped-analog-premium` | Sax: why analog wins in select categories; anti-AI moat | AI-defense, analog ritual design, physical IP planning | Context description | Analog premium analysis | Extends existing sniped-analog-premium | soon |
| `sniped-canonical-source-map-router` | Classify question into 15 input types; pull canonical sources in priority order | Any OS query requiring source routing | Question description | Source list + priority order | New | soon |
| `deep-research` | Multi-source, fact-checked research report with fan-out web searches and adversarial verification | Deep research request on any topic | Research question | Cited research report | Extends existing deep-research | now |
| `sniped-ai-seo-audit` | Princeton GEO: sourcing +40%, statistics +37%, expert quotes +30%, keyword stuffing -10% | Before any web content or case study publishes | Content draft | AI-SEO compliance report + fixes | New | soon |
| `sniped-ai-image-tool-pick` | Task-to-tool matrix: task nature/identity constraints/output register/speed-ceiling; hard identity gate | Any AI image generation decision | Task description | Tool selection + gate verdict | Extends existing sniped-ai-image-tool-pick | now |
| `sniped-prompt-method-router` | Classify task as LtM/PaS/PoTh; output step sequence; apply constraint-by-count | Any complex AI prompt task | Task description | Method classification + scaffold | New | later |
| `sniped-containment-check` | Suleyman 8-question AI tool gate: use/constrain/avoid verdict | Any new AI tool adoption decision | Tool description + proposed use | Use/constrain/avoid verdict | New | now |

---

### Governance + Integrity

| Name | One-Line Purpose | Trigger | Inputs | Outputs | Extends/Replaces | Priority |
|---|---|---|---|---|---|---|
| `sniped-canonical-truths` | Loads and enforces 12 canonical truths; spine check on any major decision | Session start or major decision | THE_SPINE.md | Canonical truth checklist | Extends existing sniped-canonical-truths | now |
| `sniped-reputation-engine-activation` | 4 access lanes, max 4 free shoots/month, reputation-building framework | Reputation or credibility decision | Context description | Lane selection + activation plan | New | soon |
| `sniped-institutional-proof-path` | LACMA/MOCA/NMAAHC institutional submission path: peer validation > producer lineage > institutional curation | Institutional access planning | Current proof state | Institutional pathway map | New | later |
| `sniped-lineage-gate` | Written from inside 5 lineages or outside? Institutional comfort-speak flag | Before any Cultural Doc, Card, or case study ships | Content draft | Pass/fail + block directive | New | now |
| `sniped-dissemblement-gate` | Gate: sincere or optimized for effect? Honest version required before ship | Before any artifact ships | Draft artifact | Pass/fail + honest version | New | now |
| `sniped-ruling-part-audit` | 5-question daily reset: is ruling part protected? what ornament strips? any decision driven by applause? | Daily session start | Current decisions + context | 5-question results + pass/fail | New | now |
| `sniped-trust-architecture-audit` | Runs Trust Equation, flags intimacy-drift, loyalty-without-judgment, language-drift, self-orientation | Periodic relationship or OS review | Relationship/OS state | Trust audit report | New | soon |
| `sniped-doctrine-audit` | Quarterly handle-suitcase check: lived vs. recited, last-tested date, evidence log | Quarterly recurring | Doctrine inventory | Doctrine health report + stale flags | New | soon |
| `sniped-character-decay-check` | Triggered by major wins; surfaces 3 structural hubris conditions | After any major win | Win description + context | Hubris risk assessment | New | soon |
| `sniped-values-filter` | Pre-collaborator gate: 5-type taxonomy (core-aligned/aspirational/permission-to-play/accidental drift) | Before any collaborator hire or partnership | Collaborator profile | Green/yellow/red classification | New | now |
| `sniped-cosmological-assumption-audit` | Quarterly: identify foundational premises; flag each as interrogated or inherited | Quarterly recurring | Current OS doctrine | Assumption inventory + interrogation flags | New | later |
| `sniped-moral-matrix-audit` | 6-foundation alignment check on any copy or outreach | Before any copy or outreach ships | Draft artifact | Foundation alignment report | New | now |
| `endorsement-due-diligence` | Lineage alignment + public record + controversies + reputational asymmetry pre-co-sign; lifetime gate | Before any public co-sign or collaboration | Collaborator profile | Due-diligence report + proceed/block | New | now |
| `sniped-founders-dilemma-gate` | Pre-structural-decision: Wealth vs. Control/Three Rs alignment/counterparty motivation/dynamic equity | Before any equity, partnership, or structural decision | Decision description | Gate checklist + proceed/block | New | soon |
| `sniped-ip-ownership-audit` | Copyright term, territorial scope, contributor rights pre-deal checklist | Before any partnership or licensing deal | Deal description | IP position report | New | soon |
| `sniped-crisis-protocol` | 4-step capital/reputational crisis response: 90-day cash, liquid assets, counter-narrative, stakeholder contact | Crisis event | Crisis description | Crisis response plan | New | soon |
| `canon-dedup` | Group by semantic stem, rank (Final > v2 > Revised > dated > (N)), quarantine rest; fold into staging-plan checklist | OS corpus deduplication session | Source file inventory | Deduped canonical file list + quarantine list | Extends existing canon-dedup/version-resolution | now |
| `corpus-contradiction-sweep` | Scan for stale tokens (Adobe Portrait, 3 VIBs/week, anti-AI, $3K x 2mo), report every doc still carrying them | Quarterly OS review | OS corpus | Contradiction report + correction list | New | soon |
| `sniped-corpus-retrieve` | MASTER_INDEX route to batch/domain, grep/jq, cite [BATCH_NNN_chunk_NNN]; build only if corpus-citation rate stays 0% | Corpus query | Query description | Retrieved chunks + citations | New | later |
| `sniped-open-loop-check` | Reads CURRENT_STATE + ACTIVE_THREADS + SESSION_LOG; flags 7+ day stale threads | Session start | State files | Stale thread report + next-action prompt | New | now |
| `sniped-algorithm-audit` | Musk Q-D-S-A-A sequence on any SOP; named owners, deletion candidates | Any SOP review | SOP description | Simplified SOP + deletion list | New | soon |
| `sniped-okr-quarterly-set` | 3-5 committed OKRs + aspirational carry-forwards; paired KR generation; single-owner assignment | Quarterly planning | Goals + current state | OKR card | New | soon |
| `sniped-okr-weekly-check-in` | 0.0-1.0 scoring; continue/update/start/stop; surfaces reds | Weekly recurring | OKR card | Weekly check-in report | New | soon |

---

### Priority Legend

- **now**: Build this sprint; active blocking gap or currently invokable functionality needed
- **soon**: Build next 30-90 days; high leverage, currently routed manually
- **later**: Build post-proof or post-Phase B trigger; valuable but not blocking current motion