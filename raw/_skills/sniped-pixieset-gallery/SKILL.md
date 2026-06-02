---
name: sniped-pixieset-gallery
description: Build a SNIPED Pixieset client delivery gallery per the locked config. Use when user is about to deliver a shoot, asks about gallery setup, needs Pixieset configuration help, or is troubleshooting gallery delivery. Covers gallery template, cover image selection, naming, password protection, expiry, and the delivery email pairing.
---

# SNIPED Pixieset Gallery Skill

The client gallery build runbook. Output target: a Pixieset gallery that reads premium and delivers cleanly.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/06_DELIVERY/pixieset_config.md` · locked Pixieset template config
2. `/Users/sniper/Downloads/    SNIPED_OS/06_DELIVERY/SOP_post_delivery.md` · delivery sequence
3. `/Users/sniper/Downloads/    SNIPED_OS/06_DELIVERY/email_templates/` · delivery email templates

## INVOKE WHEN
- Building a delivery gallery
- "How do I set up Pixieset for this client"
- Troubleshooting gallery issues
- Reviewing the delivery experience

## OUTPUT
Sequential setup:
1. **Create gallery** named `YYYY-MM-DD_Client_TYPE`
2. **Apply locked template** per `pixieset_config.md`
3. **Cover image** · pick the strongest Hero (the one that makes them want to click in)
4. **Upload Heroes** · JPG export per `SNIPED · Hero · JPG Deliverable` preset
5. **Upload Selects + Proofs** in separate sub-galleries
6. **Password protection** · client's first name + 2-digit shoot count
7. **Expiry** · 14 days from delivery (per `pixieset_config.md`)
8. **Download archive** · enabled for client
9. **Send delivery email** at 9 AM PT using locked template

## REFUSE
- Skipping the locked template
- Sending gallery without password
- Sending without the delivery email
- Letting gallery expire without archiving the bundle to `/60_DELIVERY/` per shoot
