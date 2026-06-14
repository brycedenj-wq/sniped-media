# Routing Test Report (2026-06-08)

10 real tasks run through the live router (`os_activate.py`) + the hardened Stop gate. Fields per test: prompt, domain, active skills, standards, proof gates, omitted high-relevance skills and why, missing/ambiguous routing, Stop-gate enforcement.

Legend: Stop-gate "ENFORCES" = a false "done/final/client-ready" would be blocked unless PROOF_MANIFEST verifies (hard production domain). "soft" = not auto-blocked unless deliverable_promised.

---

### 1. Film rebuild
- **Prompt:** "rebuild the Synergy brand film and fix the animatic shots"
- **Domain:** film/video
- **Active skills:** cinema-worldbuilder, kling-production-sop, banana-pro-director, os-face-lock, os-world-bible, os-vision-reject-gate, watch, sniped-crs-builder
- **Standards:** REAL_FILM_PRODUCTION_OS, FULL_FILM_STACK_COMPILATION, AI_CINEMA + HIGGSFIELD doctrines, FINISHING, COMMERCIAL_CRAFT_V2, AUTOEDIT
- **Proof gates:** STORY_GATE, Push-In Law, face-lock motion-ready, world continuity, vision-reject, 12-axis >=30/36, /watch, Gemini hostile, 9/10 floor
- **Omitted (why):** sniped-direction-stack/lighting-vault/status-psychology/higgsfield-pipeline/seedream/ai-image-tool-pick/composite-master-qa/platform-mastering held as REFERENCE (relevant but not core to a rebuild; force-load by name). All non-film domains asleep (irrelevant).
- **Missing/ambiguous:** none. Clean.
- **Stop gate:** ENFORCES (hard). The Door manifest currently verifies FAIL -> cannot be called final.

### 2. Alma campaign shoot
- **Prompt:** "plan the Alma Love campaign photo shoot and hero composite"
- **Domain:** photo_composite (+ would touch brand_campaign)
- **Active skills:** sniped-direction-stack, sniped-hero-composite-ceiling, sniped-hero-composite-lite, composite-master-qa, os-face-lock, platform-mastering, sniped-ai-image-tool-pick, sniped-seedream-prompt, banana-pro-director, os-vision-reject-gate
- **Standards:** COMMERCIAL_CRAFT_V2, HIGGSFIELD doctrine
- **Proof gates:** vision-reject, composite-master-qa 6-axis + crops, platform-mastering skin-drift, subject-identity-untouched
- **Omitted (why):** shoot-day + pre/post + capture-to-delivery + pixieset + lighting-vault held REFERENCE (load when the shoot moves from planning to execution). brand_campaign skills not auto-loaded (this read as photo-first; name "campaign rollout" to add brand).
- **Missing/ambiguous:** mild. "Campaign" + "shoot" splits photo vs brand; router chose photo (correct for a shoot). If the intent is the rollout, force brand_campaign.
- **Stop gate:** ENFORCES (hard photo).

### 3. Photoshop skin retouch
- **Prompt:** "retouch the skin on this portrait in lightroom and photoshop"
- **Domain:** editing/retouching
- **Active skills:** sniped-luxury-edit, sniped-evoto-skin-pass, sniped-capture-to-delivery, os-vision-reject-gate, composite-master-qa, platform-mastering
- **Standards:** COMMERCIAL_CRAFT_V2
- **Proof gates:** vision-reject, skin-drift, subject-identity-untouched
- **Omitted (why):** udemy-lightroom-rails (technique lookup), hero-composite-ceiling/lite, retoucher-onboarding held REFERENCE. Correct: a retouch is not a composite build or a hire.
- **Missing/ambiguous:** none.
- **Stop gate:** ENFORCES (hard).

### 4. Client text reply
- **Prompt:** "draft a caption and a short reply to a client about the post"
- **Domain:** writing/copy
- **Active skills:** sniped-caption-writer, sniped-positioning-phrases, sniped-status-psychology, sniped-canonical-truths
- **Standards:** STORY_PSYCHOLOGY dashboard
- **Proof gates:** STORY_GATE, voice gate (no em-dash/AI-tell), positioning phrase bank
- **Omitted (why):** trust-mechanics/vib-outreach/operator-review REFERENCE. ops/pricing asleep.
- **Missing/ambiguous:** YES, mild. A pure "text reply to a client" with no "caption" could read as ops (client comms) or pricing (if about a deal). The word "caption" pulled it to writing. If the reply is about scheduling/price, name it.
- **Stop gate:** soft (writing). Not auto-blocked unless a deliverable is promised. Correct: casual copy should not be hard-gated.

