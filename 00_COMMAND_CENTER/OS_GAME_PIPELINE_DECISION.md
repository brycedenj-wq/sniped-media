# OS GAME PIPELINE DECISION
### Games are a north star, not a current capability. This is the honest path in.
Built: 2026-06-05. Route `build_game_pipeline` exists and is wired, but its engine runtime is RED until a playable build exists. No engine install without explicit approval.

---

## Current honest status

- Route: `build_game_pipeline` , EXISTS, status RED.
- The OS can reason about a game (world, character, core loop, narrative) using the fused corpus.
- The OS cannot produce a playable game. There is no engine installed. `engine.godot`, `engine.unreal`, `engine.unity` are all RED.
- Refusal line (enforced by the route): "GAMES ARE NOT ACTIVE. Blender provides assets/pre-render only; engine runtime RED until a playable build exists."

---

## What owns what

| Layer | Owner | Role in a game |
|---|---|---|
| 3D assets, environments, characters, pre-render | **Blender (gated)** | already ACTIVE; models, sets, look-dev, cinematics. Not a runtime. |
| World + character system | **os.crs + os.world** | the bible the game is built from |
| Stills / concept / texture refs | **Higgsfield** | concept + texture generation |
| First playable runtime, game logic, input, real-time | **Godot (proposed first)** | the actual interactive loop. RED until installed + a playable build. |
| High-ceiling cinematic / AAA-look runtime | **Unreal (later)** | photoreal real-time, Nanite/Lumen, virtual production. Heavier. |
| Mobile / AR / client-forced runtime | **Unity (later, only if forced)** | only if a client or mobile/AR requirement demands it |

---

## Engine decision (ordered)

1. **Godot first.** Free, open-source, light, scriptable (GDScript/C#), fastest path to a *first playable*. Best fit for proving the capability without heavy install or cost. Imports Blender assets directly.
2. **Unreal later** for the high-ceiling cinematic/game route once a Godot playable proof exists and the ambition justifies the weight.
3. **Unity later** only if a client, mobile, or AR requirement forces it.

---

## What makes games ACTIVE (the proof bar)

Same bar as everything else: route + artifact + log + gate + repeat. Specifically:
- A **playable build** (runs, takes input, has one real interactive loop), and
- produced through the gated pipeline (assets from Blender, logic in-engine), logged, and
- repeatable from the route.

Until that exists, `build_game_pipeline` stays RED and refuses to claim otherwise.

---

## Smallest playable proof (the first real test, when approved)

A single-screen, single-mechanic Godot build:
- one Blender-exported asset (a character or object) imported into Godot,
- one input that moves/affects it,
- one win/lose or state-change condition,
- exported to a runnable build, logged in `game/<title>/10_logs/BUILD_LOG.csv`.

That one artifact flips `engine.godot` from RED to ACTIVE and `build_game_pipeline` from RED to AMBER.

---

## Activation sprint (LATER, only on explicit approval)

1. Install Godot (approval required; no install yet).
2. Wire a `game/` workspace + BUILD_LOG.
3. Blender -> Godot export path test (one asset).
4. Smallest playable proof (above).
5. Register `engine.godot` ACTIVE with the playable artifact as proof.
6. Promote `build_game_pipeline` to AMBER, then ACTIVE once repeatable.

---

## Why this is the right call

The fused brain already thinks through a game more completely than most scoping docs (it activates narrative_canon, world_character, decision_judgment, automation_toolchain on the prompt). The missing piece is purely the runtime. Godot is the cheapest honest way to earn the ACTIVE label. We do not claim it before the playable proof exists.
