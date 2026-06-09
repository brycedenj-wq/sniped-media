# NLE_MOMENT_BASED_EDITING_OS (LOCKED 2026-06-08)

Make the OS edit human footage like an editor, not a clip sorter. Built after the OS missed the speaker-kick (the strongest moment in the Alma shoot) by judging clips on 3 static frames.

## The core shift
- The edit unit is the **MOMENT**, not the clip and not the frame.
- A clip is not selected because it is pretty. It is selected because it contains a usable **moment** (an action, a change, a beat).
- A moment lives between frames. Static frames find pretty; they do not find a kick, a turn, a reach, a fidget, a glance.

## THE NEW LAW
**If a human remembers a specific strong moment and the OS does not surface it, the OS failed the edit.** Not the human's job to remind the OS. The moment log must contain it.

## Hard rules (these prevent the loop)
1. **3-frame filmstrips are TRIAGE ONLY, never the judge.** They decide "does this clip have a subject / is it junk." They never decide a clip's moments or its rating.
2. **To rate a clip you must scan it densely enough to see actions:** for human-performance footage, frames at <=1s spacing (finer in the action window), or watch it. A 14s clip gets >=14 sample points, not 3.
3. **Watch ONCE, properly, and PERSIST it.** The output of the watch is a permanent `MOMENT_LOG` (timestamped). Never re-derive from scratch. The looping happened because shallow passes were not persisted, so every pass re-guessed. The moment log is the cache and the source of truth.
4. **Log moments, not clips.** Every usable moment is one row (see schema). One clip can yield several moments.
5. **Cut from timestamped moments,** never from whole-clip in-points guessed blind. Every timeline beat cites a source clip + in/out to the action.
6. **Verify the cut with a watch pass.** Extract the actual edit's frames and confirm the intended moment is on screen at that beat. (This is what finally caught the V1 hook/hero misses.)
7. **Orientation + identity confirmed at real size** before rating (the D94A3315 mislabel was a rotated 300px strip). Canon here = vertical (transpose), iPhone = landscape; confirm per source.

## MOMENT LOG schema (one row per moment)
`source_file | timestamp_range | action | performance_quality | camera_quality | brand_value | edit_function | sound_potential | transition_potential | role(hook/build/payoff/ending) | keep/kill + reason`

## The 8 moment roles to fill (every edit needs these found, not assumed)
best hook moment, best attitude moment, best movement moment, best product/body moment, best weird/deadpan moment, best transition moment, best hero moment, best ending/button.

## Process (the standard, every human-footage edit)
1. Triage all clips (1 frame each) -> drop the junk, group by source/type.
2. Dense-scan every surviving clip (<=1s spacing) -> build the MOMENT_LOG (timestamped).
3. Fill the 8 roles from the log (pick the strongest moment for each).
4. Build the REAL_EDIT_MAP (moment -> timeline placement, cut-in/out, why, sound beat).
5. Cut from the moments.
6. Watch-pass the cut; confirm each intended moment is on screen.
7. Score (12-axis); fix; never call final until proof says so.

## POSTMORTEM - the Alma failure (why it kept looping)
- **Why the speaker-kick was missed:** the selects pass judged clips on 3 frames (15/50/85%). D94A3298's frames at 2.2/7.2/12.2s showed empty street / walking-in / a static near-kick frame that read as "walking with a suitcase." The ACTION (fidget -> kick at 11.4-12.5s) lives in motion the static frames did not convey.
- **Why D94A3315 was mislabeled:** rated as a "deadpan close" from a rotated 300px filmstrip; it is actually a wide car-on-street clip. Low-res + rotated triage was used as the judge (rule 1 violation).
- **Why V1 over-indexed body/car:** with no moment log, in-points were guessed; pretty body/car frames dominate the footage, so blind sampling returns body/car. No moment-role coverage (rule "fill the 8 roles") meant the attitude/movement/kick roles went unfilled.
- **The exact rule that prevents it next time:** rules 1-3 (dense scan, never judge on 3 frames, persist a moment log) + the 8-role coverage + the watch-pass verification + THE NEW LAW.
- **Skill/resource that should have fired but did not:** `os_visual_selects_engine` (dense filmstrips) at dense spacing, and `watch` on the clips, not a sparse strip. They existed; the spacing was too coarse and the output was not persisted as a moment log.

## What must change before Synergy
Do not touch Synergy until the Alma reel is cut from a real moment log and clears the rubric. If the OS cannot cut a 30s reel from real footage, it is not ready to promise a cinematic AI film. Memory: [[nle-moment-based-editing-os]].
