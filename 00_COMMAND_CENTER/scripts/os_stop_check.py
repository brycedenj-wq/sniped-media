#!/usr/bin/env python3
"""os-stop-check: Stop hook = PRODUCTION_COMPLETION_ENFORCER.

The OS cannot end a turn claiming a production task is done/final/client-ready unless the
proof trail (PROOF_MANIFEST.json, required artifacts, passed gates, send=yes) exists.

Doctrine: 00_COMMAND_CENTER/_standards/OS_PRODUCTION_COMPLETION_ENFORCER.md (Amendment 2026-06-29:
three-failure-mode law; Guard A live, Guards B+C deferred) and AGENTS.md Orchestration law #2.
Source: 00_COMMAND_CENTER/OS_UPGRADE_FROM_VIDEOS_2026-06-08.md Action #2. Guard A implemented here =
the agentic-laziness defense via PROGRESS_COUNT.json (block a completion claim while done < required).

Logic each Stop:
 1. Read transcript -> last user prompt + last assistant text.
 2. Classify the prompt (os_activate). If no HARD production domain -> do not gate (casual/soft work).
 3. Detect completion language in the assistant text. If none -> allow.
 4. Production + completion claim -> find in-scope PROOF_MANIFEST.json (paths in the message, or
    recently modified). Verify via os_proof_manifest. If missing/blocked -> exit 2 (block) with specifics.
 5. 3-strike loop guard: identical blocker signature 3x -> downgrade to a logged OVERRIDE warning so the
    session is never bricked, but the lie is on record.
Fail-open on any parse error (exit 0) but note to stderr. Also keeps the legacy state-corruption warn.
"""
import sys, os, json, time, re, hashlib, glob, importlib.util, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CC = os.path.dirname(HERE)
ROOT = os.path.dirname(CC)
HARD_DOMAINS = {"film", "image_design", "photo", "design", "website_build"}
STRIKE = "/tmp/os_completion_strike.json"
ACTIVATION_MANIFEST = os.path.join(
    ROOT,
    "OS_V2_UNIVERSAL_ENGINE",
    "AI_NATIVE_BRAND_LAB",
    "ENGINE_WIRING_001",
    "ACTIVATION_MANIFEST.json",
)
ACTIVATION_TASK_TYPES = {"visual_render", "fashion_frame", "character", "world", "deck", "copy"}

