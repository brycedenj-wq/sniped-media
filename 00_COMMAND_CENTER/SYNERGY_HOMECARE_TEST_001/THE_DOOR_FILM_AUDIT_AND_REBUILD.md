# The Door · Film Audit + Rebuild (REAL_FILM_PRODUCTION_OS pass)

No defense of the current cut. Judged against `REAL_FILM_PRODUCTION_OS.md`. v2 timeline audited (the v2 with the Kling Eleanor fix). Honest finding up front: **after the Eleanor fix, the film is roughly half real cinema and half animatic.** Two character beats are still stills with push-ins (forbidden by the Push-In Law), one beat is a moodboard state, and the rest are real but several are generic.

---

# TASK 3 — SHOT-BY-SHOT CLASSIFICATION
Buckets: **CINEMA** (subject acts, changes over the shot) · **ANIMATIC STILL** (only the camera moves) · **MOODBOARD** (a state, no action) · **INSERT** (object/detail, allowed static) · **KILL**.
The 7 questions: (a) subject doing? (b) what changes start→end? (c) why camera moves? (d) why cut? (e) sound of the action? (f) works muted? (g) advances story without VO?

| # | beat (t) | class | (a) doing | (b) change | (c) camera why | (d) cut why | (e) sound | (f) muted | (g) no-VO | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| V1 | phone 2:14 (0-3) | INSERT | nothing (object) | screen is lit | slow push = allowed for insert | to her face | phone buzz/room tone | yes (2:14 caption) | yes (sets time/dread) | KEEP, add screen actually lighting |
| V2 | daughter awake (3-6) | **ANIMATIC STILL** | nothing, lies still | nothing (camera only) | push unmotivated | — | breath | weak | weak | **REGEN → cinema** |
| V3a | pills (6-8) | CINEMA (insert-scale) | hands sort pills | pills placed | follows hands | montage | pills rattle | yes | yes | KEEP (or swap, cliché) |
| V3c | night drive (8-10) | CINEMA | drives, blinks | road moves, fatigue | follows motion | montage | engine, road | yes | yes | KEEP |
| V3d | asleep table (10-12) | **MOODBOARD** | asleep (no action) | nothing | push unmotivated | montage | clock tick | partial | partial | **REGEN small motion or KILL** |
| V4 | door opens (12-15) | CINEMA | caregiver steps in | dark→light, arrival | move on entrance | to bag | door, footsteps | yes | yes | KEEP (hero hinge) |
| V5 | bag down (15-18) | CINEMA | sets bag, settles | bag lowered | follows action | to kitchen | bag thud, sigh | yes | yes | KEEP |
| V6 | coffee + record (18-23) | CINEMA (insert) | pours, drops needle | coffee fills, steam | follows pour | to mother | pour, needle drop | yes | yes | KEEP |
| V7 | Eleanor recognition (23-29) | CINEMA (fixed in v2) | face warms, wells, almost-smiles | blank→recognition | slow push supports the performance | to hands | song under, breath | yes | yes | KEEP (now real) |
| V8 | hands held (29-34) | CINEMA (insert-scale) | hand closes, grips | contact made | settles | to place | cloth, skin | yes | yes | KEEP |
| V9 | Cape Fear (34-37) | CINEMA (M5 plate) | water/grass move | environment breathes | slow drift = M5 motivated | to daughter | water, gull, wind | yes | partial (breath beat) | KEEP (or shorten/localize) |
| V10 | daughter exhale (37-41) | CINEMA | shoulders drop, exhales | tension→release | settles | to together | breath out | yes | yes | KEEP (payoff) |
| V11 | together (41-45) | **ANIMATIC STILL** | sit still | nothing (camera only) | push unmotivated | to title | room tone | weak | weak | **REGEN → cinema** |
| V12 | title (45-48) | GRAPHIC | n/a | text in | n/a | final note | n/a | yes | yes | KEEP |

**Score of the cut as cinema:** 9 of 12 motion beats are real cinema after the Eleanor fix. **3 fail the Push-In Law / kill criteria: V2 (hook, character beat as a still), V11 (resolve, character beat as a still), V3d (moodboard state).** V1 is an allowed insert but improves with a lit-screen action.

---

# TASK 4 — REBUILD FROM VERBS (action beats only, no camera, no VO)
The film as pure action. Every beat is a verb that changes state. This is the spine; shots are designed from it.

1. A phone screen **LIGHTS** in the dark.
2. Her eyes **OPEN**. She **STARES** up.
3. Her hand **REACHES** for the phone, then **STOPS**. (she decides not to call again)
4. At the sink she **SORTS** pills, **COUNTS** under her breath.
5. On a dark road she **DRIVES**, **BLINKS** hard to stay awake.
6. At the table she **SINKS**, her head **DROPS**. (she has been carrying it alone)
7. A door **OPENS**. A caregiver **STEPS** in and **SETS** the bag down. (the weight transfers)
8. She **POURS** coffee; steam **RISES**; she **LOWERS** the needle.
9. The mother **HEARS** the song. Her face **WAKES**. She **REMEMBERS**, **MOUTHS** a word, eyes **WELL**.
10. The caregiver's hand **CLOSES** over the mother's. The mother **GRIPS** back.
11. Elsewhere, the daughter **EXHALES**; her shoulders **DROP**. (she lets go)
12. Mother and caregiver **TURN** to each other; the mother almost **SMILES**.
13. Button.

