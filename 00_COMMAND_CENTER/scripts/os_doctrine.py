#!/usr/bin/env python3
"""
os_doctrine.py , THE DOCTRINE-FUSION LAYER. Makes the OS move as one thing, quality built in.

The thesis (operator): the OS must be ONE organism. If we touch copy and there are 20 books on copy
in the OS, the copy is perfect THERE AND THEN. Copy was just the example , this applies to every
domain: visual, world, layout, pricing, distribution, trust, motion, safety.

Mechanism (two directions, both fuse doctrine into the function):
  load  , feeds the relevant certified doctrine INTO the moment of creation (proactive quality).
          Inject this into any generation prompt so the output is doctrine-correct at birth.
  check , gates an output against that doctrine AFTER (reactive quality). Deterministic checks where
          they exist + a model rubric always. Verdict PASS / FIX / REJECT, logged.

  os_doctrine.py domains
  os_doctrine.py load <domain>
  os_doctrine.py check <domain> --text "..."   |   --asset <path>   [--log LOG]
  os_doctrine.py audit <log>

Doctrine sources are the certified memory (intel_*/feedback_*) + the knowledge-base distilled docs.
"""
import os, sys, csv, time, json, argparse, re

MEM = "/Users/sniper/.claude/projects/-Users-sniper/memory"
KB = "/Users/sniper/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches"

# domain -> sources (real certified files) + rules (distilled, actionable) + how it gates
DOCTRINE = {
  "copy": {
    "sources": [f"{MEM}/intel_positioning_phrases.md", f"{MEM}/intel_wwp_proclamations.md",
                f"{KB}/ADVERTISING_RECOVERY_CHUNKS.jsonl", f"{KB}/PERSUASION_RECOVERY_CHUNKS.jsonl", f"{KB}/BRAND_CANON_CHUNKS.jsonl"],
    "rules": [
      "The headline is 80% of the spend (Ogilvy). It must be a complete thought, never a truncated fragment.",
      "One big idea per piece. Specific beats generic. Concrete noun beats abstract claim.",
      "Benefit and meaning, not feature lists or internal mechanics.",
      "Write in the world's voice, never in bible/spec language (no 'is faceless by design', no 'synthetic figure rendered as').",
      "No self-applied hype: world-class, seamless, unlock, elevate, leverage, game-changer, next-level, revolutionary.",
      "No em-dashes. Cut clean. Read it aloud; if it stops mid-thought, it fails.",
    ],
    "rubric": ["complete_thought", "one_big_idea", "in_world_voice_not_bible", "no_generic_hype", "specific_not_abstract", "no_em_dash"],
  },
  "visual_grade": {
    "sources": [f"{MEM}/feedback_visual_direction_luxury_editorial.md", f"{MEM}/intel_photo_theory.md", f"{MEM}/feedback_strongest_photograph_not_most_processed.md"],
    "rules": ["Quiet-luxury editorial restraint, Adobe-Neutral base, no teal/orange.",
              "One disciplined saturated color only; everything else neutral.",
              "The output must beat an honest camera frame, not merely complete the task.",
              "Restraint over volume. Processed-clean is not the same as alive."],
    "rubric": ["restraint_held", "one_color_discipline", "beats_the_source", "alive_not_inert"],
  },
  "world_character": {
    "sources": [f"{MEM}/feedback_lineage_doctrine.md", f"{MEM}/feedback_scene_density_thinking.md", f"{MEM}/intel_status_psychology.md", f"{KB}/STORYTELLING_NARRATIVE_CHUNKS.jsonl"],
    "rules": ["A five-second-drawable mark + one color law + faceless-safe.",
              "Cultural specificity from inside a lineage, never tourism.",
              "A reason to care beyond 'AI consistency works'; tension + stakes + a built-in arc.",
              "Status is signaled, not stated."],
    "rubric": ["ownable_mark", "culturally_specific", "has_tension_and_stakes", "faceless_safe"],
  },
  "layout_type": {
    "sources": [f"{MEM}/feedback_composite_environment_rotation.md", f"{MEM}/feedback_bw_card_dual_register.md"],
    "rules": ["Owned editorial kit (Didot/Baskerville), never a template look.",
              "Copy sits on dark / controlled ground, never illegible over a bright area.",
              "Intentional hierarchy: one masthead, one line, one mark. No filler slides.",
              "Negative space is deliberate (masthead headroom)."],
    "rubric": ["not_a_template", "legible_contrast", "intentional_hierarchy", "no_filler"],
  },
  "pricing_offer": {
    "sources": [f"{MEM}/intel_pricing_logic.md", f"{MEM}/intel_new_luxury.md", f"{MEM}/intel_status_psychology.md", f"{MEM}/intel_wwp_proclamations.md"],
    "rules": ["Price the value and the meaning, not the cost. Premium-as-insurance.",
              "Three-option architecture; anchor high.",
              "Scarcity + numbered editions for status goods.",
              "Payment follows proof; never crown a price before demand."],
    "rubric": ["values_not_cost", "scarcity_or_anchor", "proof_before_price"],
  },
  "distribution_hook": {
    "sources": [f"{MEM}/intel_hit_mechanics.md", f"{MEM}/intel_distribution_mechanics.md", f"{MEM}/intel_blockbuster_strategy.md", f"{KB}/NETWORK_DISTRIBUTION_CHUNKS.jsonl"],
    "rules": ["MAYA: advanced yet acceptable. A hook in the first beat.",
              "One repeatable signature format; clip-survival apparatus (re-attribution).",
              "Cluster spread before broadcast; concentrate firepower on few hero units."],
    "rubric": ["has_hook", "repeatable_format", "clip_survives_repost"],
  },
  "trust_sales": {
    "sources": [f"{MEM}/intel_trust_equation.md", f"{MEM}/intel_trust_mechanics.md", f"{MEM}/intel_hospitality_layer.md", f"{MEM}/feedback_hardest_to_say_no.md"],
    "rules": ["Trust = (credibility + reliability + intimacy) / self-orientation. Lower the divisor.",
              "Hospitality: deliver more than promised at the touchpoint.",
              "Make the artifact the hardest possible thing to say no to; study and beat the incumbent.",
              "No overclaim; proof beats assertion."],
    "rubric": ["low_self_orientation", "proof_not_claim", "hard_to_say_no"],
  },
  "motion": {
    "sources": [f"{MEM}/intel_photo_theory.md", f"{MEM}/feedback_bw_card_dual_register.md"],
    "rules": ["The made image, with intent in every frame.",
              "One shot is a teaser, not a trailer; a trailer needs cuts + rhythm.",
              "Caption-safe lower third; the one-color discipline must survive motion."],
    "rubric": ["intent_per_frame", "honest_teaser_vs_trailer", "color_discipline_in_motion"],
  },
  "safety_identity": {
    "sources": [f"{MEM}/feedback_possibility_engine_optionality.md", f"{MEM}/feedback_payment_follows_proof.md", f"{MEM}/feedback_capability_proof_bar.md"],
    "rules": ["No real identity, no employer overlap, no metadata leak, no public action without a go.",
              "Faceless-safe by default.",
              "Capability counts only with a proving artifact.",
              "Payment/structure follows proof; nothing irreversible without approval."],
    "rubric": ["no_identity_leak", "faceless_safe", "no_unapproved_public_action"],
  },
}

