# Email · Booking confirmation (sent immediately after Stripe deposit lands)

**Trigger:** Stripe deposit invoice paid. Calendly slot confirmed. Phase 1 manual; Phase B+ Zapier auto-fires this email.

**Subject:** `Sniped Reset confirmed · [DATE] at [TIME]`

**Body:**

```
[First name],

Reset confirmed. Date: [DATE], [DAY OF WEEK] · Time: [TIME] · Studio: 2715 S Main St, DTLA.

What is locked in:
- The session: 45 minutes on camera, 90 minutes on location total
- Deliverables: 10-12 fully retouched Heroes + 30-40 color-graded Selects + 60-100 Proofs (the 14-day upgrade window is part of the package)
- Delivery: 5 business days after the shoot · gallery via Pixieset, password-protected
- Balance: $750 due on delivery · invoice will be in your inbox the morning the gallery ships

What I will send next:
- 24 hours before the shoot: wardrobe, parking, mood brief
- The morning of the shoot: studio access details and my direct number
- Day 5: the gallery

What I need from you:
- Reply to confirm you got this
- Block the calendar for [DATE], [TIME] · the 90-minute window
- Bring two wardrobe options (the brief tomorrow will narrow it down)

If anything shifts on your end, reply here. The 48-hour reschedule window starts the moment I send this email.

· BJ
```

---

## Variants

**For Sprint ($750 warm-referral):**
- Time: 30-min session, 60-min on-location total
- Deliverables: 5-8 Heroes + 20-30 Selects (no Proofs upgrade tier)
- Delivery: 3 business days
- Deposit was full $750 (Sprint is paid in full at booking, no balance)

**For Op Kit:**
- Time: half-day session (3-4 hours), multi-look
- Deliverables: 25-35 Heroes + 80-120 Selects + 150+ Proofs
- Delivery: 10 business days
- Balance: 50% on delivery (not $750)
- Add: "We will run a 15-min pre-shoot call within 48 hours to walk the looks and the deck deployment. Calendly: [LINK]"

**For Brand System:**
- Add a project kickoff call (1 hour) within 7 days
- Pre-flight document delivery 14 days before shoot

---

**Notion update at send:**
- [ ] Pipeline DB: Status `Reset Booked` · Estimated value `$1500` · Probability `100%`
- [ ] Clients DB: row created with name, company, role, LinkedIn URL, email
- [ ] Shoots DB: row created with date, type `Reset`, location, status `Scheduled`
