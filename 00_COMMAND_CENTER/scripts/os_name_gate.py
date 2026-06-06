#!/usr/bin/env python3
"""
os_name_gate.py , scores a brand name on the 14 OS naming criteria, returns a weighted verdict,
and emits the EXACT domain + trademark checks to run next. Heuristic only: it never claims legal
clearance (counsel does), it tells you precisely what to verify.

  os_name_gate.py score "Sovra" [--suffix House] [--idea "..."]
  os_name_gate.py batch <file_of_names>            # one name per line; prints ranked
  os_name_gate.py matrix                            # show weights
  os_name_gate.py whois <name>                      # legacy: quick .com whois + manual checklist

Weights from OS_NAME_DECISION_MATRIX.csv. Doctrine: OS_NAMING_LIBRARY.md.
The Vercel domain MCP gives authoritative availability; whois here is a fast local fallback.
"""
import sys, os, csv, re, argparse, subprocess

HERE=os.path.dirname(os.path.abspath(__file__))
MATRIX=os.path.join(HERE,"..","OS_NAME_DECISION_MATRIX.csv")

DICT_WORDS={"sole","vault","seal","only","one","reserve","crucible","citadel","sovereign","hallmark",
 "keystone","monolith","obelisk","bullion","sigil","aegis","plinth","vitrine","mark","stamp","crest",
 "house","works","standard","keep","office","foundry","prime","solitaire","cornerstone","singular","strikehouse","theonly"}
IDEA_ROOTS=["sol","sole","solo","uni","unum","mono","prim","sovra","sove","regn","rex","domin","reign",
 "signa","sigil","seal","mark","crest","arx","vault","keep","custos","fortis","aegis","aurum","lumen",
 "veri","proof","petra","stele","monolith","singul","onl","ena","crown","reserve"]
TECHY=["ify","sy","hub","ster","pay","fi","bit","app","tech","ai","io","sync","ware","verse","gpt","bot","ly"]
PHARMA=["zil","dra","xa","zep","cor","vyx","nuv","pra","trip","mab"]
BAD_GLOBAL=["morto","puta","merda","kaka","cazzo"]  # illustrative; full sweep still required
VOWELS="aeiouy"
PREMIUM_TAILS=("a","o","um","an","en","ora","ova","el","is","ae")

def syllables(w):
    w=w.lower(); n=0; prev=False
    for c in w:
        v=c in VOWELS
        if v and not prev: n+=1
        prev=v
    return max(1,n)

def core_of(name):
    toks=re.split(r"\s+", name.strip())
    drop={"house","works","standard","keep","atelier","office","reserve","editions","foundry","&","co"}
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
    s={}
    s["big_idea_fit"]=clamp((8 if has_root else 4)+(1 if any(k in (idea+name).lower() for k in ["only","sovereign","seal","vault","one"]) else 0))
    s["audience_fit"]=clamp(8-(4 if techy else 0)-(4 if pharma else 0))
    s["memorability"]=clamp(10-abs(syl-2)*2-(3 if L>9 else 0)-(2 if L<4 else 0))
    s["pronunciation"]=clamp(10-max(0,clusters-2)*3-max(0,syl-3)*2-(2 if re.search(r"(gh|ough|x|ae|eo)",cl) else 0))
    s["spelling"]=clamp(10-(3 if re.search(r"(ae|eo|yn|ph|x)",cl) else 0)-(2 if "ova" in cl and L>7 else 0))
    s["crowded_bar_test"]=clamp((8 if not is_dict else 4)-max(0,syl-3)*2-(2 if clusters>3 else 0))
    s["premium_feel"]=clamp(6+(2 if premium_tail else 0)+(1 if re.search(r"[sv]",cl) else 0)-(5 if techy else 0)-(6 if pharma else 0)+(1 if cl[-1:] in "aeiou" else 0))
    s["distinctiveness"]=clamp(9-(6 if is_dict else 0)-(2 if techy else 0))
    s["trademark_risk"]=clamp(9-(5 if is_dict else 0)-(1 if L<=4 else 0))
    s["domain_path"]=clamp(7+(1 if L<=7 else 0))
    s["search_uniqueness"]=clamp(9-(6 if is_dict else 0))
    s["visual_identity_potential"]=clamp(7+(2 if L<=7 else 0))
    s["future_proofing"]=clamp(9-(5 if techy else 0)-(3 if pharma else 0))
    s["global_language_risk"]=clamp(2 if any(b in cl for b in BAD_GLOBAL) else 8)
    return core,s

