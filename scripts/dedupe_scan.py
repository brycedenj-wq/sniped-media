#!/usr/bin/env python3
"""
Dedupe scan: find exact duplicates by hashing only size-collision groups.
Outputs JSON to stdout for downstream consumption.
"""
import hashlib
import json
import os
from collections import defaultdict
from pathlib import Path

RAW = Path.home() / "AI-Brain-Refinery" / "raw"

by_size = defaultdict(list)
for root, dirs, files in os.walk(RAW):
    for f in files:
        p = Path(root) / f
        try:
            sz = p.stat().st_size
        except OSError:
            continue
        if sz == 0:
            continue
        by_size[sz].append(p)

def md5_of(path: Path, chunk=1024 * 1024) -> str:
    h = hashlib.md5()
    with path.open("rb") as fh:
        for blk in iter(lambda: fh.read(chunk), b""):
            h.update(blk)
    return h.hexdigest()

dup_groups = []
for sz, paths in by_size.items():
    if len(paths) < 2:
        continue
    hashes = defaultdict(list)
    for p in paths:
        try:
            hashes[md5_of(p)].append(p)
        except OSError:
            continue
    for digest, ps in hashes.items():
        if len(ps) >= 2:
            dup_groups.append({
                "size_bytes": sz,
                "md5": digest,
                "paths": sorted(str(p.relative_to(RAW)) for p in ps),
            })

dup_groups.sort(key=lambda g: -g["size_bytes"])
print(json.dumps(dup_groups, indent=2))
