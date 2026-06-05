# OS ONE COMMAND LAYER
### The top-level commands the organism understands
Built: 2026-06-05. Each command maps to one route in `os_tool_registry.ROUTES` and produces a full execution graph via `os_execution_graph.py command "<name>"`.

The point: you speak intent, the OS wakes the right modules, loads the right doctrine, runs the right toolchain, applies the right gates, produces the artifact, logs it, and stops at the approval line. You do not name tools.

---

## The commands (expanded 2026-06-05)

Dedicated action routes so the fused brain can ACT, not fall back to a generic campaign route.

| Command | Route | Status | Produces | Refuses / hold line |
|---|---|---|---|---|
| `build film pipeline` | build_film_pipeline | AMBER | shot list + stills + clips + trailer package | no scored film, no sound gen, no multi-shot continuity claim, no release |
| `build game pipeline` | build_game_pipeline | RED | Blender assets + design doc + first-playable plan | GAMES NOT ACTIVE; no engine install without approval |
| `build content engine` | build_content_engine | ACTIVE | repeatable format kit + drafted posts | drafts only; no live posting |
| `build money move` | build_money_move | ACTIVE | ranked move + reversibility + kill criteria | recommendation only; no payment, no published price |
| `build client pitch` | build_client_pitch | AMBER | board + one-sheet PDF (private) | no overclaim; no send without go |
| `build private demo` | build_private_demo | AMBER | private demo package | no public host; static only |
| `build proof loop` | create_proof_loop | AMBER | scored responses | not deployed; no public form |
| `build motion trailer` | build_motion_trailer | ACTIVE | titled motion trailer | no sound gen; no release |
| `build product drop` | build_product_drop | AMBER | drop mockups + print spec | no manufacture before demand; no checkout |
| `activate tool` | absorb_new_tool | ACTIVE | honest registry row + route | no ACTIVE without proof bar |
| `certify source` | certify_docs | ACTIVE | certified ledger row | no certify unless got==total |
| `build launch readiness` | run_launch_readiness_check | ACTIVE | readiness report | report only; authorizes nothing |
| `make campaign package` | make_campaign_package | ACTIVE | full kit + gate + dashboard | postproduction gate |
| `create world` | build_world_3d | ACTIVE | test scene + sandbox render | blender gate, sandbox only |
| `generate motion` | generate_motion | ACTIVE | clip + finished cut | spend approval |
| `edit video` | cut_video | ACTIVE | trimmed/resized/caption-safe | motion QA |
| `run money path` | score_money_path | ACTIVE | money-readiness score | none |
| `run max sprint` | run_max_sprint | ACTIVE | max-depth package | spend approval |
| `track leads` / `create client room` / `build pitch deck` | (resp.) | AMBER | see registry | named unblocks in backlog |

Run any command: `os_execution_graph.py command "<name>"`. Run free-text: `os_execution_graph.py graph "<intent>"`.

## Judgment / decision / review routes (2026-06-05, fall-throughs closed)

Read-only routes that emit a verdict, never silently land in the campaign route. Each carries a refusal line AND a stop-and-ask line.

| Command | Route | Status | Emits | Stop and ask |
|---|---|---|---|---|
| `judge visual quality` | judge_visual_quality | ACTIVE | EXCELLENT / TEMPLATE-LOOKING / REJECT + reasons | if it is a real-person identity edit, stop |
| `choose tool stack` | choose_tool_stack | ACTIVE | ranked stack from ACTIVE tools only + gaps | if it needs spend or install, ask first |
| `evaluate legal risk` | evaluate_legal_risk | ACTIVE | identity/employer/IP/privacy flags + reversibility | ALWAYS route binding legal to operator + lawyer |
| `decide engine stack` | decide_engine_stack | ACTIVE | Blender vs Godot vs Unreal vs Unity + why | if recommending an INSTALL, ask for approval |
| `review client readiness` | review_client_readiness | ACTIVE | SHIP / FIX / HOLD + hardest-to-say-no gaps | even on SHIP, a real-client send needs a go |
| `critique world` | critique_world | ACTIVE | weakness report + concrete fixes | internal only; do not act without a go |

These are ACTIVE because they only read/analyze and emit a verdict; they never take an outward action. The refusal + stop-and-ask lines keep them from overclaiming or crossing a held line.

---

## How to invoke

```
# full chain for a command
os_execution_graph.py command "build private demo"

# full chain for free-text intent (auto-routes)
os_execution_graph.py graph "grade this hero and cut a 9:16 teaser"
```

Every command run answers the 10 organism questions and refuses to run if a required tool or the route itself is not ACTIVE. AMBER commands return the chain plus the exact blocker, never a fake "done."

---

## Command -> module fan-out (what wakes)

- Creative make commands (`campaign`, `world`, `motion`, `pitch deck`, `max sprint`) wake the creation modules (visual/video/layout/threeD) plus their doctrine packs and the post-production gate.
- Business commands (`track leads`, `proof loop`, `client room`, `money path`) wake the ops/proof/sales modules plus the privacy + trust doctrines.
- Operating commands (`launch readiness`, `certify docs`, `absorb new tool`) wake the operations/toolchain/research modules.

The `safety_identity` doctrine is a standing floor on all of them.

---

## What is intentionally NOT a command yet (deferred)

- `post` / `publish` / `send outreach` / `host` / `deploy` / `setup payment` / `finalize legal` , all HELD by mandate until proof + explicit go. They exist as gated routes only, never as one-word commands, so they cannot fire by accident.
