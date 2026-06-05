# 08 GATE UPGRADES , taste gates (all CANDIDATE until tested)

I have everything I need. The harness pattern is clear: rubric-based gates that score declared observations, log to CSV, move folders on verdict, and `audit` for enforcement. The new gates mirror this exactly. Here is the full deliverable.

---

# GATE UPGRADES FOR TASTE
## The Estate of Her, taste-gate layer v0 (CANDIDATE, none tested)

The old harness proves one thing: the machine can keep a character CONSISTENT and ARTIFACT-CLEAN across stills, edits, and motion. `os_crs`, `os_world`, `os_facematch`, `os_herolock`, `os_motion_qa`, and `os_vision_gate` all answer the same question in different costumes: *did the output stay under control.* Not one of them asks *is the output worth remembering.* Per [CERT] feedback_strongest_photograph_not_most_processed, the actual bar is "beats the source / forces a reaction," and the machine already knows how to refuse itself on a failed mole. The job here is to point that exact refusal reflex at FORGETTABLE.

Design principle for every gate below, lifted from the existing harness so these are real, not decorative:
- Same shape as `os_vision_gate`: a named RUBRIC, the **model Reads the asset and scores each item**, HARD items quarantine outright, verdict is `SHIP / FIX / REJECT`, every verdict writes a CSV log row, and an `audit` subcommand FAILS if any approved asset skipped the gate. [CERT mirror of os_vision_gate.py + os_motion_qa.py]
- These run as **stage-7.5 and stage-9.5** in OS_CAMPAIGN_HOUSE_PIPELINE.md: AFTER the existing control gates (reject/beat-source at 7, polish/beat-source at 9), BEFORE `os_herolock register`. **A hero cannot lock until it clears taste, not just control.** That single insertion is the whole upgrade: it makes "forgettable" a quarantine condition.
- Per DRY-RUN-001 BUG-2, taste stays model-judged doctrine (not pixel-deterministic), so these are gates Claude follows at the seam, with the CSV/folder enforcement deterministic the way `os_checkpoint.py` is. Everything below is **CANDIDATE / not-yet-tested** until the validation protocol at the end runs.

The proposed bundle is one new script, `os_taste_gate.py`, holding nine sub-gates, plus one meta-gate (`beat_old_cell`) that consumes the other nine. Skill wrapper candidate: `os-taste-gates` (sibling to the existing `os-quality-gates`).

---

## GATE 1 , MEMORABILITY (`mem`)
**HARD. The gate the old cell failed: do you remember it ten minutes later.**

**Checks:** whether the frame is recognizable cropped to a face-removed thumbnail, and whether it forces a reaction. This is the [PROOF] "drawable from memory in 5 seconds" test operationalized.

**Rubric (model Reads the asset, scores 0/1/2):**
| item | hard | pass condition |
|---|---|---|
| `icon_at_thumbnail` | HARD | crop to 120px, remove the face: is the LOT 00 kraft tag / portrait-sitter silhouette / red-string still unmistakably THIS world. 0 = reads as generic premium aristocrat. |
| `five_sec_draw` | HARD | could a stranger redraw the defining mark from memory after 5 sec. The kraft tag + red string must be the answer. |
| `forces_reaction` | soft | does it provoke (the humiliation-of-lineage charge), or is it inert/pretty. |
| `ten_min_recall` | soft | distinct enough that it would not blur into the feed's other AI editorials. |

**Pass/fail rule:** SHIP requires both HARD items ≥1 and total ≥6/8. Any HARD item = 0 → REJECT (this is exactly the old failure: passes control, fails recall).

**Plug-in:** runs on the `os_herolock` candidate BEFORE register; reads the `approved` and a generated `marked` (face-removed) crop. Reuses the facecrop/identitycrop assets `os_herolock register` already expects, just inverts them (face-OUT instead of face-locked).

---

## GATE 2 , CULTURAL SPECIFICITY (`spec`)
**HARD. Placeless/timeless/tourist = REJECT.** [CERT lineage doctrine + scene-density]

**Checks:** that the frame documents from INSIDE the foreclosed-estate lineage with a committed noeme, not visiting it as costume drama. Directly answers the territory's stated `why_it_fails` (costume-drama cosplay).

