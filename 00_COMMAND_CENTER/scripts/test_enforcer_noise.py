#!/usr/bin/env python3
"""Test battery for FALSE TRIGGER / ENFORCER NOISE PATCH 001.

Proves the trigger/enforcer hygiene distinguishes real intent/claims from negated safety
language, assistant receipts, and quoted source, WITHOUT weakening the gate on a real claim.
Run: python3 test_enforcer_noise.py
"""
import os, sys, json, tempfile, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))

def _imp(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

th = _imp("os_trigger_hygiene")
pm = _imp("os_proof_manifest")
CW = pm.COMPLETION_WORDS

GEN = ["generate", "generation", "run batch", "batch 3", "render", "create image"]
PUB = ["post", "publish", "ship", "send it"]
SPEND = ["spend", "credits"]

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# A. negated safety recap must NOT trigger generation, and reads as a state report
A = "Nothing generated, nothing posted, held at boundary."
check("A no-gen-trigger", th.negation_safe_trigger(A, GEN) is None, repr(th.negation_safe_trigger(A, GEN)))
check("A is state_report", th.looks_like_state_report(A, CW), "")

# B. "do not run Batch 3" must NOT trigger a batch run
B = "Do not run Batch 3 on the tray."
check("B no-batch-trigger", th.negation_safe_trigger(B, GEN) is None, repr(th.negation_safe_trigger(B, GEN)))

# C. "the tray is not crowned" must NOT register a completion/crown claim
C = "The tray is not crowned and nothing is final."
check("C no-completion-claim", th.affirmative_hits(C, CW + ["crowned", "crown"]) == [], repr(th.affirmative_hits(C, CW + ["crowned", "crown"])))

# D. "generate Batch 3 now" MUST trigger generation intent
D = "Generate Batch 3 now."
check("D fires-generate", th.negation_safe_trigger(D, GEN) == "generate", repr(th.negation_safe_trigger(D, GEN)))

# E. "post this" MUST trigger the publish boundary
E = "Post this to the feed."
check("E fires-post", th.negation_safe_trigger(E, PUB) == "post", repr(th.negation_safe_trigger(E, PUB)))

# F. a quoted prompt containing "generate" must NOT trigger (quoted source)
F = 'The reel said: "generate 6 variants of the hero" but I did not act on it.'
check("F quoted-suppressed", th.negation_safe_trigger(F, GEN) is None, repr(th.negation_safe_trigger(F, GEN)))

# G. assistant receipt "no spend" must NOT trigger the spend gate, and reads as state report
G = "Confirmed: no spend on this run, nothing posted, held at the approval boundary."
check("G no-spend-trigger", th.negation_safe_trigger(G, SPEND) is None, repr(th.negation_safe_trigger(G, SPEND)))
check("G is state_report", th.looks_like_state_report(G, CW), "")

# H. a documented manifest with send_no_send=no is a VALID held state
tmp = tempfile.mkdtemp()
json.dump({"task_type": "image_design", "task": "held test", "deliverable_promised": True,
           "required_artifacts": {}, "required_gates": {}, "send_no_send": "no",
           "status_note": "PROOF / TEST BATCH, held at the External Visual Proof Gate",
           "known_gaps": ["operator sign-off pending"]},
          open(os.path.join(tmp, "PROOF_MANIFEST.json"), "w"))
check("H held-state-valid", pm.is_valid_held_state(tmp), "")

# POSITIVE CONTROLS (safety not weakened): real affirmative claims MUST still register.
P1 = "The deck is done and client-ready, shipped to the client this morning."
check("P1 real-completion-fires", len(th.affirmative_hits(P1, CW)) >= 1, repr(th.affirmative_hits(P1, CW)))
P2 = "Generate the hero now and post it."
check("P2 real-intent-fires", th.negation_safe_trigger(P2, GEN) == "generate" and th.negation_safe_trigger(P2, PUB) == "post", "")
# words-inside-words must NOT false-fire
P3 = "This completion enforcer note is incomplete; finally finalize later."
check("P3 no-substring-falsefire", th.affirmative_hits(P3, CW) == [], repr(th.affirmative_hits(P3, CW)))

print("=== FALSE TRIGGER / ENFORCER NOISE PATCH 001 - test battery ===")
ok = True
for name, passed, detail in results:
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"   -> {detail}" if (not passed and detail) else ""))
    ok = ok and passed
print(f"=== {'ALL PASS' if ok else 'FAILURES PRESENT'} ({sum(1 for _,p,_ in results if p)}/{len(results)}) ===")
sys.exit(0 if ok else 1)
