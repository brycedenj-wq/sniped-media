# MASTER_OS_CONDUCTOR (LOCKED 2026-06-08)

The layer above the activation spine, skill registry, proof manifest, and stop gate. Its job: make the OS behave like **one intelligence**, not a folder of disconnected resources. It guarantees the whole 78-skill body is CONSIDERED on every serious task, the relevant skills are activated and integrated, omitted ones are named, and the output proves activation changed it.

This is the answer to "did you use the whole OS?" The OS now shows that, automatically, every serious task.

## The 12 questions the conductor answers every time
1. What type of task is this? 2. What outcome am I creating? 3. What domains are involved? 4. Which of the 78 skills are relevant? 5. Which are active now? 6. Which reference skills should be consulted? 7. Which docs/books/frameworks matter? 8. What standards/gates apply? 9. What toolchain is required? 10. What makes the result excellent? 11. What makes it fail? 12. What proof must exist before done?

## Three layers

### LAYER 1 - WHOLE-OS SCAN (before work, mandatory on serious tasks)
The activation injector (`os_activate.py`, fired by the UserPromptSubmit hook) already emits the scan every turn: task type, domains detected, active skills, reference skills, standards, gates, omitted-and-why, known gaps, toolchain. On a SERIOUS task it adds the CONDUCTOR block: scan the full registry, the CROSS-DOMAIN PULL, MAX mode, and the receipt requirement. This is concise but mandatory.

### LAYER 2 - DEEP SYNTHESIS (serious / high-stakes / client-facing)
Do not just activate the obvious domain. Pull cross-domain intelligence and integrate what changes the output. The `cross_domain` map in `OS_ACTIVATION_INDEX.json` defines it per domain:
- **Film/video** also pulls writing(story/copy), editing/retouch, brand, QA, strategy(audience/offer) + toolchain.
- **Photo/composite** also pulls editing/retouch, brand, writing, QA, ops(client comms).
- **Brand/campaign** also pulls writing, strategy, pricing, film, QA.
- **Web/build** also pulls writing, brand, strategy, pricing, QA.
- **Strategy** also pulls pricing, research, writing, ops.
Resolve conflicts by the authority hierarchy (REAL_FILM_PRODUCTION_OS > AI_CINEMA > HIGGSFIELD/FINISHING > skills > benchmarks). Synthesize the best output from the union, not the loudest single skill.

### LAYER 3 - PROOF + STOP
Before saying anything is finished, the conductor requires `OS_RECEIPT.md` (via `os_receipt.py`) proving: what the OS used, what it ignored + why, **what CHANGED because the activated skills ran**, gates passed/failed, remaining blockers, honest rating + why, what blocks 10/10, and the verdict (sendable/internal/proof/draft/blocked). The Stop gate (`os_stop_check.py`) blocks completion of serious work without a verified receipt.

## The new law
**"Relevant activation" is not enough. The OS must prove that activation CHANGED the output.** A skill that touched nothing was not used. The receipt's "what changed" section is the proof.

## What counts as a serious task
Matches a hard production domain (film, photo, editing, brand, web), OR matches >=2 domains, OR contains a serious keyword (whole os, max, flagship, client deliverable, launch, campaign, build the, the best, 10/10, go all out). Serious tasks default to MAX_CAPABILITY_MODE.

## Standard
10/10 is the target. 9 is the floor, not the goal. If 10/10 is blocked, the receipt NAMES the blocker and the path to remove it. Emergency cuts scope, never quality/taste/review.

## Files
`os_activate.py` (scan + conductor block), `os_receipt.py` (receipt), `os_proof_manifest.py` (production proof), `os_stop_check.py` (enforcement), `OS_ACTIVATION_INDEX.json` (registry + cross_domain + serious signals). Companions: `MAX_CAPABILITY_MODE.md`, `OS_INPUT_PROTOCOL_FOR_BJ.md`. Memory: [[master-os-conductor]].
