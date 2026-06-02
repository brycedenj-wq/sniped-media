# Email · Day 90 reactivation reminder

**Trigger:** quarterly. Notion view: every Pipeline card with status `Re-engage 90d` is reviewed for whether the prospect's situation has changed (new role, funding, post, event).

**Logic:** if their situation HAS changed → restart with a NEW trigger (use VIB sequence with new trigger context). If their situation HAS NOT changed → the card sits another 90 days. Do not send a generic check-in.

**Send only when there is a fresh, named trigger.** Otherwise skip.

**Subject options (pick one based on trigger):**
- `Re: [their announcement / post / event] · quick frame`
- `[Their company] [milestone] · the frame I would shoot`
- `Saw [trigger event] · the next visual move`

**Body (with new trigger):**

```
[First name],

Saw [SPECIFIC TRIGGER · e.g., "your Series A announcement," "your move to [Company]," "the [PUBLICATION] piece," "the keynote you just gave at [EVENT]"].

The visual moment that comes with [TRIGGER] is the [DECK PORTRAIT / PRESS COVER / SPEAKER FRAME / TEAM-PAGE FRAME] · specifically [PROTOCOL N · NAME] is the gap that shows up on [SURFACE].

If the timing is right in the next [30-60] days, here is the Calendly: [LINK]. If not, the gallery from [PRIOR RESET DATE · IF APPLICABLE] still stands; this is just the next moment when [PROTOCOL] is the lever.

· BJ
```

---

## If they were a previous Reset client

Add a sentence about deployment of the prior work: "The header you have been running since [PRIOR RESET DATE] is doing well · this is the next-frame question, not a redo."

## If they were a never-converted prospect (cold VIB that did not book)

Use the standard VIB-style approach with the new trigger: "Saw [TRIGGER] and pulled a fresh frame comparison." Attach a new VIB image, not just a follow-up note.

---

**Notion update:**
- [ ] Pipeline DB: Last touch · Trigger used · Reply status (no reply / yes-info / yes-call / declined)
- [ ] If reply yes: move to `Engaged` or `Discovery Booked`
- [ ] If no reply after 7 days: card stays `Re-engage 90d`, sit another 90 days
