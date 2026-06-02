# Retoucher Training Notes · SNIPED Phase B Onboarding

This is the onboarding pack for the future part-time retoucher hire (Mo 6-9 per OPERATIONAL_BACKBONE Section 3). The hire is triggered when Hero edit volume sustains > 30/month for two consecutive months and edit time becomes the production bottleneck.

This doc is read-once at onboarding, referenced thereafter. The runbook layer lives in `/05_PRODUCTION/lightroom_operating_system.md` and `/05_PRODUCTION/SOP_capture_to_delivery.md`.

---

## 1. The role

The retoucher does NOT make creative direction decisions. The retoucher executes the locked SNIPED workflow on Heroes that BJ has color-labeled and queued.

What the retoucher owns:
- Lightroom Hero finish work (apply locked masks, run the decision tree, generative remove cleanup)
- Evoto round-trips (skin work to SNIPED Evoto preset)
- Photoshop work for frames flagged Red (heavy comp, frequency separation, dodge-and-burn, liquify within strict guardrails)
- Final export per SNIPED export presets
- Folder hygiene (files end in correct subfolder, no orphan files in Lightroom catalog)

What the retoucher NEVER owns:
- Cull (BJ only · this is editorial judgment)
- Color label decisions (BJ only)
- Hero promotion to Green / VIB Blue / Case Study Purple (BJ only)
- Develop preset creation or modification (BJ only)
- Final approval before delivery (BJ only)
- Direct client communication (BJ only)
- Decision to deviate from the locked workflow (escalate to BJ)

---

## 2. The system the retoucher inherits

Before Day 1, all of these must be in place:

- ✅ Master catalog: `SNIPED_YYYY.lrcat`
- ✅ Import preset: `SNIPED · IMPORT DEFAULT`
- ✅ Develop preset chain (5 presets per `/05_PRODUCTION/preset_library.md`)
- ✅ Metadata preset: `SNIPED_COPYRIGHT_YYYY`
- ✅ Smart Collection set (12 collections per `/05_PRODUCTION/lightroom_operating_system.md` Section 3.4)
- ✅ Color label vocabulary documented (Section 3 of the OS doc)
- ✅ Export presets (9 per `/05_PRODUCTION/preset_library.md` Section 4)
- ✅ AI mask stack documented (Section 6 of the OS doc)
- ✅ Retouch decision tree documented (Section 7 of the OS doc)

If any of these are missing on Day 1, BJ has not finished the prerequisite work. Do not start onboarding until all are checked.

---

## 3. Day 1 onboarding (4 hours)

### Hour 1 · Catalog architecture + import

Read with retoucher:
- `/00_BRIEF/PRODUCTION_OS.md` Sections 1-2
- `/05_PRODUCTION/lightroom_operating_system.md` Sections 1-3

Walk through:
- The `/SNIPED_PRODUCTION/YYYY/YYYY-MM-DD_Client_TYPE/` folder structure
- The catalog location and backup discipline
- The import preset and what it does automatically
- Why Smart Previews exist and when they save the day

Practice: open the catalog. Browse a recent shoot folder. Verify Smart Previews exist.

### Hour 2 · Color labels + Smart Collections

Read with retoucher:
- `/05_PRODUCTION/lightroom_operating_system.md` Section 3 (Organization system)
- The 12 Smart Collections and what each feeds

Walk through:
- The color label vocabulary (Red / Yellow / Green / Blue / Purple / none)
- The 12 Smart Collections and their rules
- The retoucher's daily workflow: filter to "01 · Heroes Pending Retouch," work the queue

Practice: filter to Heroes Pending Retouch. Identify a Red-label vs Yellow-label frame. State out loud the routing for each (Red → Lightroom + Photoshop, Yellow → Lightroom + Evoto).

### Hour 3 · Develop preset chain + AI mask stack

Read with retoucher:
- `/05_PRODUCTION/lightroom_operating_system.md` Sections 5-6
- `/05_PRODUCTION/preset_library.md` Section 1

Walk through:
- The 5 develop presets and when each applies
- The locked AI mask stack (5 masks per Hero)
- The copy-paste workflow with mask propagation

Practice: take an unedited Hero. Apply locked-look (already on import). Run the 5-mask stack. Time it · target 60-90 sec for the masks. Compare against BJ's reference Hero.

### Hour 4 · Decision tree + Evoto + Photoshop boundaries

Read with retoucher:
- `/05_PRODUCTION/lightroom_operating_system.md` Section 7 (Retouch decision tree)

Walk through:
- The 4-question tree for every Hero
- What "before Evoto" means (Lightroom is fully done first)
- What "after Evoto" means (re-import TIF, apply Hero Finish, export)
- What Photoshop is for (Red frames + Brand System tier only)
- What Photoshop is NEVER for (skin, color grade, spot removal · those have other tools)

Practice: walk three Heroes through the decision tree, narrating the routing decision for each.

---

## 4. Daily retoucher workflow

Once onboarded, the retoucher's daily session looks like this:

