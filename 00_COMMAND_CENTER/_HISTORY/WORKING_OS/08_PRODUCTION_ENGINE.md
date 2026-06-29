# 08_PRODUCTION_ENGINE · the photo and post pipeline

Single entry for any photo production or editorial task. The pipeline docs and assets live in the frozen source archive `SNIPED_OS/05_PRODUCTION`; the post skills live in the Refinery. This file routes; it does not duplicate the SOPs.

## The pipeline (SNIPED_OS/05_PRODUCTION, frozen source)
- `lightroom_operating_system.md`: the Lightroom OS (Live vs Smart Collections).
- `preset_library.md` and `_preset_backups/SNIPED_LOCKED_LOOK_v3_LUXURY.xmp`: the locked v3 LUXURY grade (A/B test pending; version-lock it).
- `SOP_capture_to_delivery.md`: capture to delivery, with the handoff points.
- `track_b_frame_walkthrough.md`: the Track B Photoshop generative-fill plus Evoto skin-pass editorial walkthrough.

## Skills (invoke via the Skill tool)
- `platform-mastering`: per-surface masters, skin-drift measurement.
- `composite-master-qa`: the 8-gate and 6-axis composite QA.
- `sniped-luxury-edit`: the locked Lightroom develop in v3 LUXURY.
- `sniped-evoto-skin-pass`: the Evoto skin pass.
- Tactical references (Refinery raw mirror): `raw/10_REFERENCE/EVOTO_TACTICAL_EXTRACTION.md`, `raw/10_REFERENCE/UDEMY_LIGHTROOM_EXTRACTION.md`.

## Entry rule
Every photo production or editorial task activates this stack first via `OS_ACTIVATION_INDEX.json`. The subject face, body, and skin are not altered without proof; no "believable" without proof crops and scores.

Updated by: when the preset finalizes after the A/B test (version plus lock-date), when the SOP changes (sync the SNIPED_OS source and the raw mirror), or when a post skill registers. Quarterly audit against SNIPED_OS/05_PRODUCTION.