**Rubric:**
| item | hard | pass condition |
|---|---|---|
| `inside_lineage` | HARD | reads as the house archivist documenting the liquidation, not a tourist shooting a pretty manor. The auction-tag intrusion is omnipresent. |
| `noeme_committed` | HARD | commits to a specific lot, a specific room in the rotation, a dated `LOT 00 / [estate] / YYYY-MM-DD` slug. "This happened here on this date." |
| `scene_thickens` | soft | adds to the named estate world (climbing lot count, recurring room aging) vs only adding a look. [CERT: "does this thicken the scene"] |
| `not_tourism` | soft | refuses single-visit cultural cosplay; the hunt-country grammar is lived, not borrowed. |

**Pass/fail:** SHIP requires both HARD ≥1 and ≥6/8. `noeme_committed` = 0 (no date/lot/room commitment) → REJECT.

**Plug-in:** consumes the chapter slug from `os_world` (the registered estate bible) and the naming convention `LOT 00 / [estate] / [YYYY-MM-DD]`. Fails if the slug is generic or absent.

---

## GATE 3 , ANTI-GENERIC-AI-EDITORIAL (`antigeneric`)
**HARD. The single most important gate, because the old cell collapsed a 7-environment vocabulary into the most cliche room.** [CERT]

**Checks:** that the frame is NOT the default Midjourney/Higgsfield output. Refusal-positioning made literal: name what this is NOT, and fail it if it drifts toward the default.

**Rubric:**
| item | hard | pass condition |
|---|---|---|
| `not_default_backdrop` | HARD | NOT clean-brutalist-monolith-plus-moody-figure. Must be a committed estate-rotation room (tack room / lot-tagged portrait gallery / horse-shaped-absence stable / crated grand stair). |
| `not_floor_consistency_flex` | HARD | the frame is NOT demoing "AI consistency works." Consistency is table stakes; if the only thing interesting is that it's the same character, REJECT. [PROOF] |
| `restraint_reveals` | soft | quiet-luxury restraint is the floor the distortion BREAKS, not the identity. If restraint reveals nothing (empty synthetic, stock-premium), fail. [CERT] |
| `no_loud_default` | soft | no teal/orange, no saturation hammer, no HDR. Counter-signal, not loud render. [CERT] |

**Pass/fail:** SHIP requires both HARD ≥1 and ≥6/8. `not_default_backdrop` = 0 → REJECT outright. This is the gate that would have killed AXIS v0.

**Plug-in:** cross-checks the plate's environment against the registered `os_world` rotation slots. If the env is not one of the four committed estate rooms, hard quarantine.

---

## GATE 4 , SYMBOL CONSISTENCY (`symbol`)
**HARD. The symbol system is the moat; a watermark is not.** [PROV worldbuilding + CERT bw_card]

**Checks:** that the recurring grammar COMPOUNDS and the color-law never leaks. This is the territory's stated single point of failure: "red-tag color-law must never leak onto non-sale objects or the literacy breaks."

**Rubric:**
| item | hard | pass condition |
|---|---|---|
| `glyph_present` | HARD | the kraft LOT 00 tag (kraft card / string / stamped number) is present and legible. The figure wears the wrist-tag reading LOT 00. |
| `color_law_clean` | HARD | auction-red appears ONLY on tag string + stamp. ANY red leak onto a non-sale object → REJECT. "Red = for sale" literacy is binary. |
| `motif_compounds` | soft | the climbing lot-number countdown is consistent with the chapter index (lot count rises as estate empties). |
| `register_correct` | soft | HERO = color (estate still hers), CARD = B&W (lot sold). Apparatus layer stays color. [CERT bw_card_dual_register] |

**Pass/fail:** SHIP requires both HARD ≥1 and ≥6/8. `color_law_clean` = 0 is the strictest fail in the whole bundle: a single leaked red pixel-region on a non-tag object is an automatic REJECT, because it breaks the world's reading literacy permanently.

**Plug-in:** this is the most automatable gate, candidate for a cheap deterministic pre-screen. A `cv2` red-mask pass (mirroring the cheap SSIM gross-drift screen pattern in os_facematch) can flag red regions; if red overlaps anything outside the registered tag bounding boxes, auto-FIX flag before the model even scores it. Cheap screen, expensive judge, exactly the harness's stated doctrine.

---

## GATE 5 , WORLD TENSION (`tension`)
**HARD. Conflict makes a frame alive; decoration kills it.** [PROOF + CERT diagnosis]

