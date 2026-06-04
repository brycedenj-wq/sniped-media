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