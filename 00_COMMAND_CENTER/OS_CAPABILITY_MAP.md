# SNIPED OS CAPABILITY MAP (harvested from 166 doctrine docs, 2026-06-04)

> Every read made the OS sharper. Possibility engine: capability grows, identity stays open.

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

---

## CONNECTORS

### Airtable

Airtable operates as the primary operational database where Notion hits its ceilings (volume, relational complexity, or multi-user scale), and as the preferred low-latency tracking layer for production workflows.

**Shoot + Production**
- Shoot folder naming scaffold: date + client + TYPE, 9-subfolder root, stamped naming convention enforced at session start [Batches 001, 021]
- Casting ledger: model name, confirmation status, strike count, wardrobe photo gate, MUA confirm, 24-hr timer flag; Zapier trigger fires on non-confirm [Casting Doctrine, B016, docxwave-shelf4]
- Production session logger: environment assignment, cull tier, edit register, lineage tags per shoot [BW2s1, docxwave-shelf4]
- Composite environment rotation log: read before Higgsfield dispatch, write after; collision checklist per chapter [B016, Batch 010]
- Postmortem table: Shoot Date / Delivery Date / Top 5 Repeat / Top 5 Stop / Execution Velocity [shelf10, B017]
- Shoot session log: environment, composition schema, Avedon gate fields, presence-reject fields [shelf10, reread series]
- Archive re-edit batch manager: frame count / audit score / re-edit flag / Evoto flag / site rebuild threshold [docxwave-shelf4]
- Beat battle production session log per chapter [BW2s1]

**CRM + Outreach**
- Primary CRM until Notion proves daily use by Day 30; overflow CRM above Notion 200-record/5-user limit [Batches 002, 013]
- CRM schema from 2_Assistant_SOP: Name / Company / Role / LinkedIn URL / Criteria Met / Visual Gap / Trigger Event / Tier / Status / Source / Owner / Date Added [docxwave-shelf1]
- ICP waterfall table: attorney and founder lead tiers with Instantly campaign routing [docxwave-shelf3b]
- On-chain census / proof ledger: 8-lead visual-gap tracker, trigger dates, engagement metrics, auto-sync Gmail / LinkedIn / Instantly [shelf8]
- VIB warm-signal CRM: Name / Tier / Signal Source / Last Touch / Engagement Ring Member / Gain-Pain Score [S21]
- Converted spy tracker: contacts by intel value, referral count, scenes opened, hub proximity [shelf17]
- Tier 0 sneezer register: contact, impression status, evangelist score, story/tool provided, touchpoint date [Bf2-shelf04]
- ICP pain-density ranker: problems x impact severity, A/B/C/D tier assignment [shelf19]
- Airtable trigger watch: LinkedIn events (funding, promotion, relocation, rebrand, IPO) routing to VIB queue [BW2s1]
- Scene-density tracker: LA clusters, crew intel, founder touchpoints, repeat booking rate, warm intro rate [reread series, A1]
- Founder cluster mapping, visual positioning deficit map [BW2s12]
- Network node CRM: collaborators, vendors, lineage connectors; node type / interaction cadence / opportunity-cascade field [Bf1-shelf07]
- Zero-rate dashboard: weekly anti-network-experience checklist (casting no-shows, unanswered DMs, abandoned shoots, dead threads) [A3-shelf12]
- Airtable + Monday.com + Zapier: casting and production scheduler feeding into Instantly confirmation cadence [shelf11]

**Operations + Metrics**
- Monday scoreboard auto-export: 8-metric weekly dashboard, daily volumes [docxwave-shelf1]
- Input metrics dashboard: post cadence / casting confirm rate / case study completion / VIB DM response rate [BW1s2b]
- Lead-gen benchmark tracker: reply / accept / convert ratios per channel [BW1s3]
- Superforecasting engagement predictions per environment, Brier score updates [B017]
- Cycle Temperature Dashboard: 20+ dimension toggle, pre-major-decision gate [shelf10]
- Bottleneck-Physics Planning: production bottleneck inventory, max sustainable output per window [shelf5]
- Content Multiplier Tracker: concept-to-format repurposing pipeline [docxwave-shelf4]
- Owner-earnings tracker: capital deployed / output / moat-widening flag / 5-year rolling [S13]
- OKR database: committed vs. aspirational labels, KR pairs, single named owner per objective [BF1-5]
- Cohort tracking: outreach month, reply rate, close rate, referral yield [shelf13]
- Proof tracker: shoots, posts, DMs, conversions, revenue logged weekly [BF1-1]
- KOTS sponsor / food vendor intake: tiers Community $300 / Sideline $1k / Court $2.5k / Crown $5k [BW1s1]
- KOTS principal revenue share tracking [BW1s1]
- KOTS pilot metrics tracker: attendance / test score delta / teacher retention / revenue share [shelf5]
- Post-delivery 8-step cadence tracker: gallery / hospitality / testimonial / Op Kit trigger [B021]
- Testimonial registry: 5-question form feeding case study archive and Card copy bank [BW2s10]
- Archive re-edit audit: 8-criteria score; 6+ = re-edit candidate, 8+ = deliverable [docxwave-shelf4]
- Lightroom session-specific preset enforcement log (Avedon 60%, Haas 30%, Eggleston monocolor, commercial 80-100%) [B016]
- Licensing Revenue Tracker: composite environments, market mapping, licensing rates by use-scope / territory / exclusivity [shelf3, series_1]

---

### Notion

Notion is the primary OS knowledge layer, production brief surface, client relationship hub, and book/content workspace. The Notion MCP (P1 decision still open for full schema lock) enables live state mutations from Claude Code.

**Production + Creative**
- Direction Stack book chapters x Art Series frames mapping [B016]
- Production brief template: 7-component specs per environment chapter [BW1s4b]
- Direction Stack documentation: Galaxy Model succession-proofing [BW1s1]
- Composite environment rotation spec: 7 environments, collision checklist, environment-to-chapter assignment [B016]
- Visual Structure Bible: Block 7-component spec per environment; each shoot and comp references it [A3-shelf4]
- Posing vocabulary library: named 5-pose baseline, seven-point checklist, mirror-technique coaching language [shelf12]
- Mood board brief library: 5-section brief linked to Midjourney board URL per chapter environment [shelf08]
- Shot-List Generator: posing ladder (5 poses, 10 framings) from intake answers via Google Drive API [shelf11]
- Direction prompt library as linked DB: chapter / lineage / character / prompts / hand-placement [shelf16]

**CRM + Client**
- PARA model import: Projects / Areas / Resources / Archives as live knowledge routing [docxwave-shelf1]
- Notion CRM Phase 1 build: Activities + Projects (DB 1 + DB 2) as primary surface; Zapier fires on state changes [Batch 013]
- Post-delivery state machine: 9-template delivery lifecycle with trigger conditions, Notion state mutations [Batch 014]
- Deal stages database: Pipeline / Deals / Clients / Contacts, with 7-day and 30-day gates [Batch 013]
- Mom Test signal log: per-conversation structured note (3 big questions, signals, commitment, next step) [shelf17]
- VIB DM outreach pipeline and 5-failure-mode rejection log [Batch 012]
- Intelligentsia map: word-makers / role / relationship tier / last touch / co-option opportunity [shelf7]
- Client intake three-conversation template: Kim Scott Life Story / Dreams / 18-Month model [S08]
- Gap Selling discovery notes: 7-gate pipeline format per prospect [shelf19]

**OS + Governance**
- STANDING_ORDER, NEXT_ACTION, CURRENT_STATE, ACTIVE_THREADS, SESSION_LOG as primary OS state surfaces [Batch 002]
- Sacred Cow Registry: non-negotiables + revision triggers [A2-shelf6]
- Doctrine renewal tracking: per-doctrine dated rep log, 10-month threshold [shelf17]
- Doctrine audit dashboard: handle-suitcase check per locked rule [A3-shelf5]
- Trust equation tracker: T = (C+R+I)/S per client, score + S-reduction actions [A3-shelf5]
- Content output matrix: stated output goal per piece before creation [A3-shelf5]
- Offer Sequencing Database: offer ladder, pricing justification, payoff proof, upsell triggers [series_2]
- JTBD Tracker: active job hypotheses, three-layer integration checklist, purpose-brand drift flags [shelf7]
- Lencioni six-question playbook; values taxonomy updated quarterly [B016]
- KOTS tournament infrastructure: roster, booster governance, revenue stack [BW1s2]
- Direction Stack book drafting: AI-generated chapter scaffolds, human voice-layer approval state [shelf8]
- Quarterly OKR visibility alongside CURRENT_STATE [BF1-5]
- Verification gate checklists as database templates: casting / shoot / delivery [A2-shelf18]
- Persona and outreach routing template linked to LinkedIn comment doctrine and Instantly [shelf2]

---

### Zapier (and Make / n8n)

Zapier is the primary automation bridge between SNIPED tools. Make and n8n are secondary depending on workflow complexity. No automation before proof is a standing gate.

**Casting + Production**
- Booking to Calendar sync to MUA confirm to Tier-2 standby alert (Casting Doctrine automation) [BW1s3]
- Pixieset form to Stripe link + Calendly prompt + Gmail intake auto-send [docxwave-shelf1]
- Visual Directive questionnaire: 13 questions, auto-reminder at 3 / 7 / 14 / 21 / 30 days pre-shoot [docxwave-shelf1]
- Zapier: Slack + Airtable for casting 24-hr confirmation timer [BW1s4b]
- Airtable casting trigger for Reset intake (9 CRM fields), tier-2 standby 24-hr escalation, casting form distribution [Batch 001]
- Tally casting call form: conditional-logic Tally to Airtable sync via Zapier webhook [series_5]
- KOTS same-day archive auto-sort [Batch 013]
- Premortem ritual + Google Calendar casting-call add + two-strike auto-flag [B017]

**Outreach + CRM**
- Instantly email sequence: affiliate whisper script auto-send + tracking link [BW2s1]
- Zapier: Ambient Audit follow-up cadence (Kling output / export / LinkedIn search / log / 3-day follow-up via Gmail MCP) [docxwave-shelf3]
- Zapier: Meta Conversions API to Airtable (Messenger / IG DMs / WhatsApp / comments aggregation) [docxwave-shelf3]
- Instantly response to Airtable lead status; OKR table to Notion dashboard [BF1-5]
- Notion CRM state-change trigger: 24-hr post-booking / post-gallery sync to 4 DBs [B020]
- Post-pipeline proof routing [Batch 013]
- Day-7 testimonial sequence + Day-30 state mutation triggers [Batches 005, 014]
- Day-19 conditional send gate: fires only if client opened gallery AND has not purchased upgrade [Batch 014]
- Zapier: Gumroad email list upsell sequence [docxwave-shelf2]
- Zapier: Pixieset + Stripe integration gateway (proof-earned, not automation-before-proof) [Batch 006]
- n8n: Pixieset + Stripe integration candidate; proof-log entry flagging via webhook + email-to-Notion [Batch 005]
- Make: invoice reminder email sequence, late-payment escalation, milestone booking to invoice drop [series_1]
- IFTTT / Zapier: Visual Directive form triggers Pixieset reminders [docxwave-shelf1]

**Content + Distribution**
- Zapier: Threads + Instagram HypeFury dual-post flow [docxwave-shelf4]
- Kling + Topaz Video AI: Image / Video / Upscale batch orchestration via Zapier or Make [docxwave-shelf5]
- Zapier: Porkbun DNS health checks + renewal reminders [docxwave-shelf3]

---

### Adobe for Creativity (Photoshop, Lightroom, Firefly)

Adobe tools handle image physics, color science, identity-layer retouching, and selective generative work. The Firefly / Generative Fill scope is tightly constrained; identity-layer AI manipulation is a hard refusal.

**Photoshop**
- Photoshop Generative Fill (Path A): background fill, remove-people, environment extension; 6-attempt cap before escalation [Batches 002, 011, 012]
- Path A Reference Image sub-workflow now quality-viable for in-Photoshop compositing [Batch 011-ext]
- Photoshop 27.6 Harmonize feature: auto skin tone, lighting, shadow, reflection matching in composites [series_3]
- Photoshop Rotate Object: subject re-orientation without quality loss [series_3]
- Photoshop Distraction Removal: poles, barriers, potholes, urban element cleanup [series_3]
- AI layer naming and cleanup automation: semantic renaming + empty layer removal [series_3]
- Camera Raw Filter as unified final grading pass on smart object [series_3]
- Composite modular 6-part workflow SOP; non-destructive layer architecture mandatory [series_3, reread series]
- Heel-finishing spec: 15-minute acrylic heel finish (platform glass, refraction, specular edges, contact shadow) [Batch 013]
- Skin-drift numeric test: RGB interior body alpha-eroded 25px check between composite approval and platform mastering [Batch 013]
- Grade.py color base (Step 2) before AI masking (Step 3); 18-frame TEST RUN before rollout [Batch 013]

**Lightroom**
- Adobe Neutral as single import baseline; Lane A vs. Lane B divergence downstream at tone curve and HSL [Batch 011-ext]
- 9 master presets (Avedon / Eggleston / Leibovitz / Shore / Herzog / Frank / Meyerowitz / Haas / Iturbide); retouch depth is frame-driven [Batch 011]
- 16-rails export chain with 9 export presets as locked single SOP [B021]
- Lightroom masking is the creative decision point; batch ops are pre-flight cleanup only [Batch 015]
- Lane A (Editorial) and Lane B (Product) saved as preset labels with color-label tagging at cull time [Batch 015]
- LUT export and branded preset distribution as revenue surface candidate [series_3]
- Evoto round-trip: LR Classic to TIFF to Evoto to TIFF ProPhoto RGB 16-bit back to LR overwrite [shelf5, shelf13]

**Firefly**
- Approved use cases: background fill, remove-people, text-to-template layouts [Batch 002]
- Empty-prompt-first reverses Firefly default: context-aware fill dominates over verbose prompts [Batch 012]
- Custom Model training per composite environment: 7 environments as seed sets [docxwave-shelf1]
- Moodboard pre-viz: S15-25 weight for photorealism, 7 environment moodboards [docxwave-shelf4]
- Firefly + Nano Banana Pro: 2K output + auto-upscale; ALVIS TEXT-TO-IMAGE formula pipeline [shelf5]
- Direct-prompt Firefly deprecated; use Path A (Photoshop Generative Fill with reference image) or Path B (Higgsfield / Seedream / Nano Banana Pro) [Batch 011-ext]
- C2PA / Content Credentials: stamp every Firefly output with tamper-evident metadata as anti-AI defensibility marker [docxwave-shelf1]
- Adobe MCP (mcp__claude_ai_Adobe_for_creativity): active and authed; route composite background generation and environment cleanup through MCP calls where available [Batch 002]

**Workflow Routing**
- Firefly via Photoshop Generative Fill = Path A (default for in-Photoshop compositing); Higgsfield / Seedream / Nano Banana Pro = Path B (better register for external plate generation) [Batch 011-ext]
- Adobe for environment generation and cleanup; identity layer stays manual [NEWFILES, series_3]
- Lightroom preset metadata layer: JSON export candidate for pipeline routing automation [Batch 015]

---

### Figma

Figma handles VIB card design, composite environment specs, brand system visual components, and Direction Stack visual grammar. All Figma work routes through official mcp__plugin_figma_figma__* and the figma:figma-use skill; community forks rejected.

**Card + Brand System**
- VIB card generation: 1920x1280, #1A1A1A background; sniped-card-production routing [Batch 002]
- Design file: figma.com/design/AiMtRfT8W33yZRf4khjnds (active production file) [Batch 002]
- Clone BASEPLATE Dossier v1 Figma file (p7qWs3AhjTHZa6vDZGoKGE) as Capability Dossier template [Batch 006]
- Dual-register Card system as locked component variants: B&W Card (document) and color HERO (moment) [BW1s3]
- Chapter Card visual system as component library with Freeman placement zones, triangular closure, dominant line-type markers [shelf10, reread series]
- Card Design System: two templates enforcing Freeman display-intent doctrine [S12]
- Pricing Proposal Template: 3-tier variant system, PDF + Loom link export [series_2]

**Composite + Production**
- Composite Environment Rotation v1 reference library: 7 environments, collision checklist, per-environment reference imagery, color palette, lighting direction [B016]
- Block visual spec (space type, depth cues, linear motif, tonal range, color scheme, shape) per named environment [A3-shelf4]
- Brand token automation: train Claude on monochromatic discipline, restraint, clinical retouch, rim light [docxwave-shelf4b]
- Direction Stack visual grammar system: Block's 7 visual components + contrast / affinity doctrine [Batch 004]

**Operations + Web**
- Living org chart: current vs. target positions, Gerber 9-position structure [S11]
- Scene-cluster relationship map: nodes = people, edges = connection type, color = tier [A2-shelf18]
- Post-shortlist naming mockups: business card + product context templates [S19]
- Center of Gravity visual map: cluster nodes + trust-conduit lines + Schwerpunkt circled [S20]
- Figma-to-Claude-Code-to-Vercel pipeline: planner-mode markdown guard; Sonnet 4+ required [shelf13]
- Commander's Intent cascade one-pager per chapter [B1-shelf03]

---

### Instantly

Instantly is the cold-email platform locked for lead generation only. Admin (Ren) owns execution; Bryce owns copy, strategy, and all customer-facing decisions.

**Infrastructure**
- 5 rotating mailboxes, 50/day max send (ramp: 15 to 25 to 35 to 50) [docxwave-shelf1]
- Custom tracking domain required; slow-ramp ON; warm-up 50-70% reply rate target [docxwave-shelf1]
- Domain separation: snipedmedia.com protected brand domain; cold outreach via variant domain [Cold Email Manifesto, BF1-5]
- DMARC authentication required; bounce rate below 8% before scaling [BF1-5]

**Campaign Routing**
- C1-C3 cold-email campaigns (tech / staffing / specialty subs) [Batches 002, 006, 012]
- Attorney outreach: Variant B frame (reputation gap + trust signal + client attraction), 3-email Day 1 / 3 / 7 rhythm [docxwave-shelf4b]
- Instantly + LinkedIn pre-suasion: search to comment-prime to DM-convert [BW1s2]
- Affiliate drip: 3 nurture to 1 sales, transformation arc narrative [BW2s10]
- Sponsor followup campaign: one-week wait, one followup, tier / date / response tracking [BW1s1]
- VIB outreach batch (50+ contacts in parallel, CSV input) [shelf14]
- Post-delivery reference-building campaign to adjacent pragmatist prospects [reread series]
- Reply triage routing: Interested = send example; Send it = before / after + 2-day follow; Not now = 60-day automation; Cost Q = 2 times not Calendly; Hostile = blacklist [docxwave-shelf1]
- Unibox 3x daily: 9 AM / 1 PM / 5 PM; Ren handles 1-7, escalates ambiguous / hostile / pricing to BJ [Batch 012]
- Speaking-cycle founder sourcing: monitor LA founder events via Super Search + LinkedIn 24-hr sort + event calendar scan [Batch 015]
- Outreach anatomy: hook + compliment + case study + CTA + signature; 4-touch arc Day 0 / 3 / 6 / 9 with breakup email at Day 9 [Cold Email Manifesto, BF1-5]

**Scale Gates**
- 200/day start; validate at 5 audit requests/day before scaling to 500/day [Batch 002]
- Response rate is keystone metric: over 10% = scale cadence; under 10% = fix offer or list; over 20% with 80%+ open rate = add appointment-setter role [BF1-5]
- One copy variant at a time; minimum 150 sends before judging; never test two simultaneously [docxwave-shelf1]
- Pilot batch response rate over 10% required before full-scale deploy [BF1-5]

---

### Higgsfield

Higgsfield is on the Plus plan (1,000 credits, brycedenj@gmail.com). Permission gate applies per generation; cost visibility required before each job. Soul ID is deferred pending explicit operator approval after proof phase.

**Use Cases**
- SNIPED Concept Film pipeline: 4-stage pipeline (research + content plan + generation + Meta Ads schedule) [Batches 007, 008, 012, B019]
- Composite environment plate generation: Higgsfield for background plates and motion cards [B019, reread series]
- Ambient Audit outreach: 5-second animated visual proof for high-volume cold outreach (Higgsfield MCP for volume; manual mock for top-10) [docxwave-shelf1, docxwave-shelf3b]
- Loom production reference visuals: BJ master audio + Higgsfield reference visuals + Descript assembly [Batch 012]
- Soul ID character library: face and outfit locked in Notion, assigned per chapter; 7-environment world rotation; screenshot-as-anchor continuity for multi-shot consistency [docxwave-shelf3b, A2-shelf11]
- Pre-shoot mandatory Higgsfield concept board: 3 frames per chapter, low spend, locked before every shoot [Batch 008]
- Pre-visualization for shoot-day protocol: generate reference composite before shoot day [shelf18]
- Video analysis for competitive intelligence scans [shelf17]
- Virality predictor on Kling motion output before final export [shelf4, docxwave-shelf4]

**Routing Rules**
- Upload-order SOP; batch-size 1 test before 4K upscale [NEWFILES2]
- Per-batch credit gate: not global; decision log required [B019, B020]
- Freakiness factor rejection: filter out commodity AI tells; identity-lock contradicts AI commodity lane [A2-shelf11]
- Higgsfield for background plates + motion; Adobe for identity-layer integration + retouching; Evoto for skin pass only [reread series]
- Finishing layer required: no composite ships without human Photoshop / color / grain pass [A2-shelf11]
- Hard gate on identity: world-building only; never face / body / skin texture [Bf1-shelf07]

---

### Google Drive

Google Drive operates as the primary file archive and document delivery endpoint. Personal Google and admin@snipedmedia.com are temporary bridges; no cross-account file moves; no Drive mutations anchoring personal account as BASEPLATE workspace.

