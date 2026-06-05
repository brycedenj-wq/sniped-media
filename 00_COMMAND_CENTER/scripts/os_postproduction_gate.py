#!/usr/bin/env python3
"""
os_postproduction_gate.py , the ship gate for a post-production run. Nothing is "done" without it.

Hybrid like os_vision_gate: the MEASURABLE checks are deterministic (script proves them); the TASTE
checks are model-judged (the model Reads the asset and records a verdict). Writes POSTPROD_GATE_LOG.csv.

Deterministic checks:
  grade_applied    , EDIT_LOG shows a grade op in the lineage
  exports_complete , every SNIPED_EXPORT_SPECS spec has a file at the right dimensions
  no_enlarge       , no export was upscaled past the source long edge (warns, does not hard-fail)
  metadata_clean   , exiftool finds no GPS/owner/artist/serial on final + exports (privacy)
  no_banned_tokens , filenames carry no real-name / employer tokens
  log_not_silent   , every produced artifact has an EDIT_LOG row

Model-judged checks (printed checklist, verdict recorded): text_legible, identity_withheld, beats_source.

  os_postproduction_gate.py run <run_dir> --final IMG [--exports DIR] [--specs JSON] [--model-scores "k=PASS,..."]
  os_postproduction_gate.py audit <run_dir>
"""
import os, sys, csv, json, time, argparse, subprocess, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
CC = os.path.dirname(HERE)
DEFAULT_SPECS = os.path.join(CC, "postproduction", "specs", "SNIPED_EXPORT_SPECS.json")
BANNED = ["bryce", "brycedenj", "denj"]          # hard: real-identity tokens
WARN_TOKENS = ["sniped"]                          # soft: brand leak on a faceless pass
MODEL_CHECKS = ["text_legible", "identity_withheld", "beats_source"]

def _dims(p):
    try:
        from PIL import Image
        with Image.open(p) as im: return im.size
    except Exception: return (0, 0)

def _exif_flags(p):
    try:
        out = subprocess.run(["exiftool", "-s", "-G", p], capture_output=True, text=True).stdout
        return [l for l in out.splitlines() if any(k in l for k in
                ("GPS", "Owner", "Artist", "Creator", "Serial", "By-line", "Copyright"))]
    except Exception: return []

def _edit_rows(run_dir):
    log = os.path.join(run_dir, "10_logs", "EDIT_LOG.csv")
    if not os.path.exists(log): return []
    return list(csv.DictReader(open(log)))

