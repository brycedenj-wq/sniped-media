#!/usr/bin/env python3
"""
bank_002d.py - bank verified-only Wave 002-D records into the canon.

Gate (ALL required, else the book stays SCHEDULED / goes to redo):
  - rec.segment_count is int > 0
  - 5-field doctrine all non-empty: operating_principles, patterns_to_steal,
    traps_to_avoid, applies_in_sniped, does_not_apply
  - verdict.pass is True AND verdict.coverage_verdict == 'whole-read'

For each PASSING record (two path-matched flips, kept in sync):
  1. append the record to WAVE_002D_RESUME_SEGMENT_LEDGERS.json  (durable segment ledger)
  2. BOOK_CANON_CERTIFICATION_LEDGER.csv: status_v2 -> ACTIVE_DOCTRINE_BOUND
  3. OS_ENGAGEMENT_MANIFEST.csv: status -> coverage_proven

Refuses to flip a book whose ledger row is already ACTIVE_DOCTRINE_BOUND (no double-bank)
or whose source path cannot be uniquely resolved in both ledgers (surfaces it instead).

Usage:
  python3 bank_002d.py <workflow_output.json> <BATCH_ID>           # DRY RUN (default)
  python3 bank_002d.py <workflow_output.json> <BATCH_ID> --write   # commit
"""
import json, csv, os, sys

CC = "/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER"
MAP = "/tmp/002d_map.json"
SEG = "/Users/sniper/AI-Brain-Refinery/01_KNOWLEDGE_BASE/cert_ledgers/WAVE_002D_RESUME_SEGMENT_LEDGERS.json"
LEDGER = os.path.join(CC, "BOOK_CANON_CERTIFICATION_LEDGER.csv")
MANIFEST = os.path.join(CC, "OS_ENGAGEMENT_MANIFEST.csv")
DOC5 = ["operating_principles","patterns_to_steal","traps_to_avoid","applies_in_sniped","does_not_apply"]

def gate(rec, verdict):
    issues=[]
    sc=rec.get("segment_count")
    if not (isinstance(sc,int) and sc>0): issues.append(f"segment_count={sc}")
    for k in DOC5:
        v=rec.get(k)
        if not (isinstance(v,list) and len(v)>0): issues.append(f"empty:{k}")
    if not verdict.get("pass") is True: issues.append("verdict.pass!=true")
    if verdict.get("coverage_verdict")!="whole-read": issues.append(f"verdict={verdict.get('coverage_verdict')}")
    return issues

def main():
    args=[a for a in sys.argv[1:] if not a.startswith("--")]
    write="--write" in sys.argv
    out_json, batch = args[0], args[1]
    # wave-parameterized: --map=<path> (default 002-D) and --override=<path>
    map_path=MAP
    ovrf="/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_CERT_WAVE_002D/control/dedup_override.json"
    for a in sys.argv:
        if a.startswith("--map="): map_path=a.split("=",1)[1]
        if a.startswith("--override="): ovrf=a.split("=",1)[1]
    mp={b["slug"]:b for b in json.load(open(map_path))}
    # extras not in the main map (e.g. 002-D Power&Prediction)
    if map_path==MAP and os.path.exists("/tmp/002d_extra_map.json"):
        for b in json.load(open("/tmp/002d_extra_map.json")): mp[b["slug"]]=b
    else:
        extra=map_path.replace(".json","_extra.json")
        if os.path.exists(extra):
            for b in json.load(open(extra)): mp[b["slug"]]=b
    # dedup/exception overrides: slug -> {status_v2, manifest_status, reason}
    OVR=json.load(open(ovrf)) if os.path.exists(ovrf) else {}
    data=json.load(open(out_json))
    records=data.get("result",{}).get("records") or data.get("records") or []
    led=list(csv.DictReader(open(LEDGER))); led_f=list(led[0].keys())
    man=list(csv.DictReader(open(MANIFEST))); man_f=list(man[0].keys())
    led_by_path={r["path"].strip():r for r in led}
    man_by_path={r["path"].strip():r for r in man if r.get("class","")=="source"}
    seg=json.load(open(SEG))
    banked=[]; rejected=[]; flips=[]
    for r in records:
        slug=r["slug"]; rec=r["rec"]; verdict=r["verdict"]
        iss=gate(rec,verdict)
        if iss:
            rejected.append((slug,iss)); continue
        b=mp.get(slug)
        if not b: rejected.append((slug,["no-map-entry"])); continue
        src=b["src"].strip()
        lr=led_by_path.get(src); mr=man_by_path.get(src)
        if not lr: rejected.append((slug,["no-ledger-row-for-path"])); continue
        if not mr: rejected.append((slug,["no-manifest-row-for-path"])); continue
        if lr["status_v2"].strip()=="ACTIVE_DOCTRINE_BOUND":
            rejected.append((slug,["already-bound (no double-bank)"])); continue
        o=OVR.get(slug)
        if o:
            tl=o["status_v2"]; tm=o.get("manifest_status","duplicate"); disp=o.get("reason","")
        else:
            tl="ACTIVE_DOCTRINE_BOUND"; tm="coverage_proven"; disp="certified whole-read"
        flips.append((slug,lr,mr,src,tl,tm))
        banked.append({"book_slug":slug,"title":r.get("title",b.get("title","")),
                       "batch":batch,"path":src,"rec":rec,"verdict":verdict,
                       "disposition":tl,"disposition_reason":disp})

    print(f"=== BANK {batch} ({'WRITE' if write else 'DRY-RUN'}) ===")
    print(f"records in: {len(records)} | passed gate: {len(flips)} | rejected: {len(rejected)}")
    for slug,lr,mr,src,tl,tm in flips:
        tag="BANK" if tl=="ACTIVE_DOCTRINE_BOUND" else "DEDUP/EXC"
        print(f"  {tag:9s} {slug[:36]:36s} led:{lr['status_v2'].strip()}->{tl}  man:{mr['status'].strip()}->{tm}")
    for slug,iss in rejected:
        print(f"  REJECT {slug[:40]:40s} :: {iss}")

    if write and flips:
        for slug,lr,mr,src,tl,tm in flips:
            lr["status_v2"]=tl
            mr["status"]=tm
        with open(LEDGER,"w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=led_f); w.writeheader(); w.writerows(led)
        with open(MANIFEST,"w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=man_f); w.writeheader(); w.writerows(man)
        seg.extend(banked)
        json.dump(seg,open(SEG,"w"),indent=1)
        print(f"WROTE: ledger + manifest flipped ({len(flips)}); segment ledger now {len(seg)} records")
    elif write:
        print("WRITE requested but nothing passed the gate; no changes.")
    # post counts
    from collections import Counter
    bound=sum(1 for r in led if r["status_v2"].strip()=="ACTIVE_DOCTRINE_BOUND")
    cov=sum(1 for r in man if r.get("class","")=="source" and r.get("status","").strip()=="coverage_proven")
    prov=sum(1 for r in man if r.get("class","")=="source" and r.get("status","").strip()=="provisional_chunked_not_certified")
    sched=sum(1 for r in led if r["status_v2"].strip()=="DOCTRINE_EXTRACTION_SCHEDULED")
    print(f"post-state: book-ledger BOUND={bound} SCHEDULED={sched} | manifest(source) coverage_proven={cov} provisional={prov}")
    print(f"reconcile: BOUND==coverage_proven? {'YES' if bound==cov else 'NO <-- INVESTIGATE'}")
    return 0

if __name__=="__main__":
    sys.exit(main())
