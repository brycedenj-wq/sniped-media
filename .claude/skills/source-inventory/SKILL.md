---
name: source-inventory
description: Inventory a named source folder against raw/ and the chunked corpus. Produces a 00_COMMAND_CENTER/*_FULL_SOURCE_INVENTORY_<date>.md report. Always count before assuming.
disable-model-invocation: false
---

Inventory the named source folder (default: `~/Downloads/    SNIPED_OS/`) and produce a Markdown report. Do not move, copy, or modify any file.

1. Confirm the source path. Quote it if it contains spaces (the SNIPED_OS folder has 4 leading spaces).
2. Count total files (excluding `.DS_Store`), total directories, total size.
3. Extension breakdown (top 20 by count).
4. Top-level subdir tree with per-chapter file counts + sizes.
5. List all archives (zip, rar, 7z, tar, gz). For each, run `unzip -l` or `tar tf` without extracting. Note misextensioned archives (e.g., a .rar that is actually a zip-EPUB).
6. Basename diff vs `~/AI-Brain-Refinery/raw/` using `comm -23` on sorted unique basename lists. Use `sed 's|.*/||'` not `xargs basename` (xargs drops brackets and apostrophes silently).
7. Basename diff vs the chunked corpus: extract `source_file` values from `01_KNOWLEDGE_BASE/batches/BATCH_*.jsonl` and cross-reference.
8. Flag: stale `~$` lock files, `.part` incomplete downloads, superseded artifacts, side-quest folders, installers (`.dmg`), internal duplicates within the source folder.
9. Write the report to `00_COMMAND_CENTER/<SOURCE-NAME>_FULL_SOURCE_INVENTORY_<YYYY-MM-DD>.md`.

Write Markdown only. No file copies. No master-file updates.


## INVOKE WHEN
- Inventory the source folder before starting a new batch
- What files are in SNIPED_OS that haven't been staged yet?
- Run a source inventory on the downloads folder

## Inputs
- Source folder path (default: ~/Downloads/    SNIPED_OS/ -- 4 leading spaces, must be quoted in shell)
- ~/AI-Brain-Refinery/raw/ for basename diff via comm -23
- 01_KNOWLEDGE_BASE/batches/BATCH_*.jsonl for source_file cross-reference

## Outputs
- 00_COMMAND_CENTER/<SOURCE-NAME>_FULL_SOURCE_INVENTORY_<YYYY-MM-DD>.md containing: total file/dir/size counts, extension breakdown (top 20), top-level subdir tree with per-chapter counts+sizes, archive listings (unzip -l / tar tf without extraction), basename diff vs raw/, basename diff vs chunked corpus, and flagged anomalies (stale lock files, .part fragments, .dmg installers, internal duplicates, superseded artifacts, side-quest folders)

## Gates
- .DS_Store files excluded from all counts before any number is reported
- Basename diffs use sed 's|.*/||' not xargs basename (xargs silently drops brackets and apostrophes)
- Archives are listed (unzip -l / tar tf) but never extracted
- No file is moved, copied, or modified -- report is write-only output
- Source path is confirmed and quoted before any shell command runs

## Test
- case: Operator says 'run a source inventory on ~/Downloads/    SNIPED_OS/ before BATCH_006.' Expected output: a dated .md report at 00_COMMAND_CENTER/SNIPED_OS_FULL_SOURCE_INVENTORY_2026-06-21.md listing total file count (DS_Store excluded), extension breakdown, per-chapter subdir tree, any archives with their contents listed (not extracted), a comm -23 basename diff showing which files are not yet in raw/, and a cross-ref showing which are not yet in any BATCH_*.jsonl source_file field.
- expected failure: Source path is provided but does not exist on disk (e.g., trailing space dropped from folder name): skill must halt, surface the path error, and not write any report.
