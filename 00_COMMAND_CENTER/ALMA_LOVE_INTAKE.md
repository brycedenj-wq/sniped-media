# ALMA LOVE , project intake (captured 2026-06-06, shoot day)

> Capture only. Today is a live shoot; this preserves context for the build. Forward-looking, no old-stuff re-litigation. Client brand (Alma Love swimwear), not operator identity.

## Engagement
- Swimwear brand "Alma Love". Operator is shooting + editing a video. **$300 video add-on** (on top of the shoot). Deliverable: a strong **30-45s main reel** (vertical for social + a horizontal cut option).
- Rollout: **Instagrid week-long rollout, starting Sunday** (boom-boom-boom cadence).

## Locked creative notes (from operator)
- **Swimsuit is the main priority** , always clearly visible; everything serves the product.
- Talent: 3 models present, **only 1 in the video**. **Bully short dog** featured. (Keep tasteful/editorial; swimsuit-forward, not explicit.)
- Set: Beverly Hills, middle-of-street, big palm trees, LA / Nipsey vibe. Possible car (Mercedes).
- Sound: **natural sound bed + upbeat 80s music**.
- AI posture: client is ALL-IN on AI (said so directly). Today = collect real footage (Canon clean beauty + iPhone 0.5x weird POV); AI/Higgsfield can extend/compose after. Can go viral angle ("car driving off, item thrown in the air, shot from behind/above, not showing her").

## Shoot doctrine (operator's, now also craft cards)
- Order: safe hero shots first (Canon: front/back swimsuit hero, hood/car still) THEN concept/weird inserts (iPhone: lens-wipe reveal, low aggressive angle, speaker gag, handcuff/palm-up detail, tug-of-war POV, trunk back-reveal, towel struggle, passenger sequence, gas-station final).
- Settings: 4K, 24fps (1/50), 60fps for slow-mo (1/125), low ISO, locked WB, face/eye AF, Neutral profile.
- Record discipline: start 2s before -> action -> hold 3s after. Shoot vertical + horizontal for important shots.

## Edit rhythm (the spine)
**awkward action -> product pause -> awkward action -> product pause.** Freeze at the end of every action. "Awkward but expensive." The product is the longest hold.

## These COMMERCIAL_CRAFT cards apply directly (run the gate on the cut)
- `cc_freeze_then_product_pause` (the core edit rhythm)
- `cc_anything_but_itself` (frame the swimsuit via a borrowed genre: editorial-crime handcuffs, heist, etc.)
- `cc_aggressive_angle_is_the_cover` (low/close/long-lens hero = thumbnail + cover)
- `cc_pacing_contrast_band` (fast inserts vs held product beats; target ASL ~2-4s, product = longest hold)
- `cc_sound_led_cut` (cut to the upbeat-80s beat; duck before the hero beat)
- `cc_branded_title_beat` (one Alma Love lockup, sparse)

## How the OS handles Alma Love going forward
Route = `video_campaign` / `social_rollout` (both now load COMMERCIAL_CRAFT). After the shoot: ingest the footage, build the reel, run `os_reference_gate.py check <reel>` against the cards before delivery. Identity-safe: client brand work, drafts/review before any posting; the Sunday rollout is the client's call.
