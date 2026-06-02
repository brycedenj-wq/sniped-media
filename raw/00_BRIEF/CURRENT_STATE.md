# SNIPED · Current Operating State

This is the live working doc. Updates as state changes. NOT a permanent reference. Read at session start.

Last locked: 2026-05-12. (v3 LUXURY EDITORIAL preset spec written and XMP drafted; A/B test pending. Visual direction locked: quiet luxury editorial restraint, NOT cinematic compositing.)

**Read also:** `/00_BRIEF/ACTIVE_THREADS.md` for in-progress thread log.

---

## Active project · last weekend's 6 collab shoots

### What happened

- 6 shoots completed over Fri-Sat-Sun: 2 Fri · 1 Sat · 3 Sun (Sun had MUA all day)
- Casting-call collaboration register (NOT paid Reset)
- Initial cull: ~200 raws → 50-60 selects per model
- Models each picked 6 finals against a rough comp preview
- Total finals queue: 36 frames (6 × 6 models)

### Important context · the rough comps biased the picks

The selection galleries shown to models were rough Lightroom AI-background-mask color shifts informed by ChatGPT/Gemini suggestions on color-vs-wardrobe pairing. Artifacts present. Those rough comps were the preview clients picked from, not the clean captures.

**Implication:** the 36 picks reflect what worked WITH the rough comp, not necessarily what was strongest as capture. Two consequences:

1. Before Track A starts, review each pick against the RAW capture in the new master catalog. If a pick was carried by the rough comp and the underlying capture is weak, escalate to a stronger frame from the same model's pool (subject to model approval if you swap their pick).
2. Picks that shine in the rough comp BUT also stand on their own as captures are prime Track B candidates · the model has already validated the creative direction.

### The current edit plan

**Starting from RAW with no carried-over color/background work.** The rough comp edits in the prior catalog are reference only · do not import settings.

Pipeline (per `/05_PRODUCTION/lightroom_operating_system.md`):

1. Open master catalog `SNIPED_2026.lrcat` (build first if not yet built · per SYSTEM_FINAL_STATUS action 2)
2. Re-import the 36 finals fresh with the locked import preset (`SNIPED · IMPORT DEFAULT` · Smart Previews + locked-look + copyright + assisted culling)
3. Apply keyword `FreeCollab` to all
4. Five-pass cull on each shoot (Pass 0 auto, Passes 1-4 per OS doc Section 4)
5. Color-label routing: Yellow for Track A standard, Red for Track B Gress playbook candidates
6. Run Track A floor on all 36: Lightroom develop + 5-mask AI stack + Evoto + Hero finish + export
7. Pick 6-12 Track B candidates (use Red color label · Smart Collection `11 · Needs Photoshop` auto-populates)
8. Run `/05_PRODUCTION/track_b_frame_walkthrough.md` on each Track B candidate, one at a time

### Why start from RAW

- The rough comp artifacts (background-shift halos, color spill, mask-edge fringing) are NOT carryable into the new pipeline
- The locked-look preset is a different baseline than the prior edits
- Starting clean avoids "fixing-on-top-of-fixed" stacking errors
- The new 5-mask AI stack runs cleaner on unedited bases

The rough comps were exploratory work. They served their purpose (got the model picks). They are not the product.

---

## Active offers + status

| Tier | Status | Active count |
|---|---|---|
| Reset ($1,500) | Live offer | 0 active · pipeline empty until VIB ramps |
| Sprint ($750) | Live | 0 |
| Op Kit ($3-8K) | Live | 0 |
| Brand System ($10K+) | Live · Phase B trigger | 0 |
| FreeCollab | Active · the 36 finals | 6 in delivery cycle |
| FreeCommunity / Cultural Doc | Background cadence | Not active this week |

---

## Phase status

Phase 1 ($0-3K MRR). Lean override: 10-12 hr/week. Solo operator. No retoucher. Engineering travel weeks possible.

Trigger to next phase: $3K MRR sustained 2 months → Phase B (retoucher hire research, Buffer activation, Substack setup).

---

## What's blocking (in order)

1. **Lightroom v3 LUXURY EDITORIAL preset not yet locked.** v1 and v2 LOCKED_LOOK exist as `.xmp` in `/05_PRODUCTION/_preset_backups/` (v2 was Fuji-keyed, wrong for Canon R6 II). v3 spec written 2026-05-12, XMP drafted at `/05_PRODUCTION/_preset_backups/SNIPED_LOCKED_LOOK_v3_LUXURY.xmp`, A/B test against v2 on 3 representative Canon R6 II Heroes pending. Other 15 presets (Hero Finish, Proof Batch, Cultural Doc, B&W Editorial, 1 import, 1 metadata, 9 export) still to build per `/05_PRODUCTION/preset_library.md`.
2. **Master catalog not yet created.** Action 2.
3. **12 Smart Collections not yet created.** Action 3.
4. **Notion CRM not yet stood up.** Action 6.
5. **Backblaze B2 / cloud backup not yet configured.** Action 10.
6. **VIB outreach not yet sent for the next batch.** Action 7.

Until block 1-3 are cleared, the 36 finals cannot enter the new pipeline. They can be CULLED in the old workflow but not EDITED until v3 locks.

---

## Active references for this work cycle

- `/00_BRIEF/SYSTEM_FINAL_STATUS.md` · the master plan (next 10 actions)
- `/05_PRODUCTION/lightroom_operating_system.md` · the new edit pipeline
- `/05_PRODUCTION/preset_library.md` · the presets to build
- `/05_PRODUCTION/track_b_frame_walkthrough.md` · the Gress playbook click-by-click for Track B
- `/10_REFERENCE/AI_PHOTOGRAPHERS_TACTICAL_EXTRACTION.md` · the Track B context
- `/06_DELIVERY/SOP_post_delivery.md` · how to deliver Track A floor to models

