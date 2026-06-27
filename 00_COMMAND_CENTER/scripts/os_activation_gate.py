#!/usr/bin/env python3
"""
os_activation_gate.py

W1 keystone fix from INTERNAL_AGENCY_ENGINE_AUDIT_001.

Converts the OS enforcement (source-activation registry) from prose law that a
build only applies if it remembers to, into a machine-readable, FAIL-CLOSED gate.

A build cannot pass for a declared task_type unless it PROVES, per the activation
manifest, that every REQUIRED source mechanism for that task type fired with:
  - a non-empty fired_condition token
  - evidence that resolves to a real on-disk artifact or line
  - a non-empty, non-placeholder visible_feature

This closes the PLAN-SIDE activation gap named in the audit (the registry was a
verifier-on-paper). It does NOT prove pixels: the pixel-side measurement gate
(audit item W5) still needs one real render. This gate is honest about that:
when an activation record marks a mechanism plan-stage only, the gate reports
PASS (plan-stage) and flags that pixel proof is pending. It never upgrades a
plan-stage proof into a pixel claim.

FAIL CLOSED is the whole point. Every one of these is a FAIL, never a default
pass:
  - missing or unreadable manifest
  - missing or unreadable record
  - unknown / undeclared task_type
  - a required mechanism absent from the record
  - a required mechanism present but with empty, placeholder, or unresolved evidence
  - a required mechanism present but with empty or placeholder visible_feature
  - a required mechanism the record explicitly marks fired:false

Usage:
  python os_activation_gate.py --manifest <path> --record <path> --task-type <t>

Exit codes:
  0 = PASS
  2 = FAIL (any reason, including any error reaching a verdict)

Stock Python 3 only. No external pip installs.
"""

import argparse
import json
import os
import re
import sys


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
PLACEHOLDER_VALUES = {
    "n/a",
    "na",
    "none",
    "null",
    "todo",
    "tbd",
    "placeholder",
    "missing",
    "unknown",
    "not sure",
    "not applicable",
    "...",
    "-",
}


def _fail(report_lines, reason):
    """Append a fatal reason and signal a fail-closed verdict."""
    report_lines.append("FAIL-CLOSED: " + reason)
    return False


def load_json(path, label, report_lines):
    """Load a JSON file. Any problem is a FAIL, never a silent pass."""
    if not path:
        return None, _fail(report_lines, "no %s path supplied" % label)
    if not os.path.isfile(path):
        return None, _fail(report_lines, "%s not found on disk: %s" % (label, path))
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError) as exc:
        return None, _fail(report_lines, "%s could not be parsed as JSON (%s): %s" % (label, exc, path))
    return data, True


def _nonempty_str(value):
    """True only for a non-empty, non-whitespace string."""
    return isinstance(value, str) and value.strip() != ""


def _is_placeholder(value):
    """True for common placeholder tokens that should never count as proof."""
    if not _nonempty_str(value):
        return True
    clean = value.strip().lower()
    return clean in PLACEHOLDER_VALUES


def _candidate_paths_from_evidence(evidence):
    """
    Extract plausible repo paths from an evidence string.

    W1b requires evidence to resolve to a real artifact, not just prose. Accepted:
      - path/to/file.md
      - path/to/file.md:12
      - path/to/file.md#L12
      - file=path/to/file.md or source: path/to/file.md
    """
    if not _nonempty_str(evidence):
        return []

    tokens = []
    for raw in re.split(r"[\s,;()<>\"']+", evidence.strip()):
        token = raw.strip()
        if not token:
            continue
        token = re.sub(r"^(file|path|source|record|artifact)[:=]", "", token, flags=re.I)
        token = token.rstrip(".")
        if "/" not in token and not re.search(r"\.(md|json|jsonl|csv|txt|py|js|ts|tsx|jsx|html|css|png|jpg|jpeg|webp|pdf)$", token, re.I):
            continue
        tokens.append(token)

    return tokens


