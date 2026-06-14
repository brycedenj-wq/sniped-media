# ALMA LOVE CLUB — SHIP STATE (live production state)

Updated 2026-06-14. The client deliverable: a 30-45s cinematic swimwear commercial for Alma Love Club (Kennedie), plus 15s + 7-10s hook + photo selects. Client notes (locked spec): WIDE / horizontal, SLOW pacing (longer holds, no fast cutting, no slo-mo), LESS sound effects, CLEAN/sharp, feels like the Margiela / Charlie Denis inspo (one intentional cinematic scene, not clips). She is fine with AI in her brand. Gate: she LOVES it (her eye + operator, never a machine score).

## LOCKED ASSETS (done)
- Logo: `03_CLIENT_DIRECTION/ALMA_LOVE_CLUB_logo_black.png` / `_white.png` / `.svg` (Archivo Black).
- Product kit: `PRODUCT_KIT/` (product_front_torso, product_front_full, product_back_twomodel, detail_cherry, detail_dice, detail_bow_tie, print_swatch) + `PRODUCT_TRUTH.md`.
- Higgsfield product Element: `alma-love-club-suit` id `d3a34776-3fb3-46f4-a2c9-19f38e599348` (embed `<<<d3a34776-3fb3-46f4-a2c9-19f38e599348>>>` in prompts to lock the suit). Older element `alma-cherry-bikini` (132fd9cb) also exists.
- Confirmed product media_ids on Higgsfield: torso ba98acf3, front c886be87, cherry e87f6456, dice a6051131, swatch 84dfc29d.
- Brand model: MARISOL. Keystone = candidate B (`MARISOL_MODEL/MARISOL_keystone.png`). Soul `soul_id: bae9312a-3ffe-42f0-8e4c-77ed35b37ea8` (TRAINING, ready ~10 min). Use with model `soul_2` + soul_id.
- Real footage: 62 clips in `New Folder With Items/01_RAW_VIDEO` (23 horizontal Canon = the widescreen spine; 39 vertical iPhone chaos = mostly drop or AI-extend). EVOTO product masters in `02_EDITED_STUDIO_PHOTO/EVOTO`.

## PLANS PRODUCED (read before building)
- Cinematic board + look bible + Higgsfield prompts: workflow `wf_35307ea3-715` output (warm Portra, faded blacks, wide 16:9, 24/35/50mm, one scene, garment-lock via 2-image EVOTO swap, identity-lock via keystone).
- Real-footage cut plan (beat -> exact take + in/out + gaps): workflow `wf_74f630d6-ae4` output. Gaps with NO real footage (AI-generate): speaker gag, handcuff, dog-leash tug.

## ALL-AI BUILD · LIVE BEATS (2026-06-14 build session)
Decision: FULLY AI (MARISOL + locked suit), one golden-hour Mercedes/Beverly-Hills scene. Client is fine with AI; mid-day low-budget realism is acceptable to her. All beats native Seedance 2.0 1080p, held camera + authored performance motion (Push-In Law honored), unified light grade (`graded_beats/`).

Source soul stills (text2image_soul_v2, MARISOL soul bae9312a, 2048x1152):
- cold-open seated-on-hood: still `4eef927b` → motion job `9dfac65a` (8s) → `ai_beats/m_coldopen.mp4` → `graded_beats/g_coldopen.mp4` DONE
- walk toward camera: still `73be4212` → motion (8s job 6b2aa0f7 = NSFW-flagged; re-run 5s job `5da40833`) IN PROGRESS
- front hero stand: still `794629bf` → motion job `e1185c07` (5s) → `ai_beats/m_fronthero.mp4` → `graded_beats/g_fronthero.mp4` DONE
- trunk back-reveal + glance: still `56c3d884` → motion job `6518d8bc` (5s) → `ai_beats/m_trunk.mp4` → `graded_beats/g_trunk.mp4` DONE (hero frame)
- product detail (hip/tie): still `bc26e43a` → garment-lock swap nano_banana [bc26e43a + real torso ba98acf3] = `1c256469` (print+cherries locked) → motion job `f6ebc4da` (5s) IN PROGRESS

