# PRODUCT FIDELITY THROUGH MOTION · HARD LAW (operator-locked 2026-06-13)

THE LAW: The product cannot drift during motion. The world can move. The model can perform. The camera can move. THE BIKINI CANNOT MUTATE. Garment accuracy is NOT a later grade-only issue.

## Product hierarchy (truth order)
1. Real studio product macros + real product frames = ABSOLUTE TRUTH (/tmp/alma_refs/ref_*.jpg + EVOTO _94A2812 cherry / _94A2810 dice / _94A2655 front / _94A2806 back; atlas SWIMSUIT_PRODUCT_ATLAS.md).
2. Keystone product-locked still (KF18, job 49271d5b) = identity/world anchor.
3. Generated keyframes = accepted only if they match product truth.
4. Generated motion = accepted only if FIRST + MID + FINAL frames all match.

## Higgsfield features to use for fidelity (every motion beat)
- image-to-video only (never text-only video); first-frame lock = the gated keyframe.
- end-frame lock when long/complex motion risks drift.
- reference chaining + garment reference controls where available; seed/identity continuity where available.
- action + camera-only prompts; DO NOT re-describe the outfit in the motion prompt.
- negative prompts against: print changes, strap/tie changes, color shift, jewelry import, extra cherries, text/signage.
- shorter duration if long motion causes garment drift.
- re-roll ONLY failed beats. Topaz ONLY after the motion gate passes.

## MOTION GATE (every product-visible clip, first/mid/final frames)
1 first-frame garment · 2 mid-frame garment · 3 final-frame garment · 4 strap/tie continuity · 5 cherry placement (RIGHT cup only, center-back charm, NO extra/bottom cherries) · 6 print consistency (coral feather-fan on cream, not floral/solid/novelty) · 7 color = CORAL-ON-CREAM matching the real photos (see CORRECTED COLOR LAW below); FAIL only if burgundy/wine (too dark), peach/rose-gold (too desaturated/gold), or pink (B>G) · 8 body/garment warping · 9 no extra jewelry imported (no necklace/pendant/bracelets) · 10 no text/signage tells · 11 no push-in-only fake motion.

## CORRECTED COLOR LAW (2026-06-13, operator-permanent) - judge against the REAL photos, NOT a hex
The real garment is CORAL-ON-CREAM, not deep red. Cream/ivory ground (~#E6DAD3) with a coral-red feather-fan stippled print (measured ~#956059 to #A8827D, hue ~12-20). Cherry + dense detail = warmer red (hue ~6-12). DO NOT force the whole suit to deep red #B84A40 (that was the flat-print macro anchor, not the on-body read). DO NOT push skin red. DO NOT crush cream to burgundy. DO NOT desaturate to peach/rose-gold. Plain coral-on-cream is a PASS. Truth = ref_front.jpg + ref_cherry.jpg.

## Verdict rules per clip
- FAIL = product visible and wrong. Do NOT grade it into passing, do NOT hide it with grain, do NOT use it as a hero/product beat.
- Failed clip options: re-roll with stronger locks; shorten the beat; crop product out; or CUT.
- Great motion + bad bikini = FAIL.
- Perfect bikini + weak motion = B-ROLL only, not hero.
- Coral-on-cream IS the correct read; it is a PASS. FAIL only on burgundy/wine (cream crushed dark), peach/rose-gold (desaturated/gold), or pink (B>G). These are not gradeable; coral-on-cream needs no grade.

## Gate outputs required BEFORE assembly
- WAVE2_MOTION_GATE.md (per-clip 11-criteria verdict + reason)
- WAVE2_GARMENT_FRAME_SHEET.jpg (first/mid/final garment crops per clip vs the real macro)
- updated MOTION_JOBS.md (keep/reroll/cut status per beat)
- keep / reroll / cut list with the exact reason for every reroll
DO NOT assemble, Topaz, or final-edit until every product-visible clip has a PASS or a documented workaround.
