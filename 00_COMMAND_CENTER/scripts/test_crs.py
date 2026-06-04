#!/usr/bin/env python3
"""Regression suite for os_crs.py. Runs in a temp sandbox; no real campaign_house writes."""
import os, sys, json, tempfile, shutil, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("os_crs", os.path.join(HERE, "os_crs.py"))
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)

results = []
def check(name, cond):
    results.append((name, bool(cond))); print(f"  {'PASS' if cond else 'FAIL'}  {name}")

class A:  # tiny args shim
    def __init__(self, **kw): self.__dict__.update(kw)


def main():
    sandbox = tempfile.mkdtemp(prefix="crstest_")
    M.CHAR_DIR = sandbox
    try:
        # leak guard
        check("leakcheck flags celebrity cue", bool(M.leak_scan("she looks like Zendaya")))
        check("leakcheck flags 'based on a real'", bool(M.leak_scan("based on a real founder")))
        check("leakcheck clean on original desc", not M.leak_scan("angular symmetrical original synthetic face"))
        # negation-aware: responsible disclaimers must PASS, affirmative refs must FAIL
        check("disclaimer 'not resembling any real person' passes",
              not M.leak_scan("fully original synthetic character; not derived from or resembling any real or public person"))
        check("disclaimer 'no resemblance to any real or famous person' passes",
              not M.leak_scan("negative prompt: resemblance to any real or famous person"))
        check("affirmative 'looks like <Name>' still flags",
              bool(M.leak_scan("the face looks like Timothee")))
        # guard fix: profession + lowercase word (e.g. 'model drift') must NOT flag
        check("'model drift' does not flag (case-sensitive name)", not M.leak_scan("fragile under model drift"))
        check("'the model drops it' does not flag", not M.leak_scan("if the model drops it, retouch"))
        check("'actor Smith' still flags", bool(M.leak_scan("cast as actor Smith")))

        # new refuses a leaky name
        rc = M.cmd_new(A(slug="leaky", name="looks like Brad Pitt"))
        check("new refuses identity-leak name", rc == 1 and not os.path.exists(os.path.join(sandbox, "leaky")))

        # new creates scaffold
        rc = M.cmd_new(A(slug="atom01", name=None))
        check("new creates scaffold", rc == 0 and os.path.isfile(os.path.join(sandbox, "atom01", "CRS.json")))

        # empty scaffold is INVALID
        rc = M.cmd_validate(A(slug="atom01"))
        check("empty scaffold is INVALID", rc == 1)

        # fill a complete, original spec
        p = os.path.join(sandbox, "atom01", "CRS.json")
        spec_obj = json.load(open(p))
        spec_obj.update({
            "face": "angular symmetrical, deep-brown eyes, mole below left eye",
            "body": "5'10 lean-athletic", "wardrobe": "charcoal wool overcoat",
            "palette": ["#2B2B2E", "#E8E4DC"], "lighting": "single soft key 45deg",
            "camera_language": "85mm chest-up f1.8", "expressions": ["neutral", "intensity"],
            "poses": ["contrapposto", "seated"], "negative_prompts": ["plastic skin", "extra fingers"],
            "identity_invariants": [
                {"key": "eye_color", "value": "deep-brown", "hard": True},
                {"key": "mole_below_left_eye", "value": "present", "hard": True},
                {"key": "hair_style", "value": "varies", "hard": False},
            ],
            "variation_rules": {"may_vary": ["hair", "wardrobe"], "must_not_vary": ["eye_color", "mole"]},
        })
        json.dump(spec_obj, open(p, "w"), indent=2)
        rc = M.cmd_validate(A(slug="atom01"))
        check("complete original spec is VALID", rc == 0)

        # sheet plan = 15 frames (incl. the tight identity-lock verify frame), plan-only
        rc = M.cmd_sheet(A(slug="atom01"))
        plan = json.load(open(os.path.join(sandbox, "atom01", "SHEET_PLAN.json")))
        check("sheet plan has 15 frames", rc == 0 and len(plan["frames"]) == 15)
        check("sheet includes identity_lock_tight verify frame",
              any("identity_lock_tight" in f["id"] for f in plan["frames"]))
        check("sheet plan is plan-only (no generation)", "PLAN ONLY" in plan["generation_status"])

        # consistency gate: matching frame passes, drifted frame quarantines
        frames = [
            {"frame_id": "f_match", "observed": {"eye_color": "deep-brown", "mole_below_left_eye": "present", "hair_style": "varies"}},
            {"frame_id": "f_drift", "observed": {"eye_color": "blue", "mole_below_left_eye": "absent", "hair_style": "varies"}},
        ]
        ff = os.path.join(sandbox, "frames.json"); json.dump(frames, open(ff, "w"))
        rc = M.cmd_gate(A(slug="atom01", frames=ff, threshold=0.9))
        rep = json.load(open(os.path.join(sandbox, "atom01", "consistency", "gate_report.json")))
        byid = {f["frame_id"]: f for f in rep["frames"]}
        check("matching frame passes the gate", byid["f_match"]["quarantined"] is False)
        check("drifted frame is quarantined (hard-invariant fail)", byid["f_drift"]["quarantined"] is True)
        check("quarantine names the hard failures", len(byid["f_drift"]["hard_failures"]) == 2)

        # soft invariants may vary: hard all hold, soft different/missing -> still passes (score 1.0)
        soft_obj = json.load(open(p))
        soft_score, soft_hard_fail = M.evaluate_frame(soft_obj, {"eye_color": "deep-brown", "mole_below_left_eye": "present"})
        check("hard-hold + missing soft -> score 1.0, no hard fail", soft_score == 1.0 and not soft_hard_fail)
        v_score, v_hard = M.evaluate_frame(soft_obj, {"eye_color": "deep-brown", "mole_below_left_eye": "present", "hair_style": "buzzcut"})
        check("hard-hold + varied soft -> not quarantined", v_score == 1.0 and not v_hard)

        # RUN-001 spec fix: four-pillar HARD structure, mole demoted to SOFT
        pillar_spec = {"identity_invariants": [
            {"key": "eye_color", "value": "deep-brown", "hard": True},
            {"key": "face_geometry", "value": "angular", "hard": True},
            {"key": "build", "value": "lean", "hard": True},
            {"key": "complexion", "value": "even-mid", "hard": True},
            {"key": "mole_below_left_eye", "value": "present", "hard": False},
        ]}
        pillars_ok = {"eye_color": "deep-brown", "face_geometry": "angular", "build": "lean", "complexion": "even-mid"}
        s_nomole, hf_nomole = M.evaluate_frame(pillar_spec, dict(pillars_ok, mole_below_left_eye="absent"))
        check("missing mole + 4 pillars hold -> NOT quarantined", s_nomole == 1.0 and not hf_nomole)
        s_eye, hf_eye = M.evaluate_frame(pillar_spec, dict(pillars_ok, eye_color="blue"))
        check("wrong eyes -> still quarantines", bool(hf_eye))
        s_face, hf_face = M.evaluate_frame(pillar_spec, dict(pillars_ok, face_geometry="round"))
        check("wrong face geometry -> still quarantines", bool(hf_face))
        s_build, hf_build = M.evaluate_frame(pillar_spec, dict(pillars_ok, build="heavy"))
        check("wrong build -> still quarantines", bool(hf_build))
        s_comp, hf_comp = M.evaluate_frame(pillar_spec, dict(pillars_ok, complexion="pale"))
        check("wrong complexion -> still quarantines", bool(hf_comp))

    finally:
        shutil.rmtree(sandbox, ignore_errors=True)

    npass = sum(1 for _, ok in results if ok); nfail = sum(1 for _, ok in results if not ok)
    print(f"\nRESULT: {npass} pass / {nfail} fail")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
