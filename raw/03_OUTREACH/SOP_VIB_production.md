# SOP · VIB production runbook

**Runbook for producing one VIB end-to-end. Target: 8 minutes per VIB after the master Figma file and reference pool are built (one-time setup).**

This is the operational checklist. The full spec lives in `VIB_figma_spec.md`; the caption library lives in `VIB_caption_library.md`. This SOP is the runbook that ties both into a daily action.

---

## One-time setup (week 1, before any VIB ships)

- [ ] Build the Figma master per `VIB_figma_spec.md`. Single page, named `SNIPED · VIB Master`. All layer architecture and styles in place.
- [ ] Curate the reference pool. Select 12-16 SNIPED frames covering the demographic spread (M/F, 20s-50s, dark/light skin, business/creative wardrobe register, studio/on-location). Save to `/03_OUTREACH/VIB_reference_pool/` with the naming convention from the spec.
- [ ] Ensure the Direction Stack book PDF (one-pager version) is exported and saved at `/08_BOOK/direction_stack_one_pager.pdf` for use in Reply 1 (`Yes, send more info`).

---

## Mon evening · Protected Hour · 3 VIBs in 25 minutes

### Step 1 · Identify three targets (5 min)

- [ ] Open LinkedIn. Search by: city = Los Angeles, role = Founder/CEO/Co-founder/Managing Director, company size = 11-200 employees (mid-stage), recent activity = posted in last 30 days
- [ ] For each candidate, scan: their profile photo (the diagnostic) + their recent post (the trigger) + their company stage (Pre-Seed/Seed/A/B for funding signal)
- [ ] Score the trigger: Tier 1 (3+ trigger conditions met) > Tier 2 (2 conditions) > Tier 3 (1 condition only). Phase 1 sends only Tier 1 and Tier 2.
- [ ] Save 3 LinkedIn URLs + screenshot of their photo + screenshot/text of their trigger post to `/03_OUTREACH/queue/YYYY-MM-DD/`

### Step 2 · Diagnose the protocol (3 min total · 1 min per target)

For each target, study the LinkedIn photo and identify the dominant Direction Stack protocol failure. The dominant protocol is the one most visible at thumbnail size on LinkedIn (which is how the photo is consumed).

- [ ] Run through protocols 01-10 in order. Stop on the first one that's visibly true. That's the diagnostic.
- [ ] Note the deployment context that protocol most affects (LinkedIn / press / deck / podcast).

If you cannot identify a clear single protocol, **skip the target.** Send the queue back to the pool and pick a different prospect. Forcing a diagnostic that doesn't fit is the fastest way to break the not-creepy test.

### Step 3 · Match the reference frame (2 min total)

For each target, pick the SNIPED reference frame from the pool that matches their demographic (gender, approximate age, skin tone, wardrobe register).

- [ ] If no clean demographic match exists in the pool, **skip the target.** Demographic mismatch defeats the contrast and reads as careless.
- [ ] Drag the matched JPG to the Figma right-panel placeholder.

### Step 4 · Assemble the Figma VIB (10 min total · 3-4 min per VIB)

For each target, in Figma:
- [ ] Duplicate the master frame, rename `VIB · [LASTNAME]`
- [ ] Drop the prospect's LinkedIn photo into the left panel placeholder. **Do not edit it. Do not crop beyond fit.** Hold the not-creepy line.
- [ ] Drop the matched reference frame into the right panel placeholder
- [ ] Update both caption blocks with the protocol diagnosed in Step 2 (use `VIB_caption_library.md` Part 1)
- [ ] Update the headline (rotate from the 5 templates in `VIB_figma_spec.md`)
- [ ] Update the footer line
- [ ] Spot check: thumbnail-zoom the frame, confirm the contrast reads in 1 second
- [ ] Export PNG @ 1x to `/03_OUTREACH/sent/YYYY-MM-DD_[LASTNAME].png`

### Step 5 · Log + queue the DM (5 min)

For each target:
- [ ] Create a new Outreach card in Notion: VIB ID · Recipient · Role · Company · LinkedIn URL · Trigger · Protocol named · today's date
- [ ] Pick the right DM script from `VIB_caption_library.md` Part 2 (Script A · cold no trigger · or Script B · cold with trigger · or Script C · Tier 0 trigger event Loom)
- [ ] Personalize the bracketed fields. Total customization should take 60 seconds per DM; if it takes longer, the script needs tightening.
- [ ] Queue the DM to send Tue/Wed/Thu (one per day, never on Friday or weekends). Use LinkedIn's native scheduler if available, or set a calendar reminder.

---

## Tue/Wed/Thu morning · send (2 min per send)

- [ ] 7:30-8:30 AM PT: open LinkedIn DM thread to the target. Paste the customized DM. Attach the VIB PNG.
- [ ] **One image, one message.** No follow-up DM in the same thread today.
- [ ] Update the Outreach card: VIB sent date · check `Loom included` if applicable
- [ ] If a Loom was included (Script C), upload via Loom, set Loom thumbnail to the VIB image, paste the Loom link in the DM body

---

## Day 5 follow-up (only if no reply)

- [ ] Check Outreach card. If Reply = `No reply` AND VIB sent date >= 5 days ago AND prospect is high-value (founder of a Series A+ company OR strong network connection): send Script D (Loom variant) in the same thread.
- [ ] If prospect is not high-value, do nothing. Let the thread sit. Move card to `Re-engage 90d` after Day 10.
- [ ] **Do not send a third message in the same thread.** Sender reputation in their inbox is the long-game asset.

---

## Tracking metric (weekly review · Mon AM)

- VIBs sent (target: 3+)
- Reply rate (target: 25-40% on Tier 1 triggers, 10-20% on Tier 2)
- Positive reply rate (target: 5-10% in Phase 1)
- Discovery calls booked (target: 1+ per week)

If reply rate falls below 10% across 5+ consecutive sends, the issue is the trigger selection, not the script. Re-segment.

If reply rate is healthy but no positive replies, the issue is the script's CTA or the protocol-deployment-context bridge. Test Script B (with trigger) variants.

If positive replies don't convert to discovery calls, the issue is the discovery booking flow (Calendly link friction, scheduling delay). Test reducing friction.
