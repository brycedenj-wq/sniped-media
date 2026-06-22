---
name: sniped-notion-crm-update
description: Update SNIPED's Notion CRM per the locked schema. Use when a new lead comes in, a shoot completes, a pipeline status changes, or user asks "where do I log this." The CRM has 4 DBs · Shoots, Pipeline, Galleries, Contacts. Each has locked properties + status options.
---

# SNIPED Notion CRM Update Skill

The CRM state-update runbook. Output target: every shoot / lead / gallery / contact represented in Notion within 24 hrs of change.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/04_CRM/notion_crm_schemas.md` · the locked schemas (if exists)
2. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/CURRENT_STATE.md` · current pipeline state

## INVOKE WHEN
- New lead comes in
- Shoot books (date set)
- Shoot completes
- Gallery delivered
- Status changes (replied / cooled / converted / dead)
- "Where do I log this in Notion"

## OUTPUT
Identify the right DB + the property update:
- **Shoots DB** · date, client name, type, status, gallery link
- **Pipeline DB** · lead status, source, last touch, next action, owner
- **Galleries DB** · gallery URL, expiry, downloaded?, testimonial received?
- **Contacts DB** · person record, role, company, cluster tag

Output the specific Notion fields to update with the exact values.

## REFUSE
- Skipping updates ("I'll do it later" creates state drift)
- Manual CRM tools outside Notion (kills single-source-of-truth)
- Updating without the locked schema (causes silent inconsistency)


## Inputs
- The triggering event type: new lead / shoot books / shoot completes / gallery delivered / status change
- Client name, shoot date, type, and any relevant details from the event
- Current pipeline status or the new status to write
- Gallery URL and/or expiry date if this is a gallery-delivery update
- notion_crm_schemas.md read result (locked DB schemas for Shoots, Pipeline, Galleries, Contacts)

## Gates
- Schema gate: locked notion_crm_schemas.md must be read before any field name is named (no guessing property names)
- Single-source gate: update targets Notion only, no parallel manual tools
- No-defer gate: refuses 'I'll do it later' -- every event gets a spec within the same session
- All-fields gate: all locked required properties for the target DB must be present in the output spec before delivery

## Test
- case: Client 'Jordan' just confirmed a headshot shoot for 2026-07-15. Expected output: a Notion Shoots DB spec with date=2026-07-15, client_name=Jordan, type=Headshot, status=Booked; plus a Pipeline DB spec with lead_status=Converted, last_touch=2026-06-21, next_action=Pre-shoot prep.
- expected failure: Operator says 'log this later' or provides no event type. Skill refuses: deferral creates state drift. Blocked also if notion_crm_schemas.md cannot be read (cannot name locked properties without the schema).
