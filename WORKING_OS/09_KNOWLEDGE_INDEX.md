# 09_KNOWLEDGE_INDEX · the retrieval index and query guide

How to query the brain without dumping it. There are TWO indexes, by design (corrected per the 2026-06-14 audit). Use the right one.

## The chunk retrieval index (Refinery, canonical)
- `/Users/sniper/AI-Brain-Refinery/01_KNOWLEDGE_BASE/MASTER_INDEX.md`: the narrative landscape (read first for the map).
- `/Users/sniper/AI-Brain-Refinery/01_KNOWLEDGE_BASE/MASTER_CHUNK_MAP.json`: the retrieval index. About 1,879 chunks, 57 batches, 62 domains. Written only by /master-consolidation; never hand-edited.

## The file-location index (SNIPED_OS, second index, real)
- `SNIPED_OS/00_BRIEF/CANONICAL_SOURCE_MAP.md` (canonical) and `SNIPED_OS/99_VAULT/_corpus_inventory/access_layer/CANONICAL_SOURCE_MAP.md` (second copy). Use it to find WHERE a topic lives when it is not yet chunked. Reconciliation of the two copies is deferred pending the SNIPED-vs-BASEPLATE decision. (The earlier claim that this index did not exist was wrong; it exists in two copies.)

## Query strategy
1. Search MASTER_CHUNK_MAP.json first for chunked knowledge.
2. If the topic is not chunked, consult CANONICAL_SOURCE_MAP.md for the source-file location.
3. The 3 supplemental batches below are NOT yet queryable via MASTER_CHUNK_MAP (see status).

## PENDING: 3 unconsolidated batches (~42 chunks, invisible until consolidated)
Staged at `SNIPED_OS/99_VAULT/_corpus_inventory/supplemental_chunks_staging/`:
- DECISION_SYSTEMS_CHUNKS.jsonl
- LEADERSHIP_SUPPLEMENTAL_CHUNKS.jsonl
- TOOLCHAIN_DISTRIBUTION_CHUNKS.jsonl
They are staged but not consolidated into MASTER_INDEX, so a query will miss them. Phase 2 runs /jsonl-validation then /master-consolidation to fold them in.

Updated by: /master-consolidation writes MASTER_INDEX.md and MASTER_CHUNK_MAP.json (read-only after each run). When the 3 batches consolidate, update the chunk count here. CANONICAL_SOURCE_MAP reconciliation is deferred to the architecture decision.
