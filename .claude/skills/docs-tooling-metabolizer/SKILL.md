---
name: docs-tooling-metabolizer
description: Metabolize a non-book backlog (tool docs, MCP docs, transcripts, app notes, video/audio) into the OS ledger-first, grouped by type, banking verified-only with a disposition per source. Use when there is a pile of docs/tooling/transcripts to process, when the operator says "open/drain the docs-tooling ledger" or "metabolize these tool docs/transcripts", or after book canon reaches SCHEDULED=0. Proven 2026-06-21 (50-source program: 1444 already-in-manifest filtered out, 50 new dispositioned). NOT for books (use corpus-wave-runner) or for metabolizing stray code repos (those are OUT of doctrine).
---

# Docs/Tooling Metabolizer

Drain a non-book backlog with the same controller discipline as the book waves, but ledger-FIRST and disposition-oriented. The single biggest failure to avoid is bulk-loading: most candidate files are usually already processed, and stray code repos are not doctrine.

## When to use
A docs/tooling/transcripts backlog; operator says open/drain it; or book canon is done and the non-book sources remain. Pairs with `corpus-wave-runner` and the master controller.

## Inputs required
- The source locations (e.g. the source universe + repo doc folders).
- The manifest (`OS_ENGAGEMENT_MANIFEST.csv`) to cross-reference already-processed sources.

## Steps (executable)
1. **Build the ledger FIRST (do NOT bulk-load):** inventory every candidate non-book source. Cross-reference basenames against the manifest. Separate ALREADY-PROCESSED (skip) from genuinely NEW. Write `DOCS_TOOLING_TRANSCRIPTS_LEDGER.csv` (columns: title, ext, group_dir, type, path, bytes, status, disposition, wave). Group by TYPE (tool_mcp_doc / transcript_video_audio / reference_pdf / project_note / artifact_or_misc).
2. **Scope out non-doctrine:** stray code repos (e.g. a cloned PowerShell/Microsoft source tree, MCP-repo source code: .cs/.ps1/.py/.cpp/.h/.jsx) are NOT doctrine. Flag OUT_OF_SCOPE; never certify them.
3. **Screen (deterministic):** md5 dedup; flag <6000-word fragments; inspect ambiguous outliers before disposition.
4. **Process in waves (one Workflow per group, Sonnet, SEQUENTIAL):** whole-read each doc; emit a tool-doc record (doc_type, what_it_does, capabilities, limits_or_gotchas, applies_in_sniped, disposition, coverage_complete, evidence-quote) -> adversarial verify (judge whether the READER whole-read, not the verifier's own spot-check scope; this exact gate quirk held 12 docs once -> corrected verifier prompt + reran failed-only).
5. **Bank verified-only:** dispositions = tool_doc_bound (real reusable tool/technique doctrine) / reference_active (context-only) / project_note_capsule (project-specific, firewalled from permanent OS) / misclassified_artifact (build output, terms, poster) / duplicate / fragment / EXCEPTION (e.g. video needing transcription under no-spend). Flip the ledger row to TRIAGED + disposition; persist records to `01_KNOWLEDGE_BASE/cert_ledgers/`.
6. **Transcription gate:** video/audio need a transcript to whole-watch. No captions + no Whisper key = transcription needs API spend. Under no-spend, HOLD as TRANSCRIPTION_NEEDED and surface to the operator (key vs EXCEPTION); never force a frames-only sampled judgment.
7. **Reconcile + close:** every row terminal-dispositioned; `os_checkpoint` CLEAN; write `OS_RECEIPT.md` (verify PASS).

## Outputs
`DOCS_TOOLING_TRANSCRIPTS_LEDGER.csv` (all rows terminal), per-type records in cert_ledgers, `OS_RECEIPT.md`.

## Boundaries
No deletion/move/archive/spend/post/publish/generation/client-send. No live tool tests. Code clones never become doctrine. No OS-complete claim until the ledger reconciles. Operator ratifies terminal dispositions (DUPLICATE/EXCEPTION/TRANSCRIPTION_NEEDED) at close.

## Test (paraphrased real task)
"Open the docs/tooling ledger" -> inventoried 1494 candidates, found 1444 already in the manifest, dispositioned the 50 new (20 tool_doc_bound + 12 reference_active + 6 misclassified + 4 project_note_capsule + 2 duplicate + 6 EXCEPTION videos), held PowerShell-master + code OUT of doctrine, receipt verify PASS.
