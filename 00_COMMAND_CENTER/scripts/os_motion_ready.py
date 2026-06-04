#!/usr/bin/env python3
"""
os_motion_ready.py , the pre-video readiness gate.

Before ANY video credit is spent, the approved still must clear EVERY gate. This
composes the Phase-1/2/3 gates into one verdict. READY only if all pass.

Checks:
  1. world          , scene continuity (os_world)
  2. pillars        , 4 hard identity invariants on the candidate (os_crs)
  3. face_match     , candidate matches the LOCKED hero (os_facematch; vision-confirmed)
  4. signature      , mole present OR a logged mark-injection exists
  5. vision_gate    , a PASS record exists for the asset
  6. harness_audit  , os_production audit returns no blockers

CLI:
  check --crs SLUG --world SLUG --scene JSON --frame-obs JSON
        --hero IMG --candidate IMG [--vision-facematch V]
        [--mark-log CSV] [--vision-gate PASS] [--audit-project NAME]
"""
import os, sys, json, csv, subprocess, argparse, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def _load(mod):
    spec = importlib.util.spec_from_file_location(mod, os.path.join(HERE, mod + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def assess(opts):
    """Pure-ish verdict; opts is a dict. Returns (verdict, checks)."""
    OS_CRS = _load("os_crs"); OS_WORLD = _load("os_world"); OS_FM = _load("os_facematch")
    checks = {}

    # 1. world
    world = OS_WORLD.load_world(opts["world"]) if opts.get("world") else None
    scene = json.load(open(opts["scene"])) if opts.get("scene") else {}
    if world is None:
        checks["world"] = (False, "world not found")
    else:
        fails, _ = OS_WORLD.evaluate_scene(world, scene)
        checks["world"] = (not fails, "; ".join(fails) or "ok")

    # 2. pillars
    crs = OS_CRS.load_crs(opts["crs"]) if opts.get("crs") else None
    obs = json.load(open(opts["frame_obs"])) if opts.get("frame_obs") else {}
    if isinstance(obs, list):
        obs = obs[0].get("observed", {}) if obs else {}
    elif "observed" in obs:
        obs = obs["observed"]
    if crs is None:
        checks["pillars"] = (False, "crs not found")
    else:
        score, hard_fail = OS_CRS.evaluate_frame(crs, obs)
        checks["pillars"] = (not hard_fail, f"score {score}" + (("; fail " + ",".join(h["key"] for h in hard_fail)) if hard_fail else ""))

    # 3. face_match vs locked hero
    if opts.get("hero") and opts.get("candidate"):
        res = OS_FM.judge(opts["hero"], opts["candidate"], opts.get("vision_facematch"))
        checks["face_match"] = (res["verdict"] == "PASS", f"{res['verdict']} (auto {res['auto_ssim']}, vision {res['vision_score']})")
    else:
        checks["face_match"] = (False, "hero/candidate not supplied")

    # 4. signature present OR logged injection
    sig_ok = str(obs.get("mole_below_left_eye", "")).lower() == "present"
    if not sig_ok and opts.get("mark_log") and os.path.exists(opts["mark_log"]):
        rows = list(csv.reader(open(opts["mark_log"])))[1:]
        sig_ok = any(opts.get("candidate", "") in r[2] or r[2] in opts.get("candidate", "") for r in rows if len(r) > 2)
        checks["signature"] = (sig_ok, "restored via logged mark-injection" if sig_ok else "mole absent + no injection log")
    else:
        checks["signature"] = (sig_ok, "present in frame" if sig_ok else "mole absent + no injection log")

    # 5. vision gate record
    checks["vision_gate"] = (str(opts.get("vision_gate", "")).upper() == "PASS",
                             opts.get("vision_gate", "(none)"))

    # 6. harness audit
    if opts.get("audit_project"):
        r = subprocess.run(["python3", os.path.join(HERE, "os_production.py"), "audit", opts["audit_project"]],
                           capture_output=True, text=True)
        checks["harness_audit"] = (r.returncode == 0, "clean" if r.returncode == 0 else "blockers present")
    else:
        checks["harness_audit"] = (False, "no --audit-project given")

    verdict = "READY" if all(ok for ok, _ in checks.values()) else "BLOCKED"
    return verdict, checks


def cmd_check(a):
    verdict, checks = assess(vars(a))
    print(f"  MOTION READINESS: {verdict}")
    for k, (ok, msg) in checks.items():
        print(f"    [{'PASS' if ok else 'BLOCK'}] {k:<14} {msg}")
    if verdict != "READY":
        print("  -> do NOT spend video credits until every check passes.")
    return 0 if verdict == "READY" else 1


def main():
    p = argparse.ArgumentParser(prog="os_motion_ready.py")
    sub = p.add_subparsers(dest="cmd")
    c = sub.add_parser("check")
    c.add_argument("--crs"); c.add_argument("--world"); c.add_argument("--scene"); c.add_argument("--frame-obs", dest="frame_obs")
    c.add_argument("--hero"); c.add_argument("--candidate")
    c.add_argument("--vision-facematch", type=float, default=None, dest="vision_facematch")
    c.add_argument("--mark-log", dest="mark_log", default=None)
    c.add_argument("--vision-gate", dest="vision_gate", default="")
    c.add_argument("--audit-project", dest="audit_project", default=None)
    a = p.parse_args()
    if a.cmd == "check":
        return cmd_check(a)
    p.print_help(); return 1


if __name__ == "__main__":
    sys.exit(main())
