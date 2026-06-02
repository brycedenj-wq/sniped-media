# IMPLEMENTATION_STACK_ACTIVATION · tooling docs as build references

**Date:** 2026-05-26
**Status:** Implementation reference. NOT a canon chunk. NOT a final identity lock. This activates the held implementation/tooling docs (per `HELD_OPERATOR_DOCS_INDEX.md` §9, unlock condition: "a build-specific need that the tool doc would directly serve"). The build need is now live: stand up the working system that runs the proof loops in `PROOF_LOOPS_30_60_90.md`.
**Frame:** the docs are implementation references, not identity canon. Building this system runs the proof-loop *test*; it does not finalize SNIPED, SNIPED Media, or BASEPLATE. SNIPED Media is the current photography company (per `CURRENT_OPERATOR_REALITY_BRIEF`), so it is the correct substrate to test on. Whether it earns is what the proof loops decide.
**Sources read (read-only · not chunked):** sniped_context_tools_only, Pixieset_Operations_Reference, The_Revenue_Stack, The_Offer_Stack, The_Outbound_Stack, Evoto_AI_Retouching_Reference, The_Higgsfield_Codex, The_Kling_AI_Codex, sniped figma, Digital_Products_AI_Services_Playbook, 06_DELIVERY/pixieset_config.md + SOP_post_delivery.md + email_templates/, 03_OUTREACH SOPs, 14_WEB/carrd_one_pager.md, the n8n automation JSON flows.

---

## 1. Tool inventory (what exists · what each is for)

