#!/usr/bin/env python3
"""
os_starthere_classify.py , classify every Start Here doc BY CONTENT (not filename).

Doc names are misleading, so this reads the full text of each doc and scores:
  - tool_family (which operator library it feeds): higgsfield/adobe/premiere/after_effects/figma/
    blender/social/money/copy/sales/photo/claude/multi
  - doc_type: how_to / transcript / playbook / framework / reference / duplicate / low_signal
  - technique density (how-to verbs + step markers per 1k words)
  - conversion_status: USE (extract cards) / QUEUE (useful, lower priority) / DISCARD (dup/low-signal)
  - reason

Writes OS_STARTHERE_OPERATIONALIZATION.csv. Marks exact-duplicate files DISCARD(duplicate).

  os_starthere_classify.py            , build the csv
  os_starthere_classify.py worklist   , print the USE-set (uncovered) extraction work list
"""
import os, sys, re, csv, hashlib, json

CMD  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # 00_COMMAND_CENTER
REPO = os.path.dirname(CMD)                                          # AI-Brain-Refinery
TXT  = os.path.join(REPO, "01_KNOWLEDGE_BASE", "STARTHERE_SOURCE_ARCHIVE", "_extracted_text")
OUT  = os.path.join(CMD, "OS_STARTHERE_OPERATIONALIZATION.csv")
CARDS_JSON = os.path.join(CMD, "TECHNIQUE_CARDS.json")

# tool-family signal keywords (content, weighted by specificity)
FAM = {
 "higgsfield": ["higgsfield","soul id","soul cast","soul cinema","seedance","kling","nano banana","wan 2","veo","popcorn","vibe motion","cinema studio","start frame","end frame","upscale","topaz","shots","angles","skin enhancer","virtual production","i2v","t2v"],
 "adobe":      ["photoshop","firefly","lightroom","camera raw","generative fill","generative expand","neural filter","frequency separation","dodge","burn","curves","clipping mask","express","brand kit","evoto","retouch","harmonization","content aware"],
 "premiere":   ["premiere","sequence","timeline","j-cut","l-cut","cut on","b-roll","edit pacing","transitions","color grade in premiere","lumetri","edl","rough cut","fine cut"],
 "after_effects":["after effects","ae ","aftereffects","keyframe","motion graphics","kinetic type","title animation","expression","null object","trapcode","rotoscope","composition panel"],
 "figma":      ["figma","design system","auto layout","components","variants","type scale","8pt grid","tokens","frames","masthead","pitch deck","wireframe","constraints"],
 "blender":    ["blender","bpy","render","cycles","eevee","mesh","viewport","object-space","volumetric","emission shader","3-point light","plinth","monolith","geometry nodes"],
 "social":     ["instagram","reels","tiktok","threads","carousel","hook","retention","algorithm","posting","content pillar","attention","garyvee","gary vee","views","followers","distribution","day trading attention"],
 "money":      ["offer","pricing","revenue","value equation","grand slam","upsell","retainer","cash","margin","monetize","productize","mrr","ticket","package","anchor"],
 "copy":       ["copywriting","headline","hook line","body copy","cta","caption","tone of voice","story","narrative","copy formula","aida","pas"],
 "sales":      ["outreach","cold email","cold dm","instantly","lead","pipeline","discovery call","objection","close","follow up","prospect","icp","booking","sequence"],
 "photo":      ["posing","lighting setup","location scout","moodboard","model","wardrobe","shoot","portrait","golden hour","softbox","rembrandt","set design","pixieset"],
 "claude":     ["claude code","mcp","subagent","slash command","claude.md","plugin","skill","workflow","anthropic","prompt template","context window","agent sdk"],
}
HOWTO = ["step 1","step 2","step 3","first,","then ","next,","->","how to","here's how","the trick is","what you do is","go to","click ","select ","open ","drag ","set the","adjust the","use the","make sure","formula","framework","exact","recipe","setting","panel"]
LOWSIG = ["lol","lmao","idk","haha","um ","uh ","you know what i mean","ngl","tbh","fr fr"]

def read(p):
    try: return open(p, encoding="utf-8", errors="ignore").read()
    except: return ""

