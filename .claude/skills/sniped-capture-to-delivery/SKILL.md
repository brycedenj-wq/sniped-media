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