**Production + Delivery**
- Cultural Doc archival: Direction Stack chapters, lineage evidence, case study masters [BW1s2]
- Composite provenance log: each final image tagged AI vs. human layers + authorship metadata, PDF legal record export [shelf3, series_1]
- Shoot log archive: auto-create Drive folder on production day, linked from Notion production page [Bf2-shelf04]
- Direction Stack book manuscript: chapter docs with version history; Notion DB tracks status, environment assignment, lineage alignment [Bf2-shelf02]
- Proof asset folder structure matching 7-tier deployment order [docxwave-shelf1]
- Case study template: Situation / Problem / Solution / Results + auto-refresh reminders, PDF export [series_2]
- PDF case study auto-feed from testimonial + before/after + metrics [BW2s10]
- Composite environment rotation library version-controlled: each environment has Drive folder with approved background plates [shelf17]
- Element library: Kling asset sheets (4-7 angles per character, version-controlled) [C01]
- Google Drive + Figma: Direction Stack V2 before / after frames folder auto-generating Figma asset library [docxwave-shelf3b]
- SketchUp pre-viz exports, mood board PDFs, prop sourcing lists as Drive assets linked from Notion [shelf09]
- Google Drive financials refresh: CAC tracking, billing method, payback window [BW1s4b]
- Franklin-model practice session log [B1-shelf01]
- Scheduled backup endpoint for Command Center docs [Batch 008]
- JSON prompt library: 7 slots, one per environment, versioned, loaded at session start [shelf20]

---

### Gmail

Gmail MCP enables draft creation, label management, thread reads, and send scheduling. Gmail handles VIB warm sequences, post-delivery cadences, and sponsor outreach.

**Outreach + Sequences**
- Authority-interview scheduling + First-Look list sequences [Batch 001]
- VIB outreach drafts + warm-list tagging [Batch 001]
- Sponsor followup: one-week wait, one followup, tier / date / response tracking [BW1s1]
- Tiered journalist + VIB outreach with personalized boutique closures [BW1s4]
- Direction Stack affiliate drip: 3 nurture to 1 sales [BW2s10]
- 5-email warm nurture sequence over 60 days + referral automation [docxwave-shelf2]
- Referral 30-day drip, post-Pixieset delivery trigger [docxwave-shelf3b]
- Recipient-facing transmission framing standard: title + what it is + why receiving, in email body before attachment [S10]
- VIB DM timing: send within 3 days of trigger event window [shelf8]
- Gmail MCP: post-delivery check-in template (30-day, personal, no ask) [S08]
- Maister 11-point client onboarding SOP auto-send on booking trigger [reread series]
- Instantly response triggers Notion CRM record creation via webhook [shelf15]

**Operational Triggers**
- Day-7 testimonial sequence trigger on Reset delivery date [Batch 001]
- Sponsor renewal check-in reminder [Batch 001]
- Pixieset Day 1 confirmation email on booking completion [docxwave-shelf3]
- Post-delivery upsell routing through Pixieset Email Campaigns [A3-shelf12]
- Gmail: Gmail MCP and Google Calendar one-way sync for conflict detection [A3-shelf12]
- Retention protocol trigger: pattern-detection on key collaborator threads for disengagement signals [Bf1-shelf12]
- Angarcion relay cadence for VIB follow-up [A3-shelf12]
- Operator plan reads Gmail and Calendar; auto-fetch on operator-state change [B020]
- Post-meeting follow-up template triggered by meeting-outcome gate result [shelf17]
- After positive VIB response: auto-schedule coffee / call offer via Google Calendar [reread series]

---

### Vercel

Vercel hosts client-facing web properties and Direction Stack digital editions. Vercel skills route through the vercel:* skill family; use Claude Code for implementation.

**Properties**
- Direction Stack book landing page + sneezer asset page: tiered pledge architecture (PDF early access / signed print / cohort session / direction day) [shelf7, Bf2-shelf04]
- BASEPLATE / Carrd one-pager (Week-1 bootstrap): Problem-Method-Offer order, 60-second booking target, Calendly embed [Batches 004, 005, 006]
- Brand System case study portal and multi-entity deployment (SNIPED / KOTS / Direction Stack independently deployable) [reread series]
- Cultural Doc archive as Vercel-hosted, SEO-indexed chapter pages [S15]
- Lead magnet landing page: email capture via vercel:vercel-storage, gated content via vercel:auth [shelf09]
- Weiss Value-Backward Calculator (Google Sheets): input founder outcome, 20:1 ROI floor + uniqueness multiplier + 3-option matrix [BW2s10]
- GA4 + Meta Pixel: RouteAnalytics.jsx + analytics.js for React / Vite site; track page_view / generate_lead / view_case_study / view_portfolio_item before paid spend [shelf15]
- Gumroad (validate at launch) vs. Vercel / Shopify (2k+ email list threshold) [shelf12]

**Implementation Routing**
- Figma-to-Claude-Code-to-Vercel pipeline: planner-mode markdown guard, one screen at a time, Windsurf for 3+ page builds [shelf13]
- Vercel:vercel-storage for email capture; vercel:auth for gated content; vercel:nextjs for site structure [shelf09]
- Lighthouse check (local or Vercel) + copy QA gate before any page ships [docxwave-shelf2]
- Design-delivery-gate (141-point checklist: Lighthouse + axe/pa11y + CLS<0.1 + single h1 + OG + canonical + 320px) [B017]

---

### PDF (Desktop + Delivery)

PDF outputs surface in Capability Dossiers, Capability Dossiers, case studies, and contractual artifacts. PDF is a delivery container, not a platform.

**Dossier + Case Study**
- Capability Dossier: 12 master components (C1-C12), 8-page assembly, type system, palette, watermark v2+ [Batch 006]
- Pixieset + PDF delivery for Dossier [Batch 006]
- Case study PDF: testimonial + before / after + metrics auto-fed from Google Drive template [BW2s10]
- Adobe template for case study PDF production [BW2s10]
- Shot-list PDF for shoot day crew distribution: posing ladder, environment grid, mood board [shelf11]
- Figma Pricing Proposal Template: 3-tier, PDF + Loom link export [series_2]
- Book production spec: written design spec (paper / printing / pacing / caption / cover) before any SNIPED print goes to production [Izis, Shelf 18]
- Composite provenance log: PDF legal record export with AI vs. human layer tags [shelf3]

**Contracts + Legal**
- Model Release Protocol: pre-shoot briefing, physical carbon-copy execution, Easy Release app, California compliance, minor guardian gate [shelf3, series_1]
- HoneyBook: contract + invoice + esign + payment methods bundled [series_1]
- DocuSign / HelloSign: e-signature for contract Sign step [docxwave-shelf1]
- Reset MSA / Op Kit MSA / Collab Agreement: unified AI composite disclosure addendum required before composite-inclusive gallery ships [Batch 013]

---

### Desktop Commander

Desktop Commander enables file system operations, bash execution, and local workflow automation through Claude Code in the SNIPED environment. It routes tasks that cannot go through an MCP or cloud connector.

**Primary Use Cases**
- Corpus batch extraction: DOCX / EPUB / PDF / MOBI to normalized plaintext per locked 7-step SOP [B017]
- JSONL validation: line count / chunk count / header count / unique chunk_id / batch_id consistency / source path resolution / master count verification [Batches 003, 005, 006]
- Source inventory and dedup: canon-pick checklist, version resolution (Final > v2 > Revised > dated > N) [Batch 001]
- rawpy batch develop: CR3 folder + XMP preset + operator gate, 75-85% Lightroom fidelity TIFFs + metadata JSON + integrity log [Batch 010]
- Sent DM artifact aggregation: YYYY-MM-DD_recipient-handle.md files in _sent_dms/ with status field; script aggregates reply rates + conversion rates [Batch 015]
- Session-end file backup: precious layer snapshot (Command Center, skills, memory, corpus chunks) before session close [Batch 008]
- Grade.py execution: rawpy color base before AI masking step [Batch 013]
- Skill file creation and update: .md skill files in .claude/skills/ directory [series_5]
- Claude Code sub-agent routing: Haiku for data-heavy tasks, Opus for synthesis, git worktrees for parallel branches, /loop for recurring tasks [A2-shelf4]
- Claude Co-work Plugin Architecture: pre-flagged docs (casting_call_doctrine, composite_environment_rotation, linkedin_comment_doctrine); parallel sub-agent architecture (10-15 agents, 5-15 tasks each) [shelf5]

**Tool-Routing Within Desktop Commander**
- Skills-sh-finder: mandatory pre-build check against available skills before any custom automation [NEWFILES]
- Swarm-consensus validation: 4+ model routing (OpenRouter) for positioning, Direction Stack refinements, factual checks [NEWFILES]
- Promptimizer: LLM prompt optimization across task / system / image generation contexts [NEWFILES]
- Blender MCP server: Claude Code to Blender Python via TCP port 9876; procedural 7-environment scene generation, Patina AI PBR, batch headless rendering; approximately $8 per environment [NEWFILES]
- Composite environment cost gate: 7 environments per chapter = approximately $56 per full-chapter AI-generated asset set [NEWFILES]

---

### Twilio

Twilio handles SMS-layer confirmation discipline and cast/MUA communication where email cadence is insufficient. Referenced but not yet fully operationalized.

**Use Cases**
- Casting confirmation: Airtable form to SMS reminder via Twilio at 24-hr window [docxwave-shelf5]
- THCPP Push-phase SMS blast simultaneous with email (retainer renewal + intake follow-up cadence) [shelf12]
- Zapier bridge: Twilio fires on Airtable trigger when casting non-confirm threshold reached [docxwave-shelf5]

**Gate**
- Twilio activates only after casting-doctrine cast-confirmation form is in Airtable and Zapier bridge is operational; manual confirmation is fallback until bridge proved [docxwave-shelf5]

---

## TOOL-ROUTING

### Meta-Rule: Tool-First Mandate

Before routing any task manually, run the 11-step Connected Toolchain audit. Manual is the fallback after the audit returns no viable path. TOOLCHAIN_ACTIVATION.md is the single source of truth. Skill discovery via `skills-sh-finder` is mandatory before any custom automation build.

---

### 1. AI Image and Composite Generation

| Task | Tool | When |
|---|---|---|
| Background plate generation (environments) | Higgsfield MCP `generate_image` | Default for world-construction plates; 7-environment rotation; batch-size 1 test before 4K upscale |
| Composite environment brief dispatch | `sniped-rememory-environment-brief` skill + Higgsfield MCP | Before every chapter shoot; Soul ID lock + environment selector |
| Identity-preserving subject generation | Seedream 5.0 Lite (plates) / 4.5 (portraits) / Nano Banana Pro (identity-preserving) | When plate generation requires subject-adjacent work; never for face/body/skin of real subject |
| Celebrity-insert / character consistency | Nano Banana Pro + CRS (Character Reference Sheet) | Multi-shot narrative sequences; CRS generated before any composite session starts |
| Pre-viz moodboard (internal only) | Adobe Firefly (structure reference tab) + Leonardo AI | Pre-shoot alignment only; never delivered or published without "reference" framing |
| Generative fill (backgrounds, props, environment extension) | Adobe Photoshop Generative Fill via Adobe MCP (`image_fill_area`) | Path A default for in-Photoshop compositing; 6-attempt cap before escalation; empty-prompt-first |
| AI background swap (batch) | Evoto Backdrop Changer | Triggers Lineage Doctrine review; studio-register-only scope; non-studio routes to composite |
| Motion / video plate generation | Higgsfield (multi-clip stability) or Kling Omni (dialogue/voice) | Platform selected at project intake based on output requirement |
| Procedural 3D environment rendering | Blender MCP server (headless, deferred job poller) + Patina AI PBR | When photorealistic Brutalist/Industrial/Futurist environments needed; ~$8/environment; pilot one environment first |
| AI tool selection decision | `sniped-ai-image-tool-pick` skill | Any new generation task; routes by task nature, identity constraints, output register, speed ceiling |

Hard gate: AI touches world-construction layer only. Face, body, skin texture of real subjects = refused across all tools, all circumstances.

---

### 2. Compositing and Post-Production

| Task | Tool | When |
|---|---|---|
| Composite assembly (subject + AI background) | Adobe Photoshop (manual) + Adobe MCP for generative steps | After Higgsfield plate approved; Camera Raw Filter as unified final grading pass on smart object |
| Composite QA gate | `composite-master-qa` skill (8-gate QA, 6-axis scorecard) | Mandatory before any client delivery or deck entry; every axis minimum 8/10 |
| Skin retouching, backdrop optimization, frequency separation | Evoto (8-capability deep-edit layer) | After hero selection confirmed; slider range 25-75%; never at 100% |
| Evoto Lightroom round-trip | LR Classic > Evoto > TIFF ProPhoto RGB 16-bit > LR overwrite | Standard pipeline for all client-grade work |
| Color grading and preset application | Adobe Lightroom (16 rails, immutable) | Adobe Neutral as single import baseline; Lane A/Lane B divergence downstream |
| Platform mastering (per surface) | `platform-mastering` skill | Mandatory slot between composite QA and publishing; includes numeric skin-drift RGB test |
| Composite shadow audit | `sniped-composite-shadow-check` skill | Pre-finalization; umbra + penumbra + occlusion + horizon convergence |
| Composite environment selection | 7-environment rotation manifest (Airtable read before dispatch, write after) | Commit dominant line-type first; environment selection is compositional commitment |
| Pre-composite subject gate | `sniped-composite-subject-gate` skill (Protocol 01-06 checklist) | Before any Higgsfield or Adobe queue entry |
| Generative Fill variant selection | 5-checkpoint gate: no seam + tonal match within 5% + no hallucinated objects + no texture loops + maintained DoF | After each generation attempt; 6-attempt cap before escalation |

---

### 3. Image Curation and Editing Workflow

| Task | Tool | When |
|---|---|---|
| 5-pass cull (Reject > Pick > Star > Hero) | Lightroom (manual) | Every shoot; hero retouch precedence 12-15 min each |
| Image quality evaluation | `sniped-image-eval` skill (Freeman Six Qualities) + `photo-qa-gate` skill (8-criterion 1-10 matrix) | Before any image ships to client or social |
| Pre-delivery reject gate | `sniped-sprezzatura-check` + `sniped-over-processing-gate` + `sniped-gesture-audit` + `sniped-color-relationship-check` | Stack in sequence before client delivery |
| Sequence evaluation | `sniped-sequence-review` skill (5-level: individual/pair/series/section/thread) | Before chapter/carousel publication |
| Lightroom preset audit | `sniped-lightroom-preset-audit` skill | Pre-export gate on every hero batch |
| Hero retouch gate | Gate 2 (client pick from proofs) mandatory before hero retouch begins | Proofs at sRGB JPEG 2048 long edge, 70-80 quality |
| Rawpy batch development | `rawpy-batch-develop` skill (Phase 2) | After operator side-by-side review and quality gate approval |
| Archive re-edit selection | 8-criteria scoring (6+ = re-edit candidate, 8+ = deliverable) | 7-year archive re-edit SOP |

---

### 4. Gallery Delivery and Client Communication

| Task | Tool | When |
|---|---|---|
| Client gallery creation and delivery | Pixieset (CSV staging, sRGB export gate, PIN config, Order Delay 24-hr hold) | Standard delivery for all Reset and Op Kit clients |
| Gallery upsell (48-hr window) | Pixieset + Stripe (auto-sync 50/50 payment schedule) | Day-0 v2 delivery; Day-19 conditional send only if client opened gallery and has not purchased upgrade |
| Post-delivery sequence (8-step state machine) | `sniped-post-delivery` skill + Gmail MCP + Notion CRM state mutations | Day-0 delivery, Day-7 testimonial ask, Day-30 Op Kit pitch, Day-45 referral drip trigger |
| Invoice generation | HoneyBook or Pixieset (primary) + Stripe (sub-$1k) + ACH via Pixieset ($3k+) | Branded, line-itemized, explicit calendar date, late-fee stated; never generic QuickBooks output |
| Payment processing | Zelle / bank-transfer / Venmo / PayPal / Square | While EIN legal-name correction is pending; Stripe only after correction live |
| Contract and e-signature | HoneyBook or DocuSign/HelloSign | No contract, no work. Non-negotiable. |
| Model release | Easy Release app + physical carbon copy | Pre-shoot execution; California compliance; minor guardian gate |

---

### 5. CRM and Outreach

| Task | Tool | When |
|---|---|---|
| Primary CRM (daily use) | Notion (DB 1 + DB 2 Activities + Projects) | Standard; Airtable overflow above 200-record limit or when Notion 30-day daily-use gate fails |
| ICP lead sourcing | Super Search + Airtable (weekly 30-lead target, 4-hard-criteria filter) | 4-of-4 gate: LA-based + active poster + visual gap + revenue/funding signal |
| Cold email outreach | Instantly (5 rotating accounts, 50/day max ramp, variant domain cold.snipedmedia.com) | After ICP profiling complete; 3-email sequence max; Day 0/3/6/9 follow-up |
| LinkedIn comment warming | Manual (5-10 comments/day, Tier 0 CRM founders only, "LA founder" past 24hr sort) | Pre-DM warm-up; comment before VIB DM; not tool-automatable at this stage |
| VIB DM drafting | `sniped-vib-outreach` skill + `sniped-vib-dm-sequence` skill (Voss mirror + label + pause) + Gmail MCP or manual LinkedIn | After thumbscrew map profiled; protocol number selected before DM ships |
| Trigger-event monitoring | Super Search + LinkedIn Sales Navigator (job-change 90-day filter) + Google Alerts + CrunchBase | Daily scan; 5-10 warm targets ranked; outreach only within 48-hr trigger window for LA-based ICP |
| Outreach sequence management | `sniped-outreach-sequence` skill + `sniped-follow-up-sequence` skill + Instantly (automation) | Standard 4-touch arc (Day 0/3/6/9 breakup); reply triage 3x daily (9AM/1PM/5PM) via Unibox |
| Discovery call prep and execution | `sniped-discovery-to-close` skill + `sniped-discovery-call-script` skill + `sniped-mom-test-intake` skill | 15-min diagnostic call structure; 9-step flow; objection handlers; same-day follow-up |
| Post-call CRM logging | Notion MCP state mutation + Airtable proof log entry | Every send/reply/call/objection/paid outcome logged; REAL PROOF = money committed or access granted |
| Referral activation | `sniped-referral-activation-loop` skill + Gmail MCP (Day-45 trigger) | After testimonial received AND photos deployed AND social signal visible |

---

### 6. Content Creation and Publishing

| Task | Tool | When |
|---|---|---|
| Caption writing | `sniped-caption-writer` skill + `sniped-caption-architecture` skill (two-level narrative) | At image selection time, not publishing time; primary declares subject + lineage connected |
| LinkedIn POV post drafting | `sniped-linkedin-pov-gen` skill + Claude Code (voice layer mandatory; AI scaffold + Bryce approval) | Minimum 3x/week; Tue/Thu/one flexible; never from AI output-ready state without voice layer |
| Instagram carousel production | `sniped-rollout-executor` skill + `sniped-audience-multiplier` skill (1-shoot-to-5-outputs routing) | Wed weekly; 5-8 frames; grid sequence rules (warm-glam alt, color motif beat, no 3-adjacent-blob) |
| Content scheduling | Buffer (Phase B gate only, not active) | Blotato or social scheduler for batch scheduling Chapter Cards, HERO posts, Cultural Doc excerpts |
| Hook generation | `sniped-hook-engine` skill + `sniped-headline-forge` skill (3 Ogilvy variants) | Before any DM/post/caption ships; Ogilvy three-variant minimum |
| Copy quality gate | `sniped-copy-audit` skill + `sniped-newspeak-gate` skill + `sniped-copy-self-critique` skill (S2A + RaR + RE2) | All external-facing copy; em-dash scan 100% before ship |
| Content from archive | `sniped-content-extraction-engine` skill | Converts Direction Stack protocols, DM conversations, or archive images into 3 LinkedIn angles + 1 IG caption |
| B&W Card production | `sniped-card-production` skill + Figma MCP (official mcp__plugin_figma_figma__*) | Per-chapter; masthead + wordmark + saturation params; 3-5 min/card; Figma file AiMtRfT8W33yZRf4khjnds |
| Cultural documentation essay | `sniped-cultural-documentation-cadence` skill + Google Drive (archival) | Monthly 30-50 frame shoot + carousel + essay; quarterly thematic mini-essay |
| VIB caption library audit | `sniped-vib-outreach` skill (validation against VIB_caption_library.md) | Before any VIB batch; failure-mode scan (no generic compliments, no multi-CTA, under 80 words, no em-dashes) |
| Logline validation | `logline-gate` skill (Snyder four-component) | Before any market-facing deliverable ships |
| Awareness stage diagnosis | `sniped-awareness-stage-diagnosis` skill | Before any copy is written; locks stage diagnosis first |

---

### 7. Web and Design

| Task | Tool | When |
|---|---|---|
| Carrd landing page (current) | Carrd (manual build) + `sniped-carrd-conversion-surface` skill | Week-1 bootstrap; Problem-Method-Offer order; 60-sec booking target; full 14_WEB deferred until proof |
| Direction Stack book landing page | Vercel + Next.js | Post-proof phase; SEO-indexed chapter URLs; tiered pledge architecture |
| Pre-ship design validation | `design-delivery-gate` skill (141-point checklist, Lighthouse + axe/pa11y) | Before any page ships; dark mode + WCAG 4.5:1 + CLS<0.1 + single h1 + OG + canonical + 320px |
| Figma design decisions | Figma MCP (official mcp__plugin_figma_figma__*) | VIB card generation, Direction Stack visual grammar, Dossier template; REJECT community forks |
| Web/app build (3+ pages) | Windsurf > Cursor; planner-mode markdown guard first; one screen at a time | When beyond single-page scope; Sonnet 4.6+ required |
| Concept validation (lo-fi) | Claude Design (concept) > Figma (polish + handoff) > Codeex from Figma (implementation) | Code-first in Claude Code for rapid mockup; NOT Figma-first |
| SEO and AI citation audit | `sniped-ai-seo-audit` skill + `sniped-ai-visibility-audit` skill + Semrush | Monthly AI search baseline (Perplexity/Claude/ChatGPT/Google Overviews); schema markup gaps |
| Schema markup implementation | `sniped-schema-markup-implementation` skill | After AI-SEO audit confirms gaps; case study pages prioritized |
| GBP optimization | Manual (Google My Business) + Core 30 content architecture | Topical authority before geographic expansion |

---

### 8. Strategy and Decision-Making

