# Admin / Marketer Inbox

Drop zone for files from the SNIPED admin/marketer (per `/03_OUTREACH/SOP_assistant.md`). 

## Why this folder exists

The admin works with raw data: lead lists, trigger event scans, visual gap drafts, CRM exports. These pass through BJ before they get filed into the right SNIPED_OS folder.

Before this folder existed, the handoff looked like: admin emails BJ → BJ has to figure out where it goes → context lost → file gets misfiled or forgotten.

Now: admin drops here → BJ tells Claude "check the inbox" → Claude reads everything, cross-references against SOP_assistant.md + CRM + current state, files what's actionable into the right canonical folder, surfaces what needs BJ's call.

## How to use

### As the admin
- Drop any file here regardless of format (csv, docx, screenshot, paste-dump in a .txt, anything)
- Name file with context if helpful (`2026-05-12_lead-scan-pearl-network.csv` better than `output.csv`) · not required
- Tell BJ you dropped something

### As BJ
- Open a Claude Code session in this project
- Say "check the admin inbox"
- Claude reads everything, summarizes, proposes routing
- Approve / revise routing
- Claude moves files to canonical folders + updates `CURRENT_STATE.md` or `ACTIVE_THREADS.md` if pipeline state changes

### As Claude
- On "check the admin inbox" instruction: list files, read each, cross-reference against:
  - `/03_OUTREACH/SOP_assistant.md` (the assistant's working manual)
  - `/03_OUTREACH/SOP_discovery_to_close.md` (closing playbook)
  - `/03_OUTREACH/SOP_VIB_production.md` (VIB outreach SOP)
  - `/04_CRM/` (CRM state)
  - Memory: `[[feedback-referral-handling]]` (Pearl network protocol), `[[user-role]]`
- Surface what's actionable, what needs decision, what's noise
- Move files to canonical folders only after BJ approves routing
- After processing, archive raw input here: `/_inbox/admin/_archive/YYYY-MM-DD/`

## What NEVER goes through Claude

Per `/03_OUTREACH/SOP_assistant.md` Section 12 (privacy):
- Financial details (raw revenue, bank, PII beyond what's in CRM)
- Memory layer files
- Strategic-only documents (CANONICAL_TRUTHS, the meta-thesis, locked decisions BJ hasn't shared with assistant)

If admin drops one of those by mistake, flag it and BJ handles offline.
