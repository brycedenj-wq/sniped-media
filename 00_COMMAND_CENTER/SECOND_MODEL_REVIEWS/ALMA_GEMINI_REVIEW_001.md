# ALMA LOVE — Gemini Second-Model Review 001

- **Subject:** `ALMA_LOVE_COMMERCIAL_V4_2_HERO.mp4` (28.0s)
- **Reviewer:** Gemini CLI 0.45.2, model `gemini-3-flash-preview`, read-only (`gemini -p ... --output-format json`)
- **Gemini tool calls / edits:** 0 (clean, verified in stats)
- **Date:** 2026-06-07
- **Raw:** `ALMA_GEMINI_REVIEW_001.json` · **Bundle:** `_bundle/ALMA_REVIEW_BUNDLE_001.md` + `_bundle/CONTACT_SHEET.jpg`

## Brutal score: 4.2 / 10 — verdict "social rough cut"

## Keep
- **0.0-1.6 hook** — the one thing that feels intentional/high-end.
- **~14-16 trunk reveal (D94A3308)** — strongest product-to-environment integration; actually reads "Deadpan Luxury."
- **~22-25 seated poster (D94A3310)** — solid hero frame "before you drown it in that cream lockup."

## Cut / fix
- **4.5-12.0 speaker gag (7.5s)** — "an eternity in a 28s spot... drags the energy into the gutter." Tighten hard; cut the wide cross ~50%; make the KICK the punchline.
- **16.0-17.5 plate** — "CLK500 license plate is a lawsuit waiting to happen. Your static-window blur is amateur-hour trash." Track it in AE or Higgsfield clean-plate patch.
- **18.2-20.9 lipstick/recline (IMG_9534)** — "generic influencer b-roll... lacks the deadpan bite." Speed-ramp or cut the recline.
- **25.0-28.0 logo hold (3s static)** — "a skip invitation, lazy." Add a subtle push-in.

## Answers
- **Hook reads?** WEAK — "engineered blur feels digital and cheap"; must read like a physical thumb on glass by ~frame 12.
- **Speaker gag clear?** YES as narrative, but pacing makes it feel like a blooper not a stylistic choice.
- **Product inserts same world?** YES — real outdoor lighting matches; "the only thing saving this from looking like a collage."
- **Wrong-person / BTS / plate?** YES — unmasked plates on D94A3308 and D94A3310, "unairable."
- **Commercial-grade or social rough?** SOCIAL ROUGH CUT.

## What the team is likely rationalizing (Gemini)
"The 7.5s speaker gag is 'vibe' when it's actually dead air. Excusing the static plate blur as 'temp' when it's a sign of a broken workflow."

## Gemini V5 plan (raw, advisory — evidence-checked in `ALMA_V5_REPAIR_PLAN_FROM_GEMINI.md`)
1. Fix Premiere/AME; stop using ffmpeg for final assembly.
2. Track + mask all plates (D94A3308, D94A3310).
3. Trim the speaker sequence by >=2.5s; prioritize the KICK.
4. Replace the static end hold with 1.5s hold + 1.5s push-in.
5. Audit the lens-wipe at 0.1s intervals so the blur isn't a glitch.

## Gemini tool routing (advisory)
Premiere avoid (broken) · After Effects use (plate track + hook) · Higgsfield use (clean-plate patch) · Adobe avoid (cloud bottleneck) · ffmpeg use only for dailies, not master LUT.
