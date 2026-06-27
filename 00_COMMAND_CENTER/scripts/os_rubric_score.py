#!/usr/bin/env python3
"""
os_rubric_score.py

W3 keystone fix from ENGINE_WIRING_001 / INTERNAL_AGENCY_ENGINE_AUDIT_001.

Closes the scoring hole the agency audit named: a single composite score is
BANNED, a per-axis VECTOR is required, and there was no executable instrument
that converts an observation into a number against fixed anchors and refuses a
composite-only score.

This is the machine behind W3/RUBRIC_SPEC.md. It consumes a JSON score record
that carries an 11-axis vector (each axis 1..100) plus a one-line evidence
string per axis. It FAILS CLOSED (exit 2), never default-passes, on:
  - a missing axis (any of the 11 not present)
  - a non-numeric score, a non-integer score, or a score out of range (1..100)
  - an empty or placeholder evidence string on any axis
  - a bare composite score with no per-axis vector ("axes" absent/empty, or a
    top-level "composite"/"score"/"total" with no axes)

On PASS it prints the per-axis vector, the floor axis by name, the computed
readiness tier (the FLOOR rule, never the average), and exits 0.

The readiness tier is the FLOOR of the 11 axes, not the average. One weak axis
caps the whole artifact. This is the rule the banned composite existed to hide.

Usage:
  python os_rubric_score.py --score <path>

Exit codes:
  0 = PASS
  2 = FAIL (any reason, including any error reaching a verdict)

Stock Python 3 only. No external pip installs.
Composed with the fail-closed pattern of os_activation_gate.py.
"""

import argparse
import json
import numbers
import os
import sys


# The 11 axes, in canonical order. Operator-named, W3-locked.
AXES = [
    "creative_originality",
    "visual_excellence",
    "source_activation",
    "story_engine",
    "character_engine",
    "market_usefulness",
    "deck_readiness",
    "execution_speed",
    "money_potential",
    "operator_excitement",
    "low_bullshit",
]

# Any top-level numeric key like these, with no axes vector, is a bare composite.
COMPOSITE_KEYS = {"composite", "score", "total", "overall", "average", "avg", "final"}

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
    "",
}

# Readiness anchors (the five-point ladder from RUBRIC_SPEC Section 1).
TIERS = [
    (90, "CLIENT-READY (agency / client-ready)"),
    (80, "STRONG INTERNAL BUILD"),
    (70, "USABLE / NEEDS SENIOR REVISION"),
    (60, "WEAK DRAFT"),
]
REBUILD_TIER = "REBUILD (below 60)"


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
    return isinstance(value, str) and value.strip() != ""


def _is_placeholder(value):
    if not _nonempty_str(value):
        return True
    return value.strip().lower() in PLACEHOLDER_VALUES


def _is_valid_score(value):
    """
    True only for an integer-valued number in 1..100.
    Rejects bools (bool is a subclass of int in Python), strings, floats with a
    fractional part, and out-of-range values. Fail-closed on anything fishy.
    """
    if isinstance(value, bool):
        return False
    if not isinstance(value, numbers.Number):
        return False
    # reject floats that are not whole numbers
    if isinstance(value, float) and not value.is_integer():
        return False
    ivalue = int(value)
    return 1 <= ivalue <= 100


def _tier_for(value):
    for threshold, label in TIERS:
        if value >= threshold:
            return label
    return REBUILD_TIER


