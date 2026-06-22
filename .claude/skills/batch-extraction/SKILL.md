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


## Inputs
- Batch number as argument (e.g. '005')
- BATCH_<NNN>_PLAN.md in 00_COMMAND_CENTER/ confirming the source-file list
- Source files staged in raw/<path> (do not modify originals)
- Conversion tools on PATH: pandoc, pdftotext, or ebook-convert (for .docx/.epub/.pdf/.mobi/.azw3/.djvu/.rtf)

## Outputs
- 01_KNOWLEDGE_BASE/batches/batch_<NNN>_extracted/ directory (created if absent)
- One .md or .txt file per source, filename normalized to lowercase-snake-case (e.g. copywriters_handbook_bly.md)
- Console summary: source count in, extracted count out, any failures
- Receipt: 'Extraction complete: N of M sources extracted to batch_005_extracted/; 0 failures' (or halted with failure detail)

## Gates
- PLAN CHECK: batch plan must exist and source-file list confirmed before any extraction begins
- NO-OVERWRITE: refuse to overwrite an existing extracted file without explicit operator confirmation
- PARSE GATE: halt and surface to operator if any source file cannot be parsed by the conversion tool
- SEPARATION: do not chunk -- extraction is step 5 only; chunking is a later separate step
- RAW IMMUTABILITY: read from raw/ only, never modify original staged files

## Test
- case: Operator says 'run batch extraction for 005'. Skill reads BATCH_005_PLAN.md, converts each .docx/.pdf/.mobi in raw/ to normalized .md files in 01_KNOWLEDGE_BASE/batches/batch_005_extracted/, prints 'Extraction complete: 12 of 12 sources extracted; 0 failures'. No chunking occurs.
- expected failure: BATCH_005_PLAN.md does not exist in 00_COMMAND_CENTER/: skill halts with 'No batch plan found for BATCH_005 -- cannot confirm source list. Halting.'


## INVOKE WHEN
- Run batch extraction for BATCH_005
- Extract the raw sources into the knowledge base
- Convert and normalize the batch 004 source files
