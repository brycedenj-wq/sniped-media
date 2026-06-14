# Edit Plan · 9:16 Master + YouTube Cut

**Assembly tool:** Premiere Pro MCP (verified available). **Motion title:** After Effects MCP if needed. **Grade:** Premiere Lumetri, warm documentary, anti-gloss.

## Sequence specs
- **Primary · 9:16 vertical:** 1080 x 1920, 24 fps (filmic, not 30), ~50s. This is the priority cut (where the client lives).
- **Secondary · YouTube 16:9:** 1920 x 1080, 24 fps, same edit conformed. Use `auto_reframe_sequence` as a starting point, then hand-correct the hero framing (V7 two-shot, V8 hands, V10 exhale) so faces never drift to the edge. Vertical was framed first, so protect headroom when widening.

## Timeline build order (Premiere MCP)
1. `create_project` then `create_sequence` at 1080x1920/24 for the vertical master.
2. `import_media` the approved clips (V1 to V12) and the audio stems (score, in-world cue, VO, SFX).
3. Lay V1 to V12 per the script timecodes in `02_WINNER_SCRIPT`. Use `add_to_timeline` and trim to the per-shot durations.
4. Audio: VO on A1, score on A2, in-world cue on A3, SFX/room tone on A4. `adjust_audio_levels` so VO sits clean over the bed; duck the score under VO lines.
5. Captions: `create_caption_track` for the muted-viewing safe captions (2:14 AM, "You're not failing.", the button). Vertical-feed viewers watch sound-off; the hook and payoff must read silent.
6. Title button: V12 via `add_text_overlay` (or AE for a slow fade) on warm near-black.
7. Grade: adjustment layer (`add_adjustment_layer`) with Lumetri. Warm, lifted-soft blacks, gentle desaturation, light grain. Match the locked anti-gloss look across all clips so the AI shots read as one film.
8. Export: `export_sequence` H.264, high bitrate, 9:16. Then duplicate, conform to 16:9, re-check framing, export the YouTube cut.

## Pacing discipline (per Commercial Craft Benchmark V2, emotional-brand-film profile)
- Target ASL 3.5 to 6.5s overall, but the carrying montage (V3) runs fast (~1.5 to 2s beats) to create the jagged edge, and the two hero beats run long: **V7 song = ~7s (the single longest hold), V10 exhale = ~6s.** That length CONTRAST is the craft signal (hero hold >= 2x the montage beats, well over the 2.2x contrast bar).
- Every cut is motivated (a line, a sound, the door, the exhale). No unmotivated dissolves. Per `edit_motivated_only`.
- One consistent grade, one title system, one music bed. Restraint is the brand here.

## Two-cut derivative plan (bonus, same asset bank)
- **Family cut (9:16, the master above).**
- **Caregiver cut (~40s, recruiting):** reorder to open on V4/V5 kitchen handoff, swap the VO to the caregiver script in `02_WINNER_SCRIPT`, end on a recruiting button. Same clips, same grade, same score. Proves the "more places to put the story" want without a second shoot.

## Output naming
`SYNERGY_THE_DOOR_v1_9x16.mp4` · `SYNERGY_THE_DOOR_v1_16x9.mp4` · (later) `SYNERGY_THE_CALLING_caregiver_9x16.mp4`. Drop renders into `_assets_bank/` then promote the approved master.