| Task | Tool | When |
|---|---|---|
| Session-start routing | `sniped-os-execution-governor` skill reads CURRENT_STATE.md > ACTIVE_THREADS.md > SESSION_LOG.md tail > `_inbox/admin/` | Every session; STANDING_ORDER surfaced first |
| Multi-dimensional SNIPED decisions | `framework-orchestrator` skill + `boardroom` skill | Brand/revenue/production/audience decisions; diagnose > evaluate > bias-check sequence |
| Pre-production gate | `sniped-premortem` skill (timeline >30d or budget >$500 triggers failure history written 12 months forward) | Before any commitment above Reset floor |
| New lane or initiative evaluation | `sniped-boat-selector` + `sniped-7-questions-audit` + `sniped-stop-signal-protocol` + `sniped-enough-gate` | Before any resource commit; market-evaluation-scorecard (10-factor, score <50 = walk) |
| Pricing decision | `sniped-pricing-decision` skill + `sniped-value-conversation` skill (Enns three-year question) + `sniped-pricing-proposal` skill | Oral price before written; 3-option architecture; anchor at 65% target; $1,500 floor holds |
| Capital allocation | `sniped-wealth-architecture` skill + `sniped-margin-of-safety-audit` skill + Airtable owner-earnings tracker | Monthly; hurdle-rate ranking; organic proof > adjacent investments > equity |
| Constraint audit | `sniped-monthly-constraint-audit` skill + Airtable constraint dashboard | Monthly (60 min, last Monday); quarterly TAM/offer-ladder/aesthetic check; annual spine recalibration |
| Reverse roadmap review | `sniped-reverse-roadmap` skill | Before any major irreversible decision; decade-vision structural review |
| Proof log validation | `proof-log-validator` skill | Weekly; REAL PROOF = money + named outcome + access; FAKE INTEREST = praise or "send info" |
| Opportunity routing | `sniped-opportunity-cascade-audit` + `opportunity-transformation` skill (20-field diagnostic, 9-fate routing) | All inbound opportunities before scheduling strategy call |
| Weekly review | `sniped-weekly-review` skill (8-section template, 11-metric audit, 10-point drift check) | Every Monday Cockpit; 3 outcomes + cadence lock; no new strategy on Monday |
| Cognitive bias pre-decision | `sniped-cognitive-bias-pre-decision-gate` skill + `sniped-halt-gate` skill (HALT diagnostic) | Before any high-stakes decision; also run when post-win expansion is tempting |

---

### 9. Production Operations

| Task | Tool | When |
|---|---|---|
| Pre-shoot prep | `sniped-pre-shoot-prep` skill + Notion (brief template) + Google Calendar (48-hr MUA confirm) | Day before shoot; weather/gear/contingencies |
| Shoot day direction reset | `sniped-shoot-day-reset` skill + Direction Stack diagnostic mandatory | Start of every shoot day; no mid-shoot scope adds |
| Casting confirmation | `sniped-casting-confirmation-flow` skill + Airtable (24-hr confirm, wardrobe gate, two-strike auto-flag) + Zapier (Slack + Airtable 24-hr timer) | T-48hr; 4-hr reply window or backup activates; wardrobe photo required |
| Post-shoot same-day protocol | `sniped-post-shoot-same-day` skill | SD > SSD > HDD > Lightroom > Notion before laptop closes |
| Production OS folder structure | `sniped-production-os` skill + Airtable (shoot folder naming scaffold: date + client + TYPE, 9-subfolder root) | Every shoot; raw export immutable; no OS mutation without BJ approval |
| Retoucher handoff | `sniped-retoucher-onboarding` skill + certification Q&A (must answer before first pass) | Phase B gate: 30+ Heroes/month x 2mo sustained; BJ owns cull/labels/Hero promotion |
| Loom production (prospect outreach) | `sniped-loom-audit-production` skill + Descript (BJ audio + Higgsfield visuals + layer mapping) | Prospect-specific 5-min Loom; hybrid operator stance; unlocks Reply-1 discovery call |
| Monday Cockpit | `sniped-monday-cockpit` skill | Every Monday; 3 outcomes + cadence lock only; ACTIVE_THREADS reconcile checkpoint |
| Session end protocol | `sniped-session-carryover` skill | Updates CURRENT_STATE.md + ACTIVE_THREADS.md + SESSION_LOG.md; saves drafted DMs |

---

### 10. Research, SEO, and Intelligence

| Task | Tool | When |
|---|---|---|
| Deep research and fact-checking | `deep-research` skill (fan-out web searches, fetch sources, adversarial verify, synthesize) | Multi-source fact-checked reports; check if question is specific enough before invoking |
| Web search (tactical) | WebSearch deferred tool | Quick market intelligence; trigger-event monitoring; competitor research |
| Web fetch (specific URLs) | WebFetch deferred tool | Fetching specific competitor pages, prospect sites, press |
| SEO research | Semrush MCP (`sniped-ai-seo-audit` skill) | After WebSearch returns no direct answer; manual audit only as last fallback |
| Swarm-consensus validation | Swarm-consensus skill (4+ models via OpenRouter) | Before Direction Stack embedding or major strategic bets |
| Competitive intelligence | Higgsfield video analysis + `deep-research` skill | Pre-campaign; Sun Tzu Five Factors + Seven Comparisons before each chapter |
| Pre-outreach prospect research | Semrush organic research + Super Search + LinkedIn Sales Navigator | Current-state evidence for Gap Selling discovery; Airtable pain-density ranker updated after each cycle |

---

### 11. Automation and Integration

| Task | Tool | When |
|---|---|---|
| Zapier automation | Zapier (Reset intake triggers, casting form distribution, post-pipeline proof routing, Pixieset expiry) | After proof earned, not before; automation-before-proof is named anti-pattern |
| n8n workflows | n8n (Pixieset + Stripe integration gateway, OS_TRANSFORMATION_ROUTER intercept) | Proof-earned; validate N8N automation assets are extractable before commit |
| Cron/scheduled tasks | `schedule` skill + CronCreate/CronList tools | Recurring constraint audit, scene-density sweep, doctrine renewal tracking |
| Airtable automation | Zapier triggers on Airtable (tier-2 standby 24-hr escalation, casting no-confirm, KOTS same-day archive sort) | After workflow is manual-tested and stable |
| Gmail MCP automation | Gmail MCP (VIB DM timing, post-delivery sequences, referral drip) | Within 3 days of trigger event window for VIB; Day-45 referral trigger automated |
| Google Calendar automation | Google Calendar MCP (90-day constraint audit block, shoot-day brief prep 48-hr before) | Recurring blocks; conflict detection before meeting acceptance |
| Notion MCP | Notion MCP (P1 decision gate pending Wave-1 vs pre-Wave-1 schema resolution; all writes blocked on Gate-8 resolution) | CRM state mutations, proof log entries, checkpoint readiness queries |
| Google Drive automation | Google Drive MCP (Command Center scheduled backup, composite environment folder management, proof asset inventory) | Session-end auto-archive; Drive = temp bridge (personal + admin@snipedmedia.com); no cross-account file moves |
| LinkedIn automation | LinkedIn API (implicit, manual comment doctrine; 5-10 comments/day manual) | No faceless AI content; comment doctrine stays manual at this stage |
| Substack API | Substack API (monthly Cultural Doc essay auto-feed from Notion archive) | Candidate, Phase B+; not active |

---

### 12. AI Orchestration and Claude Stack

| Task | Tool | When |
|---|---|---|
| Strategic synthesis (full OS) | Claude Opus (synthesis layer) | Major strategic decisions requiring full OS engagement |
| Tactical velocity (most tasks) | Claude Sonnet 4.6 (current model) | Standard task execution; VIB drafts, caption writing, skill invocation |
| Batch low-stakes processing | Claude Haiku 4.5 (sub-agents) | Data-heavy sub-agent tasks; CRM hygiene; research scanning |
| Sub-agent routing | `sniped-sub-agent-router` skill (content-writer/research-specialist/operations-agent/book-drafter) | Complexity budget scored 2/6/8; single agent first; sub-agent only if single agent fails |
| Parallel worktree tasks | Git worktrees + `/loop` command | Recurring tasks; OS batch extraction; multiple independent branches |
| Composite prompt building | `composite-prompt-builder` skill (CoT + decomposition + self-critique) | Any multi-variable SNIPED brief before Higgsfield or Adobe dispatch |
| Prompt engineering | `sniped-prompt-method-router` skill (LtM/PaS/PoTh classification) + TCREI 4-pass minimum | All AI-generated outputs; 4 revision passes minimum before approval |
| Skills discovery (pre-build) | `skills-sh-finder` skill | Mandatory before any custom automation build; check 90,000+ community skills first |
| OS corpus retrieval | `sniped-corpus-retrieve` skill + MASTER_INDEX route to batch/domain + grep/jq | When corpus-citation rate falls below threshold; cite [BATCH_NNN_chunk_NNN] |

---

### 13. KOTS Operations

| Task | Tool | When |
|---|---|---|
| KOTS sponsor management | Airtable (tiers: Community $300, Sideline $1k, Court $2.5k, Crown $5k) + Gmail (one-week wait, one followup) | Under dad (Eric Jones) authority; BJ handles materials/tracking/digital inventory |
| KOTS coach pipeline | Airtable (8-stage tracker, dual CSV export) + `kots-coach-flow` skill | 7-10 day nudge cadence; dad authority on all prospect/price conversations |
| KOTS capture ops | `kots-capture-ops` skill (10-category shot-list, M/S/N priority tiers, 4 delivery lanes, same-day backup) | Every tournament day |
| KOTS gallery delivery | `kots-gallery-delivery` skill + Evoto School Mode (CSV roster import, QR-sort, per-student link) | Annual infrastructure; folder tree + naming templates + timing schedule |
| KOTS institutional reframe | `sniped-kots-institutional-reframe` skill | Before any external positioning of KOTS; Vanguard/Marion County institution frame, not Eric Jones production |
| Sponsor renewal | Renewal recap as highest-leverage step; high-res logos + recap video + year-over-year tracker | Built into production timeline at outset of every event year |

---

### 14. Financial Operations (Routing only; records outside OS)

| Task | Tool | When |
|---|---|---|
| Payment collection | Multi-method invoicing (HoneyBook/Pixieset/Stripe/ACH) + automated reminder sequence | NEVER manual follow-up; 50% deposit at signature; milestone billing 30/30/40 |
| Bookkeeping | QuickBooks sync + accountant (NOT DIY for accrual) | Weekly/monthly/quarterly/annual cadence; P&L action gate |
| Sensitive records storage | Command Router §17 routes security/legal/tax/payment records OUTSIDE OS | Always; separate audit trail |
| Entity/capital structure decisions | `sniped-founder-control-audit` skill + attorney consultation | Before any capital event, partnership, or equity offer; voting rights, board composition, IP assignment |

---

### 15. Manual Fallback Routing

Manual execution is only authorized after the 11-step toolchain audit returns no viable path:

1. Does a Claude Code skill exist for this task?
2. Does an MCP tool cover this (Adobe, Figma, Gmail, Google Drive, Calendar, Notion, Airtable, Higgsfield)?
3. Does Zapier or n8n have a configured zap/workflow?
4. Does Instantly, Super Search, or Sales Navigator automate this?
5. Can a Claude sub-agent handle it (content-writer, research-specialist, operations-agent)?
6. Does `skills-sh-finder` return a community skill?
7. Can a script or cron job handle recurrence?
8. Can a browser-based flow (manual-assisted) reduce effort significantly?
9. Is there a Vercel serverless function or API that applies?
10. Is there an existing connector (HoneyBook, Pixieset, Gumroad, DocuSign) covering this?
11. If all above return no path: manual is authorized.

