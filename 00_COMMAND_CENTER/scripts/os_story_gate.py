#!/usr/bin/env python3
"""
os_story_gate.py - the STORY + PSYCHOLOGY + COMMERCIAL NARRATIVE operating layer.
Cards live in story_psychology_layer/STORY_INTELLIGENCE_CARDS.json (one body of intelligence).
The 8 libraries are VIEWS over that store, not separate piles.

Usage:
  os_story_gate.py libraries                # the 8 libraries + card counts
  os_story_gate.py load <project_type>      # which card-libraries auto-load before building
  os_story_gate.py gate                     # the STORY GATE proof checklist
  os_story_gate.py ask "<prompt>"           # resolve a prompt -> card+source+library+gate+application+next action
  os_story_gate.py cards [library]          # list cards (optionally filtered to a library)
"""
import json, os, sys, re

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(HERE, "..", "story_psychology_layer", "STORY_INTELLIGENCE_CARDS.json")

LIBRARIES = [
    "STORYTELLING_OPERATOR_LIBRARY", "PSYCHOLOGY_OPERATOR_LIBRARY",
    "COMMERCIAL_NARRATIVE_LIBRARY", "ATTENTION_HOOK_LIBRARY",
    "CHARACTER_AND_WORLD_LIBRARY", "BUYER_DESIRE_LIBRARY",
    "CAPTION_AND_COPY_LIBRARY", "VISUAL_STORY_EDITING_LIBRARY",
]

# which libraries (plus commercial-craft) auto-load per project type
ROUTES = {
    "video_campaign":   LIBRARIES + ["COMMERCIAL_CRAFT_LIBRARY"],
    "social_rollout":   ["STORYTELLING_OPERATOR_LIBRARY","ATTENTION_HOOK_LIBRARY","CAPTION_AND_COPY_LIBRARY","BUYER_DESIRE_LIBRARY","COMMERCIAL_NARRATIVE_LIBRARY","COMMERCIAL_CRAFT_LIBRARY"],
    "photo_post":       ["VISUAL_STORY_EDITING_LIBRARY","CHARACTER_AND_WORLD_LIBRARY","BUYER_DESIRE_LIBRARY","CAPTION_AND_COPY_LIBRARY"],
    "still_range":      ["VISUAL_STORY_EDITING_LIBRARY","CHARACTER_AND_WORLD_LIBRARY","BUYER_DESIRE_LIBRARY"],
    "brand_ip_system":  ["CHARACTER_AND_WORLD_LIBRARY","COMMERCIAL_NARRATIVE_LIBRARY","BUYER_DESIRE_LIBRARY","PSYCHOLOGY_OPERATOR_LIBRARY","CAPTION_AND_COPY_LIBRARY"],
    "offer":            ["BUYER_DESIRE_LIBRARY","PSYCHOLOGY_OPERATOR_LIBRARY","COMMERCIAL_NARRATIVE_LIBRARY","CAPTION_AND_COPY_LIBRARY"],
    "client_package":   LIBRARIES + ["COMMERCIAL_CRAFT_LIBRARY"],
    "deck":             ["STORYTELLING_OPERATOR_LIBRARY","BUYER_DESIRE_LIBRARY","PSYCHOLOGY_OPERATOR_LIBRARY","CAPTION_AND_COPY_LIBRARY"],
}

GATE_QUESTIONS = [
    "STORY TENSION: what tension/conflict drives this? (open loop)",
    "FEELING: what is the viewer supposed to FEEL (esp. first 3s)?",
    "DESIRE/STATUS: what desire or status signal is activated?",
    "HOOK: what is the hook and what loop does it open?",
    "PAYOFF: what is the payoff and where does the loop close?",
    "CHARACTER/WORLD: what character + world logic is present and consistent?",
    "WITHHOLD/REVEAL: what is withheld, what is revealed, in what order?",
    "SEQUENCE LOGIC: why THIS beat before THAT beat? (but/therefore, never and-then)",
    "SOURCE CARDS: which story/psychology cards + sources were used?",
]

def load():
    with open(STORE) as f:
        return json.load(f)["cards"]

def cmd_libraries():
    cards = load()
    print("STORY + PSYCHOLOGY OPERATING LAYER - 8 libraries (views over %d cards):\n" % len(cards))
    for lib in LIBRARIES:
        ids = [c["id"] for c in cards if lib in c.get("libraries", [])]
        print("  %-34s %d cards: %s" % (lib, len(ids), ", ".join(ids)))

