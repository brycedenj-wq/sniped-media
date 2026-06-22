---
name: sniped-luxury-edit
description: Run SNIPED's locked Lightroom edit on a single frame in the v3 LUXURY EDITORIAL direction. Use when user wants to develop a Hero, Select, or Proof frame, or asks "how should I edit this frame" / "what's the right approach for this image" in a Lightroom context. Applies SNIPED_LOCKED_LOOK_v3_LUXURY base preset, walks the 10-step develop order, runs the 5-mask AI stack, executes the retouch decision tree (Lightroom only vs Evoto vs Photoshop). Adobe Neutral foundation, Meisel/Roversi/Mert and Marcus lane, NOT cinematic compositing.
---

# SNIPED Luxury Edit Skill

The locked Lightroom workflow for SNIPED's quiet luxury editorial direction. Every frame that enters the pipeline runs through this. Output target: skin warm and dimensional, blacks creamy and lifted, restrained color, recognizable SNIPED authorship.

---

## MANDATORY READING ON INVOCATION

Read in this order:

1. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_visual_direction_luxury_editorial.md` · the locked v3 LUXURY direction
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_edit_register_bifurcation.md` · identity rules
3. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/lightroom_operating_system.md` · catalog, import, masks, retouch tree, exports
4. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/preset_library.md` · the locked preset chain
5. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/_preset_backups/SNIPED_LOCKED_LOOK_v3_LUXURY.xmp` · the v3 preset values (cross-reference if user asks about specific slider values)

After reading, ask:

> "Three questions before we tune:
> 1. Output tier · Hero (full pipeline) / Select (lightweight) / Proof (batch)?
> 2. Lighting context · studio flash / natural / mixed / location?
> 3. Anything weird about this frame I should know · skin tone challenge, unusual color, clipped highlights, etc.?"

---

## THE 10-STEP LOCKED DEVELOP ORDER

Per `/05_PRODUCTION/lightroom_operating_system.md` Section 5.2. Do not skip. Do not jump around.

1. **Crop** · rule-of-thirds upper-third for face
2. **White Balance manual** · refine if As Shot is off. Target: warm believable skin, NOT pushed orange. Editorial register favors Temp 5500-5800, Tint 0 to +5.
3. **Tone basic** · exposure, contrast, highlights, shadows, whites, blacks
   - For luxury direction: lift blacks slightly (+5-10), pull highlights (-15 to -25), midtones neutral
4. **Presence** · Texture -3 to -5 (skin), Clarity 0 to -3 (never positive for skin), Vibrance +0 to +5, Saturation 0 to -8
5. **HSL refinement** · per-image deviations from v3 LUXURY preset base
   - Orange Hue -3 (skin away from over-warm)
   - Yellow Sat -15 (kill digital yellow)
   - Greens Sat -15 (muted, not killed)
6. **Detail / Noise** · verify defaults, adjust only if visible problem
7. **Lens corrections / Transform** · verify no geometry issues
8. **Effects** · vignette OFF (use radial masks), grain baked into v3 LUXURY base
9. **Masking** · the 5-mask AI stack (Section 6 of lightroom_operating_system.md)
10. **Final review** · toggle Before/After with `\`

---

## THE 5-MASK AI STACK (apply to every Hero)

| # | Mask | Tool | Adjustment |
|---|---|---|---|
| 1 | Subject | Select Subject | Exposure +0.10 to +0.20, Clarity -5 |
| 2 | Face skin | Select Person → Face Skin | Skin tone refine, Texture -10, slight warm shift |
| 3 | Eyes (Sclera + Iris/Pupil) | Select Person → Eyes | Sclera: whites lift +8 (NOT more · over-whitening reads fake). Iris: Clarity +15, slight Sat +5 |
| 4 | Teeth (if visible) | Select Person → Teeth | Whites +10, slight yellow desat |
| 5 | Background | Select Subject → Invert | Subtle Exposure -0.20, color shift toward palette, slight radial vignette |

Total mask stack time: 60-90 sec per Hero. Copy-paste mask propagation for Heroes 2-N (see Section 6.3).

---

## THE RETOUCH DECISION TREE

After Lightroom develop is complete, walk this tree for each Hero:

```
Q1: Is the frame structurally clean (no major comp, no liquify, no body work)?
  YES → Q2
  NO  → ROUTE: Lightroom + Evoto + Photoshop

