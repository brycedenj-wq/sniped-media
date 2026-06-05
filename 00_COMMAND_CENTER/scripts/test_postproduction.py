#!/usr/bin/env python3
"""Smoke + contract tests for the post-production layer. Each script must run, produce an artifact,
log it, and refuse in-place edits. Run: python3 test_postproduction.py"""
import os, sys, csv, json, subprocess, tempfile, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
def load(n):
    s = importlib.util.spec_from_file_location(n, os.path.join(HERE, n + ".py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

P = 0; F = 0
def ok(c, m):
    global P, F
    if c: P += 1; print(f"  PASS {m}")
    else: F += 1; print(f"  FAIL {m}")

def main():
    from PIL import Image
    A = load("os_adobe_asset"); G = load("os_adobe_grade")
    C = load("os_adobe_composite"); R = load("os_adobe_reframe"); GATE = load("os_postproduction_gate")
    with tempfile.TemporaryDirectory() as d:
        run = os.path.join(d, "run");
        for sub in ("00_raw","01_graded","02_composite","03_exports","10_logs"): os.makedirs(os.path.join(run, sub))
        log = os.path.join(run, "10_logs", "EDIT_LOG.csv")
        raw = os.path.join(run, "00_raw", "t.png")
        # build a test image with a red patch (so colorlaw has something to keep)
        im = Image.new("RGB", (400, 600), (90, 92, 95));
        for x in range(180,220):
            for y in range(40,70): im.putpixel((x,y), (180, 30, 24))
        im.save(raw)

        ok(A.asset_id(raw) and len(A.asset_id(raw)) == 16, "asset: id computed")
        try:
            A.guard_not_inplace(raw, raw); ok(False, "asset: in-place guard raises")
        except SystemExit: ok(True, "asset: in-place guard raises")

        graded = os.path.join(run, "01_graded", "t.png")
        G.apply_grade(raw, graded, os.path.join(os.path.dirname(HERE), "postproduction/specs/SNIPED_LUXURY_GRADE.json"), log)
        ok(os.path.exists(graded), "grade: artifact produced")
        ok(A.sha1_file(graded) != A.sha1_file(raw), "grade: output differs from source")

        comp = os.path.join(run, "02_composite", "t.png")
        C.colorlaw(graded, comp, 5, 30, 0.12, 1.15, log)
        ok(os.path.exists(comp), "composite: colorlaw artifact produced")

        glyph = os.path.join(run, "02_composite", "tg.png")
        C.glyph(comp, glyph, 50, 50, "LOT 00", 22, [150,28,22], log)
        ok(os.path.exists(glyph), "composite: glyph artifact produced")

        res = R.run(comp, os.path.join(run, "03_exports"),
                    os.path.join(os.path.dirname(HERE), "postproduction/specs/SNIPED_EXPORT_SPECS.json"), (0.5,0.55), log)
        specs = json.load(open(os.path.join(os.path.dirname(HERE), "postproduction/specs/SNIPED_EXPORT_SPECS.json")))["specs"]
        ok(len(res) == len(specs), f"reframe: {len(res)} exports == {len(specs)} specs")

        clip = os.path.join(d, "src.mp4"); out = os.path.join(run, "cut.mp4")
        subprocess.run(["ffmpeg","-y","-f","lavfi","-i","testsrc=size=320x240:rate=24:duration=1",
                        "-pix_fmt","yuv420p", clip], capture_output=True)
        CUT = load("os_adobe_cut")
        CUT.run(clip, out, 0, 1, True, "240x426", True, 24, log)
        ok(os.path.exists(out) and os.path.getsize(out) > 0, "cut: muted resized clip produced")

        rows = list(csv.DictReader(open(log)))
        ok(len(rows) >= 5, f"log: {len(rows)} edit rows recorded (non-silent)")

        v, checks = GATE.run_gate(run, comp, None,
                    os.path.join(os.path.dirname(HERE), "postproduction/specs/SNIPED_EXPORT_SPECS.json"),
                    {"identity_withheld":"PASS","beats_source":"PASS","text_legible":"PASS"})
        ok(v in ("SHIP","FIX","REJECT"), f"gate: returned verdict ({v})")
        ok(checks["grade_applied"] == "PASS", "gate: detects grade applied")
        ok(os.path.exists(os.path.join(run,"10_logs","POSTPROD_GATE_LOG.csv")), "gate: wrote gate log")

    print(f"\n{P} passed, {F} failed")
    return 1 if F else 0

if __name__ == "__main__":
    sys.exit(main())
