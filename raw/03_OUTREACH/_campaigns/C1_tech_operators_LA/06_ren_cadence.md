# Ren · Daily + Weekly Cadence · Campaign 1

Last updated: 2026-05-12

Ren is operations + reply + production lead on Campaign 1. BJ handles strategy + master audio production + complex escalations only.

This doc is the operating playbook. Ren works against this. If contradictions arise between this doc and Slack chatter, this doc wins until updated.

---

## Weekly cadence

### Monday · pull + tag (2-3 hrs)

- **9:00-10:00** · Super Search pull · 1,200-1,500 leads using `03_super_search_filter.md`
- **10:00-12:00** · Lead cleaning + Tier tagging (Tier 1 trigger-rich, Tier 2 standard, Tier 3 edge)
- **12:00** · Upload Tier 1 + Tier 2 to Instantly campaign C1
- **EOD** · Slack update to BJ: lead count by tier, any anomalies, Super Search filter health

### Tuesday-Friday · daily execution (60-90 min/day)

- **9:00 AM** · Unibox check (15 min) · handle replies per `04_reply_scripts.md`
- **10:00 AM** · Loom queue (variable · 30 min per active queued request) · execute per `05_loom_production_workflow.md`
- **1:00 PM** · Unibox check #2 (15 min) · handle replies
- **5:00 PM** · Unibox check #3 (15 min) · handle replies + EOD Slack update

### Saturday · review + report (1 hr)

- Pull Instantly campaign metrics
- Tag any new replies from past 24 hrs
- Slack BJ a 5-line weekly summary:
  1. Emails sent
  2. Open rate (target 40-60%)
  3. Reply rate (target 3-7%)
  4. Audits requested
  5. Calls booked

### Sunday · day off (don't email, don't reply)

Inboxes pause on Sundays per Instantly best practice. Maintains domain health.

---

## Daily decision tree

```
9 AM
   │
   ▼
Check Unibox
   │
   ├─ Positive reply ("yes send it") → Reply 1, queue Loom production
   ├─ Question reply → Reply 2 (explainer)
   ├─ Deflection → Reply 3-6 based on type
   ├─ Hostile → Reply 7 (clean exit, suppress)
   └─ Nothing new → Continue
       │
       ▼
   Check Loom queue
       │
       ├─ Items in queue → Produce per workflow doc
       └─ Empty → Loop back to Unibox in 2 hrs

1 PM
   │
   ▼
Repeat: Unibox check, Loom queue check

5 PM
   │
   ▼
Repeat + EOD Slack update to BJ
```

---

## What Ren does NOT decide

These ALL escalate to BJ via Slack (never decide alone):

1. **Pricing exceptions.** Reset is $1,500. Anyone asking for a discount → BJ.
2. **Calendly-bypass requests.** Anyone trying to skip the discovery call and book the Reset direct → BJ confirms first.
3. **Ambiguous protocol diagnoses.** If Ren can't decide between two protocols, BJ adjudicates in <5 min.
4. **Negative replies that feel weird.** Anything reading like potential complaint, legal threat, journalist, competitor → BJ before responding.
5. **Lead suggestions outside the spec.** If Super Search throws an interesting profile that doesn't match the filter (e.g., a Founder who somehow slipped in), don't decide unilaterally to email them. Slack BJ.
6. **Sequence pause.** If open rate drops below 30% on any inbox, PAUSE that inbox immediately, slack BJ, do NOT keep sending.
7. **Higgsfield-generated visual that looks AI-tell.** If the generated reference has obvious artifacts (weird eyes, extra fingers, demographic mismatch), DON'T SEND. Re-generate or escalate.

---

## What Ren owns fully

1. **Super Search execution.** Pull, clean, tag, upload. Weekly.
2. **Unibox reply handling.** Replies 1-7 are templated · use them. Free to lightly adapt voice but don't rewrite.
3. **Loom production.** Per `05_loom_production_workflow.md`. Quality check before send.
4. **Calendly link maintenance.** Verify the link works monthly.
5. **Status reporting.** Daily Slack EOD + weekly Saturday summary.
6. **CRM updates.** Tag prospect status after each touchpoint.

