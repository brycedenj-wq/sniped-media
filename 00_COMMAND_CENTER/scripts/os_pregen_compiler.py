#!/usr/bin/env python3
"""
os_pregen_compiler.py - the Moving Body pre-generation compiler gate.

Implements PRE_GENERATION_COMPILER_SPEC.md (WIRE_MOVING_BODY_001). Turns source
families into prompt tokens BEFORE any generation. A source is ACTIVE only when its
token_record has a FILLED evidence slot: token_literal AND artifact_feature AND
source_pointer all non-empty. Read / installed / router-registered / post-hoc-audited
does NOT count. Generation is REFUSED (compile_verdict = HALT) if any required slot is
EMPTY/UNPROVEN, if a required source_pointer is blank, if the grade is emitted before the
uncopyable legs are filled, or if a Group C family is force-injected.

No generation happens here. This is the gate that decides if a run is allowed to proceed.

Usage:
  os_pregen_compiler.py <artifact_plan.json>          compile a plan, print manifest + verdict
  os_pregen_compiler.py <artifact_plan.json> --manifest OUT.json   also write the manifest

Exit codes: 0 = READY-TO-ASSEMBLE, 2 = HALT, 1 = usage/error.
"""
import json, sys, argparse

# family_id -> registry entry. step = assembly order (spec Section 3). uncopyable_leg = steps 4..10.
# required_routes = routes for which this family is a REQUIRED pre-gen input/gate.
REG = {
  "OS_HIGGSFIELD_PRODUCTION_DOCTRINE": {"token":"ROUTING_HEADER","gate":"none","step":1,"required_routes":{"photo_composite","character_engine"}},
  "sniped-ai-image-tool-pick":         {"token":"TOOL_PICK","gate":"B1","step":2,"required_routes":{"photo_composite","character_engine"}},
  "tool-readiness-ledger":             {"token":"READINESS_STAMP","gate":"B2","step":3,"required_routes":{"photo_composite","character_engine"}},
  "os-world-bible:subject":            {"token":"SUBJECT_CULTURE_CUE","gate":"B3","step":4,"uncopyable":True,"required_routes":{"photo_composite","character_engine"}},
  "WORLD_BIBLE_001:provenance":        {"token":"PROVENANCE_TAG","gate":"B3","step":4,"uncopyable":True,"required_routes":{"photo_composite","character_engine"}},
  "INSIDE_CULTURE_MAP/TASTE_DNA":      {"token":"VANTAGE_CUE","gate":"B5","step":4,"uncopyable":True,"required_routes":{"photo_composite","character_engine"}},
  "SREF_LIBRARY":                      {"token":"SREF_SIGNATURE","gate":"B4","step":5,"uncopyable":True,"required_routes":{"photo_composite","character_engine"}},
  "PHOTO_CRAFT_ATOMS/sniped-photo-theory": {"token":"FRAMING_IDIOM","gate":"none","step":6,"uncopyable":True,"required_routes":{"photo_composite","character_engine"}},
  "LIGHTING_TECHNIQUE_CARDS/sniped-lighting-vault": {"token":"LIGHTING_CARD","gate":"none","step":6,"uncopyable":True,"required_routes":{"photo_composite","character_engine"}},
  "banana-pro-director":               {"token":"HYPERREAL_STACK","gate":"none","step":7,"uncopyable":True,"required_routes":{"photo_composite","character_engine"}},
  "photoreal-cinema-playbook":         {"token":"PHOTO_CRAFT_STRING","gate":"none","step":7,"uncopyable":True,"required_routes":{"photo_composite","character_engine"}},
  "sniped-status-psychology":          {"token":"STATUS_SUBJECT","gate":"B11","step":8,"uncopyable":True,"required_routes":{"photo_composite","character_engine"}},
  # character-only (faced=true), steps at 9
  "CHARACTER_FACE_POLICY_001":         {"token":"KEEPER_IDENTITY_BLOCK","gate":"B7","step":9,"uncopyable":True,"faced_only":True,"required_routes":{"character_engine"}},
  "CHARACTER_CONSISTENCY":             {"token":"IDENTITY_DRIFT_TOKENS","gate":"G4","step":9,"uncopyable":True,"faced_only":True,"required_routes":{"character_engine"}},
  "os-face-lock":                      {"token":"FACE_LOCK_TOKEN","gate":"B6","step":9,"uncopyable":True,"faced_only":True,"required_routes":{"character_engine"}},
  "SOUL_ID":                           {"token":"SOUL_ID_REQUIRED","gate":"G1","step":9,"uncopyable":True,"faced_only":True,"required_routes":{"character_engine"}},
  "CLEAN_ANCHOR_POLICY":               {"token":"CLEAN_ANCHOR_PRIVATE","gate":"G2","step":9,"uncopyable":True,"faced_only":True,"required_routes":{"character_engine"}},
  "OUTWARD_FRAME_POLICY":              {"token":"OUTWARD_OFFSET","gate":"G3","step":9,"uncopyable":True,"faced_only":True,"required_routes":{"character_engine"}},
  "ai-native-brand-lab.workflow":      {"token":"DIFFERENTIATION_SET","gate":"B5","step":10,"uncopyable":True,"required_routes":{"photo_composite","character_engine"}},
  "Alma-measurement-discipline":       {"token":"GRADE_ANCHORS","gate":"B8","step":11,"grade":True,"required_routes":{"photo_composite","character_engine"}},
  "ANTI_TASTE/visual_grade":           {"token":"NEGATIVES_BLOCK","gate":"none","step":12,"required_routes":{"photo_composite","character_engine"}},
  "WORLD_BIBLE:compound-mark":         {"token":"COMPOUND_MARK_CHECK","gate":"B9","step":13,"required_routes":{"photo_composite","character_engine"}},
  # SOURCE_INTAKE_STYLE_LINEAGE_001: style + lineage authoring-intelligence families
  "STYLE_MANIFESTO:wardrobe-intent":   {"token":"WARDROBE_INTENT","gate":"G12","step":9,"uncopyable":True,"required_routes":{"character_engine"}},
  "STYLIST_PLAYBOOK:subject-read":     {"token":"SUBJECT_READ","gate":"G13","step":9,"uncopyable":True,"required_routes":{"character_engine"}},
  "AESTHETIC_STATEMENT:author-eye":    {"token":"AUTHOR_EYE","gate":"G14","step":7,"uncopyable":True,"required_routes":{"photo_composite","character_engine"}},
  "NINE_LINEAGE:atom":                 {"token":"LINEAGE_ATOM","gate":"G15","step":6,"uncopyable":True,"required_routes":{"photo_composite","character_engine"}},
  # post-build (not a pre-gen required token) and conditional
  "composite-master-qa":              {"token":"QA_SCORECARD","gate":"none","step":99,"post_build":True,"required_routes":set()},
  "sniped-seedream-prompt":           {"token":"SEEDREAM_GRAMMAR","gate":"none","step":98,"conditional":True,"required_routes":set()},
}

