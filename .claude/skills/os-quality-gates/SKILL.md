---
name: os-quality-gates
description: The 11 quality gates that keep Bryce's OS from drifting, hallucinating, over-anchoring to old docs, crowning a direction too early, exposing identity/employer, or falsely claiming completion. Run the relevant gate(s) before declaring any answer or build "done." Use whenever finishing a strategy answer, a build, a research finding, a coverage claim, or any external-facing output.
---

# OS Quality Gates

Run the gate(s) for the active mode before completion. Each gate is a pass/fail check; a fail blocks "done" until fixed.

## The 11 gates
1. **Anti-hallucination** , every factual/strategic claim cites a verified source OR is labeled inference. Uncited claim = FAIL. (Research, Critique, Strategy.)
2. **Anti-old-lane anchoring** , old offer/lane/direction names are tagged `[old/evidence-only]`; granting an old doc authority = FAIL. (Strategy.)
3. **Optionality protection** , lanes/identity stay open absent explicit proof + operator decision; collapsing optionality = FAIL. (Strategy, Decision.)
4. **Proof-before-crowning** , no lane/identity/throne crowned without current proof. "The answer is X" sans proof = FAIL. (Strategy.)
5. **Legal / ethical risk** , scan for employer data/relationships, celebrity likeness, IP assignment, platform ToS. Exposure = FLAG + may refuse/redirect. (Every build/output.)
6. **Employer-conflict** , employer-adjacent positioning, company time/tools/data, identity-exposing public association with the day job = FAIL. (Every off-grid build.)
7. **Output-usefulness** , does it advance state / can the operator act now. Vague = FAIL. (Every deliverable.)
8. **Completion-verification** , the manifest/coverage proves done (got==total, fail==0). "Conversion returned text" / "workflow completed" != done. Unproven = FAIL. (Every "done.")
9. **Source-freshness** , market/factual claims dated + current; stale-as-current = FAIL. (Research, Strategy.)
10. **Cost / runaway** , run sized to budget + session window; concurrent waves or unbounded swarm = FAIL. (Before any workflow.)
11. **Identity-collapse** , Bryce stays the operator/possibility engine; reducing him to one output (photographer/consultant/clothing/etc.) = FAIL. (Strategy, Writing.)

## How to apply
- The router (`os-command-router`) names which gates are the exit gates for the mode.
- Run them; if any fails, fix and re-run; only then declare done.
- Log a gate failure that recurs as an error-dashboard entry (a recurring failure = a process bug to fix).

## Pairs with
`os-command-router`, `os-token-safe-reader`, `OS_SELF_OPTIMIZATION_ARCHITECTURE.md` Section 9, and memory rules: extraction-audit-gate (gate 8), full-engagement-before-direction (gates 2/4), possibility-engine-optionality (gates 3/11), payment-follows-proof, name-availability-gate (gate 5 for brand names).


## Inputs
- The completed answer, build, coverage claim, or external-facing output to gate-check
- The active mode (from os-command-router routing receipt) to know which subset of the 11 gates apply
- The manifest or proof artifact for gate 8 (completion-verification)

## Outputs
- Pass/fail result for each relevant gate, with the specific failure reason if any gate fails
- Fixed output after any gate-fail is resolved
- Gate-failure log entry if the same gate fails recurrently (marks a process bug)
- Receipt: 'Gates run: [list] · All pass' OR 'Gate <N> FAIL: <reason> · blocked until fixed'

## Gates
- Gate 1 Anti-hallucination: every factual/strategic claim cites a verified source or is labeled inference -- uncited claim = FAIL
- Gate 4 Proof-before-crowning: no lane/identity/direction crowned without current proof -- 'the answer is X' without proof = FAIL
- Gate 8 Completion-verification: got==total, fail==0 from manifest/coverage proof -- 'workflow completed' without proof = FAIL
- Gate 5 Legal/ethical risk: scan for employer data, celebrity likeness, IP, ToS exposure -- exposure = FLAG and may refuse
- Gate 11 Identity-collapse: Bryce stays operator/possibility engine -- reducing him to one output type = FAIL

## Test
- case: After a strategy session on which lane to pursue, the assistant declares 'AI brand campaigns is clearly your primary lane.' OS-quality-gates runs Gate 4 (proof-before-crowning) and Gate 11 (identity-collapse). Both fail: no current proof exists for the crowning, and reducing Bryce to one output lane collapses optionality. Output is blocked. Assistant reverts to: 'AI brand campaigns is a strong candidate -- here is the proof move to test it before committing.'
- expected failure: Operator tries to skip quality gates on a client-facing deliverable with 'just send it.' Skill refuses to mark done: 'Gate 8 (completion-verification) and Gate 5 (legal/ethical) have not been run. Cannot declare done without a gate pass. Run the relevant gates first.'


## INVOKE WHEN
- finishing a strategy answer or build before declaring done
- any external-facing output before it ships
- a coverage or completion claim that needs verification
