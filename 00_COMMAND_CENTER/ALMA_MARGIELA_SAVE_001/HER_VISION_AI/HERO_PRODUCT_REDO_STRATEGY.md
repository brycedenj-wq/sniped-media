# HERO PRODUCT REDO STRATEGY · 2026-06-13 (operator-directed)
Do not generate until this is written (done). Then run the one-beat proof, gate, roll out or fall back.

## WHY THE FIRST MOTION PASS FAILED THE HEROES
Budget path (nano_banana start-image -> Seedance freehand, 5s) let the suit mutate over time: color drifted, print hallucinated, the keystone's inherited necklace propagated. The product was never LOCKED, only described. Fix = lock the product with the real pipeline + obey the visibility-vs-motion law.

## CORE LAW (operator): product-visibility vs motion is INVERSE
- Bikini fully visible -> NO large body motion (camera/env micro-motion only).
- Large body motion needed -> reduce bikini detail visibility (conceal / wider / crop).
- If the product changes, the clip fails. If it only works because of grade, it fails. No necklace-contaminated source. Do not re-describe the outfit in the motion prompt. Use real garment references as controls. Shorter clips before longer.

## COLOR LAW (corrected, PERMANENT) - judge against the REAL photos, not a hex
- The real garment is CORAL-ON-CREAM. Cream/ivory ground with a coral-red feather-fan stippled print. Measured from ref_cherry: print field ~#956059 to #A8827D (muted coral, hue ~12-20), cream ground ~#E6DAD3.
- CHERRY / DETAIL density = warmer, denser red (the rhinestone cherries + print line cores), hue ~6-12.
- DO NOT force the whole suit to deep red #B84A40 (that was the flat-print macro anchor, NOT the on-body read). DO NOT push skin red to fix the suit. DO NOT crush the cream to dark/burgundy (b12 fail). DO NOT desaturate to peach/rose-gold (b10 fail).
- GATE COLOR CRITERION (updated): pass = coral-on-cream field + warmer-red cherry that MATCHES the real photos. Fail = burgundy/wine (too dark), peach/rose-gold (too desaturated/gold), or pink (B>G). Plain coral-on-cream is now a PASS, not a fail. This corrects the prior over-strict deep-red gate that false-failed b09/b18 on color.

## FULL PIPELINE (use all of it - operator directive)
1. SOUL V2 identity lock: train a Soul on the cleaned, necklace-free synthetic lead (5-20 stills) so the deadpan woman is identical + necklace-free across every beat. Use with text2image_soul_v2 / soul_cinema_studio.
2. GARMENT LOCK: reference Elements (show_reference_elements create from the real product front/back/cherry) AND/OR Marketing Studio Pro Virtual Try-On (locks the real product items onto the avatar; proven to hold logo/product across clips). The bikini becomes a controlled real-product element, not a described guess.
3. CINEMA STUDIO 2.0 for real camera moves (named dolly/tilt/arc + Linear speed ramp) instead of freehand drift.
4. ADOBE MCP (Photoshop/Lightroom) for SURGICAL fixes on source frames: remove the turquoise pendant + cuffs, recolor only the print field to the real coral-on-cream if a frame drifted, WITHOUT regenerating (deterministic, no mutation).
5. REAL ANCHOR for the pure-product object beat: animate the REAL product (cut-out/flat-lay) with micro-motion; never AI-regenerate the product object (it mutates). Ref: [[higgsfield-vibe-motion-exact-product]].
6. Topaz only AFTER a clip passes the gate.

## RECOVERY ROUTES (operator's 4)
R1 REAL ANCHOR (real product frame, minimal motion) | R2 MICRO-MOTION (accurate AI frame-1, 2-3s, camera/env only, no body move) | R3 CONCEALMENT (hide/reduce product with towel/door/crop/shadow/back/hand/blur/wider) | R4 REPLACE-WITH-WORLD (atmosphere/action beat, bikini not product-critical).

## PER-BEAT CLASSIFICATION (6 failed heroes + 3 rerolls)