def _resolve_evidence_reference(evidence):
    """
    Return (ok, detail). Evidence must include at least one resolvable file ref.
    A line ref, when present, must be a positive line number that exists.
    """
    tokens = _candidate_paths_from_evidence(evidence)
    if not tokens:
        return False, "evidence has no resolvable path token"

    checked = []
    for token in tokens:
        line_no = None
        path_token = token

        m_hash = re.match(r"^(.*)#L(\d+)$", path_token)
        if m_hash:
            path_token = m_hash.group(1)
            line_no = int(m_hash.group(2))
        else:
            m_colon = re.match(r"^(.*?):(\d+)$", path_token)
            if m_colon and not re.match(r"^[A-Za-z]:\\", path_token):
                path_token = m_colon.group(1)
                line_no = int(m_colon.group(2))

        candidates = []
        if os.path.isabs(path_token):
            candidates.append(path_token)
        else:
            candidates.append(os.path.join(os.getcwd(), path_token))
            candidates.append(os.path.join(ROOT, path_token))

        for candidate in candidates:
            candidate = os.path.normpath(candidate)
            checked.append(candidate)
            if not os.path.isfile(candidate):
                continue
            if line_no is None:
                return True, candidate
            if line_no < 1:
                return False, "%s has invalid line %s" % (path_token, line_no)
            try:
                with open(candidate, "r", encoding="utf-8", errors="ignore") as handle:
                    for idx, _line in enumerate(handle, 1):
                        if idx == line_no:
                            return True, "%s:%s" % (candidate, line_no)
            except OSError as exc:
                return False, "could not read evidence file %s (%s)" % (candidate, exc)
            return False, "%s has no line %s" % (candidate, line_no)

    return False, "evidence path not found on disk; checked: %s" % ", ".join(checked[:4])