def evaluate(record, report_lines):
    """
    Return True only if the record carries a complete, legal 11-axis vector.
    Fail closed on every gap. On pass, print the vector, the floor axis, and the
    tier computed by the FLOOR rule (never the average).
    """
    if not isinstance(record, dict):
        return _fail(report_lines, "score record is not a JSON object")

    axes = record.get("axes")

    # --- refuse a bare composite with no per-axis vector ---
    if not isinstance(axes, dict) or not axes:
        bare_composite = [k for k in record.keys() if k.lower() in COMPOSITE_KEYS]
        if bare_composite:
            return _fail(
                report_lines,
                "bare composite score with no per-axis vector (found top-level %s; "
                "a single composite number is BANNED, an 11-axis vector is required)"
                % ", ".join("'%s'" % k for k in bare_composite),
            )
        return _fail(
            report_lines,
            "record has no 'axes' vector; a single composite number is BANNED, "
            "all 11 axes are required",
        )

    # a composite key alongside the vector is also illegal: no one number for an output
    stray_composite = [k for k in record.keys() if k.lower() in COMPOSITE_KEYS]
    if stray_composite:
        return _fail(
            report_lines,
            "record carries a banned composite key alongside the vector (%s); "
            "remove it, the vector is the only legal score"
            % ", ".join("'%s'" % k for k in stray_composite),
        )

    ok = True
    scores = {}

    # --- per-axis fail-closed validation (all 11 required) ---
    for axis in AXES:
        entry = axes.get(axis)
        if entry is None:
            ok = _fail(report_lines, "missing axis '%s'" % axis)
            continue
        if not isinstance(entry, dict):
            ok = _fail(report_lines, "axis '%s' is not an object with score+evidence" % axis)
            continue

        score = entry.get("score")
        evidence = entry.get("evidence")

        problems = []
        if score is None:
            problems.append("missing score")
        elif not _is_valid_score(score):
            problems.append("score not an integer in 1..100 (got %r)" % score)

        if not _nonempty_str(evidence):
            problems.append("empty evidence")
        elif _is_placeholder(evidence):
            problems.append("placeholder evidence (%r)" % evidence)

        if problems:
            ok = _fail(report_lines, "axis '%s': %s" % (axis, "; ".join(problems)))
            continue

        scores[axis] = int(score)

    # --- reject any unknown axis names (typo / smuggled axis) ---
    for key in axes.keys():
        if key not in AXES:
            ok = _fail(report_lines, "unknown axis '%s' is not one of the 11 W3 axes" % key)

    if not ok:
        return False

    # --- all 11 valid: compute the FLOOR, never the average ---
    floor_value = min(scores[a] for a in AXES)
    floor_axes = [a for a in AXES if scores[a] == floor_value]
    tier = _tier_for(floor_value)

    fmt = record.get("format_declared")
    report_lines.append("FORMAT DECLARED: %s" % (fmt if _nonempty_str(fmt) else "(none declared)"))
    if not _nonempty_str(fmt):
        report_lines.append(
            "  note: format not declared. Scoring without a declared surface is a "
            "HALT in the rubric; this run accepts the vector but the artifact "
            "cannot be crowned until a format is declared."
        )
    report_lines.append("")
    report_lines.append("PER-AXIS VECTOR (the only legal score; no composite):")
    width = max(len(a) for a in AXES)
    for axis in AXES:
        report_lines.append(
            "  %-*s : %3d   %s" % (width, axis, scores[axis], axes[axis]["evidence"].strip())
        )
    report_lines.append("")
    report_lines.append("FLOOR RULE (tier = the lowest axis, never the average):")
    report_lines.append("  floor value : %d" % floor_value)
    report_lines.append("  floor axis  : %s" % ", ".join(floor_axes))
    report_lines.append("  READINESS TIER: %s" % tier)
    report_lines.append("")
    report_lines.append(
        "  One weak axis caps the artifact. Raise the floor axis to lift the tier."
    )

    return True


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Fail-closed per-axis rubric scorer (W3, ENGINE_WIRING_001)."
    )
    parser.add_argument("--score", required=True, help="path to a JSON score record")
    args = parser.parse_args(argv)

    report_lines = []
    report_lines.append("=" * 70)
    report_lines.append("OS RUBRIC SCORE (fail-closed, per-axis vector, floor tier)")
    report_lines.append("=" * 70)

    record, r_ok = load_json(args.score, "score record", report_lines)

    if not (r_ok and record is not None):
        verdict = False
    else:
        verdict = evaluate(record, report_lines)

    report_lines.append("-" * 70)
    report_lines.append("VERDICT: %s" % ("PASS" if verdict else "FAIL"))
    if not verdict:
        report_lines.append(
            "This score record is NOT legal: a required axis is missing, a score is "
            "out of range or non-numeric, an evidence string is empty/placeholder, "
            "or a banned composite was supplied with no per-axis vector. "
            "Fail-closed by design."
        )
    report_lines.append("=" * 70)

    print("\n".join(report_lines))
    return 0 if verdict else 2


if __name__ == "__main__":
    sys.exit(main())
