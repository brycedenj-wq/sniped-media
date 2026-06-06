# SOLE HOUSE · THE MANIFESTO FILM SCRIPT + VOICE DIRECTION

Status: internal demo build. Nothing here is posted, sent, or published.
Faceless-safe: no operator identity, no client face, no human-trust imagery. The narrator is a disembodied house voice. The only protagonist on screen is the object under the light.
World lock: The Vault Room only. Palette and motifs per WINNER_BRIEF_SOLE.md.
Format target: 60 to 90 seconds. The Seal strikes on the final frame as the sign-off.

This document is the single source the stills, motion, and TTS pipelines all read from. The beat table drives Higgsfield plates and Blender hero-object renders. The tagged block drives ElevenLabs. The casting matrix and audio stack drive the voice and score build.

---

## 0. EXAMPLE CLIENT (invented, for demo only)

**MERIDIAN & HALE** · a regional construction law firm, Charlotte NC. Founded 1998. Twelve attorneys. Roughly $4.2M in annual billings. Competent, profitable, respected by the people who already know them. Their website looks like every other construction-litigation firm in the Southeast: stock gavel imagery, a skyline, the words "experience you can trust." They win cases and lose pitches to firms that are worse but look inevitable. The owner-operator, the managing partner, personally feels invisible in a room of identical letterheads.

**The Sole Claim written for them (the verdict, Hour 0):**

> Meridian & Hale is the only firm that tries construction disputes the way the build was engineered: as a structure, not a story.

**The category they now occupy:** Structural Litigation. Not "construction law." A category they are the sole legitimate occupant of, because they named it.

This claim is the spine of the film. Every beat below is built to make that one sentence feel already true and already expensive.

---

## 1. MANIFESTO VO SCRIPT · TIMED BEATS WITH VAULT ROOM VISUALS

Total runtime target: 78 seconds (inside the 60 to 90 window).
Read tempo: slow, deliberate, roughly 110 words per minute. Silence is part of the script. Do not fill the pauses.
Word count of spoken lines: approximately 140 words. The rest of the runtime is held image and sound.

| Beat | Time | VO line (spoken) | Vault Room visual | Motion / camera |
|---|---|---|---|---|
| 1 · Cold open | 0:00 to 0:07 | (silence) | Total black. A single shaft of hard top-light begins to resolve, striking an empty plinth in a vast dim interior. Polished stone floor catches one reflection. | Hold on black 2s. Light blooms in slow, almost imperceptible push-in. |
| 2 · The indictment | 0:07 to 0:18 | "There is a firm that wins. And a firm that gets remembered. For thirty years, you were the first one." | Camera finds rows of identical archive drawers receding into shadow. One drawer eases open: inside, a stack of identical letterheads, edges lit. | Slow lateral dolly along the drawers. The identical letterheads read as the enemy. |
| 3 · The enemy named | 0:18 to 0:30 | "The market never saw the difference. The market saw a category. And in a category, the cheapest name wins." | A wall of redaction bars slides across the letterheads, blacking them out one by one until the frame is nearly empty. | Redaction bars strike in rhythm with the line. Each bar lands on a beat. |
| 4 · The turn | 0:30 to 0:42 | "So we did not make you better. Better is a category. We took you out of it." | The redacted wall recedes. The lone shaft of light returns to the empty plinth at center. The room quiets. | Push back to reveal the full Vault Room scale. The plinth waits, empty, lit. |
| 5 · The claim | 0:42 to 0:58 | "You are no longer a construction firm that litigates. You are the only firm that tries a dispute the way the build was engineered. A structure. Not a story." | A single brass object rises into the light on the plinth: an engraved nameplate, didone caps, reading STRUCTURAL LITIGATION. Bone-white light, brass glint. | The object rises slowly into the shaft. Camera locks. This is the held hero frame. |
| 6 · The doctrine | 0:58 to 1:08 | "One claim. One category you own. One name your competitor cannot file under." | The nameplate holds. Behind it, the vault-door circular ring geometry resolves in the deep shadow, framing the object. | Static. Let the image be expensive. Minimal drift only. |
| 7 · The sign-off | 1:08 to 1:18 | "Meridian and Hale. The only one." | Hard cut to the Singular Seal: the numeral 1 as a single unbroken vertical stroke inside the vault-door ring. On the final word, the Seal STRIKES into brass with a single percussive hit and settles. Lock to black. | The strike is the last frame. No outro card crawl. The Seal is the period. |

**Direction notes for the read:**
- Beat 2 opens warm, almost a compliment, then turns. The narrator respects the firm before it indicts the market.
- Beat 3 is cold and clinical. This is the enemy. No anger, just verdict.
- Beat 5 is the entire film. Slow down. The two fragments ("A structure." / "Not a story.") are each their own sentence with a full stop of air between them.
- Beat 7 is quiet, not triumphant. The only one is a fact, not a boast. Underplay it.

---

## 2. SAME SCRIPT · ELEVENLABS V3 EMOTIONAL-TAG BLOCK