### 5. Pricing / negotiation
- **Prompt:** "a prospect wants a discount, how should I price this proposal"
- **Domain:** negotiation/pricing
- **Active skills:** sniped-pricing-decision, sniped-wwp-positioning, sniped-trust-equation, sniped-discovery-to-close, sniped-vib-outreach, sniped-partnership-protocol
- **Standards:** (frames are the skills)
- **Proof gates:** no-crown, anti-hallucination(cite), floor-held
- **Omitted (why):** new-luxury/status-psychology/trust-mechanics/operator-review REFERENCE.
- **Missing/ambiguous:** vib-outreach fired (it matched "prospect"); slightly off for an existing-deal discount, but harmless as a reference. Minor.
- **Stop gate:** soft. Correct (advice, not a production deliverable).

### 6. Model casting
- **Prompt:** "help me cast a model and prep for the shoot"
- **Domain:** photo_composite
- **Active skills:** sniped-direction-stack (intake/talent), + photo stack
- **Proof gates:** photo gates (apply when production starts)
- **Omitted (why):** pre-shoot-prep/shoot-day held REFERENCE (load at execution).
- **Missing/ambiguous:** YES. No dedicated casting skill exists. sniped-direction-stack (the intake/talent calibration) is the nearest and fires, but casting (sourcing, look-matching, releases) is only partially covered. GAP logged in SKILL_REGISTRY (candidate future skill).
- **Stop gate:** ENFORCES if a deliverable (a cast/board) is claimed done.

### 7. Deck build
- **Prompt:** "build the Drop Engine pitch deck for the campaign"
- **Domain:** brand/campaign
- **Active skills:** os-world-bible, sniped-higgsfield-pipeline, sniped-canonical-truths, sniped-caption-writer, platform-mastering, os-vision-reject-gate
- **Proof gates:** vision-reject, brand_consistency, no_method_leak_if_selling_outcome, 9/10 floor
- **Omitted (why):** art-series/hit-mechanics/blockbuster/perennial/trust-mechanics/hospitality/brand-validation/status-psychology REFERENCE (load the frame the deck needs).
- **Missing/ambiguous:** mild. A pure slide-design task could want a design-domain; here "campaign/drop" pulled brand_campaign (correct, since the deck sells the campaign). The proof domain for a deck is "design" (audience, slide review, readability/mobile, no-method-leak, export).
- **Stop gate:** ENFORCES (hard). Per the earlier test, a deck depending on a non-ready hero stays BLOCKED/internal.

### 8. Website build
- **Prompt:** "build the landing page website and deploy it on vercel"
- **Domain:** web/build
- **Active skills:** none native (intentional)
- **Reference:** update-config, vercel:* , figma:* (external plugins)
- **Proof gates:** completion-verification, responsive_check, legal-risk
- **Omitted (why):** no native SNIPED web skill exists by design; served by plugins.
- **Missing/ambiguous:** expected gap (no native skill). Routes to plugins correctly.
- **Stop gate:** ENFORCES (hard) once a deploy is claimed (needs build + responsive + deploy path in the manifest).

### 9. Research brief
- **Prompt:** "research the senior homecare market in Wilmington for 2026"
- **Domain:** research
- **Active skills:** os-token-safe-reader, os-command-router (+ deep-research plugin = the engine)
- **Proof gates:** source-freshness, anti-hallucination (cite + date)
- **Omitted (why):** udemy-ai-accelerants/operator-review/watch REFERENCE.
- **Missing/ambiguous:** the real engine (deep-research) is an external plugin, not one of the 76; the native skills are thin. Acceptable, flagged.
- **Stop gate:** soft unless a research deliverable is promised; then research proof (deliverable + sources cited/dated) applies.

### 10. Emergency drop protocol
- **Prompt:** "emergency we need to drop a campaign piece today"
- **Domain:** brand/campaign (nearest)
- **Active skills:** os-world-bible, sniped-higgsfield-pipeline, sniped-canonical-truths, sniped-caption-writer, platform-mastering, os-vision-reject-gate
- **Proof gates:** vision-reject, brand_consistency, no_method_leak, 9/10 floor
- **Omitted (why):** brand reference frames held back.
- **Missing/ambiguous:** YES, real gap. No dedicated "emergency drop / time-boxed protocol" skill. It routes to brand_campaign, which is right for the asset but does not encode the speed/triage tradeoffs (what gate to relax under time pressure, explicit-accept-the-gap path). GAP logged (candidate future skill: emergency-drop playbook with a documented, accepted gate-relaxation).
- **Stop gate:** ENFORCES (hard). Under emergency, the right move is an explicit named+accepted gap in the manifest (send=yes with documented relaxed gates), not a silent false "done."

---

## Findings
- **8 of 10 routed cleanly.** 2 had real coverage gaps (model casting, emergency drop) and 1 expected external-only routing (web build).
- **No over-bloat:** active skill sets stayed 4-10 per task; reference + all other domains stayed asleep with the why-omitted line.
- **Stop-gate coverage:** all 5 hard production tests (1,2,3,6partial,7,8,10) would block false completion; soft tasks (4,5,9) correctly not hard-gated.
- **Ambiguity pattern:** "campaign+shoot" (photo vs brand) and "client reply" (writing vs ops vs pricing) are the fuzzy edges; the router picks the dominant keyword and shows secondary domains, and the operator can force-load by naming.

