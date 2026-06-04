#!/usr/bin/env python3
"""
os_herolock.py , locked-hero registry.

Once a hero passes identity + world (+ signature recovery + vision), it becomes the
REFERENCE ANCHOR. Future continuity-critical stills/video condition on THIS hero,
not on fresh text. The registry records every path + gate report + allowed use cases.

CLI:
  register --hero-id ID --crs SLUG --world SLUG --approved PATH --source PATH
           [--facecrop PATH --identitycrop PATH --marked PATH]
           --approved-date YYYY-MM-DD --gate-reports "identity=PATH;world=PATH;facematch=PATH"
           --usecases "still-reference;video-start-image;identity-gate-anchor"
  show ID
  list
  path ID KEY            (print one stored path, e.g. approved / marked / source)
"""
import os, sys, json, csv, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
HERO_DIR = os.path.join(ROOT, "campaign_house", "locked_heroes")
REGISTRY = os.path.join(ROOT, "OS_LOCKED_HERO_REGISTRY.csv")


def hero_json(hid):
    return os.path.join(HERO_DIR, hid, "HERO.json")


def load(hid):
    p = hero_json(hid)
    return json.load(open(p)) if os.path.isfile(p) else None


def cmd_register(a):
    if not (a.approved and os.path.isfile(a.approved)):
        print(f"  REFUSED: approved asset not found: {a.approved}"); return 1
    if not (a.source and os.path.isfile(a.source)):
        print(f"  REFUSED: source asset not found: {a.source} (source must be preserved)"); return 1
    reports = {}
    for kv in (a.gate_reports or "").split(";"):
        if "=" in kv:
            k, v = kv.split("=", 1); reports[k.strip()] = v.strip()
    rec = {
        "hero_id": a.hero_id,
        "crs_slug": a.crs, "world_slug": a.world,
        "approved_path": a.approved,
        "source_path": a.source,
        "face_crop_path": a.facecrop or "",
        "identity_crop_path": a.identitycrop or "",
        "mark_injected_path": a.marked or "",
        "approved_date": a.approved_date,
        "gate_reports": reports,
        "allowed_use_cases": [u.strip() for u in (a.usecases or "").split(";") if u.strip()],
        "status": "LOCKED",
        "note": "Continuity-critical generation must condition on approved_path (or marked). No fresh text-only face for continuity.",
    }
    os.makedirs(os.path.join(HERO_DIR, a.hero_id), exist_ok=True)
    json.dump(rec, open(hero_json(a.hero_id), "w"), indent=2)
    new = not os.path.exists(REGISTRY)
    with open(REGISTRY, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["hero_id", "crs", "world", "approved_path", "approved_date", "use_cases", "status"])
        w.writerow([a.hero_id, a.crs, a.world, a.approved, a.approved_date,
                    "|".join(rec["allowed_use_cases"]), rec["status"]])
    print(f"  LOCKED hero registered: {a.hero_id} -> {hero_json(a.hero_id)}")
    print(f"  anchor for: {', '.join(rec['allowed_use_cases']) or '(none specified)'}")
    return 0


def cmd_show(a):
    rec = load(a.hero_id)
    if rec is None:
        print(f"  not found: {a.hero_id}"); return 1
    print(json.dumps(rec, indent=2)); return 0


def cmd_list(a):
    if not os.path.isdir(HERO_DIR):
        print("  no locked heroes yet"); return 0
    for d in sorted(os.listdir(HERO_DIR)):
        rec = load(d)
        if rec:
            print(f"  {d}  [{rec['status']}]  {rec['approved_date']}  anchor: {','.join(rec['allowed_use_cases'])}")
    return 0


def cmd_path(a):
    rec = load(a.hero_id)
    if rec is None:
        print(f"  not found: {a.hero_id}"); return 1
    key = {"approved": "approved_path", "source": "source_path", "marked": "mark_injected_path",
           "facecrop": "face_crop_path", "identitycrop": "identity_crop_path"}.get(a.key, a.key)
    print(rec.get(key, "")); return 0


def main():
    p = argparse.ArgumentParser(prog="os_herolock.py")
    sub = p.add_subparsers(dest="cmd")
    r = sub.add_parser("register")
    r.add_argument("--hero-id", required=True, dest="hero_id")
    r.add_argument("--crs", required=True); r.add_argument("--world", required=True)
    r.add_argument("--approved", required=True); r.add_argument("--source", required=True)
    r.add_argument("--facecrop", default=None); r.add_argument("--identitycrop", default=None)
    r.add_argument("--marked", default=None)
    r.add_argument("--approved-date", required=True, dest="approved_date")
    r.add_argument("--gate-reports", default="", dest="gate_reports")
    r.add_argument("--usecases", default="")
    sh = sub.add_parser("show"); sh.add_argument("hero_id")
    sub.add_parser("list")
    pa = sub.add_parser("path"); pa.add_argument("hero_id"); pa.add_argument("key")
    a = p.parse_args()
    return {"register": cmd_register, "show": cmd_show, "list": cmd_list, "path": cmd_path}.get(
        a.cmd, lambda _a: (p.print_help() or 1))(a)


if __name__ == "__main__":
    sys.exit(main())
