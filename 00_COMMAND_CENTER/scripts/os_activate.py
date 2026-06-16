#!/usr/bin/env python3
"""
os_activate.py - THE BRIDGE. Turns any task into the exact activation set from the whole OS body.

The gap this closes: the OS is stacked, but nothing made the relevant skills+docs+gates fire
as one unit for the task in front of you. This reads OS_ACTIVATION_INDEX.json, classifies the
task by trigger match, and emits the activation manifest: authority doc, skills to invoke, docs
to read, gates that must pass, tools, the production loop, and the hard laws.

Usage:
  os_activate.py "make a brand film for synergy"   # classify a task string, print manifest
  os_activate.py --hook                             # read {"prompt":...} JSON on stdin (UserPromptSubmit), print compact manifest
  os_activate.py --list                             # list domains + triggers
"""
import sys, os, json, re

HERE = os.path.dirname(os.path.abspath(__file__))
CC = os.path.dirname(HERE)
INDEX = os.path.join(CC, "OS_ACTIVATION_INDEX.json")
ROOT = os.path.dirname(CC)

def _norm_path(p):
    """Resolve a doc/authority pointer from repo root. Index paths are written relative to
    00_COMMAND_CENTER/; prefix that when the bare path does not resolve from root but does under CC.
    Leaves skill names, absolute paths, and annotated/non-file pointers untouched."""
    if not isinstance(p, str) or not p or p.startswith("/"):
        return p
    if "/" not in p and not p.endswith((".md", ".json", ".csv", ".py", ".sh")):
        return p
    if os.path.exists(os.path.join(ROOT, p)):
        return p
    cc_rel = "00_COMMAND_CENTER/" + p
    if os.path.exists(os.path.join(ROOT, cc_rel)):
        return cc_rel
    return p

def load():
    with open(INDEX) as f:
        return json.load(f)

def classify(task, idx):
    """Word-boundary trigger match (with optional trailing 's'). Avoids 'ad' matching 'thread',
    'edit' matching 'credit', etc., which would over-gate casual work."""
    t = task.lower()
    scores = {}
    for name, d in idx["domains"].items():
        s = 0
        for kw in d["match"]:
            k = kw.strip().lower()
            if not k:
                continue
            if re.search(r"(?<![a-z0-9])" + re.escape(k) + r"s?(?![a-z0-9])", t):
                s += 1
        if s:
            scores[name] = s
    return sorted(scores.items(), key=lambda x: -x[1])

def emergency_block(task, idx):
    t = task.lower()
    if any(trig.lower() in t for trig in idx.get("emergency_triggers", [])):
        sk = idx.get("emergency_skill", "emergency-drop-protocol")
        return ("[EMERGENCY MODE] time pressure detected -> activate " + sk + ": set deadline + the ONE must-have outcome; "
                "cut SCOPE not quality; relax only relaxable gates (record each), NEVER relax identity/legal/vision-reject/brand-core/honest-label; "
                "label honestly (proof/draft/internal/sendable, rarely final); send/no-send on the protected core.")
    return None

def is_serious(task, idx, ranked=None):
    if ranked is None:
        ranked = classify(task, idx)
    t = task.lower()
    hard = any(n in idx.get("hard_production_domains", []) for n, _ in ranked)
    multi = len([1 for _, s in ranked if s >= 2]) >= 2
    kw = any(k.lower() in t for k in idx.get("serious_keywords", []))
    return hard or multi or kw

def cross_domain_skills(top, idx):
    d = idx["domains"].get(top, {})
    out = {}
    for dom in d.get("cross_domain", []):
        dd = idx["domains"].get(dom, {})
        out[dom] = dd.get("skills", [])[:4]  # top few active from each cross domain
    return out

def _client_signal(task):
    """True when the task carries client / pricing / sales language (adds trust_sales to client work)."""
    return bool(re.search(r"(?<![a-z])(client|deliverable|sell|sale|pricing|price|quote|proposal|invoice|commission|retainer|paid|offer)s?(?![a-z])", (task or "").lower()))

def _doctrine_packs(keys):
    """Load compact os_doctrine packs for the given domain keys (order-preserving dedup). Imported by file
    path so it works whether os_activate runs directly or is loaded via importlib by a hook."""
    out = []
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("os_doctrine", os.path.join(HERE, "os_doctrine.py"))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        seen = set()
        for k in keys:
            if k in seen or k not in m.DOCTRINE:
                continue
            seen.add(k)
            out.append(m.cmd_load(k))
    except Exception as e:
        sys.stderr.write(f"[os-activate] doctrine load skipped: {e}\n")
    return out