1. **Open catalog** · `SNIPED_YYYY.lrcat`
2. **Filter to "01 · Heroes Pending Retouch"** smart collection
3. **For each frame:**
   - Apply the locked AI mask stack (60-90 sec)
   - Run Generative Remove on background distractions if needed
   - Walk the decision tree (Q1-Q4)
   - Route to Evoto or Photoshop per the tree
   - Bring back to Lightroom, apply `SNIPED_HERO_FINISH_v1`
   - Export per `SNIPED · Hero · JPG Deliverable` and `SNIPED · Hero · TIF Master`
   - Change color label from Red/Yellow → Green (signals "Hero done, ready for BJ review")
4. **End of session:** flag "Heroes Live" smart collection count (should equal completed work)
5. **Communicate to BJ:** brief Slack/Notion update with count complete + any frames escalated

---

## 5. The escalation rules

Escalate to BJ (do NOT decide alone) when:

- Frame ambiguous between Red and Yellow (heavy retouch judgment)
- Frame has client-sensitive issues (visible logo on competing brand · skin condition needing tact · expression that reads "off")
- AI mask fails to detect subject correctly and manual brush would take > 5 min
- Frame is a Hero candidate but reads better at Select tier (downgrade decision is BJ only)
- Color grade looks "off" against the locked-look reference and you're not sure why
- Anything that requires creative direction · the retoucher executes, BJ directs

Escalation method: leave color label as-is (do NOT change to Green), add a flag, message BJ in Notion / Slack with the frame name and the question. Move to next frame.

---

## 6. The off-limits list

The retoucher does NOT:

- Modify any develop preset in `/05_PRODUCTION/preset_library.md`
- Create new Smart Collections
- Re-edit a frame already labeled Green (BJ-approved · do not touch)
- Apply heavy retouch beyond what the decision tree calls for
- Use AI image generation tools (Firefly subject generation, Midjourney, etc.) on any client work
- Composite faces, bodies, or subject elements (only backgrounds, distractions, atmosphere)
- Use any preset pack outside the SNIPED_LOCKED set
- Change copyright metadata
- Export to any folder outside the locked structure
- Communicate directly with clients

The Berger / anti-AI rule (see `/10_REFERENCE/STRATEGIC_PRINCIPLES.md` Section 4h) is absolute. AI is utility. Subject is always real, present, photographed.

---

## 7. The performance contract

Targets the retoucher is measured against:

| Metric | Target |
|---|---|
| Hero edit time (full Lightroom + Evoto + back to Lightroom) | 12-15 min/Hero |
| Heroes per session (4-hour block) | 12-16 |
| Photoshop frames per Reset | 0-2 (most Resets need none) |
| Photoshop frames per Op Kit | 1-3 |
| Photoshop frames per Brand System | 4-8 |
| Color labels propagated correctly | 100% (Green only after BJ approval, not before) |
| Frames escalated unnecessarily | < 1 per session (over-escalation = re-train, not the rule) |
| Frames committed to Green that should have been escalated | 0 (this is the firing offense · decisions outside scope) |

Quality bar: every Green frame the retoucher delivers should pass BJ's Hero standard. Spot checks weekly · 5 random Greens compared against BJ-only reference Heroes from the prior month.

---

## 8. Why this discipline matters

The retoucher hire is the moment SNIPED scales without diluting. Every frame the retoucher ships carries SNIPED's name. The methodology, color label system, mask stack, decision tree, and preset chain are the rails that ensure the work that ships at scale matches the work BJ ships solo.

Per the Naval leverage logic (`/10_REFERENCE/intel_leverage_logic.md`): a retoucher is labor leverage, the lowest-multiplier form. The leverage works only if the system is locked. A loose system + a retoucher = inconsistent work that erodes the brand. A locked system + a retoucher = capacity expansion without quality drift.

Per Company of One (`/10_REFERENCE/intel_company_of_one.md`): the retoucher is right-size growth, not scale-for-scale. One part-time retoucher unlocks 30+ Heroes/month additional capacity. Two retouchers without volume to support them is overstaffed and breaks the moat.

---

## 9. Onboarding completion criteria

The retoucher is "onboarded" when they can:

- ✅ Filter to "01 · Heroes Pending Retouch" without instruction
- ✅ Apply the 5-mask stack to a Hero in under 90 sec
- ✅ Walk the decision tree out loud on any frame and route correctly 9 of 10 times
- ✅ Round-trip to Evoto and back without instruction
- ✅ Export per the correct Hero export preset to the correct subfolder
- ✅ Apply the correct color label transition (Red/Yellow → Green) only after work complete
- ✅ State the off-limits list from memory
- ✅ Identify when to escalate vs when to proceed

Onboarding period: 2 weeks of supervised work (BJ reviews every Green before delivery). After 2 weeks, sample-review only (BJ spot-checks 25% of Greens before delivery).

---

## 10. The single rule for the retoucher

**Execute the locked workflow. Refuse the temptation to invent. Escalate when uncertain. The methodology is not yours to change · it is yours to apply.**
