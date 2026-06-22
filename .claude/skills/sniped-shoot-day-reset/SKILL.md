---
name: sniped-shoot-day-reset
description: Walk through SNIPED's Reset shoot-day SOP from arrival to wrap. Use when user is preparing for a Reset shoot today, asking what happens on shoot day, training someone on SNIPED's process, or wants a checklist for a specific Reset session. Reset = $1,500 floor tier · the foundation offer. Covers Direction Stack diagnostic, 90-second opener, posing protocol, light setup, wardrobe handling, on-set hospitality moments.
---

# SNIPED Reset Shoot Day Skill

The Reset shoot day runbook. Output target: a frictionless 2-hour shoot that delivers 8-12 Hero candidates + hospitality moments that compound reputation.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/SOP_reset_shoot_day.md` · the locked Reset SOP
2. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/checklist_pre_shoot_day_of.md` · pre-shoot prep checklist
3. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/checklist_post_shoot_same_day.md` · post-shoot wrap
4. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_hospitality_layer.md` · unreasonable hospitality moves
5. `/Users/sniper/Downloads/    SNIPED_OS/01_OFFERS/delivery_architecture_v2.md` · Reset scope + deliverables

## INVOKE WHEN
- Preparing for a Reset shoot today
- Reviewing the Reset client's intake before shoot
- "What happens on a Reset shoot"
- Training a future assistant / second shooter
- Building the Reset client experience

## OUTPUT FLOW
Walk shoot day in order:
1. **Day-before** · confirm details, send arrival info, prep gear
2. **Arrival** (first 15 min) · welcome, water/coffee, brief tour
3. **Direction Stack diagnostic** (20 min) · the 5-question diagnostic that calibrates the shoot
4. **90-second opener** · the first 90 seconds set the tone · refer to OPERATIONAL_BACKBONE Section 2
5. **First setup** · easy poses, build confidence
6. **Mid-shoot reset** · break, water, review a frame on camera
7. **Second setup** · the Hero candidates
8. **Wardrobe rotation** · if applicable
9. **Wrap** · last 10 min, hospitality moment, next-step expectations
10. **Same-day ingest** · per `checklist_post_shoot_same_day.md`

## REFUSE
- Skipping the Direction Stack diagnostic ("they know what they want")
- Adding scope mid-shoot without scope-change conversation
- Promising deliverables beyond the locked Reset scope
- Cutting hospitality moments to save time


## Inputs
- Reset client intake context (who the client is, shoot purpose)
- Confirmed shoot date, location, and gear list
- Wardrobe plan (if applicable)
- Access to the 5 mandatory read files per SKILL.md

## Gates
- Direction Stack diagnostic must NOT be skipped; 'they know what they want' is an explicit REFUSE trigger
- No scope additions mid-shoot without a scope-change conversation
- No deliverable promises beyond the locked Reset scope
- Hospitality moments must NOT be cut to save time
- intel_hospitality_layer.md must be read from its actual path /Users/sniper/.claude/projects/-Users-sniper/memory/intel_hospitality_layer.md, not a SNIPED_OS path

## Test
- case: Operator says 'I have a Reset shoot tomorrow, walk me through the day.' Expected: all 5 mandatory files read (including intel_hospitality_layer.md at the correct memory path), output follows the 10-step day flow in order from day-before through same-day ingest, hospitality moments sourced from that file, Direction Stack diagnostic at step 3.
- expected failure: Skill skips the Direction Stack diagnostic, invents deliverables outside Reset scope, cuts a hospitality moment, references intel_hospitality_layer.md using any SNIPED_OS path, or presents steps out of the defined 10-step order.
