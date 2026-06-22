---
name: sniped-post-delivery
description: Walk SNIPED's post-delivery client experience SOP. Use when user is about to send a Pixieset gallery, has just delivered, or wants the post-delivery follow-up protocol. Covers the delivery email template, hospitality moments, upsell timing for Op Kit, case study capture, referral ask cadence.
---

# SNIPED Post-Delivery Skill

The post-delivery experience runbook. Output target: a delivered shoot that compounds into testimonial + case study + referral + Op Kit upsell.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/06_DELIVERY/SOP_post_delivery.md` · the locked post-delivery SOP
2. `/Users/sniper/Downloads/    SNIPED_OS/06_DELIVERY/email_templates/` · 9 deploy-ready templates
3. `/Users/sniper/Downloads/    SNIPED_OS/06_DELIVERY/pixieset_config.md` · gallery config
4. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_hospitality_layer.md` · service vs hospitality

## INVOKE WHEN
- Gallery is ready to send
- Client received delivery, what's next
- Op Kit upsell timing question
- Designing the delivery experience
- "How do I get a testimonial / referral"

## OUTPUT FLOW
1. **Send delivery email** at 9 AM PT · use the locked template
2. **Hospitality moment** · 1 unexpected gesture beyond gallery (handwritten note, printed favorite, specific compliment about their work · per `intel_hospitality_layer`)
3. **Day +1** · check Pixieset analytics, did they open the gallery?
4. **Day +3** · soft check-in if no engagement
5. **Day +7** · request feedback / testimonial (the gentle Op Kit upsell touch)
6. **Day +14** · Op Kit pitch if appropriate based on engagement signals
7. **Day +30** · case study capture request (if testimonial received)
8. **Day +60** · referral ask via warm conversation (not generic ask)

## REFUSE
- Sending the gallery without the locked email template
- Skipping the hospitality moment
- Aggressive Op Kit pitch on day 1
- Generic "do you know anyone who needs photos" referral asks · use warm specific asks instead


## Inputs
- Client name + shoot type (to personalize the delivery email from the locked template)
- Pixieset gallery link (confirmed ready to send)
- Shoot date (to anchor the Day +1 through Day +60 cadence timeline)
- Any engagement signal already received (opened gallery, replied, etc.)

## Gates
- Delivery email MUST use the locked template, never a free-form draft
- Hospitality moment is REQUIRED before gallery send (cannot be skipped)
- Op Kit pitch is BLOCKED until Day +14 at earliest (Day +7 is soft touch only)
- Referral ask must be warm and client-specific, never a generic broadcast

## Test
- case: Reset shoot for founder Marcus, Pixieset gallery live, shoot was 2 days ago. Expected: filled locked-template delivery email addressed to Marcus, one specific hospitality gesture, dated follow-up schedule from today through Day +60.
- expected failure: Invoked with no Pixieset gallery link ready. Skill halts and refuses to draft the delivery email because sending without the gallery violates the REFUSE gate.
