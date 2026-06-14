# AI Scene + Prompt Bank · "The Door"

**Pipeline doctrine:** identity-locked image first, then image-to-video. We lock three faces and one house as references, then animate. This is the only way the same mother, daughter, and caregiver read as the same people across 12 shots. Per `os-face-lock` + the Premium-stack maximization law.

**Tool routing (verified available this session):**
- **Reference / character stills:** Higgsfield Nano Banana Pro (reference-faithful character images) or Soul Character (`higgsfield-soul-id`) for hard identity lock across shots.
- **Cinematic b-roll / animation:** Higgsfield Seedance 2.0 (default video) and Kling 3.0 for the longer emotional holds. Image-to-video from the locked stills.
- **Music we own:** ElevenLabs `compose_music` (the brief wants "music you own"). One piano-led bed, ~50s, plus the in-world "old standard" as a separate composed cue we own (do not use a real copyrighted standard).
- **Voice:** ElevenLabs `text_to_speech`, warm female ~45 to 55, intimate, close-mic, slight breath. Test 2 to 3 voices from the library first.
- **SFX / room tone:** ElevenLabs `text_to_sound_effects` (door, footsteps, coffee pour, needle drop, distant gull, water).
- **Assembly + grade + captions:** Premiere Pro MCP. After Effects MCP only if the title needs motion.

## THE ANTI-GLOSS LAW (applies to every prompt below)
The fastest way to fail this brief is AI sheen. Every still and clip must read as documentary, not advertising. Bake these into every prompt and reject any output that violates them:
- Natural window light only. No studio key, no rim-light glamour, no lens flares.
- Real skin: pores, fine lines, age spots on the 78-year-old, no plastic smoothing, no beauty retouch.
- Age-accurate. The mother is genuinely elderly (~78), not a youthful actor in gray. Hands show age.
- Handheld feel: slight imperfection, natural motion, shallow but not dreamy depth of field.
- Muted, warm, slightly desaturated documentary grade. No teal-orange, no HDR pop, no glossy blacks.
- Modest, lived-in NC home. Real clutter, a worn chair, a fridge with photos. Not a staged showroom.
- No on-the-nose smiling-at-camera. Eyes meet each other, not the lens.
- Grain present. A little softness is truth here.

---

## Character + location bible (lock these FIRST, reuse the reference IDs everywhere)

**MOTHER · "Eleanor", ~78.** Soft white hair, kind tired eyes, cardigan, a wedding ring worn thin. Coastal-NC working-class warmth. Reference still prompt:
> Documentary portrait of a 78-year-old woman named Eleanor, soft white hair, gentle tired eyes, fine wrinkles and age spots, wearing a worn pale-blue cardigan, seated by a sunlit window in a modest coastal North Carolina home, natural soft morning window light, muted warm documentary color, real skin texture, shallow depth of field, shot on 35mm film grain, no makeup, no retouching, candid not posed.

**CAREGIVER · ~40s.** Warm, steady, unglamorous, scrubs or a simple cardigan, a lanyard. Reads as a real person who chose this. Reference still prompt:
> Documentary portrait of a warm caregiver in her early 40s, kind steady face, minimal makeup, simple soft cardigan over plain scrubs, a small lanyard, standing in a modest kitchen with morning light, natural window light, muted warm documentary grade, real skin texture, candid, shot on 35mm film grain, not glossy, not corporate.

**DAUGHTER · ~45.** Exhausted, tender, modern but plain. The 2 a.m. face. Reference still prompt:
> Documentary portrait of a tired 45-year-old woman, no makeup, faint dark circles, plain t-shirt, lying awake in a dark bedroom with only a phone screen lighting her face, blue light on her cheek, raw and real, shallow depth of field, 35mm film grain, candid, not glamorous.

**HOUSE + COAST.** Lock a consistent modest Wilmington-area home interior (warm wood, a worn armchair by a window, a small kitchen) and one coastal plate (Cape Fear river light / marsh grass morning). Generate 2 to 3 establishing stills to keep the world consistent.

---

## Per-shot generation bank

For each: image prompt (still) then the motion note for image-to-video. Durations match the script.

**[V1] Phone in the dark · 3s · insert, no identity risk.**
> Still: A smartphone screen glowing on a dark nightstand at night, the time visible reading 2:14 AM, soft blue glow, deep shadow, intimate, 35mm grain, no people.
> Motion (Seedance, subtle): the screen brightens as if just lit, faint hand entering frame edge. Slow, almost static.

**[V2] Daughter awake · 3s · DAUGHTER lock.**
> Still: use DAUGHTER reference. Close on her face awake in the dark, blue phone light, eyes open staring up, a single worry line between her brows.
> Motion: a slow blink, a small breath. Minimal. Kling 3.0 for the micro-expression.

