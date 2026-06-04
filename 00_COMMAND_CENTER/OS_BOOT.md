# OS_BOOT , THE FRONT DOOR

You are resuming an operating system from disk. Do this IN ORDER. Load almost nothing.

## Boot sequence (cold start)
1. Read `OS_CURRENT_STATE.md` , the ONE active mission, what's done, what's blocked, cert summary.
2. Read `NEXT_ACTION.md` , the single next step. Read the last ~5 lines of `SESSION_LOG.md`.
3. Glance at `OS_CERTIFICATION_LEDGER.csv` (or run `python3 scripts/os_certify.py report`) , what is certified vs incomplete. **Do NOT redo anything marked certified.**
4. STOP loading. Do NOT open doctrine docs or chunks yet. You are oriented.
5. For the task, invoke `os-command-router` → it reads `OS_ROUTER_INDEX.md` and pulls ONLY the doctrine doc / skill / chunk ids the task needs.
6. At session end: update `OS_CURRENT_STATE.md` + `NEXT_ACTION.md`, append to `SESSION_LOG.md`, run `python3 scripts/os_checkpoint.py --write`.

## Hard rules at boot
- Disk is truth; chat memory is disposable. Resume from these files, not from recollection.
- One active mission only (OS_CURRENT_STATE.md). Ignore `99_ARCHIVE/` and any doctrine tagged `superseded`.
- Never bulk-load chunks or all doctrine. Two-stage retrieval: index first, then the specific item.
- Chunks are evidence, not skills. Don't turn chunks into skills. (See OS_BOOTLOADER_ARCHITECTURE.md.)
- Do not produce strategy/production unless the active mission says to.

## Activation prompt (if no hook fired)
> Boot the OS: read OS_BOOT.md, OS_CURRENT_STATE.md, NEXT_ACTION.md. Resume the ACTIVE mission. Pull doctrine/chunks only via the router. Do not redo anything the cert ledger marks certified.
