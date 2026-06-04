#!/usr/bin/env python3
"""Build the full start-here certification plan: dedup by md5 (log dups), extract text,
build a segment ledger for every UNIQUE doc. Local + cheap; no reading here."""
import os, re, zipfile, hashlib, html, csv, subprocess, sys
from collections import defaultdict

DIR = "/Users/sniper/Downloads/    SNIPED_OS/start here"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
TMP = "/tmp/starthere_build"
os.makedirs(TMP, exist_ok=True)

def extract(path):
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8", "replace")
        xml = re.sub(r"</w:p>", "\n", xml); xml = re.sub(r"<[^>]+>", "", xml)
        return html.unescape(xml).replace("\r", "")
    except Exception:
        return None

def docid(name):
    return re.sub(r'[^a-zA-Z0-9]', '_', os.path.splitext(name)[0])[:50].strip('_')

docs = []
for root, _, files in os.walk(DIR):
    for fn in sorted(files):
        if fn.lower().endswith(".docx") and not fn.startswith("~$"):
            docs.append(os.path.join(root, fn))

by_md5 = defaultdict(list)
for p in docs:
    by_md5[hashlib.md5(open(p, 'rb').read()).hexdigest()].append(p)

plan = []; dups = []
for md5, paths in by_md5.items():
    canon = sorted(paths)[0]
    name = os.path.basename(canon); did = docid(name)
    txt = extract(canon)
    if txt is None:
        plan.append({"doc_id": did, "name": name, "md5": md5, "segments": 0, "status": "EXTRACT_FAIL"}); continue
    tf = os.path.join(TMP, did + ".txt"); open(tf, "w").write(txt)
    r = subprocess.run(["python3", os.path.join(HERE, "os_segment_ledger.py"), "build", tf, did],
                       capture_output=True, text=True)
    m = re.search(r'(\d+) segment', r.stdout)
    segs = int(m.group(1)) if m else 0
    valid = "VALID" in r.stdout
    plan.append({"doc_id": did, "name": name, "md5": md5, "segments": segs,
                 "status": "ledger_built" if valid else "PARTITION_FAIL"})
    for d in paths[1:]:
        dups.append({"dup_path": d, "canonical": canon, "md5": md5})

plan.sort(key=lambda r: r["segments"])
with open(os.path.join(OUT, "OS_STARTHERE_PLAN.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["doc_id", "name", "md5", "segments", "status"]); w.writeheader(); w.writerows(plan)
with open(os.path.join(OUT, "OS_STARTHERE_DUPLICATES.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["dup_path", "canonical", "md5"]); w.writeheader(); w.writerows(dups)

uniq = len(plan); totseg = sum(r["segments"] for r in plan)
print(f"unique docs: {uniq} | exact-duplicates logged: {len(dups)} | total segments: {totseg}")
print(f"  <=2 seg: {sum(1 for r in plan if r['segments']<=2)}  | 3-10 seg: {sum(1 for r in plan if 3<=r['segments']<=10)}  | >10 seg: {sum(1 for r in plan if r['segments']>10)}")
print(f"  segments in <=2: {sum(r['segments'] for r in plan if r['segments']<=2)} | 3-10: {sum(r['segments'] for r in plan if 3<=r['segments']<=10)} | >10: {sum(r['segments'] for r in plan if r['segments']>10)}")
print("  plan -> OS_STARTHERE_PLAN.csv ; dups -> OS_STARTHERE_DUPLICATES.csv")
