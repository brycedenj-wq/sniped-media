#!/usr/bin/env python3
"""
os_campaign.py , one command, full campaign kit. Orchestrates the proven post-production scripts.

NO new generation, NO motion generation (the teaser is still-based Ken Burns on the hero). One
approved hero in -> registered asset, grade + color-law final, the full export set, poster, title
card, landing, one-sheet, lookbook, thumbnail, carousel, still-based teaser, pitch board, proof
dashboard, caption, edit log, gate report, operator note. Every step logged; failures are marked,
never hidden; the run continues so you see the whole picture.

  os_campaign.py run --src HERO --name RUNNAME [--config campaign.json] [--model-scores "k=PASS,..."]
  os_campaign.py defaults    (print the baked-in LOT 00 config)

Gate taste checks (identity_withheld / beats_source / text_legible) default to PENDING unless given
via --model-scores, so the command never silently passes an asset no human has seen.
"""
import os, sys, json, shutil, argparse, importlib.util, traceback

HERE = os.path.dirname(os.path.abspath(__file__))
CC = os.path.dirname(HERE)
SPECS = os.path.join(CC, "postproduction", "specs")

def _mod(name):
    s = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

DEFAULT_CONFIG = {
    "lot": "LOT 00", "world": "THE ESTATE OF HER",
    "poster_masthead": "LOT 00",
    "poster_logline": "An heir, sold with the house that made her.",
    "poster_footer": "estate of her  .  lots 00 to 315  .  sold as seen",
    "title_kicker": "an estate liquidation", "title_main": "THE ESTATE OF HER",
    "title_sub": "everything, even the bloodline, is for sale",
    "landing_headline": "The bloodline conveys with the furniture.",
    "landing_sub": "A serialized estate catalogue. New lots weekly.",
    "landing_cta": "Request the catalogue",
    "onesheet_title": "LOT 00 , The Sitter",
    "onesheet_logline": "A synthetic heir, catalogued for auction with the estate that made her.",
    "onesheet_details": "world:The Estate of Her;medium:editorial campaign system;format:serialized lot catalogue;status:internal proof;reserve:none",
    "lookbook_caption": "Provenance: the house, entire. Condition as seen, the frayed tag original to the lot.",
    "thumbnail_kicker": "the estate of her", "thumbnail_title": ["THE", "ESTATE", "OF HER"],
    "caption": "LOT 00. The Sitter.\nProvenance: the house, entire.\nOffered with the estate that made her. Reserve: none.\nThe bloodline conveys with the furniture.",
    "carousel": [
        {"kind": "cover", "masthead": "LOT 00", "kicker": "the estate of her", "title": "an estate liquidation, in lots"},
        {"kind": "text", "bg": "ink", "kicker": "lot 00", "title": "The Sitter", "body": "A synthetic heir, catalogued for auction with the estate that made her. Offered entire."},
        {"kind": "image", "fx": 0.30, "fy": 0.30, "cap": "every ancestor, tagged"},
        {"kind": "image", "fx": 0.62, "fy": 0.78, "cap": "lot 00, sold as seen"},
        {"kind": "text", "bg": "paper", "kicker": "next", "title": "Which lot sells next.", "body": "New lots weekly. The catalogue appreciates."}
    ],
    # teaser beats: image crops are FRACTIONS of the source (0..1), converted to px at run time
    "teaser_beats": [
        {"type": "title", "kicker": "an estate liquidation", "title": "THE ESTATE OF HER", "subtitle": "everything is catalogued", "bg": "ink", "dur": 2.6},
        {"type": "image", "fcrop": [0, 0, 1, 1], "move": "in", "dur": 3.2},
        {"type": "image", "fcrop": [0.14, 0.05, 0.75, 0.64], "move": "in", "dur": 2.8},
        {"type": "image", "fcrop": [0.56, 0.68, 0.93, 0.96], "move": "in", "dur": 3.0},
        {"type": "title", "kicker": "lot 00", "title": "Sold as seen.", "subtitle": "the bloodline conveys with the furniture", "bg": "paper", "dur": 2.6}
    ]
}