**KNOWN DOC GAP (verify at generation time):** the exact inline tag vocabulary and bracket syntax for ElevenLabs v3 (eleven_v3) is not locked in this doc and must be confirmed against the live ElevenLabs v3 prompting guide at the moment of generation. v3 audio-tag support, the accepted tag set (for example whether `[pause]`, `[whispers]`, `[exhales]`, emphasis markup are all honored), and tag behavior are model-version dependent and have changed across releases. Before rendering: pull `list_models`, confirm v3 availability on the account, and run one short calibration render to verify each tag actually fires before committing the full read. Treat every tag below as a candidate, not a guarantee. Fallback: if v3 tags are not honored on the account, render on `eleven_multilingual_v2` and carry the performance with Stability / Style sliders plus punctuation and line breaks (see section 3).

Tags used below, pending verification: `[pause]`, `[short pause]`, `[whispers]`, `[softly]`, `[measured]`, `[cold]`, `[resolved]`, and CAPS for emphasis on single words. Ellipses and full stops are also doing real pacing work and should be preserved exactly.

```
[measured] There is a firm that wins. [short pause] And a firm that gets remembered. [pause] For thirty years... you were the first one.

[cold] The market never saw the difference. [short pause] The market saw a category. [pause] And in a category, the CHEAPEST name wins.

[measured] So we did not make you better. [short pause] Better is a category. [pause] We took you OUT of it.

[softly] You are no longer a construction firm that litigates. [short pause] You are the ONLY firm that tries a dispute the way the build was engineered. [pause] A structure. [short pause] Not a story.

[resolved] One claim. [short pause] One category you own. [short pause] One name your competitor cannot file under.

[whispers] Meridian and Hale. [pause] The only one.
```

**Calibration guidance for the engineer:**
- Keep Stability moderate-high so the read stays controlled and does not over-emote. This is restraint, not drama.
- The final `[whispers]` line is the highest-risk tag. If it reads thin or breathy-fake, drop it to `[softly]` or remove the tag and let the lowered punctuation carry it.
- Do not let the model rush the pauses. If v3 collapses the air, insert literal line breaks and short standalone sentences instead of relying on the tag.
- Render at least two takes of beat 5 (the claim) and beat 7 (the sign-off) and select by ear.

---

## 3. VOICE CASTING MATRIX

The brand voice is authority through restraint. Old money, not loud money. The narrator never sells, it pronounces. Think the voice of an institution that has already decided. No hype cadence, no upward inflection, no warmth that asks to be liked.

Casting priority order for the SOLE house default: 1, then 2, then 4.

| # | Archetype | Texture | Why it maps to SOLE | Recommended model | Best use |
|---|---|---|---|---|---|
| 1 | **The Verdict** (default house voice) | Low, dry, masculine-neutral, measured. A judge reading a finding, not a trailer voice. | This is the core of the Sole Claim: a verdict, not a pitch. Maximum gravitas, zero salesmanship. | `eleven_v3` for the emotional-tag performance (the pauses and the turn in beat 2 to 3 need v3 control). Fallback `eleven_multilingual_v2` with high Stability if v3 tags do not fire. | The manifesto film VO, all three tiers. |
| 2 | **The Curator** | Warmer, slower, intimate low-register. A museum after-hours guide, hushed authority. | Leans into the "museum vitrine" and Aman-materiality references. Slightly more human, still faceless and institutional. | `eleven_v3` (the `[whispers]` and `[softly]` tags carry this archetype). | Sovereign-tier extended cut and the world-asset narration where intimacy reads as exclusivity. |
| 3 | **The Banker** | Crisp, precise, cool, transactional restraint. Swiss-private-bank register. | Matches the private-bank lobby reference. Reads as discretion and money. | `eleven_multilingual_v2` (clean, controlled, less expressive by design; you WANT the flatness here). | The Category Brief deck VO and the offer / booking voice where the register is pure discretion. |
| 4 | **The Inheritor** | Younger, quietly confident, understated. New money that learned restraint. | Bridge voice if the client's category skews younger (agency, medspa) and The Verdict reads too funereal. | `eleven_v3` for control, can flex slightly more dynamic. | Alternate house voice for younger-category clients. Not the construction-law demo. |
| 5 | **The Archivist (female register)** | Low, even, unhurried female voice. Authority without softness. | Gives SOLE a non-default option that still holds the restraint lock. Avoids the trap of every brand voice being the same male baritone. | `eleven_v3` for the tag performance; `eleven_multilingual_v2` for the deck. | Alternate house voice. A/B candidate against The Verdict for any client. |

**Model-selection rule of thumb:**
- Use `eleven_v3` wherever the emotional tags and the engineered pauses are load-bearing (the film, the extended cut). v3 is the performance model.
- Use `eleven_multilingual_v2` wherever you want clean, flat, controlled discretion and do not need tag-driven emotion (the deck VO, the booking-flow voice, any utility narration). v2 is the discipline model.
- Confirm both model IDs are live on the account via `list_models` before the build. Pin the exact selected voice ID per archetype once chosen so every tier renders from the same voice (visual-drift discipline applied to audio).

---

## 4. MUSIC + SOUND DIRECTION

