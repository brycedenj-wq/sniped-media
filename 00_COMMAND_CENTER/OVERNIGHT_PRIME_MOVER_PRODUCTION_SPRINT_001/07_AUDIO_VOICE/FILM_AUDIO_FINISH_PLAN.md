# FILM + AUDIO FINISH PLAN , SOLE/SOVRA manifesto (2026-06-06)

> Precise finish plan. Not a rebuild. No paid music/audio generation without explicit go.

## 1. What the 25s teaser v2 already does well
- Holds the world: vault open, vault door, the Blender Seal at the sign-off. On-palette, faceless, restrained.
- Has the brand's two signature audio beats wired: the VO sign-off line + the seal-strike SFX landing on the Seal.
- Title cards carry the thesis ("We do not make you better...", "The only one."). Clean cut, real pacing (25.1s, 1080p), assembled via the proven ffmpeg route.
- Good enough to open a private buyer conversation today.

## 2. What the 60-90s version needs (the gap)
- A spoken VO arc, not just a sign-off line: the full manifesto script (beats 1-7) performed end to end.
- A continuous score + room-tone bed under the whole runtime (currently silent except VO + one SFX).
- More motion coverage: ~6-8 timed beats instead of 2 clips + stills, so the film breathes for 60-90s.
- An owned kinetic-type title system (not centered system-serif cards) , match the Bodoni/Didot deck register.
- The example-client claim built on screen (the nameplate rising into the light, per the script's beat 5).

## 3. Music engine recommendation
- **Recommend: Suno (v4+) for a custom SOLE drone/score**, with **a licensed library track (Musicbed / Artlist) as the zero-AI-risk fallback.** Rationale: the score is a single austere register (low drone, sparse stone-cold tone, one swell into the strike), which Suno does cheaply and fast in instrumental mode; Udio is the fidelity alternative if Suno's master is thin. For a buyer-facing brand asset, a licensed library cue removes any AI-music provenance question at zero creative risk.
- **Decision: DEFER paid generation until go.** ElevenLabs covers VO + SFX (done, free tier); it does not do melody. Pick Suno-vs-library at greenlight, not before.

## 4. ElevenLabs V3 emotional-tag plan
- v3 is confirmed callable via the MCP (model `eleven_v3` accepted inline `[whispers]`/`[pause]` and returned audio). Audible tag-firing is NOT yet ear-verified.
- Plan: (1) pin ONE "Verdict" voice ID (low, dry, judge-reading-a-finding); (2) run a short calibration render of beats 2->3 and 7 and CONFIRM BY EAR that `[pause]`, emphasis, and the turn actually fire; (3) if a tag does not fire, fall back to `eleven_multilingual_v2` with high Stability + punctuation/line-break phrasing (the script already carries both a tagged block and a v2-safe block); (4) render beats 5 and 7 in multiple takes, select by ear, export stems DRY (no baked reverb) so the mix places the voice in the Vault Room acoustically.

## 5. Voice direction
Authority through restraint. Old money, not loud money. The narrator pronounces, never sells. No hype cadence, no upward inflection. Long pauses are load-bearing. One voice across all tiers (audio-drift discipline).

## 6. Sound design map
- Continuous bed: deep, present, slightly reverberant vault room-tone for the full runtime (stone, distance, cold air). Never fully gone until the final decay.
- The Seal strike (signature): full bed cuts to near-silence, then ONE percussive die-stamp (deep low thud + short bright metallic ring, fast decay). Loudest + most restrained moment. SFX already generated (free tier) , reuse as the locked SOLE audio mark.
- Sparse accents only: a low swell into the claim (beat 5), a sub-drop on the strike. No risers, no trailer-cliche hits.

## 7. Render route (proven)
- **Stills/plates:** Higgsfield nano_banana (existing 7 + as needed).
- **Motion beats:** Higgsfield Seedance i2v (proven) for camera moves; ffmpeg ken-burns on existing stills for static beats (zero credits).
- **Seal strike motion:** render in **Blender (0 credits)** , a short rim-glint/strike animation of the FINAL Seal. This REPLACES the ip-flagged Higgsfield seal i2v (avoids the moderation block entirely).
- **Titles/kinetic type:** After Effects authoring (proven) -> `aerender` CLI, OR HyperFrames; match the Bodoni/Didot deck type.
- **Assembly + export:** ffmpeg hybrid (proven). Premiere is read+sequence+FCPXML-proven; FCPXML is the interchange if hand-finishing in Premiere is wanted. AME video render stays blocked -> ffmpeg is the export spine.

## 8. What must be rendered next (ordered)
1. Full VO read (ElevenLabs v3, calibrated) , 0 paid-credit (free tier; ~1.5k chars of the 10k/mo cap).
2. Blender seal-strike animation (sign-off) , 0 credits.
3. 4 new Seedance i2v beats (claim build, nameplate rise, gallery move, redaction) , ~90 credits.
4. Ken-burns beats on existing stills for connective tissue , 0 credits.
5. AE/HyperFrames kinetic title system , 0 credits.
6. Music: Suno custom or licensed cue , deferred to go (paid).
7. ffmpeg assembly + grade -> 60-90s master.

## 9. Estimated credits
- Higgsfield: ~90-115 credits (4 i2v beats + 1-2 re-rolls). Well within the 250 ceiling; current balance 546.5.
- Audio: $0 if VO stays free-tier + SFX done + library/Suno deferred. Suno (if greenlit) ~ $10-30/mo plan, not credits.
- Blender / AE / ffmpeg: 0 credits.
**Total to a finished 60-90s film: ~90-115 Higgsfield credits + a music decision. No spend without explicit go.**
