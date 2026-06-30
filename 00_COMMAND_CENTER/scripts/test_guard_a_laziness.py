#!/usr/bin/env python3
"""Smallest local test for Guard A (agentic-laziness defense) in os_stop_check.laziness_blockers.

Three-failure-mode law, Guard A only (OS_UPGRADE_FROM_VIDEOS Action #2; Doctrine: _standards/
OS_PRODUCTION_COMPLETION_ENFORCER.md Amendment 2026-06-29). Proves:
  1. PROGRESS_COUNT.json with done < required blocks.
  2. PROGRESS_COUNT.json with done == required does not block by Guard A.
  3. No PROGRESS_COUNT.json preserves existing behavior (no block).
Run: python3 test_guard_a_laziness.py
"""
import os, sys, json, tempfile, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))

def _imp(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

sc = _imp("os_stop_check")

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# 1. done < required MUST block (laziness defense fires)
d1 = tempfile.mkdtemp()
json.dump({"done": 3, "required": 10}, open(os.path.join(d1, "PROGRESS_COUNT.json"), "w"))
b1 = sc.laziness_blockers(f"The batch in {d1} is complete.")
check("1 done<required blocks", len(b1) == 1 and "LAZINESS" in b1[0], repr(b1))

# 2. done == required MUST NOT block by Guard A
d2 = tempfile.mkdtemp()
json.dump({"done": 10, "required": 10}, open(os.path.join(d2, "PROGRESS_COUNT.json"), "w"))
b2 = sc.laziness_blockers(f"The batch in {d2} is complete.")
check("2 done==required no block", b2 == [], repr(b2))

# 3. no PROGRESS_COUNT.json preserves existing behavior (no block)
d3 = tempfile.mkdtemp()
b3 = sc.laziness_blockers(f"The batch in {d3} is complete.")
check("3 absent file no block", b3 == [], repr(b3))

print("=== Guard A (agentic-laziness defense) test battery ===")
ok = True
for name, passed, detail in results:
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"   -> {detail}" if not passed and detail else ""))
    ok = ok and passed
print(f"=== {'ALL PASS' if ok else 'FAILURES PRESENT'} ({sum(1 for _,p,_ in results if p)}/{len(results)}) ===")
sys.exit(0 if ok else 1)
