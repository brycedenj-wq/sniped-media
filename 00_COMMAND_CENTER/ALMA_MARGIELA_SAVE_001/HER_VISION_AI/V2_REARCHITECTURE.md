# DEADPAN SUMMER · V2 RE-ARCHITECTURE (2026-06-13)

## Why (the wall, named)
Three strict adversarial keyframe rounds + a hero re-check at the operator's 10/10 bar proved a hard toolchain ceiling:
1. **Sustained full-body print regen drifts.** Every REGENERATED product-hero pose mutates the coral-on-cream feather-fan print (to tie-dye / pink / floral / heart / near-nude). Confirmed on b18, b12, b06, b03, original motion gate.
2. **Prominent hero hands tell.** Macro/focal hands melt or finger-merge on pixel-zoom (b04 button, b10 towel grip, b14 lipstick grip).
3. **Regen can swap identity.** b15 recline came back a different woman with a drink (independently confirms the v1 off-model flag).

Hero re-check verdicts: b09 back-reveal = KEEP; b18/b12/b06 = REROLL (print); b15 = CUT (wrong person). So 4 of 5 "heroes" were over-crowned (self-preferential bias) and fail the real 10/10 bar.

## The fix (design out both walls)
- **Product truth comes from CROPPING the one correct source, not regenerating.** The keystone (job 2aef74e4) print MATCHES the real product (verified vs REAL_front / REAL_cherry). Upscaled it to 4K (job be7e2aea -> KEYSTONE_4K.png) and crop multiple framings. Same pixels => the print physically cannot drift, and there are no hero hands to melt.
- **Connective/comedy beats are product-NEUTRAL with hands designed out** (suit concealed/out of frame; hands cropped off). The 5 product beats carry the suit; inserts don't need it.
- Motion: product beats get MICRO motion (Seedance i2v + Element <<<132fd9cb>>> to lock print) or a tasteful in-post camera move (guaranteed zero drift) as fallback. Connective beats can take more authored motion.

## ASSEMBLY SET (gated by wf waznvgy4l before animation)
PRODUCT-TRUE (keystone crops, print = source pixels):
- KS_wide  (establishing, bulldog)      keyframes/v2/kscrop/KS_wide.png
- KS_medium (waist-up deadpan hero)     keyframes/v2/kscrop/KS_medium.png
- KS_chest  (suit-top detail)           keyframes/v2/kscrop/KS_chest.png
- KS_hip    (side-tie + print detail)   keyframes/v2/kscrop/KS_hip.png
- b09 back-reveal (motion clip, holds)  motion/gate_redo/b09_backreveal.mp4
CONNECTIVE (product-neutral, hands out):
- b02 stepin (legs/feet)                keyframes/v2/b02_stepin.png (+ motion/b02_stepin.mp4)
- towel_crop (deadpan over towel)       keyframes/v2/conn/towel_crop.png
- rearview_face (deadpan red lipstick)  keyframes/v2/conn/rearview_face_up.png
END CARD: audio/ENDCARD.png

## CUT (do not chase; covered by the above or unfixable at 10/10)
b01 lenswipe, b03 speaker, b04 button, b05 kick, b08 leash, b15 recline (wrong person), b06 walkoff (near-nude), b18 poster (print drift), b12 palmbeauty (print drift), b14 full rearview (hand melt; replaced by the tight face crop), b10 full towel (hands; replaced by the cropped version).

## NEXT
gate waznvgy4l -> animate keeps (Seedance micro + Element; post camera-move fallback) -> dual-gate clips -> assemble 16:9 (open KS_wide) -> coral-on-cream unify grade + grain + 4K text/plate sweep -> music + endcard -> alma-final-verify -> send/no-send. send_no_send stays NO until the final verify clears >=9/10.
