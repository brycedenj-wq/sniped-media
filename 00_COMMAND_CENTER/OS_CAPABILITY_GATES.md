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