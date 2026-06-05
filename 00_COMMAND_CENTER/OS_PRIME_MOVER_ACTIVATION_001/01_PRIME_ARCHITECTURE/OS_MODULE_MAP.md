# OS MODULE MAP , the 18 organs of the one organism

Each module: what triggers it, what doctrine loads, what tools route, what gates apply, what excellent means, what failure looks like, what is learned back.

## copy
- triggers: copy, headline, caption, tagline, write, words, cta, name
- doctrine loads: `copy` | tools: os.adobe_layout | gates: os_doctrine:copy
- excellent: complete thought, one big idea, in-world voice, no hype, no fragment
- failure: fragment / bible-dump / generic hype
- learns: new phrase patterns + failure modes -> positioning doctrine

## visual_image
- triggers: image, hero, still, photo, render an image, portrait, visual
- doctrine loads: `visual_grade` | tools: mcp.higgsfield.image, mcp.adobe.crop_resize, os.adobe_grade, os.adobe_composite | gates: os_postproduction_gate, os_doctrine:visual_grade
- excellent: beats an honest camera frame, one-color discipline, restraint
- failure: AI slop / inert / color-law broken
- learns: prompt+grade combos that pass -> visual doctrine

## video_motion
- triggers: motion, video, clip, animate, moving, seedance
- doctrine loads: `motion` | tools: mcp.higgsfield.video, hyperframes | gates: os_motion_qa, os_doctrine:motion
- excellent: intent per frame, color discipline survives motion
- failure: moving still passed off as a trailer
- learns: shot recipes that hold the world

## editing
- triggers: edit, cut, trim, trailer, reel, subtitle, footage
- doctrine loads: `motion` | tools: skill.video_use, os.adobe_cut, local.ffmpeg | gates: os_motion_qa
- excellent: rhythm + cuts + clean audio + caption-safe
- failure: no cuts, audible pops, captions misaligned
- learns: pacing patterns -> editing doctrine

## sound
- triggers: sound, audio, music, sfx, soundtrack, voice, score
- doctrine loads: `motion` | tools: adobe.firefly_sound(HANDOFF), skill.video_use(transcribe) | gates: taste
- excellent: room tone + a single deliberate hit + restraint
- failure: stock-music wallpaper
- learns: sound briefs that worked

## layout_design
- triggers: layout, poster, deck, one-sheet, carousel, design, typography, board
- doctrine loads: `layout_type` | tools: os.adobe_layout, mcp.adobe.render_layout, mcp.figma | gates: os_doctrine:layout_type
- excellent: owned editorial kit, legible, intentional hierarchy, no filler
- failure: template look / illegible / filler slide
- learns: layout grammar that reads premium

## threeD_worldbuilding
- triggers: 3d, blender, substance, sculpt, object, virtual set, plinth, mockup 3d, world, character
- doctrine loads: `world_character` | tools: blender(SANDBOX), substance(HANDOFF), os.crs, os.world | gates: os_world, os_blender_gate
- excellent: ownable mark, cultural specificity, faceless-safe, real geometry
- failure: generic 3D / tourism / unsafe code
- learns: world rules + scene recipes

## strategy
- triggers: strategy, direction, lane, positioning, which, decide, plan
- doctrine loads: `distribution_hook` | tools: claude+os_docs | gates: proof_before_crown
- excellent: proof decides, optionality protected, no lane crowned early
- failure: crowning a lane from a confident doc
- learns: which calls proof later validated

## sales_offer
- triggers: offer, price, pricing, sell, monetize, package the offer
- doctrine loads: `pricing_offer` | tools: os.money_path | gates: os_doctrine:pricing_offer, os_doctrine:trust_sales
- excellent: values not cost, scarcity/anchor, proof before price
- failure: price before demand / cost-plus
- learns: offer shapes that converted

## proof_loop
- triggers: proof, validate, form, signup, demand, test interest
- doctrine loads: `trust_sales` | tools: os.form_ingest, os.form_score, mcp.airtable | gates: keep_kill_scale
- excellent: private, identity-safe, real signal, not validation until shared
- failure: vanity signal / premature scale
- learns: what signal predicted real buyers

## legal_privacy
- triggers: legal, privacy, identity, employer, nda, terms, metadata, leak
- doctrine loads: `safety_identity` | tools: os_privacy_gate, legal_stubs | gates: os_privacy_gate, legal_review_needed
- excellent: no identity leak, faceless-safe, stubs flagged not final
- failure: identity/employer leak / final legal claim
- learns: new banned tokens + leak surfaces

## finance_cost
- triggers: cost, budget, credits, spend, ledger, money tracking
- doctrine loads: `pricing_offer` | tools: os_cost, spend_ledgers | gates: budget_gate
- excellent: every credit logged across both tanks, ceiling respected
- failure: silent spend / fake-free
- learns: cost per output type

## operations
- triggers: operate, readiness, launch check, backup, session, continuity, run the office
- doctrine loads: `safety_identity` | tools: os_launch_check, os_checkpoint, os_boot | gates: launch_readiness
- excellent: safe-to-restart, public actions blocked, danger gaps named
- failure: unsafe state / lost work
- learns: recurring ops gaps

## toolchain
- triggers: tool, connect, wire, mcp, install, activate, route
- doctrine loads: `safety_identity` | tools: os_tool_registry, os_tool_router | gates: capability_proof
- excellent: every tool ACTIVE only with an artifact; input routes
- failure: access called capability
- learns: new tools + statuses

## research_doctrine
- triggers: research, doctrine, book, study, learn from, intel, certify
- doctrine loads: `copy` | tools: os_doctrine, memory, knowledge_base | gates: certification
- excellent: read-whole, certified, distilled to usable doctrine
- failure: read called certified / chunk called coverage
- learns: new doctrine fused into modules

## product_drop
- triggers: drop, print, edition, product, merch, certificate, physical
- doctrine loads: `pricing_offer` | tools: os.adobe_composite, blender(SANDBOX), print_spec | gates: validation_before_manufacture
- excellent: numbered, scarce, analog-premium, validated before a run
- failure: manufacture before demand
- learns: drop mechanics that sold

## client_delivery
- triggers: client, deliver, pitch, present, handoff to a person, sellable
- doctrine loads: `trust_sales` | tools: os.adobe_layout, mcp.adobe.render_layout, local.pdf | gates: hardest_to_say_no, os_privacy_gate
- excellent: premium, hardest to say no to, privacy-clean, no overclaim
- failure: internal scaffolding shown / overclaim
- learns: what a recipient said yes to

## learning_self_improvement
- triggers: learn, improve, failure, lesson, rule, gap, self-correct
- doctrine loads: `safety_identity` | tools: failure_ledger, lessons, next_time_rules | gates: active_standard
- excellent: every failure logged+classified+ruled so it never recurs
- failure: same surprise gap twice
- learns: the rule that prevents recurrence
