#!/usr/bin/env python3
"""
os_proof_manifest.py - the arbiter of completion. Defines per-domain REQUIRED artifacts + gates,
reads/writes PROOF_MANIFEST.json in a production folder, and verifies a completion claim against reality.

The OS cannot say "done / final / client-ready" for a production task unless verify() passes here.

  os_proof_manifest.py init <folder> --domain film --task "..."     # scaffold a manifest with the domain's required slots
  os_proof_manifest.py verify <folder>                              # PASS/FAIL + what is missing (exit 0 pass, 2 fail)
  os_proof_manifest.py audit [root]                                 # scan all PROOF_MANIFEST.json, print send/no-send
"""
import sys, os, json, glob, subprocess, time

HERE = os.path.dirname(os.path.abspath(__file__))
CC = os.path.dirname(HERE)
ROOT = os.path.dirname(CC)

# Per-domain required completion artifacts + gates. Soft domains gate only if a deliverable is promised.
DOMAIN_REQUIREMENTS = {
    "film": {
        "hard": True,
        "artifacts": ["activation_manifest", "action_beat_sheet", "shot_classification_table", "tool_choice_per_shot",
                       "watch_pass", "hostile_review", "rebuild_list", "final_export_path", "proof_packet", "scorecard"],
        "gates": ["watch", "hostile_review", "story_gate", "push_in_law", "twelve_axis", "owned_music", "nine_floor"],
    },
    "image_design": {
        "hard": True,
        "artifacts": ["composite_master_qa", "crops_100", "before_after_or_proof_sheet", "scorecard"],
        "gates": ["vision_reject", "composite_qa", "skin_identity_drift", "platform_mastering_if_client"],
    },
    "photo": {
        "hard": True,
        "artifacts": ["composite_master_qa", "platform_mastering_if_client", "crops_100", "before_after_or_proof_sheet", "scorecard"],
        "gates": ["vision_reject", "composite_qa", "skin_identity_drift", "subject_identity_untouched"],
    },
    "design": {
        "hard": True,
        "artifacts": ["intended_audience", "slide_page_review", "readability_mobile_check", "export_path"],
        "gates": ["no_method_leak_if_selling_outcome", "brand_consistency"],
    },
    "website_build": {
        "hard": True,
        "artifacts": ["build", "responsive_check", "deploy_path"],
        "gates": ["completion_verification", "legal_risk"],
    },
    "writing": {
        "hard": False,  # gate only if deliverable_promised=true in manifest
        "artifacts": ["audience", "output_file"],
        "gates": ["voice_no_emdash", "story_gate"],
    },
    "research": {
        "hard": False,
        "artifacts": ["deliverable", "sources_cited_dated"],
        "gates": ["source_freshness", "anti_hallucination"],
    },
    "strategy": {"hard": False, "artifacts": ["deliverable"], "gates": ["no_crown"]},
}

COMPLETION_WORDS = ["done", "final", "finalized", "client-ready", "client ready", "sendable", "ready to send",
                    "send it", "complete", "completed", "finished", "deck built", "video finished",
                    "hero passed", "shipped", "ready to ship", "good to go", "publish", "delivered"]

def manifest_path(folder):
    return os.path.join(folder, "PROOF_MANIFEST.json")

def git_commit():
    try:
        return subprocess.run(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True).stdout.strip() or None
    except Exception:
        return None

def load(folder):
    p = manifest_path(folder)
    return json.load(open(p)) if os.path.exists(p) else None

def init(folder, domain, task):
    req = DOMAIN_REQUIREMENTS.get(domain, DOMAIN_REQUIREMENTS["film"])
    m = {
        "task_type": domain,
        "task": task,
        "folder": folder,
        "deliverable_promised": req["hard"],
        "activated_standards": [],
        "files_generated": [],
        "required_artifacts": {a: "" for a in req["artifacts"]},
        "required_gates": {g: "" for g in req["gates"]},
        "scores": {},
        "known_gaps": [],
        "send_no_send": "no",
        "last_updated": "(set on update)",
        "commit": git_commit(),
    }
    os.makedirs(folder, exist_ok=True)
    json.dump(m, open(manifest_path(folder), "w"), indent=2)
    print(f"PROOF_MANIFEST scaffolded -> {manifest_path(folder)} (domain={domain})")
    print("Fill required_artifacts (path/desc) + required_gates (pass/fail) + send_no_send before claiming done.")

def verify(folder, claim="(completion claim)"):
    m = load(folder)
    if m is None:
        return False, ["NO PROOF_MANIFEST.json in this production folder"], []
    domain = m.get("task_type", "film")
    req = DOMAIN_REQUIREMENTS.get(domain, DOMAIN_REQUIREMENTS["film"])
    hard = req["hard"] or m.get("deliverable_promised")
    if not hard:
        return True, [], []  # soft domain, no deliverable promised -> not gated
    missing = [a for a, v in m.get("required_artifacts", {}).items() if not str(v).strip()]
    failed = [g for g, v in m.get("required_gates", {}).items()
              if str(v).strip().lower() not in ("pass", "n/a", "na", "skip-justified") and not str(v).strip().startswith("pass")]
    send = str(m.get("send_no_send", "no")).strip().lower()
    blockers = []
    if missing: blockers += [f"missing artifact: {a}" for a in missing]
    if failed: blockers += [f"gate not passed: {g}={m['required_gates'][g] or 'blank'}" for g in failed]
    if send not in ("yes", "send"): blockers.append(f"send_no_send = '{send}' (not approved to send)")
    ok = not blockers
    return ok, blockers, [domain]

def is_valid_held_state(folder):
    """A documented HELD proof state (send_no_send='no' WITH status_note or known_gaps recorded) is a
    VALID terminal state, not a completion failure to repair. FALSE TRIGGER / ENFORCER NOISE PATCH 001.
    The completion enforcer must not loop on a held state; only an AFFIRMATIVE done/ship claim does."""
    m = load(folder)
    if m is None:
        return False
    send = str(m.get("send_no_send", "")).strip().lower()
    documented = bool(str(m.get("status_note", "")).strip()) or bool(m.get("known_gaps"))
    return send in ("no", "hold", "held") and documented


def audit(root=None):
    root = root or ROOT
    found = glob.glob(os.path.join(root, "**", "PROOF_MANIFEST.json"), recursive=True)
    print(f"=== PROOF MANIFEST AUDIT ({len(found)} found) ===")
    for p in found:
        try:
            m = json.load(open(p))
            ok, blockers, _ = verify(os.path.dirname(p))
            print(f"[{'SENDABLE' if ok else 'BLOCKED '}] {m.get('task_type','?'):12} {m.get('task','?')[:40]:40} -> {os.path.relpath(p, root)}")
            if not ok:
                for b in blockers[:4]:
                    print(f"             - {b}")
        except Exception as e:
            print(f"[ERROR  ] {p}: {e}")

def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); return
    def opt(n, d=None):
        if n in a:
            i = a.index(n); v = a[i + 1]; del a[i:i + 2]; return v
        return d
    domain = opt("--domain", "film"); task = opt("--task", "(unnamed)")
    cmd = a[0]
    if cmd == "init" and len(a) > 1:
        init(os.path.abspath(a[1]), domain, task)
    elif cmd == "verify" and len(a) > 1:
        ok, blockers, doms = verify(os.path.abspath(a[1]))
        print(f"{'PASS' if ok else 'FAIL'} (domain={doms[0] if doms else '?'})")
        for b in blockers:
            print(f"  - {b}")
        sys.exit(0 if ok else 2)
    elif cmd == "audit":
        audit(os.path.abspath(a[1]) if len(a) > 1 else None)
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