### b18 poster (seated freeze) -> ONE-BEAT PROOF TARGET
- Original role: THE money-shot poster (the still she can pull); front suit + dog + Mercedes + palms.
- Why failed: inherited necklace + push-in-only motion (color coral = NOW acceptable).
- Route: R2 MICRO-MOTION. (This is also the keystone fix: clean it once, re-Soul from it.)
- New start frame: Adobe-strip the pendant off the keystone (49271d5b) -> Soul-locked regen at full quality; suit = real garment via Element. Necklace-free.
- End frame: no (settle-then-hold).
- Duration: 3-4s. Motion allowed: slow settle, one deadpan look, dog settles, tie-ends sway, hair, shutter click at end. Forbidden: necklace, push-in-only, body twist that changes the suit.
- Product visibility: HIGH. QA pass: no necklace/pendant/cuffs; suit coral-on-cream + cherry on correct cup holds f/m/f; print = feather-fan (not floral/novelty); ends on a clean held poster frame; authored settle (not push-in).
- Verdict target: HERO.

### b12 palm-beauty (front beauty breath)
- Role: longest clean FRONT product hold. Why failed: backlit dusk crushed cream to burgundy; print unreadable; near-static.
- Route: R2 MICRO-MOTION. Start: Soul + garment Element keyframe in BRIGHT EVEN daylight (cream must stay cream). End: no. Duration 3-4s.
- Motion allowed: palm sway, dappled light shift, heat shimmer, micro camera drift. Forbidden: body move, backlight that darkens the suit.
- Visibility HIGH. QA: cream ground visibly cream (not dark), coral print reads, cherry right cup, no necklace. Verdict: HERO.

### b09 trunk reveal (back hero)
- Role: trunk back-reveal, the suit-back architecture moment. Why failed: missing center-back rhinestone cherry charm (color coral = now OK).
- Route: R2 MICRO-MOTION. Start: Soul + garment Element back keyframe WITH the center-back charm explicit. End: no. Duration 2-3s.
- Motion: slow camera tilt up the back, tie-tails sway. Forbidden: rummaging/body twist.
- Visibility HIGH. QA: center-back cherry charm present + holds; cheeky-back construction; coral-on-cream; no necklace. Verdict: HERO.

### b06 walk-off (back hero)
- Role: deadpan walk-away, back of suit. Why failed: print MUTATED to cherry-novelty on cool white during the walk (body motion).
- Route: R2 MICRO-MOTION (NOT walking). She stands, back to camera; camera does the move. Start: Soul + garment Element back keyframe. End: no. Duration 2-3s.
- Motion: slow camera push-back or tilt, tie-tails + hair sway. Forbidden: walking, leg/hip motion (that is what mutated the print).
- Visibility HIGH. QA: feather-fan coral-on-cream holds (no cherry-novelty), warm ivory ground (not cool white), no necklace. Verdict: HERO (if holds) else demote to a distant B-roll walk where print is not legible.

### b10 towel (comedy peak)
- Role: giant-towel struggle, the deadpan gag. Why failed: peach/rose-gold suit + gold necklace + print unconfirmable at width.
- Route: R3 CONCEALMENT. The oversized towel HIDES most of the suit during the action; frame so the TOWEL is the subject and the suit is largely occluded. Necklace-free Soul source. Duration 3-4s (action allowed because product is concealed).
- Motion allowed: towel cascade/billow, she holds the edge deadpan. Forbidden: necklace; suit as focal subject.
- Visibility LOW-MED (occluded). QA: no necklace; towel no-text; the suit glimpses read coral-on-cream not peach/gold. Verdict: HERO-comedy (product-incidental by design).

### b13 bikini-top (the product object)
- Role: bikini-top graphic, the PURE PRODUCT alone mid-air. Why failed: AI mutated it (floral print, coral, no dice, exited frame).
- Route: R1 REAL ANCHOR. Use the REAL product top (cut-out from ref_front / a real flat-lay) and animate with micro-motion (gentle rotation/sway against a sky plate) via Adobe/AE or Higgsfield i2v on the real cut-out. NEVER AI-regenerate the top.
- End frame: optional (sway arc). Duration 2-3s. Motion: gentle tumble/sway of the REAL top; ties flutter. Forbidden: AI re-rendering the garment; exiting frame.
- Visibility MAX (it is the product). QA: exact real print + cherry + dice (pixel-real); stays in frame; reads as the real suit. Verdict: HERO graphic.

### b07 handcuff (chaos insert)
- Role: handcuff palm glossy detail. Why failed: AI put a wrong burgundy sleeve on the wrist (suit irrelevant here).
- Route: R1 REAL ANCHOR / R3 CONCEALMENT. No suit body in frame: a real chrome handcuff + car key + the real dice-tie macro, micro-motion light gleam. Or AI palm with ONLY the dice-tie Element, no garment.
- Duration 1-2s. Visibility LOW (tie-tail only). QA: chrome handcuff + key present; dice-tie warm-red; NO sleeve/garment; glossy not dark. Verdict: B-ROLL insert (never a true product hero).

