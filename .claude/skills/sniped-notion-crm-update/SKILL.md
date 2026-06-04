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