| Tool | Doc(s) | What it is for |
|---|---|---|
| **Pixieset Pro** ($30/mo) | Pixieset_Operations_Reference, 06_DELIVERY/pixieset_config.md, SOP_post_delivery.md | The core client surface. Four modules: Client Gallery (deliver photos + the 48hr/14-day upsell), Store (sell prints/extra images via print labs), **Studio Manager (CRM, invoicing, contracts, questionnaires, booking/scheduling)**, Website. |
| **Carrd** ($19/yr) | 14_WEB/carrd_one_pager.md | The one-page conversion site at snipedmedia.com. 7 sections, no nav, single CTA routing to Calendly. The answer to "where can I see your work?" |
| **Calendly** | carrd_one_pager.md (CTA target), 03_OUTREACH/SOP_discovery_call.md | Discovery-call booking. The CTA on the Carrd and in outreach routes here. |
| **Google Workspace** | pixieset_config.md (bj@snipedmedia.com) | Professional email domain + the client email sequence (templates below). |
| **Email templates (9)** | 06_DELIVERY/email_templates/ 01-09 | Pre-shoot brief, Day-0 delivery, Day-7 testimonial, Day-19 window-closing, Day-30 Op Kit pitch, Day-90 reengagement, referral ask, booking confirmation, no-show followup. The client communication layer, already written. |
| **Instantly.ai** | sniped_context_tools_only, The_Outbound_Stack | Cold email at scale: 5 domains / 25 inboxes / 150 sends per day, Super Search lead scraping (LinkedIn-verified, city/title/industry/size), Unibox reply management. The outbound demand-gen engine. |
| **LinkedIn (+ Buffer)** | sniped_context_tools_only | Relationship-layer channel 2: 10 connects/day, 2-3 DMs, 3 posts/week scheduled via Buffer, 5-10 comments/day. |
| **Adobe (Lightroom/Photoshop)** | The_Adobe_Stack_Manual | Primary edit/grade pipeline (the v3 LUXURY preset work). |
| **Evoto** | Evoto_AI_Retouching_Reference | AI retouching accelerator for skin/cleanup, feeding the Adobe pipeline. |
| **Higgsfield** | The_Higgsfield_Codex, Higgsfield_AI_Operator_Playbook | AI video/motion content generation (IG creative engine). |
| **Kling** | The_Kling_AI_Codex | AI video generation (alternative/complement to Higgsfield). |
| **Figma** | sniped figma | Design surface for landing assets, brand/identity mockups, decks. |
| **n8n automations** | 10_REFERENCE/.../automations/*.json (8 flows) | Advanced AI-agent automations: AI Content Strategy Generator, ElevenLabs/RetellAI lead-qualifying phone agents, prompt-writing agents, form-submission agents. |

## 2. Active now vs later vs duplicate vs ignore

- **ACTIVE NOW (the proof-loop core):** Pixieset Pro (Studio Manager + Gallery + Store), Carrd, Calendly, Google Workspace + the 9 email templates, Adobe + Evoto (edit pipeline). This is everything needed to take a real client from inquiry to paid to delivered to upsold.
- **ACTIVE-BUT-PARALLEL (demand gen · not required for first reps):** Instantly.ai, LinkedIn + Buffer. These fill the top of the funnel at volume. For the very first reps, warm/network outreach is cheaper and faster; run Instantly in parallel as it warms, do not block proof on it.
- **LATER (after the core loop has reps):** n8n agent automations (RetellAI/ElevenLabs caller, content-strategy generator), Higgsfield/Kling content engine. These add leverage once there is a working loop to amplify; building them first would be automation-before-proof.
- **DUPLICATE / SUPERSEDED:** "PIXIESET NEW USE .docx" overlaps Pixieset_Operations_Reference (use the Reference). LeadSwift/VA scraping (Option 2 in context-tools) is retired in favor of Instantly Super Search. The v1 post-delivery 48hr sequence is superseded by delivery_architecture_v2 (14-day window) per SOP_post_delivery.md.
- **IGNORE FOR NOW (not implementation tools):** the SNIPED brand-strategy / identity-direction docs (held per the index), Figma beyond simple landing/asset needs.

## 3. First buildable workflow (smallest useful stack)

**Workflow: Inquiry to Paid to Delivered to Upsold.** The minimal end-to-end system that captures a real paid signal from a real client and delivers, with the upsell mechanic attached. It is the cheapest real test of the visual-work and founder-portrait hypotheses, and every required tool is already documented.

Flow: **see work (Carrd) -> book discovery (Calendly) -> qualify + send contract/deposit (Pixieset Studio Manager) -> shoot -> edit (Adobe + Evoto) -> deliver + upsell (Pixieset Gallery + Store) -> email sequence (Google Workspace templates) -> testimonial + referral.**

## 4. Exact app stack for that workflow

| Layer | Tool | Why this one (from the docs) |
|---|---|---|
| Conversion surface | **Carrd** ($19/yr · snipedmedia.com) | Already specced: 7-section one-pager, single CTA to Calendly. |
| Booking | **Calendly** | The documented CTA target for discovery calls. |
| CRM + contract + deposit/invoice | **Pixieset Studio Manager** (Pro) | One tool already covers lead capture, questionnaire, contract, invoice, and payment collection. Avoids adding Stripe/HoneyBook separately for v1. |
| Capture edit | **Adobe (Lightroom/Photoshop) + Evoto** | The existing v3 LUXURY pipeline + AI retouch accelerator. |
| Delivery + upsell | **Pixieset Client Gallery + Store** (Pro) | Password gallery, high-res download, 14-day upgrade window, extra-image upsell at the documented price. |
| Client comms | **Google Workspace + the 9 email templates** | bj@snipedmedia.com + pre-written booking/delivery/testimonial/referral emails. |

**One decision flag:** payments can run through Pixieset Studio Manager invoicing (recommended for v1 · one fewer tool) OR Stripe if BJ wants a standalone checkout. Default to Pixieset invoicing first; add Stripe only if a real friction shows up.

## 5. Step-by-step setup

1. **Google Workspace:** confirm bj@snipedmedia.com is live (it is the from-address for all client email and the Pixieset studio email).
2. **Pixieset Pro:** subscribe ($30/mo). Set branding (charcoal #1A1A1A, no gallery logo), studio name Sniped Media, USD, PT. Connect `gallery.snipedmedia.com` (CNAME).
3. **Pixieset gallery template:** build the `[TEMPLATE] Reset · DUPLICATE PER CLIENT` collection per pixieset_config.md (cover, title format, password-protected, 14-day expiry, watermark off, download on). 30 min once; 5 min per client thereafter.
4. **Pixieset Store:** enable the extra-image upsell at the documented price; connect a print lab if selling prints. This is the 14-day upgrade-window mechanic.
5. **Pixieset Studio Manager:** create the lead/inquiry pipeline, the contract template, the questionnaire (pre-shoot brief), and the invoice/deposit template. This is the CRM + payment layer.
6. **Calendly:** create the 10-minute discovery event; paste the link into the Carrd CTA and the outreach scripts.
7. **Carrd:** build the 7-section one-pager per carrd_one_pager.md; CTA routes to Calendly; publish to snipedmedia.com.
8. **Email templates:** load email_templates 01-09 into Google Workspace (drafts/canned responses) or Studio Manager; wire the Day-0 delivery and booking-confirmation ones first.
9. **Edit pipeline:** confirm Adobe v3 LUXURY presets + Evoto retouch step are ready (already in place).
10. **Demand gen (parallel):** confirm Instantly campaigns are warming and the LinkedIn/Buffer cadence is running; for first reps, send 5-10 warm/network asks directly.

Target: the core (steps 1-9) is a 1-2 day stand-up since the templates and configs already exist.

## 6. What each automation should do

- **Carrd:** convert a visitor to a booked discovery call in under 60 seconds (single CTA, no nav).
- **Calendly:** book the call, send confirmation + reminders, drop the event into the calendar.
- **Pixieset Studio Manager:** on a won lead, send contract + deposit invoice; on payment, mark booked; hold client/shoot data.
- **Pixieset Gallery + Store:** on delivery, serve the password gallery, open the 14-day upgrade window, take upsell purchases automatically.
- **Email sequence:** booking confirmation (pre-shoot), Day-0 delivery, Day-7 testimonial ask, Day-19 window-closing, Day-30 Op Kit pitch, referral ask. Trigger manually for v1; automate later.
- **(Later) n8n / RetellAI:** auto-qualify inbound leads by phone; auto-generate content from a form. Not for v1.

## 7. What data gets captured

Per client, in Pixieset Studio Manager (plus a simple row in a tracking sheet that mirrors the proof log):
- Lead source (warm/network, LinkedIn, Instantly, referral, Carrd inbound).
- Inquiry date, discovery booked (y/n), discovery held (y/n).
- Offer presented + price quoted.
- Deposit paid (y/n + amount), shoot date.
- Delivery date, upgrade-window purchases (count + revenue).
- Testimonial given (y/n), referral given (y/n).

This is exactly the signal the proof log needs (paid? referred? repeated? upsold?).

## 8. Client/user experience

1. Sees BJ's work via LinkedIn/IG/in-person, lands on the Carrd.
2. Reads one scroll (problem -> method -> the Reset offer -> selected work -> testimonial), clicks "Book a 10-min Discovery."
3. Books via Calendly, gets a confirmation + pre-shoot brief email.
4. Discovery call -> contract + deposit invoice from Studio Manager -> pays -> booked.
5. Shoot day.
6. Receives the Day-0 delivery email: password gallery, 20 retouched finals, high-res download, plus the extra-image upgrade window (14 days).
7. Optionally buys extra frames; gets the Day-7 testimonial ask and (Day-30) the Op Kit pitch; may refer.

Premium, low-friction, branded end-to-end. No tool feels bolted on.

## 9. Which proof-loop hypothesis this tests

- **Primary: H1 (paid visual work)** and **H2 (founder/operator portrait offer)** from `PROOF_LOOPS_30_60_90.md`. The system exists to produce real paid sessions with real founders/operators.
- **Also: H5 (premium taste/status pull)** via the upgrade-window upsell and premium positioning, and the on-ramp to **H6 (consulting/diagnostic)** via the Direction Stack diagnostic on the Carrd.
- It does NOT yet test H3 (AI workflow/OS) or H4 (school/event infrastructure); those need their own minimal builds later.

## 10. What to log in PROOF_LOOPS_30_60_90

- Open a **Proof entry** (§6 template) for each real booking and delivery: hypothesis (H1/H2), test run, who, cost/effort, observed signal (paid? upsold? referred?), honest read, KEEP/KILL/ITERATE, next action.
- Move **H1 and H2** from UNTESTED to TESTING once the first real inquiry enters the system; update toward KEEP/KILL/ITERATE as signals land.
- Check the **30-day boxes** for H1 ("N paid sessions at floor") and H2 ("N real offers made") as they happen.
- Note upsell revenue against **H5**.
- Run the **anti-hiding check** at the weekly review: setup is necessary, but a week of building tools with zero real inquiries is a flag, not progress.

## 11. What docs were useful

- **sniped_context_tools_only** · the single most useful: it names the actual live stack (Instantly, LinkedIn, Buffer) and the daily flow. Confirmed NOT worth chunking; very worth using.
- **Pixieset_Operations_Reference** · the operational backbone for CRM/booking/delivery/store/invoicing in one tool.
- **06_DELIVERY/pixieset_config.md + SOP_post_delivery.md + email_templates/** · turnkey: the gallery template, the post-delivery sequence, and 9 written emails.
- **14_WEB/carrd_one_pager.md** · the exact conversion-surface spec + the Calendly routing.
- **The_Revenue_Stack / The_Offer_Stack / The_Outbound_Stack** · pricing, offer ladder (Reset -> Op Kit -> Brand System), and the outbound engine context.
- **Evoto_AI_Retouching_Reference + The_Adobe_Stack_Manual** · the edit pipeline.

## 12. What docs were not useful yet

- **The_Higgsfield_Codex / The_Kling_AI_Codex / Higgsfield_AI_Operator_Playbook** · content/video engine, not needed for the inquiry-to-delivery proof loop. Useful later for the IG creative layer (demand gen amplification), not for first paid reps.
- **sniped figma** (73K words) · large; only relevant if a custom landing/brand asset is needed beyond the Carrd. Not required for v1.
- **n8n automation JSON flows** · advanced agent automations; valuable later, automation-before-proof now.
- **Digital_Products_AI_Services_Playbook / Business_Operations_Playbook / The_Operator_Playbook / GaryVee_Attention_Operating_System** · these stay held (identity-risk / business-model doctrine per the index); not implementation tools for this loop.

## 13. What is still missing

- **A single payments decision:** Pixieset invoicing (recommended v1) vs Stripe. Pick one; do not build both.
- **A tracking sheet** that mirrors the proof log (Airtable/Sheets/Notion are all viable; the docs do not mandate one). Recommend the simplest: a Google Sheet or Notion table with the §7 fields. Not yet specced anywhere.
- **No field-engineering / data-center / local-business tooling** for H3 (AI workflow/OS) and **no school/event infrastructure** spec for H4. Those hypotheses have no existing implementation doc; they would need a separate minimal build when their proof loops activate.
- **Demand-gen-to-CRM handoff:** Instantly/LinkedIn replies currently land in Unibox/LinkedIn, then are manually moved to Pixieset Studio Manager. Fine for v1; a future n8n flow could automate the handoff.

---

**Guardrails (unchanged):** these docs are implementation references, not identity canon. Standing up this system runs the proof-loop test on the current SNIPED Media photography direction; it does not finalize SNIPED, SNIPED Media, or BASEPLATE, and forces no agency/SaaS/creator/photography-only identity. The Bible stays held until a deliberate SPIRITUAL_FOUNDATION decision. No chunking, no master-file updates, no new domain, no raw mutation were performed to produce this reference.