GENERIC_HYPE = ["world-class", "seamless", "unlock", "elevate", "leverage", "game-changer",
                "game changer", "next-level", "next level", "revolutionary", "cutting-edge",
                "best-in-class", "synergy", "disrupt", "how it sells", "is faceless by design",
                "synthetic figure rendered"]

def copy_checks(text):
    """Deterministic copy checks (the part that does not need a model)."""
    out = {}
    out["no_em_dash"] = "PASS" if "—" not in text else "FAIL"
    low = text.lower()
    hits = [h for h in GENERIC_HYPE if h in low]
    out["no_generic_hype"] = "PASS" if not hits else f"FAIL({hits})"
    out["no_bible_language"] = "PASS" if not any(p in low for p in ["is faceless by design", "synthetic figure rendered", "rendered only as", "color law:", "visual law:"]) else "FAIL"
    # fragment: a headline that ends without terminal punctuation AND on a weak word (verb/prep/article)
    weak_end = re.search(r"\b(the|a|an|of|to|in|on|with|and|or|stamps|files|that|which|as)\s*$", text.strip(), re.I)
    terminal = text.strip().endswith((".", "!", "?", '"'))
    out["complete_thought"] = "PASS" if (terminal or not weak_end) and len(text.split()) >= 2 else "FAIL(fragment)"
    out["length_ok"] = "PASS" if len(text) <= 140 else f"WARN(len {len(text)}; headline too long)"
    return out

def fix_copy(text):
    """Deterministic repair of mechanical copy failures. Returns (fixed_text, still_needs_rewrite, notes).
    Fixes what is safe to fix (em-dash, hype phrases, trailing whitespace). Flags what needs real
    writing taste (fragments, bible-language, over-length) so an agent rewrites it with the doctrine pack."""
    notes = []; t = text
    if "—" in t:
        t = t.replace(" — ", ", ").replace("—", ", "); notes.append("em-dash removed")
    low = t.lower()
    for h in GENERIC_HYPE:
        if h in low:
            # remove the hype phrase and tidy spacing/punctuation
            t = re.sub(re.escape(h), "", t, flags=re.I); notes.append(f"hype removed: '{h}'")
    t = re.sub(r"\s{2,}", " ", t).strip(" .,:;").strip()
    chk = copy_checks(t)
    needs_rewrite = any(str(v).startswith("FAIL") for k, v in chk.items() if k in ("complete_thought", "no_bible_language"))
    if needs_rewrite:
        notes.append("NEEDS REWRITE (fragment or bible-language) , inject the doctrine pack and regenerate")
    return t, needs_rewrite, notes

