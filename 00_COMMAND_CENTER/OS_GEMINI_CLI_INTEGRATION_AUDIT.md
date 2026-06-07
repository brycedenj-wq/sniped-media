# OS GEMINI CLI — INTEGRATION AUDIT

Audited + wired 2026-06-07. Gemini is the OS's **second-model critique lane**: a hostile reviewer / second set of eyes / commercial-grade quality gate. It is NOT a builder, NOT a source of truth.

## Install proof
- `which gemini` → `/opt/homebrew/bin/gemini`
- `gemini --version` → `0.45.2`
- `rg --version` → `ripgrep 15.1.0`
- Model in use: `gemini-3-flash-preview` (multimodal, large context).

## Read-only proof (this session)
- Smoke test: `gemini -p "..." --output-format json` → returned `{session_id, response, stats}`; `stats.tools.totalCalls = 0` (no tool/edit calls).
- Alma review run: `stats.tools.totalCalls = 0`, exit 0, zero file edits. Prior operator test also showed `totalLinesAdded:0 / totalLinesRemoved:0`.
- **Conclusion:** `gemini -p ... --output-format json` is a clean, non-interactive, read-only invocation. No edit-approval path is exercised. The wrapper (`os_gemini_review.py`) verifies `totalCalls==0` on every run and flags otherwise.

## Output schema (wrapper-relevant)
```
{ "session_id": str, "response": str, "stats": { "models": {...}, "tools": {"totalCalls": int, ...} } }
```
The critique lives in `response` (we prompt for strict JSON inside it). `stats.tools.totalCalls` is the read-only proof.

## What was wired
- `scripts/os_gemini_review.py` — bundle builder (contact sheet) + read-only runner (saves `.json` + `.md`, verifies 0 edits).
- `scripts/os_second_model_gate.py` — reconciliation gate (Gemini note → evidence check → accept/reject/partial → V5 action).
- `00_COMMAND_CENTER/SECOND_MODEL_REVIEWS/` — review artifacts home.
- `OS_SECOND_MODEL_LANE_STANDARD.md`, `GEMINI_USAGE_POLICY.md` — doctrine + guardrails.
- Tool registry, one-command layer, source router, session log — updated (see those files).

## Security / scope posture
- Gemini runs in the repo working dir, read-only. It can read code/folders we point it at.
- **Privacy gate FIRST** before any private/client folder is exposed to Gemini (see policy). Default review inputs are de-identified bundles, not raw client trees.
- No network publish, no payments, no delivery decisions through Gemini.

## First real use
Alma Love V4.2 hero review → `SECOND_MODEL_REVIEWS/ALMA_GEMINI_REVIEW_001.*` → reconciled into `FINISHING_PASS_001/ALMA_V5_REPAIR_PLAN_FROM_GEMINI.md`. Gemini scored 4.2/10; two evidence-backed catches (over-long gag, uncertified plate) accepted into V5; three non-evidence notes rejected.
