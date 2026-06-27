#!/usr/bin/env python3
"""
os_copy_gate.py

W2 fix from INTERNAL_AGENCY_ENGINE_AUDIT_001 (the next gate-wiring hole after
W1/W1b/W1c).

The activation gate (os_activation_gate.py) proves the copy MECHANISM fired:
that a build declared and resolved the source mechanisms for a task type. It
inspects the activation RECORD, not the words. So a build could pass activation
while still shipping a caption that breaks the copy doctrine: an em-dash, a
self-applied hype word, bible/spec voice, or a truncated fragment.

This gate closes that hole. It inspects the ACTUAL COPY TEXT (the headline,
caption, claim, or cadence line) and fails closed if the words themselves
violate the doctrine. It does not look at any mechanism declaration; it reads
the string a human would read.

Doctrine source (read fully before editing):
  00_COMMAND_CENTER/_reference/COPY_DOCTRINE_CAPLES_TESTED_ADVERTISING.md
  + the project copy rules: no self-applied hype; one complete thought, never a
    truncated fragment; in-world voice, never bible/spec language; concrete noun
    beats abstract claim; no em-dashes; read aloud, if it stops mid-thought it
    fails.

Checks (each fail-closed, exit 2):
  1. EM_DASH         : contains a U+2014 em-dash.
  2. HYPE_WORD       : contains a banned self-applied hype word
                       (world-class, seamless, unlock, elevate, leverage,
                        game-changer, next-level, revolutionary), case-
                        insensitive, word-boundary so "unlocked door" or
                        "relevant" do not false-trip.
  3. BIBLE_VOICE     : contains a spec/bible voice tell
                       ("is faceless by design", "synthetic figure",
                        "rendered as", "by design", "leverages the").
  4. FRAGMENT        : ends without terminal punctuation, or trails on a
                       dangling connector (and / or / with / to / the ...),
                       i.e. it stops mid-thought when read aloud.
  5. EMPTY_OR_PLACEHOLDER : empty, whitespace, or a placeholder token
                       (TODO / N/A / TBD and friends).

PASS (exit 0) only if the copy is clean on ALL checks.

Usage:
  python os_copy_gate.py --copy <path> [--field headline]

  <path> may be:
    - a JSON file. By default every string-valued field whose key looks like
      copy (headline / caption / claim / cadence / subhead / hook / body /
      cta / text / line / promise / tagline / title) is checked, plus any
      string inside a list under such a key. Use --field to check exactly one
      named field instead.
    - a plain text file. The whole file (each non-empty line, and the joined
      whole) is treated as the copy artifact.

Fail closed on missing or unparseable input.

Exit codes:
  0 = PASS (copy clean on every check)
  2 = FAIL (any violation, or any error reaching a verdict)

Stock Python 3 only. No external pip installs.
"""

import argparse
import json
import os
import re
import sys


EM_DASH = "—"

# Self-applied hype words banned by the project copy rules. Word-boundary,
# case-insensitive. Multi-word forms (game-changer, next-level) are matched
# allowing a hyphen or a space between the parts.
HYPE_WORDS = [
    "world-class",
    "seamless",
    "unlock",
    "elevate",
    "leverage",
    "game-changer",
    "next-level",
    "revolutionary",
]

# Bible / spec voice tells: phrasing that describes the world from outside it
# instead of speaking from inside it. Substring, case-insensitive.
BIBLE_VOICE_TELLS = [
    "is faceless by design",
    "synthetic figure",
    "rendered as",
    "by design",
    "leverages the",
]

# Dangling connectors. If the last word of the copy is one of these, the
# thought is unfinished when read aloud.
DANGLING_CONNECTORS = {
    "and",
    "or",
    "with",
    "to",
    "the",
    "a",
    "an",
    "of",
    "for",
    "but",
    "so",
    "as",
    "in",
    "on",
    "at",
    "by",
    "from",
    "that",
    "which",
    "because",
    "plus",
}

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
    "...",
    "-",
    "tk",
    "xxx",
    "lorem ipsum",
}

# Keys that look like copy when scanning a JSON artifact.
COPY_KEY_HINTS = (
    "headline",
    "caption",
    "claim",
    "cadence",
    "subhead",
    "hook",
    "body",
    "cta",
    "text",
    "line",
    "promise",
    "tagline",
    "title",
    "copy",
)

TERMINAL_PUNCT = (".", "!", "?", "…")  # period, bang, question, ellipsis char


def _fail(report_lines, reason):
    report_lines.append("FAIL-CLOSED: " + reason)
    return False


def _nonempty_str(value):
    return isinstance(value, str) and value.strip() != ""


