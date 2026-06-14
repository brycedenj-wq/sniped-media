# ALMA LOVE — EXACT-PRODUCT VIDEO PIPELINE (the can't-fail SOP)

Date: 2026-06-14. Built from the failures of the all-AI attempt.

## THE ONE LAW
WIN THE SUIT EXACT ON A STILL FIRST. Hold every still next to the real product photos and reject it if the suit is wrong, BEFORE you animate anything. Motion cannot be made pixel-exact with today's AI. Stills can. Every failure so far came from gambling the exact suit inside a generation or inside motion. This pipeline never does that.

## WHY TODAY FAILED (so we never repeat it)
- Freehand prompting the print: AI repaints it every time, gets paisley/mottle. FAIL.
- Garment-swap in one shot: fused the two-piece into a one-piece, approximated the print. FAIL.
- Product-lock in motion (Marketing Studio): closest print, but forces UGC vertical talking style + failed on swimwear moderation. WRONG VIBE.
- Conclusion: exact print + cinematic + our character, all three in one MOVING shot, is not reliably possible in June 2026. So we win exactness on stills and keep motion subtle.

## THE DIVISION OF LABOR (who does what)
- WEB APP, you, visual control: Higgsfield web (Soul, Soul Cinema Studio stills, Virtual Try-On, pick/regenerate). You SEE each result and re-roll instantly. This is where judgment lives.
- PHOTOSHOP, you or a retoucher: the guaranteed-exact print composite on hero + product-detail stills. The only method that is truly pixel-exact.
- ME (in chat / MCP): the repeatable mechanical parts, batch stills, assemble the cut, one master grade, sound design, file wrangling, the proof pack.

## THE STEPS

### 1. Character (DONE, reuse forever)
Higgsfield Soul "alma-lead-deadpan" (already trained). Same woman every shot. Never retrain.

### 2. Generate the SHOT STILL on the web (Soul Cinema Studio)
- Higgsfield web -> Soul Cinema Studio -> pick the Soul -> prompt the scene (Palm Springs desert, black vintage convertible, pose, deadpan, aviators).
- Generate 4. Pick the best by eye.
- GATE: composition + character right? (Suit can be wrong here, we fix it next.)

### 3. Put the EXACT suit on the still (the make-or-break step)
Pick ONE path, in this order:
- 3a. WEB VIRTUAL TRY-ON: Higgsfield web -> Virtual Try On -> the still + the product "Alma Love Bikini FULL REF" (18 real photos, already uploaded). On a STILL the product-lock is far more reliable than in motion. Output a fitted still.
- 3b. IF try-on drifts the print: PHOTOSHOP. Open the still, mask the suit (Select Subject then refine, or pen-tool the triangles + bottoms), place the real print swatch (PRINT_SWATCH_clean.png), Edit > Transform > Warp to follow the body, set the print layer to Multiply or Overlay so the suit's shadows/folds show through, drop opacity to taste. Add the cherry (CHERRY_clean.png) on the cup and the dice (DICE_clean.png) on the tails as small overlays. This is GUARANTEED exact because it is the real fabric pixels.
- HARD GATE (do not skip, do not proceed until it passes): put the still next to FRONT_full / CHERRY_detail / DICE_detail / BACK_detail. Check: two-piece? coral feather-fern stipple on cream (not paisley, not mottle)? cherry on a cup? silver dice on the tails? NO necklace? If any are wrong, fix it HERE on the still. Never carry a wrong suit into motion.

### 4. Animate ONLY the approved exact still (web Seedance or Kling i2v)
- Use the approved exact still as the START frame.
- Author SUBTLE motion only: a head turn, wind in the hair, a slow push-in. Keep the torso/suit nearly static so the print barely moves.
- Generate 2-3 takes. Keep the one where the suit holds. Cut around any frame where it drifts/melts.
- GATE: watch the clip end to end. Suit still reads as the real product? No melt? Keep or re-roll.

### 5. The product-detail / "buy it" beats
- For the shots a customer pauses on to see what they are buying: keep them as the EXACT still with a slow, controlled push (Ken Burns) ONLY. Do NOT heavily animate the print. A slow push on a Photoshop-exact still is pixel-exact AND moving.
- Intercut these exact detail beats with the AI-motion wides.

### 6. Assemble + grade + sound
- Cut the approved clips + detail beats to the story. One warm master grade. Diegetic sound + a music bed.
- I do this in chat, or you in CapCut/Premiere.

### 7. Final gate
- Whole-watch. Your eye. The client's eye.

## WHY THIS CAN'T FAIL LIKE TODAY
1. Exactness is won on STILLS (controllable, human-gated against the real photos), never gambled in motion.
2. The exact suit comes from Virtual Try-On or real-print Photoshop compositing, human-controlled, not freehand AI guessing.
3. A hard product gate stops any wrong suit before it ever moves.
4. Motion is kept subtle so the exact print barely moves; detail beats stay near-still and stay pixel-exact.

## ASSETS ALREADY BUILT (ready to use)
- Soul: alma-lead-deadpan (reusable character).
- Product (web): "Alma Love Bikini FULL REF" = 18 real photos (front/back/cherry/dice/angles). Also "ALMA SWIMSUIT CHERRY" (5 photos).
- Custom avatar (web Marketing Studio): "Alma Lead Deadpan".
- Exact garment assets (in keyframes/v2/GARMENT_TRUTH/): ALMA_SUIT_SPEC.png, PRINT_SWATCH_clean.png, FRONT_TORSO_clean.png, CHERRY_clean.png, DICE_clean.png, FRONT_full.png, BACK_detail.png.
- A proven cinematic shot: the Palm Springs desert trunk shot (Soul + Seedance), vibe-correct.
