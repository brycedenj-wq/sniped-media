#!/usr/bin/env python3
"""
os_name_gate.py , scores a brand name on the 14 OS naming criteria with INCUMBENT-AWARE legal
weighting, assigns a risk TIER, and emits the exact domain + trademark checks to run next.
Heuristic only: it never claims legal clearance (counsel does); design-adjacent incumbents are
penalized hard so idea/sound scores cannot overpower trademark risk.

  os_name_gate.py score "Sovra" [--suffix House] [--idea "..."]
  os_name_gate.py batch <file>                      # one name per line; ranked, with tier
  os_name_gate.py matrix                            # show weights
  os_name_gate.py whois <name>                      # legacy quick .com whois + checklist

Weights: OS_NAME_DECISION_MATRIX.csv (legal-hardened). Doctrine: OS_NAMING_LIBRARY.md.
"""
import sys, os, csv, re, argparse, subprocess

HERE=os.path.dirname(os.path.abspath(__file__))
MATRIX=os.path.join(HERE,"..","OS_NAME_DECISION_MATRIX.csv")

# Known incumbents (live-verified) -> risk class. DESIGN_ADJACENT/DICT are the killers.
# DESIGN_ADJACENT: incumbent in brand/fashion/home/design/marketing (our Class 35/42) -> confusion.
# DICT: dictionary word, crowded everywhere. ADJACENT_SOFT: software/services touching 35/42.
# CROSS_CLASS: real incumbent but unrelated class (coexistable). CROWDED: big/public co, search-buried.
KNOWN_INCUMBENTS={
 "sole":("DICT","dictionary word; crowded all classes"),
 "sovra":("ADJACENT_SOFT","mdf/SOVRA procurement SaaS; procurement touches Class 35/42"),
 "soven":("DESIGN_ADJACENT","Atelier SOVEN (Paris fashion) + Soven wool; design-adjacent"),
 "onora":("DESIGN_ADJACENT","registered ONORA mark + Onora Casa home/design"),
 "solum":("CROWDED","Samsung-spinoff retail-tech ESL (Class 9); large-brand search crowding"),
 "veris":("CROWDED","Veris Residential (public REIT) + Veris Industries; search-crowded"),
 "sovran":("CROSS_CLASS","Sovran self-storage REIT (Class 36/39); unrelated"),
 "aurum":("CROWDED","aurum=gold; many incumbents incl fintech"),
 "lumen":("DESIGN_ADJACENT","Lumen Technologies (huge) + design/agency uses"),
 "aegis":("CROWDED","Aegis = insurance/defense/many"),
 "sigil":("CROSS_CLASS","sigil common in games/crypto"),
 "vault":("DICT","dictionary/crowded fintech"),"seal":("DICT","dictionary/crowded"),
 "regna":("CROSS_CLASS","minor health/pharma uses"),
}
INCUMBENT_ADJ={  # (trademark_risk, search_uniqueness, distinctiveness_cap)
 "DICT":(1,2,3),"DESIGN_ADJACENT":(2,3,6),"ADJACENT_SOFT":(4,5,9),
 "CROWDED":(6,3,9),"CROSS_CLASS":(7,6,9),
}

DICT_WORDS={"sole","vault","seal","only","one","reserve","crucible","citadel","sovereign","hallmark",
 "keystone","monolith","obelisk","bullion","sigil","aegis","plinth","vitrine","mark","stamp","crest",
 "house","works","standard","keep","office","foundry","prime","solitaire","cornerstone","singular"}
IDEA_ROOTS=["sol","sole","uni","unum","mono","prim","sovra","sove","regn","rex","domin","reign","signa",
 "sigil","seal","mark","crest","arx","vault","keep","custos","fortis","aegis","aurum","lumen","veri",
 "proof","petra","stele","monolith","singul","onl","ena","crown","reserve","solv","unic","kee"]
