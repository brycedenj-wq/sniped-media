---
name: sniped-capture-to-delivery
description: Walk SNIPED's complete capture-to-delivery pipeline · the 5-pass cull + AI mask stack + retouch decision tree + export discipline + Pixieset delivery. Use when user is starting a fresh shoot's post-production, asks about the full pipeline from RAW to delivered gallery, or is training someone on SNIPED's process end to end.
---

# SNIPED Capture-to-Delivery Skill

The complete post-production pipeline runbook. Output target: a delivered Pixieset gallery within the locked SLA, with consistent SNIPED house style across every frame.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/SOP_capture_to_delivery.md` · the master SOP
2. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/lightroom_operating_system.md` · catalog, masks, exports
3. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/preset_library.md` · preset chain
4. `/Users/sniper/Downloads/    SNIPED_OS/06_DELIVERY/SOP_post_delivery.md` · delivery
5. Memory: `[[sniped-visual-direction-luxury-editorial]]` · the locked register

## INVOKE WHEN
- Starting post-production on a freshly shot session
- Onboarding a future retoucher / VA
- Building the pipeline diagram for documentation
- "Walk me through the full process"

## OUTPUT
Sequential walkthrough:
1. **Same-day ingest** (per `sniped-post-shoot-same-day`)
2. **5-pass cull** (Pass 0 auto, Pass 1 manual reject, Pass 2 stars, Pass 3 color labels, Pass 4 hero count check) · 15-25 min target
3. **Hero develop** · 10-step locked order + 5-mask AI stack (per `sniped-luxury-edit`)
4. **Retouch decision tree** · Lightroom only / Evoto / Photoshop routing
5. **Evoto round-trip** (if Q3 yes) · 16-bit TIF, locked Evoto preset, back to LR
6. **Photoshop assembly** (if Q4 yes) · Track B walkthrough or hero-composite-ceiling skill
7. **Export** per the 9 locked export presets
8. **Pixieset gallery build** per `pixieset_config.md`
9. **Delivery** per `sniped-post-delivery`

## REFUSE
- Skipping any of the 5 cull passes
- Editing without the locked-look preset on import
- Hero work over 25 min without escalation decision
- Delivering past SLA without proactive communication


## Inputs
- Freshly ingested shoot folder with RAW files (same-day ingest already complete per sniped-post-shoot-same-day)
- Client name and session type (Reset / Op Kit / Brand System) to drive cull target count and retouch routing
- Locked-look preset confirmed loaded on import in Lightroom catalog
- Retouch routing decisions: Q3 (Evoto?) and Q4 (Photoshop composite?) answers

## Gates
- All 5 cull passes must complete in order (Pass 0-4): skipping any pass is an explicit REFUSE condition
- Locked-look preset must be on import before any hero develop work begins; hero develop capped at 25 min before escalation
- Evoto round-trip uses 16-bit TIF not JPG (JPG destroys gradients per the SOP)
- Export uses the 9 locked export presets only; no ad-hoc export settings
- Delivery past SLA requires proactive client communication before it happens

## Test
- case: BJ just wrapped a Reset session with 180 RAWs in a fresh Lightroom catalog. Expected output: a sequential walkthrough of all 9 pipeline steps from 5-pass cull through Pixieset gallery build, with routing decision flags at Q3 (Evoto skin pass?) and Q4 (Photoshop composite?), and the 9-preset export checklist.
- expected failure: If the shoot folder has not been ingested yet (same-day ingest step not complete), the skill must refuse to begin the pipeline and route to sniped-post-shoot-same-day first. Starting the cull before ingest is confirmed is a gate violation.