### b15 recline (front)
- Role: passenger recline luxury hold. Why failed: necklace (suit otherwise CORRECT).
- Route: R2 MICRO-MOTION + necklace-free source. Adobe-remove the necklace from the recline keyframe (or Soul regen necklace-free). Duration 2-3s.
- Motion: settle deeper, one tie sway, light. Forbidden: necklace, body move. Visibility MED-HIGH. QA: no necklace; suit coral-on-cream holds. Verdict: HERO.

### b17 gas station (front, wide)
- Role: gas-station forecourt mood beat. Why failed: too wide to resolve print/cherry + static (color was fine).
- Route: R4 REPLACE-WITH-WORLD. Keep it a WIDE atmosphere/world beat (suit is incidental at that distance); add one authored motion (hair gust, heat shimmer, a slow quarter-turn). Do NOT treat as a product-detail hero.
- Duration 2-3s. Visibility LOW (wide). QA: world reads (retro forecourt, numeric-only pumps, no text); suit color-family coral-on-cream; one real motion. Verdict: B-ROLL / world beat (not a product hero).

## ONE-BEAT PROOF
Target = b18 poster (highest stakes + highest risk: full front suit visible, requires the necklace fix, tests micro-motion + garment Element + coral-color-hold all at once, and fixes the keystone). 
Method: Adobe-strip pendant off keystone -> Soul + real-garment Element keyframe (necklace-free, coral-on-cream) -> Cinema Studio / Seedance micro-motion 3-4s (settle + dog + sway, no push-in) -> gate first/mid/final through alma-motion-product-gate with the CORRECTED color law.
- If PASS: roll R2 micro-motion + Soul + Element across b12, b09, b06, b15; execute R1/R3/R4 for b13, b10, b07, b17.
- If FAIL: switch b18 to R1 real-anchor (build the poster around a real product frame) or R3 concealment, and treat full-front-visible motion as not viable -> all front heroes go R1/R3.

## VALIDATED METHOD (2026-06-13, one-beat proof on b18 PASSED on product)
The product-lock recipe WORKS: a fresh adversarial judge confirmed the garment PRINT + COLOR held coral-on-cream through motion (the exact failure that killed all 6 heroes). Recipe:
1. NECKLACE-FREE SOURCE: nano_banana image-edit to strip the pendant/cuffs from the keyframe (proven: keystone cleaned -> KF18_KEYSTONE_CLEAN.png, job 2aef74e4).
2. GARMENT ELEMENT: alma-cherry-bikini = element 132fd9cb-f743-4a50-aee8-1a7f4a492906; embed <<<132fd9cb-f743-4a50-aee8-1a7f4a492906>>> in the motion prompt -> backend injects the real product so it cannot mutate.
3. CORRECTED COLOR LAW: coral-on-cream judged vs the real photos.
4. SEEDANCE micro-motion, start_image = clean keyframe, 4s (min), env-only motion, HARD NEGATIVES: no earrings/necklace/chain/pendant + bare neck and ears, no license plate / no readable text, minimal body movement (she does not stand/twist).
5. GATE first/mid/final (no self-crown).
Proof result: print+color HELD. Only trivial fixes needed (plate text + re-crept hoop earrings + a touch much motion) -> b18 reroll fired with those negatives (job 9b83daeb).

## ROLLOUT (apply the validated recipe)
- b12 palm-beauty: clean (necklace-strip if needed) keyframe in BRIGHT daylight + Element + micro-motion (palm sway). 
- b09 trunk back-reveal: clean back keyframe WITH center-back charm + Element + slow camera tilt, tie sway.
- b06 walk-off: she STANDS (back to camera), camera moves, tie/hair sway (NOT walking) + Element.
- b15 recline: necklace-strip the recline keyframe + Element + settle micro-motion.
- b13 bikini-top: REAL ANCHOR (remove_background the real top, animate the cut-out) - do not AI-generate.
- b10 towel: CONCEALMENT (towel hides suit) + necklace-free source.
- b17 gas / b07 handcuff: REPLACE-WITH-WORLD / B-roll (suit not product-critical).
Every rollout clip RE-GATES through alma-motion-product-gate before assembly.

## DO-NOT
Do not assemble. Do not Topaz before a clip passes. Do not grade a wrong suit into passing. Do not use a necklace-contaminated source. Do not re-describe the outfit in motion prompts. Do not force deep red. Judge color against ref_front / ref_cherry, not a hex.