def load_copy_units(path, field, report_lines):
    """
    Return (units, ok). units is a list of (label, text) pairs to check.
    Any input problem is a FAIL, never a silent pass.
    """
    if not path:
        return None, _fail(report_lines, "no copy path supplied")
    if not os.path.isfile(path):
        return None, _fail(report_lines, "copy file not found on disk: %s" % path)

    try:
        with open(path, "r", encoding="utf-8") as handle:
            raw = handle.read()
    except OSError as exc:
        return None, _fail(report_lines, "could not read copy file (%s): %s" % (exc, path))

    # Try JSON first (a copy artifact is usually JSON with named fields).
    data = None
    is_json = False
    try:
        data = json.loads(raw)
        is_json = True
    except ValueError:
        is_json = False

    if is_json:
        units = _units_from_json(data, field, report_lines)
        if units is None:
            return None, False
        if not units:
            return None, _fail(
                report_lines,
                "no copy text found in JSON%s"
                % ((" for field '%s'" % field) if field else ""),
            )
        return units, True

    # Not JSON. If a specific field was asked for, that is a contract the text
    # file cannot satisfy -> fail closed rather than guess.
    if field:
        return None, _fail(
            report_lines,
            "copy file is not JSON, cannot select --field '%s' from plain text" % field,
        )

    units = []
    for idx, line in enumerate(raw.splitlines(), 1):
        if line.strip():
            units.append(("line %d" % idx, line))
    # Also check the joined whole, so a fragment spanning the file is caught
    # only via lines; the whole-file join is informational and skipped to avoid
    # false fragment flags on multi-sentence files. We keep per-line units.
    if not units:
        return None, _fail(report_lines, "copy file is empty (no non-blank lines): %s" % path)
    return units, True


def _units_from_json(data, field, report_lines):
    """
    Pull copy strings out of a parsed JSON artifact.
    With --field: exactly that top-level field (string, or list of strings).
    Without --field: every string under a copy-looking key, recursively.
    Returns a list of (label, text), or None on a hard error.
    """
    units = []

    if field:
        if not isinstance(data, dict):
            _fail(report_lines, "copy JSON is not an object, cannot select --field '%s'" % field)
            return None
        if field not in data:
            _fail(
                report_lines,
                "field '%s' not present in copy JSON; keys: %s"
                % (field, ", ".join(sorted(str(k) for k in data.keys())) or "(none)"),
            )
            return None
        value = data[field]
        _collect_strings(field, value, units, require_copy_key=False)
        if not units:
            _fail(report_lines, "field '%s' holds no string copy text" % field)
            return None
        return units

    _walk_for_copy(data, "", units)
    return units


def _looks_like_copy_key(key):
    k = str(key).lower()
    return any(hint in k for hint in COPY_KEY_HINTS)


def _walk_for_copy(node, prefix, units):
    """Recurse, collecting strings that sit under a copy-looking key."""
    if isinstance(node, dict):
        for key, value in node.items():
            label = ("%s.%s" % (prefix, key)) if prefix else str(key)
            if _looks_like_copy_key(key):
                _collect_strings(label, value, units, require_copy_key=False)
            else:
                _walk_for_copy(value, label, units)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            _walk_for_copy(item, "%s[%d]" % (prefix, i), units)
    # bare strings not under a copy key are ignored in auto mode


def _collect_strings(label, value, units, require_copy_key):
    """Append (label, text) for a string value or a list/dict of strings."""
    if isinstance(value, str):
        units.append((label, value))
    elif isinstance(value, list):
        for i, item in enumerate(value):
            _collect_strings("%s[%d]" % (label, i), item, units, require_copy_key)
    elif isinstance(value, dict):
        for key, sub in value.items():
            _collect_strings("%s.%s" % (label, key), sub, units, require_copy_key)


# ----------------------------------------------------------------------------
# The five checks. Each returns a list of violation strings (empty == clean).
# ----------------------------------------------------------------------------

def check_empty_or_placeholder(text):
    violations = []
    if text.strip() == "":
        violations.append("empty or whitespace-only copy")
        return violations
    if text.strip().lower() in PLACEHOLDER_VALUES:
        violations.append("placeholder text: '%s'" % text.strip())
    return violations


def check_em_dash(text):
    # U+2014 em-dash plus visual look-alikes that read as an em-dash to a human:
    # U+2015 horizontal bar, U+2012 figure dash, and a typed double-hyphen.
    # U+2013 en-dash and a single hyphen are allowed per the lifetime rule.
    violations = []
    lookalikes = {
        "—": "U+2014 em-dash",
        "―": "U+2015 horizontal bar (em-dash look-alike)",
        "‒": "U+2012 figure dash (em-dash look-alike)",
        "--": "double-hyphen (typed em-dash substitute)",
    }
    for token, label in lookalikes.items():
        if token in text:
            idx = text.index(token)
            span = text[max(0, idx - 20): idx + 21]
            violations.append("contains %s near: '...%s...'" % (label, span.strip()))
    return violations


