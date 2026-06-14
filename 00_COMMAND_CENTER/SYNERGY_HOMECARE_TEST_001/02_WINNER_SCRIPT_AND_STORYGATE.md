# Winner: "The Door" · Script + STORY_GATE Proof

**Length:** 50 seconds (inside the 30 to 60s window, the cleanest length for this arc).
**Aspect:** 9:16 master, conformed to 16:9 for YouTube.
**VO:** one warm voice, spoken TO the daughter (second person). Sparse. Silence and score carry the rest.
**Working title on screen:** none until the button. Let the images breathe.

---

## The 50-second script (shot + sound)

Notation: `[Vx]` visual beat · `(VO)` voiceover · `«...»` on-screen caption (vertical, muted-viewing safe) · `~Ns` target hold.

| t | Visual | Sound / VO | Caption |
|---|---|---|---|
| 0.0 to 3.0 | **[V1]** A phone screen lights the dark. The time reads 2:14 AM. A woman's eyes open, staring at the ceiling. ~3s, slow. | Room tone. A single low piano note. **(VO):** "It's 2 a.m. again." | «2:14 AM» |
| 3.0 to 6.0 | **[V2]** Close on her face, awake, the blue phone light on her cheek. | **(VO):** "And you're still awake. Wondering if you're doing enough." | |
| 6.0 to 13.0 | **[V3]** Carrying montage, fast and tender: a hand sorting a weekly pill organizer at a sink · a missed-call screen · headlights on a dark coastal road, her tired face at the wheel · her asleep at the kitchen table, coat still on. 4 quick beats. | Piano builds gently. **(VO):** "You've been carrying this a long time." Beat. "Alone." | |
| 13.0 to 16.0 | **[V4 · HINGE]** From inside the house: a front door opens and morning light floods in. A caregiver steps into the frame, calm, warm. ~3s, the turn. | The piano lifts into a warmer chord. A door, footsteps. **(VO):** "You don't have to." | |
| 16.0 to 19.0 | **[V5]** The caregiver sets her bag down on a kitchen chair. Unhurried. She belongs here. | Bag down. Soft. | |
| 19.0 to 24.0 | **[V6]** Coffee poured into two mugs, steam in window light. A small radio or record player. | Coffee, a record needle drop. First notes of an old standard. | |
| 24.0 to 31.0 | **[V7 · HERO]** The mother, ~78, hears the song. Her eyes change. She remembers every word. The caregiver watches her, and something moves across the caregiver's face too. Hold long. This is the longest hold in the film. ~7s. | The old song, low and warm under. No VO. Let it land. | «she remembers every word» (fades in/out, optional) |
| 31.0 to 36.0 | **[V8 · HERO INSERT]** A close hand held: the caregiver's hand resting over the mother's on the armrest. ~5s. | Song continues. **(VO, gentle):** "Someone kind. Someone steady. In the home with her now." | |
| 36.0 to 39.0 | **[V9]** A breath of place: Cape Fear morning. River light through a window, or marsh grass and soft water. | Song softens. A distant gull, water. | |
| 39.0 to 45.0 | **[V10 · PAYOFF]** The daughter, somewhere in her own life: parked in her car, or at the edge of her kid's soccer field, phone face-down. For the first time her shoulders drop. She exhales. ~6s. | Music opens up, resolves. **(VO):** "And for the first time in a long time, you can breathe." | |
| 45.0 to 48.5 | **[V11]** The mother and caregiver by the window, calm, together, light on them. | Music settles. **(VO):** "You're not failing. You're carrying a lot." | «You're not failing.» |
| 48.5 to 50.0 | **[V12 · BUTTON]** Clean title on warm near-black: **Synergy HomeCare of Cape Fear.** Sub: "Let us carry it with you." | Final piano note, sustain. | «Synergy HomeCare of Cape Fear / Let us carry it with you.» |

**Total VO word count:** ~70 words across 50 seconds. Deliberately spare. The film is mostly faces and light.

---

## Caregiver cut (same asset bank, recut for recruiting, ~40s)
Same footage, re-VO'd and reordered to open on the kitchen handoff. Spec only; not part of the first test send.

> "Everywhere else, they called it a shift. Clock in. Clock out. Move on. / Here, her name is Eleanor. She likes her coffee light. And this song, this one, she remembers every word. / This isn't a shift. It's the reason you started. / Come do work that means something. Synergy HomeCare of Cape Fear."

---

## STORY_GATE proof (all 9 answered = build is "strong")
Run: `python3 00_COMMAND_CENTER/scripts/os_story_gate.py gate`

1. **Story tension / open loop:** Will the mother be safe, and is the daughter failing her? Opened at 2:14 AM, held until the door opens.
2. **Feeling (first 3s):** dread and guilt, the specific 2 a.m. ache. Named per card `story_emotional_target`.
3. **Desire / status:** relief and absolution for the daughter ("you're not failing"); dignity and meaning for the caregiver ("not a shift, a calling"). Per `psy_status_new_luxury` reframed as emotional status, not luxury status.
4. **Hook:** the lit phone at 2:14 AM and the line "It's 2 a.m. again." Opens the loop in under 3s. Per `story_open_loop_hook`.
5. **Payoff / loop close:** the daughter's exhale (V10) and the button "you're not failing." The 2 a.m. worry resolves into being held. Per `story_loop_closed_ending`.
6. **Character / world:** three consistent people (daughter ~45, mother ~78, caregiver ~40s) in one coastal NC home, consistent light and grade. Per `char_flawed_protagonist` (the daughter's flaw is the guilt of not doing it all herself).
7. **Withhold / reveal:** we withhold relief through the whole carrying montage, reveal it only at the door, and withhold the daughter's exhale until after we have seen the home become safe. Per `psy_withhold_reveal`.
8. **Sequence logic (but/therefore):** mapped explicitly in `01_CONCEPTS`. Never and-then. Worry THEREFORE alone, BUT the door, THEREFORE the home warms, THEREFORE she can breathe.
9. **Source cards used:** `story_open_loop_hook`, `story_but_therefore`, `story_emotional_target`, `psy_withhold_reveal`, `story_loop_closed_ending`, `story_specificity_detail` (pill organizer, 2:14 AM, coffee light, the song), `story_visual_focal_light` (the lit thing wins: phone, then doorway light, then the window), `edit_motivated_only`, `story_proverb_tagline` ("Let us carry it with you"). Sources: Callaway storytelling techniques + SNIPED status/hospitality skills, per `OS_STORY_PSYCHOLOGY_OPERATIONALIZATION_DASHBOARD.md`.

**Brief's own pass test:** does the viewer feel "you're not failing, you're carrying a lot"? The film names it out loud at the payoff, having earned it through the carrying montage. Pass condition for the final cut.
