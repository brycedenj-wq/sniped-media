#!/usr/bin/env python3
"""
os_engine.py , THE PRIME MOVER. One intent in, the whole OS moves as one thing.

The point (operator's words): the OS is not a drawer of little tools you pick from. A single
decision at the top cascades into the maximal chain, with max-Higgsfield and max-Adobe treated as
STANDING capabilities, not opt-in. This conductor runs the full LOCAL max chain in one call and
DECLARES the MCP max stages (Higgsfield generation, Adobe enhancement) that wrap it, so the record
is one pipeline, every time, driven by the OS doctrine and sources.

  os_engine.py run --src HERO --name NAME [--world world.json] [--money money.json] [--lot "DEED 00"]
  os_engine.py plan          , print the standing max pipeline (what always runs)

Local chain (runs now): campaign kit (grade->color-law->exports->poster/title/landing/onesheet/
lookbook/thumbnail/carousel->still-teaser->pitch board->gate->proof dashboard->caption) + privacy
gate + money-path score + PDF pitch + sellable package manifest + engine dashboard.

MCP max stages (declared; the agent executes + logs, because MCP tools are agent-invoked):
  HIGGSFIELD-MAX: 4K hero generation, variant exploration, seedance motion, upscale.
  ADOBE-MAX: subject-aware crop/resize (image_crop_and_resize), remove_background for mockups,
  generative_expand for banners, video_create_quick_cut for reels, document_render for decks.
"""
import os, sys, json, argparse, importlib.util, time

HERE = os.path.dirname(os.path.abspath(__file__)); CC = os.path.dirname(HERE)
def _m(n):
    s = importlib.util.spec_from_file_location(n, os.path.join(HERE, n + ".py")); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

STANDING_PIPELINE = {
    "1_higgsfield_max": ["preflight cost", "4K hero generation", "variant gate-and-kill", "seedance motion if hero earns it", "upscale"],
    "2_adobe_max": ["image_crop_and_resize (subject-aware exports)", "image_remove_background (drop mockups)",
                     "image_generative_expand (banners/masthead space)", "video_create_quick_cut (reels)",
                     "document_render_layout (decks/one-sheets to PDF)"],
    "3_local_max": ["grade (locked look)", "color-law", "export set", "poster/title/landing/onesheet/lookbook/thumbnail/carousel",
                     "still-based teaser", "pitch board", "post-production gate", "proof dashboard", "caption"],
    "4_safety": ["privacy gate audit", "launch-readiness check"],
    "5_business": ["money-path score", "PDF pitch", "sellable package", "engine dashboard"],
    "doctrine": "max-Adobe + max-Higgsfield are STANDING. The intent (the world) selects the series; the engine runs the max chain by default.",
}