def gate_run(run_dir, domains_text, log=None):
    """Master doctrine gate for a whole run. domains_text = {domain: [texts]}.
    The OS calls this so every run is doctrine-gated as one thing. Returns verdict + per-domain results."""
    results = {}
    for domain, texts in domains_text.items():
        d = DOCTRINE.get(domain)
        if not d: continue
        items = []
        for tx in texts:
            if not tx: continue
            if domain == "copy":
                ch = copy_checks(tx)
                v = "PASS" if all(str(x).startswith("PASS") for x in ch.values()) else "FLAG"
            else:
                v = "MODEL_RUBRIC"  # the agent reads the asset and scores d["rubric"]
            items.append({"text": tx[:60], "verdict": v})
        results[domain] = items
    flagged = sum(1 for d, its in results.items() for it in its if it["verdict"] == "FLAG")
    verdict = "PASS" if flagged == 0 else "FLAG"
    if log:
        os.makedirs(os.path.dirname(log), exist_ok=True)
        new = not os.path.exists(log)
        with open(log, "a", newline="") as f:
            w = csv.writer(f)
            if new: w.writerow(["ts", "verdict", "flagged", "domains"])
            w.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), verdict, flagged, ";".join(results)])
    return verdict, results

def cmd_load(domain):
    d = DOCTRINE.get(domain)
    if not d: return f"unknown domain. domains: {', '.join(DOCTRINE)}"
    present = [s for s in d["sources"] if os.path.exists(s)]
    lines = [f"# DOCTRINE PACK , {domain}  (inject this into the generation prompt)",
             "## Rules (apply at the moment of creation)"]
    lines += [f"- {r}" for r in d["rules"]]
    lines.append("## Self-check before output (the gate will verify): " + ", ".join(d["rubric"]))
    lines.append(f"## Certified sources ({len(present)}/{len(d['sources'])} present): " + "; ".join(os.path.basename(s) for s in d["sources"]))
    return "\n".join(lines)

def cmd_check(domain, text, asset, log):
    d = DOCTRINE.get(domain)
    if not d: print(f"unknown domain: {domain}"); return 1
    det = {}
    if domain == "copy" and text is not None:
        det = copy_checks(text)
    hard_fail = any(str(v).startswith("FAIL") for v in det.values())
    verdict = "REJECT" if hard_fail else ("FIX" if domain != "copy" or not det else "PASS")
    # for non-deterministic domains, the model reads the asset/text and scores the rubric
    print(f"DOCTRINE CHECK , {domain}: {verdict if det else 'MODEL-RUBRIC'}")
    for k, v in det.items():
        print(f"  {'OK ' if str(v).startswith('PASS') else ('?? ' if str(v).startswith('WARN') else '!! ')}{k:22s} {v}")
    if not det or domain != "copy":
        print("  model reads the asset/text and scores each (PASS/FAIL):")
        for r in d["rubric"]: print(f"    {r}")
    if log:
        os.makedirs(os.path.dirname(log), exist_ok=True)
        new = not os.path.exists(log)
        with open(log, "a", newline="") as f:
            w = csv.writer(f)
            if new: w.writerow(["ts", "domain", "verdict", "checks", "subject"])
            w.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), domain, verdict, json.dumps(det), (text or asset or "")[:60]])
    return 0 if verdict in ("PASS",) else (1 if verdict == "REJECT" else 2)

def main():
    ap = argparse.ArgumentParser(prog="os_doctrine.py"); sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("domains")
    l = sub.add_parser("load"); l.add_argument("domain")
    c = sub.add_parser("check"); c.add_argument("domain"); c.add_argument("--text", default=None); c.add_argument("--asset", default=None); c.add_argument("--log", default="")
    fx = sub.add_parser("fix"); fx.add_argument("domain"); fx.add_argument("--text", required=True)
    a = ap.parse_args()
    if a.cmd == "domains":
        for k, v in DOCTRINE.items(): print(f"  {k:18s} <- {len(v['sources'])} sources, {len(v['rules'])} rules")
    elif a.cmd == "load":
        print(cmd_load(a.domain))
    elif a.cmd == "check":
        return cmd_check(a.domain, a.text, a.asset, a.log or None)
    elif a.cmd == "fix":
        if a.domain != "copy":
            print("fix is deterministic for copy only; other domains use load+regenerate"); return 2
        fixed, needs, notes = fix_copy(a.text)
        print(f"IN : {a.text}\nOUT: {fixed}\nneeds_rewrite: {needs}\nnotes: {'; '.join(notes) or 'none'}")
        return 1 if needs else 0
    else: ap.print_help()
    return 0

if __name__ == "__main__": sys.exit(main())
