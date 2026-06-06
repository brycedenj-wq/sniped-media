# FILM FINISH PLAN , SOVRA/SOLE manifesto (2026-06-06)

> Build the 90s master from EXISTING assets + Blender/ffmpeg + free-tier VO/SFX. Higgsfield only if a beat truly needs generation. Ceiling 120 cr (target: 0). Music = paid-engine blocker -> brief, not melody.

## Pre-checks (done)
boot 6cb0384 · balance 546.5 · video edit route: Premiere ACTIVE (preferred), ffmpeg = assembly/export spine, AE automated available · audio stack gate: BLOCK (music engine; ElevenLabs PASS) · libraries loaded.

## 90s structure (beats)
| # | Beat | t | Visual (existing asset) | VO |
|---|---|---|---|---|
| 1 | Cold open | 0:00-0:09 | S01 open vault, slow push to the light | "Every market begins the same way..." |
| 2 | The problem | 0:09-0:24 | S04 empty plinth, slow ken-burns + title | "Then the work got good. All of it. Good is now free..." |
| 3 | The turn | 0:24-0:33 | clip2 vault-door push (gravity) | "So we stopped trying to make you better. Better is a category." |
| 4 | The claim | 0:33-0:50 | clip1 open-vault push + claim title card | "Meridian and Hale is no longer a firm that litigates..." |
| 5 | World proof | 0:50-1:05 | montage: S05 door, S09 silhouette, S11 gallery (ken-burns) | "One claim. One world built to hold it. One mark, struck once." |
| 6 | Seal strike | 1:05-1:16 | Blender Seal FINAL, ffmpeg push + brass flash on SFX hit | "[pause] The only one." (STRIKE) |
| 7 | Offer thesis | 1:16-1:26 | title cards over ink / S11 | "Seventy-two hours. One house at a time. A verdict you repeat for years." |
| 8 | Final line | 1:26-1:32 | cardD + Seal | "We do not make you better. We make you the only one." |

Runtime target ~92s. Faceless throughout (S09 is pure silhouette).

## Version map
- **90s** , the full manifesto (above). Master.
- **30s** , beats 1 (short) + 4 claim + 6 strike + 8 final. Cut from the master.
- **15s** , beats 1 (2s) + 4 (one line) + 6 strike + 8 final.
- **6s** , the strike + "The only one." (bumper). Silent-safe.
All exported 16:9 1080p; a 9:16 reframe is a documented next step (not in this pass).

## Captions / safe areas
- Burn-in captions OFF for the master (VO carries it); an SRT sidecar is generated for the 90s for accessibility + sound-off viewing.
- Title-safe: keep titles within 5% margin (96px at 1920). Lower-third titles sit at y=820-980. Seal/center elements within action-safe.

## Routes used
- Assembly + export: **ffmpeg** (proven HYBRID spine). Seal-strike = ffmpeg zoom + brass flash on the Blender still (0 cr, avoids the ip-flagged i2v).
- Motion: 2 existing Seedance clips + ken-burns on 7 stills. **0 new Higgsfield generation** (no beat required it; the "nameplate rising" claim beat is carried by a title card + the vault push, logged as the one place a future generated beat would add lift).
- Titles: PIL/ffmpeg drawtext cards in the Bodoni/Didot register (AE authoring proven; aerender available for a later kinetic-type upgrade).
- VO: ElevenLabs (free tier). SFX: seal-strike (have) + a generated free vault room-tone bed.

## Spend
Higgsfield: **0 credits** this build. Audio: free tier. Blender/ffmpeg/AE: 0. Under the 120 ceiling with full headroom.

## Final-call rule
The film is NOT called "final/complete sound" because the music (melody) engine is a paid blocker (see SOUND_MUSIC_BRIEF.md). It is a **complete picture-cut + VO + SFX + room-tone master**; music is the one logged remaining layer.

---
## STATUS (2026-06-06): MASTER BUILT
70.2s 1080p master + 30/15/6 cutdowns assembled via ffmpeg (build.sh). Picture + VO (eleven_v3-capable, rendered v2-safe @0.9 speed) + seal-strike SFX + vault room-tone bed. 0 Higgsfield credits this build. NOT called "final sound": MUSIC (melody) remains the paid-engine blocker per SOUND_MUSIC_BRIEF.md. Audio stack gate stays BLOCK on music; everything else done.