def manifest(task, idx, compact=False):
    ranked = classify(task, idx)
    out = []
    emg = emergency_block(task, idx)
    if not ranked:
        if emg:
            out.append(emg)
        out.append("[OS ACTIVATE] No domain matched. Run os-command-router to classify, then re-check the index.")
        out.append("ALWAYS: " + " | ".join(idx["always"]))
        return "\n".join(out)
    if emg:
        out.append(emg)
    top = ranked[0][0]
    d = idx["domains"][top]
    also = [n for n, _ in ranked[1:] if _ >= 2]
    _multi = len([1 for _, s in ranked if s >= 2]) >= 2
    _kw = any(k.lower() in (task or "").lower() for k in idx.get("serious_keywords", []))
    fire = (ranked[0][1] >= 2) or _multi or _kw
    if not fire:
        # weak single-keyword match: stay quiet (no loud banner, no doctrine), just hint how to engage.
        out.append(f"[OS] light touch: '{top}' looked possible but the signal was weak. Name the medium (film/video/campaign/landing page/offer/strategy) and add 'client' for client work to activate the full stack.")
        out.append("ALWAYS: " + " | ".join(idx["always"]))
        return "\n".join(out)
    out.append(f"[OS ACTIVATE] domain={top} ({d.get('label','')})" + (f" (+{','.join(also)})" if also else "") + f"  authority={_norm_path(d['authority'])}")
    out.append("ACTIVATE AS ONE BODY before producing. Read the docs, invoke the skills, pass the gates. Do not ship until they pass.")
    out.append("SKILLS (auto): " + (", ".join(d.get("skills", [])) or "none"))
    if d.get("reference_skills"):
        out.append("REFERENCE (available, NOT auto-loaded to avoid bloat; name one to force-load): " + ", ".join(d["reference_skills"]))
    out.append("DOCS to read: " + (", ".join(_norm_path(x) for x in d.get("docs", [])) or "none"))
    out.append("GATES (must pass): " + (", ".join(d.get("gates", [])) or "none"))
    if d.get("production_loop"):
        out.append("LOOP: " + d["production_loop"])
    if d.get("pipeline"):
        out.append("PIPELINE (do not stop at a treatment; run the chain to a shippable asset): " + d["pipeline"])
    if d.get("tools"):
        out.append("TOOLS: " + ", ".join(d["tools"]))
    if d.get("loader"):
        out.append("LOADER: " + d["loader"])
    out.append("WORKFLOWS: standing verify = .claude/workflows/adversarial-verify.workflow.js (run before crowning; pass target + claim). Long/parallel/adversarial work -> spawn a Workflow with role-scoped agents (select/grade/taste/build), always ending in adversarial-verify.")
    for law in d.get("hard_laws", []):
        out.append("LAW: " + law)
    if d.get("gaps"):
        out.append("KNOWN GAPS: " + "; ".join(d["gaps"]))
    if d.get("hard"):
        out.append("PROOF: hard production domain -> os_proof_manifest.py init this folder; Stop gate blocks 'done' without it.")
    # DOCTRINE BIND: auto-inject the compact doctrine pack(s) for this task.
    # Guard fires on a strong/serious match (top score >= 2, multi-domain, or a serious keyword),
    # NOT on a bare single-keyword hard-domain touch (the same guard gates the loud banner above).
    if fire:
        _keys = []
        for _name in [top] + also:
            _keys += idx["domains"].get(_name, {}).get("doctrine", [])
        if _client_signal(task):
            for _name in [top] + also:
                _keys += idx["domains"].get(_name, {}).get("doctrine_client", [])
        _packs = _doctrine_packs(_keys)
        if _packs:
            out.append("INJECTED DOCTRINE (auto-fired; apply now, self-check before output):")
            out.extend(_packs)
    if fire:
        out.append("=== MASTER OS CONDUCTOR: SERIOUS TASK -> MAX CAPABILITY MODE ===")
        out.append("Scan the FULL registry (12 domains / 78 skills), not just this domain. Target 10/10; 9 is the floor not the goal. If 10/10 is blocked, NAME the blocker + the path to remove it.")
        cds = cross_domain_skills(top, idx)
        if cds:
            out.append("CROSS-DOMAIN PULL (consult, integrate what changes the output): " + " | ".join(f"{k}: {', '.join(v)}" for k, v in cds.items()))
        out.append("RECEIPT REQUIRED: produce OS_RECEIPT.md (os_receipt.py init <folder> \"<task>\") proving what activated, what stayed asleep + why, what CHANGED because of activation, gates passed/failed, blockers, rating + why, verdict. Stop gate blocks 'done' on serious work without it.")
        out.append("HARNESS ROUTING (do not grind single-threaded): if the task is LONG, PARALLEL, or ADVERSARIAL (whole-watch many clips, whole-read many docs, multi-asset QA, broad sweep) -> spawn a WORKFLOW (fan out fresh-context agents), not one agent. A few delegated steps -> subagent. Recurring scoped job -> Managed Agent. Cadence/laptop-off -> Routine. End every harness with the adversarial Verify phase.")
        out.append("THREE FAILURE MODES to defend (single long agent): laziness (declares done partial -> count done vs required), self-preferential bias (never self-crown -> route judging to a fresh-context/second-model verify), goal drift (re-read the pinned goal + 'do not' constraints each phase).")
        out.append("Emergency cuts SCOPE, never quality/taste/review. Max mode does not settle for good-enough.")
    out.append("WHY-OMITTED: reference_skills (above) + every other domain's skills stayed asleep by design (not relevant / context-precise). Force-load any by name.")
    out.append("ALWAYS: " + " | ".join(idx["always"]))
    return "\n".join(out)

def main():
    a = sys.argv[1:]
    idx = load()
    if not a:
        print(__doc__); return
    if a[0] == "--list":
        for n, d in idx["domains"].items():
            print(f"{n}: {', '.join(d['match'][:10])}...")
        return
    if a[0] == "--hook":
        raw = sys.stdin.read()
        task = ""
        try:
            task = (json.loads(raw) or {}).get("prompt", "") or ""
        except Exception:
            task = raw
        print(manifest(task, idx, compact=True))
        return
    print(manifest(" ".join(a), idx))

if __name__ == "__main__":
    main()