def cmd_load(ptype):
    libs = ROUTES.get(ptype)
    if not libs:
        print("unknown project_type '%s'. known: %s" % (ptype, ", ".join(ROUTES))); return
    cards = load()
    print("AUTO-LOAD for project_type: %s\n" % ptype)
    print("libraries:", ", ".join(libs), "\n")
    used = set()
    for lib in libs:
        for c in cards:
            if lib in c.get("libraries", []): used.add(c["id"])
    print("cards that apply (%d):" % len(used))
    for c in cards:
        if c["id"] in used:
            print("  [%s] %s" % (c["id"], c["title"]))
    print("\nRULE: STORY_GATE must pass before this build is called strong (os_story_gate.py gate).")

def cmd_gate():
    print("=== STORY GATE - a commercial edit/deck/caption/campaign is not 'strong' until it answers all: ===\n")
    for i, q in enumerate(GATE_QUESTIONS, 1):
        print("  [ ] %d. %s" % (i, q))
    print("\nIf any answer is missing -> NOT STRONG. Cite the source cards used (os_story_gate.py cards).")

def cmd_cards(lib=None):
    cards = load()
    for c in cards:
        if lib and lib not in c.get("libraries", []): continue
        print("[%s] %s" % (c["id"], c["title"]))
        print("    source: %s" % c["source"])

def cmd_ask(prompt):
    cards = load()
    p = prompt.lower()
    # keyword -> card scoring
    scored = []
    for c in cards:
        hay = " ".join([c["title"], c["problem"], c["when_to_use"], c["story_principle"],
                        c["psychology_principle"], c["application"], c["bad_output_prevented"],
                        " ".join(c.get("libraries", []))]).lower()
        score = 0
        for w in re.findall(r"[a-z]{4,}", p):
            if w in hay: score += 1
        # intent boosts
        if "montage" in p or "story" in p or "random" in p: score += (3 if c["id"] in ("story_but_therefore","story_emotional_target") else 0)
        if "hook" in p or "first 3" in p or "3 second" in p: score += (3 if c["id"] in ("story_open_loop_hook","story_emotional_target") else 0)
        if "payoff" in p or "ending" in p: score += (3 if c["id"]=="story_loop_closed_ending" else 0)
        if "brand story" in p or "no point" in p or "missing" in p: score += (2 if c["id"] in ("char_flawed_protagonist","story_emotional_target") else 0)
        if "expensive" in p or "memorable" in p or "status" in p: score += (3 if c["id"] in ("psy_status_new_luxury","story_mechanics_distribution") else 0)
        if "caption" in p or "copy" in p: score += (2 if "CAPTION_AND_COPY_LIBRARY" in c.get("libraries",[]) else 0)
        if "buy again" in p or "buy" in p or "client" in p: score += (3 if c["id"]=="psy_repeatable_buyer" else 0)
        if "book" in p or "framework" in p: score += 1
        if "before that" in p or "why this shot" in p or "order" in p: score += (3 if c["id"]=="story_but_therefore" else 0)
        if "ai edit" in p or "more than" in p or "random ai" in p: score += (2 if c["id"] in ("char_flawed_protagonist","story_but_therefore","story_emotional_target") else 0)
        if score: scored.append((score, c))
    scored.sort(key=lambda x: -x[0])
    if not scored:
        print("No card matched. Add a card or rephrase."); return
    print("PROMPT: %s\n" % prompt)
    for score, c in scored[:3]:
        print("CARD:        [%s] %s" % (c["id"], c["title"]))
        print("SOURCE:      %s" % c["source"])
        print("LIBRARY:     %s" % ", ".join(c.get("libraries", [])))
        print("GATE:        %s" % c["gate"])
        print("APPLICATION: %s" % c["application"])
        print("NEXT ACTION: apply '%s' -> %s" % (c["title"], c["alma_example"]))
        print()

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(0)
    cmd = a[0]
    if cmd == "libraries": cmd_libraries()
    elif cmd == "load" and len(a) > 1: cmd_load(a[1])
    elif cmd == "gate": cmd_gate()
    elif cmd == "cards": cmd_cards(a[1] if len(a) > 1 else None)
    elif cmd == "ask" and len(a) > 1: cmd_ask(" ".join(a[1:]))
    else: print(__doc__)