---

## What BJ owns

1. **Strategic decisions.** ICP shifts, offer shifts, campaign launches/pauses.
2. **Master audio recording.** 10 protocol audio scripts, once, then permanent.
3. **Discovery calls.** When a Loom converts to a call, BJ runs the call.
4. **Reset shoots.** Production execution at the studio.
5. **Op Kit upsell.** Week 2 post-shoot pitch if conditions are right.
6. **Copy iteration.** Email 1 / 2 / 3 rewrites based on Ren's data report.
7. **Slack escalations.** Within 30 min during business hours.

---

## Tools Ren uses

| Tool | Purpose | Access |
|---|---|---|
| Instantly.ai | Send + Unibox + Super Search | Ren's login (shared via BJ) |
| Higgsfield Soul | Reference visual generation | Ren's account (BJ funds) |
| Descript | Loom assembly + light editing | Ren's account |
| Calendly | Booking link | BJ-owned, Ren references |
| Slack | Daily communication with BJ | Shared workspace |
| Google Drive | Loom file storage backup | SNIPED Media folder |
| CRM (Notion or whatever's live) | Lead tracking + tier tagging | SNIPED workspace |

---

## What Ren reports to BJ

### Daily (EOD Slack, 1 message)

```
C1 status:
- Sent today: NNN
- Replies today: NN (positive: NN, deflect: NN, hostile: NN)
- Looms produced today: NN
- Looms in queue: NN
- Anything weird: (1-2 lines or "nothing")
```

### Weekly (Saturday Slack summary)

```
C1 week of [date]:
- Emails sent: NNN
- Open rate: XX% (target 40-60%)
- Reply rate: X.X% (target 3-7%)
- Audits requested: NN
- Calls booked: NN
- Reset booked: N
- Top issue worth flagging: (1-2 lines)
- Top win worth celebrating: (1-2 lines)
```

### Monthly (1st of month Slack summary)

```
C1 month of [month]:
- Emails sent total
- Reply rate vs prior month
- Audit-to-call conversion
- Call-to-Reset conversion
- Revenue from C1
- 3 things to change / test next month
```

---

## Pay structure (TBD · BJ owns this)

Open question for BJ to decide:
- Hourly?
- Fixed per Loom produced?
- Fixed per qualified call booked?
- Commission on Reset bookings?

My recommendation: **Hybrid · base + per-Loom + Reset-booking bonus.**
- Base: small hourly for the lead-pull + Unibox handling (~15 hrs/week × $X)
- Per Loom produced: $Y per delivered Loom (~$15-25 range)
- Reset bonus: 10% commission on any Reset that comes through C1 cold email (~$150 per close)

This aligns Ren's incentive with what we actually want: high reply handling speed, high Loom quality, calls that close.

---

## Failure modes to watch

1. **Ren burns out on Loom production at volume.** Symptom: Loom queue grows, Looms delivered slower than 48 hrs. Fix: throttle email volume OR escalate the production workflow.
2. **Ren skips quality checks.** Symptom: BJ catches a Loom with AI artifacts in a delivered email. Fix: re-emphasize the quality checklist, possibly require BJ approval on first 10 Looms.
3. **Inbox open rate drops below 30%.** Symptom: deliverability issue. Fix: pause that inbox, audit warmup, may need to rotate domains.
4. **Reply rate above 10%.** Symptom: things going TOO well, possibly indicates a domain about to get marked spam. Fix: throttle volume on that domain, audit content.
5. **Ren makes a pricing exception without escalating.** Symptom: prospect on a Reset call says "Ren said you'd do it for $X." Fix: immediate retraining on the escalation rule.

---

## When to revise this doc

- After 4 weeks of running C1
- After Ren's first 50 Looms delivered
- If Reset booking rate is significantly above or below target
- If Ren raises a workflow friction that's not solvable in the current spec

BJ owns the doc. Ren proposes changes via Slack. Doc lives in SNIPED_OS · single source of truth, version-controlled.
