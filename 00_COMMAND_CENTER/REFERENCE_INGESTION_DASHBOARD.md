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

---
## UPDATE 2026-06-06 , first batch (6 refs) + BENCHMARK V1 + gate wired
Ingested batch: creative_tv_comp_1 (6.92s, compilation) · best_comm_2 Super Bowl funny (1.96s) · best_comm_3 best commercials (3.85s) · best_comm_4 Heinz/Ed Sheeran SINGLE spot (2.47s) · show_editing_1 MKBHD tutorial (4.76s) · show_editing_2 Reels tutorial (16.67s). Captions captured for the 5 new (copy/VO structure available).
- **COMMERCIAL_CRAFT_BENCHMARK_V1.md** built from this batch (ASL bands, hook patterns, transitions, audio-sync, typography, shot variety, structures, expensive-vs-amateur).
- **os_reference_gate.py wired to the benchmark**: named auto-verdicts TOO_SLOW / TOO_FAST / TOO_REPETITIVE / NO_COMMERCIAL_PAYOFF / LOW_SHOT_VARIATION / AUDIO_NOT_MOTIVATING_CUTS + manual WEAK_TRANSITION_LOGIC / COPY_VO_NOT_CARRYING. `--type commercial|comedy|story|cinematic|tutorial`.
- **Validation:** Heinz single commercial PASSES (ASL 2.47s, no auto-fails); our SOLE manifesto FAILS as a commercial (TOO_SLOW 11.7s, low variation) , correct: it is a luxury art-film pace, not a spot. Gate discriminates real-commercial vs slow-film.
- Single spots > compilations confirmed: best_comm_4 (single) gives the cleanest data; compilations skew ASL via title cards.