def _imp(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def read_transcript(path):
    """Return (last_user_text, last_assistant_text) from a Claude Code JSONL transcript."""
    lu, la = "", ""
    try:
        for line in open(path):
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except Exception:
                continue
            role = o.get("role") or o.get("type") or (o.get("message", {}) or {}).get("role")
            msg = o.get("message", o)
            content = msg.get("content", msg.get("text", ""))
            text = ""
            if isinstance(content, str):
                text = content
            elif isinstance(content, list):
                parts = []
                for c in content:
                    if isinstance(c, dict) and c.get("type") in ("text", None) and isinstance(c.get("text"), str):
                        parts.append(c["text"])
                text = "\n".join(parts)
            if not text:
                continue
            if role == "user" and "tool_result" not in line:
                lu = text
            elif role == "assistant":
                la = text
    except Exception:
        pass
    return lu, la

def find_with(assistant_text, fname):
    """Folders mentioned in the message (preferred) or recently modified that contain <fname>."""
    mentioned = set()
    for mobj in re.finditer(r"[\w./\-]+/[\w./\-]+", assistant_text or ""):
        p = mobj.group(0).strip()
        ap = p if os.path.isabs(p) else os.path.join(ROOT, p)
        d = ap if os.path.isdir(ap) else os.path.dirname(ap)
        if os.path.exists(os.path.join(d, fname)):
            mentioned.add(d)
    if mentioned:
        return list(mentioned)
    recent = set()
    for mp in glob.glob(os.path.join(ROOT, "**", fname), recursive=True):
        try:
            if time.time() - os.path.getmtime(mp) < 7200:
                recent.add(os.path.dirname(mp))
        except Exception:
            pass
    return list(recent)

def candidate_manifests(assistant_text):
    # Prefer manifests whose folder is explicitly mentioned in the completion message (scopes to the task).
    mentioned = set()
    for mobj in re.finditer(r"[\w./\-]+/[\w./\-]+", assistant_text or ""):
        p = mobj.group(0).strip()
        ap = p if os.path.isabs(p) else os.path.join(ROOT, p)
        d = ap if os.path.isdir(ap) else os.path.dirname(ap)
        if os.path.exists(os.path.join(d, "PROOF_MANIFEST.json")):
            mentioned.add(d)
    if mentioned:
        return list(mentioned)
    # Fallback: any manifest modified in the last 2 hours (this session's production).
    recent = set()
    for mp in glob.glob(os.path.join(ROOT, "**", "PROOF_MANIFEST.json"), recursive=True):
        try:
            if time.time() - os.path.getmtime(mp) < 7200:
                recent.add(os.path.dirname(mp))
        except Exception:
            pass
    return list(recent)

def _mentioned_dirs_with(assistant_text, fnames):
    """Folders mentioned in assistant text that contain any required file."""
    dirs = set()
    for mobj in re.finditer(r"[\w./\-]+/[\w./\-]+", assistant_text or ""):
        p = mobj.group(0).strip()
        ap = p if os.path.isabs(p) else os.path.join(ROOT, p)
        d = ap if os.path.isdir(ap) else os.path.dirname(ap)
        for fname in fnames:
            if os.path.exists(os.path.join(d, fname)):
                dirs.add(d)
    return dirs

def candidate_activation_dirs(assistant_text):
    """
    W1c bridge. If a build folder marks activation as required, or provides an
    activation record, the Stop hook auto-runs the activation gate before any
    completion claim is allowed.
    """
    fnames = ("ACTIVATION_REQUIRED.json", "ACTIVATION_RECORD.json", "activation_record.json")
    mentioned = _mentioned_dirs_with(assistant_text, fnames)
    if mentioned:
        return list(mentioned)

    recent = set()
    for fname in fnames:
        for mp in glob.glob(os.path.join(ROOT, "**", fname), recursive=True):
            try:
                if time.time() - os.path.getmtime(mp) < 7200:
                    recent.add(os.path.dirname(mp))
            except Exception:
                pass
    return list(recent)

def _load_json_file(path):
    try:
        return json.load(open(path))
    except Exception:
        return {}

def activation_gate_blockers(assistant_text):
    blockers = []
    dirs = candidate_activation_dirs(assistant_text)
    if not dirs:
        return blockers
    if not os.path.exists(ACTIVATION_MANIFEST):
        return ["activation manifest missing: " + os.path.relpath(ACTIVATION_MANIFEST, ROOT)]

    gate = os.path.join(HERE, "os_activation_gate.py")
    for d in dirs:
        required_path = os.path.join(d, "ACTIVATION_REQUIRED.json")
        record_path = os.path.join(d, "ACTIVATION_RECORD.json")
        alt_record_path = os.path.join(d, "activation_record.json")

        required = _load_json_file(required_path) if os.path.exists(required_path) else {}
        if required.get("record"):
            rp = required["record"]
            record_path = rp if os.path.isabs(rp) else os.path.join(d, rp)
        elif not os.path.exists(record_path) and os.path.exists(alt_record_path):
            record_path = alt_record_path

        task_type = required.get("task_type")
        record = _load_json_file(record_path) if os.path.exists(record_path) else {}
        task_type = task_type or record.get("task_type")

        rel = os.path.relpath(d, ROOT)
        if not task_type or task_type not in ACTIVATION_TASK_TYPES:
            blockers.append(f"{rel}: ACTIVATION_REQUIRED present but task_type is missing or invalid")
            continue
        if not os.path.exists(record_path):
            blockers.append(f"{rel}: activation gate required for {task_type}, but no ACTIVATION_RECORD.json exists")
            continue

        proc = subprocess.run(
            [sys.executable, gate, "--manifest", ACTIVATION_MANIFEST, "--record", record_path, "--task-type", task_type],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if proc.returncode != 0:
            out = (proc.stdout or proc.stderr or "").strip().splitlines()
            tail = " | ".join(out[-8:]) if out else "no activation-gate output"
            blockers.append(f"{rel}: activation gate FAIL for {task_type}: {tail}")
    return blockers

def laziness_blockers(assistant_text):
    """Guard A - agentic-laziness defense (three-failure-mode law, OS_UPGRADE_FROM_VIDEOS Action #2).

    If a task/project folder named in the assistant text carries a PROGRESS_COUNT.json with explicit
    integer done/required counts, a completion claim is blocked while done < required. The guard fires
    ONLY when that file is present; its absence never blocks (existing behavior is preserved). Guards B
    (self-preferential bias) and C (goal drift) are deliberately NOT implemented in this pass.
    Doctrine: _standards/OS_PRODUCTION_COMPLETION_ENFORCER.md Amendment 2026-06-29 (Guard A only)."""
    blockers = []
    for d in find_with(assistant_text, "PROGRESS_COUNT.json"):
        pc = _load_json_file(os.path.join(d, "PROGRESS_COUNT.json"))
        if not isinstance(pc, dict) or "done" not in pc or "required" not in pc:
            continue
        try:
            done = int(pc["done"]); required = int(pc["required"])
        except (TypeError, ValueError):
            continue
        if required > 0 and done < required:
            rel = os.path.relpath(d, ROOT)
            blockers.append(
                f"{rel}: AGENTIC LAZINESS defense (done vs required): PROGRESS_COUNT.json shows "
                f"done={done} < required={required}. Finish all required items, or restate the result "
                f"as a proof/draft with the count named. Do not crown a partial set.")
    return blockers

def strikes(sig):
    try:
        d = json.load(open(STRIKE))
    except Exception:
        d = {}
    n = d.get(sig, 0) + 1
    d = {sig: n}  # keep only current signature
    json.dump(d, open(STRIKE, "w"))
    return n

def legacy_warn():
    """Original state-corruption warn (non-blocking-ish), preserved."""
    import csv
    MAN = os.path.join(CC, "OS_ENGAGEMENT_MANIFEST.csv"); DB = os.path.join(CC, "OS_ENGAGEMENT_DASHBOARD.md")
    MARK = "/tmp/os_stop_warned"
    try:
        rows = list(csv.DictReader(open(MAN))); src = [r for r in rows if r["class"] == "source"]
        from collections import Counter
        V = Counter(r["status"] for r in src).get("read_verified", 0)
        paths = [r["path"] for r in rows]; dup = len(paths) - len(set(paths))
        empty = sum(1 for r in src if not r["status"])
        db = open(DB).read(); m = re.search(r"\((\d+) / [\d,]+ verified", db); db_v = int(m.group(1)) if m else V
        issues = []
        if dup: issues.append(f"{dup} duplicate manifest paths")
        if empty: issues.append(f"{empty} empty-status source rows")
        if abs(db_v - V) > 0: issues.append(f"dashboard {db_v} vs manifest {V} verified")
        if issues and not (os.path.exists(MARK) and time.time() - os.path.getmtime(MARK) < 7200):
            open(MARK, "w").write(str(time.time()))
            sys.stderr.write("[os-stop-check] state contradiction: " + "; ".join(issues) + "\n")
    except Exception:
        pass

def main():
    raw = sys.stdin.read() if not sys.stdin.isatty() else ""
    tpath = ""
    try:
        tpath = (json.loads(raw) or {}).get("transcript_path", "") if raw.strip().startswith("{") else ""
    except Exception:
        pass

    legacy_warn()

    if not tpath or not os.path.exists(tpath):
        sys.exit(0)  # fail-open: cannot read transcript

    lu, la = read_transcript(tpath)
    if not la:
        sys.exit(0)

    # 2. production domain? serious task?
    try:
        act = _imp("os_activate"); idx = act.load()
        ranked = act.classify(lu or la, idx)
        domains = {n for n, _ in ranked}
        serious = act.is_serious(lu or la, idx, ranked)
    except Exception:
        domains, serious = set(), False
    is_prod = bool(domains & HARD_DOMAINS)
    if not (is_prod or serious):
        sys.exit(0)  # not hard production and not serious -> do not gate

    # 3. completion language? (negation/quote/receipt-aware; FALSE TRIGGER / ENFORCER NOISE PATCH 001)
    pm = _imp("os_proof_manifest")
    th = _imp("os_trigger_hygiene")
    # Assistant held-state receipts are STATE_REPORT, not a completion claim -> never gate.
    if th.looks_like_state_report(la, pm.COMPLETION_WORDS):
        th.log_suppress("trigger_suppressed_assistant_receipt", la[:160])
        sys.exit(0)
    # Affirmative claim only: whole-word, not negated, not quoted, not the enforcer's own vocabulary.
    claimed = th.affirmative_hits(la, pm.COMPLETION_WORDS)
    if not claimed:
        if th.raw_present(la, pm.COMPLETION_WORDS):
            th.log_suppress("trigger_suppressed_negated_safety_language", la[:160])
        sys.exit(0)
    # belt-and-suspenders: an explicit not-done disclaimer still suppresses.
    low = la.lower()
    if any(p in low for p in ["not client-ready", "not final", "not done", "is not ready",
                              "no-send", "not sendable", "do not render", "proof not", "still animatic"]):
        th.log_suppress("trigger_suppressed_not_done_disclaimer", la[:160])
        sys.exit(0)

    blockers = []
    detected = sorted(domains & HARD_DOMAINS) or sorted(domains)[:1]

    # 4a. production proof trail (hard domains)
    if is_prod:
        cands = candidate_manifests(la)
        if not cands:
            blockers.append("NO PROOF_MANIFEST.json for a production completion claim. "
                            "Run os_proof_manifest.py init <folder> --domain <d> --task '...', fill it, set send_no_send.")
        else:
            for d in cands:
                ok, bl, doms = pm.verify(d)
                if not ok:
                    blockers.append(f"{os.path.relpath(d, ROOT)} [{doms[0] if doms else '?'}]: " + "; ".join(bl))

    # 4c. Source activation auto-call (W1c)
    blockers.extend(activation_gate_blockers(la))

    # 4d. Guard A: agentic-laziness defense (done vs required). Three-failure-mode law, Guard A only.
    # Doctrine: _standards/OS_PRODUCTION_COMPLETION_ENFORCER.md Amendment 2026-06-29.
    blockers.extend(laziness_blockers(la))

    # 4b. OS_RECEIPT (serious work, the conductor law)
    if serious:
        try:
            rc = _imp("os_receipt")
            rcands = find_with(la, "OS_RECEIPT.md")
            if not rcands:
                blockers.append("NO OS_RECEIPT.md for a SERIOUS task. The conductor requires it. "
                                "Run os_receipt.py init <folder> \"<task>\" and fill Layer 3 (what changed, gates, rating, verdict).")
            else:
                for d in rcands:
                    ok, bl = rc.verify(d)
                    if not ok:
                        blockers.append(f"{os.path.relpath(d, ROOT)} OS_RECEIPT: " + "; ".join(bl))
        except Exception as e:
            sys.stderr.write(f"[conductor] receipt check skipped: {e}\n")

    if not blockers:
        sys.exit(0)  # proof + receipt present and pass -> allow completion

    # 5. loop guard
    sig = hashlib.md5(("|".join(sorted(blockers))).encode()).hexdigest()[:10]
    n = strikes(sig)
    msg = ("[OS CONDUCTOR / COMPLETION ENFORCER] You used completion language "
           f"({', '.join(claimed[:3])}) for a {','.join(detected)}"
           + (" SERIOUS" if serious else "") + " task, but the proof trail is incomplete:\n"
           + "\n".join("  - " + b for b in blockers)
           + "\nDo NOT claim done/final/client-ready. Complete the missing artifacts/gates (PROOF_MANIFEST) and the "
             "OS_RECEIPT (what changed, gates, rating, verdict), or restate the result as a proof/draft with the gap named.")
    if n >= 3:
        sys.stderr.write("[PRODUCTION_COMPLETION_ENFORCER] OVERRIDE LOGGED (3rd identical block): shipping with the "
                         "above unmet blockers on record. This is a known, recorded gap, not a clean completion.\n" + msg + "\n")
        sys.exit(0)  # do not brick the session, but it is on record
    sys.stderr.write(msg + "\n")
    sys.exit(2)

if __name__ == "__main__":
    main()
