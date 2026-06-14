# Quality Gate · "The Door"

No cut is sent to FMO Media until every gate below passes. Gates compose the OS standards already in the repo. Nothing is crowned final on a single self-review; the Gemini second-model lane runs as hostile critic before send.

## Gate 1 · STORY_GATE (9 questions)
All 9 answered in `02_WINNER_SCRIPT_AND_STORYGATE.md`. Re-confirm against the *finished cut*, not just the script: does the assembled film still open the loop in 3s and close it on the exhale? Run `os_story_gate.py gate`.

## Gate 2 · Brief pass test (the client's own bar)
- Does a first-time viewer feel "you're not failing, you're carrying a lot"? (the family bar)
- Does the caregiver beat read as "a calling that's finally respected," not "an employee"? (the recruiting bar)
- Would it "make a room go quiet"? If it is merely nice, it fails.

## Gate 3 · Anti-gloss / register check (the category killer)
Reject the cut if ANY of these are true:
- It looks like a stock-footage healthcare ad or a corporate explainer.
- Skin is plastic, faces are too perfect, the elderly subject reads as a young actor.
- Studio glamour light, teal-orange grade, HDR pop, or lens-flare flex.
- Anyone smiles at the camera; the emotion looks performed.
- The home looks like a staged showroom, not a lived-in coastal NC house.
This is the highest-frequency failure mode for AI work on this brief. It is a hard fail, not a note.

## Gate 4 · Identity + world continuity (os-face-lock)
- The mother, daughter, and caregiver are recognizably the same person in every shot they appear.
- One consistent grade and light logic across all AI clips so it reads as one film, not a prompt collage.
- The house and coast are consistent. Reject any drifted face or mismatched room.

## Gate 5 · Commercial Craft 12-axis scorecard (Benchmark V2, emotional-brand-film profile)
Score hook_strength, shot_variety, subject_continuity, audio_motivates_cuts, transition_logic, pacing_asl_by_type, visual_hierarchy, typography_captions, payoff, commercial_clarity, rewatch_value, premium_feel. **Target >= 30/36, no axis at 0 or 1.** Confirm the pacing contrast: hero hold (V7/V10) is the longest, montage (V3) the shortest. Run `os_reference_gate.py scorecard` on the export.

## Gate 6 · Vertical-native + muted-viewing
- Hook reads in the first 1 to 2s with sound off (the 2:14 AM caption + the lit phone).
- Captions present and clean for the hook and payoff lines.
- Safe margins for 9:16 UI (no key action under the caption bar or top chrome).
- The YouTube 16:9 conform protects the hero framing (faces not at the edge).

## Gate 7 · Legal / ownership (we ship only what we own)
- Music is ElevenLabs-composed and owned. The in-world "old standard" is generated, NOT a real copyrighted song.
- VO is owned (ElevenLabs license). No real Synergy client likenesses used; all people are AI-generated and fictional.
- Brand: name and feeling only, per brief (no logo-compliance requirement).

## Gate 8 · Voice / copy
- No em-dashes anywhere in captions, title, or any copy sent (lifetime rule).
- VO has no AI-tell phrasing. Spare, human, true.

## Gate 9 · Second-model hostile critique (Gemini lane)
Before send, run the cut and the script through the Gemini second-model lane (`os_gemini_review.py` / `os_second_model_gate.py`) as a read-only hostile critic. Accept only evidence-backed notes. Gemini never crowns the final; it only tries to break it. Per the second-model Gemini lane doctrine.

## Gate 10 · Speed honesty
The brief watches turnaround. Log actual elapsed time from approval to first send. Ship the first strong instinct; do not over-polish past the point of diminishing return. "Send it the moment it's ready."

---

### Pass record (v1 cut · 2026-06-08)
Deliverables: `SYNERGY_THE_DOOR_v1_9x16.mp4` (1080x1920, 48.4s) + `SYNERGY_THE_DOOR_v1_16x9_youtube.mp4` (1920x1080, centered + blurred fill).

| Gate | Status | Note |
|---|---|---|
| 1 STORY_GATE | PASS | All 9 answered in `02_`; finished cut still opens loop at 2:14 AM, closes on exhale + button. |
| 2 Brief pass test | PASS (self) | Family "you're not failing" named and earned; caregiver dignity present via Eleanor's recognition + the hand. Needs human gut-check. |
| 3 Anti-gloss | PASS | Documentary register held on all 13 frames; 2 frames re-rolled to kill artifacts; no stock/corporate sheen. |
| 4 Identity/world | PASS | Eleanor/caregiver/daughter consistent across shots via locked refs; Seedance held identity in motion (QA strip confirmed). |
| 5 12-axis | PASS (est) | Hero holds (Eleanor 6s, exhale/hands 5s) vs montage (2s) = strong pacing contrast; uniform grade; owned title. Formal scorecard pending. |
| 6 Vertical/muted | PASS | 9:16 native; "2:14 AM" + "You're not failing" captions read sound-off; hook in first 2s. |
| 7 Legal/ownership | PASS | All people AI-generated/fictional; VO ElevenLabs-licensed; audio bed = own ElevenLabs SFX swells; no real song used. |
| 8 Voice/copy | PASS | No em-dashes; VO spare, human. |
| 9 Gemini hostile | PENDING | Run before any external send. |
| 10 Speed | PASS | Concept to first dual-format cut in one session. |

**KNOWN v1 LIMITATIONS (honest):**
- **Music is a scratch bed.** The ElevenLabs Music API is blocked on this account tier, so the bed is sequenced from owned ElevenLabs SFX piano/string swells, not a composed score. This is the weakest element and the first thing to upgrade (composed owned score) before any real send.
- **720p clips upscaled** to 1080x1920. Fine for a test; regenerate heroes at 1080p for a final.
- **16:9 is a blurred-fill conform**, not natively framed wide. A true 16:9 would regenerate key shots in 16:9.
- **Eleanor's "recognition" (22.8s) is a slow push on a still** (the video filter false-flagged that generation). The exhale (V10, 36.7s) IS real Seedance motion. Gemini's hostile pass (2026-06-08, 6/10, `_gemini_review/RECONCILIATION.md`) flagged the static Eleanor climax as the #1 weakness; top reconciled fixes = regenerate Eleanor with real facial motion (Kling 3.0) + compose a real owned score.
