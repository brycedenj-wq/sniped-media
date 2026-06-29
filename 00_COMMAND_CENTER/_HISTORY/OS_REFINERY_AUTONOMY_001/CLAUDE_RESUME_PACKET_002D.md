# Claude Resume Packet - 002-D With Strong Loop

Paste this into Claude Code before resuming 002-D.

```text
Before resuming 002-D, read these two Codex control files:

1. /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_CERT_WAVE_002D_CODEX_SHADOW/CODEX_SHADOW_002D.md
2. /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_REFINERY_AUTONOMY_001/AUTONOMOUS_REFINERY_LOOP_SPEC.md

Do not resume as a loose long chat. Upgrade the active 002-D loop into a controller loop first.

Required before launching the next batch:
- Create or update 00_COMMAND_CENTER/OS_CERT_WAVE_002D/control/RUN_STATE.json.
- Create or update 00_COMMAND_CENTER/OS_CERT_WAVE_002D/control/PROGRESS_LEDGER.csv.
- Create or update 00_COMMAND_CENTER/OS_CERT_WAVE_002D/control/WATCHDOG.md.
- Create or update 00_COMMAND_CENTER/OS_CERT_WAVE_002D/control/RESUME_QUEUE.md.

The watchdog rules are mandatory:
- If no output grows for 30 minutes, inspect the batch.
- If no output grows for 45 minutes, stop that batch if safe, mark STALLED_RETRY, and resume failed-only.
- If server-side rate-limit text appears, drop to 1 in-flight Sonnet batch for at least 2 clean batches.
- Do not launch a new batch while an active batch has a stale heartbeat.
- Do not re-read already banked 53 records unless their verifier/ledger fails.

Current verified baseline from Codex:
- 297 book ledger rows.
- Overall ACTIVE_DOCTRINE_BOUND: 131.
- Overall DOCTRINE_EXTRACTION_SCHEDULED: 117.
- 002-D official target rows: 100.
- 002-D bound rows: 53.
- 002-D scheduled rows: 47.
- Partial segment ledger exists and has 53 records.
- Checkpoint dry-run is CLEAN.
- 002-D is not closed.
- OS is not complete.

Resolve the bookkeeping edge before final close:
- The single REJECTED_AFTER_REVIEW row is currently wave="-", lane="business".
- If that journal fragment belonged to the 002-D official 100, explain or fix the target math.
- If it was outside the official 100, say so clearly in the 002-D final receipt.

Resume plan:
1. Clear stale lock only after proving no live writer exists.
2. Relaunch d14 through d24 one at a time or 1 to 2 in flight max, Sonnet.
3. Use cooldown between launches.
4. Run redo pool failed-only, including Dalio as the 2011 edition, not the 2017 slug.
5. Bank verified-only: non-empty segment ledger, 5-field doctrine, adversarial whole-read verify.
6. Update RUN_STATE and PROGRESS_LEDGER after every batch.
7. Close 002-D only when all 100 target rows reconcile.
8. Do not call the OS complete unless DOCTRINE_EXTRACTION_SCHEDULED = 0 across the 297-book ledger.

After 002-D closes, continue 002-E/F/G only if the watchdog is healthy and the operator's boundary rules still hold.

Boundary rules:
- No deletion, move, archive, spend, post, publish, generation, or client-facing send.
- No visual final authority from Claude alone.
- No broad project context blending.
- No false completion.

Morning report must include:
- starting count
- current count
- what changed on disk
- failures/stalls
- rejected rows and reasons
- remaining rows
- checkpoint status
- exact resume command/message
- what must not be claimed yet
```

## Operator Summary

This packet makes Claude install the missing loop control before continuing. It keeps the refinery moving, but it blocks the exact failure that burned the night: a batch hanging silently for hours while the chat keeps thinking the run is alive.