**[V3] Carrying montage · 4 beats, ~1.5 to 2s each.**
- Pill organizer: > Still: aged hands sorting a weekly plastic pill organizer at a kitchen sink, morning light, real skin, 35mm grain. Motion: hands placing pills, gentle.
- Missed call: > Still: a phone screen showing a missed call from "Mom", held in a tired hand, soft light. Motion: thumb hovers, does not tap.
- Night drive: > Still: DAUGHTER at the wheel of a car on a dark coastal road, dashboard glow, tired, oncoming headlights. Motion: subtle road movement, reflections passing.
- Asleep at table: > Still: DAUGHTER asleep at a kitchen table, coat still on, a cold cup of coffee, dawn light starting. Motion: barely breathing, light slowly warming.

**[V4 · HINGE] The door opens · 3s · CAREGIVER + HOUSE lock.**
> Still: Interior view of a modest home entryway, a front door opening with bright warm morning light flooding in, the silhouette of the CAREGIVER stepping inside, calm and warm. Backlit, documentary.
> Motion (Kling 3.0, the turn): the door swings, light blooms gently, the caregiver steps forward into the warm interior. This is the emotional turn, let the light do the work.

**[V5] Bag set down · 3s · CAREGIVER + HOUSE.**
> Still: the CAREGIVER setting a worn shoulder bag down on a kitchen chair, unhurried, at home. Morning kitchen light.
> Motion: the bag lowers and rests, her hand lingers a second, she exhales lightly.

**[V6] Coffee + record · 5s · HOUSE.**
> Still: two ceramic mugs on a counter, coffee being poured, steam in window light, a small vintage record player or radio nearby, warm modest kitchen.
> Motion: coffee streams into the mug, steam rises, a hand lowers a record needle.

**[V7 · HERO] The song lands · 7s · ELEANOR + CAREGIVER lock. The hold of the film.**
> Still: ELEANOR seated by the window hearing music, her eyes changing as she remembers, the CAREGIVER beside her watching with quiet feeling. Two faces, real emotion, soft morning light, 35mm grain, no one looking at camera.
> Motion (Kling 3.0, slow): Eleanor's expression shifts from blank to recognition, a faint mouthing of a lyric, eyes glisten; the caregiver's small moved smile. Hold long. Reject any take where the emotion looks performed or the skin looks plastic.

**[V8 · HERO INSERT] Hand held · 5s · hands only.**
> Still: a close macro of the CAREGIVER's hand resting over ELEANOR's aged hand on a worn armchair armrest, wedding ring, real skin, soft light.
> Motion: a gentle squeeze, thumbs move slightly. Stillness and warmth.

**[V9] Cape Fear breath · 3s · COAST plate.**
> Still: Cape Fear coastal morning, river light through a window or marsh grass and calm water, soft and quiet, muted warm documentary grade.
> Motion: water shimmer, grass moving in light wind. A held breath of place.

**[V10 · PAYOFF] The daughter exhales · 6s · DAUGHTER lock.**
> Still: DAUGHTER parked in her car in daylight (or at the edge of a youth soccer field), phone face-down on the seat, eyes closed, the moment the weight lifts.
> Motion (Kling 3.0): her shoulders drop, a long slow exhale, the smallest relief crossing her face. This and V7 are the two beats the whole film exists for.

**[V11] Mother + caregiver, together · 3.5s.**
> Still: ELEANOR and the CAREGIVER by the window, calm, side by side, warm light, safe.
> Motion: a quiet shared moment, light settling.

**[V12 · BUTTON] Title card.**
> Build in Premiere/AE on a warm near-black: "Synergy HomeCare of Cape Fear" with sub "Let us carry it with you." Simple serif or clean humanist sans, generous spacing, slow fade up. No logo-compliance pressure per brief.

---

## Audio bank
- **Score (own it):** ElevenLabs compose_music, ~50s, solo piano leading, strings entering at the door (t=13), resolving warm at the exhale (t=39), single sustained note on the button. Brief: "music you own."
- **In-world song (own it):** compose a short, warm, old-standard-flavored cue (gentle, nostalgic, public-domain-feel melody we generate ourselves) for V6 to V8. Do NOT use a real copyrighted standard, even though it would be tempting. We own everything we ship.
- **VO:** ElevenLabs TTS, audition 2 to 3 warm female voices ~45 to 55, intimate close-mic read, then `isolate_audio` if needed for cleanliness.
- **SFX:** door + footsteps, coffee pour, needle drop, distant gull, soft water, room tone bed under the whole film.

## Identity + continuity rule
Before any video generation, approve the 3 character stills and the house/coast plates. Every clip pulls from those locked references (Soul ID or Nano Banana reference). Any clip where a face drifts off the locked identity is rejected and regenerated. Per `os-face-lock`.
