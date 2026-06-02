# SOP · Post-Delivery

**The post-delivery sequence is what turns a one-time Reset into a recurring revenue relationship. Three triggers: Day 0 (delivery + 48-hour upsell), Day 7 (testimonial), Day 30 (Operator Kit pitch).**

The Reset is the entry point. The Op Kit is the business model. The Brand System is the ceiling. Every Reset that ships without a clean post-delivery sequence leaves money and trust on the table.

---

## Day 0 · Delivery + 14-day upgrade window opens

> **v2 OVERRIDE (2026-05-06):** The Day-0 / Day-1 / Day-2 / 48-hour-upsell sequence is superseded by `/01_OFFERS/delivery_architecture_v2.md` Section 5. New mechanic: single Day-0 delivery email with the 3-tier reveal (Heroes · Selects · Proofs) and a 14-day upgrade window. The Day-1 24-hour-mark email and Day-2 last-call email from v1 are retired (the natural gallery expiry replaces them as the time pressure). Day-7 testimonial ask and Day-30 Op Kit pitch from v1 stay unchanged. Read v2 Section 5 for the new delivery email template.

The v1 sequence below is preserved for reference but is NOT the deployed workflow. Use v2.

### v1 (deprecated) · for reference only

This sequence runs immediately after the Pixieset gallery goes live (per `SOP_capture_to_delivery.md` Phase 5).

### Email 1 of 3 · Delivery email (sent at 9:00 AM PT on Day 0)

**Subject:** `Sniped Reset · your gallery is live`

**Body:**
> Hey [First name],
>
> Your gallery is live: [Pixieset link] · password: [pwd]
>
> Twenty retouched final images. High-res download enabled.
>
> Three suggested deployments based on what we shot:
> 1. **LinkedIn header:** [filename or thumbnail reference] (the angled three-quarter; reads strong at the LinkedIn banner crop)
> 2. **Press / podcast cover:** [filename] (the eyes-committed front-on)
> 3. **Deck portrait:** [filename] (the off-axis with negative space for type)
>
> Also in the gallery: 12 additional images that didn't make the contracted twenty but are still strong frames. They're available for $80 each through Friday at [time]. After that the gallery stays live with the contracted twenty for 14 days.
>
> Reply if anything looks off. · BJ

### Pixieset config (already done if `pixieset_config.md` is deployed)
- Gallery expiry: Delivery + 14 days
- Upsell collection visible: Yes, for first 48 hours only
- Upsell pricing: $80/image, $300 for any 5
- Auto-reminder: Pixieset built-in, fires at 24h before upsell window closes

### Notion update (same day)
- [ ] Galleries DB: Pixieset URL · Delivered date · Expiry date · Upsell sequence sent → check `Email 1 (delivery)`
- [ ] Pipeline DB: Status `Reset Delivered` · Last touch · Next action `Send Email 2 in 24h` · Next action date

---

## Day 1 · 24-hour mark · Email 2 of 3 (sent at 9:00 AM PT)

**Subject:** `Re: Sniped Reset · 24 hours left on the additional images`