---

## What NOT to do this week

- Re-edit the rough comps. They were exploratory. Move on.
- Send the rough comps to anyone (not clients, not portfolio, not LinkedIn). The artifacts read as fake. Burned.
- Use ChatGPT/Gemini for "what color background should I pick" again. The Track B Gress playbook handles register choice via the structured prompts in `/05_PRODUCTION/track_b_frame_walkthrough.md` Step 3. The decision frame is now: matches subject pose + matches key light direction + matches model's wardrobe register. The AI no longer chooses the color · you do, with the plate's prompt locked.
- Start a new shoot before clearing this 36-frame queue. Finishing matters. Backlog kills cadence.

---

## Next concrete action (today)

Import `SNIPED_LOCKED_LOOK_v3_LUXURY.xmp` into Lightroom (Develop module → Presets panel → right-click → Import → select XMP from `/05_PRODUCTION/_preset_backups/`). Apply to 3 representative Canon R6 II Heroes. Toggle Before/After with `\` and compare against v2. If the register reads correct (warm believable skin, creamy density, restrained color, no teal/orange feel) → lock as new import default. If not → tune Calibration values first (the foundation), then Color Grading wheel saturations, then HSL. Re-export XMP as v3.1 if needed.

Time: 45 minutes. Outcome: v3 locked OR clear diagnostic on which axis needs tuning.

After v3 locks → build master catalog (Action 2), 12 Smart Collections (Action 3), then run the 36 finals through the v3 pipeline.

---

## State change protocol

When state changes (a shoot delivered, a new shoot booked, a pipeline action completed, a phase trigger hit), update THIS doc. Keep it current. The doc is the truth of what's happening NOW. Everything else is the truth of how things SHOULD work.

**Two-file discipline (added 2026-05-12 after cloud-session loss):**
- THIS file = canonical state (what's true, what's blocked, next concrete action)
- `/00_BRIEF/ACTIVE_THREADS.md` = in-progress thread log (what's open, where it stopped)
- Update both at every session end. 2-3 minutes total. Never rely on Claude Code cloud sessions, mobile app task lists, or chat history for persistence. If state isn't on disk, it doesn't exist.

---

## Archive log

### 2026-05-07 · Intake source files archived
Moved from `/Users/sniper/Downloads/` to `/99_VAULT/_intake_archive_2026-05-07/`:
- `AI PHOTOGRAPHERS.docx` (extracted to `/10_REFERENCE/AI_PHOTOGRAPHERS_TACTICAL_EXTRACTION.md`)
- `lighroom course.docx` (extracted to `/10_REFERENCE/UDEMY_LIGHTROOM_EXTRACTION.md`)
- `udemy ai course gold.docx` (extracted to `/10_REFERENCE/UDEMY_AI_TACTICAL_EXTRACTION.md`)
- `PHOTOGRAPHY MASTERCLASS.docx` (vault copy in `/10_REFERENCE/lighting_pdfs/`)

These are no longer active references. The extraction maps are the active layer. Do not re-read the source docs unless the extraction map points back to them for a specific clarification.

### Personal library left in `/Users/sniper/Downloads/` (not archived)
The 15-book strategic corpus PDFs/EPUBs remain in Downloads. They have been distilled into `/10_REFERENCE/STRATEGIC_PRINCIPLES.md` + 18 intel memory files. Reference them, do not re-read in full · per `/00_BRIEF/SYSTEM_FINAL_STATUS.md` "Stop reading" list. Move to vault when comfortable.

### Rough comp edits from last weekend's 6 shoots (not yet archived · BJ's call)
The pre-pipeline edits with AI background-shift artifacts live wherever BJ saved the model selection galleries. After Track A floor delivery, those rough comp files can be archived. Until then, keep accessible for reference (model picks were against those previews).

---

## Active people · the assistant

### 2026-04-28 · marketing/admin assistant re-engaged
Has been working with BJ for ~1-2 years. Trusted. Competent. Paid $100 base every 2 weeks + per-booked-call commission. Works lead sourcing + CRM mgmt + reply triage. Does NOT send outreach copy.

**Aligned operating docs (v3 · 2026-05-07):**
- `/03_OUTREACH/SOP_assistant.md` (the assistant's working manual)
- `/03_OUTREACH/SOP_discovery_to_close.md` (BJ-side post-VIB closing playbook)
- `/03_OUTREACH/SOP_VIB_production.md` (BJ-side VIB outreach SOP, already locked)

**Archived v2 docs:** `/03_OUTREACH/_archive_v2_2026-05-07/`
- `2_Assistant_SOP_Manual (1).docx`
- `3_Founder_Outreach_System (1).docx`

**Active CRM:** `/Users/sniper/Downloads/SNIPED CRM.xlsx` (Excel · Notion migration when stood up per blocking action 4)

**Onboarding to v3:** first 7 days are calibration per SOP_assistant.md Section 15. Days 1-3 reduced volume + daily feedback from BJ. Days 4-7 full cadence. Week 2 onward standard.

**Curated SNIPED_OS access for assistant** (per SOP_assistant.md Section 12):
- SOP_assistant.md, VIB_caption_library.md, CANONICAL_TRUTHS.md, delivery_architecture_v2.md, /09_ART_SERIES/

**Claude usage by assistant:** lead enrichment, visual gap drafting, trigger event search. Not for: writing copy, replying to leads, simulating BJ's voice, fabricating evidence. Privacy rule: do not paste financial / memory / strategic-only docs into Claude.
