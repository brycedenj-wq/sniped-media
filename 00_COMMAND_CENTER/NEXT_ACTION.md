# NEXT_ACTION

Wave 1 DONE (59/60 certified). Wave 2 (giants, task wmo834km6) RUNNING.

When Wave 2 completes:
1. Aggregate `/tmp/wave2_out/<id>.json` (consolidated) + `<id>__s*.json` (shard harvest). Verify `segments_read == expected` per doc; flag mismatches; re-run any exception.
2. Persist: copy to `starthere_results/wave2/`, write `OS_STARTHERE_WAVE2.md`, append cert-ledger rows, append SESSION_LOG.
3. Reconcile: confirm ALL 98 unique docs are certified or exception-logged. Only THEN is the folder done.
4. Write `OS_STARTHERE_COMPLETE.md` (final folder certification summary by file class + curated contradictions/weird-gold).
5. Update OS_CURRENT_STATE: mission complete; await next direction. No strategy/production until asked.