TECHY=["ify","sy","hub","ster","pay","fi","bit","app","tech","ai","io","sync","ware","verse","gpt","bot","ly"]
PHARMA=["zil","dra","xa","zep","cor","vyx","nuv","pra","trip","mab"]
BAD_GLOBAL=["morto","puta","merda","kaka","cazzo"]
VOWELS="aeiouy"; PREMIUM_TAILS=("a","o","um","an","en","ora","ova","el","is","ae")

def syllables(w):
    w=w.lower(); n=0; prev=False
    for c in w:
        v=c in VOWELS
        if v and not prev: n+=1
        prev=v
    return max(1,n)
def core_of(name):
    toks=re.split(r"\s+",name.strip())
    drop={"house","works","standard","keep","atelier","office","reserve","editions","foundry","&","co","studio"}
    keep=[t for t in toks if t.lower().strip(".") not in drop]
    return (keep[0] if keep else toks[0]).strip()
def load_weights():
    w={}
    with open(MATRIX) as f:
        for r in csv.DictReader(f): w[r["criterion"]]=float(r["weight"])
    return w
def clamp(x): return max(0,min(10,int(round(x))))

def score_name(name, idea=""):
    core=core_of(name); cl=re.sub(r"[^a-z]","",core.lower()); L=len(cl); syl=syllables(cl)
    has_root=any(rt in cl for rt in IDEA_ROOTS)
    is_dict=cl in DICT_WORDS
    techy=any(t in cl for t in TECHY); pharma=any(p in cl for p in PHARMA)
    clusters=max((len(m) for m in re.findall(r"[^aeiouy]+",cl)),default=0)
    premium_tail=cl.endswith(PREMIUM_TAILS)
    inc=KNOWN_INCUMBENTS.get(cl)
    s={}
    s["big_idea_fit"]=clamp((8 if has_root else 4)+(1 if any(k in (idea+name).lower() for k in ["only","sovereign","seal","vault","one"]) else 0))
    s["audience_fit"]=clamp(8-(4 if techy else 0)-(4 if pharma else 0))
    s["memorability"]=clamp(10-abs(syl-2)*2-(3 if L>9 else 0)-(2 if L<4 else 0))
    s["pronunciation"]=clamp(10-max(0,clusters-2)*3-max(0,syl-3)*2-(2 if re.search(r"(gh|ough|x|ae|eo)",cl) else 0))
    s["spelling"]=clamp(10-(3 if re.search(r"(ae|eo|yn|ph|x)",cl) else 0)-(2 if "ova" in cl and L>7 else 0))
    s["crowded_bar_test"]=clamp((8 if not is_dict else 4)-max(0,syl-3)*2-(2 if clusters>3 else 0))
    s["premium_feel"]=clamp(6+(2 if premium_tail else 0)+(1 if re.search(r"[sv]",cl) else 0)-(5 if techy else 0)-(6 if pharma else 0)+(1 if cl[-1:] in "aeiou" else 0))
    s["distinctiveness"]=clamp(9-(6 if is_dict else 0)-(2 if techy else 0))
    s["trademark_risk"]=clamp(8-(5 if is_dict else 0)-(1 if L<=4 else 0))   # heuristic caps at 8 (never "clear")
    s["domain_path"]=clamp(7+(1 if L<=7 else 0))
    s["search_uniqueness"]=clamp(9-(6 if is_dict else 0))
    s["visual_identity_potential"]=clamp(7+(2 if L<=7 else 0))
    s["future_proofing"]=clamp(9-(5 if techy else 0)-(3 if pharma else 0))
    s["global_language_risk"]=clamp(2 if any(b in cl for b in BAD_GLOBAL) else 8)
    # INCUMBENT OVERRIDE: real-world data overrides the optimistic heuristic
    note=""
    if inc:
        kind,note=inc; tr,su,dcap=INCUMBENT_ADJ[kind]
        s["trademark_risk"]=min(s["trademark_risk"],tr)
        s["search_uniqueness"]=min(s["search_uniqueness"],su)
        s["distinctiveness"]=min(s["distinctiveness"],dcap)
    else:
        note="no known incumbent (heuristic); clearance still required"
    return core,s,inc

def weighted(s,w): return round(100*sum(w[k]*s[k] for k in s)/sum(w[k]*10 for k in s),1)

