#!/usr/bin/env python3
"""
os_motion_qa.py , Motion / video QA gate.

Proves the OS controls MOTION the same way it controls character and world.
A clip is judged on three stacked gates, all carried from Phase 1:
  A. identity-hold , every sampled frame must hold AXIS's hard invariants (os_crs core)
  B. world-continuity , the scene must stay inside MERIDIAN-HOUSE (os_world core)
  C. motion rubric , 7 visual-motion items scored 0..2

Verdict SHIP only if: no identity quarantine, world passes, no hard-zero motion item,
and overall motion score >= threshold. SHIP means "eligible for human taste", NOT auto-post.
No generation here. Runs on declared observations (synthetic now, vision-filled later).

Commands:
  rubric                                    print the motion QA rubric
  gate --crs SLUG --world SLUG --clip FILE [--threshold 0.75]   judge a clip
"""
import os, sys, json, argparse, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def _load(mod):
    spec = importlib.util.spec_from_file_location(mod, os.path.join(HERE, mod + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

OS_CRS = _load("os_crs")
OS_WORLD = _load("os_world")

# Motion rubric: each item scored 0 (fail) / 1 (weak) / 2 (clean).
# HARD-ZERO items quarantine the clip outright if scored 0.
RUBRIC = [
    ("grounding",          True,  "feet/contact + shadow anchored to the floor; no floating or sliding"),
    ("edge_integrity",     True,  "stable silhouette; no warping, melting, or boiling edges"),
    ("temporal_stability", True,  "no flicker; no identity morph or texture crawl frame-to-frame"),
    ("ai_tells",           True,  "no extra/fused fingers mid-motion, no face warp, no melt artifacts"),
    ("physics",            False, "plausible body/cloth/hair motion; no impossible deformation"),
    ("register",           False, "motion matches AXIS's register (composed, no out-of-register gestures)"),
    ("beat_source",        False, "the clip beats a static hero still as a moving asset (taste-assisted)"),
]
HARD_MOTION = [k for (k, hard, _) in RUBRIC if hard]
MAX_SCORE = 2 * len(RUBRIC)


def cmd_rubric(a):
    print("MOTION QA RUBRIC (0=fail, 1=weak, 2=clean):")
    for k, hard, desc in RUBRIC:
        tag = "HARD" if hard else "soft"
        print(f"  [{tag}] {k:<18} {desc}")
    print(f"\n  + identity-hold gate (AXIS hard invariants, per sampled frame)  [HARD]")
    print(f"  + world-continuity gate (MERIDIAN-HOUSE forbidden/env)         [HARD]")
    print(f"  SHIP requires: no identity quarantine, world pass, no HARD motion item == 0, score >= threshold.")
    print(f"  SHIP = eligible for human taste approval, never auto-post.")
    return 0


def judge_clip(crs_spec, world, clip, threshold=0.75):
    """Pure function , returns a verdict dict. Reused by tests."""
    reasons = []
    # A. identity-hold across sampled frames (reuse os_crs core)
    frame_results = []
    id_quar = 0
    for fr in clip.get("sampled_frames", []):
        score, hard_fail = OS_CRS.evaluate_frame(crs_spec, fr.get("observed", {}))
        q = bool(hard_fail) or score < 0.9
        if q:
            id_quar += 1
            reasons.append(f"identity drift in {fr.get('frame_id','?')}: " +
                           ",".join(h["key"] for h in hard_fail) if hard_fail else
                           f"identity score {score} < 0.9 in {fr.get('frame_id','?')}")
        frame_results.append({"frame_id": fr.get("frame_id", "?"), "score": score,
                              "hard_failures": hard_fail, "quarantined": q})
    # B. world continuity (reuse os_world core)
    world_fail, world_warn = OS_WORLD.evaluate_scene(world, clip.get("scene", {}))
    for wf in world_fail:
        reasons.append(f"world: {wf}")
    # C. motion rubric
    motion = clip.get("motion", {})
    item_scores = {}
    hard_zero = []
    total = 0
    for k, hard, _ in RUBRIC:
        v = int(motion.get(k, 0))
        v = max(0, min(2, v))
        item_scores[k] = v
        total += v
        if hard and v == 0:
            hard_zero.append(k)
            reasons.append(f"motion HARD-zero: {k}")
    score = round(total / MAX_SCORE, 3)
    if score < threshold:
        reasons.append(f"motion score {score} < threshold {threshold}")

    ship = (id_quar == 0) and (not world_fail) and (not hard_zero) and (score >= threshold)
    return {
        "clip_id": clip.get("clip_id", "?"),
        "verdict": "SHIP" if ship else "QUARANTINE",
        "motion_score": score,
        "threshold": threshold,
        "identity_quarantined_frames": id_quar,
        "world_failures": world_fail,
        "world_warnings": world_warn,
        "motion_items": item_scores,
        "hard_zero_items": hard_zero,
        "frames": frame_results,
        "reasons": reasons,
    }


def cmd_gate(a):
    crs_spec = OS_CRS.load_crs(a.crs)
    if crs_spec is None:
        print(f"  CRS not found: {a.crs}"); return 1
    world = OS_WORLD.load_world(a.world)
    if world is None:
        print(f"  world not found: {a.world}"); return 1
    with open(a.clip, "r", encoding="utf-8") as f:
        clip = json.load(f)
    res = judge_clip(crs_spec, world, clip, a.threshold)
    # write report next to the production package if a dir is implied, else cwd
    outdir = os.path.dirname(os.path.abspath(a.clip))
    outp = os.path.join(outdir, "MOTION_QA_REPORT.json")
    with open(outp, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)
    print(f"  MOTION QA: {res['clip_id']} -> {res['verdict']} "
          f"(score {res['motion_score']}, id-quarantined frames {res['identity_quarantined_frames']})")
    if res["verdict"] != "SHIP":
        for r in res["reasons"]:
            print(f"    - {r}")
    for w in res["world_warnings"]:
        print(f"    ~ {w}")
    print(f"  report: {outp}")
    return 0 if res["verdict"] == "SHIP" else 1


def main():
    p = argparse.ArgumentParser(prog="os_motion_qa.py")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("rubric")
    g = sub.add_parser("gate")
    g.add_argument("--crs", required=True); g.add_argument("--world", required=True)
    g.add_argument("--clip", required=True); g.add_argument("--threshold", type=float, default=0.75)
    a = p.parse_args()
    if a.cmd == "rubric":
        return cmd_rubric(a)
    if a.cmd == "gate":
        return cmd_gate(a)
    p.print_help(); return 1


if __name__ == "__main__":
    sys.exit(main())