def weighted(s,w):
    return round(100*sum(w[k]*s[k] for k in s)/sum(w[k]*10 for k in s),1)

def verdict(x):
    return "STRONG , advance to clearance" if x>=78 else "VIABLE , advance with caveats" if x>=68 else "WEAK , only if nothing better" if x>=58 else "KILL"

def next_checks(core):
    b=re.sub(r"[^a-z]","",core.lower())
    return [f"DOMAIN: {b}.house / {b}.studio / {b}house.com / {b}.co  (Vercel check_domain_availability_and_price)",
            f"TRADEMARK: USPTO + global '{core}' in Nice Class 35 + 42; look for same-class live marks",
            f"INCUMBENT: web search '{core} brand company'; flag a sizable same-category occupant",
            f"GLOBAL: meaning sweep '{core}' across EN/ES/FR/DE/IT/PT before public use"]

def do_whois(name):
    dom=re.sub(r'[^a-z0-9-]','',name.strip().lower())+".com"
    try: out=subprocess.run(["whois",dom],capture_output=True,text=True,timeout=20).stdout.lower()
    except Exception as e: out=""; print(f"whois error: {e}")
    avail=bool(re.search(r"no match|not found|no data found|no entries found|status: free",out)) and "registrar:" not in out
    print(f"NAME: {name} | {dom}: {'AVAILABLE (likely)' if avail else 'TAKEN/registered'}")
    for c in ["no major brand/app owns it (web+app stores)","USPTO clear for Class 35/42",
              "social handles free","coined/distinctive not generic","no OS brand/lane collision"]:
        print(f"  [ ] {c}")
    return 0 if avail else 1

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="cmd")
    sc=sub.add_parser("score"); sc.add_argument("name"); sc.add_argument("--suffix",default=""); sc.add_argument("--idea",default="")
    b=sub.add_parser("batch"); b.add_argument("file"); b.add_argument("--idea",default="")
    sub.add_parser("matrix"); ww=sub.add_parser("whois"); ww.add_argument("name")
    a=ap.parse_args()
    if a.cmd=="whois": sys.exit(do_whois(a.name))
    w=load_weights()
    if a.cmd=="matrix":
        for k in sorted(w,key=lambda k:-w[k]): print(f"{int(w[k]):>2}  {k}")
        return
    if a.cmd=="score":
        full=(a.name+" "+a.suffix).strip(); core,s=score_name(full,a.idea); total=weighted(s,w)
        print(f"NAME: {full}   core='{core}'   SCORE {total}/100 -> {verdict(total)}\n")
        for k in sorted(s,key=lambda k:-w[k]*s[k]): print(f"  {s[k]:>2}/10  (w{int(w[k])})  {k}")
        print("\nNEXT CHECKS (gate does NOT clear legally):")
        for c in next_checks(core): print("  - "+c)
        return
    if a.cmd=="batch":
        rows=[]
        for line in open(a.file):
            nm=line.strip()
            if not nm or nm.startswith("#"): continue
            core,s=score_name(nm,a.idea); t=weighted(s,w); rows.append((t,nm,verdict(t)))
        for t,nm,vd in sorted(rows,reverse=True): print(f"{t:5}  {nm:<28} {vd}")
        return
    ap.print_help()

if __name__=="__main__": main()
