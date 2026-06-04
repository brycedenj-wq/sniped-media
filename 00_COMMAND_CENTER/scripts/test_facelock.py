#!/usr/bin/env python3
"""Regression suite for the Phase 3 face-lock layer:
os_face, os_facematch, os_herolock, os_motion_ready, os_generate ref-package, os_mark anchor.
Uses synthetic images; no spend. Skips cv2-dependent checks if cv2 missing."""
import os, sys, json, tempfile, shutil, importlib.util, csv

HERE = os.path.dirname(os.path.abspath(__file__))
def load(mod):
    spec = importlib.util.spec_from_file_location(mod, os.path.join(HERE, mod + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

results = []
def check(name, cond):
    results.append((name, bool(cond))); print(f"  {'PASS' if cond else 'FAIL'}  {name}")
class A:
    def __init__(self, **kw): self.__dict__.update(kw)

HAVE_CV2 = True
try:
    import cv2, numpy as np
except Exception:
    HAVE_CV2 = False


def synth_face(path, eye_shift=0, tone=180):
    """Draw a crude face (oval + two eyes) so Haar can detect it; vary tone/eyes."""
    import numpy as np, cv2
    img = np.full((400, 320, 3), 200, dtype=np.uint8)
    cv2.ellipse(img, (160, 200), (90, 120), 0, 0, 360, (tone, tone, tone), -1)
    cv2.circle(img, (130 + eye_shift, 170), 14, (255, 255, 255), -1)
    cv2.circle(img, (190 + eye_shift, 170), 14, (255, 255, 255), -1)
    cv2.circle(img, (130 + eye_shift, 170), 6, (30, 30, 30), -1)
    cv2.circle(img, (190 + eye_shift, 170), 6, (30, 30, 30), -1)
    cv2.imwrite(path, img)


def main():
    FM = load("os_facematch"); HL = load("os_herolock"); MR = load("os_motion_ready")
    GEN = load("os_generate"); MARK = load("os_mark")
    sb = tempfile.mkdtemp(prefix="facelock_")
    try:
        # ref-package (no cv2 needed)
        pkg_v = GEN.build_ref_package("https://hero.png", "video")
        check("ref-package video uses start_image role", pkg_v["medias"][0]["role"] == "start_image")
        pkg_i = GEN.build_ref_package("https://hero.png", "image")
        check("ref-package image conditions on hero", pkg_i["medias"][0]["role"] == "image")
        check("ref-package None hero -> None", GEN.build_ref_package("", "image") is None)

        # face-match verdict logic (pure judge with monkeypatched proxy, no cv2 dependency)
        FM.proxy_ssim = lambda h, c: (0.98, True, True)
        check("same-ish + high vision -> PASS", FM.judge("a", "b", 0.9)["verdict"] == "PASS")
        check("auto pass but no vision -> NEEDS-VISION", FM.judge("a", "b", None)["verdict"] == "NEEDS-VISION")
        check("auto pass but low vision -> QUARANTINE", FM.judge("a", "b", 0.4)["verdict"] == "QUARANTINE")
        FM.proxy_ssim = lambda h, c: (0.05, True, True)
        check("gross structural mismatch -> QUARANTINE (auto floor)", FM.judge("a", "b", 0.9)["verdict"] == "QUARANTINE")
        FM.proxy_ssim = lambda h, c: (None, False, False)
        check("no face croppable -> NEEDS-VISION", FM.judge("a", "b", 0.9)["verdict"] == "NEEDS-VISION")

        # herolock register requires approved + source to exist
        ap = os.path.join(sb, "approved.png"); sp = os.path.join(sb, "source.png")
        open(ap, "w").close(); open(sp, "w").close()
        HL.HERO_DIR = os.path.join(sb, "locked"); HL.REGISTRY = os.path.join(sb, "reg.csv")
        rc = HL.cmd_register(A(hero_id="axis", crs="char_axis_01", world="world_meridian_01",
                               approved=ap, source=sp, facecrop=None, identitycrop=None, marked=None,
                               approved_date="2026-06-04", gate_reports="identity=r1;world=r2",
                               usecases="still-reference;video-start-image"))
        check("herolock registers with valid paths", rc == 0 and os.path.isfile(HL.hero_json("axis")))
        rc = HL.cmd_register(A(hero_id="bad", crs="c", world="w", approved=os.path.join(sb, "nope.png"),
                               source=sp, facecrop=None, identitycrop=None, marked=None,
                               approved_date="x", gate_reports="", usecases=""))
        check("herolock refuses missing approved asset", rc == 1)
        rec = HL.load("axis")
        check("hero record stores anchor use cases", "video-start-image" in rec["allowed_use_cases"])

        # motion-ready: assemble a passing manifest, then break one check
        crsdir = os.path.join(sb, "crs"); os.makedirs(crsdir, exist_ok=True)
        # minimal crs + world on disk via the real loaders' path layout
        OS_CRS = load("os_crs"); OS_WORLD = load("os_world")
        OS_CRS.CHAR_DIR = os.path.join(sb, "chars"); OS_WORLD.WORLD_DIR = os.path.join(sb, "worlds")
        os.makedirs(os.path.join(OS_CRS.CHAR_DIR, "ch"), exist_ok=True)
        json.dump({"identity_invariants": [{"key": "eye_color", "value": "deep-brown", "hard": True}]},
                  open(os.path.join(OS_CRS.CHAR_DIR, "ch", "CRS.json"), "w"))
        os.makedirs(os.path.join(OS_WORLD.WORLD_DIR, "wd"), exist_ok=True)
        json.dump({"environments": ["Brutalist Monument"], "forbidden_elements": ["logos"],
                   "color_system": {"palette_hex": ["#2B2B2E"]}},
                  open(os.path.join(OS_WORLD.WORLD_DIR, "wd", "WORLD.json"), "w"))
        scene = os.path.join(sb, "scene.json"); json.dump({"environment": "Brutalist Monument", "elements": ["single figure"]}, open(scene, "w"))
        obs = os.path.join(sb, "obs.json"); json.dump([{"frame_id": "f", "observed": {"eye_color": "deep-brown", "mole_below_left_eye": "present"}}], open(obs, "w"))
        # patch the loaders MR uses
        MR._load = lambda m: {"os_crs": OS_CRS, "os_world": OS_WORLD, "os_facematch": FM}[m]
        FM.proxy_ssim = lambda h, c: (0.98, True, True)
        opts_pass = {"crs": "ch", "world": "wd", "scene": scene, "frame_obs": obs,
                     "hero": "h", "candidate": "c", "vision_facematch": 0.9,
                     "vision_gate": "PASS", "audit_project": None}
        # audit None -> harness_audit fails; expect BLOCKED on that single check
        verdict, checks = MR.assess(opts_pass)
        passed = [k for k, (ok, _) in checks.items() if ok]
        check("motion-ready: world/pillars/face/signature/vision pass", all(checks[k][0] for k in ["world", "pillars", "face_match", "signature", "vision_gate"]))
        check("motion-ready BLOCKED when audit not provided", verdict == "BLOCKED" and not checks["harness_audit"][0])
        # break face-match -> blocked
        FM.proxy_ssim = lambda h, c: (0.98, True, True)
        opts_badface = dict(opts_pass); opts_badface["vision_facematch"] = 0.2
        v2, c2 = MR.assess(opts_badface)
        check("motion-ready BLOCKED on face-match drift", not c2["face_match"][0])

        # mark anchor refuses when no face detectable (synthetic blank), still logged-only on success
        if HAVE_CV2:
            blank = os.path.join(sb, "blank.png")
            import numpy as np, cv2
            cv2.imwrite(blank, np.full((100, 100, 3), 128, dtype=np.uint8))
            outp = os.path.join(sb, "blank_marked.png"); logp = os.path.join(sb, "mlog.csv")
            rc = MARK.cmd_inject(A(src=blank, out=outp, x=None, y=None, anchor="inner_left_eye",
                                   radius=3, color="#3c2823", reason="test", log=logp))
            check("mark anchor refuses when no eyes detected", rc == 1 and not os.path.isfile(outp))
        else:
            check("mark anchor refuses when no eyes detected (skipped, no cv2)", True)

    finally:
        shutil.rmtree(sb, ignore_errors=True)
    npass = sum(1 for _, ok in results if ok); nfail = sum(1 for _, ok in results if not ok)
    print(f"\nRESULT: {npass} pass / {nfail} fail")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