def evaluate(manifest, record, task_type, report_lines):
    """
    Return True only if EVERY required mechanism for task_type is proven in the
    record. Fail closed on every gap.
    """
    ok = True

    # --- validate manifest shape ---
    mechanisms = manifest.get("mechanisms")
    required_index = manifest.get("task_type_required_mechanism_ids")
    if not isinstance(mechanisms, list) or not mechanisms:
        return _fail(report_lines, "manifest has no 'mechanisms' array")
    if not isinstance(required_index, dict) or not required_index:
        return _fail(report_lines, "manifest has no 'task_type_required_mechanism_ids' index")

    mech_by_id = {}
    for mech in mechanisms:
        if isinstance(mech, dict) and _nonempty_str(mech.get("id")):
            mech_by_id[mech["id"]] = mech

    # --- validate task type (unknown = FAIL, never default pass) ---
    if not _nonempty_str(task_type):
        return _fail(report_lines, "no task_type supplied")
    if task_type not in required_index:
        return _fail(
            report_lines,
            "unknown task_type '%s'; manifest declares only: %s"
            % (task_type, ", ".join(sorted(required_index.keys()))),
        )

    required_ids = required_index.get(task_type)
    if not isinstance(required_ids, list) or not required_ids:
        return _fail(report_lines, "task_type '%s' has no required mechanism ids in the manifest" % task_type)

    # --- validate record shape ---
    rec_task = record.get("task_type")
    if not _nonempty_str(rec_task):
        ok = _fail(report_lines, "record declares no task_type")
    elif rec_task != task_type:
        ok = _fail(
            report_lines,
            "record task_type '%s' does not match the requested task_type '%s'" % (rec_task, task_type),
        )

    fired = record.get("mechanisms_fired")
    if not isinstance(fired, list):
        return _fail(report_lines, "record has no 'mechanisms_fired' array")

    # index the record's fired mechanisms by id
    fired_by_id = {}
    for entry in fired:
        if isinstance(entry, dict) and _nonempty_str(entry.get("id")):
            fired_by_id[entry["id"]] = entry

    # --- the core fail-closed check, per required mechanism ---
    report_lines.append("Task type: %s" % task_type)
    report_lines.append("Required mechanisms for this task type: %d" % len(required_ids))
    report_lines.append("")

    missing = []
    unproven = []
    plan_stage = []
    proven = []

    for mid in required_ids:
        mech_def = mech_by_id.get(mid)
        mech_name = mech_def.get("name") if mech_def else "(NOT IN MANIFEST)"

        # a required id that is not even in the manifest is a manifest integrity fail
        if mech_def is None:
            ok = _fail(report_lines, "required id '%s' is listed for this task type but is not defined in 'mechanisms'" % mid)
            missing.append(mid)
            continue

        entry = fired_by_id.get(mid)
        if entry is None:
            missing.append(mid)
            ok = False
            continue

        # explicit fired:false is a FAIL
        if entry.get("fired") is False:
            unproven.append((mid, "record marks fired:false"))
            ok = False
            continue

        evidence = entry.get("evidence")
        visible = entry.get("visible_feature")

        problems = []
        if not _nonempty_str(evidence):
            problems.append("empty evidence")
        elif _is_placeholder(evidence):
            problems.append("placeholder evidence")
        else:
            evidence_ok, evidence_detail = _resolve_evidence_reference(evidence)
            if not evidence_ok:
                problems.append("unresolved evidence (%s)" % evidence_detail)
        if not _nonempty_str(visible):
            problems.append("empty visible_feature")
        elif _is_placeholder(visible):
            problems.append("placeholder visible_feature")

        if problems:
            unproven.append((mid, "; ".join(problems)))
            ok = False
            continue

        # proven. note plan-stage honesty without upgrading it to a pixel claim.
        if entry.get("stage") == "plan":
            plan_stage.append(mid)
        proven.append(mid)

    # --- report ---
    if proven:
        report_lines.append("PROVEN (%d):" % len(proven))
        for mid in proven:
            tag = "  [plan-stage, pixel proof pending]" if mid in plan_stage else ""
            report_lines.append("  + %s (%s)%s" % (mid, mech_by_id[mid]["name"], tag))
        report_lines.append("")

    if missing:
        report_lines.append("MISSING from record (%d) -> FAIL:" % len(missing))
        for mid in missing:
            name = mech_by_id[mid]["name"] if mid in mech_by_id else "(not in manifest)"
            report_lines.append("  - %s (%s)" % (mid, name))
        report_lines.append("")

    if unproven:
        report_lines.append("PRESENT BUT UNPROVEN (%d) -> FAIL:" % len(unproven))
        for mid, why in unproven:
            name = mech_by_id[mid]["name"] if mid in mech_by_id else "(not in manifest)"
            report_lines.append("  - %s (%s): %s" % (mid, name, why))
        report_lines.append("")

    return ok


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Fail-closed source-activation gate (W1, INTERNAL_AGENCY_ENGINE_AUDIT_001)."
    )
    parser.add_argument("--manifest", required=True, help="path to ACTIVATION_MANIFEST.json")
    parser.add_argument("--record", required=True, help="path to a build's activation record JSON")
    parser.add_argument("--task-type", required=True, dest="task_type", help="declared task type")
    args = parser.parse_args(argv)

    report_lines = []
    report_lines.append("=" * 70)
    report_lines.append("OS ACTIVATION GATE (fail-closed)")
    report_lines.append("=" * 70)

    manifest, m_ok = load_json(args.manifest, "manifest", report_lines)
    record, r_ok = load_json(args.record, "record", report_lines)

    if not (m_ok and r_ok and manifest is not None and record is not None):
        verdict = False
    else:
        verdict = evaluate(manifest, record, args.task_type, report_lines)

    report_lines.append("-" * 70)
    report_lines.append("VERDICT: %s" % ("PASS" if verdict else "FAIL"))
    if not verdict:
        report_lines.append(
            "This build is NOT crown-eligible: at least one required source mechanism "
            "did not fire with evidence and a visible feature, or the gate could not "
            "reach a clean verdict. Fail-closed by design."
        )
    report_lines.append("=" * 70)

    print("\n".join(report_lines))
    return 0 if verdict else 2


if __name__ == "__main__":
    sys.exit(main())
