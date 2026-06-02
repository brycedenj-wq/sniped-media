# STEP 005 · Build Master Index

Goal:
Merge BATCH_001 and BATCH_002 awareness into one command-center view so the system knows what knowledge exists, where it lives, and what to retrieve from.

Inputs:
- 01_KNOWLEDGE_BASE/batches/BATCH_001_CHUNKS.jsonl
- 01_KNOWLEDGE_BASE/batches/BATCH_002_CHUNKS.jsonl
- 01_KNOWLEDGE_BASE/summaries/BATCH_001_SUMMARY.md
- 01_KNOWLEDGE_BASE/summaries/BATCH_002_SUMMARY.md
- 01_KNOWLEDGE_BASE/indexes/BATCH_001_SOURCE_INDEX.md
- 01_KNOWLEDGE_BASE/indexes/BATCH_002_SOURCE_INDEX.md

Outputs:
- 01_KNOWLEDGE_BASE/MASTER_INDEX.md
- 01_KNOWLEDGE_BASE/MASTER_CHUNK_MAP.json
- 00_COMMAND_CENTER/ACTIVE_KNOWLEDGE_STATE.md

Instructions:
1. Read both batch summaries.
2. Read both source indexes.
3. Inspect the first 10 and last 10 chunks from each JSONL.
4. Create a MASTER_INDEX.md that explains:
   - what Batch 001 contains
   - what Batch 002 contains
   - highest-value concepts
   - source families
   - domains
   - conflicts or doctrine updates
   - what should be retrieved for strategy, brand, operations, AI tools, pricing, outreach, content, leadership, power, and systems
5. Create MASTER_CHUNK_MAP.json with:
   - batch_id
   - chunk_count
   - source_files
   - domains
   - primary_use_cases
   - retrieval_notes
6. Create ACTIVE_KNOWLEDGE_STATE.md that tells the next AI agent:
   - what has already been processed
   - what is canon
   - what is stale or overridden
   - what not to reprocess
   - what batch should come next

Do not invent sources.
Do not summarize vaguely.
Do not overwrite the existing batch files.
