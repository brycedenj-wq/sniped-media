# NEXT_ACTION

When Wave 1 (task wkm034ejp) completes:
1. Read `/tmp/wave1_out/*.json` , verify each doc's `segments_read == expected_segs` (coverage proof); flag mismatches.
2. Persist: write `OS_STARTHERE_WAVE1.md` (doctrine + harvest), append rows to `OS_STARTHERE_CERT_LEDGER.csv`, append to `SESSION_LOG.md`, update this file.
3. Launch Wave 2: the 30 giants (`/tmp/giants.json`, 1,243 segments), SHARDED (~10 seg/agent) with a per-doc consolidation step. Same schema. One wave at a time (cost guard blocks concurrency).
4. After every wave: update cert ledger + dashboard + journal. Do not say "folder done" until all 98 docs are certified or exception-logged.

Mission stays locked to `start here`. No strategy, no production.
