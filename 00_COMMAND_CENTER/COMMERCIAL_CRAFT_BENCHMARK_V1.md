# COMMERCIAL CRAFT BENCHMARK V1 (2026-06-06)

> Built from the first ingested batch (REFERENCE_LIBRARY): creative_tv_comp_1 (compilation, ASL 6.92), best_comm_2 "Super Bowl funny" (ASL 1.96), best_comm_3 "Best commercials" (ASL 3.85), best_comm_4 "Heinz/Ed Sheeran" single spot (ASL 2.47), show_editing_1 "MKBHD method" tutorial (ASL 4.76), show_editing_2 "Reels" tutorial (ASL 16.67). The bands below are evidence-backed, not vibes. The edit gate (`os_reference_gate.py`) enforces the measurable ones.

## Content-type ASL bands (measured)
| Type | ASL band | Evidence |
|---|---|---|
| Commercial, energetic/comedy | 1.5-3.0s | best_comm_2 1.96, best_comm_4 2.47 |
| Commercial, measured/story | 3.0-5.0s | best_comm_3 3.85 |
| Commercial, cinematic/luxury | 4.0-6.0s (but product beat = longest hold) | SOLE register; creative_tv spectacle spots |
| TOO SLOW for a commercial | sustained >6.5s without a held-payoff reason | creative_tv_comp_1 6.92 (title-card skew); SOLE film 11.7s |
| Editing tutorial / talking-head (NOT the commercial bar) | 5-17s | show_editing_1 4.76, show_editing_2 16.67 |

## 1. Hook patterns (first 1-3s)
- **Spectacle/impossible open**, withhold the product (moon-creature spot).
- **Story/idea cold-open** , a character mid-situation or a line that opens a loop (Heinz: "I've got an idea for a Heinz ketchup commercial").
- **Pattern interrupt / juxtaposition** , the product framed as anything-but-itself (cc_anything_but_itself).
Rule: the first 1-3s must pose a question the rest answers. No soft logo-first opens.

## 2. Average shot length (ASL) ranges
Use the band table above per content type. The hero/product beat is ALWAYS the single longest shot in its neighborhood (pacing contrast >= 2x ASL). Energetic spots ride 1.5-3s; never let a non-payoff shot exceed ~6.5s in a commercial.

## 3. Transition types
- **Hard cut** = default, motivated by action or musical beat.
- **Cut-on-action**, **match cut**, **whip/motion**, **object wipe** (towel/hand across lens , operator doctrine).
- **J/L cuts** (audio leads or trails the picture) for flow.
- Avoid unmotivated dissolves/fades/zooms; reserve dissolve for a real time/scene change.

## 4. Audio-sync rules
Lay music FIRST. Cut on the beat/downbeat; sync the biggest action + the product reveal to accents. J/L cuts for momentum. One beat of near-silence or a duck right before the payoff (SOLE seal-strike method). For narrated spots, the VO is the spine and cuts serve the line.

## 5. Typography rules
One OWNED type system. Title/brand lockup is a STRUCTURAL beat (open or sign-off), not filler. <=1 title per ~30s; 1.5-2.5s legible holds; safe margins (5%). Kinetic type lands on beats. No readable filler text scattered through the cut.

## 6. Shot variety rules
Rotate wide/establishing -> medium -> insert/detail -> aggressive-angle hero. Never two same-size shots back to back. One deliberate extreme angle = the cover/thumbnail (cc_aggressive_angle_is_the_cover). The product gets its own clean insert.

## 7. Common commercial structures
- **Problem -> Agitate -> Product -> Payoff** (Snickers "you're not you when you're hungry").
- **Idea/Story -> Build -> Brand button** (Heinz narrated pitch).
- **Spectacle -> Withhold -> Reveal**.
- **Vignette montage -> Tagline**.
- **Demo -> Proof -> CTA**.
End on the brand + the longest, cleanest hold.

## 8. What makes an edit feel EXPENSIVE
Motivated cuts; pacing contrast (fast inserts vs a held hero); consistent intentional grade; shallow DOF / deliberate framing; audio-led cutting; one strong title system; the product is the longest + cleanest beat; restraint (no filter stacking); one genuinely aggressive hero angle.

## 9. What makes an edit feel AMATEUR
Monotone ASL (every cut the same length); unmotivated dissolves/zooms; auto-WB / grade drift; everything eye-level and the same shot size; music the cut ignores; readable filler text everywhere; no clean product beat; over-long static shots; jump cuts without intent; product shown flat like a catalog.

## Gate mapping (enforced by os_reference_gate.py --type commercial)
too_slow (ASL > band) · too_repetitive (low pacing contrast / uniform shot lengths) · audio_not_motivating_cuts (checklist + no-audio flag) · weak_transition_logic (checklist) · low_shot_variation (shot count vs duration) · no_commercial_payoff (no longest-hold product beat near end , checklist) · copy_not_carrying (no transcript/VO when structure needs it).