def run_gate(run_dir, final, exports_dir, specs_path, model_scores):
    rows = _edit_rows(run_dir)
    ops = [r["op"] for r in rows]
    logged_outs = {r["out"] for r in rows}
    checks = {}

    checks["grade_applied"] = ("PASS" if any("grade" == o for o in ops) else "FAIL")

    cfg = json.load(open(specs_path))
    # true source long edge = the raw asset (never the enlarged outputs)
    src_long = 0
    raw_dir = os.path.join(run_dir, "00_raw")
    if os.path.isdir(raw_dir):
        for f in os.listdir(raw_dir):
            w, h = _dims(os.path.join(raw_dir, f))
            src_long = max(src_long, w, h)
    if not src_long:  # fallback: smallest src_dims seen in the log (the original, not the upscales)
        cand = []
        for r in rows:
            d = r.get("src_dims", "")
            if "x" in d:
                try: cand.append(max(int(v) for v in d.split("x")))
                except Exception: pass
        src_long = min(cand) if cand else 0
    missing, enlarged = [], []
    exdir = exports_dir or os.path.join(run_dir, "03_exports")
    present = os.listdir(exdir) if os.path.isdir(exdir) else []
    for s in cfg["specs"]:
        want = f"{s['w']}x{s['h']}"
        hit = [f for f in present if want in f]
        if not hit: missing.append(s["key"])
        else:
            if max(s["w"], s["h"]) > src_long and src_long: enlarged.append(s["key"])
    checks["exports_complete"] = "PASS" if not missing else f"FAIL(missing:{missing})"
    checks["no_enlarge"] = "PASS" if not enlarged else f"WARN(enlarged:{enlarged})"

    to_scan = [final] + [os.path.join(exdir, f) for f in present]
    exif_hits = {os.path.basename(p): _exif_flags(p) for p in to_scan if os.path.exists(p)}
    dirty = {k: v for k, v in exif_hits.items() if v}
    checks["metadata_clean"] = "PASS" if not dirty else f"FAIL({list(dirty)})"

    names = " ".join(present + [os.path.basename(final)]).lower()
    banned_hit = [t for t in BANNED if t in names]
    warn_hit = [t for t in WARN_TOKENS if t in names]
    checks["no_banned_tokens"] = "PASS" if not banned_hit else f"FAIL({banned_hit})"
    if warn_hit: checks["no_banned_tokens"] += f" WARN({warn_hit})"

    produced = [f for f in present] + [os.path.basename(final)]
    silent = [f for f in produced if f not in logged_outs]
    checks["log_not_silent"] = "PASS" if not silent else f"WARN(unlogged:{silent})"

    # model-judged
    ms = {}
    for c in MODEL_CHECKS:
        ms[c] = model_scores.get(c, "PENDING")
    checks.update(ms)

    hard_fail = any(str(v).startswith("FAIL") for k, v in checks.items())
    pending = any(v == "PENDING" for v in ms.values())
    verdict = "REJECT" if hard_fail else ("FIX" if pending else "SHIP")

    # log
    log = os.path.join(run_dir, "10_logs", "POSTPROD_GATE_LOG.csv")
    os.makedirs(os.path.dirname(log), exist_ok=True)
    new = not os.path.exists(log)
    with open(log, "a", newline="") as f:
        w = csv.writer(f)
        if new: w.writerow(["ts", "final", "verdict"] + list(checks.keys()))
        w.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), os.path.basename(final), verdict] + list(checks.values()))
    return verdict, checks

def main():
    ap = argparse.ArgumentParser(prog="os_postproduction_gate.py")
    sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("run"); r.add_argument("run_dir"); r.add_argument("--final", required=True)
    r.add_argument("--exports", default=""); r.add_argument("--specs", default=DEFAULT_SPECS)
    r.add_argument("--model-scores", default="")
    au = sub.add_parser("audit"); au.add_argument("run_dir")
    a = ap.parse_args()
    if a.cmd == "run":
        ms = {}
        if a.model_scores:
            for kv in a.model_scores.split(","):
                if "=" in kv: k, v = kv.split("="); ms[k.strip()] = v.strip().upper()
        verdict, checks = run_gate(a.run_dir, a.final, a.exports or None, a.specs, ms)
        print(f"POST-PRODUCTION GATE: {verdict}")
        for k, v in checks.items():
            mark = "OK " if (str(v).startswith("PASS") or v in ("PASS",)) else ("?? " if v in ("PENDING",) else "!! ")
            print(f"  {mark}{k:18s} {v}")
        if any(v == "PENDING" for v in checks.values()):
            print("\n  model-judged checks PENDING (the model Reads the asset and re-runs with --model-scores):")
            for c in MODEL_CHECKS: print(f"    {c}: PASS | FAIL")
        return 0 if verdict == "SHIP" else (1 if verdict == "REJECT" else 2)
    if a.cmd == "audit":
        log = os.path.join(a.run_dir, "10_logs", "POSTPROD_GATE_LOG.csv")
        if not os.path.exists(log): print("AUDIT FAIL: no gate log"); return 1
        rows = list(csv.DictReader(open(log)))
        ship = [r for r in rows if r["verdict"] == "SHIP"]
        print(f"AUDIT: {len(rows)} gate run(s), {len(ship)} SHIP. Last verdict: {rows[-1]['verdict'] if rows else 'none'}")
        return 0
    ap.print_help(); return 0

if __name__ == "__main__":
    sys.exit(main())
