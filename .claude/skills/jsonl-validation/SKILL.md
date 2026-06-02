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
