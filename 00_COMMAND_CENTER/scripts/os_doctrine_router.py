#!/usr/bin/env python3
"""
os_doctrine_router.py , given a task, choose WHICH doctrines matter and how confident we are.

os_doctrine.py already knows how to LOAD and CHECK a domain. What was missing is the selection layer:
for an arbitrary task, which doctrine domains should fire, in what order, and at what confidence. This
router answers that so the execution graph can fuse the right doctrine packs into the moment of creation
without a human deciding each time.

Confidence is honest:
  CERTIFIED  , all sources are present certified memory files (intel_*/feedback_*) -> trust at creation.
  MIXED      , some certified present + some knowledge-base (provisional) or missing.
  PROVISIONAL, mostly knowledge-base jsonl or missing files -> usable but label it provisional, don't crown.

  os_doctrine_router.py route "<task text>"      , ranked doctrines + confidence + load command per domain
  os_doctrine_router.py domains                    , every domain with its standing confidence
"""
import os, sys, json, argparse, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = "/Users/sniper/.claude/projects/-Users-sniper/memory"

def _m(n):
    s = importlib.util.spec_from_file_location(n, os.path.join(HERE, n + ".py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

# task keyword -> doctrine domain(s), weighted. Mirrors prime_router module triggers but maps straight
# to os_doctrine.DOCTRINE domains so the two layers stay consistent.
TASK_TO_DOCTRINE = {
    "copy":           ["headline","caption","tagline","copy","words","cta","write","name","subject line","email"],
    "visual_grade":   ["image","photo","grade","color","hero","still","portrait","retouch","composite","render an image"],
    "world_character":["world","character","3d","blender","environment","scene","set","mark","logo","creature"],
    "layout_type":    ["layout","deck","poster","one-sheet","onesheet","carousel","slide","typography","board","pdf"],
    "pricing_offer":  ["price","pricing","offer","package","sell","monetize","money path","tier","quote"],
    "distribution_hook":["distribution","hook","reach","launch","post","viral","clip","feed","audience"],
    "trust_sales":    ["client","pitch","proposal","deliver","trust","sell","close","demo","present","sales"],
    "motion":         ["motion","video","animate","reel","trailer","clip","cut","seedance","footage"],
    "safety_identity":["privacy","identity","employer","legal","public","host","deploy","safe","leak","metadata","nda"],
}

def confidence(domain, doc):
    srcs = doc["sources"]
    present = [s for s in srcs if os.path.exists(s)]
    certified = [s for s in present if s.startswith(MEM) and ("/intel_" in s or "/feedback_" in s)]
    if present and len(certified) == len(srcs):
        return "CERTIFIED", present, certified
    if certified:
        return "MIXED", present, certified
    return "PROVISIONAL", present, certified

def route(text):
    doctrine = _m("os_doctrine").DOCTRINE
    t = text.lower()
    scored = []
    for domain, kws in TASK_TO_DOCTRINE.items():
        s = sum(2 if kw in t else 0 for kw in kws)
        if s and domain in doctrine:
            scored.append((s, domain))
    scored.sort(reverse=True)
    # safety_identity is a standing floor doctrine: it always applies, even if not triggered.
    domains = [d for _, d in scored]
    if "safety_identity" not in domains:
        domains.append("safety_identity")
    out = []
    for d in domains:
        doc = doctrine[d]
        conf, present, certified = confidence(d, doc)
        out.append({
            "domain": d,
            "confidence": conf,
            "sources_present": f"{len(present)}/{len(doc['sources'])}",
            "certified_sources": len(certified),
            "rubric": doc["rubric"],
            "load_cmd": f"os_doctrine.py load {d}",
            "check_cmd": f"os_doctrine.py check {d} --text/--asset",
            "standing_floor": d == "safety_identity",
        })
    return {"task": text, "doctrines": out}

def main():
    ap = argparse.ArgumentParser(prog="os_doctrine_router.py"); sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("route"); r.add_argument("text")
    sub.add_parser("domains")
    a = ap.parse_args()
    if a.cmd == "route":
        res = route(a.text)
        print(f"TASK: {res['task']}\nDOCTRINES (ranked, floor last):")
        for d in res["doctrines"]:
            flag = " [STANDING FLOOR]" if d["standing_floor"] else ""
            print(f"  [{d['confidence']:11s}] {d['domain']:18s} sources {d['sources_present']} (certified {d['certified_sources']}){flag}")
            print(f"               load: {d['load_cmd']}")
    elif a.cmd == "domains":
        doctrine = _m("os_doctrine").DOCTRINE
        for d, doc in doctrine.items():
            conf, present, certified = confidence(d, doc)
            print(f"  [{conf:11s}] {d:18s} {len(present)}/{len(doc['sources'])} present, {len(certified)} certified")
    else: ap.print_help()
    return 0

if __name__ == "__main__": sys.exit(main())
