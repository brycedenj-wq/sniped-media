# Post-shoot same-day checklist (run before closing the laptop)

**The 30-45 minute window after the client leaves. Run this list every shoot. Skipping any step costs SLA discipline + backup safety.**

---

## Within 30 minutes of client leaving · in studio or coffee shop

- [ ] Pull cards from camera · into reader (not the laptop's built-in slot · slower)
- [ ] Photo Mechanic Plus auto-import OR Lightroom Classic import to `/SNIPED_PRODUCTION/YYYY/YYYY-MM-DD_LASTNAME_TYPE/10_RAW/`
- [ ] Verify file count matches camera display (sanity check · catches partial transfers)
- [ ] Run mirror to Warm HDD: `sniped_backup ~/SNIPED_PRODUCTION/YYYY/YYYY-MM-DD_LASTNAME_TYPE/`
- [ ] Verify both copies bit-identical (Photo Mechanic verify OR rsync --dry-run --checksum)
- [ ] Eject card · DO NOT FORMAT YET · label "[DATE] · DO NOT FORMAT" until next shoot day
- [ ] AirDrop BTS phone footage to laptop · into `/70_BTS/`
- [ ] Save any handwritten notes / phone notes from the shoot to `/90_NOTES/post_shoot.md`

---

## Within 60 minutes · still same evening

- [ ] Notion update · Shoots DB: status `Captured` · raw frame count noted · location confirmed
- [ ] Notion update · Pipeline DB: status `Reset Captured` · last touch · next action `Cull tomorrow / Day 1`
- [ ] Send post-shoot summary email (3-line confirmation):
  > "[First name] · session was strong. Frame count [N], cull tomorrow, gallery in 5 business days as scheduled. Reply if anything came up that should affect the edit. · BJ"
- [ ] Check the Stripe deposit landed · if not, send polite reminder
- [ ] Calendar: confirm cull block for tomorrow morning is locked

---

## Within 24 hours · the next morning

- [ ] Cull pass 1 · Reject pass · Lightroom (5-8 min)
- [ ] Cull pass 2 · Pick pass (10-15 min)
- [ ] Cull pass 3 · Star pass on Picks (10-15 min)
- [ ] Cull pass 4 · Heroes selection (5 min)
- [ ] Output: smart collection of Hero candidates per shoot type
- [ ] Notion update · Shoots DB: status `Editing` · cull complete date · Hero candidate count

---

## Within 5 business days · delivery SLA

- [ ] Day 1-3: Hero retouch (10-12 Heroes × 12-15 min · 2-3 hr)
- [ ] Day 3-4: Selects (30-40 × 1-2 min · 30-60 min)
- [ ] Day 4: Proofs (60-100 × 30-45 sec · 30-75 min batch · run in background)
- [ ] Day 5: Pixieset upload + delivery email (30 min · per `/06_DELIVERY/email_templates/02_day0_delivery.md`)
- [ ] Day 5: Notion update · Shoots DB: status `Delivered` · gallery URL · Pipeline DB: status `Reset Delivered`

---

## Same-day content layer (parallel to edit work · 45 min)

- [ ] BTS Reel cut from `/70_BTS/` clips (CapCut · ~30-45 min)
- [ ] Reel posted within 24 hours of shoot day (build trust signal · the work is documented in real time)
- [ ] IG Stories · 5-8 frames same day (if not posted live during shoot)
- [ ] Caption draft for the eventual Day-14 case-study LinkedIn post saved to `/80_CONTENT/CAPTIONS.md`

---

## Within 7 days · the trust ratchet

- [ ] Day 7: Testimonial ask (per `/06_DELIVERY/email_templates/03_day7_testimonial.md`)
- [ ] Day 7: Notion update · Pipeline DB: next action `Day-30 Op Kit pitch`

---

## Within 14-21 days · the audience compound

- [ ] Day 14-21: LinkedIn case-study post (with subject permission)
- [ ] Day 14-21: IG Carousel of Hero frames (with subject permission)
- [ ] Day 19: upgrade-window-closing reminder (per template 04 · Pixieset auto-fires the reminder, this is the personalized version)

---

## Within 30 days · the relationship deepen

- [ ] Day 30: Op Kit pitch (per template 05)
- [ ] Day 30: shoot folder archived from Hot SSD → Warm HDD (after upgrade window closes)
- [ ] Day 30: cards from this shoot can finally be formatted (now that delivery, archive, cloud upload are all complete)

---

## Failure modes · same-day risks

| Failure | Cause | Recovery |
|---|---|---|
| Card not transferring | Reader fault, card fault | Try second reader · if still failing, leave card in safe place, do not format · pull frames at home |
| Backup HDD full | Working storage at capacity | Add second 8TB HDD · move oldest year to cold storage |
| Lightroom crashes during cull | Software fault | Save catalog frequently · cull from .xmp sidecar files if needed |
| Forgot to update Notion | Habit failure | This is the friction point that the Saturday Build addresses · install Notion mobile app, log via voice if needed |

---

## The pre-shoot checklist closed when the post-shoot checklist began. The post-shoot checklist closes when:

- Cards are archived (Day 30+)
- Notion is updated through `Reset Delivered`
- Day-7 testimonial ask sent
- BTS Reel posted
- Day-30 Op Kit pitch is on the calendar

**If any of these are open, the loop is incomplete.**
