#!/usr/bin/env python3
"""
os_facematch.py , face-match gate: "does this still look like the approved hero?"

HONEST design. No face-embedding model is installed, so this gate does NOT claim
automated face recognition. It combines:
  A. a structural proxy (SSIM on cv2-aligned grayscale face crops) , screens GROSS
     drift automatically; it can FAIL a frame but can never solely PASS it.
  B. a required vision-assisted identity score (operator/Claude reads a side-by-side
     and scores 0..1) , this is the authoritative "is it the same person" call.
A PASS needs BOTH: auto_score >= floor AND vision_score >= threshold.
Missing vision_score -> NEEDS-VISION (writes a side-by-side crop to read).
If/when a face-embedding ONNX model is added, swap the proxy for cosine similarity.

CLI:
  gate --hero IMG --candidate IMG [--vision-score V] [--floor 0.15] [--threshold 0.70] [--out SIDEBYSIDE] [--log CSV]
"""
import os, sys, csv, time, argparse


def proxy_ssim(hero_path, candidate_path):
    """Return (ssim 0..1 clamped, hero_face_detected, cand_face_detected)."""
    import importlib.util, numpy as np
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location("os_face", os.path.join(here, "os_face.py"))
    of = importlib.util.module_from_spec(spec); spec.loader.exec_module(of)
    from skimage.metrics import structural_similarity as ssim
    h = of.aligned_face_crop(hero_path); c = of.aligned_face_crop(candidate_path)
    if h is None or c is None:
        return None, False, False
    score = ssim(h, c)
    return max(0.0, float(score)), of.detect_face(hero_path) is not None, of.detect_face(candidate_path) is not None


def write_sidebyside(hero_path, candidate_path, out):
    import importlib.util
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location("os_face", os.path.join(here, "os_face.py"))
    of = importlib.util.module_from_spec(spec); spec.loader.exec_module(of)
    import cv2, numpy as np
    h = of.aligned_face_crop(hero_path, 256); c = of.aligned_face_crop(candidate_path, 256)
    if h is None or c is None:
        return False
    gap = np.full((256, 8), 255, dtype=h.dtype)
    cv2.imwrite(out, np.hstack([h, gap, c]))
    return True


def judge(hero_path, candidate_path, vision_score=None, floor=0.15, threshold=0.70):
    """Pure verdict function (reused by tests)."""
    auto, hero_ok, cand_ok = proxy_ssim(hero_path, candidate_path)
    reasons = []
    if auto is None:
        return {"verdict": "NEEDS-VISION", "auto_ssim": None, "vision_score": vision_score,
                "reasons": ["could not crop one/both faces; vision read required"],
                "hero_face_detected": hero_ok, "candidate_face_detected": cand_ok}
    if not (hero_ok and cand_ok):
        reasons.append("face not detected on one side; auto proxy unreliable, vision read required")
    if auto < floor:
        return {"verdict": "QUARANTINE", "auto_ssim": round(auto, 3), "vision_score": vision_score,
                "reasons": [f"auto structural proxy {round(auto,3)} < floor {floor}: gross mismatch"],
                "hero_face_detected": hero_ok, "candidate_face_detected": cand_ok}
    if vision_score is None:
        reasons.append("auto proxy passed the floor; vision identity score required to PASS")
        return {"verdict": "NEEDS-VISION", "auto_ssim": round(auto, 3), "vision_score": None,
                "reasons": reasons, "hero_face_detected": hero_ok, "candidate_face_detected": cand_ok}
    if vision_score >= threshold:
        return {"verdict": "PASS", "auto_ssim": round(auto, 3), "vision_score": vision_score,
                "reasons": reasons + [f"vision score {vision_score} >= {threshold}"],
                "hero_face_detected": hero_ok, "candidate_face_detected": cand_ok}
    return {"verdict": "QUARANTINE", "auto_ssim": round(auto, 3), "vision_score": vision_score,
            "reasons": reasons + [f"vision score {vision_score} < {threshold}: not the same person"],
            "hero_face_detected": hero_ok, "candidate_face_detected": cand_ok}


def cmd_gate(a):
    res = judge(a.hero, a.candidate, a.vision_score, a.floor, a.threshold)
    if a.out:
        ok = write_sidebyside(a.hero, a.candidate, a.out)
        if ok:
            print(f"  side-by-side (hero | candidate) -> {a.out}  (Read it, then re-run with --vision-score)")
    print(f"  FACE-MATCH: {res['verdict']}  auto_ssim={res['auto_ssim']} vision={res['vision_score']}")
    for r in res["reasons"]:
        print(f"    - {r}")
    if a.log:
        new = not os.path.exists(a.log)
        os.makedirs(os.path.dirname(a.log) or ".", exist_ok=True)
        with open(a.log, "a", newline="") as f:
            w = csv.writer(f)
            if new:
                w.writerow(["ts", "hero", "candidate", "verdict", "auto_ssim", "vision_score", "reasons"])
            w.writerow([time.strftime("%Y-%m-%d %H:%M"), a.hero, a.candidate, res["verdict"],
                        res["auto_ssim"], res["vision_score"], " | ".join(res["reasons"])])
        print(f"  logged -> {a.log}")
    return 0 if res["verdict"] == "PASS" else (2 if res["verdict"] == "NEEDS-VISION" else 1)


def main():
    p = argparse.ArgumentParser(prog="os_facematch.py")
    sub = p.add_subparsers(dest="cmd")
    g = sub.add_parser("gate")
    g.add_argument("--hero", required=True); g.add_argument("--candidate", required=True)
    g.add_argument("--vision-score", type=float, default=None, dest="vision_score")
    g.add_argument("--floor", type=float, default=0.15); g.add_argument("--threshold", type=float, default=0.70)
    g.add_argument("--out", default=None); g.add_argument("--log", default=None)
    a = p.parse_args()
    if a.cmd == "gate":
        return cmd_gate(a)
    p.print_help(); return 1


if __name__ == "__main__":
    sys.exit(main())