**Body:**
> Hey [First name],
>
> Quick check-in. The 12 additional images come out of the gallery tomorrow at [time].
>
> If you've already grabbed any of them, ignore this. If not, the gallery is here: [Pixieset link]
>
> Specifically [reference 2 of the strongest of the 12 by what they're useful for]. The low-key eye-direct for [their use case]. The half-turn with the negative space for [their use case].
>
> No pressure. Window closes tomorrow regardless.
>
> · BJ

### Notion update
- [ ] Galleries DB: Upsell sequence sent → check `Email 2 (24h)`

---

## Day 2 · 44-hour mark · Email 3 of 3 · last call (sent 4 hours before window closes)

**Subject:** `Re: Sniped Reset · last 4 hours`

**Body:**
> [First name],
>
> Window closes at [time] today. After that the additional 12 are off the gallery.
>
> Last call: [Pixieset link]
>
> · BJ

**Short. Done. Don't elaborate.**

### Notion update
- [ ] Galleries DB: Upsell sequence sent → check `Email 3 (44h, last call)`

---

## Day 3 · upsell window closes (automated by Pixieset)

- [ ] Galleries DB: Upsell window status auto-flips to `Closed-window` via formula
- [ ] Capture the upsell revenue into the Galleries card
- [ ] Pipeline DB: Cash collected updated to include upsell revenue

**Phase 1 benchmark:** 15-30% of Reset clients buy at least one upsell image, average upsell revenue $150-400 per shoot. Track in `Closed windows · revenue tally` view.

---

## Day 7 · Testimonial ask

The day-7 mark is when the gallery has settled, the client has shared the images, and the social signal (LinkedIn header updated, photo used in a deck, etc.) has happened. This is the warmest possible moment for a testimonial.

### Testimonial DM (sent via LinkedIn or email, whichever they used to book)

**Subject:** `Quick ask · how the photos landed`

**Body:**
> [First name],
>
> Saw the new LinkedIn header · looks great in deployment.
>
> One ask: if the session and the deliverables met the bar, would you be open to a 2-3 sentence testimonial I can use? Specifically about (1) the protocol we corrected and (2) where the new frames are showing up in your business.
>
> Two sentences is enough. I'll handle formatting / attribution however you want · name and company, first name only, anonymized.
>
> Reply here in whatever form is easiest.
>
> · BJ

### Notion update
- [ ] Pipeline DB: Next action `Day 30 Op Kit pitch on [date+30]`
- [ ] When testimonial received: save to `/06_DELIVERY/testimonials/YYYY-MM-DD_[LASTNAME].md` with attribution permissions noted

### What to do with the testimonial
1. Add to the LinkedIn portfolio post (case study format)
2. Add to the Carrd site testimonial section
3. Use as proof point in future VIB DM Reply 2 (`Yes, let's call`) replies
4. Quote in the Day 30 Op Kit pitch deck

---

## Day 30 · The Operator Kit pitch

The most undervalued lever in the SNIPED business model. The Day-30 trigger fires from the Notion view `Day-30 Op Kit pitch trigger`. **Every delivered Reset is pitched, regardless of conversion expectation.** The pitch is the practice; even zero conversions for the first 5 Resets is acceptable. The discipline is the cycle.

### Day 30 message · the pitch (sent via the original DM thread)

**Subject:** `One month in · the next move`

**Body:**
> [First name],
>
> Quick update on my end and a thought.
>
> One month since the Reset shipped. From what I've seen on your LinkedIn, [specific observation: post that's getting traction, deck deployment you mentioned, a press pickup that used the photos]. The Reset was Tier 1 · single look, single deployment context.
>
> The next move is the Operator Kit. Multi-look, broader visual system, commercial license attached so the photos can run on paid ads + press without a separate license fee per use. Three looks, two locations, half-day session, forty retouched, ten-day delivery. Pricing for the early Op Kit is $3,000-5,000 depending on scope.
>
> Specifically for you, the gap I'd look to close is [specific protocol or context that the Reset didn't address · e.g., "the on-location founder portrait for the Series A press cycle" or "the team-page consistency across your six executives"].
>
> If the timing's right for the next 60 days, here's the Calendly: [Op Kit Discovery link, 15 min]. If not, the Reset stands; this is just the next rung when it makes sense.
>
> · BJ

### Notion update
- [ ] Pipeline DB: Status `Op Kit Pitched` · Last touch · Next action: respond on follow-up
- [ ] If they accept: re-run discovery call (Op Kit version is 15 min not 10) · then Op Kit MSA + 50% deposit
- [ ] If they decline: mark `Closed Lost` on the Op Kit pipeline (the original Reset stays `Reset Delivered`); add `Re-engage 90d` flag for next quarter

---

## Day 90 · Reactivation reminder (for Closed Lost · Re-engage 90d cards only)

Quarterly TAM refresh: every Pipeline card with status `Re-engage 90d` is reviewed for whether the prospect's situation has changed (new role, funding, post, event). If yes, restart the VIB sequence with a new trigger. If no, the card sits another 90 days.

This is the Davis Law Group / Tracy mechanism in operation. The 90-day reminder is built in; the work is the trigger discovery on each touch.

---

## Failure modes

| Failure | Cause | Recovery |
|---|---|---|
| Day 0 email opens but no upsell purchase | Either upsell images aren't strong, or copy isn't connecting them to a use case | Test the Day 1 email with a more specific deployment hook for each upsell image |
| No testimonial response on Day 7 | Ask was vague or feels like work for the client | Give them a 2-sentence draft they can edit and send back. "Hate writing testimonials? Here's two sentences you can edit and send back. [draft]." |
| Day 30 pitch goes silent | Either timing is genuinely off, or the Reset experience didn't deliver enough to warrant the upgrade | Don't push. The pitch is the practice. Mark `Closed Lost` on the Op Kit, retain Reset trust, set Re-engage 90d. |
| Op Kit pitch converts at 0% across first 5 Resets | The pitch script needs tightening, OR the early Resets didn't produce results worth scaling | Audit the 5 Reset deliveries for case-study quality. If the work is strong, refine the Day 30 message. If the work is weak, the bottleneck is upstream. |
