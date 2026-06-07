# GEMINI USAGE POLICY

Binding guardrails for the Gemini CLI second-model lane. Locked 2026-06-07. See [[OS_SECOND_MODEL_LANE_STANDARD]] + [[OS_GEMINI_CLI_INTEGRATION_AUDIT]].

## Invocation (the ONLY sanctioned form)
```
gemini -p "<prompt>" --output-format json     # run from the repo root, read-only
```
- Always `--output-format json`. Always non-interactive (`-p`). Never hand Gemini an edit/approval loop.
- The wrapper `os_gemini_review.py` verifies `stats.tools.totalCalls == 0` and flags any run that isn't clean.
- ripgrep (`rg`) must be present (Gemini uses it for repo search). Confirmed 15.1.0.

## Read-only, always
Gemini reviews. It does NOT write, edit, move, delete, or render. If a run shows tool calls > 0, treat the output as suspect and re-run with a stricter prompt.

## Privacy gate FIRST
- Do NOT point Gemini at private/client folders, raw client trees, identity files, secrets, `.git`, `node_modules`, or credentials.
- Reviews run on **de-identified bundles** (contact sheet + timestamped frames + EDL + notes), not raw client material.
- Client name / operator identity stays out of the bundle unless the operator explicitly clears it. Scrub before bundling.

## Authority limits
- Gemini is a critic, never the source of truth.
- Gemini does NOT crown anything final, does NOT make client-delivery / posting / payment / hosting decisions.
- Gemini notes are adopted only after Claude's evidence reconciliation (accept / partial / reject). Brief-contradicting notes are rejected with a reason.

## Cost / runaway
- One review job = one (or few) `gemini -p` calls. No loops, no unattended fan-out.
- Keep bundles tight; do not dump the whole repo into a prompt.

## What Gemini is good for here
Hostile cut critique, contact-sheet review, EDL/selects/structure review, "what are we missing", settling-check, brief/doctrine comparison, read-only code/folder review.

## What Gemini is NOT for
Editing, building, deciding delivery, holding the canon, or overriding verified footage / locked creative without evidence. No em-dashes in any artifact Gemini work feeds into.
