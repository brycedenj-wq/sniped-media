#!/usr/bin/env python3
"""
os_world.py , World Bible engine.

Defines and gates the world rules a character lives in, so every output is
continuous instead of random. Continuity is GATED in code. No generation here.

Commands:
  new <slug> [--name NAME]                scaffold a world bible
  validate <slug>                         completeness check (all 9 rule categories)
  continuity <slug> --scene FILE          continuity gate for a proposed scene
  show <slug>

Storage: 00_COMMAND_CENTER/campaign_house/worlds/<slug>/WORLD.json
"""
import os, sys, json, re, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WORLD_DIR = os.path.join(ROOT, "campaign_house", "worlds")

REQUIRED = ["environments", "materials", "light_logic", "color_system",
            "camera_language", "forbidden_elements", "recurring_motifs",
            "sref_style_slots", "continuity_rules"]


def world_path(slug):
    return os.path.join(WORLD_DIR, slug)


def load_world(slug):
    p = os.path.join(world_path(slug), "WORLD.json")
    if not os.path.isfile(p):
        return None
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def scaffold(slug, name):
    return {
        "slug": slug,
        "working_name": name or slug.upper(),
        "name_status": "CODENAME , public name pending name-availability gate (not a brand decision)",
        "environments": [],
        "materials": [],
        "light_logic": "",
        "color_system": {"foundation": "", "palette_hex": [], "forbidden_hues": []},
        "camera_language": "",
        "forbidden_elements": [],
        "recurring_motifs": [],
        "sref_style_slots": [],   # [{slot, role, value|"TBD-manual-pull"}]
        "continuity_rules": [],
    }


def cmd_new(a):
    slug = a.slug
    if not re.match(r"^[a-z0-9][a-z0-9_-]*$", slug):
        print(f"  refused: '{slug}' not a valid slug"); return 1
    d = world_path(slug)
    if os.path.exists(os.path.join(d, "WORLD.json")):
        print(f"  refused: {slug} already exists"); return 1
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "WORLD.json"), "w", encoding="utf-8") as f:
        json.dump(scaffold(slug, a.name), f, indent=2)
    print(f"  created world scaffold: {slug}. Fill the 9 rule categories, then `validate`.")
    return 0


def cmd_validate(a):
    w = load_world(a.slug)
    if w is None:
        print(f"  not found: {a.slug}"); return 1
    problems = []
    for k in REQUIRED:
        v = w.get(k)
        if v in (None, "", [], {}):
            problems.append(f"empty required category: {k}")
    cs = w.get("color_system") or {}
    if isinstance(cs, dict):
        if not cs.get("palette_hex"):
            problems.append("color_system.palette_hex empty")
        if not cs.get("forbidden_hues"):
            problems.append("color_system.forbidden_hues empty (state what is banned, e.g. teal/orange)")
    if not w.get("forbidden_elements"):
        problems.append("forbidden_elements must be explicit")
    if problems:
        print(f"  INVALID: {a.slug}")
        for p in problems:
            print(f"    - {p}")
        return 1
    print(f"  VALID: {a.slug} , {len(w['environments'])} env(s), "
          f"{len(w['forbidden_elements'])} forbidden, {len(w['continuity_rules'])} continuity rule(s)")
    return 0


def evaluate_scene(world, scene):
    """Shared scene-continuity core (reused by the motion QA layer).
    Returns (failures [hard], warns [advisory])."""
    allowed_env = [e.lower() for e in world.get("environments", [])]
    forbidden = [x.lower() for x in world.get("forbidden_elements", [])]
    failures, warns = [], []
    env = str(scene.get("environment", "")).lower()
    if env and env not in allowed_env:
        failures.append(f"environment '{scene.get('environment')}' not in world rotation")
    for el in scene.get("elements", []):
        if str(el).lower() in forbidden:
            failures.append(f"forbidden element present: {el}")
    pal = [h.lower() for h in (world.get("color_system", {}).get("palette_hex") or [])]
    for h in scene.get("palette_hex", []):
        if pal and h.lower() not in pal:
            warns.append(f"off-palette hue {h} (advisory)")
    return failures, warns


def cmd_continuity(a):
    """Scene continuity gate. scene = {environment, materials[], palette_hex[], elements[], camera}.
    Forbidden element present, or environment not allowed -> QUARANTINE."""
    w = load_world(a.slug)
    if w is None:
        print(f"  not found: {a.slug}"); return 1
    with open(a.scene, "r", encoding="utf-8") as f:
        scene = json.load(f)
    failures, warns = evaluate_scene(w, scene)
    quarantined = bool(failures)
    print(f"  continuity gate: {a.slug} <- scene")
    if failures:
        print("    [QUARANTINE]")
        for fl in failures:
            print(f"      - {fl}")
    else:
        print("    [pass]")
    for wn in warns:
        print(f"      ~ {wn}")
    return 1 if quarantined else 0


def cmd_show(a):
    w = load_world(a.slug)
    if w is None:
        print(f"  not found: {a.slug}"); return 1
    print(json.dumps(w, indent=2)); return 0


def main():
    p = argparse.ArgumentParser(prog="os_world.py")
    sub = p.add_subparsers(dest="cmd")
    n = sub.add_parser("new"); n.add_argument("slug"); n.add_argument("--name", default=None)
    v = sub.add_parser("validate"); v.add_argument("slug")
    c = sub.add_parser("continuity"); c.add_argument("slug"); c.add_argument("--scene", required=True)
    sh = sub.add_parser("show"); sh.add_argument("slug")
    a = p.parse_args()
    handlers = {"new": cmd_new, "validate": cmd_validate, "continuity": cmd_continuity, "show": cmd_show}
    if a.cmd not in handlers:
        p.print_help(); return 1
    return handlers[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
