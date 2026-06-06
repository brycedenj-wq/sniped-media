# OS COMMERCIAL CRAFT LIBRARY

> Repeatable editing/copy/design/audio moves extracted from ingested references + operator doctrine. Each card is callable by `os_reference_gate.py`. NOT inspiration; specific moves. Build references with `os_reference_ingest.py`, add cards with `os_commercial_card.py add`.

**{len(cards)} cards.**

## cc_anything_but_itself  (concept/copy)
- **Problem:** Product shots read like a catalog; nobody stops for them.
- **When to use:** Any product hero where the literal object is boring (swimsuit, watch, sneaker, bottle).
- **Principle:** Frame the product as anything BUT what it is. Borrow a charged genre (editorial crime, heist, museum, sport) so the object gains stakes.
- **Exact move:** Pick one juxtaposition ('what if this were a drug bust / a Rolex / contraband') and stage one image around it: e.g. handcuffs dangling off the index finger, palm up, as the opening frame.
- **Evidence:** operator shoot-doctrine (Alma Love prep) + creative_tv_comp_1 spectacle spots
- **Tool route:** shotlist / Higgsfield plate / Premiere insert
- **Gate influenced:** elite_art_direction, reference_gate(hook), copywriting
- **Do NOT copy:** the specific borrowed brand's lockup or a real campaign's exact staging; borrow the GENRE, not the ad.

## cc_freeze_then_product_pause  (edit/direction)
- **Problem:** Footage is mushy; no clean cut points; product never lands.
- **When to use:** Editing a 30-60s product reel from handheld/awkward action footage.
- **Principle:** Rhythm = awkward action -> product pause -> awkward action -> product pause. Freeze at the END of every action so there is a clean held frame to cut to and to let the product read.
- **Exact move:** Direct talent to freeze 3s after each action (mannequin, 'awkward but expensive'). In edit, cut OUT of motion INTO a 1-2s held product beat. Start record 2s before / hold 3s after every take.
- **Evidence:** operator shoot-doctrine voice memo + shot list
- **Tool route:** on-set direction + Premiere/AE edit route
- **Gate influenced:** reference_gate(pacing, transition_motivation), premiere_edit
- **Do NOT copy:** n/a (this is a method, not a brand asset)

## cc_aggressive_angle_is_the_cover  (design/camera)
- **Problem:** Every frame is eye-level and safe, so none earns the poster slot.
- **When to use:** Choosing the hero/cover frame for a campaign or thumbnail.
- **Principle:** The most AGGRESSIVE angle is the cover. Extremely low, uncomfortably close, or long-lens compression that makes the subject a superhero.
- **Exact move:** Shoot one deliberate extreme: camera on the ground at the tire/feet, OR subject pushed to frame edge uncomfortably close, OR long lens straight-on for fisheye-ish hero pop. That frame becomes thumbnail + deck cover.
- **Evidence:** operator camera-doctrine voice memo
- **Tool route:** camera on set + Higgsfield reframe + thumbnail layout
- **Gate influenced:** reference_gate(shot_variety), elite_art_direction, social_rollout(thumbnail)
- **Do NOT copy:** n/a

## cc_pacing_contrast_band  (edit)
- **Problem:** Edit is monotone: all cuts the same length, so it reads flat or frenetic.
- **When to use:** Any commercial cut; check before export.
- **Principle:** Contrast the pacing band. Fast insert bursts (<1.5s) against held product beats (3-6s). The hero/product frame is always the LONGEST shot in its neighborhood.
- **Exact move:** Target an overall ASL ~2-4s for a punchy spot, but make the product reveal the single longest hold. Use reference_gate to compare your cut's ASL to the reference band.
- **Evidence:** creative_tv_comp_1 pacing.json (mixed band 0.16s-27.4s shows contrast) + craft
- **Tool route:** Premiere edit + os_reference_gate pacing check
- **Gate influenced:** reference_gate(pacing), max_readiness
- **Do NOT copy:** n/a

## cc_earn_attention_spectacle_open  (visual)
- **Problem:** Spots that open soft get skipped in the first 2 seconds.
- **When to use:** Opening frame of any ad meant to stop a scroll.
- **Principle:** Open on a frame that should not be possible or is unexpectedly cinematic, then withhold the product so the viewer stays to resolve the tension.
- **Exact move:** First 1-2s = the single most surprising/expensive image (scale, creature, impossible scene), product enters LATER as the payoff. (Ref: astronaut vs moon-creature, ~46s.)
- **Evidence:** creative_tv_comp_1 shot_008 @46.4s
- **Tool route:** Higgsfield generate + Premiere cold-open
- **Gate influenced:** reference_gate(hook), elite_art_direction
- **Do NOT copy:** the specific creature/scene design from the referenced spot; take the WITHHOLD structure only.

## cc_sound_led_cut  (audio)
- **Problem:** Cuts feel arbitrary; music and picture drift.
- **When to use:** Any music-driven reel (e.g. Alma Love: upbeat 80s).
- **Principle:** Let the track drive the edit. Cut on the beat / downbeat; sync the product reveal and the biggest action to musical accents; use one beat of near-silence before the payoff.
- **Exact move:** Lay the music first, mark beats, place cuts and the product hold on accents; drop a 0.3s silence/duck right before the hero beat (see SOLE seal-strike method).
- **Evidence:** Alma Love brief (upbeat 80s) + SOLE strike-duck method
- **Tool route:** Premiere/ffmpeg audio sync + ElevenLabs SFX
- **Gate influenced:** reference_gate(audio_sync), audio_stack_gate
- **Do NOT copy:** uncleared music; use licensed/owned tracks only.

## cc_branded_title_beat  (design/motion)
- **Problem:** Brand gets lost; or title cards feel like filler.
- **When to use:** Establishing or sign-off beat of a spot/social cut.
- **Principle:** A branded title lockup is a STRUCTURAL beat, not filler: one strong lockup at open or sign-off, in the brand's owned type, held long enough to read once.
- **Exact move:** One title card max per 30s, on-brand type + color, 1.5-2.5s hold; never mid-action. (Ref: compilation title card shot_001 shows the principle; keep it sparse.)
- **Evidence:** creative_tv_comp_1 shot_001 @2.5s
- **Tool route:** AE/HyperFrames title + Figma type system
- **Gate influenced:** reference_gate(typography), figma_design, elite_art_direction
- **Do NOT copy:** the reference's floral/generic template style; use the project's owned type system.
