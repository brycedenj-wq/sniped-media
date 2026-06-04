#!/usr/bin/env python3
"""Regression suite for os_world.py. Temp sandbox; no real writes."""
import os, sys, json, tempfile, shutil, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("os_world", os.path.join(HERE, "os_world.py"))
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)

results = []
def check(name, cond):
    results.append((name, bool(cond))); print(f"  {'PASS' if cond else 'FAIL'}  {name}")

class A:
    def __init__(self, **kw): self.__dict__.update(kw)


def main():
    sandbox = tempfile.mkdtemp(prefix="worldtest_")
    M.WORLD_DIR = sandbox
    try:
        rc = M.cmd_new(A(slug="world01", name=None))
        check("new creates world scaffold", rc == 0 and os.path.isfile(os.path.join(sandbox, "world01", "WORLD.json")))

        rc = M.cmd_validate(A(slug="world01"))
        check("empty world is INVALID", rc == 1)

        p = os.path.join(sandbox, "world01", "WORLD.json")
        w = json.load(open(p))
        w.update({
            "environments": ["Brutalist Monument", "Monochromatic Void"],
            "materials": ["raw concrete", "oxblood leather"],
            "light_logic": "single dominant source, deep shadow tolerance",
            "color_system": {"foundation": "Adobe Neutral", "palette_hex": ["#2B2B2E", "#4A1C24"],
                             "forbidden_hues": ["teal-orange", "neon"]},
            "camera_language": "editorial restraint, 50/85mm, negative space",
            "forbidden_elements": ["logos", "text overlay", "lens flare", "crowds"],
            "recurring_motifs": ["single figure in vast space", "raking light"],
            "sref_style_slots": [{"slot": 1, "role": "primary editorial", "value": "TBD-manual-pull"}],
            "continuity_rules": ["one environment per chapter", "palette locked"],
        })
        json.dump(w, open(p, "w"), indent=2)
        rc = M.cmd_validate(A(slug="world01"))
        check("complete world is VALID", rc == 0)

        # continuity gate: clean scene passes
        clean = {"environment": "Brutalist Monument", "materials": ["raw concrete"],
                 "palette_hex": ["#2B2B2E"], "elements": ["single figure", "raking light"], "camera": "85mm"}
        sf = os.path.join(sandbox, "clean.json"); json.dump(clean, open(sf, "w"))
        rc = M.cmd_continuity(A(slug="world01", scene=sf))
        check("clean scene passes continuity", rc == 0)

        # forbidden element quarantines
        dirty = {"environment": "Brutalist Monument", "materials": [], "palette_hex": [],
                 "elements": ["logos", "single figure"], "camera": "85mm"}
        df = os.path.join(sandbox, "dirty.json"); json.dump(dirty, open(df, "w"))
        rc = M.cmd_continuity(A(slug="world01", scene=df))
        check("forbidden element quarantines scene", rc == 1)

        # off-rotation environment quarantines
        offenv = {"environment": "Sunny Beach", "materials": [], "palette_hex": [], "elements": [], "camera": "50mm"}
        of = os.path.join(sandbox, "offenv.json"); json.dump(offenv, open(of, "w"))
        rc = M.cmd_continuity(A(slug="world01", scene=of))
        check("off-rotation environment quarantines scene", rc == 1)

    finally:
        shutil.rmtree(sandbox, ignore_errors=True)

    npass = sum(1 for _, ok in results if ok); nfail = sum(1 for _, ok in results if not ok)
    print(f"\nRESULT: {npass} pass / {nfail} fail")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
