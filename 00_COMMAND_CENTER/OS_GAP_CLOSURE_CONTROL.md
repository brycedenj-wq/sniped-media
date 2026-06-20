# OS GAP CLOSURE CONTROL

**Opened:** 2026-06-19  
**Reason:** Operator called out that the OS cannot remain a pile of half-unlocked docs, provisional books, stale dashboards, and unbound field manuals. This file is the closure board until the OS is verified, active, and improving as one body.

## Non-negotiable definition of done

A source is not done because it exists, got chunked, or appeared in a transcript summary. It is done only when it passes all five gates:

1. **Coverage:** whole-read or segment-ledger coverage proves beginning, middle, and end were read.
2. **Distillation:** the signal became doctrine, an operating rule, a skill, a gate, a tool route, a technique card, or a confidence-labeled knowledge atom.
3. **Activation:** future tasks can retrieve it through a router, library, skill, field manual, graph node, or dashboard without the operator reminding the agent.
4. **Verification:** a fresh pass can trace the claim back to source and find no false completion.
5. **State binding:** the relevant dashboard, manifest, ledger, or current-state pointer knows it exists.

If any gate is missing, the source is not fully unlocked.

## Current live accounting

From `python3 00_COMMAND_CENTER/scripts/os_checkpoint.py --write`, run 2026-06-19:

| Bucket | Count | Meaning |
|---|---:|---|
| Total source rows | 1,260 | Current manifest source universe after duplicate and derivative correction |
| Read verified | 910 | Segment/coverage proven enough to trust as verified |
| Coverage proven via Start Here | 5 | Covered through the Start Here certification path |
| Provisional chunked, not certified | 300 | Usable only with a provisional label |
| Needs OCR | 34 | Not unlocked until OCR pass |
| Needs visual review | 5 | Meaning is visual/table/image dependent |
| Needs transcription | 1 | Media source requires transcript |
| Not read | 2 | Source rows not attempted |
| Duplicates | 3 | Excluded from source truth |

## Activation state

| Layer | Status | Gap |
|---|---|---|
| Engagement manifest | CLEAN | POST WAVE 001+001-B: 953 verified (75.6%), 297 provisional, 0 unresolved (the 42 finite rows are closed: 40 read + 2 exceptions), 3 duplicate. Pending pile = 0. |
| Engagement dashboard | Reconciled with live checkpoint | Legacy inventory text still needs a full rebuild |
| Start Here operationalization | 97 docs converted, 0 USE docs without cards, 1,026 callable cards | 6 queued docs need routing decisions or small fold-in passes |
| Creator AI Production Field Manual | Exists with OS_RECEIPT PASS | Not yet bound into routing, SREF library, AI-film lane, or field-manual index |
| Corpus fusion map | 0 family/atom orphans in current fusion layer | Counts are older than the latest checkpoint and need regeneration after certification cleanup |
| Book layer | Large provisional pile | Promote high-use books from provisional to certified with segment ledgers, not reread everything blindly |

## Queue order

1. **Close the tiny hard gaps first:** 2 not-read files, 1 transcription, 5 visual reviews, 34 OCR. These are finite and should go to zero.
2. **Bind the new field manual:** Creator AI Production Field Manual must be routed into SREF use, AI production methods, field manual index, and relevant project loaders.
3. **Promote the 300 provisional sources:** certify by value and usage, not by panic. High-use books and frequently cited families first.
4. **Rebuild stale dashboards:** dashboard text should match the live manifest and not carry older contradictory totals.
5. **Run adversarial verification at the end of each wave:** no source graduates on self-report.

## Immediate next harness

**Harness name:** OS Gap Closure Wave 001  
**Budget shape:** local audit first, no external spend, no generation, no posting.  
**Target:** the 42 finite unresolved source rows plus the 6 queued Start Here docs.  
**Outputs required:**

- Updated manifest statuses.
- Updated dashboard counts.
- A delta report of what became active behavior.
- A list of sources that remain blocked and exactly why.
- An OS_RECEIPT with verdict `internal`.

## Field manual binding checklist

The `CREATOR_AI_PRODUCTION_FIELD_MANUAL` folder is useful, but not fully active until these are done:

- Add it to the OS field-manual index.
- Extract the exact SREF table into an active SREF reference used by image/world workflows.
- Add routing notes from AI production methods into video, world-build, and motion project loaders.
- Decide whether any section becomes technique cards, and if not, record why it stays reference-only.
- Add a stale-tool warning gate for scrape-dated tools.

## Source retirement gate

The operator wants freedom to delete or offload source clutter once the OS has actually absorbed it. That is valid, but source deletion needs a stricter gate than normal OS activation.

No original doc, book, PDF, transcript, image, or app-export source may be deleted until it has a **SOURCE_RETIREMENT_RECEIPT** proving:

1. **Identity preserved:** original path, file name, size, md5, source class, and source date are recorded.
2. **Coverage proven:** the source is `read_verified`, `coverage_proven_via_starthere`, or otherwise certified with a segment ledger. Provisional, pending OCR, pending visual review, pending transcription, and not-read sources fail.
3. **Signal extracted:** the useful content exists in active OS form: doctrine, field manual, card, skill, gate, route, graph node, or memory atom.
4. **Retrieval tested:** a fresh task can retrieve and use the extracted content without opening the original source.
5. **Backup path chosen:** before deletion, either keep one cold archive copy or intentionally mark the source as disposable because the derived OS artifacts are sufficient. Default is cold archive, not deletion.
6. **Operator approval:** deletion or offloading requires explicit operator go. Planning sessions may recommend, never delete.

Practical rule: first goal is **source independence**, not deletion. Once a source passes the retirement gate, the Mac can be cleaned by moving originals into cold storage, external drive, cloud archive, or a deletion queue. Until then, the source stays.

Recommended retirement states:

| State | Meaning | Mac action |
|---|---|---|
| `KEEP_ACTIVE_SOURCE` | Still needed for current work or legal/source fidelity | Keep in place |
| `COLD_ARCHIVE_OK` | OS can operate without it, but original should be preserved | Move to cold archive after approval |
| `DELETE_ELIGIBLE` | Duplicate, corrupted, superseded, or fully replaceable after receipt | Delete only after approval |
| `DO_NOT_DELETE` | Client/legal/original-media/source-of-record | Preserve |

Wave 001 should produce a source-retirement pilot for the 6 queued Start Here docs and any duplicates it encounters. Do not delete anything during Wave 001.

## Standing rule

No future agent may answer “the OS used everything” unless it can name:

- which verified sources were activated,
- which provisional sources were labeled provisional,
- which pending sources were excluded,
- and which gate checked the answer.

Anything less is performance, not operating intelligence.