def run_campaign(src, name, cfg, model_scores):
    A = _mod("os_adobe_asset"); G = _mod("os_adobe_grade"); C = _mod("os_adobe_composite")
    R = _mod("os_adobe_reframe"); L = _mod("os_adobe_layout"); T = _mod("os_adobe_teaser")
    GATE = _mod("os_postproduction_gate")
    from PIL import Image

    run = os.path.join(CC, "postproduction", name)
    for sub in ("00_raw", "01_graded", "02_composite", "03_exports", "04_artifacts", "04_artifacts/carousel", "04_motion", "10_logs"):
        os.makedirs(os.path.join(run, sub), exist_ok=True)
    log = os.path.join(run, "10_logs", "EDIT_LOG.csv")
    grade_spec = os.path.join(SPECS, "SNIPED_LUXURY_GRADE.json")
    export_spec = os.path.join(SPECS, "SNIPED_EXPORT_SPECS.json")
    A_ = os.path.join(run, "04_artifacts")
    steps = []  # (label, status, detail)

    def step(label, fn):
        try:
            out = fn(); steps.append((label, "ACTIVE", os.path.relpath(out, run) if isinstance(out, str) else "ok")); return out
        except Exception as e:
            steps.append((label, "FAIL", str(e).split("\n")[0][:120]))
            sys.stderr.write(f"[FAIL] {label}: {e}\n{traceback.format_exc()[-400:]}\n"); return None

    raw = os.path.join(run, "00_raw", "hero.png")
    step("registered asset", lambda: (shutil.copy2(src, raw), A.log_edit(log, "register", raw, raw, "", "campaign input"), raw)[-1])
    graded = step("grade", lambda: G.apply_grade(raw, os.path.join(run, "01_graded", "graded.png"), grade_spec, log))
    final = step("grade/color-law final", lambda: C.colorlaw(graded, os.path.join(run, "02_composite", "final.png"), 5, 30, 0.12, 1.15, log))
    src_for_layout = final or graded or raw
    step("export set (story/web/print/+)", lambda: R.run(src_for_layout, os.path.join(run, "03_exports"), export_spec, (0.52, 0.52), log))
    step("poster", lambda: L.poster(src_for_layout, os.path.join(A_, "01_poster.png"), cfg["poster_masthead"], cfg["lot"], cfg["poster_logline"], cfg["poster_footer"], log))
    step("title card", lambda: L.titlecard(os.path.join(A_, "02_titlecard.png"), 1920, 1080, cfg["title_kicker"], cfg["title_main"], cfg["title_sub"], "ink", log))
    step("landing hero", lambda: L.landing(src_for_layout, os.path.join(A_, "03_landing_hero.png"), cfg["landing_headline"], cfg["landing_sub"], cfg["landing_cta"], log))
    step("one-sheet", lambda: L.onesheet(src_for_layout, os.path.join(A_, "07_onesheet.png"), cfg["onesheet_title"], cfg["onesheet_logline"], cfg["onesheet_details"], log))
    step("lookbook page", lambda: L.lookbook(src_for_layout, os.path.join(A_, "08_lookbook.png"), cfg["lookbook_caption"], log))
    step("thumbnail", lambda: L.thumbnail(src_for_layout, os.path.join(A_, "13_thumbnail.png"), cfg["thumbnail_title"], cfg["thumbnail_kicker"], log))
    slides_path = os.path.join(run, "10_logs", "_slides.json"); json.dump(cfg["carousel"], open(slides_path, "w"))
    step("social carousel", lambda: L.carousel(src_for_layout, os.path.join(A_, "carousel"), slides_path, log))

    # still-based teaser (NOT generation): convert fractional crops to pixels for this hero
    def _teaser():
        iw, ih = Image.open(src_for_layout).size
        beats = []
        for b in cfg["teaser_beats"]:
            b2 = dict(b)
            if b.get("type") == "image" and "fcrop" in b:
                fx0, fy0, fx1, fy1 = b["fcrop"]; b2["crop"] = [int(fx0*iw), int(fy0*ih), int(fx1*iw), int(fy1*ih)]; b2.pop("fcrop", None)
            beats.append(b2)
        bpath = os.path.join(run, "10_logs", "_beats.json"); json.dump(beats, open(bpath, "w"))
        return T.build(src_for_layout, bpath, os.path.join(run, "04_motion", "teaser_9x16.mp4"), 1080, 1920, 30, log)
    step("still-based teaser", _teaser)

    # caption
    def _caption():
        p = os.path.join(run, "caption.md"); open(p, "w").write(f"# {cfg['lot']} , caption\n\n{cfg['caption']}\n"); return p
    step("caption", _caption)

    # pitch board from produced artifacts
    def _board():
        def pick(*names):
            for n in names:
                p = os.path.join(A_, n)
                if os.path.exists(p): return p
            return None
        teaser_still = None
        # grab a teaser frame for the board cell if ffmpeg present
        import subprocess
        tv = os.path.join(run, "04_motion", "teaser_9x16.mp4")
        if os.path.exists(tv):
            teaser_still = os.path.join(run, "10_logs", "_teaser_still.png")
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", "10.2", "-i", tv, "-frames:v", "1", teaser_still], capture_output=True)
        cells = [
            {"img": pick("01_poster.png"), "label": "campaign poster", "status": "ACTIVE", "fy": 0.4},
            {"img": pick("02_titlecard.png"), "label": "title card", "status": "ACTIVE"},
            {"img": pick("03_landing_hero.png"), "label": "landing hero", "status": "ACTIVE", "fy": 0.5},
            {"img": teaser_still or pick("13_thumbnail.png"), "label": "still-based teaser", "status": "ACTIVE"},
            {"img": pick("07_onesheet.png"), "label": "one-sheet", "status": "ACTIVE", "fy": 0.35},
            {"img": os.path.join(A_, "carousel", "slide_01.png"), "label": "social carousel", "status": "ACTIVE"},
            {"img": pick("08_lookbook.png"), "label": "lookbook page", "status": "ACTIVE", "fy": 0.4},
            {"img": pick("13_thumbnail.png"), "label": "thumbnail", "status": "ACTIVE"},
        ]
        man = {"cols": 4, "sub": f"{cfg['lot']} campaign kit , internal , not for release", "cells": cells}
        mp = os.path.join(run, "10_logs", "_board.json"); json.dump(man, open(mp, "w"))
        return L.board(os.path.join(A_, "09_pitch_board.png"), f"{cfg['lot']}  ,  {cfg['world']}", mp, log)
    step("pitch board", _board)

    # gate
    verdict = "PENDING"; checks = {}
    try:
        verdict, checks = GATE.run_gate(run, final or src_for_layout, None, export_spec, model_scores)
        steps.append(("post-production gate", "ACTIVE" if verdict == "SHIP" else ("AMBER" if verdict == "FIX" else "RED"), f"verdict {verdict}"))
    except Exception as e:
        steps.append(("post-production gate", "FAIL", str(e)[:120]))

    # proof dashboard from step results + gate checks
    def _dash():
        rows = [(lbl, st, det) for (lbl, st, det) in steps]
        for k, v in checks.items():
            rows.append((f"gate:{k}", v, ""))
        return L.dashboard(os.path.join(A_, "10_proof_dashboard.png"), f"{cfg['lot']} CAMPAIGN", f"{cfg['world']} , one-command kit", rows, log)
    dash = None
    try: dash = _dash()
    except Exception as e: steps.append(("proof dashboard", "FAIL", str(e)[:120]))
    else: steps.append(("proof dashboard", "ACTIVE", os.path.relpath(dash, run)))

    # operator note + manifest
    n_active = sum(1 for _, s, _ in steps if s == "ACTIVE"); n_fail = sum(1 for _, s, _ in steps if s == "FAIL")
    note = os.path.join(run, "OPERATOR_NOTE.md")
    with open(note, "w") as f:
        f.write(f"# OPERATOR NOTE , {name} (one-command campaign)\n\n")
        f.write(f"- Hero in: `{os.path.relpath(src, CC)}`\n- Steps: {n_active} ACTIVE, {n_fail} FAILED. Gate verdict: {verdict}.\n")
        f.write(f"- No new generation. Still-based teaser only. Internal, not hosted/posted.\n\n## Steps\n")
        for lbl, st, det in steps: f.write(f"- [{st}] {lbl} , {det}\n")
        if verdict != "SHIP":
            f.write(f"\n## Gate not SHIP\nVerdict {verdict}. ")
            f.write("Taste checks PENDING means a human/model has not signed off identity_withheld / beats_source / text_legible yet; re-run with --model-scores once seen.\n" if verdict == "FIX" else "A hard check FAILED, see gate:* rows in the dashboard.\n")
    manifest = os.path.join(run, "CAMPAIGN_MANIFEST.json")
    json.dump({"name": name, "src": src, "verdict": verdict, "steps": steps, "checks": checks}, open(manifest, "w"), indent=1)
    return run, steps, verdict, checks