The two beats the v2 cut got wrong now have verbs: beat 2-3 (REACHES/STOPS, a decision, not "lies there") and beat 12 (TURN/SMILE, a connection, not "sit together"). **No shot is final if its only motion is camera.**

---

# TASK 5 — TOOL DECISION PER SHOT (cinematic need, not convenience)
Routing per `REAL_FILM_PRODUCTION_OS` IV1-IV5. Identity-critical character beats = image-to-video from the locked reference (keyframe). Environment/insert with no locked identity = text-to-video or i2v as needed.

| beat | tool decision | engine | why |
|---|---|---|---|
| 1 phone lights | i2v from V1 still, animate screen wake | Seedance | object insert, locked frame, small real motion |
| 2-3 wakes + reaches/stops | **i2v keyframe from locked daughter ref** | **Kling 3.0** (real facial/hand motion; Seedance filter risk on face) | character beat, must perform |
| 4 pills | i2v (hands) | Seedance | action insert, no identity lock needed |
| 5 drive | i2v from locked daughter ref | Kling or Seedance | identity + motion |
| 6 asleep→stir OR replace | i2v keyframe (a small stir/eye-open) | Kling | turn moodboard into a micro-action, or KILL |
| 7 door | keep v2 (real) | Seedance (done) | works |
| 8 coffee | keep v2 | Seedance (done) | works |
| 9 Eleanor recognition | keep v2 (Kling) | Kling (done) | fixed |
| 10 hands | keep v2 | Seedance (done) | works |
| 11 coast | keep v2 (shorten) | Seedance (done) | M5 plate |
| 12 exhale | keep v2 | Seedance (done) | works |
| 13 together turn/smile | **i2v keyframe start→end from locked two-shot** | **Kling 3.0** (start: facing away/neutral; end: turned, almost-smiling) | resolve must be a real connection, not a static push |

Practical note: nothing here is true practical footage (no live shoot in scope); the "practical-feel" is achieved by the anti-gloss documentary grade, not by faking a camera the AI did not use.

---

# TASK 6 — MINIMUM REAL-FILM REBUILD SHOT LIST
The smallest set of changes that turns The Door from animatic into film. Only the failing beats are rebuilt; the 9 working cinema beats are kept. This is the cheapest path to a real film, not a from-scratch redo.

| # | action beat | camera language | performance direction | sound design | tool | generation direction | keep/kill/regen | why cinematic |
|---|---|---|---|---|---|---|---|---|
| R1 | phone LIGHTS | M1, locked-off, 100mm insert, no move | n/a (object) | soft buzz, room tone, distant clock | i2v from V1 still | screen wakes, faint glow blooms, a hand edge enters then withdraws | REGEN (light upgrade) | a real change occurs (dark→lit), not a push |
| R2 | she WAKES, REACHES, STOPS | M1, 75mm, handheld breath, slight settle | eyes open, focus to ceiling, hand reaches to phone then pulls back, jaw tightens | sheet rustle, held breath, phone buzz stops | **i2v keyframe, Kling 3.0**, locked daughter ref | "she lies awake, slowly opens her eyes, reaches toward the glowing phone then stops her hand and lets it fall, a tired breath, subtle real facial tension" | **REGEN (was animatic still)** | a decision plays on her face and hand: performance + change |
| R3 | asleep → STIRS (or kill) | M1, 55mm, locked, faint | head heavy, a small stir, one eye opens at dawn light | clock tick, fridge hum, faint breath | i2v keyframe, Kling | "asleep at the table, dawn light grows, she stirs slightly, a slow breath, does not fully wake" | REGEN or KILL | turns a frozen state into a micro-action; if it can't, cut it |
| R4 | they TURN, almost SMILE | M1, 55mm two-shot, locked + 3" settle | mother turns from window to caregiver, recognition softening to the faintest smile; caregiver meets her eyes | song tail, fabric, a small breath of a laugh | **i2v keyframe start→end, Kling 3.0**, locked two-shot ref | start neutral side-by-side → end: mother turns to caregiver, eyes meet, almost-smile; warm window light | **REGEN (was animatic still)** | the resolve becomes a human connection that changes on screen |

**Keeps (already cinema, do not touch):** door (V4), bag (V5), coffee (V6), Eleanor recognition (V7, Kling), hands (V8), coast (V9, optionally shorten), exhale (V10). **Pills (V3a) and night-drive (V3c)** are real cinema but generic; optional swap for fresher carrying details, not required for the film/animatic line.

**Net minimum to cross from animatic to film: 3 regenerations (R2 wake, R4 together) + 1 optional (R3 asleep) + 1 polish (R1 phone).** Plus the still-open music gap (owned Suno score). Everything else already passes.

---

## Gate after rebuild
Re-run Stages 11-14: /watch, Gemini hostile, reconcile, score. Target: every motion beat passes the kill criteria (subject acts, reads muted, advances story), and the film clears 9/10 with owned music in place. Until R2 and R4 are real motion, the film stays classified ANIMATIC and is not client-ready, regardless of how it looks.
