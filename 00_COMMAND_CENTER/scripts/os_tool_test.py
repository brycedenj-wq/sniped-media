#!/usr/bin/env python3
"""
os_tool_test.py , runs tool-route tests end to end, producing a real artifact + log row per route.
Proves the router/registry are not theory: each ACTIVE local route executes and validates.

  os_tool_test.py run [--outdir DIR]
"""
import os, sys, csv, json, time, subprocess, argparse, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__)); CC = os.path.dirname(HERE)
def _m(n):
    s = importlib.util.spec_from_file_location(n, os.path.join(HERE, n + ".py")); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd", nargs="?", default="run")
    ap.add_argument("--outdir", default=os.path.join(CC, "OS_OVERNIGHT_MAX_OPERATING_SPRINT_001", "01_TOOLCHAIN", "route_tests"))
    a = ap.parse_args()
    out = a.outdir; os.makedirs(out, exist_ok=True)
    log = os.path.join(out, "ROUTE_TEST_LOG.csv")
    rows = []
    from PIL import Image
    router = _m("os_tool_router"); layout = _m("os_adobe_layout")
    grade = _m("os_adobe_grade"); cut = _m("os_adobe_cut")
    # a small source image with a red patch
    src = os.path.join(out, "_src.png"); im = Image.new("RGB", (600, 800), (92, 94, 97))
    for x in range(260, 340):
        for y in range(80, 130): im.putpixel((x, y), (170, 30, 24))
    im.save(src)

    def record(route, ok, artifact, detail):
        rows.append((route, "PASS" if ok else "FAIL", artifact, detail))

    # 1 classify route
    rid = router.classify("build me the full campaign package from this hero")
    record("classify", rid == "make_campaign_package", "-", f"-> {rid}")
    # 2 edit_image
    try:
        o = os.path.join(out, "t_edit.png"); grade.apply_grade(src, o, os.path.join(CC, "postproduction/specs/SNIPED_LUXURY_GRADE.json"), None)
        record("edit_image", os.path.exists(o), o, "graded")
    except Exception as e: record("edit_image", False, "-", str(e)[:60])
    # 3 update_dashboard
    try:
        o = os.path.join(out, "t_dash.png"); layout.dashboard(o, "ROUTE TEST", "toolchain self-test", [("edit_image","PASS",""),("cut_video","PASS",""),("generate_pdf","PASS","")])
        record("update_dashboard", os.path.exists(o), o, "dashboard rendered")
    except Exception as e: record("update_dashboard", False, "-", str(e)[:60])
    # 4 build_landing_page
    try:
        o = os.path.join(out, "t_landing.png"); layout.landing(src, o, "Route test headline", "subhead", "Request access")
        record("build_landing_page", os.path.exists(o), o, "landing rendered")
    except Exception as e: record("build_landing_page", False, "-", str(e)[:60])
    # 5 generate_pdf (Pillow images -> PDF)
    try:
        o = os.path.join(out, "t_doc.pdf")
        imgs = [Image.open(os.path.join(out, f)).convert("RGB") for f in ("t_dash.png", "t_landing.png") if os.path.exists(os.path.join(out, f))]
        imgs[0].save(o, save_all=True, append_images=imgs[1:])
        record("generate_pdf", os.path.exists(o) and os.path.getsize(o) > 0, o, f"{len(imgs)} pages")
    except Exception as e: record("generate_pdf", False, "-", str(e)[:60])
    # 6 cut_video (synthetic clip)
    try:
        clip = os.path.join(out, "_src.mp4")
        subprocess.run(["ffmpeg","-y","-f","lavfi","-i","testsrc=size=320x240:rate=24:duration=1","-pix_fmt","yuv420p",clip], capture_output=True)
        o = os.path.join(out, "t_cut.mp4"); cut.run(clip, o, 0, 1, True, "240x426", True, 24, None)
        record("cut_video", os.path.exists(o) and os.path.getsize(o) > 0, o, "muted caption-safe")
    except Exception as e: record("cut_video", False, "-", str(e)[:60])
    # 7 score_money_path
    try:
        mp = _m("os_money_path")
        r = mp.score({"has_glyph":1,"has_color_law":1,"faceless_safe":1,"identity_safe":1,"asset_shippable":1,"has_physical_product":1,"has_recurring_revenue":1,"has_licensing_lane":1,"low_capital":1,"fast_first_dollar":1,"low_legal_risk":1,"demand_proven":0})
        record("score_money_path", 0 <= r["score"] <= 100, "-", f"score={r['score']} band={r['band']}")
    except Exception as e: record("score_money_path", False, "-", str(e)[:60])
    # 8 run_launch_readiness_check
    try:
        lc = _m("os_launch_check"); checks = lc.run_checks()
        record("run_launch_readiness_check", len(checks) >= 8, "-", f"{len(checks)} checks")
    except Exception as e: record("run_launch_readiness_check", False, "-", str(e)[:60])

    new = not os.path.exists(log)
    with open(log, "a", newline="") as f:
        w = csv.writer(f)
        if new: w.writerow(["ts", "route", "verdict", "artifact", "detail"])
        for route, v, art, det in rows:
            w.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), route, v, os.path.relpath(art, CC) if art != "-" else "-", det])
    npass = sum(1 for _, v, _, _ in rows if v == "PASS")
    print(f"ROUTE TESTS: {npass}/{len(rows)} PASS")
    for route, v, art, det in rows:
        print(f"  {'OK ' if v=='PASS' else '!! '}{v}  {route:26s} {det}")
    print(f"  log: {log}")
    return 0 if npass == len(rows) else 1

if __name__ == "__main__": sys.exit(main())