def tier(core, s, inc):
    cl=re.sub(r"[^a-z]","",core.lower())
    if inc and inc[0] in ("DICT","DESIGN_ADJACENT"):
        return "INTERNAL CODENAME ONLY" if inc[0]=="DICT" else "HIGH-RISK / DO NOT USE"
    if inc and inc[0] in ("ADJACENT_SOFT","CROWDED"):
        return "COUNSEL REQUIRED"
    if inc and inc[0]=="CROSS_CLASS":
        return "COUNSEL REQUIRED"
    # coined, no known incumbent
    if s["trademark_risk"]>=7 and s["distinctiveness"]>=8 and weighted_ok(s):
        return "PUBLIC-FACING SAFE-ish (pending clearance)"
    return "COUNSEL REQUIRED"
def weighted_ok(s):
    return s["pronunciation"]>=7 and s["premium_feel"]>=7

def verdict(x):
    return "STRONG" if x>=78 else "VIABLE" if x>=66 else "WEAK" if x>=56 else "KILL"
def next_checks(core):
    b=re.sub(r"[^a-z]","",core.lower())
    return [f"DOMAIN: {b}.house / {b}.studio / {b}.works / {b}house.com (Vercel)",
            f"TRADEMARK: USPTO + WIPO '{core}' Class 35 + 42; same/adjacent-class live marks",
            f"INCUMBENT: web '{core} brand/studio/agency'; flag design/marketing occupant",
            f"GLOBAL+SOCIAL: meaning sweep EN/ES/FR/DE/IT/PT + IG/X/LinkedIn/YT handle '{core} house'"]
def do_whois(name):
    dom=re.sub(r'[^a-z0-9-]','',name.strip().lower())+".com"
    try: out=subprocess.run(["whois",dom],capture_output=True,text=True,timeout=20).stdout.lower()
    except Exception as e: out=""; print(f"whois error: {e}")
    avail=bool(re.search(r"no match|not found|no data found|no entries found|status: free",out)) and "registrar:" not in out
    print(f"NAME: {name} | {dom}: {'AVAILABLE (likely)' if avail else 'TAKEN/registered'}")
    return 0 if avail else 1

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="cmd")
    sc=sub.add_parser("score"); sc.add_argument("name"); sc.add_argument("--suffix",default=""); sc.add_argument("--idea",default="")
    b=sub.add_parser("batch"); b.add_argument("file"); b.add_argument("--idea",default="")
    sub.add_parser("matrix"); ww=sub.add_parser("whois"); ww.add_argument("name")
    a=ap.parse_args();
    if a.cmd=="whois": sys.exit(do_whois(a.name))
    w=load_weights()
    if a.cmd=="matrix":
        for k in sorted(w,key=lambda k:-w[k]): print(f"{int(w[k]):>2}  {k}")
        return
    if a.cmd=="score":
        full=(a.name+" "+a.suffix).strip(); core,s,inc=score_name(full,a.idea); total=weighted(s,w)
        print(f"NAME: {full}   core='{core}'   SCORE {total}/100 -> {verdict(total)}   TIER: {tier(core,s,inc)}")
        if inc: print(f"  INCUMBENT[{inc[0]}]: {inc[1]}")
        print()
        for k in sorted(s,key=lambda k:-w[k]*s[k]): print(f"  {s[k]:>2}/10  (w{int(w[k])})  {k}")
        print("\nNEXT CHECKS (gate does NOT clear legally):")
        for c in next_checks(core): print("  - "+c)
        return
    if a.cmd=="batch":
        rows=[]
        for line in open(a.file):
            nm=line.strip()
            if not nm or nm.startswith("#"): continue
            core,s,inc=score_name(nm,a.idea); t=weighted(s,w); rows.append((t,nm,verdict(t),tier(core,s,inc)))
        for t,nm,vd,tr in sorted(rows,reverse=True): print(f"{t:5}  {nm:<24} {vd:<7} {tr}")
        return
    ap.print_help()

if __name__=="__main__": main()