**Score mood:** one sustained, low, architectural drone. Not a song, a pressure. Think the sub-bass hum of a vast empty room, a single held cello or synth pad in a minor register, with almost no melodic movement. The score is the air of the Vault Room, not a soundtrack over it. It should feel like the building breathing. Aman-hotel quiet, heist-film tension held just under the surface, never released into a swell.

**Score arc across the 78 seconds:**
- 0:00 to 0:18 · near-silence with a barely-present low drone. Room tone dominates.
- 0:18 to 0:30 (the enemy / redaction beats) · a single low pulse enters, one note per redaction bar, cold and rhythmic. This is the only rhythmic element in the piece.
- 0:30 to 0:42 (the turn) · the pulse drops out. Return to drone. The absence is the drama.
- 0:42 to 1:08 (the claim and doctrine) · the drone lifts a single half-step, a barely-perceptible rise in pitch and warmth as the brass object enters the light. Do not swell. One quiet harmonic shift is the entire emotional payoff.
- 1:08 to 1:18 (sign-off) · everything drops to room tone for one second of near-silence, then the Seal strike, then a long slow decay of the drone into black.

**Sound design moments:**
- **Room tone:** a deep, present, slightly reverberant vault ambience runs under the entire film. Stone, distance, cold air. This is the foundation bed and should never fully disappear until the final decay.
- **Archive drawer (beat 2):** a single low wooden-and-metal slide, slow, weighty. One sound, well-placed.
- **Redaction bars (beat 3):** each bar lands with a short, dry, percussive impact, tight and controlled, like a stamp or a gavel-tap dampened. These hits sync to both the visual and the music pulse.
- **The object rising (beat 5):** a low brass-resonant tone, a single sustained metallic bloom as the nameplate enters the shaft of light. Warm, not bright.
- **THE SEAL STRIKE (beat 7, the signature moment):** the entire audio bed cuts to a held breath of near-silence, then ONE percussive metal-on-metal strike: a die stamping brass. Deep, single, final. Heavy low-end thud fused with a short high metallic ring that decays fast. This is the period at the end of the film and the sonic signature of the SOLE brand. It should be the loudest single moment in the piece and the most restrained, one hit, then the drone decays to black. Design this once, lock it, reuse it as the SOLE audio mark across every film and every tier (the Seal strikes the same way every time, audio-drift discipline).

**Mix discipline:** quiet film. Keep the bed low so the VO sits clearly on top with headroom. The dynamic range is the luxury. Loud is cheap. The only peak in the entire piece is the Seal strike.

---

## 5. AUDIO STACK PLAN

| Layer | Engine | Decision | Notes |
|---|---|---|---|
| **Voice (VO)** | ElevenLabs | LOCKED engine. Render on `eleven_v3` for the film (tag-driven performance), `eleven_multilingual_v2` for deck and utility VO. | Pin one voice ID per archetype. Verify v3 availability and exact tag syntax at generation time (section 2 gap). Render multiple takes of beats 5 and 7, select by ear. Export stems dry (no baked reverb) so the mix can place the voice in the Vault Room acoustically. |
| **Music / score** | Suno vs Udio · **PENDING DECISION** | NOT yet locked. Both are candidates for generating the sustained architectural drone and the single half-step harmonic shift. | Decision criteria to resolve before the build: (a) which engine produces a clean, loopable, low-movement drone without forcing melody or vocals, (b) which gives usable instrumental stems or at least a clean instrumental with no lyrics, (c) license terms for commercial client delivery. Bias: whichever can hold a near-static minor drone and not "write a song." If neither delivers the restraint, fall back to a single sustained pad sourced or synthesized directly and shaped in Premiere / After Effects. The score must serve the room, not perform. |
| **SFX · room tone** | Library or generated | Vault ambience bed. Can be sourced from a licensed ambience library or generated via ElevenLabs `text_to_sound_effects`. | One continuous bed for the full runtime. Deep, reverberant, cold. |
| **SFX · discrete hits** | ElevenLabs `text_to_sound_effects` (candidate) or library | Drawer slide, redaction-bar impacts, object-rise bloom, and the Seal strike. | The Seal strike is the highest-value SFX. Generate or source several candidates, audition, and LOCK one as the permanent SOLE audio mark. Design once, reuse forever. |
| **Assembly / mix** | Premiere + After Effects | All layers assembled, synced to picture, and mixed in the existing operator stack. | VO on top with headroom, score low, room tone underneath, hits synced to picture cuts. Final mix is quiet with one peak (the Seal). Pass the OS max-readiness gate before handoff. |

**Build order:**
1. Lock the Sole Claim copy (done above for the demo). 2. Render VO takes on ElevenLabs, select. 3. Resolve Suno vs Udio, generate the drone. 4. Generate / source SFX, lock the Seal strike. 5. Lay picture from Higgsfield plates + Blender hero-object renders. 6. Mix in Premiere / After Effects to the beat timings in section 1. 7. Max-readiness gate, then timestamped handoff.

**Open items flagged:**
- ElevenLabs v3 exact tag syntax: verify live before render (section 2).
- Suno vs Udio: undecided, resolve before the score build (section 5).
- Seal strike SFX: design once, then lock as the permanent SOLE audio signature.
