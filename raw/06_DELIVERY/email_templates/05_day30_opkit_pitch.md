# Email · Day 30 Operator Kit pitch

**Trigger:** Day 30 after Reset delivery. Calendar reminder Phase 1, Zapier-with-manual-approval-gate Phase C. **Every delivered Reset is pitched, regardless of conversion expectation. The pitch is the practice.**

**Surface:** the same DM thread used for the original Reset booking (LinkedIn or email). Continuity matters.

**Subject:** `One month in · the next move`

**Body:**

```
[First name],

Quick update on my end and a thought.

One month since the Reset shipped. From what I have seen on your LinkedIn, [SPECIFIC OBSERVATION: post that is getting traction / deck deployment they mentioned / press pickup that used the photos / new role announcement / etc.].

The Reset was Tier 1 · single look, single deployment context.

The next move is the Operator Kit. Multi-look, broader visual system, commercial license attached so the photos can run on paid ads + press without a separate license fee per use. Three looks, two locations, half-day session, 25-35 retouched Heroes, 10-day delivery. Pricing for the early Op Kit is $3,000-5,000 depending on scope.

Specifically for you, the gap I would look to close is [SPECIFIC PROTOCOL OR CONTEXT THE RESET DID NOT ADDRESS · examples: "the on-location founder portrait for the Series A press cycle" / "the team-page consistency across your six executives" / "the speaker / podcast / public appearance frame set" / "the website hero + about-page pairing"].

If the timing is right for the next 60 days, here is the Calendly: [OP KIT DISCOVERY LINK · 15 MIN]. If not, the Reset stands; this is just the next rung when it makes sense.

· BJ
```

---

## Specific-observation library (paste the fitting one into [SPECIFIC OBSERVATION])

- "The new LinkedIn header is reading well · the comment volume on your last post jumped"
- "The deck portrait you mentioned ended up in the [PUBLICATION] piece, which is exactly the deployment the Reset was built for"
- "Saw the [funding announcement / role announcement / launch] · the press cycle is the moment Op Kit was designed for"
- "You posted about [their topic] and used one of the Heroes · the coherence between the message and the image is what compounds"

---

## Specific-gap library (paste the fitting one into [SPECIFIC PROTOCOL OR CONTEXT])

- "The on-location founder portrait for the next press cycle, shot at your office or a real working environment"
- "The team-page consistency across your full leadership · same lighting, same color, same register, every face"
- "The speaker / podcast / public-appearance frame set · 3 different looks, deployable across event sponsors"
- "The website hero + about-page pairing · the editorial frame as the visual anchor"
- "The brand campaign frame set · 2-3 commercial-license-attached frames the marketing team can use across paid"

---

## If they reply yes

- Re-run discovery call (Op Kit Discovery is 15 min, not 10).
- Send Op Kit MSA (`/02_CONTRACTS/03_operator_kit_msa.md`) via HelloSign.
- 50% deposit invoice via Stripe.
- Schedule the half-day session.

## If they reply no

- Mark `Closed Lost` on the Op Kit pipeline (the original Reset stays `Reset Delivered`).
- Add `Re-engage 90d` flag on the Pipeline card.
- Reply with: "All good · the Reset stands. I will check back at the 90-day mark in case the timing shifts."

## If they go silent

- Do NOT follow up. The pitch is the practice. Mark `Op Kit Pitched · No response` and add `Re-engage 90d`.

---

**Notion update at send:**
- [ ] Pipeline DB: Status `Op Kit Pitched` · Last touch · Date · Next action `Respond on follow-up OR Re-engage 90d`

**Notion update at conversion:**
- [ ] Pipeline DB: Status `Op Kit Booked` · Estimated value `[OP KIT PRICE]` · Probability `90%` once deposit paid

**Notion update at decline / silence:**
- [ ] Pipeline DB: Op Kit row → `Closed Lost`. Original Reset row stays `Reset Delivered`. Add `Re-engage 90d` tag.
