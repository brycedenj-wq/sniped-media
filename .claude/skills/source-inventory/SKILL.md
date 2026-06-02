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
