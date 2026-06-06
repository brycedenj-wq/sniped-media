#!/usr/bin/env python3
"""
os_naming_engine.py , the OS naming generator.

Generates brand-name candidates across 8 lanes from a root bank + morphology + sound-symbolism
constraints, tuned to a big idea. Deterministic (no RNG) so runs are reproducible.

  os_naming_engine.py generate [--n 120] [--lane LANE] [--json]
  os_naming_engine.py lanes
  os_naming_engine.py roots

Lanes: suggestive invented associative compound foreign soundsymbolic domain suffix
Doctrine: OS_NAMING_LIBRARY.md . Score output with os_name_gate.py.
"""
import sys, argparse, json, itertools

# ---- ROOT BANK (themes the brief must express) ----
ROOTS = {
  "only_one": ["sol","sole","solo","uni","unum","unus","mono","monos","primus","unica","singul","onlie","onli","ena","prime"],
  "sovereign": ["sovra","sove","soveren","regna","regn","rex","imperia","anweald","domin","crown","reign"],
  "seal_mark": ["signa","signum","sigil","seal","mark","stamp","hallmark","brand","crest","emblem"],
  "vault_keep": ["arx","vault","keep","custos","crypta","fortis","castel","strong","aegis","bastion","reserve","bullion"],
  "proof": ["veritas","testis","proba","witness","proof","attest","cred"],
  "light_stone": ["lumen","lux","sol","aurum","petra","lapis","stele","obelis","monolith","plinth","vitrine"],
}
SUGGESTIVE = ["Sovra","Solum","Solus","Regna","Sovera","Soveren","Aurum","Lumen","Vesta","Vauld","Solene","Onora","Soleil","Regis","Crovo","Sevra","Veris","Solvent-no"]
ASSOCIATIVE = ["Vault","Seal","Keystone","Monolith","Obelisk","Bullion","Hallmark","Sovereign","Citadel","Plinth","Vitrine","Aegis","Sigil","Crucible","Reserve","Strikehouse","Theonly","Singular","Solitaire","Cornerstone"]
FOREIGN = ["Unum","Solus","Signum","Sigillum","Arx","Custos","Aurum","Lumen","Regnum","Monos","Veritas","Petra","Aegis","Solum","Primus","Unica","Sovrano","Soleil","Anweald","Regalis"]
INV_SUFFIX = ["a","o","um","is","ae","ova","ora","en","ic","ix","el","ar","eo","ia","us","yn"]
INV_BASES = ["Sov","Sol","Sov","Vor","Sev","Reg","Aur","Lum","Vau","Ona","Solv","Onl","Una","Mon","Vest","Cust","Arx","Sign","Soren","Veri"]
COMPOUND_A = ["Sole","Only","One","Sovra","Solum","Vault","Seal","Prime","Aurum","Mono","Singular"]
COMPOUND_B = ["mark","keep","seal","proof","works","standard","house","crest","stamp","reserve","field","forge"]
# sound-symbolic premium skeletons: struck consonant + hushed premium tail
SS_HEADS = ["So","Sa","Se","Vo","Va","Au","Re","No","Lo","Ro"]
SS_MIDS  = ["v","vr","l","r","ren","va","vo","ra","ro","na"]
SS_TAILS = ["a","o","um","an","en","ova","ora","el"]
SUFFIX_ARCH = ["House","Works","Standard","Keep","Atelier","& Co","Office","Reserve","Editions","Foundry"]

def cap(s): return s[:1].upper()+s[1:].lower() if s else s

def lane_suggestive():
    out=[w for w in SUGGESTIVE if not w.endswith("-no")]
    return out

def lane_invented():
    out=[]
    for b in INV_BASES:
        for suf in INV_SUFFIX:
            w=cap(b)+suf
            if 4<=len(w)<=8: out.append(w)
    return out

def lane_associative():
    return ASSOCIATIVE[:]

def lane_compound():
    out=[]
    for a in COMPOUND_A:
        for b in COMPOUND_B:
            w=cap(a)+b
            if len(w)<=12 and a.lower()!=b: out.append(w)
    return out

def lane_foreign():
    return FOREIGN[:]

def lane_soundsymbolic():
    out=[]
    for h in SS_HEADS:
        for m in SS_MIDS:
            for t in SS_TAILS:
                w=h+m+t
                if 4<=len(w)<=7:
                    # premium filter: no triple-consonant, must end vowel-ish or -um/-an/-en
                    if not any(c*3 in w.lower() for c in "bcdfgsvrlmn"):
                        out.append(cap(w))
    # de-dup, keep pleasant ones (avoid awkward clusters)
    bad=("vrv","lrl","rnr","vov ")
    out=[w for w in dict.fromkeys(out) if not any(b in w.lower() for b in bad)]
    return out

def lane_domain():
    # base coinages most likely to anchor an acquirable address, paired with on-brand TLD/suffix forms
    bases=["Sovra","Solum","Onora","Regna","Aurum","Sevra","Solene","Veris","Sovera","Vauld"]
    out=[]
    for b in bases:
        out.append(f"{b} (try {b.lower()}.house / {b.lower()}house.com / {b.lower()}.studio)")
    return out

def lane_suffix():
    bases=["Sovra","Solum","Aurum","Regna","Veris","Sole","Sigil","Aegis"]
    out=[]
    for b in bases:
        for s in SUFFIX_ARCH:
            out.append(f"{b} {s}")
    return out

LANES={
 "suggestive":lane_suggestive,"invented":lane_invented,"associative":lane_associative,
 "compound":lane_compound,"foreign":lane_foreign,"soundsymbolic":lane_soundsymbolic,
 "domain":lane_domain,"suffix":lane_suffix,
}

def generate(n, lane=None):
    items=[]
    lanes = [lane] if lane else list(LANES)
    # round-robin across lanes for a balanced spread
    pools={L:LANES[L]() for L in lanes}
    idx={L:0 for L in lanes}
    while len(items)<n and any(idx[L]<len(pools[L]) for L in lanes):
        for L in lanes:
            if idx[L]<len(pools[L]):
                items.append({"name":pools[L][idx[L]],"lane":L})
                idx[L]+=1
                if len(items)>=n: break
    return items

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="cmd")
    g=sub.add_parser("generate"); g.add_argument("--n",type=int,default=120); g.add_argument("--lane",default=None); g.add_argument("--json",action="store_true")
    sub.add_parser("lanes"); sub.add_parser("roots")
    a=ap.parse_args()
    if a.cmd=="lanes": print("\n".join(LANES)); return
    if a.cmd=="roots": print(json.dumps(ROOTS,indent=2)); return
    if a.cmd=="generate":
        items=generate(a.n,a.lane)
        if a.json: print(json.dumps(items,indent=2))
        else:
            for i,it in enumerate(items,1): print(f"{i:3}. [{it['lane']:>12}] {it['name']}")
        return
    ap.print_help()

if __name__=="__main__": main()