Cut order (one scene, slow, hard cuts): cold-open → walk → front-hero → detail → trunk → END CARD.
- END CARD: `endcard/endcard.mp4` (REAL client white logo `Alma Love Logo.png.PNG`, trimmed 784x116, warm near-black, grain). DONE.
- MUSIC: owned bed `audio/music__20260614_110832.mp3` (38s, ElevenLabs compose, clean rights). DONE.
- Grade string (unified, light): crop 0.96 → scale 1920x1080 lanczos → curves black-lift 0.02/white 0.98 → sat 1.03 → warm colorbalance → grain noise=3 → unsharp 0.25 → 24fps.
- Validated pipeline: `_DRAFT_3beat.mp4` (cold-open+front+trunk+card+music, 19.6s) builds clean.
- Product-fidelity note: garment-lock landed print + cherries + cream bows; SILVER DICE on tails still missing (tails cropped short) = the one known micro-miss to flag in verify.

## V4 PRODUCT-EXACT PIPELINE (2026-06-14, operator gate: "exact suit is THE gate")
Adversarial verify on v3 = DO-NOT-SHIP: AI never holds the real fine dotted-feather print, the rhinestone cherries, or the silver dice on a body. Operator rule: Higgsfield = scene/model/pose/motion; the GARMENT is locked from REAL EVOTO pixels; demote/cut any beat that can't be exact.
- REAL exact-product signature beats (the unmistakable core): real cherry crop uploaded `471484d8` -> i2v `63e513c2` -> `graded_beats/g_cherry.mp4` (paired rhinestone cherries EXACT, glint, 4s); real dice crop uploaded `78640c6a` -> i2v `332ff2ee` -> `graded_beats/g_dice.mp4` (silver dice + dot print EXACT, sway, 4s). Source = PRODUCT_KIT detail_cherry/detail_dice warm-graded.
- Front-hero on-body: improved 3-ref swap (794629bf + real torso ba98acf3 + real cherry 471484d8) with PRECISE fine-dotted-print description = still `4634480c` (print now fine coral-dot on cream, cherry at cup, reads as her suit at full-body scale) -> i2v `eebd42be` -> grade g_fronthero.
- Trunk re-graded WARMER (g_trunk) to kill the bluer-sky "second scene" read.
- Cold-open + walk = AI atmosphere (suit small/backlit, scene only).
- v4 cut order: cold-open -> walk -> front-hero(corrected) -> CHERRY(real) -> DICE(real) -> trunk -> END CARD. Macros carry exact signature right after the full-body look.
- Skin note: real EVOTO model is deeper-skinned than MARISOL; macros kept TIGHT (mostly suit/jewels) + warm-graded so no face/skin clash.
- Prior v3 (`ALMA_v3_full.mp4`) = all-coral but AI-approx print, NO dice/cherries = superseded.

## ROADMAP TO SHIP (remaining)
1. Generate the AI cinematic beats (establishing/world + the 3 gap beats) with MARISOL soul + the suit Element, garment-locked, warm-Portra look. Win stills first, then motion (Seedance/Kling), product-vs-motion inverse honored.
2. Assemble in Premiere: real Canon hero/product holds + AI beats, slow, wide, one continuous scene. Mask the Mercedes plate where visible.
3. Finish: Lumetri warm-dusty grade; After Effects ALMA LOVE CLUB title bookends, lens-wipe, freezes; ElevenLabs sparse SFX + one music bed.
4. Adversarial whole-watch vs Kennedie's exact notes (wide/slow/clean/inspo/suit-hero) + second-model hostile pass + operator eye. No self-crown.
5. Deliver: 30-45s hero + 15s + 7-10s hook + 8-12 photo selects.

## STANDING LAWS
Garment never freehand (2-image swap to the EVOTO product). Stills before motion. Real product footage carries fidelity; AI carries the wide world. Necklace/cuffs are styling, not product. No em-dashes.
