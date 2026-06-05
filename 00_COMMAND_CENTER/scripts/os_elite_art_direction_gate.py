#!/usr/bin/env python3
"""
os_elite_art_direction_gate.py , the standard that rejects "merely clean".

The post-production gate proves an asset is finished and safe. It does NOT prove the work is ELITE.
This gate exists because clean-but-generic passed every other gate and still was not sellable at the
highest level. It scores the things a serious creative director actually judges, and it refuses to
call competent work elite.

Scoring is model-judged (the model Reads the assets and scores each dimension 0-3) EXCEPT the
template-leak check, which is deterministic (boilerplate tokens from another world = automatic
non-template FAIL). 0=absent 1=weak 2=strong 3=undeniable.

  os_elite_art_direction_gate.py rubric
  os_elite_art_direction_gate.py score --scores "concept=1,tension=1,..." [--world AXIS] [--copy "..."] [--log L]
"""
import sys, csv, os, time, argparse

DIMENSIONS = [
  ("concept_originality",   "a real idea, not a mood; could not be any AI campaign"),
  ("emotional_tension",     "desire/danger/intimacy/stakes; it makes you feel, not just calm"),
  ("symbol_system",         "a mark + recurring object/motif + meaning the world is built on"),
  ("editorial_authority",   "reads like an authored fashion/editorial campaign, not a render"),
  ("cinematic_sequence",    "shots imply a sequence with range; not one location reframed"),
  ("typography_quality",    "an owned type system (pairing, grid, tracking), not a default serif"),
  ("layout_hierarchy",      "deliberate hierarchy + negative space; eye is led; nothing filler"),
  ("non_template_feel",     "does not read like a magazine template applied to a photo"),
  ("anti_ai_slop",          "no AI tells: impossible architecture, pasted scale, plastic skin"),
  ("campaign_sellability",  "a buyer understands the value fast; a CD would not reject it"),
  ("world_depth",           "range + tension + lineage specificity; a world, not a look"),
  ("proof_loop_usefulness", "advances a real proof loop, not just a pretty artifact"),
]
KEYS = [k for k, _ in DIMENSIONS]
MAXP = 3 * len(DIMENSIONS)  # 36

# boilerplate tokens that mean a different world leaked in (deterministic non-template FAIL)
WORLD_BOILERPLATE = {
  "THE ESTATE OF HER", "LOT 00", "DEED CERTIFICATES",
}

def verdict(total, mins, template_clean):
    if total >= 30 and mins >= 2 and template_clean:
        return "ELITE"
    if total >= 24 and template_clean:
        return "STRONG BUT NOT ELITE"
    if total >= 16:
        return "CLEAN BUT GENERIC"
    return "REJECT"

def cmd_rubric():
    print("ELITE ART DIRECTION RUBRIC (0=absent 1=weak 2=strong 3=undeniable):")
    for k, d in DIMENSIONS:
        print(f"  {k:24s} {d}")
    print(f"\n  max {MAXP}. ELITE >=30 AND every dim >=2 AND non-template clean.")
    print( "  STRONG 24-29 | CLEAN BUT GENERIC 16-23 | REJECT <16.")
    print( "  non_template_feel auto-FAILs if another world's boilerplate is detected in the copy.")
    return 0

def cmd_score(a):
    scores = {}
    for pair in (a.scores or "").split(","):
        if "=" in pair:
            k, v = pair.split("=", 1); k = k.strip()
            try: scores[k] = max(0, min(3, int(v)))
            except ValueError: pass
    missing = [k for k in KEYS if k not in scores]
    if missing:
        print(f"  missing scores for: {', '.join(missing)}"); return 2
    # deterministic template-leak check
    copy = (a.copy or "").upper()
    leaked = [t for t in WORLD_BOILERPLATE if t in copy and (a.world or "").upper() not in t]
    template_clean = (not leaked) and scores["non_template_feel"] >= 2
    if leaked:
        scores["non_template_feel"] = 0
    total = sum(scores[k] for k in KEYS)
    mins = min(scores[k] for k in KEYS)
    v = verdict(total, mins, template_clean)
    print(f"ELITE ART DIRECTION GATE: {v}   ({total}/{MAXP}, weakest dim {mins})")
    for k in KEYS:
        flag = "OK " if scores[k] >= 2 else "!! "
        print(f"  {flag}{k:24s} {scores[k]}/3")
    if leaked:
        print(f"  !! TEMPLATE LEAK (auto non-template FAIL): {leaked}")
    weak = [k for k in KEYS if scores[k] < 2]
    if weak:
        print(f"  fix to reach ELITE: {', '.join(weak)}")
        print("  SELF-SOLVE: os_technique_cards.py solve \"" + " ".join(weak[:4]).replace('_',' ') + "\"")
    if a.log:
        os.makedirs(os.path.dirname(a.log), exist_ok=True)
        new = not os.path.exists(a.log)
        with open(a.log, "a", newline="") as f:
            w = csv.writer(f)
            if new: w.writerow(["ts", "world", "verdict", "total", "weakest"] + KEYS)
            w.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), a.world or "", v, total, mins] + [scores[k] for k in KEYS])
    return 0 if v == "ELITE" else 1

def main():
    ap = argparse.ArgumentParser(prog="os_elite_art_direction_gate.py"); sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("rubric")
    s = sub.add_parser("score"); s.add_argument("--scores", required=True); s.add_argument("--world", default="")
    s.add_argument("--copy", default=""); s.add_argument("--log", default="")
    a = ap.parse_args()
    if a.cmd == "rubric": return cmd_rubric()
    if a.cmd == "score": return cmd_score(a)
    ap.print_help(); return 1

if __name__ == "__main__": sys.exit(main())
