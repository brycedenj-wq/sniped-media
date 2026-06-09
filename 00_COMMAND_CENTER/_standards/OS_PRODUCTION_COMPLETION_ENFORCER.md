# OS PRODUCTION COMPLETION ENFORCER (LOCKED 2026-06-08)

**The OS cannot say done / final / client-ready / sendable on a production task unless the proof trail exists.** This is the Stop-gate hardening of the activation spine. It makes the OS unable to lie about completion by accident.

## The three parts
1. **`scripts/os_proof_manifest.py`** - the arbiter. Defines per-domain REQUIRED artifacts + gates, reads/writes `PROOF_MANIFEST.json` in a production folder, and `verify`s a claim against reality.
   - `os_proof_manifest.py init <folder> --domain <film|photo|image_design|design|website_build|writing|research> --task "..."`
   - `os_proof_manifest.py verify <folder>` (exit 0 pass / 2 fail, prints what is missing)
   - `os_proof_manifest.py audit [root]` (every manifest, SENDABLE vs BLOCKED)
2. **`scripts/os_stop_check.py`** - the Stop hook. Each turn end: reads the transcript, classifies the user prompt (via the spine), detects completion language in the assistant reply, and if it is a HARD production task with a completion claim, verifies the in-scope `PROOF_MANIFEST.json`. Missing/blocked -> exit 2 (blocks the stop, feeds the reasons back to the model). 3-strike loop guard downgrades to a logged OVERRIDE so the session is never bricked, but the gap is on record.
3. **`PROOF_MANIFEST.json`** - lives in each production folder. Records task_type, activated_standards, files_generated, required_artifacts (filled with paths/desc), required_gates (pass/fail/n-a), scores, known_gaps, send_no_send, last_updated, commit.

## Per-domain required completion (the floor)
- **film/video:** activation_manifest, action_beat_sheet, shot_classification_table, tool_choice_per_shot, watch_pass, hostile_review, rebuild_list, final_export_path, proof_packet, scorecard + gates: watch, hostile_review, story_gate, push_in_law, twelve_axis, owned_music, nine_floor.
- **photo/composite:** composite_master_qa, platform_mastering_if_client, crops_100, before_after_or_proof_sheet, scorecard + gates: vision_reject, composite_qa, skin_identity_drift, subject_identity_untouched.
- **image_design:** composite_master_qa, crops_100, before_after_or_proof_sheet, scorecard + gates: vision_reject, composite_qa, skin_identity_drift, platform_mastering_if_client.
- **design/deck:** intended_audience, slide_page_review, readability_mobile_check, export_path + gates: no_method_leak_if_selling_outcome, brand_consistency.
- **website_build:** build, responsive_check, deploy_path + gates: completion_verification, legal_risk.
- **writing / research / strategy:** SOFT. Gated only if `deliverable_promised=true` in the manifest. Casual writing/brainstorm is never gated.

## Not ceremonial (point 5)
The Stop gate only fires on HARD production domains (film, photo, image_design, design, website_build) AND when completion language is present AND the claim is not explicitly hedged ("not final", "named gap", "proof not final"). Casual/soft work passes silently. The classifier uses word-boundary matching so "thread" never reads as "ad", "credit" never as "edit".

## Proven on real failures (2026-06-08)
- The Door v2 (film) -> BLOCKED: push_in_law fail, owned_music fail, nine_floor fail, scorecard missing, send=no. Correct: not a final film.
- Alma BH v2 ceiling claim (photo) -> BLOCKED: composite_qa fail (heel/100% unresolved), crops_100 + scorecard missing.
- Alma platform masters (image_design) -> SENDABLE, scoped as EXPORT ONLY (the manifest task name states it does not certify the hero as ceiling).
- Drop Engine deck (design) -> BLOCKED: brand_consistency fail (depends on a non-ready hero), send=no -> internal/proof only.
- Live Stop-hook test: false film completion -> exit 2 with reasons; honest "not final, gap named" -> exit 0; casual "done" -> exit 0.

## How to use going forward
On any production task: `os_proof_manifest.py init` the folder at the start, fill artifacts/gates honestly as you go, set `send_no_send=yes` only when verify passes. The Stop hook does the rest: it will not let a completion claim through without it. Composes under [[os-activation-spine]] and [[real-film-production-os]]. Memory: [[production-completion-enforcer]].
