# "The Door" v2 · Proof Packet + Re-score (2026-06-08)

Ran the full mandated loop per `OS_AI_CINEMA_PRODUCTION_DOCTRINE.md`: A watch → B/C hostile-review + reconcile → D fix top-2 → E recut → F re-score.

## A. Watch (via /watch, frames-only)
Watched the v1 cut frame-by-frame. Findings: arc holds, anti-gloss look strong, exhale (38s) is real motion and works. CONFIRMED the one true defect: at 22s vs 24s only the camera pushes; Eleanor's face never changes through her own recognition. Frozen at the emotional peak.

## B/C. Hostile review + reconcile
The cut was unchanged since the prior Gemini pass (6/10), and Gemini reviews frames, so a re-run reproduces the same verdict; the watch independently confirmed its #1 finding. Reconciliation (`RECONCILIATION.md`): accepted frozen-Eleanor + scratch-music + minor cliché/locale notes; rejected the misread that the exhale is a still (it is real motion).

## D. Fixes applied (top-2 leverage)
1. **Eleanor recognition regenerated with REAL facial motion** via **Kling 3.0 Pro** (non-Seedance route, since Seedance's NSFW filter false-flagged the shot). Output 1080x1920. Watch QA confirms: neutral (23s) → lips part on a breath (25s) → soft warm almost-smile (27.5s). She now acts. Spliced in (stretched 5.0→6.0s to hold the timeline), graded consistently with the film.
2. **Music: BLOCKED, named gap.** Owned-music route is not executable in-session: Suno is not connected as a tool here, and the ElevenLabs Music API is blocked on this account tier (402, paid plan). The scratch SFX bed remains as a LABELED placeholder, not final.

## E. Recut
`SYNERGY_THE_DOOR_v2_9x16.mp4` (1080x1920, 48.4s) + `..._16x9_youtube.mp4` + `..._9x16_web.mp4`. Only the Eleanor beat changed; everything else identical.

## F. Re-score
- v1 internal: ~7/10 (Gemini hostile 6), ceiling = frozen Eleanor + scratch music.
- **v2 internal: ~8/10.** The #1 defect (frozen climax) is fixed and that beat is now the strongest in the film, at full res.
- **Held below the 9/10 floor by ONE thing: music.** The scratch bed is not final per doctrine point 7. Minor polish (pills/asleep cliché inserts at 6s/10s, generic marsh at 33.7s) is optional, not a blocker.

## Verdict (per doctrine: not "client-ready" unless 9/10 or gap named+accepted)
**v2 is NOT called client-ready.** It is ~8/10, one fix from the floor. The remaining gap is explicitly named: **owned music score.** To close it, either BJ generates the score in Suno (he has it) and drops the file, or ElevenLabs music is upgraded. On receipt of the track I remux and re-score; expected to clear 9/10.

## Next-lift (exact)
1. Owned Suno score (~50s, solo piano → strings lift at the door t=12 → warm resolve at exhale t=39 → sustained final note). Remux. [BLOCKER: needs Suno file or EL upgrade]
2. Optional polish: swap pills (6s) + asleep (10s) for quieter beats; localize/trim marsh (33.7s).
3. Re-run /watch + Gemini on the music-locked cut for the final gate.