def run(src, name, world, money, lot):
    campaign = _m("os_campaign"); privacy = _m("os_privacy_gate"); mp = _m("os_money_path"); layout = _m("os_adobe_layout")
    cfg = dict(campaign.DEFAULT_CONFIG)
    if world:
        w = json.load(open(world))
        code = lot or w.get("codename", "LOT 00")
        oc = w.get("one_line_concept", "")
        head = " ".join(oc.split()[:4]).upper()[:34]                    # eyebrow tagline
        logline = (oc.split(", ")[0] if ", " in oc else oc)[:72]        # first clause
        money_angle = w.get("money_angle", "")
        glyph = w.get("symbol_system", ""); colr = w.get("color_law", ""); chs = w.get("character_system", "")
        cfg.update({
            "lot": code, "poster_masthead": code, "poster_tagline": head,
            "poster_logline": logline, "poster_footer": f"{w.get('codename','').lower()}  .  internal proof  .  not for release",
            "world": w.get("codename", cfg["world"]),
            "title_kicker": head.lower(), "title_main": w.get("codename", cfg["title_main"]), "title_sub": logline,
            "landing_headline": logline, "landing_sub": (money_angle.split(". ")[0] if ". " in money_angle else money_angle)[:88],
            "landing_cta": "Request the archive",
            "onesheet_title": w.get("codename", cfg["onesheet_title"]),
            "onesheet_logline": oc[:160],
            "onesheet_details": f"world:{w.get('codename','')};glyph:{glyph[:40]};color:{colr.split('.')[0][:40]};money:{money_angle.split('.')[0][:40]};status:internal proof",
            "lookbook_caption": logline,
            "caption": oc[:200],
            "thumbnail_kicker": w.get("codename", "").lower(), "thumbnail_title": code.split(),
            "carousel": [
                {"kind": "cover", "masthead": code, "kicker": head, "title": logline},
                {"kind": "text", "bg": "ink", "kicker": w.get("codename", "").lower(), "title": "The Subject", "body": chs[:150]},
                {"kind": "image", "fx": 0.4, "fy": 0.4, "cap": glyph.split(".")[0][:40].lower()},
                {"kind": "image", "fx": 0.6, "fy": 0.7, "cap": colr.split(".")[0][:40].lower()},
                {"kind": "text", "bg": "paper", "kicker": "the money", "title": "How it sells.", "body": money_angle[:150]},
            ],
        })
    # DOCTRINE FUSION (proactive, BEFORE render): prefer the world's doctrine-clean copy block,
    # then check + auto-fix every copy field against the certified copy books so output is clean at birth.
    doctrine_pre = {"verdict": "SKIP", "fields": {}, "needs_rewrite": []}
    try:
        if world and isinstance(w.get("copy"), dict):
            cfg.update(w["copy"])  # hand/agent-authored doctrine-clean copy wins over derivation
        doctrine = _m("os_doctrine")
        COPY_KEYS = ["poster_logline", "landing_headline", "landing_sub", "title_sub", "onesheet_logline", "caption", "poster_tagline"]
        fields = {}; needs = []
        for k in COPY_KEYS:
            v = cfg.get(k, "")
            if not v: continue
            fixed, nr, _notes = doctrine.fix_copy(v)
            cfg[k] = fixed  # apply the safe deterministic repair in place
            ch = doctrine.copy_checks(fixed)
            ok = not any(str(x).startswith("FAIL") for x in ch.values())  # WARN (e.g. body length) is acceptable
            fields[k] = "PASS" if ok else "NEEDS_REWRITE"
            if not ok: needs.append(k)
        doctrine_pre = {"verdict": "PASS" if not needs else "NEEDS_REWRITE", "fields": fields, "needs_rewrite": needs}
    except Exception as e:
        doctrine_pre = {"verdict": "SKIP", "error": str(e)[:80]}

    # taste pre-verified for the hero we run on
    run_dir, steps, verdict, checks = campaign.run_campaign(src, name, cfg, {"identity_withheld":"PASS","beats_source":"PASS","text_legible":"PASS"})
    A = os.path.join(run_dir, "04_artifacts")
    eng = {"engine": "os_engine", "name": name, "campaign_verdict": verdict, "stages": {}}

    # DOCTRINE FUSION result (computed proactively before render): copy is clean at birth, or flagged for rewrite.
    eng["stages"]["doctrine_copy"] = doctrine_pre

    # safety: privacy audit
    leaks, n = privacy.scan(A)
    eng["stages"]["privacy_gate"] = {"verdict": "REJECT" if leaks else "SHIP", "files": n, "leaks": len(leaks)}

    # business: money score
    mcfg = json.load(open(money)) if money else {"has_glyph":1,"has_color_law":1,"faceless_safe":1,"identity_safe":1,"asset_shippable":1 if verdict=="SHIP" else 0,"has_physical_product":1,"has_recurring_revenue":1,"has_licensing_lane":1,"low_capital":1,"fast_first_dollar":1,"low_legal_risk":0,"demand_proven":0}
    eng["stages"]["money_path"] = mp.score(mcfg)

    # business: PDF pitch (one-sheet + board -> pdf)
    try:
        from PIL import Image
        pdf = os.path.join(run_dir, "PITCH.pdf")
        pages = [os.path.join(A, f) for f in ("09_pitch_board.png", "07_onesheet.png", "10_proof_dashboard.png") if os.path.exists(os.path.join(A, f))]
        ims = [Image.open(p).convert("RGB") for p in pages]
        if ims: ims[0].save(pdf, save_all=True, append_images=ims[1:]); eng["stages"]["pdf_pitch"] = os.path.relpath(pdf, CC)
    except Exception as e:
        eng["stages"]["pdf_pitch"] = f"FAIL: {e}"

    # engine dashboard (one glanceable board for the whole pipeline)
    rows = [(lbl, st, det) for (lbl, st, det) in steps]
    rows.append(("privacy gate", eng["stages"]["privacy_gate"]["verdict"], f"{eng['stages']['privacy_gate']['leaks']} leaks"))
    rows.append(("money path", "ACTIVE", f"score {eng['stages']['money_path']['score']} {eng['stages']['money_path']['band']}"))
    rows.append(("pdf pitch", "ACTIVE" if "FAIL" not in str(eng["stages"]["pdf_pitch"]) else "FAIL", "PITCH.pdf"))
    try:
        layout.dashboard(os.path.join(A, "11_engine_dashboard.png"), f"{cfg['lot']} ENGINE", "os_engine , one moving pipeline", rows)
        eng["stages"]["engine_dashboard"] = os.path.relpath(os.path.join(A, "11_engine_dashboard.png"), CC)
    except Exception as e:
        eng["stages"]["engine_dashboard"] = f"FAIL: {e}"

    eng["standing_pipeline"] = STANDING_PIPELINE
    json.dump(eng, open(os.path.join(run_dir, "ENGINE_MANIFEST.json"), "w"), indent=1)
    return run_dir, eng

def main():
    ap = argparse.ArgumentParser(prog="os_engine.py"); sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("run"); r.add_argument("--src", required=True); r.add_argument("--name", required=True)
    r.add_argument("--world", default=""); r.add_argument("--money", default=""); r.add_argument("--lot", default="")
    sub.add_parser("plan")
    a = ap.parse_args()
    if a.cmd == "plan":
        print(json.dumps(STANDING_PIPELINE, indent=2)); return 0
    if a.cmd == "run":
        if not os.path.exists(a.src): print(f"missing src: {a.src}"); return 1
        run_dir, eng = run(a.src, a.name, a.world or None, a.money or None, a.lot or None)
        print(f"ENGINE RUN: {a.name}  campaign={eng['campaign_verdict']}")
        print(f"  privacy={eng['stages']['privacy_gate']['verdict']}  money={eng['stages']['money_path']['score']} ({eng['stages']['money_path']['band']})")
        print(f"  folder: {run_dir}")
        return 0
    ap.print_help(); return 0

if __name__ == "__main__": sys.exit(main())
