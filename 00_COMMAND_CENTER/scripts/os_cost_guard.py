#!/usr/bin/env python3
"""os-cost-guard: PreToolUse hook for the Workflow tool. Blocks concurrent waves (the proven
session-drain failure) and oversized inline scripts. Fails OPEN (never bricks the tool on error).
Block = exit code 2 + reason on stderr."""
import sys, json, os, time
LOCK="/tmp/os_wf.lock"; LOCK_TTL=1200  # 20 min stale window
MAX_SCRIPT_BYTES=480_000  # > ~480KB inline script implies a very large embedded plan
def block(msg): sys.stderr.write(f"[os-cost-guard BLOCK] {msg}\n"); sys.exit(2)
try:
    raw=sys.stdin.read()
    data=json.loads(raw) if raw.strip() else {}
    ti=data.get("tool_input",data)
    # 1) concurrency: one wave at a time
    if os.path.exists(LOCK):
        age=time.time()-os.path.getmtime(LOCK)
        if age < LOCK_TTL:
            block(f"a workflow started {int(age)}s ago (<{LOCK_TTL}s). NO concurrent waves (drains the session). Wait or TaskStop it. Override: rm {LOCK}")
    # 2) oversized inline script
    script=ti.get("script") or ""
    if len(script) > MAX_SCRIPT_BYTES:
        block(f"inline script is {len(script)//1000}KB (> {MAX_SCRIPT_BYTES//1000}KB). Likely an oversized plan. Split the wave or load via scriptPath.")
    # allow + set the lock
    open(LOCK,"w").write(str(time.time()))
except SystemExit: raise
except Exception:
    pass  # fail open
sys.exit(0)
