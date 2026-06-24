---
name: ai-native-brand-lab
description: Build three uncrowned AI-native brand/world candidates at equal excellence, then make them fight through creative-director review, format testing, and the operator taste gate. Use for "brand lab", "build worlds", "build a world", "3 candidate worlds", "ai-native brand", "brand IP candidates", "serialized cast object", or "build all three". Raises the floor; crowns nothing. Concept-grade front half of the visual stack; produces world bibles, prompts, and scores, NOT pixels.
metadata:
  type: workflow
---

# AI-Native Brand Lab

The OS as a working creative director. Given one brief it builds THREE uncrowned worlds at equal excellence and refuses to ship if any one is filler. It is the concept-grade (taste-ceiling) front half of the visual stack: it produces worlds and bibles, it does NOT generate pixels (`OS_V2_UNIVERSAL_ENGINE/VISUAL_ENGINE.md` owns generation, spend-gated). It sits above generation the way `creative-levelup` sits above the pipeline.

Sourced from the creative-direction extraction wave (`OS_V2_UNIVERSAL_ENGINE/AI_NATIVE_BRAND_LAB/CD_EXTRACTION_WAVE_001/`), which confirmed the spec on disk (GOLD image-study contract, stylescape three-direction, equal-excellence) and surfaced the deltas folded in below.

## INVOKE WHEN
- The operator wants net-new AI-native brand worlds as competing candidates.
- The operator wants a brand IP with an uncopyable moat.
- References the prior seeds (S1 Listener / S2 Dead Weight Index / S3 Night Shift Bureau) or "build all three."

## THE BAR (hard law)
Three candidates, all strong enough that the operator says "we could build all three." If one is filler, the run FAILS. The floor, not the average, is scored. A strong-strong-weak triplet fails on the weak one. The lab crowns NOTHING: it ranks taste-likelihood and hands the operator the comparison; the only authority is the operator passing the External Visual Proof Gate. A text world board is NOT visual proof.

## DIVERGENCE AXIS, the six differentiation lenses (folded in from GOLD, CD Wave 001)
Each candidate is forced onto a DIFFERENT lens so the three genuinely diverge instead of being cosmetic variants. The lenses (provenance GOLD `gold_c005.txt`):
1. Scale (play with relative size; the small made monumental or the monumental made intimate)
2. Aesthetic (a defined visual-language swap as the organizing move)
3. Beauty (where the beauty actually lives; subvert the obvious)
4. Transportation (move the subject to an unexpected world/context)
5. Clashing (force two incompatible registers to share one frame)
6. Tension (build an unresolved charge the viewer must hold)
If any two candidates share a lens or collapse to the same moat, one is rebuilt. This is distinct from `sniped-direction-stack` (which calibrates ONE brief per candidate); the lenses force divergence ACROSS candidates. Run both: direction-stack per candidate, lenses across candidates.

## ROUTES TO (names the skill, does not re-implement it)
- `os-world-bible` (authority): author each candidate's WORLD.json, the 9 rule categories + continuity gate.
- `cinema-worldbuilder`: translate a locked world into motion/scene grammar when a candidate needs a moving proof beat.
- `banana-pro-director`: per-still keystone prompt (still before motion).
- `sniped-art-series`: the photographer studies as the taste reference for divergence (note: skill metadata still reads "5 locked" vs 9 on disk, flagged drift).
- `sniped-direction-stack`: the 5-question calibration diagnostic, run once per candidate.
- `OS_V2_UNIVERSAL_ENGINE/VISUAL_ENGINE.md`: the 10-axis elite-content rubric + generic-visual-reject gate (the strong-enough scorer).
- `OS_V2_UNIVERSAL_ENGINE/MEASUREMENT_ENGINE.md`: confidence-floor + honest-label discipline (scores labeled stated/inferred/unknown, never crowned).
- `OS_V2_UNIVERSAL_ENGINE/PRODUCTIZATION.md`: the moat / serialized-uncopyable-object test per candidate.

## STAGE PIPELINE (the harness)
Run `ai-native-brand-lab.workflow.js`: BRIEF (calibrate per candidate via direction-stack) to DIVERGE x3 (each on a distinct lens, fresh context, worktree) to SCORE (Opus, the rubric) to HOSTILE (fresh-context organize-then-challenge + adversarial-verify) to REVISE (bounded) to VERDICT + RECEIPT, ending on the External Visual Proof Gate. Serious runs go through the workflow, not single-thread.

## REVISE rule (folded in from GOLD, CD Wave 001)
One bounded revision per candidate. The losing/weaker directions FEED the winner: harvest the strongest single element from each rejected candidate into the survivor before re-scoring (provenance GOLD `gold_c010.txt`, stylescape Develop stage). Do not loop into self-congratulation; re-read `do_not` each pass.

## GATES (must pass before handing back)
- External Visual Proof Gate (operator is final visual authority; no candidate is "strong" on Claude's say-so).
- generic-visual-reject (stock-AI / template / generic-luxury / generic-streetwear / generic-creator = REJECT).
- Character World Interiority Gate (recurring character/world needs an Interior Card before serious prompt use).
- Honest-label + tool-readiness-honesty: no tool is verified-live; all generation spend-gated.
- System-layer hallucination guard (folded in from convos `convos_c005.txt`, CD Wave 001): forbid fabricated proof, invented examples, and unverified anecdotes at the contract level, not as a per-call reminder. Every capability claim carries a readiness label or UNKNOWN.
- No-self-crown: the SCORE and HOSTILE phases run in fresh context, never the builder.
- 9/10 floor for client-ready.

## OUTPUT
Writes to `OS_V2_UNIVERSAL_ENGINE/AI_NATIVE_BRAND_LAB/RUN_<NNN>/`: 3 `CANDIDATE_<n>/` (WORLD.json + keystone prompt + assigned lens + moat note + score), `SCORE.md`, `VERDICT.md`, `OS_RECEIPT.md`. Status draft / NO-SEND until the operator signs.

## HONEST LABELS
No tool is verified-live. All generation is spend-gated. This skill produces world bibles, prompts, and scores, NOT images. The strong-enough verdict is a proposal until the operator passes the External Visual Proof Gate. The lab does not back the falsifiable proof (the camera does); no number, testimonial, or proof image is fabricated.