Q2: Did Lightroom Generative Remove handle the small distractions?
  YES → Q3
  NO  → ROUTE: Lightroom + Photoshop

Q3: Does skin need professional retouch beyond AI masks?
  YES → ROUTE: Lightroom → Evoto → Lightroom (Hero finish)
  NO  → ROUTE: Lightroom only

Q4 (optional): Brand System tier requiring frequency separation, D&B, compositing?
  YES → ROUTE: Lightroom → Evoto → Photoshop → Lightroom (final)
  NO  → already routed
```

Reset frames DO NOT trigger Q4 yes. Reset = Lightroom + Evoto. Period.

---

## TIME TARGETS

| Tier | Time per frame |
|---|---|
| Hero (full pipeline) | 12-15 min |
| Select | 1-2 min |
| Proof | 30-45 sec (batch) |

Hero over 25 min: stop. Downgrade to Select or escalate to Photoshop.

---

## OUTPUT FORMAT

When the user shares a frame, work through:

1. State the current observed issue (color cast / exposure / clipped highlights / etc.)
2. Recommend the specific adjustment (slider name + value or AI mask + values)
3. Apply order matters · always reference where in the 10-step locked order this lives
4. After full pipeline: confirm output tier (Hero / Select / Proof) and where it ships (IG / Pixieset / portfolio / Carrd)

---

## WHAT TO REFUSE

- "Let's try a teal/orange grade" · refused per v3 LUXURY direction
- "Crank the clarity for more pop" · refused. Luxury work is never crunchy.
- "Push the saturation hard" · refused. Restraint over volume.
- "Use Auto in the Basic panel" · refused. Kills authorship.
- "Use this preset I bought" · refused if it conflicts with v3 LUXURY signature.
- "Apply this to a client deliverable using AI-generated subject" · refused per identity rule.

---

## FILES

```
sniped-luxury-edit/
└── SKILL.md (this file)
```

Cross-references (read on invocation):
- All locked Lightroom OS docs in /05_PRODUCTION/
- Memory: visual direction, edit register bifurcation, photo theory


## Inputs
- A specific frame to develop (Hero / Select / Proof tier declared by operator)
- Lighting context (studio flash / natural / mixed / location)
- Known frame challenges (skin tone, clipped highlights, unusual color, etc.)
- feedback_visual_direction_luxury_editorial.md + feedback_edit_register_bifurcation.md + lightroom_operating_system.md + preset_library.md (all read on invocation)

## Gates
- The 10-step locked develop order (Section 5.2 of lightroom_operating_system.md) must not be skipped or reordered
- Hero frames require the full 5-mask AI stack before routing to the retouch decision tree
- Hero edit over 25 min triggers a hard stop: downgrade to Select or escalate to Photoshop
- Teal/orange grade, positive Clarity on skin, hard Saturation push, and Auto in Basic panel are all refused per v3 LUXURY direction
- AI-generated subject frames are refused for client deliverables per the identity rule in feedback_edit_register_bifurcation.md

## Test
- case: BJ has a studio flash hero frame with a slight cool cast and visible pore texture on the forehead and asks 'how do I develop this one?' Expected output: skill asks the 3 intake questions (tier/lighting/challenges), then prescribes WB Temp nudge in Step 2, shadow/highlight values in Step 3, Texture -4 on skin in Step 4, the Face Skin AI mask at Texture -10, and routes to LR + Evoto via the retouch decision tree since professional skin retouch is needed.
- expected failure: User asks to apply a cinematic teal and orange grade to a client hero frame. Skill must refuse per v3 LUXURY direction and produce no teal/orange adjustment values regardless of how the request is framed.