## Recommended next builds (gaps, not blockers)
1. `emergency-drop` skill: time-boxed protocol with an explicit, recorded gate-relaxation path (never a silent skip).
2. `casting` skill: sourcing + look-match-to-reference + model release, feeding os-face-lock.
3. Optional: a native `web-build` skill wrapping the vercel/figma plugins to SNIPED standards.

---

# Addendum: 5 new tests (78-skill state, after building emergency-drop-protocol + model-casting-protocol)

Run after the two new skills were registered. Confirms emergency promotion + casting routing.

### 1. Emergency $60 editor handoff
- **Prompt:** "emergency $60 editor handoff, need this video edit today"
- **Domain:** film/video + **[EMERGENCY MODE]** promoted
- **Active skills:** cinema-worldbuilder, kling-production-sop, banana-pro-director, os-face-lock, os-world-bible, os-vision-reject-gate, watch, sniped-crs-builder (+ emergency-drop-protocol promoted)
- **Omitted + why:** reference set (direction-stack, lighting-vault, higgsfield-pipeline, seedream, ai-image-tool-pick, composite-master-qa, platform-mastering, model-casting) held; not core to a fast editor handoff. All non-film domains asleep.
- **Proof gates:** film gates apply; emergency RECORDS which are relaxed (coverage, full 12-axis, Gemini hostile -> fast self vision-reject); never-relax = identity/legal/vision-reject/brand-core/honest-label.
- **Send/no-send:** Stop gate ENFORCES. Output labeled "sendable (emergency, named gaps)", never "final". $60 budget = scope cut, not quality cut on the one thing.

### 2. Same-day shoot model casting
- **Prompt:** "cast a model for a same-day shoot today"
- **Domain:** photo/composite + **[EMERGENCY MODE]** promoted
- **Active skills:** model-casting-protocol, sniped-direction-stack, composite-master-qa, os-face-lock, platform-mastering, sniped-ai-image-tool-pick, sniped-seedream-prompt, banana-pro-director, os-vision-reject-gate (+ emergency-drop promoted)
- **Omitted + why:** shoot-day SOPs (pre-shoot, reset, post-shoot, capture-to-delivery, pixieset) held reference, load at execution not casting.
- **Proof gates:** vision-reject, composite QA, subject-identity-untouched; casting release = never-relax.
- **Send/no-send:** "cast locked" only when availability + comfort + usage + pay + release confirmed in writing; same-day pressure cuts shortlist size, not the confirmation gate. Backup #2 held warm.

### 3. Alma swimwear model issue
- **Prompt:** "the Alma swimwear model is being difficult about usage and edits"
- **Domain:** photo/composite (no emergency, correct)
- **Active skills:** model-casting-protocol, sniped-direction-stack, os-face-lock, + photo stack
- **Omitted + why:** shoot-day refs asleep (this is a dispute, not a shoot). Emergency correctly NOT triggered.
- **Proof gates:** subject-identity-untouched; brand-final-wins; release/usage terms.
- **Send/no-send:** model-casting-protocol Law 7 governs: if the model's edit/usage demands conflict with brand integrity, brand final wins. If unresolved, NO-SEND on the disputed asset; renegotiate usage or replace per backup plan. (Routing was fixed this pass: model-dispute phrasing now triggers the casting skill.)

### 4. Rush client proof delivery
- **Prompt:** "rush, deliver a client proof right now"
- **Domain:** QA/proofing + **[EMERGENCY MODE]** promoted
- **Active skills:** os-quality-gates, os-vision-reject-gate, composite-master-qa, watch, challenge (+ emergency-drop promoted)
- **Omitted + why:** platform-mastering, os-command-router held reference.
- **Proof gates:** 11 OS gates, vision-reject, completion-verification; vision-reject never relaxed even in a rush.
- **Send/no-send:** the artifact is labeled "proof" by definition (not final). Emergency relaxes polish gates (recorded); a vision-reject hard fail still blocks send. Honest label is mandatory.

### 5. Normal campaign (non-emergency control)
- **Prompt:** "plan a brand campaign rollout for next quarter"
- **Domain:** brand/campaign (NO emergency, correct)
- **Active skills:** os-world-bible, sniped-higgsfield-pipeline, sniped-canonical-truths, sniped-caption-writer, platform-mastering, os-vision-reject-gate
- **Omitted + why:** brand frames (art-series, hit-mechanics, blockbuster, perennial, trust-mechanics, hospitality, brand-validation, status-psychology) held reference; load the one the rollout needs. emergency-drop stayed asleep (control passed).
- **Proof gates:** brand_consistency, no_method_leak_if_selling_outcome, 9/10 floor.
- **Send/no-send:** standard hard gate; Stop gate blocks false "done"; no time-pressure relaxation.

**Result:** 5/5 behave correctly. Emergency fires on 1/2/4, stays off on 3/5. Casting routes on 2/3. Regression check: "data model" does NOT route to photo. 78/78 coverage, 0 dead.