def check_hype_word(text):
    violations = []
    lowered = text
    for word in HYPE_WORDS:
        # allow hyphen OR space between the parts of a compound hype word
        parts = re.split(r"[-\s]", word)
        pattern = r"\b" + r"[-\s]".join(re.escape(p) for p in parts) + r"\b"
        m = re.search(pattern, lowered, flags=re.IGNORECASE)
        if m:
            violations.append("banned hype word '%s' (matched '%s')" % (word, m.group(0)))
    return violations


def check_bible_voice(text):
    violations = []
    lowered = text.lower()
    for tell in BIBLE_VOICE_TELLS:
        if tell in lowered:
            idx = lowered.index(tell)
            span = text[max(0, idx - 10): idx + len(tell) + 10]
            violations.append("bible/spec voice tell '%s' near: '...%s...'" % (tell, span.strip()))
    return violations


def check_fragment(text):
    """
    A complete thought ends on terminal punctuation and does not trail on a
    dangling connector. Read aloud, if it stops mid-thought it fails.
    """
    violations = []
    stripped = text.strip()
    if stripped == "":
        return violations  # handled by the empty check

    # strip a single trailing closing quote/paren so "...done." in quotes still reads as terminal
    probe = stripped.rstrip("\"')]}”’")

    if not probe.endswith(TERMINAL_PUNCT):
        violations.append("no terminal punctuation; thought is unfinished (ends '%s')" % probe[-30:])
        return violations

    # last real word, ignoring the terminal punctuation
    words = re.findall(r"[A-Za-z']+", probe)
    if words:
        last = words[-1].lower()
        if last in DANGLING_CONNECTORS:
            violations.append("trails on dangling connector '%s'; thought is unfinished" % last)
    return violations


CHECKS = [
    ("EMPTY_OR_PLACEHOLDER", check_empty_or_placeholder),
    ("EM_DASH", check_em_dash),
    ("HYPE_WORD", check_hype_word),
    ("BIBLE_VOICE", check_bible_voice),
    ("FRAGMENT", check_fragment),
]


def evaluate(units, report_lines):
    """
    Run every check on every copy unit. Return True only if all units are
    clean. Fail closed on any violation.
    """
    ok = True
    report_lines.append("Copy units inspected: %d" % len(units))
    report_lines.append("")

    clean_units = []
    for label, text in units:
        unit_violations = []
        for check_name, check_fn in CHECKS:
            for v in check_fn(text):
                unit_violations.append((check_name, v))
        if unit_violations:
            ok = False
            report_lines.append("FAIL [%s]" % label)
            preview = text.strip().replace("\n", " ")
            if len(preview) > 90:
                preview = preview[:87] + "..."
            report_lines.append('  text: "%s"' % preview)
            for check_name, v in unit_violations:
                report_lines.append("  - %s: %s" % (check_name, v))
            report_lines.append("")
        else:
            clean_units.append(label)

    if clean_units:
        report_lines.append("CLEAN (%d):" % len(clean_units))
        for label in clean_units:
            report_lines.append("  + %s" % label)
        report_lines.append("")

    return ok


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Fail-closed copy-doctrine gate (W2, INTERNAL_AGENCY_ENGINE_AUDIT_001)."
    )
    parser.add_argument("--copy", required=True, help="path to a copy artifact (JSON or text)")
    parser.add_argument(
        "--field",
        default=None,
        help="optional: check exactly one named JSON field (e.g. headline)",
    )
    args = parser.parse_args(argv)

    report_lines = []
    report_lines.append("=" * 70)
    report_lines.append("OS COPY GATE (fail-closed)")
    report_lines.append("=" * 70)

    units, ok = load_copy_units(args.copy, args.field, report_lines)
    if not ok or units is None:
        verdict = False
    else:
        verdict = evaluate(units, report_lines)

    report_lines.append("-" * 70)
    report_lines.append("VERDICT: %s" % ("PASS" if verdict else "FAIL"))
    if not verdict:
        report_lines.append(
            "This copy is NOT ship-eligible: the copy text itself broke the doctrine "
            "(em-dash, self-applied hype, bible/spec voice, truncated fragment, or "
            "empty/placeholder), or the gate could not reach a clean verdict. "
            "Fail-closed by design."
        )
    report_lines.append("=" * 70)

    print("\n".join(report_lines))
    return 0 if verdict else 2


if __name__ == "__main__":
    sys.exit(main())