GROUP_C = {"REAL_FILM_PRODUCTION_OS","cinema-worldbuilder","sniped-shortform-retention",
           "distribution_hook","copy-writing-doctrine","Route1-real-vantage-moat"}

# SOURCE_INTAKE_STYLE_LINEAGE_001 content checks: a style/lineage token that is present but
# generic / incomplete / citation-only is NOT active. Keywords required in token_literal+feature.
# wardrobe/subject/author require ALL keywords (AND); lineage requires ANY one atom name (OR) + a feature.
CONTENT = {
  # garment lock (CHARACTER_LOCK_REPAIR_001): wardrobe must carry the logics AND name the locked rust garment system
  "STYLE_MANIFESTO:wardrobe-intent": ["intent", "fit", "material", "color", "rust"],
  "STYLIST_PLAYBOOK:subject-read":   ["proportion", "color", "hand", "continuity"],
  "AESTHETIC_STATEMENT:author-eye":  ["graphic"],
  "NINE_LINEAGE:atom":               ["avedon","leibovitz","eggleston","shore","herzog","meyerowitz","frank","iturbide","haas"],
  # identity (repair): hair committed to the sculptural AFRO + skin anchor; beauty mark is OPTIONAL and deliberately NOT required here
  "CHARACTER_CONSISTENCY":           ["afro", "skin"],
  # prop / second-person ban (repair): the negatives block must carry the PR002 contamination bans
  "ANTI_TASTE/visual_grade":         ["second person", "printed", "badge"],
}
MOODY_DRIFT = ["dark moody", "moody room", "moody interior", "dark tasteful room", "moody dark"]


