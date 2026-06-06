# REFERENCE INGESTION DASHBOARD

> State of the Commercial Craft layer. Updated 2026-06-06.

## Capability status: ACTIVE (proven end-to-end)
| Piece | Status |
|---|---|
| os_reference_ingest.py | ACTIVE , real YouTube ingest proven (403 bypassed via player_client) |
| os_commercial_card.py | ACTIVE , 7 cards seeded, render-md works |
| os_reference_gate.py | ACTIVE , loads cards + scores a built video (flagged SOLE film slow) |
| OS_COMMERCIAL_CRAFT_LIBRARY.md | rendered (7 cards) |
| REFERENCE_LIBRARY_INDEX.md | auto-maintained by ingest |
| Route wiring | video_campaign / film / ad / social_rollout / photo_post / still_range load COMMERCIAL_CRAFT |
| Registry | os.reference_ingest / os.commercial_card / os.reference_gate = ACTIVE |

## References ingested
| ref_id | source | shots | ASL | notes |
|---|---|---|---|---|
| creative_tv_comp_1 | YouTube bIRa63nR2mU (Top 10 Creative TV Commercials), 90s | 13 | 6.92s | compilation (mixed pacing); proves pipeline. Frames + audio captured; no captions -> STT-fallback path logged |

## Card library: 7 cards
cc_anything_but_itself · cc_freeze_then_product_pause · cc_aggressive_angle_is_the_cover · cc_pacing_contrast_band · cc_earn_attention_spectacle_open · cc_sound_led_cut · cc_branded_title_beat
(seeded from the ingested reference + operator shoot-doctrine; grow by ingesting single spots.)

## Next references worth ingesting (operator-supplied links, single spots > compilations)
The 5 other links the operator dropped (commercial + show-editing compilations) , ingest each as a single-spot section for clean craft cards. Run: `os_reference_ingest.py <url> --id <name> --seconds 120`.

## Acceptance test (2026-06-06): PASS
frames extracted (13) · transcript fallback logged (STT on audio.mp3) · shot_map.csv + pacing.json written · 7 craft cards created · gate loaded + scored a built video against cards · video_campaign loadout now includes COMMERCIAL_CRAFT (373 cards).

## Honest gaps
- Captions absent on the test video -> STT not yet run (audio.mp3 ready; ElevenLabs speech_to_text is the next call).
- Scene-cut threshold (0.3) merges slow/dissolve cuts on compilations; tune per source.
- Music nuance is inferred, not analyzed.