Tasks confirmed manual-only at current phase (no automation path available or warranted):
- LinkedIn commenting (doctrine requires real insight, not scheduling)
- Direction Stack diagnostic conversation with client (non-delegable, non-automatable)
- Final image selection and composite environment approval (Bryce's editorial judgment, non-delegable)
- Hero retouch final approval
- Casting subjective evaluation (ranked comparison via anchored vignettes, human decision)
- High-stakes negotiation (pricing, partnership, equity)
- Cultural documentation fieldwork and scene presence

---

## GATES

Below is the complete SNIPED OS gate library synthesized from all 166 doctrine docs. Each entry states the gate name, what it checks, pass/fail criteria, and where it fires in the production sequence.

---

### AUTHORIZATION AND STAGING GATES

**Staging Authorization Gate**
What it checks: Whether planning and execution are separated across distinct sessions.
Pass: Operator has given explicit separate authorization for mutation before any batch writes occur.
Fail: Execution proceeds in the same session as planning without authorization.
Fires: Before any batch extraction, OS write, or corpus mutation.

**Ephemeral-State Freshness Gate**
What it checks: Whether CURRENT_STATE.md, ACTIVE_THREADS.md, and SESSION_LOG.md have been read fresh at session start.
Pass: All three docs read at session open; no stale snapshot used as truth.
Fail: Prior session's in-memory state used without re-reading disk state.
Fires: Session start, before any standing-order execution.

**Proof-Before-Write Gate**
What it checks: Whether a workflow or schema has been run live at least once before being committed as a skill or memory entry.
Pass: At least one live run logged; BJ approval confirmed in writing before new database builds.
Fail: Skill or memory write attempted from hypothetical design only.
Fires: Before any new skill file is created or OS memory is mutated.

**Verification-Before-Canonical Gate**
What it checks: Seven-point bash ritual on JSONL output: JSON valid, schema fields present, chunk IDs unique, batch ID consistent, source paths resolve on disk, master count correct, line count matches chunk count and header count.
Pass: All seven checks return clean.
Fail: Any single check fails.
Fires: Between "I have a JSONL file" and "this batch is canonical."

**Source-Quality Verification Gate**
What it checks: Whether a corpus batch meets full integrity standards.
Pass: JSONL line count equals chunk count equals header count; source_file resolves on disk; schema complete; chunk_id unique; batch_id consistent; master count correct.
Fail: Any mismatch or unresolved path.
Fires: After extraction, before batch is merged into MASTER_INDEX.

**Six-Check Reconciliation Gate**
What it checks: JSON validity, schema field presence, chunk_id uniqueness, batch_id consistency, source path resolution, master count verification.
Pass: All six pass.
Fail: Any one fails, triggering halt and escalation.
Fires: Before master-file isolation lock is applied.

**Master-File Isolation Gate**
What it checks: Whether JSONL validation is complete before master files are locked.
Pass: Validation complete and clean.
Fail: Master file locked before validation confirmed.
Fires: Immediately after six-check reconciliation.

**Staging Gate (Copy Pass)**
What it checks: Whether explicit operator authorization exists after pre-flight peeking.
Pass: Operator has separately approved the mutation pass.
Fail: Execution starts without explicit post-peek authorization.
Fires: After planning peek, before any write execution.

---

### IDENTITY AND VISUAL QUALITY GATES

**Strongest Photograph != Most Processed Gate**
What it checks: Whether the automated or edited output beats the source photograph visually, not just completes the task.
Pass: Output is visually superior to source on compositional weight, presence, and editorial quality.
Fail: Output completes a task (background swap, skin pass, composite) but is weaker than source; failed cleanup artifacts visible.
Fires: After every automated treatment pass, before any delivery or deck entry.

**Identity Preservation Gate**
What it checks: Whether face, body, and skin texture of the real subject are untouched.
Pass: Identity layer (face, skin texture, body proportions) unchanged across all outputs; hair styling and environment are variable.
Fail: Any generative or retouching tool has altered facial features, skin identity, or body shape.
Fires: Before final composite delivery and before any Higgsfield, Adobe Firefly, or Evoto output is approved.

**Evoto Scope Gate**
What it checks: Whether Evoto is applied only to studio-register images.
Pass: Source image is studio-context portrait with stable lighting and background.
Fail: Non-studio source is routed into Evoto identity-adjacent tools; backdrop changer triggers lineage review.
Fires: Before Evoto batch is initiated.

**Evoto Slider Restraint Gate**
What it checks: Whether Evoto sliders are within the 25-75 percent professional discipline range.
Pass: No slider at 100 percent without explicit override justification; blemish, hair, texture all within documented range.
Fail: Any slider at maximum shipped without justification.
Fires: Before Evoto export is approved.

**Evoto Identity-Preservation Gate**
What it checks: Freckles, beauty marks, and skin texture preserved; face reshape below 15 percent; hair smoothing below 75 percent.
Pass: All three axes within spec.
Fail: Any axis exceeded.
Fires: During Evoto review before TIFF export.

**Pre-Composite QA Gate (Composite Master QA)**
What it checks: Proof crops at 100 percent zoom for hair and feet, plus a six-axis scorecard: lighting match, grounding, edge-hair quality, color marriage, artifact presence, brand-fit. Each axis minimum 8 out of 10. Zero Gate-8 hard rejects (AI smear, warped geometry, barcode sky, melted plants).
Pass: All axes at 8 or above; no Gate-8 items present.
Fail: Any axis below 8 or any Gate-8 reject visible.
Fires: Before any composite enters client delivery, deck, or posting queue.

**Platform Mastering Gate**
What it checks: Whether the hero image has been re-composed per aspect ratio and safe-area spec for each platform surface, with numeric skin-drift RGB validation.
Pass: Color and B&W renders confirmed per aspect, safe-area passes, skin-drift test shows uniform delta.
Fail: Composite approved but not re-composed per platform; delta uneven across skin areas.
Fires: After composite master QA, before any image is published.

**Subject-Grade Read-Only Gate**
What it checks: Whether the TIFF or PNG cutout from the hero is locked against reinterpretation.
Pass: Compositing session modifies only environment integration; subject color, skin, and identity untouched.
Fail: Composite operator applies color or skin grade to subject layer.
Fires: At start of every compositing session.

**Plate Quality Gate**
What it checks: Whether the AI-generated background plate matches the required direction before Photoshop is opened.
Pass: Plate direction is correct; lighting, perspective, and register match the environment spec.
Fail: Plate direction is wrong; plate has been sent into Photoshop to be corrected.
Fires: After Higgsfield or Adobe Firefly generates plate, before Photoshop opens.

**Generative Fill Reject Gate**
What it checks: Whether any generative fill output meets the five-checkpoint standard: no seam, tonal match within 5 percent, no hallucinated objects, no texture loops, maintained depth of field.
Pass: All five checkpoints clean.
Fail: Any checkpoint fails; output is weaker than source.
Fires: After each generative fill attempt, before accepting result. Six-attempt cap before escalation to manual.

**Generative Fill Identity Gate**
What it checks: Whether generative fill is applied only to backgrounds, environments, and prop extensions.
Pass: Fill is confined to world layer; face, body, and skin are excluded from selection.
Fail: Selection includes face, body, or skin texture of subject.
Fires: Before any generative fill tool is invoked.

**Composite QA 11-Gate (Ceiling Spec)**
What it checks: Gates 1-8 cover lite and internal standards; Gates 9-11 cover depth of field and lens match, perspective and camera-height alignment, directional color bleed.
Pass: All 11 gates clear.
Fail: Any gate fails; Gates 9-11 failure means work is not client-ready.
Fires: Before client-ready composite delivery.

**Non-Destructive Layer Architecture Gate**
What it checks: Whether all Photoshop edits use smart objects, adjustment layers, masks, and smart filters.
Pass: No destructive edits; every layer reversible.
Fail: Destructive edit detected.
Fires: At start of Photoshop session and before saving final PSD.

**Shadow Anatomy Gate**
What it checks: Whether composite shadows include umbra, penumbra, occlusion, horizon convergence, and source-distance correlation.
Pass: All five shadow elements present and internally consistent.
Fail: Any element absent or inconsistent with lighting direction.
Fires: Before composite is approved for delivery.

**Lighting Direction Lock Gate**
What it checks: Whether the composite was assembled with matching light directions from the start.
Pass: Subject light direction matches background plate; no irreconcilable studio-versus-outdoor conflict.
Fail: Harsh studio light is paired with an outdoor AI background without resolution.
Fires: Before Photoshop assembly begins.

**Halo Removal Mask Quality Gate**
What it checks: Whether fringe artifacts have been addressed with minimum 1-pixel shrink on mask edges.
Pass: No halo or fringe visible at 100 percent zoom.
Fail: Fringe artifacts visible; output reads as vending-machine quality.
Fires: Before final composite merge.

**Atmospheric Perspective Gate**
What it checks: Whether background has more fade, less saturation, and lower contrast than foreground, with separate blur layers.
Pass: Credible depth separation achieved.
Fail: Background matches foreground in contrast or saturation.
Fires: Before composite finalization.

**Gesture Specificity Gate**
What it checks: Whether a specific gesture, body micro-detail, or relational dynamic is present.
Pass: Identifiable trigger (gesture, eye contact moment, hand placement) present.
Fail: No specific trigger; generic pose only.
Fires: Before any image enters delivery or posting queue.

**Color Relationship Gate**
What it checks: Whether colors are interacting rather than competing; maximum three color families without hierarchy before refinement required.
Pass: Colors interact with clear dominant and accent logic.
Fail: Three or more color families with no hierarchy.
Fires: Before composite is finalized.

**Bliss-Point Gate**
What it checks: Whether the composite or photograph contains two to four identifiable visual hook moments.
Pass: At least two distinct hook moments present.
Fail: Single-mood image with no visual punctuation.
Fires: Before client delivery or posting.

**Freeman Six-Qualities Gate**
What it checks: Image scored against Freeman's six visual quality dimensions with pass/fail per dimension.
Pass: All six dimensions pass.
Fail: Any dimension fails; image rerouted.
Fires: Before any image ships.

**Five-Level Sequence Gate**
What it checks: Whether the image batch has been evaluated at individual, pair, series, environment, and full-lineage-thread levels.
Pass: All five levels reviewed; sequence manifest complete.
Fail: Only individual image quality reviewed; sequence not addressed.
Fires: Before chapter or carousel publication.

**Sprezzatura Gate**
What it checks: Whether the output looks less processed than the source and passes a snapshot test.
Pass: Effort is invisible; result reads as naturally arrived at.
Fail: Processing effort is visible.
Fires: Before any image is published or delivered.

**Trafalgar Gate**
What it checks: Whether one editorial-memory image (surprising, lineage-rooted, non-hero) is designated per composite chapter.
Pass: One Trafalgar candidate identified and placed mid-sequence.
Fail: No editorial-memory image designated.
Fires: At chapter sequencing stage.

**B&W Card Dual-Register Gate**
What it checks: Whether HERO posts are in full v3 LUXURY color and Chapter Card images are in B&W.
Pass: Dual-register maintained; apparatus layer stays color.
Fail: B&W applied to HERO or color applied to Card incorrectly.
Fires: Before any Card or HERO post is scheduled.

**Skin-Drift Numeric Gate**
What it checks: Whether skin color is consistent between composite approval and platform-mastered version, measured via RGB comparison on an alpha-eroded 25-pixel interior body region.
Pass: Delta is uniform across the skin region.
Fail: Delta is uneven; skin drift detected.
Fires: Between composite master QA approval and platform mastering.

**Avedon Authenticity Gate**
What it checks: Three questions - Does the environment serve the subject's authentic presence? Is the identity untouched? Is existential weight present?
Pass: All three affirmative.
Fail: Any one negative.
Fires: Before any hero image is published.

**Air Gate**
What it checks: Four-question binary: air presence, identity hold, punctum detail, blind field.
Pass: All four affirmative.
Fail: Any one negative; image not published.
Fires: Before portfolio or grid post.

**Over-Processing Gate**
What it checks: Whether the output serves the photograph or mythology.
Pass: Edit reveals and enhances; output beats source visually.
Fail: Edit buries air, falsifies skin, or erases lineage markers.
Fires: After every treatment pass.

**Three-Level Photo Gate**
What it checks: Physical quality, depictive clarity, and mental/psychological weight.
Pass: All three levels pass; mental is the primary criterion.
Fail: Mental level absent regardless of processing investment.
Fires: At image selection stage.

**Composition Reject Gate**
What it checks: Context contribution threshold, single dominant line-type, off-center justification, key-register match, productive ambiguity.
Pass: All five present.
Fail: Any absent.
Fires: Before image enters sequence or posting queue.

**Noeme Gate**
What it checks: Whether the subject was actually photographed (real light-trace).
Pass: Real subject with documentable shoot; emanation intact.
Fail: AI-generated identity used as subject.
Fires: Before any image is published as client work or lineage documentation.

---

### COPY, MESSAGING, AND POSITIONING GATES

**Em-Dash Scan Gate**
What it checks: Whether any em-dash (U+2014) is present in any output.
Pass: Zero em-dashes detected.
Fail: Any em-dash present.
Fires: Before every external-facing output is sent or published.

**Name Availability Gate**
What it checks: Whether the .com domain is available and no major brand or app owns the proposed name.
Pass: .com available; no trademark conflict; no major brand ownership.
Fail: .com taken or major brand conflict exists.
Fires: Before any brand, product, or lane name is proposed or published.

**VIB Failure-Mode Checklist Gate**
What it checks: Five failure modes - no generic compliments, no multi-CTA, under 80 words, no em-dashes, not price-in-first-message.
Pass: All five clean.
Fail: Any failure mode present.
Fires: Before any VIB DM is sent.

**Five Copy Failure Modes Gate**
What it checks: Premature pitching, generic compliments, volume language, begging tone, multi-CTA.
Pass: None of the five present.
Fail: Any one present.
Fires: Before any outbound DM, email, or LinkedIn post ships.

**Newspeak Compression Gate**
What it checks: Whether positioning language could describe a competitor without modification.
Pass: Language is specific and non-transferable.
Fail: Any sentence passes unchanged to a competitor.
Fires: Before any external positioning copy ships.

**One-Liner Grunt Test Gate**
What it checks: Whether a stranger can state what SNIPED offers, how it improves their life, and how to buy it within five seconds.
Pass: All three answered immediately.
Fail: Any one unclear.
Fires: Before scaling any format or outreach sequence.

**SUCCESs Gate**
What it checks: Six-axis score: Simple, Unexpected, Concrete, Credible, Emotional, Story.
Pass: All six axes pass; any axis below six triggers rewrite.
Fail: Any axis below six.
Fires: Before any positioning asset, Direction Stack chapter, or VIB outreach ships.

**Curse of Knowledge Gate**
What it checks: Jargon presence, buried lead, missing emotional hooks, missing story arc, feature-versus-identity appeal, proof within first 100 words.
Pass: All checks clean.
Fail: Any check fails.
Fires: Before any external artifact ships.

**Two-Level Narrative Gate**
What it checks: Whether the caption has both a surface human-interest layer and a lineage subtext layer.
Pass: Both layers present.
Fail: Single-level caption only.
Fires: Before any caption is published.

**Reading Sequence Gate**
What it checks: Whether copy follows notice, identity, relevance, support, details order.
Pass: Sequence respected.
Fail: Features appear before identity or relevance.
Fires: Before any marketing asset ships.

**Logline Gate**
What it checks: Snyder four-component pass/fail: irony, compelling image, audience/cost, title.
Pass: All four components present.
Fail: Any component absent.
Fires: Before any market-facing deliverable ships.

**Caption Architecture Gate**
What it checks: Primary declaration of subject, lineage connection, platform variant, and direction of beholder's share.
Pass: All four elements present.
Fail: Any element absent.
Fires: At image-selection time, not publishing time.

**Intent Audit Gate**
What it checks: Whether the aesthetic serves the intent or conceals it.
Pass: Aesthetic clearly serves stated intent.
Fail: Aesthetic conceals intent.
Fires: Before any content is published.

**Documentary Authority Gate**
What it checks: Whether Cultural Doc entries and Chapter Card captions contain at least one specific person, place, community, lineage root, or historical date.
Pass: At least one specific anchor present.
Fail: Generic narrative without specificity.
Fires: Before any Cultural Doc or Card caption ships.

**Testimony-Format Gate**
What it checks: Four criteria - inside-experience voice, specific detail not category, no savior framing, contradiction allowed to stand.
Pass: All four present.
Fail: Any one missing.
Fires: Before any testimonial, case study, or Cultural Doc entry is published.

**Self-Criticism Loop Gate**
What it checks: Whether any LLM-generated copy has passed at least one self-criticism revision pattern before approval.
Pass: Minimum one S2A, RaR, or RE2 pass completed.
Fail: AI output approved without self-criticism loop.
Fires: Before any AI-generated copy asset is used externally.

**Lollapalooza Positioning Audit Gate**
What it checks: Whether all seven argument pillars are present before any positioning deck ships - lineage, editorial, hybrid-operator, scene density, case studies, behavioral science, cultural document, Direction Stack book.
Pass: All pillars documented.
Fail: Any pillar absent.
Fires: Before positioning deck or major external positioning move.

**Psycho-Logic Landing Gate**
What it checks: Whether positioning phrases land unconsciously without requiring rational work from the reader.
Pass: Phrases activate without explanation.
Fail: Phrases require rational unpacking.
Fires: Before any external positioning copy ships.

**Category Naming Gate**
What it checks: Whether the coined category name has the .com available, no major brand ownership, and is empty enough for audience projection.
Pass: All three conditions met.
Fail: Any one fails.
Fires: Before book launch or major external positioning.

**Froto Gate**
What it checks: Whether every outreach, pitch, or copy moves the reader from old thinking to new thinking.
Pass: From-state and to-state are both explicit; reader cannot maintain old frame.
Fail: Copy describes the service without naming the problem it replaces.
Fires: Before any outreach or positioning copy ships.

**Negative Social Proof Trap Gate**
What it checks: Whether copy emphasizes the 97 percent who make a strong choice rather than the 3 percent who do not.
Pass: Positive-majority framing used.
Fail: Problem-majority framing (for example, "most founders fail at this") used.
Fires: Before any LinkedIn post or outreach copy ships.

**Doorbell Gate**
What it checks: Whether content earns attention before delivering its claim.
Pass: Content hooks before asserting.
Fail: Announcement or claim appears before attention is earned.
Fires: Before any content or cold-outreach message ships.

**Brand Adjective Gate**
What it checks: Whether the output reinforces the single locked SNIPED adjective or diffuses it.
Pass: Output reinforces the adjective.
Fail: Output introduces a competing or contradicting descriptor.
Fires: Before any external copy ships.

**Logline/One-Word Attribute Gate**
What it checks: Whether a single ownable one-word attribute is claimed in external positioning before the 2026 market push.
Pass: One word selected and consistently applied.
Fail: Multiple words compete without hierarchy.
Fires: Before any external campaign launches.

**Sowell Test Gate**
What it checks: Three questions - Compared to what? At what cost? What evidence?
Pass: All three answered before any policy, pricing, or program decision.
Fail: Decision made without answering all three.
Fires: Before any major policy, pricing, or program decision.

**Silence Gate (Caption)**
What it checks: Whether the caption adds what the image cannot say rather than explaining what the image already says.
Pass: Caption orients; does not explain.
Fail: Caption explains visible content.
Fires: Before any caption ships.

---

### PROOF AND SALES GATES

**Proof Fabrication Guardrail**
What it checks: Whether any logged proof entry involves invented pilots, clients, testimonials, case studies, or metrics.
Pass: Every proof entry has money committed or access granted plus a named role or bid.
Fail: Praise alone is logged; no payment or access; hypothetical scenario treated as real.
Fires: Before every proof log entry is recorded.

**Room-Access Unlock Gate**
What it checks: Whether progress toward market represents real paid engagement or just interest.
Pass: At least one paid pilot or LOI and at least one room opened (access granted, named bid or role commitment).
Fail: Calls booked or interest expressed without payment or room access.
Fires: After every client conversation; at kill gate when 15 conversations produce zero paid and zero rooms.

**Proof-Only Delivery Gate**
What it checks: Whether only proof-stage images (sRGB JPEG 2048 long edge) are delivered before client confirms hero selection.
Pass: No high-res, finals, heroes, retouch, or internal files included at proof stage.
Fail: Final or hero files delivered before client confirmation.
Fires: Before any proof gallery is sent.

**Hero Retouch Gate**
What it checks: Whether the client has made their selection from proofs before hero retouching begins.
Pass: Client confirmation of hero selection documented.
Fail: Hero retouching started before client pick.
Fires: Before any hero retouching session.

**Outcome-Anchored Offer Gate**
What it checks: Whether the offer uses only capability-proof or bid-support framing.
Pass: Offer language is "capability proof" (hire) or "bid-support" (infra).
Fail: Offer uses "portfolio," "content," or "photography" as primary language; compliment with zero payment treated as proof.
Fires: Before any offer is presented to a prospect.

**Commitment vs. Compliment Gate**
What it checks: Whether positive sentiment from a prospect includes a specific next step.
Pass: Sentiment paired with concrete next step (deposit, meeting, named commitment).
Fail: Positive sentiment with no next step.
Fires: After every prospect interaction.

**Proof-First Referral Trigger Gate**
What it checks: Whether the referral ask is sent only after testimonial received, photos deployed, and social signal visible.
Pass: All three conditions met.
Fail: Referral ask sent before any of the three conditions.
Fires: Before any referral ask is sent.

**Day-19 Conditional Send Gate**
What it checks: Whether the conditional upsell email is sent only if the client has opened the gallery and has not yet purchased an upgrade.
Pass: Client opened gallery and no upgrade purchased.
Fail: Email sent without checking both conditions.
Fires: 19 days after gallery delivery.

**Social-Norm-to-Market-Norm Boundary Gate**
What it checks: Whether warming mode (no money language) and qualification mode (MLE declared) are kept sequential.
Pass: Warming completes before qualification begins; modes never mixed.
Fail: Price or payment language introduced during warmth phase.
Fires: Before any outreach message is sent.

**Anchor-Setting Gate**
What it checks: Whether the first number or category perception moment has been set intentionally.
Pass: Highest-quality anchor stated first; nothing cheaper shown first.
Fail: Prospect anchors first or lower-priced option leads.
Fires: Before any pricing conversation.

**Option 1 Completeness Gate**
What it checks: Whether the first pricing option meets all stated client objectives.
Pass: Option 1 fully satisfies the stated objective.
Fail: Option 1 requires the client to upgrade to meet their own stated need.
Fires: Before any three-option proposal is sent.

**Price Verbal-Before-Written Gate**
What it checks: Whether price range has been floated verbally on the discovery call before a written proposal is sent.
Pass: Verbal price stated; objections surfaced before proposal.
Fail: Written proposal sent without verbal price discussion.
Fires: Before any written proposal is prepared.

**Batch Approval Gate**
What it checks: Whether first-result performance data has been collected before batch production is approved.
Pass: First result measured against named signal metrics; approval conditional on performance.
Fail: Batch approved before any first-result data.
Fires: Before any batch campaign or content series is scaled.

**ICP Sourcing 4-of-4 Gate**
What it checks: Whether the prospect meets all four ICP criteria - LA-based, active poster in past seven days, visual gap present, revenue or funding signal visible.
Pass: All four confirmed.
Fail: Any one missing.
Fires: Before any VIB DM or cold outreach is initiated.

**4-Yes Test Gate (Keenan)**
What it checks: Four questions - problem exists, buyer agrees, buyer wants fix, buyer joins journey.
Pass: All four answered affirmatively.
Fail: Any one negative.
Fires: Before booking any creative work.

**Proposal Earning Gate**
What it checks: Whether close rate suggests the proposal gate is calibrated correctly. Below 50 percent means too loose; above 80 percent means potentially too restrictive.
Pass: Close rate in 50 to 80 percent range.
Fail: Outside range triggers recalibration.
Fires: Quarterly review.

**No-Show/Late Reschedule Policy Gate**
What it checks: Whether the no-show or reschedule policy is applied consistently.
Pass: First reschedule honored (14-day window); second triggers $150 fee; third forfeits deposit; 60-minute no-show triggers binary offer.
Fail: Policy waived without documented reason.
Fires: At each reschedule or no-show event.

**Proof Density Gate**
What it checks: Whether three to five named founder case studies with measurable outcomes exist before scaling VIB outreach volume.
Pass: Minimum three case studies on record with quantified outcomes.
Fail: Fewer than three; scaling proceeds without proof base.
Fires: Before any VIB outreach volume increase.

**Weiss Pro-Bono Gate**
What it checks: Whether uncompensated shoots meet three conditions - strategic marketing budget line, one per quarter limit, documented ROI expectation.
Pass: All three conditions met.
Fail: Any one absent.
Fires: Before any free or below-floor-rate shoot is booked.

**Reset Floor Gate**
What it checks: Whether pricing holds at $1,500 minimum; $750 deposit only; $1,000 first-three exception is time-boxed.
Pass: Price at floor or above.
Fail: Price below $1,500 without documented exception; discount offered rather than scope adjusted.
Fires: Before any Reset booking is confirmed.

**Sprint Floor Gate**
What it checks: Whether the Sprint $750 tier is limited to warm-referral-only segmentation.
Pass: Client source confirmed as warm referral before Sprint pricing offered.
Fail: Sprint pricing offered to cold inbound.
Fires: Before Sprint pricing is discussed.

**Payback-Window Gate**
What it checks: Whether sub-30-day payback is confirmed before VIB v2, Op Kit v2, or Brand System launch.
Pass: Revenue from offering covers costs within 30 days.
Fail: Payback window exceeds 30 days.
Fires: Before any new offer version launch.

**Advantage Inventory Reality Check Gate**
What it checks: Four factors - expensive problem, paying now, reachable, growing market.
Pass: All four factors confirmed before advancing.
Fail: Fewer than four confirmed.
Fires: Before any new lane or offer is activated.

---

### OPERATIONS AND SCALING GATES

**Pre-Scaling Gate**
What it checks: Whether the minimum viable execution proof package exists before any new tool, channel, hire, or lane is added.
Pass: At least one closed and delivered Reset plus testimonial, one Op Kit pitch, and one surfaced SLA failure on record.
Fail: Any of the four conditions unmet.
Fires: Before any proposed expansion of tools, channels, hires, or lanes.

**Phase B Hire Gate**
What it checks: Whether $3,000 MRR has been sustained for two consecutive months before any labor hire.
Pass: Two consecutive months at or above $3,000 MRR.
Fail: MRR below threshold.
Fires: Before any hire or retoucher engagement is initiated.

**Retoucher Volume Gate**
What it checks: Whether the volume of heroes per month and calendar timing meet the Phase B threshold before a retoucher is onboarded.
Pass: 30-plus heroes per month sustained for two months AND calendar-month timing aligned. CURRENT_STATE.md governs any discrepancy.
Fail: Volume below threshold or timing misaligned.
Fires: Before retoucher onboarding is initiated.

**Tutorial-to-Asset Conversion Gate**
What it checks: Whether every tutorial consumed from the five canonical sources produces a persistent OS asset within the same week.
Pass: Asset (checklist, reject gate, .atn, PSD template, or doctrine note) created and filed within the week.
Fail: Tutorial consumed without producing a persistent asset; resource is deleted.
Fires: Within one week of any tutorial consumption.

**Photoshop Reject-Gate Discipline**
What it checks: Whether any Photoshop technique falls into the locked reject list - beginner basics, plastic skin, preset culture, trendy AI effects, wrinkle removal, HDR, Dragan processing, eye enlargement, Liquify reshaping, warm-teal cinematic grades.
Pass: No technique on the reject list is used.
Fail: Any reject-list technique is applied.
Fires: Before any Photoshop technique is included in an SOP or delivered work.

**Tutorial Source Whitelist Gate**
What it checks: Whether all new Photoshop or Lightroom tutorials clear the six-author whitelist (Naik, Nace, Dewis, Malley, Adobe, Adler) and five auto-reject pattern gates.
Pass: Author on whitelist; no auto-reject patterns.
Fail: Author not on whitelist or auto-reject pattern present.
Fires: Before any tutorial is distilled into OS doctrine.

**Notion Schema Decision Gate**
What it checks: Whether the Notion Wave-1 vs. pre-Wave-1 schema conflict has been resolved and overlaps addressed by operator before any write.
Pass: Operator has resolved schema conflicts in writing.
Fail: Writes attempted while schema conflict is unresolved.
Fires: Before any Notion database write.

**30-Day Phase-1 Notion Activation Gate**
What it checks: Whether DBs 1 and 2 have been used on at least one day within each 14-day window by Day 30.
Pass: No 14-plus consecutive unused days by Day 30.
Fail: Either DB unused for 14 consecutive days triggers archive-to-markdown-only routing.
Fires: At Day 30 calendar checkpoint.

**EIN Payment Preflight Gate**
What it checks: Whether the payment processing path is clear before accepting paid pilots.
Pass: Zelle, bank transfer, Venmo, PayPal, or Square confirmed as active path; Stripe gated until EIN legal-name correction is live.
Fail: Stripe used for payment before EIN correction is confirmed.
Fires: Before any paid booking is confirmed.

**Payment Processing Gate**
What it checks: Whether Stripe is being used before the EIN legal-name correction is live.
Pass: Stripe not used; alternative payment path confirmed.
Fail: Stripe invoked for Alma Love or any payment before EIN correction.
Fires: Before any invoice or payment link is generated.

**AI Composite Disclosure Gate**
What it checks: Whether a unified disclosure addendum covering AI-generated backgrounds exists before any composite-inclusive gallery ships under any MSA.
Pass: Disclosure addendum attached to Reset MSA, Op Kit MSA, or Collab Agreement.
Fail: Composite-inclusive gallery ships without disclosure addendum.
Fires: Before any composite-inclusive gallery is delivered to a client.

**Security/NDA Compliance Gate**
What it checks: Whether any proposed shoot involves secure floors, equipment, logos, or PII at hyperscalers or colos.
Pass: Shoot confined to non-secure, owner-controlled settings.
Fail: Any of the restricted elements are proposed.
Fires: Before any B2B shoot scope is confirmed.

**Free-Conditional-on-Margin Gate**
What it checks: Whether any free pricing tier has a paid layer behind it and near-zero marginal cost.
Pass: Both conditions present.
Fail: Free pricing proposed without paid layer or with meaningful marginal cost.
Fires: Before any free offer or freemium model is designed.

**Employer NDA Read Gate**
What it checks: Whether the current employment NDA has been read before the first paid BASEPLATE client is engaged.
Pass: NDA read; non-compete scope confirmed; attorney review completed.
Fail: BASEPLATE client engaged before NDA review.
Fires: Before first paid BASEPLATE engagement.

**School/Event Photography Decline Gate**
What it checks: Whether any proposed engagement is school or event photography outside the KOTS institutional model.
Pass: Engagement declined cleanly.
Fail: School or event shoot accepted that is off-thesis and below ceiling.
Fires: On any inbound inquiry for school or event photography.

**ACTIVE_THREADS Stale-State Gate**
What it checks: Whether ACTIVE_THREADS.md has been updated within 16 days.
Pass: Last update within 16 days.
Fail: 16-day gap detected; execution-governor failure flagged.
Fires: At Monday Cockpit and session start.

**Boost-Worthiness Gate**
What it checks: Whether a post qualifies for paid promotion after 48 to 72 hours of organic performance.
Pass: Post achieves greater than 3 percent impression save rate or greater than 1.5 percent share rate.
Fail: Neither threshold met.
Fires: 48 to 72 hours after any post goes live, before any paid spend is authorized.

**Vendor-AI Infrastructure Proof Gate**
What it checks: Whether N8N automation assets are extractable and the field-ops workflow gap is addressable before a productized AI-ops commitment is made.
Pass: Both conditions confirmed via live test.
Fail: Commitment made before live validation.
Fires: Before any AI-ops product commitment.

**Constraint-Shift Detection Gate**
What it checks: Whether the binding constraint has moved from Bryce's time to portfolio depth, casting quality, or outreach consistency.
Pass: Binding constraint correctly identified and updated.
Fail: Effort directed at non-constraint while true constraint goes unaddressed.
Fires: Quarterly at Constraint Audit and on demand when performance plateaus.

**Missing-Middle Routing Gate**
What it checks: Whether any proposed tool or task is Wave 2 (automate outdated) or Wave 3 (reimagine) before adoption.
Pass: Classification made; appropriate wave-level action taken.
Fail: Tool adopted without wave classification.
Fires: Before any new tool or automation is adopted.

**Idiocy Index Gate**
What it checks: Whether the cost-to-material ratio for a proposed process is unreasonably high relative to the output.
Pass: Ratio is reasonable; algorithm audit (Question-Delete-Simplify-Automate-Accelerate) run and passed.
Fail: High ratio without audit.
Fires: Before any new SOP step or production process is adopted.

**Requirement-Owner Gate**
What it checks: Whether every SOP step has a named owner.
Pass: All steps have named owners.
Fail: Any step lacks a named owner; that step is flagged as a deletion candidate.
Fires: At every SOP review.

**Barnacle Removal Gate**
What it checks: Whether any OS component has produced proof, revenue, or moat contribution in the past 90 days.
Pass: Component demonstrates at least one contribution.
Fail: No contribution; flagged as prune candidate.
Fires: Quarterly.

**Canada Principle Gate**
What it checks: Whether a new lane passes the five-factor moat-dilution test - moat dilution, operational muscle, revenue structure, founder time, repetition lock.
Pass: All five factors pass.
Fail: Any one fails.
Fires: Before any new lane is activated.

**Positioning Phase Gate**
What it checks: Whether a proposed positioning move is classified as Phase 1, Phase 2, or Phase 3 and whether Phase 1 proof exists before Phase 3 moves are made.
Pass: Phase identified; Phase 1 proof established before Phase 3 activation.
Fail: Phase 3 move attempted without Phase 1 proof.
Fires: Before any major positioning move.

**Synergy Architecture Gate**
What it checks: Whether a proposed activation touches at least three surfaces simultaneously.
Pass: Three or more surfaces confirmed.
Fail: Fewer than three surfaces; asset is being underutilized.
Fires: Before any major content or campaign activation.

**Barnacle Gate**
What it checks: Whether any OS process, content format, or lane has gone 90 days without proof, revenue, or moat contribution.
Pass: Contribution documented.
Fail: No contribution; prune candidate.
Fires: Quarterly.

---

### CONTENT AND DISTRIBUTION GATES

**Hook Layering Gate**
What it checks: Whether every IG post has a visual hook, audible hook, and text hook all triggered within the first three seconds.
Pass: All three present.
Fail: Any one missing.
Fires: Before any IG post is scheduled.

**BS Continuum Gate**
What it checks: Whether content is essential trust signaling or manipulation - red flags include artificial scarcity, vague claims, borrowed cultural equity.
Pass: Content is essential trust signaling; no red flags.
Fail: Any red flag present.
Fires: Before any IG or LinkedIn post ships.

**Allee Threshold Gate**
What it checks: Whether a new cluster has minimum viable density before activation.
Pass: Density confirmed; cluster ready for activation.
Fail: Insufficient density; all effort goes to existing clusters.
Fires: Before any new community or cluster is activated.

**Zero-Rate Gate**
What it checks: Whether any sub-network shows more than 30 percent non-response or no-show.
Pass: Zero-rate below 30 percent.
Fail: Zero-rate exceeds 30 percent; expansion paused until anti-network experience is fixed.
Fires: Weekly audit.

**Take-Rate Platform Gate**
What it checks: Whether a high-effort content platform is in an extraction phase.
Pass: Platform not in extraction phase; owned-channel priority maintained.
Fail: High-effort content distributed to extracting platform without owned-channel routing.
Fires: Before any major content investment on a third-party platform.

**Threads Hard No Gate**
What it checks: Whether any SNIPED content is being routed to Threads.
Pass: No Threads content planned; routing is LinkedIn plus Instagram only.
Fail: Threads activated as content surface.
Fires: At any content calendar planning session.

**Phase-1 Content Lock Gate**
What it checks: Whether content plans include only the three permitted Phase-1 streams - LinkedIn POV 1x/week, IG Carousel 1x/week, Stories daily on shoot weeks.
Pass: Only three streams active.
Fail: Cultural Doc carousel, Substack, BTS video, or separate Reels added in Phase 1.
Fires: At weekly content planning.

**Carousel vs. Single-Image Gate**
What it checks: Whether single images are being used appropriately - reserved for Art Series, statement portraits, and cultural-doc weight-carrying moments only.
Pass: Single images limited to approved categories.
Fail: Single image used for utility content that should be carousel.
Fires: Before any single-image post is scheduled.

**W3 Sacred Block Gate**
What it checks: Whether the 35-minute window before to 5 minutes after sunset (golden hour W3) is protected during shoots.
Pass: W3 block is untouched; cuts made from W1 and W2 if needed.
Fail: W3 block is cut or compressed; video shot in W3 when behind schedule.
Fires: During shoot-day scheduling and on-set when behind schedule.

**Audience-of-Audience Relevance Gate**
What it checks: Whether a published Card would create relevance for a Tier-0 founder's investor or advisor network if that founder reposted it.
Pass: Card is relevant to both founder and their network.
Fail: Card is relevant only to Bryce's direct audience.
Fires: Before any Card is published.

**Disconnected Virality Gate**
What it checks: Whether audience-growth bets have trigger frequency, behavioral residue, and reference-group validation before paid amplification.
Pass: All three habitat conditions confirmed.
Fail: Paid amplification sought without habitat proof.
Fires: Before any paid content amplification.

**Content Format Ratio Gate**
What it checks: Whether the content ratio holds at Judgment 2-3 per week, Proof 1-2, Behind Structure 1, Direct Offer every 10-14 days, Conversation Extract 1.
Pass: Ratio maintained.
Fail: Ratio violated.
Fires: At weekly content planning.

**Give-to-Ask Ratio Gate**
What it checks: Whether the last four outreach touches contain at least three gives before any ask.
Pass: Gives equal or exceed three of four touches.
Fail: Asks equal or exceed gives.
Fires: Before any ask or CTA is sent.

---

### LINEAGE, BRAND, AND INTEGRITY GATES

**Lineage Doctrine Veto Gate**
What it checks: Whether all Tier HOT and warm founder outreach has passed a lineage check.
Pass: Outreach is from inside one of the five lineages or clearly adjacent; single-visit cultural tourism refused.
Fail: Outreach targets a lineage the sender has not genuinely inhabited.
Fires: Before any Tier HOT DM is sent.

**Protocol Diagnosis Gate on DM Send**
What it checks: Whether the prospect's photo has been reviewed and a specific Direction Stack protocol number (not a template) has been selected before the DM is sent.
Pass: Photo reviewed; specific protocol number selected.
Fail: Template used without protocol selection.
Fires: Before any VIB DM is sent.

**Lineage Purity Gate**
What it checks: Whether documentation is produced from inside the lineage rather than from outside it.
Pass: Documentation is witnessed from inside; single-visit cultural reference refused.
Fail: Content is cultural tourism from outside the lineage.
Fires: Before any Cultural Doc, case study, or Direction Stack chapter ships.

**KOTS Program-Source Stats Gate**
What it checks: Whether every figure cited is verifiable from the official program book - 79 state champions, 215 schools, 140 out-of-state participants, two national champions.
Pass: All figures match official program book.
Fail: Any figure unverifiable or modified.
Fires: Before any KOTS-related public communication is sent.

**Dual-Track AI Authenticity Gate**
What it checks: Whether SNIPED client veto (no AI on client deliverables) and BASEPLATE authored-media tagging (disclosure for AI-generated world elements) are both respected per track.
Pass: Each track follows its specific rule.
Fail: AI applied to client identity layer in SNIPED track; or AI background shipped without disclosure in BASEPLATE track.
Fires: Before any composite or AI-assisted output is delivered or published.

**Freakiness Factor Rejection Gate**
What it checks: Whether any composite output exhibits faceless-AI-influencer impossible-anatomy optimizations.
Pass: No impossible-anatomy or identity-lock contradictions.
Fail: AI optimization present that contradicts SNIPED's identity-lock doctrine.
Fires: Before any Higgsfield or AI output is approved.

**Nomos Gate**
What it checks: Whether the output contains nomos - lived cultural practice, lineage participation, inherited obligation - rather than only physis (environment or world simulation).
Pass: Nomos present; real subject carrying lineage weight.
Fail: Pure physis; no lived cultural authenticity.
Fires: Before any Cultural Doc or lineage-claiming content ships.

**Authentic Brand Alignment Gate**
What it checks: Whether a partner's value system authentically aligns with the SNIPED audience.
Pass: Genuine alignment confirmed.
Fail: Alignment is superficial or commercially motivated only.
Fires: Before any partnership or co-branding agreement is signed.

**Dissemblement Gate**
What it checks: Whether the artifact is sincere or optimized purely for effect.
Pass: Honest version confirmed.
Fail: Artifact is optimized for effect at the expense of sincerity.
Fires: Before any artifact ships.

**Proof vs. Claim Gate**
What it checks: Whether the image alone makes the argument without the caption.
Pass: Image carries the argument; caption adds what image cannot say.
Fail: Image is claim-dependent; caption explains what is already visible.
Fires: Before any portfolio or grid post ships.

**Commandment Gate**
What it checks: Whether any positioning, brand, or mission change has been compared word-by-word against THE_SPINE.md to confirm no operational meaning has been inverted while surface language is preserved.
Pass: No inversion detected.
Fail: Meaning inverted while surface preserved.
Fires: Before any positioning or brand revision is finalized.

**Benjamin Activation Gate**
What it checks: Whether every OS doc read at session start produces a visible action - decision logged, thread updated, contradiction resolved.
Pass: At least one visible action per doc read.
Fail: Doc read without any action logged.
Fires: At end of each session.

**Boxer Trap Gate**
What it checks: Whether an effort escalation is responding to a directional problem rather than a legitimate execution gap.
Pass: Direction confirmed clear in CURRENT_STATE.md before effort escalation; escalation addresses a genuine execution gap.
Fail: Effort escalated while direction is unclear or while compounding a known misalignment.
Fires: Before any effort escalation decision.

**Moral Authority vs. Mechanical Advantage Gate**
What it checks: Whether positioning claims are grounded in lineage, trust, and proof rather than specifications alone.
Pass: Claims rooted in moral authority.
Fail: Claims rest solely on technical specs.
Fires: Before any positioning copy ships.

**Values Stampede Gate**
What it checks: Whether a new value or principle replaces an existing item or only adds to the list.
Pass: New value replaces an existing one; redundancy removed.
Fail: Value added without replacing anything.
Fires: Before any new doctrine or value is added to the OS.

---

### PRODUCTION AND SHOOT GATES

**Casting Confirm Discipline Gate**
What it checks: Whether the 24-hour confirmation with a four-hour reply window is followed, wardrobe photo received, two-strike rule applied.
Pass: Confirmation received within window; wardrobe photo on file; strike count tracked.
Fail: Any element missing or waived.
Fires: 24 hours before every shoot.

**Verification Gate (Tuna Sandwich Rule)**
What it checks: Whether cast, MUA, wardrobe, lighting, and retouching are all confirmed before production proceeds.
Pass: All five confirmed.
Fail: Any one unconfirmed.
Fires: T-48 hours before every shoot.

**Free-Shoot Return Mechanic Gate**
What it checks: Whether a written return mechanic exists before any free shoot is booked.
Pass: Written return mechanic documented; 60-day audit: zero return triggers pause of that category.
Fail: Free shoot booked without written return mechanic.
Fires: Before any free shoot is confirmed.

**Video/Stills Fallback Gate**
What it checks: Whether video is shed first when behind schedule on a shoot, protecting the W3 golden-hour block.
Pass: Video dropped first; W3 golden-hour block maintained.
Fail: W3 block compromised to preserve video.
Fires: During shoot-day scheduling when behind schedule.

**Retoucher Escalation Gate**
What it checks: Whether the retoucher is escalating rather than overriding the decision tree when encountering a frame that should be escalated.
Pass: Retoucher escalates; does not proceed.
Fail: Retoucher overrides decision tree and applies treatment to a frame that should have been escalated.
Fires: During retoucher review of any deliverable.

**Retoucher Authority Ceiling Gate**
What it checks: Whether the retoucher is staying within their lane - no color labels, no hero promotion, no preset tweaks, no decision-tree deviation.
Pass: Retoucher operates within ceiling; escalates at any boundary.
Fail: Retoucher performs any of the four prohibited actions.
Fires: During retoucher handoff review.

**4-Pass Cull Standard Gate**
What it checks: Whether the cull follows the four-pass protocol: Reject, Pick, Star, Heroes.
Pass: All four passes completed in sequence.
Fail: Passes skipped or merged.
Fires: Before any images are submitted for retouching.

**Heel-Finishing Spec Gate**
What it checks: Whether the 15-minute Photoshop heel finish passes the phone-scale 100 percent credibility test.
Pass: Finish credible at 100 percent zoom on phone screen.
Fail: Finish does not pass credibility test.
Fires: Before any heel-visible image is delivered.

**Direction Stack Diagnostic Gate**
What it checks: Whether the Direction Stack diagnostic has been run before any shoot begins.
Pass: Diagnostic complete; protocol selected; no mid-shoot scope additions.
Fail: Shoot begins without diagnostic.
Fires: At the start of every shoot.

**Concept-First Before Palette Gate**
What it checks: Whether a one-sentence thesis statement exists before any palette or aesthetic direction is locked for a shoot.
Pass: Thesis statement written and confirmed.
Fail: Palette locked before thesis exists.
Fires: Before pre-shoot prep is finalized.

---

### ACQUISITION AND BUSINESS IDEA GATES

**4-Question Concept Route Filter**
What it checks: Whether a proposed concept scores adequately on proof-loop fit, operator-coded register, lineage doctrine, and environment fit.
Pass: Score of 4 executes immediately; 3 adjusts; 2 defers; 0-1 vaults.
Fail: Score below 2 without vault parking.
Fires: Before any new concept is developed.

**4-Question Event Filter**
What it checks: Lane fit, reciprocity, time cost, and identity check.
Pass: All four affirmative; Day 0-30 cadence locked.
Fail: Any one negative; event declined.
Fires: Before any event engagement is confirmed.

**3-Question Business Idea Filter**
What it checks: Does the idea advance an existing locked lane? Does it serve the Year-10 state? Does it survive the five-step proof gate?
Pass: All three affirmative.
Fail: Any one negative; idea vaulted with reopen condition.
Fires: Before any new business idea is developed.

**Sniped Acquisition Gate**
What it checks: Four-question filter - refuse-list, saturation audit, Gap Map tier fit, proof-loop dependency.
Pass: All four pass.
Fail: Any one fails; acquisition declined.
Fires: Before any new capability or tool acquisition is considered.

**Opportunity Transformation Gate**
What it checks: Whether an incoming opportunity has been diagnosed against the 20-field diagnostic before routing to one of nine fates.
Pass: Full diagnostic complete; fate assigned.
Fail: Opportunity acted on without diagnostic.
Fires: At intake of any external opportunity.

**Network Opportunity Filter**
What it checks: Five questions - reciprocity, operator-coded fit, lane fit, trust transfer, time cost.
Pass: Four or more affirmative.
Fail: Fewer than four; engagement declined.
Fires: Before any strategy call is scheduled.

**Money Urgency Speed-Lever Gate**
What it checks: Whether the fastest legitimate revenue path has been identified before any discount trigger is considered.
Pass: Speed-lever path identified (escrow, warm lead, VIB queue, cold fresh); $1,500 floor holds.
Fail: Discount offered without exhausting speed-lever options.
Fires: At any money-urgency request.

---

### KOTS AND INSTITUTIONAL GATES

**KOTS Institutional Reframe Gate**
What it checks: Whether evidence supports treating KOTS as a Vanguard/Marion County institution rather than an Eric Jones production.
Pass: Principal engagement, school committee structure, revenue share agreement on record.
Fail: Institutional framing claimed without structural evidence.
Fires: Before any KOTS public communication or institutional outreach.

**KOTS Final-Six Field Selection Gate**
What it checks: Whether Eric Jones has supplied the final six school names or selection criteria, coach contacts, true status of all 10 named schools, and a confirmation deadline.
Pass: All four elements supplied.
Fail: Any one missing; field selection deferred.
Fires: Before any KOTS field-selection decision is finalized.

**Family Monetization Gate**
What it checks: Whether the two-week post-event waiting period has passed before any family monetization decision is made.
Pass: Two weeks post-event; gated business decision confirmed.
Fail: Decision made before two-week window.
Fires: At the two-week post-event checkpoint.

**BASEPLATE Institutional Structure Pre-Gate for KOTS**
What it checks: Whether committee approval of BJ's media role, the principal conversation, the Coach Jones timing, and the EIN gate are all cleared.
Pass: All four confirmed.
Fail: Any one missing.
Fires: Before any KOTS media execution begins.

---

### FINANCIAL AND CAPITAL GATES

**Margin of Safety Gate**
What it checks: Three questions - Is there intrinsic value floor? Is the proposed price or investment below intrinsic value? Is there meaningful margin between them?
Pass: All three affirmative.
Fail: Any one negative.
Fires: Before any capital or time deployment decision.

**Worst-Case Math Gate**
What it checks: Whether the literal floor - financial, reputational, relational - is survivable.
Pass: Floor survivable; upside real.
Fail: Floor not survivable.
Fires: Before any major commitment.

**Power-Law Bet Gate**
What it checks: Whether maximum success from the proposed bet generates 10x or more in reputation, revenue, or cultural authority.
Pass: 10x potential confirmed.
Fail: Modest win only; bet classified as distraction.
Fires: Before any major strategic or capital commitment.

**Domain-Specificity Gate**
What it checks: Whether any capital or time deployment is in an exact domain match.
Pass: Exact domain match confirmed.
Fail: "Adjacent" or "promising" used as justification.
Fires: Before any capital or time deployment.

**Analog Premium Gate**
What it checks: Whether a proposed physical or constrained offering has physical/constrained scarcity, ownership signal, ritual or tactility, and digital amplification rather than digital replacement.
Pass: All four present.
Fail: Any one absent.
Fires: Before any analog or premium physical product is developed.

**Earned Scarcity Gate**
What it checks: Whether any scarcity signal is based on real constraints rather than manufactured urgency.
Pass: Scarcity is real (limited calendar, seven environments, genuine capacity).
Fail: Manufactured urgency without structural basis.
Fires: Before any scarcity claim is made in copy or outreach.

---

### COGNITIVE AND DECISION GATES

**HALT Decision Gate**
What it checks: Whether the operator is hungry, angry, lonely, or tired.
Pass: None of the four states active; decision can proceed.
Fail: Any one state active; decision deferred until state restored.
Fires: Before any high-stakes decision, negotiation, or client-facing communication.

**False-Mind Detection Gate**
What it checks: Whether a decision is driven by original mind (clarity, lineage, proof) or false mind (ego, comparison, scarcity, trend).
Pass: Original mind confirmed.
Fail: False mind detected.
Fires: Before any major creative, strategic, or composite prompt decision.

**Culminating-Point Gate**
What it checks: Whether scene depth has peaked and returns are diminishing, requiring a deepen-versus-transition decision.
Pass: Depth not yet at peak; continue.
Fail: Past diminishing returns; transition evaluation triggered.
Fires: Quarterly at strategic review.

**Cognitive Distortion Audit Gate**
What it checks: Whether any of 17 CBT distortion patterns are active before a major strategic decision.
Pass: No active distortions.
Fail: One or more distortions active; decision deferred.
Fires: Before any major strategic move.

**Grandiosity Gate**
What it checks: Whether a major win has triggered unbroken success plus flattery exposure plus reduced accountability.
Pass: At least one honest-audit touchpoint exists in the post-win period.
Fail: All three hubris conditions present without counter-structure.
Fires: After every major win before any expansion commitment.

**Ruling-Part Gate**
What it checks: Whether a decision subordinates reason to external validation, scale lust, or short-term comfort.
Pass: Decision grounded in doctrine, not praise or comfort.
Fail: Any of the three influences present.
Fires: Daily at session start; before any major decision.

**Flattery Hazard Gate**
What it checks: Whether any recent decision was influenced by praise rather than doctrine.
Pass: Doctrine-based reason exists independent of praise.
Fail: Praise is the operative reason.
Fires: Biweekly review; before any expansion decision.

**Suitcase Problem Gate**
What it checks: Whether any locked doctrine phrase has calcified - gap between the name and the actual living discipline.
Pass: Doctrine phrase matches lived behavior confirmed by recent evidence.
Fail: Phrase repeated without behavioral evidence.
Fires: Quarterly at doctrine audit.

**Director Tyrant Gate**
What it checks: Whether locked frameworks are becoming permanent tyranny rather than productive constraint.
Pass: Frameworks still animating; not restricting.
Fail: Frameworks creating restrictions without producing growth.
Fires: Every 90 days.

**Full Engagement Before Direction Gate**
What it checks: Whether a full OS read has been completed before any lane is crowned or any final direction is given.
Pass: Full OS synthesis complete; no partial findings treated as authority.
Fail: Direction given from partial OS engagement.
Fires: Before any major strategic direction or lane recommendation.

---

### NAMING AND BRAND EXTENSION GATES

**Sniped Naming Gate (7-Variable)**
What it checks: Seven conditions - .com available, no major brand or app ownership, trademark category clear, regional and cultural sensitivity clear, linguistic safety confirmed, longevity test passed (not trendy), empty-vessel risk assessed.
Pass: All seven pass.
Fail: Any one fails.
Fires: Before any brand, product, or lane name is proposed.

**SMILE + SCRATCH Gate**
What it checks: SMILE criteria (Simple, Meaningful, Imagery, Legs, Emotional) and SCRATCH criteria (Spelling, Copycat, Restrictive, Annoying, Trendoid, Curse of Knowledge, Hard to pronounce).
Pass: SMILE met; SCRATCH avoided.
Fail: Any SCRATCH criterion violated.
Fires: Before any name is presented.

**Line Extension Gate**
What it checks: Shopping List Test (does the name survive being put on an unrelated product?), Teeter-Totter check, and Multibrand trigger.
Pass: All three pass.
Fail: Any one fails.
Fires: Before any SNIPED house name is extended to a new product.

**Prestige-Symbol Collapse Gate**
What it checks: Whether a new distribution or pricing move is collapsing prestige signals into commodity.
Pass: Scarcity and prestige architecture maintained.
Fail: Upstream prestige signals moved downstream.
Fires: Before any new distribution or pricing tier is announced.

**Touchpoint Coherence Gate**
What it checks: Whether all 30-plus touchpoints across every SNIPED surface are coherent with the Brand Brief.
Pass: All surfaces coherent.
Fail: Any surface contradicts Brand Brief.
Fires: Before brand launch, client delivery, or portfolio refresh.

---

### LEGACY AND INSTITUTIONAL GATES

**Succession Clarity Gate**
What it checks: Whether any lane or SOP can be executed from documentation alone without Bryce present.
Pass: Documentation sufficient for successor execution.
Fail: Lane or SOP requires Bryce's presence.
Fires: Before any lane is taken to market; at quarterly SOP review.

**Institutional Senility Gate**
What it checks: Whether any OS process is still solving a real problem or has become ceremonial.
Pass: Process produces value; not ceremonial.
Fail: Process ceremonial, triggering disdain or consuming hours without client value.
Fires: Annually at OS review; at any performance plateau.

**Estate Clarity Gate**
What it checks: Whether KOTS revenue or SNIPED institutional IP has legal structure before scale.
Pass: Legal structure in place before scaling begins.
Fail: Scaling proceeds without legal structure.
Fires: Before any KOTS or SNIPED institutional IP is scaled.

**Endorsement Due-Diligence Gate**
What it checks: Lineage alignment, public record, controversies, reputational asymmetry.
Pass: All four clean.
Fail: Any one problematic.
Fires: Before any public co-sign, partnership announcement, or endorsement.

**IP Ownership Gate**
What it checks: Whether SNIPED retains copyright, territorial scope is confirmed, and contributor rights are clear.
Pass: All three confirmed.
Fail: Any one unresolved.
Fires: Before any licensing, partnership, or publishing deal is signed.

**Domain Protection Gate**
What it checks: Whether snipedmedia.com is protected and all cold outreach routes through a variant domain.
Pass: Brand domain protected; cold outreach on variant domain.
Fail: Cold outreach routed through brand domain.
Fires: Before any cold email campaign is launched.

---

## DECISIONS

### HOW THIS SECTION IS ORGANIZED

Six capability domains with interlock logic. Every entry reports what is known; no lane is crowned. The possibility engine stays open per global guardrail.

---

### 1. CHOOSING OPPORTUNITIES

**Core filter (non-negotiable before any new lane or initiative):**

- **Opportunity cascade gate** (Kelly): any proposed artifact or lane must generate 2+ downstream opportunities before resource commit. Single-outcome work is closed-loop; cascade work is compounding.
- **Boat-quality gate** (Marks): before any new client type, assess structural growth or decline in the segment. Entering declining boats with superior execution still loses.
- **4 Yes Test / Keenan commitment gate**: problem exists, buyer agrees, buyer wants fix, buyer will join journey. All four required before booking creative work.
- **Otaku density gate** (Godin): target market must have 5+ willing proselytizers in sub-market. Below that threshold, prove a single node first.
- **Sniped 7-questions audit** (Thiel): Engineering, Timing, Monopoly, People, Distribution, Durability, Secret. Run before any significant lane commitment.
- **Market-evaluation scorecard**: 10-factor go/no-go. Score below 50 = walk. 50-75 = mitigate. 75+ = commit.

**Opportunity routing:**

- **9-fate framework** (OS_TRANSFORMATION_ROUTER): every inbound classifies as favor, paid-service, SNIPED, BASEPLATE, separate-venture, declined, referred, proof-loop, or codified-template. Unclassified = not actionable.
- **Sniped-opportunity-cascade-audit**: routes every proposed artifact through Kelly network-value principle. Firm value vs. marketplace value vs. network value.
- **Sniped-gates-function**: five-question triage before any inbound is accepted or advanced.
- **Fire-triage**: session-start routing: Distribution blocking revenue > Product blocking distribution > Revenue model > Ops > Competition.

**Opportunity suppressors (hard stops):**

- **School and event photography**: decline cleanly. Off-thesis, low ceiling. Batch-004/006 locked.
- **No new strategic frameworks or new lanes until July 2026**: architecture set, execution phase active.
- **Pre-scaling gate**: no new tool, channel, hire, or lane until MVE delivers a closed and delivered Reset plus testimonial plus Op Kit pitch plus one surfaced SLA failure.
- **Canada Principle gate**: new lane must pass moat-dilution, operational-muscle, revenue-structure, founder-time, and repetition-lock checks.
- **Enough gate** (Housel): does scope expansion increase baseline cost before prior proof? Does it move the goalpost before confirmation? If yes, halt.
- **Culminating-point audit**: confirm not past diminishing depth returns before expansion. Quarterly.

**Open decisions on opportunity selection (not crowned):**

- Which revenue lane gets proof first: cannot be determined from doctrine; requires June-July 2026 proof-cycle data.
- BASEPLATE as standalone cash vertical: 14-day $2,500 repeatable product is architecturally ready. Q3 2026 capacity allocation decision pending.
- KOTS cash vertical status: live vertical or holding pattern; pending Dad conversations and school committee structure.
- Three-party brand-funded production model: track-not-build. Pre-condition: scene density must reach brand-relevant founder segment threshold.
- IP licensing hypothesis: composite environments, Direction Stack, edit register are licensable. Logged as live hypothesis; pending proof.
- Photography community platform: post-proof only. Not activated.

---

### 2. PROTECTING OPTIONALITY

**Global guardrail (load-bearing across every batch):**

The possibility engine stays open. Identity emerges from proof, not positioning. Six lanes remain live: SNIPED, BASEPLATE, Founder portraits, AI workflows, Premium visual systems, School-event-photo infrastructure. None is crowned by doctrine, pattern library, or confident old doc. Old work informs, current proof decides.

**Specific optionality protections in force:**

- **No premature lane lock**: Bryce is operator, engineer, photographer, consultant. All roles held open. Proof earns authority.
- **BASEPLATE = live hypothesis**: name is filed, thesis and buyer target remain falsifiable through June 2026 checkpoint. Not the locked throne.
- **Sovereign identity gate**: any public positioning decision that crowns one lane permanently or reduces exit optionality fails the gate. Reframe as one lane among open lanes.
- **Formlessness check**: before commitment, is it reversible? Does it hand competitors a fixed target? Does it close optionality? One yes = hold.
- **Pattern library vs. operative doctrine distinction**: biography, classical strategy, finance, literary, media-business patterns inform. They do not finalize identity or lane.
- **Synergy architecture gate**: activation touching fewer than 3 surfaces simultaneously underutilizes the asset.
- **Positioning ceiling audit**: periodic check of brand language against TAM ceiling risk. Candidate reframes, larger-category options, optionality flag.

**Optionality and timing:**

- **Director tyrant check**: mandatory 90-day revisit. Locked doctrine must be tested against current evidence; if restricting movement without cause, knife it.
- **Doctrine creep gate**: every spine-invoked decision survives contact with current market evidence. Old work informs; current proof decides.
- **Director-revisit-gate**: 90-day repetition doctrine is correct; mandatory revisit gate appended every 90 days to prevent Cathedral becoming tyrant.
- **Mentor-separation check**: quarterly evaluation of any ongoing framework, tool, or doc. Animating, plateauing, or restricting? Apply the knife naturally.

**Resolved optionality conflicts:**

- "Repetition over Novelty" governs strategic frameworks and architectural positioning. Tactical methods re-evaluate quarterly. Architectural lock and tactical adaptation are separable.
- "Full engagement before direction" remains mode for identity and lane questions. Naming a structural posture (Rich vs. King) is not crowning identity; it is setting a decision filter.
- "Build internal-tight before market" does not mean indefinite delay. Requires defined readiness threshold: minimum proof package justifying first offer. Not open-ended.

---

### 3. MONEY

**Floor and pricing architecture (non-negotiable):**

- **Reset floor**: $1,500 minimum. $750 deposit only. First-three-at-$1,000 is time-boxed exception only. Triple-confirmed (Kahneman Prospect Theory, Airey studio minimums, Wheeler case studies). Never lower. Scope flexes; price does not.
- **Sprint $750 tier**: warm-referral-only segmentation gate. Cold inbound stays $1,500 floor.
- **Payment follows proof**: EIN/LLC/bank imperfection = admin cleanup. Waterfall to fastest legit link now. PayPal, Square, link, Zelle, Venmo, bank transfer. Stripe gated until EIN legal-name correction live.
- **No fake progress**: reading, tooling, free interest, compliments, registry-before-payment are named anti-patterns.
- **Proof-log discipline**: REAL PROOF = money committed or access granted + named role/bid. FAKE INTEREST = praise, "send info," no door opened. Log every touch.
- **EIN gate DOWNGRADED to P3 admin cleanup**: not a money blocker. Selling, deposits, invoicing proceed now via sole-prop, personal, Stripe, PayPal, Square, link. Cleanup after proof.
- **Phase-B trigger**: multi-criteria gate (all four): $3K/month x 2 consecutive months + 5 Resets + first Op Kit pitched + cash reserve above $3K.

**Pricing escalation logic:**

- **$20K to $50K lever sequence**: price raise first, retainer add second, client reduction third, high-ticket project fourth.
- **Wedge offer pricing locked**: Pilot $2,500-4K, Standard $6-10K, Premium $15-25K (Capability Dossier).
- **Three-option architecture**: Option 1 meets ALL stated objectives. Options 2 and 3 add cumulatively. No a la carte. Price verbally before written. No publishing specific prices for customized services (Enns Rule 1).
- **Anchor before proof**: set positioning language, editorial refs, and named-client proximity before proof artifact. Proof lands into high anchor.
- **Mercedes-Benz Syndrome**: underpricing is a brand contradiction. Premium signals lower risk, not higher cost.
- **Value-based pricing**: price against generatives (Embodiment, Authenticity, Interpretation), not market rates. Weiss 10:1 ROI floor.
- **Oral price first** (Enns Rule 4): locked protocol, not suggestion. Float range on discovery call before written proposal. Surface objections early.
- **Decoy integrity**: decoy must be genuinely inferior on one attribute, superior on none.
- **Scarcity as cost-free demand signal**: waiting list plus full-capacity announcement vs. margin-eating discounts.

**Revenue structure and cash management:**

- **Phase-1 revenue targets**: Month 3 = $3K, Month 6 = $5K, Month 9-12 = $10K. Capacity-gated 8-15 hours per week.
- **Milestone billing**: 30% upfront + 30% mid + 40% delivery, protects working capital on $1,500 floor. Sub-30-day payback required before VIB v2, Op Kit v2, or Brand System launch.
- **Early-pay framing**: 2/10 Net 30 = 36.7% annualized ROI for client. Frame as exclusive-access psychology.
- **Retainer cash-flow hardening**: invoice in advance (first of month before service delivery). Stop work at 30-day non-payment.
- **Op Kit MSA auto-renewal**: 12-month commercial license + 30-50% auto-renewal at 30-day opt-out window. First structural recurring revenue mechanism.
- **Wage separation**: revenue pooling account + fixed personal draw + expense deduction + profit allocation + lifestyle ceiling declaration. Not optional.
- **Capital hygiene stack**: SPAXX for idle cash (4.96%), Roth IRA funded annually, emergency fund at 3+ months.
- **Passive income benchmark (long-run)**: 75% from Direction Stack book, courses, mentorship.
- **KOTS structured cash vertical**: Year-1 income ceiling $10K-$19.5K from 4-day trip. Six-line B2B2C stack. Recurring $1,500 retainer. Transferable model.
- **Quarterly Visual Management Retainer** ($750/quarter): pre-staged in Pixieset. Not yet activated in outreach or cold email. One half-day per quarter, 15 retouched images, no rollover.
- **Passive licensing revenue**: existing composite environments currently unlicensed. Archive as asset class. Secondary licensing can exceed original commission.

**Revenue contradictions requiring resolution:**

- **Founder Kit ($12,500) vs. Reset ($1,500)**: Spine locks Reset at $1,500 floor. Shelf introduces Founder Kit at 8.3x. Is FK the new flagship, the upsell, or a parallel lane? Explicit resolution required before it enters any outreach.
- **LA Photography Operator Kit ($4K-$8K) vs. Founder Kit ($12,500)**: Phase-1 Plan (April 2026) governs. Prior doc likely superseded. Confirm and retire.
- **ICP bifurcation conflict**: THE_MACHINE locks law firms as core ICP. Channel Alignment Plan proposes Series A-C founders. Which is primary revenue lever in 2026?
- **Payment split conflict**: 50/50 single session vs. 40-30-30 multi-deliverable vs. 25-50% ranges coexist. Formalize as context-dependent by scope type.

---

### 4. CREATIVE

**Identity lock / world variable (load-bearing):**

- Face, body, skin texture: untouched across all output. Categorical, not per-project.
- Hair styling and clothing: variable. World and environment: variable.
- This is grammar-level AI defense: light from sensor from this person at this moment. AI generates environments. Both real. Different jobs.
- "Sculpted AI" replaces binary "anti-AI": AI for world-construction, environment generation, motion transfer. Human for identity lock, in-camera primacy, skin and face retouching.
- No AI identity-touch ever ships. Applies across all 8 AI and motion engines regardless of quality.

**Visual direction lock (LOCKED 2026-05-12):**

- Meisel, Roversi, Mert and Marcus lane. Not Tadder, not jpwphoto cinematic.
- Adobe Neutral as single import baseline.
- No teal, no orange. Restraint over volume.
- v3 LUXURY is the floor and current working register. Evolves through reps and operator sign-off, not doc revision.
- Grain: v3 LUXURY locked preset (amount 12, size 25) is authoritative. Overrides v1 no-global-grain rule.
- Film fade signature (blacks 0-8/10/5 lift, grain mandatory even in Studio): visual identity, not style choice. Promote to locked visual direction doctrine.

**Composite environment system (LOCKED 2026-05-12):**

- 7 environments: Brutalist Monument, Industrial Minimal, Monochromatic Void, Sculptural Gallery, Cinematic Urban, Organic Surreal, Futurist Editorial.
- One per chapter. Constrained world-building beats random AI prompts.
- Environment selection is a gestural decision, not a visual-variety choice. Each environment encodes specific gestural logic (confinement vs. freedom, brutalist density vs. void).
- Composite environment rotation: Airtable rotation log read before dispatch. Write after.
- Composite QA: mandatory before any client delivery. 11 gates. Gates 9-11 (DOF/lens match, perspective/camera-height, directional color bleed) = ceiling/client-ready. Gate 8 hard reject: AI smear, warped geometry, barcode sky, melted plants.
- Visual Structure Bible: Block 7-component spec applied to each of the 7 composite environments. Every shoot and comp references it.
- Platform mastering: mandatory between composite approval and publishing. Includes numeric skin-drift test. Not discretionary.

**Evoto and Photoshop scope (RESOLVED):**

- Evoto handles all 8 capabilities for Brand System tier (color match, backdrop optimization, perspective, frequency separation, dodge-burn sculpt, AI culling, tethered shooting Phase B+, cloud sync).
- Photoshop = Track B environmental compositing only.
- Slider restraint: 30-75% editorial range. No slider at 100% ships without explicit override justification.
- Preserve-first is mandatory editing doctrine. Flatten-and-rebuild on skin never acceptable.

**Composite workflow tooling (RESOLVED):**

- Path A (Firefly Generative Fill + Reference Image) = Photoshop default for in-Photoshop compositing.
- Path B (Higgsfield, Seedream, Nano Banana Pro) = external plate generation. Better register in some environments.
- Direct-prompt Firefly deprecated.
- Empty-prompt-first reverses Firefly default. Verbose prompts invite hallucination.
- 6-attempt cap before escalation to manual or documentary.
- Generative Fill: no seam, tonal match within 5%, no hallucinated objects, no texture loops, maintained DoF. 5 checkpoints before variant selection.

**Seedream model routing (locked):**

- 5.0 Lite = plates. 4.5 = portraits. Nano Banana Pro = identity-preserving subjects.

**Preset library:**

- 9 masters: Avedon, Eggleston, Leibovitz, Shore, Herzog, Frank, Meyerowitz, Haas, Iturbide.
- Retouch depth is frame-driven (lane plus master selection), not blanket.
- Lightroom as locked machine: 16 rails, immutable annual system.

**Content and production direction:**

- Concept-first before palette (Leibovitz): name thesis statement before palette lock on any portrait or chapter shoot.
- Direction Stack = BJ-only non-delegable: diagnostic runs as conversation, not form. No template, no automation, no proxy.
- Posing: Seven Posing Points, Three-Pillar structure. Body angle standing direction order: 15-30 degree offset, head back to lens.
- Hands: images where hands show grip or tension fail the strongest-photograph gate. Three locked solutions: crop tight shoulders-up, hand on shoulder, hands in pockets or lapels.
- W3 (golden hour 0:35 before to 0:05 after sunset) is sacred. If cuts required, cut W1/W2, never W3. Video is first shed if behind.
- Extended-shoot protocol: all commercial shoots add 15-20 minutes unstructured buffer post "final shot." Log buffer frames separately.
- Trafalgar selection: one editorial-memory image per composite chapter. Mid-sequence, non-hero.

**B&W Card dual-register (LOCKED 2026-05-13):**

- HERO posts = full v3 LUXURY color. Chapter Card images = B&W. Apparatus stays color. Apparatus layer framing per Aperture, LIFE, Magnum tradition.
- B&W is prestige sidecar, not default. Color leads conversion.

**Cultural documentation:**

- Elevated to primary long-term positioning axis. 10-year archive horizon, 5 subject ecosystems, monthly cadence. Not optional.
- Monthly 30-50 frame shoot + carousel + essay. Quarterly thematic mini-essay. Annual archive review.
- Direction Stack book launch deferred until 3-5 Resets closed. Q3 2026 timing confirmed safe.

**Leonardo AI:** internal alignment only. Never delivered or published without "reference" framing.

**Creative contradictions (pending resolution):**

- Depth mechanism gate: Shore panfocus vs. Meyerowitz atmospheric are opposite physics. Both untested in SNIPED production. Test before SOP adoption.
- Found-color bifurcation gate: mark OPEN until one found-color personal session logged.
- Direction Stack triple-version reconciliation: Final_Manuscript = canonical narrative source. FINAL_PRINT = print-production file. File creation date check needed to confirm UPDATED label supersedes FINAL_PRINT.

---

### 5. OPS

**Core operating model:**

- **Execution Governor**: 12-step runtime dispatch, session-start and session-end protocol. Default response is action, not report.
- **Session start**: read CURRENT_STATE.md, ACTIVE_THREADS.md, SESSION_LOG.md tail, check _inbox/admin.
- **Session end**: update all three files. If state is not on disk, it does not exist.
- **ACTIVE_THREADS stale-state protocol**: Monday Cockpit includes ACTIVE_THREADS reconcile checkpoint. 16-day gap = execution-governor failure.
- **Open-loop check**: reads CURRENT_STATE + ACTIVE_THREADS + SESSION_LOG. Flags 7+ day stale threads. Session-start gate.
- **Fire-triage hierarchy**: Distribution blocking revenue > Product blocking distribution > Revenue model > Ops > Competition.
- **Monday/Saturday operational split**: Monday = 3 outcomes plus cadence only, no new strategy. Saturday = infrastructure and systems.

**Tool-routing (Connected Toolchain Default, LOCKED 2026-05-28):**

- Tool-first routing: connector, API, MCP, skill, script, browser. Manual is fallback after toolchain audit returns no path.
- 11-step audit required before claiming "do this manually."
- TOOLCHAIN_ACTIVATION.md is single source of truth.
- skills-sh-finder mandatory pre-build check before any custom automation build.
- Manual-first assumption is killed.

**CRM and lead tracking:**

- Airtable is primary CRM until Notion proves daily use by Day 30. Notion MCP P1 open decision unresolved.
- Account Status bins: Cold, Warming, DM Opened, Call Booked, Proposal Earned, Booked, Delivered, Referral Active.
- Proof-log entry mandate: every send, reply, call, objection, paid outcome logged. Schema: date, contact, touch-type, response, money-flag, room-flag.
- Sent DM artifact system: YYYY-MM-DD_recipient-handle.md files with status field (drafted, sent, replied, dead, converted) in _sent_dms/. Aggregates reply rates and conversion rates without third-party CRM.

**Outreach stack (locked):**

- LinkedIn comment-to-DM = primary funnel for LA founder segment.
- Instantly + Super Search + cold-email gold doc = cold outbound. Not generic email scrape.
- VIB queuing lockdown: 3 VIBs queued by Monday EOD, sent Tuesday/Wednesday/Thursday.
- VIB re-scoped from default to conditional: prospect warrant check required before VIB asset build. Ship cold email if no warrant.
- Cold email reply SLA: Positive 2-hour (30-minute target), Questions 4-hour, Deflections 24-hour. Unibox 3x daily (9 AM, 1 PM, 5 PM).
- Rule of Three: 3 exposures before preference locks. Design all outreach sequences around 3-touch minimum.

**Production OS (load-bearing anchor):**

- Folder lock, naming lock, storage tiering Hot/Warm/Cold.
- 5-pass cull: Reject, Pick, Star, Heroes. Hero retouch precedence 12-15 minutes each.
- v2 delivery architecture: 3-tier Heroes/Selects/Proofs with 14-day natural expiry. Upsell unbundled: Path A Select-to-Hero $60/image, Path B Proof-to-Select $30/image, Path C commercial license $250-3K.
- Casting call doctrine: 24-hr confirm, wardrobe photo gate, two-strike permanent removal, tier-2 standby pre-stage, 48-hr MUA confirm.
- Retoucher authority ceiling: no color labels, no Hero promotion, no preset tweaks, no decision-tree deviation. Escalate instead.
- Retoucher hire gate (Phase B): 30+ Heroes per month x 2 months sustained. Calendar-month qualification. CURRENT_STATE.md governs.

**Constraint management:**

- Single constraint identification: monthly kill gate. Fix the one binding constraint; subordinate everything else.
- Constraint Audit cadence: monthly constraint kill gate + quarterly TAM/offer-ladder/aesthetic check + annual spine recalibration.
- Weekly loop locked: Tuesday/Thursday LinkedIn POV, Wednesday IG carousel, 5-10 VIB messages, 1 shoot/follow-up/case-study, 1 Notion update, 1 backup verify.
- Hard NOs in Phase 1: Substack, retoucher hire, print module, AI headshots (never), Buffer (Phase B gate).

**Automation discipline:**

- Automate only after question, delete, simplify sequence (Musk de-automation doctrine).
- Batch before individual: every repeatable SNIPED operation has batch workflow designed before scaling.
- Phase-1 content locked to three streams only: LinkedIn POV 1x/week + IG Carousel 1x/week + Stories daily on shoot weeks.
- Ingest as propose-and-await: never auto-mutate. No OS mutation without BJ approval.

**OKR cadence:**

- Committed vs. aspirational OKR taxonomy: committed = 1.0 required with postmortem if missed. Aspirational = 0.7 is success, carries forward.
- Paired KR rule: every output-volume goal pairs with quality counter-measure. No standalone volume OKRs.
- Weekly OKR tracking routed to SESSION_LOG update.

**SOP and doctrine maintenance:**

- Requirement-owner gate: every SOP step has named owner or is deletion candidate.
- Handle-suitcase gate: locked doctrine tested in last 90 days? Live behavior or repeated phrase?
- Named-system registry: name, lock date, version, disk location, description. Every recurring workflow.
- Barnacles doctrine: quarterly prune of unused, revenue-free, or complexity-without-moat OS components.

**Ops contradictions requiring resolution:**

- Reset SLA 5 vs. 7 vs. 10 days: CURRENT_STATE.md governs. Manual audit required before enforcement.
- Notion schema decision gate: Wave-1 vs. pre-Wave-1 spec unresolved. Overlaps in Pipeline/Deals, Clients/Contacts. Operator resolution required before any write.
- Synthesis vs. Repetition-over-Novelty tiebreaker: when full OS synthesis contradicts 90-day rep freeze, protocol is missing. Recommended: synthesis completes at session start, then freeze applies unless external forcing function. Codify in EXECUTION_GOVERNOR.
- Google account bridges: personal Google plus admin@snipedmedia.com authed for Drive and Calendar are TEMPORARY bridges. No cross-account file moves. No mutations that anchor personal account as BASEPLATE workspace.

---

### 6. DELIVERY

**Delivery pipeline (locked architecture):**

- v2 delivery architecture: Heroes/Selects/Proofs in 2-3.5 hours. 8-12 Heroes, 30-40 Selects, 60-100 Proofs. 14-day natural gallery expiry.
- Hero retouch gate: client picks from proofs (Gate 2) MANDATORY before hero retouch begins. Proofs at sRGB JPEG 2048 long edge, 70-80 quality.
- Proof-only delivery gate: no high-res, no finals, no heroes, no retouch, no internal files at proof stage. Client confirm before hero pass. TEST vs. REAL folder isolation enforced.
- Pixieset Additional tier: promoted to contracted delivery slot, not optional. $80/image x 10-15/Reset is revenue lever. 48-hour upsell window enforced. Day-19 conditional send gate: send ONLY if client opened gallery AND has not yet purchased upgrade.

**Post-delivery revenue sequence (8-step cadence):**

- Day 0: gallery delivery and hospitality gesture.
- Day 7: testimonial ask.
- Day 30: Op Kit pitch with specific Reset observation + specific gap closure + Op Kit value map + pricing tier + Calendly link.
- Day 45: referral drip trigger (automated).
- Referral-ask timing: send only after testimonial received AND photos deployed AND social signal visible.
- Op Kit MSA auto-renewal: 12-month commercial license + 30-50% auto-renewal at 30-day opt-out window.
- Fulfillment is a sales engine: measure fulfillment quality impact on repeat rate and referral rate, not cost per hour.
- Retention and referral tracking belongs in revenue architecture: expands 3-engine model (Revenue, Audience, Reputation) to include post-sale repeat mechanics.

**Quality gates (delivery-critical):**

- **Strongest photograph != most processed** (LOCKED 2026-05-28): automated output must beat source visually, not just complete task. Failed cleanup artifacts are worse than honest studio context. Mandatory reject gate on every treatment pass.
- **Composite Master QA** (LOCKED 2026-06-02): proof crops at 100% (hair, feet) + 6-axis scorecard (lighting, grounding, edge-hair, color-marry, artifact, brand-fit, each out of 10) mandatory before client or deck entry. Every axis 8/10 minimum.
- **Platform mastering** (LOCKED 2026-06-02): color + B&W per aspect per safe-area. Contrast, sharpen, text applied. Skin-drift measurement mandatory. Not discretionary.
- **Heel-finishing spec gate**: 15-minute Photoshop finish. Phone-scale 100% credibility test is pass criterion.
- **AI composite disclosure gate**: Reset MSA, Op Kit MSA, Collab Agreement are currently silent on AI-generated backgrounds. Unified disclosure addendum required before composite-inclusive gallery ships.

**Client experience and hospitality:**

- Hospitality compounds separately from service: service = delivery SOP. Hospitality = reputation compounding above SOP. Budget-neutral moves signal outsized status effect.
- Proof-first protocol as client experience asset: 6-image proof-of-system (editorial + product split) is a hospitality differentiator. Package as visible SNIPED client experience protocol layer.
- Observational-pitch frame for Day-30 Op Kit: must contain (1) specific Reset observation, (2) specific gap closure, (3) Op Kit value map, (4) pricing tier, (5) friction-lowering Calendly link.
- Peak-end design: concentrate hospitality investment at shoot reveal and final gallery delivery.
- No-show/late reschedule policy: first reschedule free (14-day window). Second $150. Third deposit forfeited. No-show (60+ minutes): deposit protection, binary offer.

**Delivery contradictions and open gates:**

- Calendar-based content retired: replaced by stateless, date-independent reusable engines. Shoot date no longer determines content output timing.
- Proof deployment hierarchy: website first, then outreach, then content. Forces prioritization.
- BRIEF_TEMPLATE.md must cross-reference 3 locked doctrines: current template does not surface Lineage Doctrine, Casting Call Doctrine v1, or Composite Environment Rotation v1. Next update adds links.
- Reset SLA conflict: 5 vs. 7 vs. 10 day delivery windows coexist in different docs. CURRENT_STATE.md governs until manual audit resolves.

---

### CROSS-DOMAIN DECISIONS: ACTIVE CONFLICTS REQUIRING OPERATOR RESOLUTION

| Conflict | Domains | Status |
|---|---|---|
| Founder Kit ($12,500) vs. Reset ($1,500) offer architecture | Money, Ops | CRITICAL. No doc explains transition. Crown or retire. |
| ICP bifurcation: law firms vs. Series A-C founders as 2026 primary | Choosing, Money | Requires explicit decision. Both in docs simultaneously. |
| Reset SLA 5 vs. 7 vs. 10 days | Delivery, Ops | CURRENT_STATE.md governs. Manual audit required. |
| Notion MCP vs. Airtable as primary CRM | Ops | P1 open. Impacts Wave-1 infrastructure. |
| Repetition-over-novelty vs. Synthesis-before-direction tiebreaker | All | Protocol missing. Codify in EXECUTION_GOVERNOR. |
| BASEPLATE public wrapper test: permanent or trial | Choosing, Optionality | 30-day test (May 26 to June 26 2026). No permanence gate yet defined. |
| CF-002: architecture locked (May 12) vs. hypothesis-generation mode (June 2) | Choosing | Productive tension. Needs one-sentence protocol rule. |

---

## DOCTRINE

### Section 1: Promoted Doctrine (Newly Elevated or Multi-Source Confirmed)

**Read Whole, Then Distill**
Source: Batch-002, feedback_read_whole_then_distill.md
Single most important OS rule. Every doc/book read in whole, segmented if huge, distilled to usable doctrine. Chunks only matter if retrieved and used.

**Full-OS Synthesis Every Answer**
Source: Batch-002, feedback_full_os_synthesis_every_answer.md
Big SNIPED asks require fresh synthesis crunching the entire OS. Existing docs are raw material to beat. Nothing previously made is "the answer."

**Connected Toolchain Default (Manual-First Assumption Killed)**
Source: Batch-002, feedback_connected_toolchain_default.md
Tool-first routing always. Manual is fallback after 11-step toolchain audit returns no path. TOOLCHAIN_ACTIVATION.md is single source of truth. This supersedes all prior "do this manually" instructions.

**Payment Follows Proof**
Source: Batch-002, feedback_payment_follows_proof.md, BW2s11, shelf5, Lean Startup frame
EIN/LLC/bank imperfection = admin cleanup, not money friction. Waterfall to fastest legit link now. Confirmed independently by Weiss, Dalio, Fitzpatrick, Engels, Lean Startup "achieved failure" concept.

**Repetition Over Novelty**
Source: LOCKED 2026-05-12, confirmed across shelf3/4/5/7/8, Ericsson, Kahneman, Wheeler, all five shelf-7 books, Ries/Trout, Mollick, Thompson, Dalio 5-step OS
90-day ban on new strategic frameworks through 2026-08-12. Architecture is built. Cathedral exists; run the office. Confirmed as scientific law across the most independent sources of any single doctrine. Qualifier: applies to architectural layer (identity, visual direction, editorial lane), NOT to tactical layer (outreach, distribution, pricing, cadence) which evaluates quarterly.

**Scene-Density Over Audience-Growth Thinking**
Source: LOCKED 2026-05-12, confirmed across shelf4/5/7/8, Anderson, Thompson, Spinks, Senge, Dixon, Chen Allee Threshold, Elberse, McLuhan, Stoute, Drake, Coyle Allen Curve
Every shoot/post/relationship asks "does this thicken the scene?" Depth compounds; breadth dissipates. Scene-density IS circumstance specification. Scene-density thinking is system-solution, not optimization.

**Proof Over Packaging / Proof-First Governance**
Source: LOCKED 2026-05-26, confirmed across Hormozi, Munger, Kupor, Weatherford, Kelly, Moore, Graham, Rubin, Feld, all five BW2s12 books
Ingestion phase complete; move from absorbing input to shipping output. Ask for smallest real test before asking what to build. Lean Startup "achieved failure" (perfect execution of flawed plan) is the exact failure mode this rule guards against. Confirmed authority is ledger-recorded, not claimed.

**Strongest Photograph Is Not Most Processed (Reject Gate Mandatory)**
Source: LOCKED 2026-05-28, Batch-002/005/009/011, confirmed via cognitive science
Every automated output must beat source visually, not just complete task. Failed cleanup artifacts are worse than honest studio context. Visual clarity and restraint produce cognitive ease; brain links ease to quality. Overprocessed images create cognitive strain. This is not subjective. 7 lessons from Untitled-1.CR3 arc formalized as permanent gate.

**Lineage as Non-Negotiable Moat**
Source: Confirmed across Dilla, Greene, Elberse, Berger-Dyer, Morrison/Hurston/Walker, Herodotus, YSL/Dior/Jobs, Gucci, Stoute
Lineage depth is the moat, not aesthetic preference. Authority comes from inside, not declaration. Lineage moat beats aesthetic moat: aesthetic restrained = direction, not lock; lineage embedded = sufficient moat. Nomos (lived cultural practice/lineage participation) cannot be replicated by AI. AI simulates physis (environment/world); cannot replicate nomos. Four confirmations: Herodotus, Berger-Dyer, SNIPED hybrid-operator stance, Chen community depth.

**Operator Language Over Photographer Language**
Source: shelf5/baseplate_alignment, LOCKED
Assets not photos, deploy not shoot, infrastructure not session. Vocabulary determines perceived value. Apply uniformly across all copy, contracts, Pixieset, Baseplate.

**Hybrid Human + AI as Stable Architecture (Not Transitional)**
Source: Prediction Machines, Free structural, Lean Startup, BF1-3, multiple
AI for world-construction/IG creative engine; anti-identity-AI on client deliverables. Imperfection Principle: deliberately add scanner echo/film grain/light artifacts to prevent plastic look. Confirmed permanent architecture. Centaur model (human holds identity/direction/approval; AI handles background/environment/styling) beats cyborg intertwining.

**Restraint as Structural Power**
Source: PROMOTED, confirmed across Talley, Rumelt, Berger, Evoto, Dior/Thomas/Marx/Shotton/Iger, Meisel/Roversi, Herodotus Pausanias meal
Foundation stronger than aesthetic preference. Restraint = moat. Restraint signals authority; volume signals desperation. Material austerity communicates civilizational superiority without argumentation. Confirmed across four independent sources spanning fashion, strategy, photography, and retouching.

**Human Authorship as Copyright Gate**
Source: PROMOTED, series_1/segs 1+12, Thaler v. Perlmutter, Bartz v. Anthropic June 2025
Real subject + AI environment + human direction = copyrightable. Pure AI = not. Hardens SNIPED's anti-identity-AI + pro-world-construction stance.

**Noeme as AI Defense**
Source: Camera Lucida, Barthes, shelf21
Human subject is light-trace (ontologically continuous); AI background is construction. Different categories. Replace "AI can't do identity" with "We document actual human consciousness experiencing light. AI generates environments. Both real. Different jobs." Noeme argument is harder to counter than aesthetic/ethical frame.

**System Design Beats Individual Talent**
Source: Confirmed Gawande, Thorndike, Iger, Kupor, Weatherford, shelf8/Steiner+Peterffy
SNIPED_OS is the algorithm; photography is the execution. OS maintenance beats individual talent. Operator who maintains the system outlasts the artist who makes one great image.

**Referral Compounding as Only Exponential Lever**
Source: confirmed Company of One, Shelf 12, referral economics 5x cost gap
Referrals exceed churn = exponential. All other growth = linear. Structured 14-day post-delivery activation loop closes 83%-willing/29%-doing gap.

**Proof Loop as Leverage Architecture**
Source: Batch-014
Proof inventory, proof sorting, proof deployment, portfolio reframe, case-study structure form 5-step loop closing output-to-money cycle. Operationalizes empire leverage thesis.

**Sequencing Is the Primary Creative Act**
Source: shelf6 (Batch-S series), S06
Shooting is research; selection is art; sequencing is argument. Sequence manifest required before publication. Five-Level Image Evaluation: individual/pair/series/environment/full lineage thread. Level-a only = good photograph, not great SNIPED image.

**Execution Governor Default to Action, Not Report**
Source: LOCKED 2026-05-29, Batch-002/003, Dalio 5-step
Inside SNIPED_OS, default response shape is action not report. Read STANDING_ORDER + NEXT_ACTION at session start. Trust the spine. Qualifier: action is default for proof-phase execution tasks (shooting, outreach, content, production). Action is NOT default for structural decisions (equity, formal roles, capital, governance).

**Caller's Reading List / Doctrine Embodiment Over Documentation**
Source: Batch-012, Senge, Dixon, ClaudeGuide
Written doctrine is not lived doctrine. Operationalization (skills, commands, crew scaffolding, post-shoot reflection loops, commons escalation, forgiveness protocols) is running the office.

**OS Engagement Protocol (Read Whole Before Any Full OS Answer)**
Source: feedback_os_engagement_protocol.md, LOCKED 2026-06-03
Fully engage the OS: every source doc whole-read + distilled, proven coverage, tracked on a live dashboard. 2,361 sources (1,145 text + 1,216 books). Invokable as os-engagement.

**Full Engagement Before Direction**
Source: feedback_full_engagement_before_direction.md, LOCKED 2026-06-03
Today governs. Partial OS findings are evidence, not authority. No lane crowned from partial engagement. Full OS read before any final direction. Checkpoints REPORT (changed/promoted/weakened/contradictions/pending), never sell a lane.

**Old Work Informs, Current Proof Decides**
Source: feedback_old_work_informs_proof_decides.md, LOCKED 2026-06-03
OS preserves memory but proof earns authority. Old docs = evidence (court-weighted), not law. Six lanes stay OPEN until proof. BASEPLATE = live hypothesis, not locked throne.

**Possibility Engine / No Lane Crowned**
Source: feedback_possibility_engine_optionality.md, LOCKED 2026-06-03, confirmed across all 166 doctrine docs
Bryce is the OPERATOR/possibility engine, not any one output. OS must NOT collapse him into one identity. Identity emerges from PROOF not brainstorm. Do not determine the throne before the kingdom exists.

**Dissemblement as First-Order OS Rule**
Source: Marcus Aurelius, Bf1-shelf11
Every artifact tested for sincerity before shipping. Soul wrongs itself when it dissembles. Hard gate: honest version required.

**Process Authority Is the Moat**
Source: Confirmed across 6 books/B016-BW2s1
Production OS + Session Protocol + Composite Environment Rotation + 90-day rep lock are authority sources, not biography.

**Magic Cycle Operational Frame**
Source: Bf2-shelf04 Godin
Cycle 1 = Remarkable (current: composite/casting/environment), Cycle 2 = Milk (Brand System, operator licensing), Cycle 3 = Reinvest (Book, KOTS, Cultural Doc). Track position quarterly.

**Rarity Economics as Scarcity Defense**
Source: shelf8/Steiner+Emmy
Volume destroys prestige; AI composite engine produces unlimited environments; Bryce's editorial curation (one per chapter) restores scarcity. Automate execution; keep selection human.

**Ruling-Part Daily Audit**
Source: Marcus Aurelius, Bf1-shelf11
Explicit 5-question internal check before day's first major decision. Not just session-start doc read. Ruling part = reason protected from external validation, scale lust, short-term comfort.

**Mortality Clarity Filter**
Source: O'Connor model, Bf1-shelf19
O'Connor test on every decision. Would I make this decision with one year left?

**Designed Incubation Rule**
Source: Csikszentmihalyi, Bf1-shelf12
Unstructured time is not rest. Schedule explicitly. Semi-automatic physical activity (location scouts, long drives, walks) is highest-yield incubation environment. Do not fill with admin.

**Belonging Architecture Not Copy**
Source: shelf10/Airbnb
Every operational layer reflects belief, not just copy. Casting + lineage + edit register = operational belonging.

**Broadcast Infrastructure as Named Requirement**
Source: Thompson 95% broadcast rule, shelf8
Dark broadcaster (comment doctrine/VIB/Instantly/trigger monitoring) must be live before organic discovery matters. Debunks viral cascade myth.

**Calibration Discipline as Standing Order**
Source: Batch-012 (docxwave-shelf3)
All SNIPED forecasts (revenue targets, conversion rates, pipeline velocity, set calendar economics) ship with confidence level + post-mortem review cycle.

**Output-First Content Rule**
Source: A3_shelf5
Every asset has defined output goal before creation. No asset ships without stated purpose. "Post for presence" fails.

---

### Section 2: Assumptions Weakened

**"Anti-AI" as Categorical Positioning**
Prior: binary "anti-AI" was the positioned stance.
Weakened by: Hybrid-operator stance is more precise. AI for world-construction/IG creative engine; human for identity. Not "anti-AI." Multiple sources (BF1-3, shelf16, NEWFILES, multiple). Replacement language: "We photograph for people who look." Sculpted AI (bounded, containment-doctrine) replaces binary anti-AI.

**"Evoto Is a Simple Skin Tool"**
Prior: Evoto framed as skin-only correction tool.
Weakened by: Batch-011 corrected scope to 8-capability deep-edit layer (color match, backdrop optimization, perspective/horizon, frequency separation, dodge-burn sculpt, AI culling, tethered shooting Phase B+, cloud sync). Evoto + Photoshop scope resolved. Docs needing update: lightroom_operating_system.md, PRODUCTION_OS.md.

**"More Tools = More Capability"**
Prior: tool accumulation implied capability.
Weakened by: Broken processes automated are broken at speed. Process first, tool second. A3_shelf1/Hammer.

**"Confident Intuition Is Reliable in High-Stakes Decisions"**
Prior: gut instinct treated as valid strategic input.
Weakened by: Correlates poorly with accuracy in low-feedback environments. Apply formula where feedback is delayed. A3_shelf3/Kahneman.

**"Authority Comes from Volume of Proof"**
Prior: more proof = more authority.
Weakened by: Community depth and social signal outweigh transaction count. McKee 17,000 sales vs. MCR 10,000 pre-existing fans. A3_shelf12/Anderson.

**"Photography Lane Is a Proven Permanent Moat"**
Prior: photography excellence as locked defense.
Weakened by: Long Tail shows direction mastery (not technical skill) is the moat. Six-lane openness remains correct. A3_shelf12/Anderson.

**"Build Internal-Tight Before Market" as Indefinite Permission**
Prior: internal preparation as open-ended delay authorization.
Weakened by: Multiple sources (Branson, Jarvis, Arnold, shelf12, Total Recall, A3_shelf10). The rule means: lock spine, confirm proof package visible + survivable, THEN market. Not wait for system completion. First offer should be minimum profitable version, not polished system. Define readiness threshold rather than leave open-ended.

**"More Output Increases Authority"**
Prior: content volume drove authority.
Weakened by: Teflon Don outperforms Hood Billionaire. Compression + filter over volume. shelf19.

**"Stated Founder Preference for Authentic Photography = Behavioral Hiring Signal"**
Prior: testimonials and preference data treated as behavioral signal.
Weakened by: Shotton survey/behavior gap; track bookings and referrals, not testimonials. A3_shelf4.

**"Anti-AI Moat Is Self-Evident"**
Prior: positioning required no testing.
Weakened by: Unintended expectancy associations can destroy positioning. Test before scaling. A3_shelf4.

**"Warm Response = Progress"**
Prior: positive sentiment from any contact = pipeline advancement.
Weakened by: Warm response from low-authority stakeholder is not progress. Route energy toward decision-maker. shelf17/Voss.

**"Cold Outreach as Primary Lead Engine" (Complete Reliance)**
Prior: Instantly/cold email treated as primary engine.
Weakened by: Retention/referral economics (5x cost gap, 83% word-of-mouth) require equally systematic retention counterpart. shelf12. Cold outreach is one of three layers: Instantly cold email (cold-to-warm) + LinkedIn comment doctrine (warm) + VIB DM (hot).

**"Lorne-Style Approval Withholding Generates Authority"**
Prior: scarcity of acknowledgment as power move.
Weakened by: Generates long-run resentment. SNIPED culture: generous, direct, attributive. Extract architectural discipline; refuse psychological manipulation. SNL oral history, Shelf 6.

**"VIB DM Warming Is Sufficient Outreach Infrastructure"**
Prior: LinkedIn comment + VIB DM covers full outreach infrastructure.
Weakened by: Covers warm-to-hot only. Cold email layer (Instantly, 5-part anatomy, 4-touch sequence) is the missing cold-to-warm layer. Both required. BF1-5.

**"Repetition Over Novelty" Applied Without Qualification**
Prior: blanket rule.
Weakened by: (a) High ideation volume INSIDE the locked constraint required - lock is direction, not thinking rate. (b) Repetition of fundamentals correct; repetition of prior identity frames without evolution is Louis XV trap. Do reps; do not become past. Confirmed across shelf03/shelf10/Bf1-shelf19.

**"Maximum-by-Default" as Maximum Features or Content Density**
Prior: maximum depth meant maximum output.
Weakened by: Maximum strategic depth, minimum executional noise. Featuritis (Neumeier) is the failure mode. Maximum depth within defined scope, not maximum scope. shelf8.

**"Possibility Engine Protection" as Permanent State**
Prior: optionality protection as unconditional permanent rule.
Weakened by: Correct as current-phase rule. Identity eventually stabilizes around discipline + ecosystem service + proof-first culture. Rule is phase-specific, not permanent. Total Recall.

---

### Section 3: Rules Superseded or Upgraded

**SUPERSEDED: "When Revenue Hits $3K" as Static Activation Trigger for Production OS**
Replaced by: Connected Toolchain Default (LOCKED 2026-05-28). PRODUCTION_OS sections 7.3-7.6 now subject to EIN-gate + Connected Toolchain routing, not static revenue-based instructions.

**SUPERSEDED: EIN Correction as Money Blocker**
Replaced by: EIN gate DOWNGRADED to P3 admin cleanup (LOCKED 2026-06-03). NOT a money blocker. Payment/deposits proceed sole-prop now. Cleanup happens after proof. Source: feedback_ein_correction_gate.md.

**SUPERSEDED: Phase-B Trigger at $3K MRR x 2 months**
Replaced by: Lowered to $2K MRR x 3mo per 100Q_AUDIT_OPTIMIZATIONS_2026-05-13.md. Canonical source overrides legacy memory. Multi-criteria gate (all four required): $3K/mo x 2 consecutive + 5 Resets + first Op Kit pitched + cash reserve >$3K. Batch-001/009/011.

**SUPERSEDED: "Do This Manually" as Default Instruction**
Replaced by: Manual is always last, never default. 11-step fallback audit required before "manual" claim. Source: Batches 002/003.

**SUPERSEDED: Evoto as "Skin-Only" Tool**
Replaced by: Evoto handles all 8 capabilities for Brand System tier; Photoshop = Track B compositing only. Source: Batch-011 resolution.

**SUPERSEDED: "No-Global-Grain Rule" (v1)**
Replaced by: v3 LUXURY locked preset (amount 12, size 25) is authoritative. Overrides v1 no-global-grain rule. Source: Batch-011.

**SUPERSEDED: Direct-Prompt Firefly as Default**
Replaced by: Firefly via Photoshop Generative Fill (with reference image) = Path A default for in-Photoshop compositing; Higgsfield/Seedream/Nano Banana Pro = Path B for external plate generation; direct-prompt Firefly deprecated. Source: Batch-011-ext C-04.

**SUPERSEDED: Adobe Portrait as Shoot Profile Baseline**
Replaced by: Adobe Neutral as single import baseline (C-03 resolved). LOS locked-look = Adobe Neutral preset import. Lane A vs Lane B divergence happens downstream (tone curve, HSL), not at profile selection. Source: Batch-011-ext.

**SUPERSEDED: Path B as Quality Ceiling for Composite**
Replaced by: Path A (PS Generative Fill + Reference Image) now quality-viable. Control preference, not quality gap, drives path selection. Source: Batches 011/012.

**SUPERSEDED: "Photoshop for All Retouching"**
Replaced by: Evoto handles 8-capability deep-edit layer. Photoshop moved to Track B environmental compositing only. Source: Batch-011.

**SUPERSEDED: "3 VIBs per Week" as Fixed Outreach Cadence**
Upgraded to: VIB queuing lockdown at 3 VIBs queued by Mon EOD, sent Tue/Wed/Thu. Source: Batch-008.

**SUPERSEDED: "VIB DM Is Default Outreach for All Targets"**
Replaced by: VIB re-scoped from default to conditional. Prospect warrant check required before VIB asset build; ship cold email if no warrant. Source: Batch-014.

**SUPERSEDED: "Posting for Presence" as Content Justification**
Replaced by: Every asset has defined output goal before creation. "Post for presence" fails output-first gate. Source: A3_shelf5.

**SUPERSEDED: "Calendar-Based Content"**
Replaced by: Stateless, date-independent reusable engines. Shoot date no longer determines content output timing. Source: Batch-014.

**SUPERSEDED: Five-Class Constraint Taxonomy as Blanket Ban Framing**
Replaced by: Only 10 Class A hard constraints are refusable. B (style), C (tactical-defer), D (not-in-rotation), E (stale-lock) route differently. Source: Batch-001.

**SUPERSEDED: "Proof Decides the Throne" as Sufficient Identity Frame**
Upgraded by: Hybrid identity = moat, not liability. Engineer + photographer + founder + LA cultural operator + Southern lineage background is the design surface, not a problem. Source: shelf9/SHELF SYNTHESIS point 4.

**SUPERSEDED: "LinkedIn 1x/week POV"**
Replaced by: LinkedIn POV minimum 3/week. Broadcast compounding + exposure mechanics require this. Source: Batch-010.

**SUPERSEDED: intel_positioning_phrases as Primary Positioning Language Reference**
Replaced by: Operator Voice (Bryceden Voice Style Guide) supersedes at operational specificity level. 6 voice DNA attributes, vocabulary lock, three signature moves, three traps. Source: docxwave-shelf4.

---

### Section 4: New Doctrine (First-Time Formalized)

**Trace Doctrine for AI Defense**
Human subject is light-trace (ontologically continuous); AI background is construction. Different categories. Identity in trace, environment in construction. Source: shelf6 Batch-S series.

**Rememory as Composite Environment Architecture**
Composite Environment Rotation is memory architecture, not aesthetic system. Each environment chosen because it encodes specific cultural frequency from inside one of five lineages. Source: Bf1-shelf07 Morrison.

**Gesture Specificity as Anti-AI Moat**
AI generates symbols/icons. SNIPED captures particulars: specific gesture, micro-detail, relational counterpoint. Market language: "We photograph for people who look." Source: Bf2-shelf04 Maisel/Szarkowski.

**Counter-Epistemology**
Embodied knowledge outranks definitional authority. "I know because I lived" = legitimate and superior authority for lineage work. Philosophical grounding for anti-AI-on-identity + Direction Stack authority claim. Source: Bf1-shelf07 Kelly/Morrison.

**Opportunity Cascade as Primary Production ROI Metric**
Fewer than 2 downstream opportunities = redesign before committing resources. Production decisions evaluated on cascade node value, not deliverable count or aesthetic quality in isolation. Source: Bf1-shelf07 Kelly.

**Narrative Refusal as Positioning**
SNIPED does not convert subjects into consumable narrative. Documents from inside subject's interior logic + lineage. Add to THE_LINEAGE_DOCTRINE.md. Source: Bf1-shelf07 Morrison.

**The Offering Frame**
Every SNIPED output is gift to life force, not product. Reframes pricing (ritual artifact), distribution (lineage placement), production (honor offering). Source: Bf1-shelf17 Becker. Add to THE_SPINE.md.

**Transference Architecture**
Personality-level (fragile) vs. lineage-level (durable). Every positioning asks which level. Add to trust_mechanics.md. Source: Bf1-shelf17 Becker.

**Founders Dilemma Doctrine**
Rich vs. King gate (name motivation lane), Three Rs equilibrium, Playing-with-Fire mechanics. SNIPED current provisional lane = King until proof demonstrates otherwise. Create intel_founders_dilemmas_doctrine.md at /00_BRIEF/. Source: Bf1-shelf18 Wasserman.

**Self-Criticism Loop as OS Default**
Any LLM-generated copy asset embeds minimum one self-criticism pattern (S2A/RaR/RE2) in originating prompt. Part of generation sequence, not review step. Source: Bf1-shelf19.

**Newspeak Compression Test**
Before any positioning language exits OS, run compression test. "Could this describe a competitor without modification?" Yes = flag for specificity re-injection. Generic = failed. Source: Bf1-shelf19.

**Three-Track Dialogue Rule**
Captions/DMs/case studies/chapters carry: Track 1 (plot/action), Track 2 (moral/values claim), Track 3 (repeating key word, placed last). Source: shelf4 Batch-S series.

**Bliss Point Encoding Rule**
3-4 visual hook moments per artifact required, neurologically grounded. Source: Bf2-shelf03 Seabrook.

**Prestige-Symbol Collapse Rule**
When upstream signals move downstream, prestige collapses. Every positioning/visual/artifact must hold scarcity until proof scales it. Source: BW1s2.

**Mechanic-Over-Instinct Doctrine**
Human behavior operates on discoverable physics (status/persuasion/narrative/attention). Operator with visible leverage points beats instinct-player. Source: BW1s2.

**Sneezer Enablement as Magic Cycle Step 2**
Post-delivery impression = story + tool to Tier 0 within 48 hours. Not optional hospitality; structural requirement. Source: Bf2-shelf04 Godin.

**Two Creative Acts**
Capture + edit are both generative. Edit is second full creative opportunity, not fix. Source: Bf2-shelf04 Maisel.

**Environment as Gestural Character**
Each of 7 environments has gestural logic (confinement vs. freedom, brutalist density vs. void). Environment selection is gestural decision, not visual variety choice. Source: Bf2-shelf04 Maisel.

**Authentic Brand Alignment Gate**
Partner value system must authentically align with SNIPED audience. Source: BW1s4.

**Costly Signal Verification**
Composite restriction + edit register + casting discipline ARE the costly signal. Four previously separate doctrines (costly signals = AI-defense moat = analog premium = craft depth) now unified frame. Source: Batch-007.

**Five-Level Image Evaluation**
Individual/pair/series/environment/full lineage thread. Level-a only = good photograph, not great SNIPED image. Source: S06.

**Reading Sequence Doctrine**
Every artifact honors notice > identity > relevance > support > details. Features first = audience rejection (Neumeier: 3x sales lift). Source: shelf8/Neumeier.

**Value Network Separation**
Each lane (Track B/Direction Stack/KOTS/Connected OS) needs separate process logic + success metrics. Sustaining proof does not transfer to emerging market proof. Source: S09.

**Operator vs. Talent Distinction Named**
Moat is system not Bryce personally. Operator captures system margin. Source: S05.

**Comps Treadmill as Named Antipattern**
"Plan = do what worked at higher volume" requires values-based rationale. Success earns right to iterate from values, not right to repeat. Source: S10.

**Named Systems Outlast Founders**
Name/lock date/version on every recurring workflow/doctrine/format after 2+ uses. Anonymous systems degrade silently. Source: S10.

**Generatives as Pricing Layer**
In free-copy economy, price the uncopyable (Embodiment/Authenticity/Interpretation). Kelly eight generatives: Embodiment + Authenticity are required minimums. Source: S07.

**Scapegoat Risk as Named Anti-Pattern**
Audience growth via scapegoating is predatory and structurally unstable. Add to feedback_scene_density_thinking.md. Source: Bf1-shelf08 Morrison.

**Pauline Bifurcation Risk**
Commercial work as beauty/order site while Direction Stack becomes afterthought. Quarterly self-audit: "Equal editorial care this quarter?" Add to EXECUTION_GOVERNOR.md. Source: Bf1-shelf08 Morrison.

**Give-to-Ask Ratio as Trackable Gate**
Named, tracked: minimum 3:1 give-to-ask in any 30-day window before any monetization ask. Source: Bf1-shelf09 Newsletter Ninja.

**Silence Is Data, Not Failure**
Diagnostic rule for cold contacts/stalled relationships. Add Sohrab Test before any VIB follow-up. Source: Bf1-shelf08 Hosseini.

**Output vs. Activity Named Distinction**
Every week: separate what was done (activity) from what changed (output). If activity does not map to output, it is motion without leverage. Source: Bf1-shelf12 Grove.

**Limiting Step Scheduling Protocol**
Every multi-step project begins identifying one longest/most constrained step. Schedules not built this way are fictional. Source: Bf1-shelf12 Grove.

**Architecture Beats Individual Genius**
Every SNIPED output should be producible by successor. If Bryce must be present, not architecture. Source: Bf1-shelf13 Morgan.

**Coenus Stop-Signal Doctrine**
Symmetry to Execution Governor: default to action on KNOWN work within current thematic goal. Apply stop-signal before initiating NEW work outside current goal. Source: Bf1-shelf16 Alexander.

**Courtier Capture Risk**
Zero-pushback signal is flag, not compliment. Requires at least one explicit invitation to disagree per production cycle. Source: Bf1-shelf16 Alexander.

**Resilience Ceiling Is Real**
Even exceptional operators hit mutiny point. Limited-hours constraint is operational intelligence. Production calendar must include enforced breaks. Cannot be overridden by ambition. Source: Bf2-shelf01 Chernow Washington.

**Expectations Are Output Architecture**
Explicitly stated expectations produce measurably better performance. Before every shoot and client call: state capability beliefs explicitly. Source: Bf2-shelf01 Ariely/Alexie.

**Non-Negotiability as Market Signal**
Selectivity strongest when non-negotiation is visible + consistent. "I could, but I don't" is stronger than "I can't." Source: Bf2-shelf01 Chernow Washington.

**Power-Law Portfolio Discipline**
Top 20% drive 80%+ proof/revenue. Concentrate; cut bottom tier without sentiment. Quarterly review. Source: Bf2-shelf03 Power Law.

**Manufactured Serendipity as Operating Standard**
One unscripted connection per client interaction, engineered. Source: Bf2-shelf03 Sequoia/Guidara.

**One Commandment Rule (External Positioning)**
Internal OS holds N doctrines. External positioning collapses to one moral premise, historically grounded, provably better. Candidate: "Photography from inside lineage, not tourism." Source: Bf1-shelf19.

**Missionary vs. Mercenary Filter**
Purpose alignment predicts performance more reliably than portfolio volume or credentials. Source: Bf1-shelf19.

**Ebb-and-Flow Scheduling**
Inward sprint (proof building, production, OS work) alternates with outward sprint (outreach, content distribution, VIB warming). Not balanced; cyclical. Source: Bf1-shelf19.

**Commitment + Advancement Standard**
Every client, talent, partner conversation ends with concrete next step + value given up. No exceptions. Add to ACTIVE_THREADS.md standing filter. Source: shelf17/Voss.

**AI Visibility as Distinct Channel**
AI search (Perplexity/Claude/ChatGPT/Google Overviews) is citation-based, not ranking-based. Schema markup + structured data + stats + quotes drive citations. Track monthly as scene-density signal. Source: Batch-010.

**Archive as Institutional Moat**
One growing archive + improving website + proof that ships = moat. Applies KOTS (50-year), SNIPED (10-year arc), Baseplate (founder journey). Source: Batch-010.

**Claude Phase Stack as OS Infrastructure Backbone**
Opus 4.7 strategic / Sonnet 4.6 tactical velocity / Haiku 4.5 batch low-stakes. Cowork + Computer Use deferred Phase B+. Source: Batch-012.

**CLAUDE Skills as Doctrine-Packaging Layer**
SNIPED has extensive written doctrine but no Claude-accessible mechanism without manual paste; skill .md architecture = delivery mechanism for OS corpus. Source: series_5/seg18.

---

### Section 5: Contradictions Requiring Human Decision

**CF-001: Founder Kit ($12,500) vs. Reset ($1,500)**
Spine locks Reset at $1,500 floor; docxwave-shelf1, docxwave-shelf2, and docxwave-shelf4b introduce Founder Kit at 8.3x. Multiple docs also reference "LA Photography Operator Kit" at $4k-$8k. No document explains transition, overlap, or targeting hierarchy. Is Founder Kit the new flagship, a post-Reset upsell, or a parallel lane targeting a different ICP?
DECISION REQUIRED: Which is the primary 2026 offer, what is the transition path, and do docxwave-era pricing tiers supersede Phase 1 Plan pricing?

**CF-002: ICP Bifurcation (Law Firms vs. LA Founders)**
THE_MACHINE locks law firms as core ICP (attorney vertical with 1,652+ C7 leads). Channel Alignment Plan and multiple B016-BW2 docs propose Series A-C LA founders as primary. These are structurally different ICPs with different outreach stacks, copy registers, and proof requirements.
DECISION REQUIRED: Which is the primary revenue lever in 2026? Is the attorney vertical a parallel volume track (confirmed in docxwave-shelf4b as "niche rotation") or has it been superseded by the founder ICP?

**CF-003: BASEPLATE Positioning vs. "Visual Perception Engineering"**
Multiple docs test whether "Visual Perception Engineer" language elevates pricing ceiling 10x vs. current Baseplate positioning. No resolution on record. Baseplate public wrapper test is locked at 30 days (2026-05-26 to 2026-06-26).
DECISION REQUIRED: Has the 30-day test window passed? What was the signal? Does Baseplate positioning hold, or does VPE language replace it?

**CF-004: Repetition Over Novelty Exit Condition**
Doctrine correct for 90-day sprint but lacks companion clause for when repetition phase ends. Monthly moment-readiness review is partial solution but does not define exit criteria. The 90-day ban runs through 2026-08-12.
DECISION REQUIRED: What are the specific signal conditions that trigger the next architectural review? Who authorizes it?

**CF-005: KOTS as Active Cash Vertical vs. Holding Pattern**
Multiple docs classify KOTS as "live cash vertical pending dad convos." BW2s1 describes it as "talent factory (Boca Juniors model)." Other docs treat institutional reframe as prerequisite. School committee + principal engagement + Eric Jones authority structure remain unresolved.
DECISION REQUIRED: Has the primary dad conversation happened? Is KOTS advancing to active vertical or staying parked?

**CF-006: Reset SLA Contradiction**
5-day, 7-day, and 10-day delivery windows coexist across docs. CURRENT_STATE.md governs but has not been cited as resolved.
DECISION REQUIRED: What is the current operational SLA? Update CURRENT_STATE.md explicitly.

**CF-007: Retoucher Hire Trigger Conflict**
Volume-based trigger ($2K x 3mo) and calendar-month-based trigger (Mo 6-9) may diverge depending on when proof arrives. sniped-retoucher-onboarding (Batch-011) sets Phase B gate at 30+ Heroes/month x 2mo sustained.
DECISION REQUIRED: Which trigger governs? Confirm in CURRENT_STATE.md.

**CF-008: Strategic Free Frame Count Single Point of Failure**
4-8 frame specification exists in sniped-shoot-day-strategic-free but has not been replicated to sniped-production-os.
DECISION REQUIRED: Authorize replication to sniped-production-os or confirm current single-source design is intentional.

**CF-009: B&W Card Dual-Register in BASEPLATE STUDIO Context**
B&W Chapter Card rule (LOCKED 2026-05-13) is clear for SNIPED. Unclear whether it carries forward into BASEPLATE STUDIO industrial register for CH02+ production.
DECISION REQUIRED: Does B&W Card doctrine apply to all future chapter production regardless of brand label?

**CF-010: Direction Stack Version Conflict**
Direction_Stack_Final_R2, direction_stack_complete.txt, FINAL_PRINT, and UPDATED labels coexist. File creation date check needed to confirm which is canonical.
DECISION REQUIRED: Which file is the single canonical Direction Stack manuscript? Retire all others or mark explicitly as deprecated.

**CF-011: Synthesis vs. Repetition-Over-Novelty Tiebreaker Protocol Missing**
When full OS synthesis contradicts locked 90-day rep freeze, no protocol exists. Recommended resolution: synthesis completes at session start, then 90-day freeze applies unless external forcing function. Needs to be codified in EXECUTION_GOVERNOR.
DECISION REQUIRED: Authorize this resolution and add to EXECUTION_GOVERNOR.md.

**CF-012: KOTS Lane-Branding Boundary**
Methods borrowed quietly from KOTS into SNIPED. Unclear rule on named co-branding between SNIPED and KOTS for any public surface.
DECISION REQUIRED: One-sentence rule before any public co-branding surfaces.

**CF-013: Freelance Platform vs. Win Without Pitching**
Blair Enns proclamations and the OS spine favor selectivity over platform availability. Several docxwave docs reference Peerspace and agency platforms as valid sourcing channels. These create positioning tension.
DECISION REQUIRED: Operator decision only. Which sourcing methods are inside the lane?

**CF-014: Payment Structure Conflict**
50/50 single-session, 40-30-30 multi-deliverable, and 25-50% ranges coexist across Business_Operations and docxwave docs. No single canonical payment split per scope type.
DECISION REQUIRED: Formalize as context-dependent by scope type and document in one location.

**CF-015: Threads Distribution Activation**
Batch-014 marks Threads as hard NO (hobby-leaning, engagement-bait, no premium distribution). Docxwave-shelf4b identifies dual-algorithm stacking (Threads + Instagram) as material leverage opportunity with 85-97% cross-platform impressions.
DECISION REQUIRED: Is Threads in or out? If in, what is the activation condition?

**CF-016: Website Hero Copy Register**
Fear-based ("Stop Losing Clients") vs. identity-based ("Commercial Portrait System for LA Founders") unresolved creative choice for the Carrd/website primary headline.
DECISION REQUIRED: Which register governs the current live site?

**CF-017: Proof Order Staging for BASEPLATE vs. SNIPED**
5-step proof order (BJ > SNIPED cash > BASEPLATE credible > actual assets > OS package for others) is clear directionally. But multiple docxwave docs position BASEPLATE as a $2,500 14-day install product ready to deploy. This creates tension with "no external launch until steps 1-4 produce repeated proof."
DECISION REQUIRED: Has proof at step 2 (SNIPED cash) been established at sufficient level to authorize BASEPLATE market entry? What is the threshold?

**CF-018: KOTS Sponsorship Authority Structure**
Sponsorship tiers not final until Eric confirms authority structure + money paths set. Contact line updates if Principal/committee chair holds authority. This has been open since Batch-010.
DECISION REQUIRED: Has Eric confirmed? Who is the authority holder for KOTS sponsor conversations?

**CF-019: Superstar Theory vs. Scene-Density Strategy**
Elberse superstar economics (winner-take-most) and SNIPED scene-density strategy both confirmed in OS. No resolution on when scene-density strategy should transition to concentration-for-superstar positioning.
DECISION REQUIRED: Stress-test against LA Black founder market data when proof accumulates. Flag for 2026-Q4 checkpoint.

**CF-020: AI Disclosure Addendum for Composite Galleries**
Reset MSA, Op Kit MSA, and Collab Agreement are all silent on AI-generated backgrounds. A unified disclosure addendum is required before any composite-inclusive gallery ships commercially. No record of this addendum having been created.
DECISION REQUIRED: Has the disclosure addendum been drafted? If not, block composite-inclusive gallery delivery until it exists.

---


## Capability candidates from "new hot shit .docx" (PASS 1, partial_read_only , NOT verified)
- process-step-audit (self-optimization gate/skill): remove/combine/simplify steps; find the invisible problem (Fadell). HIGH value.
- self-documentation-channel (skill candidate): publishable build-in-public digital journal from the harness/journal.
- anticipation-marketing (production method): mystery/livestream-reveal drop cadence.
- Execution-Governor line: "do the committed steps; belief is optional" (Brad Rushing).
- possibility-engine reinforcement: "bigger than the game" anti-identity-collapse phrase.
Source: OS_DOCTRINE_NEWHOTSHIT_pass1.md. Promote to real skills/gates only after a fuller read.