def compile_plan(plan):
    route = plan.get("route")
    faced = bool(plan.get("faced", route == "character_engine"))
    provided = plan.get("families", {})
    run_id = plan.get("run_id", "wiring-dry-run")

    tokens, blockers, out_of_scope, halts = [], [], [], []

    # group C force-injection check
    for fid in provided:
        if fid in GROUP_C:
            out_of_scope.append({"family_id": fid, "reason": "Group C, out of scope; forbidden from force-injection"})
            halts.append("OUT_OF_SCOPE family force-injected: " + fid)

    # which families are required for this route + faced state
    required_ids = []
    for fid, e in REG.items():
        if route in e["required_routes"]:
            if e.get("faced_only") and not faced:
                continue
            required_ids.append(fid)

    filled_count = 0
    grade_filled = False
    uncopyable_empty = []
    for fid, e in REG.items():
        rec = {"family_id": fid, "token_type": e["token"], "gate_id": e["gate"],
               "step": e["step"], "route": route}
        p = provided.get(fid, {})
        sp = (p.get("source_pointer") or "").strip()
        tl = (p.get("token_literal") or "").strip()
        af = (p.get("artifact_feature") or "").strip()
        rec["source_pointer"], rec["token_literal"], rec["artifact_feature"] = sp, tl, af
        # conditional family: N/A-with-reason is FILLED; silence is not
        if e.get("conditional") and not p:
            rec["evidence_status"] = "FILLED"; rec["token_literal"] = "N/A"
            rec["artifact_feature"] = "not applicable; reason: no Seedream lane"
            rec["required"] = False
        else:
            filled = bool(sp and tl and af)
            rec["evidence_status"] = "FILLED" if filled else ("UNPROVEN" if (tl or af) and not sp else "EMPTY")
            rec["required"] = fid in required_ids and not e.get("post_build")
        # content check: a style/lineage token that is generic/incomplete/citation-only is NOT active
        cc = CONTENT.get(fid)
        if cc and rec["evidence_status"] == "FILLED":
            low = (tl + " " + af).lower()
            if fid == "NINE_LINEAGE:atom":
                if not any(k in low for k in cc) or not af:
                    rec["evidence_status"] = "UNPROVEN"; rec["content_fail"] = "lineage citation with no named atom reaching a visible feature"
            else:
                missing = [k for k in cc if k not in low]
                if missing:
                    rec["evidence_status"] = "UNPROVEN"; rec["content_fail"] = "generic/incomplete (missing logic: " + ", ".join(missing) + ")"
        if rec["evidence_status"] == "FILLED":
            filled_count += 1
        # track grade + uncopyable legs for order rule
        if e.get("grade"):
            grade_filled = (rec["evidence_status"] == "FILLED")
        if e.get("uncopyable") and rec["required"] and rec["evidence_status"] != "FILLED":
            uncopyable_empty.append(fid)
        tokens.append(rec)

    # BLOCK rule
    for rec in tokens:
        if rec["required"] and rec["evidence_status"] in ("EMPTY", "UNPROVEN"):
            reason = rec.get("content_fail")
            msg = "required slot %s (%s) is %s" % (rec["token_type"], rec["family_id"], rec["evidence_status"])
            if reason:
                msg += " :: " + reason
            halts.append(msg)
    if grade_filled and uncopyable_empty:
        halts.append("ORDER VIOLATION: GRADE_ANCHORS filled while uncopyable legs empty: " + ", ".join(uncopyable_empty))
    # unsupported dark-moody-room drift (AUTHOR_EYE correction): a moody-room scene must carry the
    # graphic-over-atmospheric AUTHOR_EYE structure or it is refused.
    alltext = " ".join((r.get("token_literal", "") + " " + r.get("artifact_feature", "")) for r in tokens).lower()
    author_ok = any(r["family_id"] == "AESTHETIC_STATEMENT:author-eye" and r["evidence_status"] == "FILLED" for r in tokens)
    if any(p in alltext for p in MOODY_DRIFT) and not author_ok:
        halts.append("unsupported dark-moody-room drift: AUTHOR_EYE graphic-over-atmospheric structure not satisfied")

    evidence_complete = not any(r["required"] and r["evidence_status"] != "FILLED" for r in tokens)
    verdict = "READY-TO-ASSEMBLE" if (evidence_complete and not halts) else "HALT"

    manifest = {
        "run_id": run_id, "route": route, "faced": faced,
        "assembly_order_locked": True, "grade_enters_last": True,
        "tokens": sorted(tokens, key=lambda r: r["step"]),
        "out_of_scope": out_of_scope, "blockers": blockers,
        "required_family_count": len(required_ids),
        "families_filled": filled_count,
        "evidence_complete": evidence_complete,
        "halts": halts,
        "compile_verdict": verdict,
    }
    return manifest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--manifest", default=None)
    a = ap.parse_args()
    try:
        plan = json.load(open(a.plan))
    except Exception as e:
        print("ERROR reading plan:", e); return 1
    m = compile_plan(plan)
    if a.manifest:
        json.dump(m, open(a.manifest, "w"), indent=2)
    print("route=%s faced=%s required=%d filled=%d evidence_complete=%s" % (
        m["route"], m["faced"], m["required_family_count"], m["families_filled"], m["evidence_complete"]))
    print("COMPILE_VERDICT:", m["compile_verdict"])
    if m["halts"]:
        print("HALT reasons:")
        for h in m["halts"]:
            print("  -", h)
    if m["out_of_scope"]:
        print("OUT_OF_SCOPE:")
        for o in m["out_of_scope"]:
            print("  -", o["family_id"], "::", o["reason"])
    return 0 if m["compile_verdict"] == "READY-TO-ASSEMBLE" else 2


if __name__ == "__main__":
    sys.exit(main())
