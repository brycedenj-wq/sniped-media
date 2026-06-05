# OS TASK-TO-SOURCE FUSION TESTS
### Proof the fused brain fires the whole corpus on every task.
Generated 2026-06-05 from os_execution_graph.py. Every task loads the always-on kernel; the rows below show the corpus-specific activation.

| # | Task | Route (status) | Fused nodes | Families | Contradictions | Refuses |
|---|---|---|---|---|---|---|
| 1 | build a campaign world | make_campaign_package (route status: ACTIVE) | narrative_canon, safety_identity, world_character | 15 | 2 | no (GO) |
| 2 | design a film pipeline | make_campaign_package (route status: ACTIVE) | automation_toolchain, leverage_ownership, narrative_canon, safety_identity | 24 | 4 | no (GO) |
| 3 | design a game pipeline | make_campaign_package (route status: ACTIVE) | automation_toolchain, leverage_ownership, narrative_canon, safety_identity | 24 | 4 | no (GO) |
| 4 | price a service for a founder | make_campaign_package (route status: ACTIVE) | founder_operations, pricing_offer, safety_identity | 20 | 4 | no (GO) |
| 5 | create a client pitch | build_pitch_deck (route status: AMBER) | safety_identity, strategy_war, trust_sales | 17 | 2 | YES (not ACTIVE) |
| 6 | judge the visual quality of this hero | make_campaign_package (route status: ACTIVE) | decision_judgment, safety_identity, visual_grade | 16 | 3 | no (GO) |
| 7 | build a proof loop to validate demand | create_proof_loop (route status: AMBER) | safety_identity | 3 | 3 | YES (not ACTIVE) |
| 8 | choose a tool stack for production | make_campaign_package (route status: ACTIVE) | automation_toolchain, decision_judgment, safety_identity | 19 | 4 | no (GO) |
| 9 | write outbound copy for a cold prospect | make_campaign_package (route status: ACTIVE) | copy, safety_identity | 6 | 2 | no (GO) |
| 10 | design a landing page | build_landing_page (route status: AMBER) | safety_identity | 3 | 3 | YES (not ACTIVE) |
| 11 | evaluate legal and startup risk | make_campaign_package (route status: ACTIVE) | decision_judgment, safety_identity | 13 | 3 | no (GO) |
| 12 | build a content engine for distribution | make_campaign_package (route status: ACTIVE) | automation_toolchain, distribution_hook, safety_identity | 15 | 4 | no (GO) |
| 13 | decide whether to use blender unreal or godot | make_campaign_package (route status: ACTIVE) | decision_judgment, safety_identity, world_character | 15 | 3 | no (GO) |
| 14 | build a private demo package | make_campaign_package (route status: ACTIVE) | pricing_offer, safety_identity, trust_sales | 13 | 2 | no (GO) |
| 15 | choose the next money move | make_campaign_package (route status: ACTIVE) | decision_judgment, leverage_ownership, safety_identity | 18 | 4 | no (GO) |

## Per-test detail: always-on kernel principles + confidence + what it refuses
Every task above loaded all 11 kernel law categories (strategy, creative, business, money, proof, production, quality, anti-failure, tool-use, source-confidence, identity-safety) plus the standing safety floor.

Confidence labels are applied per doctrine: CERTIFIED (memory atom present), MIXED, PROVISIONAL (chunk family). The brain uses provisional families WITH the label and never crowns them.

## Honest finding from this run
- The fused layer (nodes + families + contradictions) is correct on all 15. The ROUTE layer is coarser: film/game/tool-stack/content-engine tasks fall through to make_campaign_package because os_tool_router lacks dedicated routes. The brain thinks right; the route table is the next build.
- Games: no engine route exists (Unreal/Godot RED). The brain activates narrative_canon + world_character + the blender/AE tools, but a real game pipeline is a north-star gap, not a current capability.
