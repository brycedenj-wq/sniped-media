---
name: batch-extraction
description: Extract normalized source files for BATCH_<NNN> from raw/ into 01_KNOWLEDGE_BASE/batches/batch_<NNN>_extracted/. Argument is the batch number.
disable-model-invocation: false
---

Extract source files for the batch identified by `$ARGUMENTS` (e.g., `005`).

1. Read the BATCH plan from `00_COMMAND_CENTER/` if one exists (`BATCH_<NNN>_PLAN.md`). Confirm the source-file list.
2. Mirror the pattern from `scripts/extract_batch_002.py`, `extract_batch_003.py`, `extract_batch_004.py`. Each existing script handles its batch's source-folder-to-extract mapping.
3. Create `01_KNOWLEDGE_BASE/batches/batch_$ARGUMENTS_extracted/` if it does not exist.
4. For each source in the batch plan:
   - Read from `raw/<path>` (do not modify the original).
   - Convert to plain text where the source is `.docx`, `.epub`, `.pdf`, `.mobi`, `.azw3`, `.djvu`, `.rtf`. Use `pandoc`, `pdftotext`, or `ebook-convert` as appropriate.
   - Normalize the filename to lowercase-snake-case (e.g., `Robert W. Bly - The copywriter's handbook.mobi` → `copywriters_handbook_bly.md`).
   - Write the extracted text to `01_KNOWLEDGE_BASE/batches/batch_$ARGUMENTS_extracted/<normalized-name>.md` or `.txt`.
5. Refuse to overwrite an existing extracted file without explicit operator confirmation.
6. Print a summary: source count in, extracted count out, any failures.
7. Do NOT chunk. Extraction is a separate step from chunking.

Halt and surface to the operator if any source file cannot be parsed.
