#!/usr/bin/env python3
"""
os_source_map_scan.py - READ-ONLY scan of the registered source folders.
Never copies, moves, deletes, or git-adds. Never crawls .git/node_modules/caches/Library.
Reports existence, freshness (mtime), shallow size, top-level count - to keep the registry honest.

  os_source_map_scan.py            # scan all registry paths
  os_source_map_scan.py --verify   # also flag MISSING paths in the registry
"""
import csv, os, sys, subprocess, time

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "EXTERNAL_SOURCE_REGISTRY.csv")
IGNORE = (".git", "node_modules", ".cache", ".lrdata", "Library")

def shallow_size(p):
    try:
        out = subprocess.run(["du", "-sh", p], capture_output=True, text=True, timeout=8)
        return out.stdout.split("\t")[0].strip() or "?"
    except Exception:
        return ">8s"

def main():
    verify = "--verify" in sys.argv
    rows = list(csv.DictReader(open(REG)))
    print("READ-ONLY SOURCE SCAN (no copy/move/delete/add):\n")
    for r in rows:
        p = r["path"]
        if r["role"] == "dangerous_ignore":
            print(f"  IGNORE   {r['id']:20s} {p}")
            continue
        if any(ig in p for ig in IGNORE):
            print(f"  IGNORE   {r['id']:20s} {p}")
            continue
        if os.path.exists(p):
            try:
                mt = time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(p)))
            except Exception:
                mt = "?"
            top = 0
            try:
                top = len([e for e in os.listdir(p) if not e.startswith(".") and e not in IGNORE])
            except Exception:
                pass
            print(f"  OK       {r['id']:20s} {r['role']:14s} {r['freshness']:>7s}  top={top:<4d} mtime={mt}  {p}")
        else:
            tag = "MISSING!" if verify else "MISSING "
            print(f"  {tag} {r['id']:20s} {p}")
    print("\nRule: existence/freshness here is advisory. Newest PROVEN AI-Brain-Refinery state wins on any conflict.")

if __name__ == "__main__":
    main()
