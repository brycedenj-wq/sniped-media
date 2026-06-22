---
name: jsonl-validation
description: Validate BATCH_<NNN>_CHUNKS.jsonl against the locked schema. Run BEFORE master-consolidation. Argument is the batch number.
disable-model-invocation: false
---

Validate `01_KNOWLEDGE_BASE/batches/BATCH_$ARGUMENTS_CHUNKS.jsonl`. Run every check. Refuse to pass if any check fails.

```bash
B=$ARGUMENTS
J=~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/BATCH_${B}_CHUNKS.jsonl
E=~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/batch_${B}_extracted

# 1. JSONL parse
jq -c . "$J" > /dev/null || { echo "FAIL: JSONL parse"; exit 1; }

# 2. Required fields per line (chunk_id, batch_id, source_title, source_file, domain, concept, summary, tags)
jq -c 'select(.chunk_id == null or .batch_id == null or .source_title == null or .source_file == null or .domain == null or .concept == null or .summary == null or .tags == null)' "$J" | head -5

# 3. chunk_id uniqueness within the batch
DUPES=$(jq -r '.chunk_id' "$J" | sort | uniq -d)
[ -z "$DUPES" ] || { echo "FAIL: duplicate chunk_id: $DUPES"; exit 1; }

# 4. batch_id consistency · exactly one distinct value
BATCH_COUNT=$(jq -r '.batch_id' "$J" | sort -u | wc -l | tr -d ' ')
[ "$BATCH_COUNT" = "1" ] || { echo "FAIL: multiple batch_id values"; exit 1; }

# 5. source_file resolution · each must exist in extracted/ OR raw/
jq -r '.source_file' "$J" | sort -u | while read -r f; do
  [ -f "$E/$f" ] || [ -f ~/AI-Brain-Refinery/raw/"$f" ] || echo "MISSING SOURCE: $f"
done

# 6. Counts
TOTAL=$(wc -l < "$J" | tr -d ' ')
SOURCES=$(jq -r '.source_file' "$J" | sort -u | wc -l | tr -d ' ')
echo "Chunks: $TOTAL · Unique sources: $SOURCES"
```

For BATCH_002, the schema uses `batch` instead of `batch_id`. Branch on the batch number when running check #2 and #4.

Report PASS or FAIL for each check. If any FAIL, halt. Do NOT proceed to `master-consolidation`.


## Inputs
- Batch number as argument (e.g. '005')
- 01_KNOWLEDGE_BASE/batches/BATCH_<NNN>_CHUNKS.jsonl (the file to validate)
- 01_KNOWLEDGE_BASE/batches/batch_<NNN>_extracted/ directory (for source_file resolution)
- ~/AI-Brain-Refinery/raw/ (fallback path for source_file resolution; note BATCH_002 uses 'batch' not 'batch_id')

## Outputs
- PASS or FAIL report for each of 6 checks: JSONL parse, required fields, chunk_id uniqueness, batch_id consistency, source_file resolution, counts
- On full PASS: 'Chunks: N / Unique sources: M -- all 6 checks passed. Safe to proceed to master-consolidation.'
- On any FAIL: halted report naming the failing check, the offending value(s), and 'Do NOT proceed to master-consolidation.'

## Gates
- JSONL PARSE: every line must parse via 'jq -c .' or FAIL immediately
- REQUIRED FIELDS: chunk_id, batch_id (or 'batch' for BATCH_002), source_title, source_file, domain, concept, summary, tags must be present on every line
- CHUNK_ID UNIQUENESS: no duplicate chunk_id values within the batch
- BATCH_ID CONSISTENCY: exactly one distinct batch_id value across all lines (branch on BATCH_002 schema)
- HALT ON FAIL: if any single check fails, stop -- do not proceed to master-consolidation under any circumstance

## Test
- case: Operator runs jsonl-validation with argument 005. BATCH_005_CHUNKS.jsonl has 47 lines. Skill runs all 6 checks, finds chunk_id 'B005_031' duplicated, reports 'FAIL: duplicate chunk_id: B005_031 -- halted. Do NOT proceed to master-consolidation.' No master files are touched.
- expected failure: BATCH_006_CHUNKS.jsonl does not exist at the expected path. Skill reports: 'FAIL: BATCH_006_CHUNKS.jsonl not found at 01_KNOWLEDGE_BASE/batches/BATCH_006_CHUNKS.jsonl. Cannot validate. Halted.'


## INVOKE WHEN
- Validate BATCH_005 before consolidation
- Run jsonl-validation on the new chunks
- Check the chunk file is clean before I merge it into master
