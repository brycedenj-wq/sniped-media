#!/usr/bin/env python3
"""os_trigger_hygiene: shared text classification so OS triggers/enforcers stop firing on
negated safety language, assistant state-reports/receipts, quoted source, and words-inside-words.

FALSE TRIGGER / ENFORCER NOISE PATCH 001. Goal: make the gates SMARTER, never weaker.
A real affirmative claim still fires; safety recaps and quoted prompts do not.

Classes a piece of text can carry a keyword in:
  USER_INTENT      - the user asked for the action (fires)
  AFFIRMATIVE      - the assistant claims it happened/is done (fires the completion gate)
  NEGATED_SAFETY   - "no generation", "nothing posted", "not crowned" (suppress)
  STATE_REPORT     - an assistant held-state receipt (suppress)
  QUOTED_SOURCE    - inside quotes / code fences / a pasted prompt (suppress unless told to execute)

Behavioral rule for callers (encode at the call site): if a scanner is UNSURE, ask ONE
clarifying question rather than launching a workflow or repeating the held status.
"""
import re, json, time

LOG = "/tmp/os_trigger_hygiene.log"

# Pure negation markers only (kept conservative so we never suppress a real affirmative claim).
NEG_RE = re.compile(r"(?<![a-z])(no|not|never|without|nothing|none|cannot|neither|nor)(?![a-z])|n't|no-", re.I)

# The enforcer's own vocabulary, echoed inside an explanation, must not count as a claim.
META = ["completion enforcer", "completion language", "completion claim", "completion word",
        "production_completion_enforcer", "completion-verification", "completion gate",
        "stop gate", "stop-check", "stop check", "the enforcer", "trigger word", "send_no_send",
        "trigger_suppressed", "false trigger", "enforcer noise"]

# Held / safety state-report markers. Presence of one of these + NO affirmative claim = STATE_REPORT.
HELD_MARKERS = ["held at the approval boundary", "held at boundary", "approval boundary",
                "send_no_send = no", "send_no_send=no", "send_no_send': 'no", "send_no_send\": \"no",
                "no generation", "nothing generated", "nothing is generated", "do not generate",
                "no spend", "nothing posted", "no post", "not crowned", "no crown", "nothing crowned",
                "stop and hold", "stop and show", "holding for", "awaiting operator", "awaiting your",
                "nothing generates", "parked", "in progress", "state report", "state_report", "held state"]


def log_suppress(reason, detail=""):
    try:
        with open(LOG, "a") as f:
            f.write(json.dumps({"t": int(time.time()), "reason": reason, "detail": (detail or "")[:200]}) + "\n")
    except Exception:
        pass


def strip_quoted(text):
    """Remove fenced code blocks, markdown blockquotes, and inline double-quoted spans so a
    pasted prompt / quoted source does not count as the assistant's own claim. Single quotes are
    left intact on purpose (contractions/possessives would cause false strips)."""
    if not text:
        return ""
    t = re.sub(r"```.*?```", " ", text, flags=re.S)     # fenced code blocks
    t = re.sub(r"^\s*>.*$", " ", t, flags=re.M)          # blockquote lines
    t = re.sub(r"\"[^\"]{0,600}\"", " ", t)              # inline "double quoted" spans
    return t


def _word_pat(word):
    # word-boundary; spaces/hyphens in the keyword match either; allow common verb/plural suffixes.
    core = re.escape(word.lower()).replace(r"\ ", r"[\s\-]")
    return r"(?<![a-z0-9])" + core + r"(?:s|ed|ing|d)?(?![a-z0-9])"


def _spans(text, word):
    return [(m.start(), m.end()) for m in re.finditer(_word_pat(word), text or "", flags=re.I)]


def _negated_before(text, start, window=44):
    return bool(NEG_RE.search(text[max(0, start - window):start]))


def _in_meta(text, start, window=60):
    seg = text[max(0, start - window):start + window].lower()
    return any(mw in seg for mw in META)


def raw_present(text, words):
    """True if any keyword appears at all as a whole word (before negation/quote filtering)."""
    return any(_spans(text, w) for w in words)


def affirmative_hits(text, words, strip=True):
    """Keywords that appear as a GENUINE affirmative claim: whole word, not negated, not quoted,
    not inside the enforcer's own meta-vocabulary."""
    src = strip_quoted(text) if strip else (text or "")
    hits = []
    for w in words:
        for (s, _e) in _spans(src, w):
            if _negated_before(src, s) or _in_meta(src, s):
                continue
            hits.append(w.lower())
            break
    return hits


def looks_like_state_report(assistant_text, completion_words):
    """True when the assistant text is a held/safety state-report with NO affirmative completion claim."""
    low = (assistant_text or "").lower()
    has_held = any(m in low for m in HELD_MARKERS)
    return has_held and not affirmative_hits(assistant_text, completion_words)


def negation_safe_trigger(text, triggers, strip=True):
    """For UserPromptSubmit scanners (emergency / boundary): return the first trigger that fires
    as a whole-word, NON-negated, NON-quoted occurrence, else None."""
    src = strip_quoted(text) if strip else (text or "")
    for trig in triggers:
        tl = str(trig).strip().lower()
        if not tl:
            continue
        for (s, _e) in _spans(src, tl):
            if not _negated_before(src, s):
                return tl
    return None


def actions_in_transcript(path, names):
    """Set of the given tool names that ACTUALLY appear as tool_use in the transcript (words
    alone should not imply an action happened; check the log)."""
    found = set()
    try:
        with open(path) as f:
            for line in f:
                for n in names:
                    if ('"name": "' + n) in line or ('"name":"' + n) in line:
                        found.add(n)
    except Exception:
        pass
    return found
