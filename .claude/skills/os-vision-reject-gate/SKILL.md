---
name: os-vision-reject-gate
description: Visually review any generated frame, video still, product shot, campaign image, or AI composite BEFORE it ships. Use after any image/motion generation and before posting/delivery. Reads the asset and scores it against the slop/hands/skin/clothing-physics/text/identity/brand/likeness/beat-source checklist; any hard-fail = REJECT.
---

# OS Vision Reject-Gate

Before any generated asset ships:
1. Run `scripts/os_vision_gate.py <path>` to emit the checklist (and confirm the file exists).
2. **Read the asset** (Read tool handles images; for video, review key stills) and score EACH item:
   slop · hands · skin (melanin-true, not plastic) · clothing physics · text artifacts · identity consistency (matches CRS) · brand consistency (v3 LUXURY, no teal/orange) · copyright/likeness (owned character only, no celebrity) · beat-source (must beat an honest camera frame).
3. **Verdict: SHIP / FIX / REJECT.** Any hard-fail = REJECT, do not ship. Log a REJECT to the error/quarantine dashboard.

Placeholder for automation: when a vision-model API is wired, this skill calls it per item; until then the model performs the review via Read. Pairs with `os-quality-gates` (beat-source/reject), the campaign-house pipeline stages 7-9, and the visual doctrine in OS_MASTER_DOCTRINE.
