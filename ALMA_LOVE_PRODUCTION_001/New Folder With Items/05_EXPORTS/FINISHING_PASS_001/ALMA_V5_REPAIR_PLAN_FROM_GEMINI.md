# ALMA LOVE V5 — REPAIR PLAN (reconciled from Gemini review 001)

Source review: `00_COMMAND_CENTER/SECOND_MODEL_REVIEWS/ALMA_GEMINI_REVIEW_001.{json,md}` (Gemini 4.2/10, "social rough cut").
Rule: a Gemini note becomes a V5 action ONLY if footage / brief / director-correction backs it. Gemini is a hostile critic, not the source of truth. Director-label-is-truth-until-disproven still holds.

## Reconciliation: Gemini said X / footage says Y / V5 action Z

| # | Gemini claim | Footage / brief / correction check | Verdict | V5 action |
|---|---|---|---|---|
| 1 | Speaker gag 4.5-12 is 7.5s of dead air; tighten, cut wide cross ~50%, KICK = punchline | **CONFIRMS.** EDL beats 4-8 = cross 1.6 + wide D94A3297 2.0 + fidget 1.2 + KICK 1.4 + walk-off 1.0 = **7.2s**. Story-arc pacing spec says gag inserts should be **0.8-1.3s**, action 1.5-2s. 7.2s violates the team's own locked pacing. | **ACCEPT** (evidence-backed by EDL + arc) | Trim gag to ~4.5-5.0s: cut D94A3297 wide to ~1.0s, fidget to ~0.9s, land hard on KICK (1.2s) then quick walk-off (0.8s). |
| 2 | Plates on D94A3308 (CLK500) + D94A3310 unmasked; static blur is trash; track properly | **CONFIRMS.** Selects map flags `D94A3308 plate CLK500 blur req` AND `D94A3310 plate lower blur req`. My own V4.2 check: inherited blur is a static window (~t16 only), not tracked. | **ACCEPT — this is THE blocker** | Tracked-mask blur on BOTH D94A3308 and D94A3310 over their full on-screen windows. Re-verify unreadable on fresh proof crops. (route below) |
| 3 | Lipstick/recline (IMG_9534) = generic influencer b-roll, lacks deadpan bite; speed-ramp or cut recline | **PARTIAL.** Brief/arc beat 7 intends "glossy intimate detail" (legit), so do NOT cut lipstick. But two IMG_9534 beats (lipstick 1.4 + recline 1.3 = 2.7s) is one beat of softness in a tight spot. | **PARTIAL** (problem real, full-cut wrong) | Cut the **recline** beat (EDL #14, 1.3s); keep the lipstick close. Recovers time for the held poster. |
| 4 | 3s static logo hold is lazy; add a push-in to keep the frame alive | **DENIES.** Brief + arc mandate the poster **"held long, mannequin-still"**; deadpan stillness IS the brand sell ("the suit survived"). A push-in contradicts the locked creative. | **REJECT** (contradicts brief; Gemini overriding a deliberate decision without evidence) | Keep the held poster. Optional life WITHOUT motion: film-grain + a single shutter/boom SFX on the lockup. No push-in. |
| 5 | Hook "engineered blur feels digital/cheap"; must read like a physical thumb by ~frame 12 | **PARTIAL.** Director map: the wipe is REAL (IMG_9510 @15.4 finger-over-lens). But the engineered blur ramp layered on top could read synthetic. Worth a 0.1s audit. | **PARTIAL** (re-verify, don't assume) | Audit hook at 0.1s; lean on the real finger-wipe frames, reduce synthetic blur so the clear reads as physical glass-wipe. |
| 6 | Speaker fidget should be the most uncomfortable beat; tighter face crop to sell deadpan indifference | **PLAUSIBLE / on-brief.** Brief = poise vs malfunctioning world. A tight deadpan FACE during the struggle sells the core tension. Need to confirm a usable face-close exists (IMG_9514 / D94A3298). | **CONDITIONAL ACCEPT** (verify footage first) | Dense-watch IMG_9514 + D94A3298 for a deadpan face close during fidget; if it exists, insert a 0.6-0.8s tight face beat. If not, log absent (no fabrication). |
| 7 | Premiere avoid (broken), AE use for plate+hook | **CONFIRMS Premiere broken** (QE DOM empty, AME no-start, 2026-06-07 retest). AE-MCP has no import/render, so AE = manual or via handoff. | **ACCEPT (Premiere) / PARTIAL (AE)** | Premiere stays timeline/handoff only. Plate route options below, not auto-AE-MCP. |
| 8 | Higgsfield clean-plate patch to delete the plate | **PLAUSIBLE.** Higgsfield is live; can generate/inpaint a clean plate region. Viable. | **ACCEPT as candidate** | Evaluate Higgsfield inpaint AND Adobe generative-fill for the plate; pick whichever holds across the window. |
| 9 | Adobe avoid (cloud bottleneck) | **DENIES.** Adobe cloud generative-fill / `image_select_subject` is a strong plate-removal/inpaint tool, proven available. "Bottleneck" is not evidence-backed. | **REJECT** | Keep Adobe generative-fill as a plate-removal candidate (#8). |
| 10 | Stop ffmpeg for master LUT / "you'll never hit professional luma" | **DENIES.** `lut3d` applies the identical 33^3 brand cube Premiere's Lumetri would; grade proof shows a correct, clean grade. The luma claim is unfounded. | **REJECT** (tool-purity, not evidence) | Keep ffmpeg + brand LUT for the master while Premiere render is down. |
| 11 | Overall: 4.2/10, "social rough cut" | **PARTIAL.** Agree it is NOT commercial-grade yet, but the gap is concentrated in PACING (gag) + the PLATE, not "everything is trash" (real footage, correct grade, matched inserts, working payoff are genuine strengths Gemini itself credits). | **NOTED, not crowned** | Treat as rough cut. Fix gag + plate + recline + hook; re-score with the finish gate AND a Gemini re-review before any "good enough" call. |

## Accepted V5 actions (evidence-backed, ordered)
1. **Tracked plate blur** on D94A3308 + D94A3310 (full windows). Route: try Adobe generative-fill / Higgsfield clean-plate first (delete the plate), else AE tracked mask; verify unreadable. **[blocker]**
2. **Tighten the speaker gag** from ~7.2s to ~4.5-5.0s (cut D94A3297 wide + fidget, land on KICK). **[biggest craft win]**
3. **Cut the recline beat** (EDL #14); keep lipstick. Reclaim ~1.3s.
4. **Hook audit at 0.1s**; lean on the real finger-wipe, less synthetic blur.
5. **Conditional deadpan face beat** during the fidget — only if a usable face-close exists (verify; no fabrication).
6. Re-master audio -14 LUFS after the re-cut; optional grain + shutter SFX on the poster (no push-in).

## Rejected (not evidence-backed / contradicts locked creative)
- Push-in on the final poster (breaks mannequin-still doctrine).
- "Stop ffmpeg for the master LUT" / luma claim (LUT math identical).
- "Adobe avoid" (Adobe generative-fill is a plate-removal candidate).
- Treating 4.2/10 as gospel — the strengths Gemini itself lists contradict the "trash" framing.

## Net
Gemini's two highest-value, evidence-backed catches: the **7.2s gag is over the team's own pacing spec**, and the **plate is uncertified on two shots**. Both are real and become V5's spine. The rest is tightening (recline, hook) plus one conditional addition (deadpan face). V5 is a surgical re-cut + the tracked plate fix, NOT a teardown.

**DO NOT RENDER V5 until operator go.**
