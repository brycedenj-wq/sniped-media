# OS RUNTIME CONTRACT

The permanent operating body. One general OS that handles any project, any client, any task. This contract is domain-agnostic and already enforced by the live runtime (the UserPromptSubmit activation hook `os_gate_injector.py` -> `os_activate.py`, the MAX MODE conductor block, the Stop hook `os_stop_check.py`, and `os_proof_manifest.py` / `os_receipt.py`). This doc states the contract those parts implement so it can be audited and held.

## The contract: for any serious task, the OS must
1. **Classify** the task and domain (os_activate.classify).
2. **Surface doctrine/source packs** for that domain (os_doctrine packs auto-inject; certified sources cited).
3. **Surface relevant skills and workflows** (SKILLS / REFERENCE / WORKFLOWS lines).
4. **Identify required inputs**, and mark what is missing as HUMAN-INPUT REQUIRED.
5. **Choose an execution path** (the domain PIPELINE, the named skill, or a Workflow with role-scoped agents).
6. **Produce the required output format** for that lane (the lane's defined deliverable shape).
7. **Run proof / QA** (the lane's gates + adversarial-verify before crowning).
8. **Name human-input boundaries** (taste, priority, money facts, real assets, send approval).
9. **Refuse false completion** (no done/final/client-ready without PROOF_MANIFEST + OS_RECEIPT; Stop gate enforces).
10. **Produce the next action** (the concrete next step, not vibes).

## Applies across all lanes
film · story/concept · short-form · brand/campaign · copy · web · offer/pricing · strategy · app/software · QA/proof · client deliverables · source/library use. Each lane already has an activation trigger, a doctrine/source connection, an executable skill or workflow, an output format, a QA/proof gate, and a human-input boundary (see the execution-coverage audit, commit 2b3441e).

## Contamination boundary (the law that keeps the OS general)
- **Permanent OS** = doctrine packs (`os_doctrine.py`), memory, `OS_ACTIVATION_INDEX.json`, the standards docs, skills, workflows. These hold only GENERAL laws true across clients.
- **Project truth** = a PROJECT CAPSULE (see `PROJECT_CAPSULE_TEMPLATE.md`), lives in the project folder, is temporary, and is used by the OS but NOT merged into the permanent OS.
- A fact graduates from a capsule into the permanent OS ONLY if it is general (true for any client) and passes the same proof bar as any doctrine change. The Kling/Omni full-clip swap law graduated (general). A client's exact product color, identity, or taste note does NOT graduate; it stays in the capsule.
- Default: project facts stay in the capsule. When in doubt, do not write to the permanent OS.

## How a task runs end to end
intake (build/load the project capsule via `sniped-project-intake`) -> the 10-step contract above -> deliverable -> proof/QA -> next action. The capsule supplies the project truth the contract needs at steps 4-8 without polluting steps 2-3 (the permanent doctrine/source layer).