def main():
    ap = argparse.ArgumentParser(prog="os_campaign.py"); sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("run"); r.add_argument("--src", required=True); r.add_argument("--name", required=True)
    r.add_argument("--config", default=""); r.add_argument("--model-scores", default="")
    sub.add_parser("defaults")
    a = ap.parse_args()
    if a.cmd == "defaults":
        print(json.dumps(DEFAULT_CONFIG, indent=2)); return 0
    if a.cmd == "run":
        if not os.path.exists(a.src): print(f"missing src: {a.src}"); return 1
        cfg = dict(DEFAULT_CONFIG)
        if a.config and os.path.exists(a.config): cfg.update(json.load(open(a.config)))
        ms = {}
        if a.model_scores:
            for kv in a.model_scores.split(","):
                if "=" in kv: k, v = kv.split("="); ms[k.strip()] = v.strip().upper()
        run, steps, verdict, checks = run_campaign(a.src, a.name, cfg, ms)
        print(f"\nCAMPAIGN: {a.name}  ,  gate {verdict}")
        for lbl, st, det in steps:
            mark = "OK " if st == "ACTIVE" else ("!! " if st in ("FAIL", "RED") else "?? ")
            print(f"  {mark}{st:7s} {lbl}")
        print(f"\n  folder: {run}")
        return 0 if verdict in ("SHIP", "FIX") and not any(s == "FAIL" for _, s, _ in steps) else 1
    ap.print_help(); return 0

if __name__ == "__main__":
    sys.exit(main())
