# OS ONE COMMAND LAYER
### The top-level commands the organism understands
Built: 2026-06-05. Each command maps to one route in `os_tool_registry.ROUTES` and produces a full execution graph via `os_execution_graph.py command "<name>"`.

The point: you speak intent, the OS wakes the right modules, loads the right doctrine, runs the right toolchain, applies the right gates, produces the artifact, logs it, and stops at the approval line. You do not name tools.

---

## The 14 commands

| Command | Route | Status | Produces | Hard gate / approval line |
|---|---|---|---|---|
| `make campaign package` | make_campaign_package | ACTIVE | full kit + gate + dashboard | postproduction gate |
| `build private demo` | build_private_demo | AMBER | private demo package (no public host) | privacy gate; HTML host HELD |
| `create world` | build_world_3d | ACTIVE | test scene + sandbox render | blender gate, sandbox only |
| `generate motion` | generate_motion | ACTIVE | clip + finished cut | spend approval |
| `edit video` | cut_video | ACTIVE | trimmed/resized/caption-safe | motion QA |
| `build pitch deck` | build_pitch_deck | AMBER | board + one-sheet -> PDF | multi-page deck not templated |
| `build proof loop` | create_proof_loop | AMBER | scored responses | not deployed (held) |
| `track leads` | track_leads | AMBER | tracked records | no proven Airtable write route yet |
| `create client room` | create_client_room | AMBER | Drive folder + Notion record | storage-write; none built yet |
| `launch readiness check` | run_launch_readiness_check | ACTIVE | readiness report | none |
| `run money path` | score_money_path | ACTIVE | money-readiness score | none |
| `certify docs` | certify_docs | ACTIVE | certified ledger row | got==total verify |
| `absorb new tool` | absorb_new_tool | ACTIVE | honest registry row + route | capability proof bar |
| `run max sprint` | run_max_sprint | ACTIVE | max-depth package across modules | spend approval |

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
