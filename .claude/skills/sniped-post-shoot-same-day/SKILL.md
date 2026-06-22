---
name: sniped-post-shoot-same-day
description: Walk SNIPED's same-day post-shoot wrap protocol. Use when user just finished a shoot, asks "what do I do now," or wants the ingest + backup + first-pass cull workflow. SD card → SSD → HDD before laptop closes. Same-day discipline prevents data loss and keeps the pipeline moving.
---

# SNIPED Post-Shoot Same-Day Skill

The same-day wrap protocol. Output target: secured backup chain, frames in the pipeline, lights-out by midnight.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/checklist_post_shoot_same_day.md` · the locked checklist
2. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/lightroom_operating_system.md` Section 2 · import discipline
3. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/PRODUCTION_OS.md` Section 1 · backup tiers

## INVOKE WHEN
- Just finished a shoot today
- "What do I do with the files"
- Building the same-day workflow
- "What's my ingest discipline"

## OUTPUT FLOW
1. **Ingest** (15-20 min) · SD card → Hot SSD `/SNIPED_PRODUCTION/YYYY/YYYY-MM-DD_Client_TYPE/10_RAW/`
2. **Backup tier 1** · Hot SSD → Warm HDD (rsync)
3. **Lightroom import** · with locked import preset (`SNIPED · IMPORT DEFAULT`)
4. **Assisted cull pass 0** · let Lightroom AI flag rejects (subject focus + eye focus)
5. **Quick scan** · 5 min review of auto-rejects for false rejects
6. **Notion update** · log the shoot, gallery placeholder, status = "in cull"
7. **Phone BTS** · AirDrop any phone BTS to `/70_BTS/` of the shoot folder
8. **Same-day SLA reminder** · Reset = 5 day delivery, Op Kit = 10 day, Strategic Free = 7 day
9. **Tomorrow** · Pass 1-4 cull per `lightroom_operating_system.md` Section 4

## REFUSE
- Closing laptop without dual backup confirmed
- Editing same-day (don't fall in love with frames hours after shooting · sleep on it)
- Skipping Notion update ("I'll do it tomorrow") · creates state drift


## Inputs
- Shoot wrapped today (trigger condition)
- Client name and shoot type (to construct YYYY-MM-DD_Client_TYPE folder path)
- SD card contents confirmed present on card
- Delivery SLA tier: Reset (5-day), Op Kit (10-day), or Strategic Free (7-day)

## Gates
- Laptop MUST NOT close until both Hot SSD and Warm HDD backups are confirmed
- Editing same-day is REFUSED (sleep-on-it rule)
- Notion update is REQUIRED same day, not deferred to tomorrow
- Lightroom import MUST use the locked preset, not manual settings

## Test
- case: Photographer just wrapped a Reset shoot for client Jordan on 2026-06-21. Expected: ingest path to /SNIPED_PRODUCTION/2026/2026-06-21_Jordan_RESET/10_RAW/, rsync backup command, Lightroom import with SNIPED preset, Notion log entry, delivery deadline set to 2026-06-26.
- expected failure: Photographer asks to do a quick edit on a hero frame before backing up. Skill refuses editing same-day and blocks proceeding until the dual-backup gate is confirmed.
