#!/usr/bin/env python3
"""
os_crs.py , Character Reference System engine.

Defines, validates, plans, and gates a fully ORIGINAL (non-real, non-celebrity)
character so it survives multiple outputs. Consistency is GATED in code, never
claimed from doctrine. Generation is NOT performed here , `sheet` emits a PLAN;
real frame-observations are filled by an approved vision/generation pass.

Commands:
  new <slug> [--name NAME]              scaffold a CRS spec (refuses likeness leaks)
  validate <slug>                       completeness check (all fields, >=1 hard invariant)
  sheet <slug>                          write the 14-reference sheet PLAN (no generation)
  gate <slug> --frames FILE [--threshold 0.9]   cross-frame identity consistency gate
  leakcheck (--text "..."|--file F)     identity-leak guard, standalone
  show <slug>

Storage: 00_COMMAND_CENTER/campaign_house/characters/<slug>/
  CRS.json  SHEET_PLAN.json  consistency/<report>.json
"""
import os, sys, json, re, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CHAR_DIR = os.path.join(ROOT, "campaign_house", "characters")

REQUIRED = ["face", "body", "wardrobe", "palette", "lighting", "camera_language",
            "expressions", "poses", "negative_prompts", "identity_invariants",
            "variation_rules"]

# Identity-leak guard , refuses obvious real-person / celebrity references.
# Cannot detect every covert reference; covert leaks remain a manual responsibility.
# Negation-aware: a responsible disclaimer ("NOT resembling any real person") passes,
# while an affirmative reference ("looks like <celebrity>") is flagged.
LEAK_PATTERNS = [
    r"looks?\s+like\s+[A-Z]", r"resembl", r"based\s+on\s+(a\s+)?real",
    r"\bceleb", r"likeness\s+of", r"\blookalike\b", r"spitting\s+image",
    r"deepfake", r"real\s+person\s+named", r"photo\s+of\s+[A-Z][a-z]+\s+[A-Z][a-z]+",
    r"\b(actor|actress|model|singer|athlete|president)\s+[A-Z][a-z]+",
]
# If any of these appear within ~45 chars on either side of a match, treat it as a
# disclaimer (the spec is asserting the character is NOT based on a real person).
LEAK_DISCLAIMERS = [
    "not", "no ", "never", "without", "avoid", "free of", "zero", "nor ",
    "any real", "any public", "any famous", "original synthetic", "not derived",
    "no celebrity", "fully original",
]

CANONICAL_14 = [
    ("01_front_neutral", "front, eye-level", "chest-up", "anchor identity, default key"),
    ("02_three_quarter_left", "3/4 left, eye-level", "chest-up", "volume of the face"),
    ("03_three_quarter_right", "3/4 right, eye-level", "chest-up", "volume, symmetry check"),
    ("04_profile_left", "left profile, eye-level", "head", "nose/jaw line"),
    ("05_profile_right", "right profile, eye-level", "head", "symmetry of profile"),
    ("06_back", "back, eye-level", "full", "hair/silhouette continuity"),
    ("07_hero_slight_below", "front, slight-below", "chest-up", "authority hero frame"),
    ("08_slight_above", "front, slight-above", "head", "softness / vulnerability range"),
    ("09_expr_subtle_smile", "front, eye-level", "chest-up", "in-register subtle smile"),
    ("10_expr_intensity", "3/4, eye-level", "chest-up", "slow-burn intensity"),
    ("11_expr_candid", "candid angle", "chest-up", "natural motion, register-safe"),
    ("12_pose_seated", "3/4, eye-level", "full", "seated forward-lean posture"),
    ("13_pose_walking", "environmental", "full", "mid-stride motion reference"),
    ("14_detail_signature", "macro", "hands/accessory", "hands + signature accessory detail"),
]


def char_path(slug):
    return os.path.join(CHAR_DIR, slug)


