# OS FAILURE LEDGER , Overnight Sprint 001
> Every failure/gap caught, classified, fixed-or-queued, with the rule that prevents recurrence.

| # | failure | class | root cause | fix | status | rule added |
|---|---|---|---|---|---|---|
| F1 | Adobe MCP rejected the Higgsfield cloudfront URL | integration | Adobe only accepts assets in its own trusted storage | upload via asset handshake OR mark Adobe-MAX AMBER-needs-upload | FIXED | R1: upload to Adobe storage via os_adobe_cloud handshake first, then call image tools |
| F2 | DEED poster showed "THE ESTATE OF HER" + LOT 00 logline | content-bleed | os_adobe_layout.poster HARD-CODED the subtitle; os_engine did not override poster_logline/footer/carousel from the world | parameterize poster tagline; os_engine overrides all world-text fields | FIXED | R2: no layout function may hard-code world copy; all world text flows from the world JSON |
| F3 | os_engine money low_legal_risk=0 by default | safety-correct | legal review genuinely pending | keep 0 until legal pass (correct, not a bug) | ACCEPTED | R3: legal risk stays flagged until a real legal pass |
| F4 | os_engine crashed: File name too long | variable-shadow | local `money` clobbered the `money` param (money.json path) | renamed local to money_angle | FIXED | R4: never reuse a parameter name as a local; lint for shadowing |

## PRIME MOVER RUN (2026-06-05)
| # | failure | class | fix | status | rule |
|---|---|---|---|---|---|
| F5 | `timeout` cmd not found (macOS) on HyperFrames init | tooling | use the Bash tool timeout param / gtimeout, not shell `timeout` | FIXED | R11: do not assume GNU coreutils on macOS |
| F6 | Figma MCP route times out with nothing selected | integration | needs a frame selected in a /design/ file | QUEUED | R12: Figma route requires an explicit node selection |
| F7 | HyperFrames warned: 'Didot' not in deterministic font list | cosmetic | fell back + rendered; map font or @font-face for determinism | ACCEPTED | R13: register fonts for deterministic renders |
