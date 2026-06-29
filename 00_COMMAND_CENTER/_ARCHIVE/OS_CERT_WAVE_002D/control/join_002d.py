import re,json,csv,os,glob,sys
SCR="/Users/sniper/.claude/projects/-Users-sniper-AI-Brain-Refinery/f8601c5d-b7f2-4e27-8081-dd6623684617/workflows/scripts"
LED="/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/BOOK_CANON_CERTIFICATION_LEDGER.csv"
rows=[r for r in csv.DictReader(open(LED)) if r["wave"].strip() in("002-D","002D")]
sched=[r for r in rows if r["status_v2"].strip()=="DOCTRINE_EXTRACTION_SCHEDULED"]
def norm(s):
    s=s.lower(); s=re.sub(r'[^a-z0-9]+',' ',s); return ' '.join(s.split())
# harvest R3..R13 books
books=[]
for n in range(3,14):
    p=f"{SCR}/wave002d-R{n}.js"
    t=open(p).read()
    m=re.search(r'const BOOKS = (\[.*?\])\n',t,re.S)
    arr=json.loads(m.group(1))
    for b in arr:
        b["_batch"]=f"R{n}"; books.append(b)
print(f"R3-R13 books harvested: {len(books)}")
# join each book.title to a sched ledger row by normalized-prefix containment
used=set(); mapping=[]; unmatched=[]
for b in books:
    bt=norm(b["title"])
    best=None
    for r in sched:
        if r["path"] in used: continue
        lt=norm(r["title"])
        # match if one normalized title is a prefix of the other for first ~6 words
        a=' '.join(bt.split()[:7]); c=' '.join(lt.split()[:7])
        if lt.startswith(bt[:30]) or bt.startswith(lt[:30]) or a==c or a in lt or c in bt:
            best=r; break
    if best:
        used.add(best["path"]); 
        mapping.append({"slug":b["slug"],"batch":b["_batch"],"parts":b["parts"],
                        "units":b["units"],"title":best["title"].strip(),
                        "src":best["path"].strip(),"ext":best["ext"].strip().lower()})
    else:
        unmatched.append(b["title"])
print(f"matched: {len(mapping)}  unmatched: {len(unmatched)}")
for u in unmatched: print("  UNMATCHED:",u[:60])
# which sched rows are NOT covered by R3-R13 (the extras)
covered=used
extras=[r for r in sched if r["path"] not in covered]
print(f"\nSched rows NOT in R3-R13 (extras): {len(extras)}")
for r in extras: print(f"  EXTRA [{r['ext'].strip()}] {r['title'].strip()[:60]}")
# verify all srcs exist
missing=[m for m in mapping if not os.path.exists(m["src"])]
print(f"\nsrc files missing on disk: {len(missing)}")
for m in missing: print("  MISSING SRC:",m["src"][:70])
json.dump(mapping,open("/tmp/002d_map.json","w"),indent=0)
print("\nwrote /tmp/002d_map.json")
# show the R3 + R4 subset (next to run)
print("\n=== R3 + R4 source map (next batches) ===")
for m in mapping:
    if m["batch"] in ("R3","R4"):
        print(f"  {m['batch']} {m['slug'][:36]:36s} parts={m['parts']} ext={m['ext']} <- {os.path.basename(m['src'])[:50]}")