def load_crs(slug):
    p = os.path.join(char_path(slug), "CRS.json")
    if not os.path.isfile(p):
        return None
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def leak_scan(text):
    """Return the list of leak patterns that hit AFFIRMATIVELY (not in a disclaimer
    context). A match is skipped if a disclaimer token appears within ~45 chars on
    either side, so 'not resembling any real person' passes while 'looks like X' fails."""
    low = (text or "").lower()
    hits = []
    for pat in LEAK_PATTERNS:
        flagged = False
        for m in re.finditer(pat, text, re.IGNORECASE):
            s, e = m.start(), m.end()
            window = low[max(0, s - 45):min(len(low), e + 45)]
            if any(d in window for d in LEAK_DISCLAIMERS):
                continue  # disclaimer context, not a leak
            flagged = True
            break
        if flagged:
            hits.append(pat)
    return hits


def scaffold_spec(slug, name):
    return {
        "slug": slug,
        "working_name": name or slug.upper(),
        "name_status": "CODENAME , public name pending name-availability gate (do not treat as a brand decision)",
        "original": True,
        "provenance": "fully original synthetic character; not derived from any real or public person",
        "face": "",
        "body": "",
        "wardrobe": "",
        "palette": [],
        "lighting": "",
        "camera_language": "",
        "expressions": [],
        "poses": [],
        "negative_prompts": [],
        "identity_invariants": [],   # list of {key, value, hard:bool, tolerance?}
        "variation_rules": {"may_vary": [], "must_not_vary": []},
    }


