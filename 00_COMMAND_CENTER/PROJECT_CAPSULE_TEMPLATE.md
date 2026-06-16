# PROJECT CAPSULE TEMPLATE

A project capsule holds the temporary truth of ONE project/client. The OS reads it to do the work; it is NOT merged into the permanent OS. Copy this file to the project folder and fill it. Filled capsules live at `00_COMMAND_CENTER/<PROJECT_NAME>/PROJECT_CAPSULE.md` (or the project's own folder), never inside doctrine, memory, the activation index, or the standards.

## Lifecycle
1. Intake messy input -> fill the capsule (`sniped-project-intake` does this).
2. Separate truth from noise (approved truth vs conflicting/unusable notes).
3. The OS uses the capsule as project truth through the runtime contract (see `OS_RUNTIME_CONTRACT.md`).
4. On project end, archive the capsule with the project. Do NOT fold its facts into the permanent OS unless a fact is GENERAL (true for any client) and passes the doctrine proof bar.

---

## CAPSULE (copy below, fill per project)

```
PROJECT_CAPSULE v1
- project_name:
- client_brand:
- objective:                # the one outcome that defines success
- deliverable:              # exact format(s) + spec (aspect, length, count)
- deadline:                 # absolute date/time, not "soon"
- approved_truth:           # facts confirmed by the client/operator (locked)
- product_asset_truth:      # exact product/SKU/identity facts + real reference files (paths)
- taste_references:         # links/files the client approves as the taste target
- client_notes:             # raw notes as given
- conflicting_notes:        # notes that contradict each other or the doctrine (flag, do not silently pick)
- usable_assets:            # files verified present + usable (paths; mark "inspected" only if actually opened)
- unusable_assets:          # present-but-rejected (with reason)
- assumptions:              # what the OS is assuming in the absence of confirmation
- risks:                    # what could break the deliverable
- human_input_required:     # the specific facts/files/decisions only the human can supply
- external_check_required:  # current tool limits/credits/APIs to verify before spend
- approval_status:          # draft | internal | operator-approved | client-approved
- send_no_send:             # NO-SEND by default until proof + approval
```

## Rules
- **NO-SEND / NOT client-ready by default** until the proof gate passes (PROOF_MANIFEST + OS_RECEIPT) and `send_no_send` is set yes by the operator.
- **Do not invent product/identity/taste facts.** If `product_asset_truth` is empty, it is HUMAN-INPUT REQUIRED and gates any garment/identity/brand-bearing work.
- **Do not claim an asset was inspected** unless a file was actually opened; list paths and mark inspected/uninspected honestly.
- **Conflicting notes are surfaced, not resolved silently.** Flag the conflict and ask, or state the assumption.
- **Project facts never write to the permanent OS.** The capsule is the boundary that keeps the OS general and uncontaminated.
