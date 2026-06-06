# COMMERCIAL CRAFT BENCHMARK V2 (2026-06-06)

> Correction baked in: **classify the FORMAT first.** Fast cuts != commercial. Slow is only a failure when the hold is **unmotivated** (low contrast), **repetitive** (uniform shot lengths), or has **no payoff**. A luxury manifesto, a swimsuit reel, a comedy spot, and a tutorial are NOT judged by one ASL band. Enforced by `os_reference_gate.py --type` + the format profiles. Built from single-spot data where possible (best_comm_4 Heinz single = 2.47s comedy) + the V1 batch + craft doctrine. Grows as more SINGLE spots are ingested.

## The core rule
1. Classify format. 2. Apply that format's profile. 3. Slow fails ONLY with (repetitive OR no-payoff). 4. Score the 12-axis scorecard. Speed is never the goal; motivation + payoff + variety are.

## Format profiles (gate-enforced)
| Format | ASL band | Cuts/min | Variety | Transition logic | Audio-sync | Payoff |
|---|---|---|---|---|---|---|
| **comedy / punchline** | 1.3-3.5s | >=12 | high | hard cuts on lines; cut to the joke beat | dialogue/timing drives cuts | yes , the punchline/brand button |
| **product spot** | 1.5-4.0s | >=10 | high | cut-on-action; clean inserts | beat-synced; reveal on accent | yes , product = longest clean hold |
| **beauty / fashion reel** | 1.0-4.5s | >=10 | med-high | fast texture/detail inserts + held hero; whip/match | cut to the track, on beat | yes , the hero look held |
| **luxury manifesto** | 3.5-9.0s | >=3 | med | slow, deliberate; motivated holds; minimal cuts | score-led, space + silence | yes , a held hero, contrast >=2.2x |
| **social teaser** | 0.6-2.5s | >=16 | high | relentless; hook in <1s | every cut on beat | yes , one payoff |
| **BTS / personality** | 2.0-8.0s | >=5 | med | looser; personality carries; jump cuts OK if intentional | natural sound + bed | optional |
| **tutorial / explanation** | 4.0-18.0s | >=2 | low-med | b-roll over talking-head; clarity cuts | VO-led | optional |

(Generic `commercial` fallback: 1.5-6.5s, cpm>=8, contrast>=2.0, payoff yes , use only when format is unclear.)

## Per-format expectations (beyond ASL)
- **Comedy:** structure Problem->Agitate->Payoff or setup->turn->button. The turn lands on a cut. (Snickers, Heinz.)
- **Beauty/fashion:** macro/texture inserts (fabric, skin, water, hair) intercut with the held hero; grade is consistent and rich; the product/look is the longest clean frame. (Alma Love sits here, swimsuit = hero.)
- **Luxury manifesto:** restraint is the brand. Long holds are a feature, but each must be motivated (camera move, light change, performance) and the film must still contrast (one beat longer than the rest) and pay off. Speed is wrong here.
- **Social teaser:** front-load the hook; one idea; vertical-native.
- **Tutorial:** clarity and b-roll beat pace; no payoff requirement.

## The 12-axis EDIT SCORECARD (`os_reference_gate.py scorecard`; 0-3 each, ELITE >=30/36, no axis 0-1)
hook_strength · shot_variety · subject_continuity · audio_motivates_cuts · transition_logic · pacing_asl_by_type · visual_hierarchy · typography_captions · payoff · commercial_clarity · rewatch_value · premium_feel.
Auto-filled axes (from `check`): pacing_asl_by_type, shot_variety, audio_motivates_cuts (presence). The rest are eye/ear-confirmed.

## Expensive vs amateur (format-agnostic)
- **Expensive:** motivated cuts; pacing CONTRAST (the hero is the longest hold regardless of band); consistent intentional grade; shallow DOF / deliberate framing; audio-led cutting; one owned title system; restraint; one genuinely aggressive hero angle; subject/world continuity.
- **Amateur:** monotone ASL; unmotivated dissolves/zooms; auto-WB/grade drift; everything eye-level + same shot size; music the cut ignores; filler captions; no clean hero beat; over-long UNMOTIVATED static holds (the real fail, not "slow"); jump cuts without intent; product shown flat like a catalog.

## Data + honesty
Single-spot anchor: best_comm_4 Heinz (comedy, ASL 2.47s, PASSES comedy profile). Chanel N5 luxury film ingest failed (age/format-gated) , retry to add a real luxury-band anchor. Bands for less-sampled formats (beauty/fashion, social teaser, BTS) are craft-set and will be tightened as single spots in each format are ingested. The gate prints which profile it used so the judgment is never one-size-fits-all.
