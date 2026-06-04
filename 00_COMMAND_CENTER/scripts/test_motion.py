#!/usr/bin/env python3
"""Regression suite for os_motion_qa.py + os_generate video estimator.
Runs on synthetic observations. No generation, no spend."""
import os, sys, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
def load(mod):
    spec = importlib.util.spec_from_file_location(mod, os.path.join(HERE, mod + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
MQ = load("os_motion_qa")
GEN = load("os_generate")

results = []
def check(name, cond):
    results.append((name, bool(cond))); print(f"  {'PASS' if cond else 'FAIL'}  {name}")

# minimal in-memory CRS spec + world (no disk needed)
CRS = {
    "identity_invariants": [
        {"key": "eye_color", "value": "deep-brown", "hard": True},
        {"key": "mole_below_left_eye", "value": "present", "hard": True},
        {"key": "build", "value": "lean", "hard": True},
        {"key": "hair_style", "value": "varies", "hard": False},
    ]
}
WORLD = {
    "environments": ["Brutalist Monument", "Monochromatic Void"],
    "forbidden_elements": ["logos", "crowds", "lens flare"],
    "color_system": {"palette_hex": ["#2B2B2E"]},
}
GOOD_OBS = {"eye_color": "deep-brown", "mole_below_left_eye": "present", "build": "lean", "hair_style": "varies"}
DRIFT_OBS = {"eye_color": "blue", "mole_below_left_eye": "absent", "build": "lean", "hair_style": "varies"}
CLEAN_MOTION = {"grounding": 2, "edge_integrity": 2, "temporal_stability": 2, "ai_tells": 2,
                "physics": 2, "register": 2, "beat_source": 2}


def clip(**over):
    base = {"clip_id": "c1",
            "scene": {"environment": "Brutalist Monument", "elements": ["single figure"], "palette_hex": ["#2B2B2E"]},
            "sampled_frames": [{"frame_id": "f0", "observed": dict(GOOD_OBS)},
                               {"frame_id": "f1", "observed": dict(GOOD_OBS)}],
            "motion": dict(CLEAN_MOTION)}
    base.update(over)
    return base


def main():
    # 1. clean clip ships
    r = MQ.judge_clip(CRS, WORLD, clip())
    check("clean clip -> SHIP", r["verdict"] == "SHIP")

    # 2. identity drift in a sampled frame quarantines
    r = MQ.judge_clip(CRS, WORLD, clip(sampled_frames=[
        {"frame_id": "f0", "observed": dict(GOOD_OBS)},
        {"frame_id": "f1", "observed": dict(DRIFT_OBS)}]))
    check("identity drift mid-clip -> QUARANTINE", r["verdict"] == "QUARANTINE" and r["identity_quarantined_frames"] == 1)

    # 3. forbidden element in scene quarantines (world gate carried)
    r = MQ.judge_clip(CRS, WORLD, clip(scene={"environment": "Brutalist Monument", "elements": ["logos"], "palette_hex": []}))
    check("forbidden world element -> QUARANTINE", r["verdict"] == "QUARANTINE" and r["world_failures"])

    # 4. off-rotation environment quarantines
    r = MQ.judge_clip(CRS, WORLD, clip(scene={"environment": "Beach", "elements": [], "palette_hex": []}))
    check("off-rotation environment -> QUARANTINE", r["verdict"] == "QUARANTINE")

    # 5. hard-zero motion item (grounding=0) quarantines even if everything else perfect
    m = dict(CLEAN_MOTION); m["grounding"] = 0
    r = MQ.judge_clip(CRS, WORLD, clip(motion=m))
    check("grounding=0 (HARD) -> QUARANTINE", r["verdict"] == "QUARANTINE" and "grounding" in r["hard_zero_items"])

    # 6. ai_tells=0 quarantines
    m = dict(CLEAN_MOTION); m["ai_tells"] = 0
    r = MQ.judge_clip(CRS, WORLD, clip(motion=m))
    check("ai_tells=0 (HARD) -> QUARANTINE", r["verdict"] == "QUARANTINE")

    # 7. low overall score (all soft+hard weak=1) below threshold quarantines
    m = {k: 1 for k in CLEAN_MOTION}
    r = MQ.judge_clip(CRS, WORLD, clip(motion=m), threshold=0.75)
    check("mediocre clip below threshold -> QUARANTINE", r["verdict"] == "QUARANTINE" and r["motion_score"] < 0.75)

    # 8. score exactly at threshold with no hard-zero ships
    m = {"grounding": 2, "edge_integrity": 2, "temporal_stability": 2, "ai_tells": 2, "physics": 1, "register": 1, "beat_source": 1}
    r = MQ.judge_clip(CRS, WORLD, clip(motion=m), threshold=0.75)
    check("score>=threshold + no hard-zero -> SHIP", r["verdict"] == "SHIP" and r["motion_score"] >= 0.75)

    # 9. cost estimator refuses to invent a rate
    est, note = GEN.estimate_video_credits(5, None)
    check("estimator refuses to invent a rate", est is None and "UNCONFIRMED" in note)

    # 10. cost estimator computes when given a rate
    est, note = GEN.estimate_video_credits(5, 4)
    check("estimator computes ceil(seconds*rate)", est == 20)

    npass = sum(1 for _, ok in results if ok); nfail = sum(1 for _, ok in results if not ok)
    print(f"\nRESULT: {npass} pass / {nfail} fail")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
