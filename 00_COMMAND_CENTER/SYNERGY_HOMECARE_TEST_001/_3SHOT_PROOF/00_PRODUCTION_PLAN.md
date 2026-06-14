# Synergy "The Door" · 3-Shot Competence Proof · Production Plan

**Question this answers:** are we actually competent to make Synergy as a REAL AI film now (motion, performance, change), not stills panning?
**Method:** attack the exact three beats The Door v2 FAILED (character performance done as frozen stills / push-ins). If we can now make these three move and perform, we are competent to scale. If not, we diagnose the method before building the film.
**Standard:** cinematic, client-safe, emotionally clear. Sendable ONLY if proof gates pass. No still push-in pretending to be cinema. No Ken Burns. No animatic called a film.

## 1. Brief (re-read, whole)
Synergy HomeCare of Cape Fear, FMO Media paid AI-production vetting. They are auditing a storyteller, not buying a healthcare ad. Target feeling: "the moment the weight lifts" (family) = the same moment the work becomes a calling (caregiver). Avoid corporate-healthcare gloss (the category's #1 failure mode). AI used for emotional truth, not spectacle. 9:16 priority.

## 2. Story as ACTION BEATS only (verbs, the three test beats)
- **Beat A (open):** at 2 a.m. a phone glows on a sleepless daughter's face. She LOWERS the phone, her eyes LIFT, she EXHALES, she DECIDES not to call again. (a decision plays on her face)
- **Beat B (hero):** an old song begins. The mother's face WAKES from blank to recognition, her eyes WELL, she almost-SMILES, she TURNS a few degrees toward the music. (internal recognition, the longest hold)
- **Beat C (resolve):** the mother TURNS from the window to the caregiver, their eyes MEET, the faintest almost-smile PASSES between them, the caregiver's hand SETTLES over hers. (a real connection forms)

Each beat has a start-to-end state change that is NOT camera-only.

## 3. Mini world bible
- **Place:** a lived-in coastal North Carolina home (Cape Fear region). Bookshelves, plants, soft window light, wood kitchen. Modest, warm, real, NOT a staged set.
- **Light:** natural available light. Cool blue 2 a.m. for Beat A; warm low morning/window light for Beats B and C. Anti-gloss documentary grade (Kodak-ish, gentle grain, no glossy commercial sheen).
- **Tone:** quiet, restrained, true. Small moments. Silence and (later) owned score carry it. No spectacle, no flex.
- **Camera language:** locked-off or micro-handheld breathing only; any movement must be motivated by the performance. NO unmotivated push-in.
- **Continuity:** same three faces, same home, same grade across all shots so they cut together.

## 4. Character / identity anchors (locked refs)
- **Eleanor, mother ~78:** white hair, blue cardigan. Ref: `REF_01_eleanor_mother.png`; start still `SB_V07_song_recognition.png`.
- **Daughter ~45:** tired, brown hair, grey tee. Ref: `REF_03_daughter.png`; start still `SB_V02_daughter_awake.png`.
- **Caregiver ~40s:** brown cardigan over blue scrubs, lanyard. Ref: `REF_02_caregiver.png`; appears in start still `SB_V11_together.png`.
All three start stills are already identity-consistent with the refs and were used as the i2v keyframes (stills-before-motion law: animate only approved frames).

## 5. Tool decision per shot (cinematic need, not convenience)
All three are identity-critical character performance beats -> **image-to-video keyframe from the locked still, Kling 3.0, mode=pro, 9:16, sound=off**. Rationale (from THE_DOOR_FILM_AUDIT): Kling 3.0 carries real facial/hand micro-motion; Seedance has face-filter softening + NSFW false-positive risk on tender/elderly beats. Sound off = prove MOTION purely + lower credits; diegetic sound + owned music (Suno) are a finishing pass, not part of the motion competence test. Cost preflight: 10.5 credits / 6s pro shot.

## 6. Verb-first shot prompts (what CHANGES, not what it looks like)
- **Shot 1 (Beat A, ~5s):** "The woman lies in bed in the dark, phone glow on her face. She slowly lowers the phone away from her face, her eyes lift from the screen toward the ceiling, she blinks slowly and exhales a tired breath, her jaw tightens then eases as she decides not to call. Subtle real facial motion, micro-handheld breathing camera, the phone screen dims. Documentary realism, available cool light, fine grain. No fast movement."
- **Shot 2 (Beat B, ~7s):** "The elderly woman sits by the window, her face blank and distant. As an old song begins she changes: her eyes focus and begin to glisten, her lips part slightly as she remembers, the faintest almost-smile lifts one corner of her mouth, she turns her head a few degrees toward the music. Tiny, restrained, real emotion building across the shot. Slow motivated push-in supporting the performance. Warm window light, skin texture, no exaggeration, no grin."
- **Shot 3 (Beat C, ~5s):** "The elderly woman and the caregiver sit together by the window holding hands. The elderly woman slowly turns her head from the window to the caregiver, their eyes meet, and the faintest warm almost-smile passes between them; the caregiver's hand gently settles over hers. A quiet real human connection forming. Gentle camera settle, warm light, documentary realism, two consistent faces, restrained motion."

## 7. What would make each shot FAIL (kill criteria, judged by fresh-context verify + Gemini, not by me)
- **Universal:** face identity drift/morph/melt; waxy plastic skin; teeth/eye artifacts; hands melting or merging; the change does NOT happen (stays a frozen state = animatic fail = the exact thing we are testing against); unmotivated push on a non-changing subject.
- **Shot 1:** phone warps; eyes go uncanny/dead; no real decision reads.
- **Shot 2:** over-smiling/grin instead of restrained almost-smile; stays blank (no recognition arc); Eleanor's face changes identity.
- **Shot 3:** either face swaps/morphs; two-person consistency breaks; the turn looks robotic; no connection change (just two stills sitting).

## Gate after generation
Whole-watch each clip (no sampling) -> per-shot 12-axis-style score -> adversarial-verify workflow (fresh-context skeptics) + Gemini second-model lane -> mini proof packet -> honest verdict: proceed / regen specific shots / revise concept / stop (not competent yet). No full film until this passes.
