# ALMA LOVE CLUB v2 · GRADE CONSISTENCY NOTES
The finishing decisions and the measured proof they worked. Master: ALMA_LOVE_FULL_CUT_v2_FINISH.mp4 (29.08s, 1920x1080).

## THE PROBLEM (v1)
A fresh-context whole-watch judge measured v1: cool noon (R-B -4) cut against warm gas (+14), solitaire (+41), night (+43). Three color worlds = the "bunch of clips" read. No grain. Plus a draggy 20-24s macro stretch.

## THE FIX (v2), data-driven
1. MEASURED every beat's mean warmth (R-B) via 1x1 downscale. Noon was the cool outlier (-4); solitaire and the real macros were the hot end (+41, +46).
2. PER-BEAT WHITE BALANCE before any LUT: warmed the cool noon (+12 to +15), cooled the hot solitaire (-22) and the warm studio macros, leaving night warm-dark but in the family. Target band: day beats ~ +8 to +12.
3. ONE MASTER LUT: the real ALMA_LOVE_signature_look_v1.cube, blended at 30%. Full strength (and even 42%) pushed magenta and turned skin purple, so 30% + a green-recovery pass keeps the brand tint while skin stays natural.
4. GREEN-RECOVERY (global, after the LUT): colorbalance gm +0.10 / gh +0.07 / gs +0.04, bm -0.05 / bh -0.03, rm -0.02. This pulls the magenta the LUT introduces and restores natural skin (R > G > B).
5. UNIFORM FILM FINISH on the whole body: halation (highlights isolated > blur 14 > screen 22%, near-neutral so the glow is not pink), 35mm grain (noise alls=11 temporal), sharpness pulldown (unsharp la -0.45), vignette (PI/8).
6. END CARD built CLEAN and appended AFTER the grade, from the operator's real ALMA LOVE CLUB wordmark (white on black), so it is not washed by the film grade.
7. TIGHTENED: dropped the redundant bow macro; the 20-24s stretch no longer drags.

## MEASURED PROOF (skin patch mean RGB, must be R>G>B for natural tan)
| Beat | R | G | B | Verdict |
|------|---|---|---|---------|
| noon | 176 | 136 | 81 | R>G>B natural |
| gas | 170 | 145 | 95 | R>G>B natural |
| solitaire | 128 | 110 | 70 | R>G>B natural |
| night | 164 | 138 | 84 | R>G>B natural |
Independent judge re-measured and confirmed R>G>B on all four beats. The v1 magenta cast (B>G) is gone.

## GRADE BALANCE TARGETS (the master look)
- Skin: natural warm tan, never magenta, never crushed (detail held in shadows).
- Car blacks: deep but not clipped (vignette + LUT hold them rich).
- Red/pink swimwear: saturated cherry red reads as the signature accent, not blown.
- Sky (noon): retains believable blue under the warm wash.
- Night/gas: warm but inside the same film family as day, not a separate stock.

## RESIDUAL (honest, below the send bar)
- Mild softness at the red-heel / foot junction on two beats (AI generation limit, not grade).
- Mercedes badge chrome slightly mushy on the gas beat (AI limit).
These are generation artifacts, not finishing errors, and do not read at fashion-film viewing distance.

## TOOLCHAIN NOTE
This master was finished via ffmpeg applying the REAL brand .cube LUT (identical look to Premiere Lumetri with the same file), because the Premiere CEP bridge hung on a modal dialog mid-session and AE's MCP cannot import/render external footage. The editable Premiere route is fully documented in MANUAL_PREMIERE_AE_FINISHING_PACKAGE.md and reproduces these exact settings.
