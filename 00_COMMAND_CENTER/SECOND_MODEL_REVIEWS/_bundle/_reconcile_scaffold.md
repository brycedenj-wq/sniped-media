# SECOND-MODEL RECONCILIATION (Gemini vs evidence)

Rule: a Gemini note becomes a V5 action ONLY if footage/brief/correction backs it. Gemini is a critic, not source of truth.


**Gemini brutal score: 4.2/10**


| # | Gemini claim | Evidence (footage / brief / correction) | Verdict | V5 action |
| --- | --- | --- | --- | --- |
| 1 | **hook_reads**: {"verdict": "weak", "why": "The 'engineered blur' feels digital and cheap. If it doesn't look like a physical thumb on glass by frame 12, the 'Deadpan Summer' aesthetic is dead on arrival."} | _NEEDS-EVIDENCE_ | _pending_ | _pending_ |
| 2 | **speaker_gag_clear**: {"verdict": "yes", "why": "The narrative of 'expensive world malfunctioning' is clear through the KICK, but the pacing makes it feel like a blooper rather than a stylistic choice."} | _NEEDS-EVIDENCE_ | _pending_ | _pending_ |
| 3 | **product_inserts_same_world**: {"verdict": "yes", "why": "The real outdoor lighting on the bikini-on-door shots (T13.7, T21.1) actually matches the hero footage, which is the only thing saving this from looking like a collage."} | _NEEDS-EVIDENCE_ | _pending_ | _pending_ |
| 4 | **wrong_person_bts_plate_issue**: {"found": "yes", "where": "16.0-17.5, 22.0-28.0", "detail": "Unmasked license plates on the CLK500. D94A3308 and D94A3310 are unairable."} | _NEEDS-EVIDENCE_ | _pending_ | _pending_ |
| 5 | **commercial_grade_or_social_rough**: social rough cut | _NEEDS-EVIDENCE_ | _pending_ | _pending_ |
| 6 | **cut/fix**: 4.5-12.0: 7.5 seconds for a speaker gag is an eternity in a 28s spot. It drags the energy into the gutter. -> Aggressively tighten the speaker sequence. Cut the 'wide cross' (T6.1-8.1) by 50%. Make the KICK the punchline, not a slow-motion  | _NEEDS-EVIDENCE_ | _pending_ | _pending_ |
| 7 | **cut/fix**: 16.0-17.5: The 'CLK500' license plate is a legal lawsuit waiting to happen. Your 'static window' blur is amateur-hour trash. -> Track the plate properly in After Effects or use a Higgsfield clean-plate patch. No static windows. | _NEEDS-EVIDENCE_ | _pending_ | _pending_ |
| 8 | **cut/fix**: 18.2-20.9: The lipstick and recline beats (IMG_9534) feel like generic influencer b-roll. They lack the 'deadpan' bite promised in the brief. -> Speed ramp the recline or cut it entirely for a tighter product detail hold at 21.1. | _NEEDS-EVIDENCE_ | _pending_ | _pending_ |
| 9 | **cut/fix**: 25.0-28.0: A 3-second static hold on the logo is a 'skip' invitation. It's lazy. -> Introduce a subtle push-in on the model during the lockup fade to keep the frame alive. | _NEEDS-EVIDENCE_ | _pending_ | _pending_ |
| 10 | **missed**: The Speaker Fidget (T7.7-8.9) should be the most uncomfortable part of the ad; currently, it just looks like she's struggling with a heavy prop. Cut to a tighter crop on her face to sell the 'deadpan' indifference while the object malfuncti | _NEEDS-EVIDENCE_ | _pending_ | _pending_ |
| 11 | **settling?**: The team is rationalizing that the 7.5s speaker gag is 'vibe' when it's actually just 'dead air'. They are also excusing the static plate blur as a 'temp' fix when it's a sign of a broken workflow. | _NEEDS-EVIDENCE_ | _pending_ | _pending_ |

## Gemini V5 edit plan (raw, to be evidence-checked)

- [ ] 1. Fix the Premiere/AME pipeline immediately; stop using FFmpeg for final assembly or you'll never hit professional luma targets.
- [ ] 2. Track and mask all license plates in D94A3308 and D94A3310.
- [ ] 3. Trim the Speaker sequence (4.5-12.0) by at least 2.5 seconds. Prioritize the KICK (T10.2).
- [ ] 4. Replace the static 3-second hold at the end with a 1.5s hold + 1.5s active push-in.
- [ ] 5. Audit the 'lens-wipe' frames at 0.1s intervals to ensure the blur transition doesn't look like a glitch.

## Tool routing (Gemini opinion, advisory)

- **premiere**: avoid - pipeline is currently broken and wasting time.
- **after_effects**: use - mandatory for tracking the license plates and fixing the 'engineered blur' hook.
- **higgsfield**: use - perfect for creating a clean-plate patch for the car trunk to delete the plate entirely.
- **adobe**: avoid - cloud sync is a bottleneck for this grade.
- **ffmpeg**: use - only for quick h.264 dailies, stop using it for the master LUT application.

## Accept/reject rules

- Accept ONLY if a timestamped frame / EDL / brief / director-correction backs the note.
- Reject if Gemini contradicts verified footage (director-label-is-truth-until-disproven).
- Partial if the problem is real but Gemini's fix is wrong; keep problem, replace fix.
- Never let Gemini crown anything final or make a delivery call.
- A lower score from Gemini is a prompt to re-verify, not an automatic truth.