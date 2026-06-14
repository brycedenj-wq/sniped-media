# Synergy "The Door" V8 - Editorial Handoff (Premiere-centered)

Premiere is the editorial authority. Open `SYNERGY_THE_DOOR_V8.prproj` (Premiere 26.2.2) OR import `SYNERGY_THE_DOOR_V8.fcpxml`. Sequence: 1080x1920, 30fps, sequence id 385afc18. Picture runs 0-24.07s; the music clip on A2 is the full 2:45 track - TRIM its tail to ~24s in finish.

## EDL / shot pull list (V1, in order)  [source = graded beat clips in _FILM_BUILD/build/]
| # | TL in | dur | clip | beat | grade note |
|---|---|---|---|---|---|
| 1 | 0.00 | 2.20 | s1n.mp4 | phone 2:14 AM (no-hand insert) | warm push (R-B ~+7), 2am cool-warm |
| 2 | 2.20 | 3.83 | s2n.mp4 | daughter decision (face-only) | warm bedroom (~+13) |
| 3 | 6.03 | 2.70 | s_dl.mp4 | the door / light floods (no person) | warm interior (~+27) |
| 4 | 8.73 | 5.37 | s5.mp4 | Eleanor recognition HERO (longest hold) | warm window (~+20), reference WB |
| 5 | 14.10 | 3.63 | s_cg.mp4 | caregiver reaction (connection, shot/reverse) | warm interior (~+29, can cool ~ -7) |
| 6 | 17.73 | 2.83 | s7.mp4 | Cape Fear breath (coast) | warm (~+24) |
| 7 | 20.57 | 3.50 | s8v3.mp4 | title / CTA card | near-black + cream/gold |
Total 24.07s. Source masters (ungraded) in _FILM_BUILD/shots/SHOT_*.mp4. Grade applied via ffmpeg eq+colorbalance+vignette (recipe per beat above); re-grade in Lumetri for finish.

## Audio cue sheet
- A2 Music: Thinking_of_You_511566838.wav (Adobe Stock LICENSED) @0.00, vol -10dB approx (mix 0.30), fade in 1.5s, fade out from ~22s. Trim tail to 24s.
- A3 VO (ElevenLabs "Sarah - Mature, Reassuring, Confident"):
  - vo1 @0.8  "It's two a.m. again. And you're still awake, wondering if you're doing enough."
  - vo2 @5.6  "You've been carrying this a long time. Alone."
  - vo3 @8.6  "You don't have to."
  - vo4 @10.0 "Someone kind. Someone steady. In the home with her now."
  - vo5 @14.3 "And for the first time in a long time, you can breathe."
  - vo6 @20.8 "You're not failing. You're carrying a lot."

## Marker / beat sheet (7 markers in the sequence)
0.0 Phone hook | 2.2 Daughter decision | 6.03 Door/hinge (light) | 8.73 Eleanor HERO | 14.1 Caregiver reaction | 17.73 Cape Fear breath | 20.57 Title/CTA.

## Transitions / finish notes
- Cuts are hard cuts. RECOMMEND a 6-8 frame cross-dissolve at the bedroom->door boundary (2.20 / 6.03) and into the title (20.57) to soften.
- Title card (s8v3) is a PLACEHOLDER text card -> swap for the real Synergy HomeCare logo + phone/website CTA (AE comp provided / to-build).
- 16:9 master is a true per-beat reframe (SYNERGY_THE_DOOR_v8_16x9_youtube.mp4), not pillarbox.

## HUMAN-FINISHER must-fix to cross ~7 -> 9 (the honest AI ceiling)
1. Real hand-touch insert (the brand's core): shoot a real hand-over-hand plate or hand-double, drop between HERO and caregiver-reaction. AI hands failed every reroll - this is a human/plate job.
2. Face-lock Eleanor across any future two-shot via a trained Soul-ID (AI two-shot identity drifted).
3. Real Synergy logo + CTA on the end card.