def covered_docs():
    if not os.path.exists(CARDS_JSON): return {}
    cards = json.load(open(CARDS_JSON))
    from collections import Counter
    def norm(s):
        s=(s or "").lower().split("/")[-1]; s=re.sub(r"\.(txt|docx)$","",s); return re.sub(r"\s+"," ",s).strip()
    c=Counter(norm(x.get("source_doc","")) for x in cards)
    return c

def classify():
    docs = sorted(os.listdir(TXT))
    cov = covered_docs()
    def norm(s):
        s=s.lower(); s=re.sub(r"\.(txt|docx)$","",s); return re.sub(r"\s+"," ",s).strip()
    # pre-compute hash groups, pick canonical = most existing cards, then cleanest name
    groups={}
    for d in docs:
        h=hashlib.md5(read(os.path.join(TXT,d)).encode("utf-8",errors="ignore")).hexdigest()
        groups.setdefault(h,[]).append(d)
    def dirty(n): return ("copy" in n.lower())+("(1)" in n)+(len(n)/100.0)
    canonical={}  # hash -> canonical doc
    for h,members in groups.items():
        canonical[h]=sorted(members, key=lambda m:(-cov.get(norm(m),0), dirty(m)))[0]
    rows=[]
    for d in docs:
        p=os.path.join(TXT,d); txt=read(p); low=txt.lower()
        words=len(txt.split()); wk=max(words/1000.0,0.001)
        h=hashlib.md5(txt.encode("utf-8",errors="ignore")).hexdigest()
        dup_of = None if canonical[h]==d else canonical[h]
        # family scores
        fam_scores={f:sum(low.count(k) for k in kws) for f,kws in FAM.items()}
        ranked=sorted(fam_scores.items(), key=lambda x:-x[1])
        top=[f for f,s in ranked if s>0][:3]
        primary=top[0] if top else "multi"
        if len([f for f,s in ranked if s>= max(1,ranked[0][1]*0.6)])>=3: primary="multi"
        # technique density
        howto_hits=sum(low.count(k) for k in HOWTO)
        density=round(howto_hits/wk,1)
        low_hits=sum(low.count(k) for k in LOWSIG)
        # doc_type
        if dup_of: dtype="duplicate"
        elif density>=8 and words>4000: dtype="how_to"
        elif "playbook" in d.lower() or "stack" in d.lower() or "reference" in d.lower() or "manual" in d.lower() or "codex" in d.lower(): dtype="playbook"
        elif "framework" in low[:2000] or "worksheet" in d.lower(): dtype="framework"
        elif words<1500: dtype="reference"
        elif density<3 and low_hits/wk>2: dtype="low_signal"
        else: dtype="transcript"
        # conversion status
        ncards=cov.get(norm(d),0)
        if dup_of: status,reason="DISCARD",f"exact duplicate of {dup_of}"
        elif dtype=="low_signal" and words<3000: status,reason="DISCARD","low technique density, chat noise"
        elif ncards>0: status,reason="USED",f"{ncards} cards already extracted"
        elif top and ranked[0][1]>=5: status,reason="USE", f"high {primary} signal ({ranked[0][1]} hits), density {density}"
        elif words<1500 and density<4: status,reason="QUEUE","short/low-density, fold into playbook cards later"
        else: status,reason="USE", f"{primary} content, density {density}, {words} words"
        rows.append({
            "doc":d,"words":words,"primary_family":primary,
            "families":";".join(f"{f}:{fam_scores[f]}" for f in top) or "none",
            "doc_type":dtype,"density":density,"existing_cards":ncards,
            "conversion_status":status,"reason":reason,
        })
    rows.sort(key=lambda r:(r["conversion_status"]!="USE", -r["words"]))
    with open(OUT,"w",newline="") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    # summary
    from collections import Counter
    sc=Counter(r["conversion_status"] for r in rows); fc=Counter(r["primary_family"] for r in rows)
    print(f"classified {len(rows)} docs -> {OUT}")
    print("status:", dict(sc))
    print("primary family:", dict(fc))
    return rows

def worklist():
    rows=list(csv.DictReader(open(OUT)))
    use=[r for r in rows if r["conversion_status"]=="USE"]
    print(f"USE-set (extract cards) : {len(use)} docs")
    for r in sorted(use,key=lambda r:-int(r["words"])):
        print(f"  {int(r['words']):>9d}  {r['primary_family']:13s} {r['doc']}")

if __name__=="__main__":
    if len(sys.argv)>1 and sys.argv[1]=="worklist": worklist()
    else: classify()