def cmd_new(a):
    slug = a.slug
    if not re.match(r"^[a-z0-9][a-z0-9_-]*$", slug):
        print(f"  refused: '{slug}' not a valid slug")
        return 1
    d = char_path(slug)
    if os.path.exists(os.path.join(d, "CRS.json")):
        print(f"  refused: {slug} already exists")
        return 1
    if a.name and leak_scan(a.name):
        print(f"  REFUSED (identity-leak): name '{a.name}' trips the real/celebrity guard")
        return 1
    os.makedirs(os.path.join(d, "consistency"), exist_ok=True)
    spec = scaffold_spec(slug, a.name)
    with open(os.path.join(d, "CRS.json"), "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2)
    print(f"  created CRS scaffold: {slug} (original=True). Fill fields, then `validate`.")
    return 0


def cmd_validate(a):
    spec = load_crs(a.slug)
    if spec is None:
        print(f"  not found: {a.slug}")
        return 1
    problems = []
    if not spec.get("original") is True:
        problems.append("original must be True (no real/celebrity basis)")
    # leak scan over all string content
    blob = json.dumps(spec)
    leaks = leak_scan(blob)
    if leaks:
        problems.append(f"identity-leak patterns present: {leaks}")
    for k in REQUIRED:
        v = spec.get(k)
        if v in (None, "", [], {}):
            problems.append(f"empty required field: {k}")
    inv = spec.get("identity_invariants") or []
    hard = [i for i in inv if isinstance(i, dict) and i.get("hard")]
    if len(hard) < 1:
        problems.append("identity_invariants needs >=1 hard invariant (the consistency anchor)")
    vr = spec.get("variation_rules") or {}
    if not vr.get("must_not_vary"):
        problems.append("variation_rules.must_not_vary must list locked attributes")
    if problems:
        print(f"  INVALID: {a.slug}")
        for p in problems:
            print(f"    - {p}")
        return 1
    print(f"  VALID: {a.slug} , {len(hard)} hard invariant(s), {len(spec['identity_invariants'])} total")
    return 0


def cmd_sheet(a):
    spec = load_crs(a.slug)
    if spec is None:
        print(f"  not found: {a.slug}")
        return 1
    inv = spec.get("identity_invariants") or []
    hold = [i.get("key") for i in inv if isinstance(i, dict) and i.get("hard")]
    plan = {
        "slug": a.slug,
        "working_name": spec.get("working_name"),
        "generation_status": "PLAN ONLY , not generated. Generation requires approved credit spend.",
        "invariants_to_hold_every_frame": hold,
        "negative_prompts": spec.get("negative_prompts"),
        "frames": [
            {"id": fid, "angle": ang, "framing": fr, "purpose": purp,
             "lighting": spec.get("lighting"), "camera": spec.get("camera_language")}
            for (fid, ang, fr, purp) in CANONICAL_14
        ],
    }
    out = os.path.join(char_path(a.slug), "SHEET_PLAN.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2)
    print(f"  wrote 14-reference sheet PLAN: {out}")
    print(f"  frames planned: {len(plan['frames'])} | invariants to hold: {hold}")
    print("  NOTE: no images generated. Run an approved generation pass to populate frames.")
    return 0


def evaluate_frame(spec, observed):
    """Shared identity-scoring core (reused by the motion QA layer).
    Identity-HOLD is judged on HARD invariants only , soft invariants are explicitly
    allowed to vary, so they must never penalize the hold score.
    Returns (hard_score 0..1, list of hard-invariant failures)."""
    inv = spec.get("identity_invariants") or []
    hard = [(i["key"], i["value"]) for i in inv if isinstance(i, dict) and i.get("hard")]
    matches, hard_fail = 0, []
    for k, expected in hard:
        got = observed.get(k)
        if str(got).strip().lower() == str(expected).strip().lower():
            matches += 1
        else:
            hard_fail.append({"key": k, "expected": expected, "got": got})
    score = round(matches / len(hard), 3) if hard else 1.0
    return score, hard_fail


def cmd_gate(a):
    """Cross-frame identity consistency gate.
    frames file = list of {frame_id, observed:{invariant_key: value}}.
    Hard-invariant mismatch OR score<threshold -> QUARANTINE."""
    spec = load_crs(a.slug)
    if spec is None:
        print(f"  not found: {a.slug}")
        return 1
    with open(a.frames, "r", encoding="utf-8") as f:
        frames = json.load(f)
    report = {"slug": a.slug, "threshold": a.threshold, "frames": []}
    n_quar = 0
    for fr in frames:
        fid = fr.get("frame_id", "?")
        obs = fr.get("observed", {})
        score, hard_fail = evaluate_frame(spec, obs)
        quarantined = bool(hard_fail) or score < a.threshold
        if quarantined:
            n_quar += 1
        report["frames"].append({
            "frame_id": fid, "score": score, "quarantined": quarantined,
            "hard_failures": hard_fail,
        })
    cdir = os.path.join(char_path(a.slug), "consistency")
    os.makedirs(cdir, exist_ok=True)
    outp = os.path.join(cdir, "gate_report.json")
    with open(outp, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"  consistency gate: {len(frames)} frame(s), {n_quar} quarantined (threshold {a.threshold})")
    for fr in report["frames"]:
        tag = "QUARANTINE" if fr["quarantined"] else "pass"
        hf = (" hard-fail:" + ",".join(h["key"] for h in fr["hard_failures"])) if fr["hard_failures"] else ""
        print(f"    [{tag}] {fr['frame_id']} score={fr['score']}{hf}")
    print(f"  report: {outp}")
    return 0


def cmd_leakcheck(a):
    text = a.text
    if a.file:
        with open(a.file, "r", encoding="utf-8") as f:
            text = f.read()
    hits = leak_scan(text or "")
    if hits:
        print(f"  LEAK: real/celebrity reference patterns hit: {hits}")
        return 1
    print("  clean: no real/celebrity reference patterns detected (covert leaks still operator's call)")
    return 0


def cmd_show(a):
    spec = load_crs(a.slug)
    if spec is None:
        print(f"  not found: {a.slug}")
        return 1
    print(json.dumps(spec, indent=2))
    return 0


def main():
    p = argparse.ArgumentParser(prog="os_crs.py")
    sub = p.add_subparsers(dest="cmd")
    n = sub.add_parser("new"); n.add_argument("slug"); n.add_argument("--name", default=None)
    v = sub.add_parser("validate"); v.add_argument("slug")
    s = sub.add_parser("sheet"); s.add_argument("slug")
    g = sub.add_parser("gate"); g.add_argument("slug"); g.add_argument("--frames", required=True)
    g.add_argument("--threshold", type=float, default=0.9)
    lc = sub.add_parser("leakcheck"); lc.add_argument("--text", default=""); lc.add_argument("--file", default=None)
    sh = sub.add_parser("show"); sh.add_argument("slug")
    a = p.parse_args()
    handlers = {"new": cmd_new, "validate": cmd_validate, "sheet": cmd_sheet,
                "gate": cmd_gate, "leakcheck": cmd_leakcheck, "show": cmd_show}
    if a.cmd not in handlers:
        p.print_help(); return 1
    return handlers[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
