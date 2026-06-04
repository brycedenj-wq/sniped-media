# PHASE 2 , FIRST REAL MOTION TEST, RUN 001 (2026-06-04)

> The first live generation through the atom + motion layer. The gate caught a real identity miss on a real image and stopped the spend before video. Failure treated as data.

## Final credits spent
- **2 credits** (hero still only). Motion clip NOT generated.
- Balance: 881 -> **879** (confirmed by live read). 18 credits saved by the gate. Ceiling was 20; spent 2.

## Asset paths
- generated: `campaign_house/axis_meridian_motion_001/04_generations/axis_hero_v1.png` (then moved on REJECT)
- rejected: `campaign_house/axis_meridian_motion_001/07_rejected/axis_hero_v1.png` (1.5MB, real)
- source URL: cloudfront `hf_20260604_210410_33ef4d32...png` (896x1200, 3:4)
- gate reports: `10_logs/hero_identity_gate_report.json`, `10_logs/hero_frame_obs.json`, `10_logs/hero_scene.json`
- harness logs: `10_logs/PROMPT_VERSIONS.csv`, `GENERATION_LOG.csv`, `VISION_GATE_LOG.csv`, `SKILL_EXTRACTION_LOG.csv`

## Still gate result
- **Identity gate: QUARANTINE.** score 0.8. Hard-fail: `mole_below_left_eye` absent. The other 4 hard invariants held (eye_color deep-brown, face_geometry angular-symmetrical-high-cheekbones, build lean-athletic, complexion even-ambiguous-mid-tone), read from a zoomed face crop, not guessed.
- **World gate: PASS.** Brutalist Monument interior, doorway aperture, bone-white + concrete, neutral in-palette, no forbidden elements.

## Motion gate result
- **NOT RUN.** Per the rule "do not generate video from a failed base," the pipeline stopped at the still. No clip, no motion QA.

## What passed
- the world/visual language rendered correctly and in-register on the first try (environment, light, palette, wardrobe, negative space, composed expression).
- 4 of 5 identity hard invariants held on a real generation.
- the entire harness mechanically: prompt logged -> generated -> ingested (real 1.5MB asset, no placeholder) -> vision-read -> gated -> verdict logged -> asset moved to 07_rejected -> skill candidate logged.
- the cost discipline: preflight matched actuals exactly (2 cr), balance reconciled.

## What failed
- the **signature mole** (a hard identity invariant) did not render. A single text-to-image pass dropped the 1-2mm mark.

## What got quarantined
- `axis_hero_v1.png` , moved to `07_rejected/` with the reason recorded. No video built on it.

## Whether the pipeline held
- **YES.** This is the strongest possible proof: on a REAL generation the gate caught a real identity miss, refused to certify, and stopped 18 credits of downstream spend. A faked or loose gate would have passed a 4/5 "close enough" hero and built motion on an off-spec base. The OS controlled motion by refusing to start it.

## What needs fixing before Phase 3
1. **Signature-mark robustness (the real lesson).** A 1-2mm mole is a fragile anchor for generative consistency. Options: (a) demote the mole to a SOFT invariant and rely on geometry/eyes/complexion/build (already robust); (b) add a post-gen signature-mark injection step (inpaint the mole deterministically); (c) require a tight face-crop verification frame so the mark is actually checkable. Recommendation: (a) + (b) , keep a signature, but do not make a sub-pixel detail a HARD gate.
2. **Verification framing.** Editorial-wide hero framing makes face-level invariants hard to verify; the CRS sheet should include a tight identity-lock frame for gating.
3. **Vision-observation step.** The per-frame observation is currently me reading the image; Phase 3 should formalize a repeatable vision-extraction (crop + read) so it is not ad hoc.

## Whether this atom is strong enough to build on
- **Yes, with one spec adjustment.** The hard structure proved out on real output: the world, visual language, lighting, wardrobe, and 4 of 5 identity anchors rendered cleanly and in-register, and the gates + harness + cost discipline all worked. The only weakness is the choice of a sub-pixel mole as a HARD invariant, which is a spec fix, not a system failure. Make the signature robust (demote mole to soft + add mark-injection, add a tight verify frame), re-run one hero, and the atom is ready for Phase 3. The machine is sound; the character spec needs one edit.

## Guardrails honored
No posting. No extra variants. No spend beyond approval (2 of 20). No celebrity/real likeness. No employer material. No brand decision. Failure recorded as data.