**Checks:** the figure is in CONFLICT with the space (scale-violence, intrusion, refusal), never compliantly decorating it. This is the territory's spine: "subject-vs-world scale-violence keeps every frame alive instead of decorative."

**Rubric:**
| item | hard | pass condition |
|---|---|---|
| `scale_violence` | HARD | the figure is in scale-conflict: dwarfed by crated heirlooms, hemmed by stacked lots. NOT centered, comfortable, well-proportioned to the room. |
| `figure_vs_world` | HARD | she is AGAINST the space (catalogued, hemmed, sold), not posing in front of a pretty backdrop. If she decorates, REJECT. |
| `stance_fightable` | soft | the cold-defiant aristocratic refusal reads (chin level, spine vertical, held glove). Not neutral, not longing. |
| `mess_preserved` | soft | the liquidation disorder (crates, tags, the horse-shaped absence) is present, not cleaned into a tidy luxury set. |

**Pass/fail:** SHIP requires both HARD ≥1 and ≥6/8. This gate is the direct antidote to the root cause: it FAILS the "empty controllable room, no conflict, no mess" choices that the QA engine optimizes toward.

**Plug-in:** runs alongside `os_crs` body-grammar check. `os_crs` proves the stance is HELD (control); `tension` proves the stance is FIGHTING (taste). They share the same pose-reference inputs.

---

## GATE 6 , EMOTIONAL CHARGE (`charge`)
**HARD. One dominant non-neutral register, owned.** [PROOF]

**Checks:** the frame carries the single locked emotion (cold defiance under dispossession) and is NOT neutral. The root cause names "no emotional edge" as a memorability killer.

**Rubric:**
| item | hard | pass condition |
|---|---|---|
| `not_neutral` | HARD | the frame is NOT emotionally flat. A neutral synthetic = stock = REJECT. |
| `register_locked` | HARD | the emotion is the territory's ONE register: held aristocratic refusal, chin level, gaze unbroken (or implied via stance, faceless-safe). Not grief, not longing, not menace. One owned register. |
| `punctum_present` | soft | one unplanned wound is preserved, not retouched out (a thread out of place, the off-fall of the held glove, light on a single fingernail). [PROV: do-not-clean list] |
| `composure_under_sale` | soft | "refusing to flinch while being auctioned" reads. The defiance is the point. |

**Pass/fail:** SHIP requires both HARD ≥1 and ≥6/8. `punctum_present` connects to a **do-not-clean list** the pipeline must override the AI's smoothing instinct against, the territory's anti-stock weapon.

**Plug-in:** new soft-signature field in `os_crs` ("one preserved punctum per hero frame"), so the harness's existing soft-signature recovery logic (`os_mark`) protects the wound instead of cleaning it.

---

## GATE 7 , CAMPAIGN USEFULNESS (`useful`)
**Soft-bundle, HARD on format. Is this a deposit into one compounding franchise, or a one-off.** [CERT entertainment + advertising lens]

**Checks:** the frame functions as a numbered LOT entry in the serialized estate-catalogue format, with the apparatus that survives being clipped.

**Rubric:**
| item | hard | pass condition |
|---|---|---|
| `format_locked` | HARD | renders as an auction-house LOT listing: masthead, edition stamp, `LOT 00 / [estate] / YYYY-MM-DD` slug, ledger-serif type. Not a loose pretty image. [CERT: the room is the upgrade] |
| `hero_or_fill` | HARD | declared as one canonical HERO lot-frame OR supporting cluster-fill. No undeclared 50-equal-posts diffusion. [CERT: concentrate firepower] |
| `clip_survives` | soft | re-attribution code / colophon baked in so it survives being reposted by fan-pages. [CERT: clip-survival apparatus] |
| `loop_open` | soft | caption closes on which lot sells next, building toward "when does LOT 00 sell." [PROV: Sugarman open loop] |

**Pass/fail:** SHIP requires both HARD ≥1 and ≥6/8. `hero_or_fill` forces the Elberse concentration discipline: the gate will not let the cell ship 50 equal posts.

**Plug-in:** reads the apparatus/masthead layer; this is the "room" gate. Ties to stage 9 (edit/finish) where the catalogue wrapper is applied.

---

## GATE 8 , SHAREABILITY (`share`)
**Soft-bundle, [PROOF] heavy. Why would a stranger repost this.** [CERT distribution + PROOF status-betrayal]

