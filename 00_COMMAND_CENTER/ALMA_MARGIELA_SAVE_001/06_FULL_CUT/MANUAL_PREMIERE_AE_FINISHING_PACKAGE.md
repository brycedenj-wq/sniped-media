# ALMA LOVE CLUB · MANUAL PREMIERE / AE FINISHING PACKAGE
For executing the commercial finish by hand in Premiere Pro + After Effects. Mirrors the automated ffmpeg master so the two match. Premiere bridge connected (v26.2.2); AE bridge needs the MCP Bridge Auto panel open + "Allow Scripts to Write Files" ON.

## SOURCE CLIPS (clean, ungraded) and TIMELINE ORDER
Sequence: 1920x1080, 23.976 or 24 fps, ProRes 422 or H.264 master.
Base path for beats: 00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/02_VIDEO_TESTS/ ; macros: 03_REAL_MACROS/

| # | Clip | In | Dur | Notes |
|---|------|----|-----|-------|
| 1 | B01_kling_c94b30be.mp4 (noon wide) | 0.0 | 3.0 | establish, deadpan hold |
| 2 | PROD_hood_ab35eaac.mp4 (product on hood) | 0.4 | 2.0 | product only, no body |
| 3 | B03_walk_b41fac11.mp4 (walk from speaker) | 0.5 | 2.6 | |
| 4 | MACRO_cherry_2812.mp4 (REAL rhinestone cherry) | 0.0 | 2.0 | real garment macro |
| 5 | B06_gas_kling_ba948b6e.mp4 (gas station) | 0.0 | 3.0 | golden hour |
| 6 | B08_rearview_a75d09fe.mp4 (rearview lipstick) | 0.4 | 2.6 | |
| 7 | PROD_mirror_a7638a45.mp4 (product on mirror) | 0.4 | 2.0 | product only |
| 8 | B10_solitaire_f028ce60.mp4 (cards on hood) | 0.0 | 2.8 | |
| 9 | MACRO_dice_2810.mp4 (REAL dice beads) | 0.0 | 1.8 | real garment macro |
| - | 4-frame dip to black | - | 0.166 | motivated breath before payoff |
| 10 | B19_night_kling_b0aecae7.mp4 (night finale) | 0.0 | 4.0 | headlight payoff, longest hold |
| 11 | END CARD (designed, see below) | - | 3.2 | |
Total picture ~29.0s. NOTE the bow macro was dropped (was redundant with dice; tightened the draggy 20-24s stretch).

## PER-CLIP WHITE BALANCE (unify the cool/warm mismatch BEFORE the LUT)
Measured mean warmth (R-B) per beat and the correction applied (Lumetri > Basic > Temperature/Tint, or Color Balance). Positive temp = warmer.
- B01 noon: measured COOL (R-B -4). WARM it: Temperature +12 to +15.
- B03 walk: +5. Temperature +3.
- B06 gas: +14. Temperature -4 (slightly cool the over-warm).
- B08 rearview: +10. neutral.
- B10 solitaire: +41 (hottest). Temperature -22, Tint slightly green to kill orange.
- B19 night: +43. Temperature -20, lift shadows (Lumetri > Curves, raise shadow point), keep warm-dark.
- PROD_hood: +8. neutral.
- PROD_mirror: +25. Temperature -13.
- MACRO_cherry: +46 (real studio, warm). Temperature -16 but PROTECT the red cherries (keep highlights red).
- MACRO_dice: +32. Temperature -12.
Target: all DAY beats land near +8 to +12 warmth; night/macros stay warmer but in the family.

## ONE MASTER LUT (the unified look)
- LUT file: ALMA_LOVE_PRODUCTION_001/.../ALMA_LOVE_BRAND_KIT/preset/ALMA_LOVE_signature_look_v1.cube
- Apply on a SINGLE adjustment layer over the whole timeline (Lumetri > Creative > Look = the .cube).
- CRITICAL: intensity ~40-45%, NOT 100%. At full strength on this AI material it pushes magenta and turns skin purple. 42% keeps the brand tint while skin stays natural. (The automated master uses a 42% blend; match that.)

## FILM FINISH (one adjustment layer over everything, after the LUT)
1. 35mm grain: AE > Add Grain (or Premiere Noise ~6-8%), temporal. Keep visible but not crunchy.
2. Halation: AE pass = duplicate, Levels to isolate highlights (clip below ~0.75), Gaussian Blur ~14, tint warm (slight red/orange), composite SCREEN at ~28% opacity. (Premiere alt: Lumetri Glow or a screened blurred-highlights track.)
3. Sharpness pulldown: negative sharpen / Lumetri Sharpen ~ -15, or a 0.4px Gaussian, to kill the clean digital edge.
4. Vignette: Lumetri > Vignette amount ~ -1.0, feather high.

## TRANSITIONS (motivated only, no templates)
- All cuts are HARD CUTS (Margiela grammar). No cross-dissolves, no wipes.
- The ONLY non-hard element: a 4-frame dip-to-black before the night finale (a breath before the payoff). Motivated by the day-to-night jump.
- The real-garment macros (clips 4, 9) act as texture cut-aways that bridge the human beats; place them ON the cut, not as transitions.

## DESIGNED END CARD (not a flat screenshot)
- Asset: ALMA_LOVE_BRAND_KIT/logo/ALMA_LOVE_wordmark_cream.png (2727x648, transparent alpha). Operator's real wordmark.
- On deep near-black (0x0A0708). Scale wordmark to ~820px wide, centered.
- Give it a soft drop shadow (4px down), a faint halation glow (duplicate > blur 10 > screen), and the SAME film grain as the body so it belongs to the film, not a Canva overlay.
- Hold 3.2s. Optional: 8-frame fade up from black.
- For a wordmark-over-footage moment (e.g. lower third on the night beat), match perspective/scale, drop opacity to ~85%, add grain + slight blur so it sits in the plate.

## AUDIO
- Owned, commercially licensed track: 05_AUDIO/music__20260612_200235.mp3 (ElevenLabs, 35s). Backup: MUSIC_sonilo_4dbb75a5.m4a (Higgsfield).
- Trim to picture length, fade in 0.6s, fade out 1.6s, loudness normalize to about -15 LUFS, true peak -1.5.
- Optional diegetic SFX layer (ElevenLabs text_to_sound_effects, now on a paid plan): street tone, heels, distant traffic, a single dice click on the night beat. The film must read with music muted.

## EXPORT SETTINGS
- Master: H.264, 1920x1080, 24fps, ~20-40 Mbps VBR 2-pass, AAC 256k. Or ProRes 422 HQ for archive.
- Web preview: H.264 1280x720, CRF ~23, faststart, AAC 160k.
- Platform masters (later): 4:5 and 9:16 reframes that keep the product fully in frame, measure skin/product color drift per master.

## QA GATES BEFORE ANY CLIENT SEND
/watch full pass, Gemini hostile pass, Commercial Craft 12-axis >= 30/36, 9/10 floor, skin not crushed, one consistent grade, no per-shot AI glow mismatch. PROOF_MANIFEST updated. Operator send/no-send.