**Checks:** the status-betrayal charge (hijack old-money grammar, then stage its humiliation) and the "1.25-inch bauble of identity" a subculture shares to signal who they are.

**Rubric:**
| item | hard | pass condition |
|---|---|---|
| `status_betrayal` | soft | hijacks the deepest old-money grammar then stages its humiliation. A sharper charge than reverent luxury. [PROOF: status-betrayal travels, share pull UNPROVEN] |
| `bauble_of_identity` | soft | a specific cluster (post-human-luxury / old-money-aesthetic) would repost it to signal who they are. |
| `coinable_phrase` | soft | "LOT 00" reads as a coin-able phrase + number system in one. [PROOF: coinability unproven until a real loop] |
| `cluster_fit` | soft | seeds into ONE dense cluster, not diffuse reach. |

**Pass/fail:** no HARD items (shareability is genuinely [PROOF], cannot be gated on taste alone). SHIP requires ≥5/8. **Critically: this gate's verdict is logged but NOT trusted as final** until the real proof loop runs, per the confidence-label rule. It flags weak-share candidates for the kill/keep/scale call at stage 13, it does not certify share pull.

**Plug-in:** feeds stage 12 proof-tracking. Its predictions get reconciled against actual saves/shares/DMs once a real loop runs, which is how [PROOF] claims earn or lose status. Candidate to wire `mcp__claude_ai_Higgsfield__virality_predictor` as a CHEAP SCREEN input here, not as the judge, exactly the screen-cheap-judge-expensive pattern.

---

## GATE 9 , BEAT THE OLD PROOF CELL (`beat_old_cell`)
**META-GATE. HARD. The whole point.** [CERT strongest-photograph reject gate, pointed at memorability]

**Checks:** does THIS frame make the old clean AXIS proof cell feel like version 0. This is the gate that consumes the other eight and asks the one question that was never on the test sheet.

**Rubric (consumes Gates 1-8 + one head-to-head):**
| item | hard | pass condition |
|---|---|---|
| `beats_v0_head_to_head` | HARD | placed beside the old AXIS/brutalist hero, a stranger picks THIS one as more memorable. If v0 holds its own, this frame has not earned the upgrade. |
| `taste_floor_met` | HARD | Gates 1-6 (the HARD taste gates: mem/spec/antigeneric/symbol/tension/charge) ALL returned SHIP. One taste REJECT below = automatic REJECT here. |
| `beats_wild_editorial` | soft | beats the best AI-editorial currently in the wild, not just the old cell. [PROOF] |
| `would_stranger_remember` | soft | the final "ten minutes later" recall test on the finished, captioned, apparatus-wrapped unit. |

**Pass/fail:** SHIP requires both HARD ≥1 and ≥6/8. `taste_floor_met` makes this gate strictly downstream: it cannot pass unless the six hard taste gates passed. This is the structural lock that prevents the old failure mode, control-pass being mistaken for a win.

**Plug-in:** this is the **gate immediately before `os_herolock register`.** Wiring: `os_herolock register` should REFUSE (the same way it already refuses a missing source asset) if `beat_old_cell` did not log a SHIP. One line added to `cmd_register`'s guard clause:
```
if not _taste_cleared(a.hero_id):
    print(f"  REFUSED: hero {a.hero_id} has no beat_old_cell SHIP in taste log"); return 1
```
That single refusal turns the entire `os_herolock` registry from a control-only anchor into a taste-AND-control anchor. The locked-hero canon can no longer fill with forgettable frames.

---

## HOW THE BUNDLE PLUGS INTO THE EXISTING HARNESS

```
stage 7  os_vision_gate  (slop/hands/skin/identity/beat_source)   [CONTROL, exists]
stage 7.5  os_taste_gate gate-all  (mem,spec,antigeneric,symbol,    [TASTE, NEW]
            tension,charge,useful,share)
stage 8  os_motion_qa    (grounding/edges/temporal/physics)        [CONTROL, exists]
stage 9  edit/finish + beat_source                                 [CONTROL, exists]
stage 9.5  os_taste_gate beat_old_cell  (meta, consumes 7.5)       [TASTE, NEW]
   -> os_herolock register  (REFUSES without beat_old_cell SHIP)   [hard seam]
```

Proposed CLI, mirroring `os_vision_gate`/`os_motion_qa` exactly:
```
os_taste_gate.py rubric <gate>                          print one rubric
os_taste_gate.py intake <project> <asset>               copy to 05.5_taste_quarantine, print all 9 checklists
os_taste_gate.py verdict <project> <asset> <gate> <SHIP|FIX|REJECT> "<scores>"   log one gate
os_taste_gate.py gate-all <project> <asset>             run 1-8, require all HARD-gate SHIP, then 9
os_taste_gate.py audit <project>                        FAIL if any 06_approved asset lacks 9 taste-log rows
```
Log: `10_logs/TASTE_GATE_LOG.csv`, columns `[ts, asset, gate, verdict, scores, judge]`. The `audit` subcommand is the enforcement teeth, identical to `os_vision_gate audit`: no asset reaches `06_approved` without a full taste record, so taste becomes survival-by-enforcement, not survival-by-discipline (the BUG-2 fix applied to taste).

---

## VALIDATION PROTOCOL (how every gate gets tested BEFORE activation)

Every gate above is **CANDIDATE / not-yet-tested.** None ships until it clears this, mirroring the harness's own proof discipline (the gate that quarantined a real drift and saved 18 credits earned trust by CATCHING a real miss).

1. **Calibration set:** assemble 12 frames: 4 old-cell AXIS/brutalist heroes (known forgettable), 4 strong reference editorials from the certified Nine-Masters lane (known undeniable), 4 fresh ESTATE OF HER candidates. Hand-label each frame's ground-truth verdict per gate.
2. **Catch-the-miss test (the real bar):** a gate is only trusted if it REJECTS at least one frame the old control gates passed. If `antigeneric` does not reject all 4 old brutalist heroes, it is not measuring taste, it is measuring nothing. This is the activation gate for the gates: each must quarantine a real forgettable that control-gates cleared, the same standard the drift gate met.
3. **False-positive ceiling:** no taste gate may REJECT more than 1 of the 4 known-strong reference editorials. A gate that rejects undeniable work is miscalibrated and stays CANDIDATE.
4. **Inter-pass stability:** run each gate twice on the same frame; verdict must not flip. Mirrors `os_motion_qa` running on declared observations: if the model's score is unstable, the rubric items are too vague and get rewritten.
5. **Promotion:** a gate moves CANDIDATE → ACTIVE in `OS_SKILL_REGISTRY.csv` only after it (a) catches ≥1 real miss, (b) stays under the false-positive ceiling, (c) passes inter-pass stability, on the 12-frame set. Logged with the same per-class proof discipline as `os_certify.py`.
6. **`beat_old_cell` is tested last** and only after Gates 1-6 are ACTIVE, since it consumes them. Its specific test: it must pick the 4 strong references and the best ESTATE candidates over the 4 old-cell heroes in blind head-to-head, ≥10/12 correct, or it stays CANDIDATE.

---

## WHAT THIS CHANGES (the one-line case)

The old cell stopped on a failed mole and called inconsistency the only enemy. These nine gates teach the same refusal reflex a second enemy: forgettable. [CERT] The machine already knows how to say no. After this bundle, `os_herolock` cannot crown a frame that is merely under control, it can only crown one that is under control AND undeniable, AND beats v0 head-to-head, AND never leaks a red pixel onto a non-sale object. Taste stops being the thing the operator hopes survives the control gates, and becomes a quarantine condition with CSV teeth.

**Status: all nine gates + meta-gate are CANDIDATE / not-yet-tested.** Nothing is ACTIVE until the 12-frame catch-the-miss protocol runs. The script `os_taste_gate.py` is specced, not written (this was a creative pass, no generation). [PROOF] claims (shareability, coinability of "LOT 00," fifty-chapter durability) remain unproven until a real loop runs and stage-12 proof-tracking reconciles the `share`-gate predictions against actual saves and DMs.

Relevant existing harness files these specs mirror and plug into:
- `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_vision_gate.py` (rubric/verdict/audit pattern)
- `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_motion_qa.py` (HARD-item quarantine + threshold pattern)
- `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_herolock.py` (the register refusal seam for `beat_old_cell`)
- `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_CAMPAIGN_HOUSE_PIPELINE.md` (stage insertion points 7.5 / 9.5)
- `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_SKILL_REGISTRY.csv` (where `os-taste-gates` registers as CANDIDATE)