#!/usr/bin/env python3
"""Write DECISION_JUDGMENT_MEANING_CHUNKS.jsonl · 9 curated chunks from the 2 net-new sources.
Existing domains only · decision-making anchor · no new domain. Em-dash swept + asserted.
Frankl held with dignity (NOT hustle/motivation); Berne held as interpersonal-pattern awareness (NOT diagnosis/labeling)."""
import json, os

ROOT = "/Users/sniper/AI-Brain-Refinery"
OUT = os.path.join(ROOT, "01_KNOWLEDGE_BASE/batches/DECISION_JUDGMENT_MEANING_CHUNKS.jsonl")
EXTRACT = "01_KNOWLEDGE_BASE/batches/decision_judgment_meaning_extracted"
DASH = chr(0x2014)
BATCH = "DECISION_JUDGMENT_MEANING"

FRANKL = ("Man's Search for Meaning", "Viktor E. Frankl", "mans_search_for_meaning_frankl.txt")
BERNE = ("Games People Play", "Eric Berne", "games_people_play_berne.txt")

GUARD = (
    " Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support / pattern-library only, "
    "NOT doctrine and NOT a directive. NOT a directive that BJ become a therapist, a psychologist, a self-help teacher, "
    "a religious or spiritual guide, an existential writer, a trauma commentator, or a diagnosis-brand operator. "
    "Frankl's material is held with dignity and care, NOT reduced to hustle or motivation content; Berne's games material "
    "is held as interpersonal-pattern awareness, NOT armchair diagnosis or a tool for labeling people. The methods are "
    "translated into practical agency, meaning-anchoring, and interaction-pattern awareness for BJ's actual build-mode stage. "
    "No final SNIPED, SNIPED Media, or BASEPLATE direction; photography remains one option among several. "
    "The Bible remains held separately and untouched."
)

def C(n, src, domain, concept, summary, principle, relevance, quotes, tags):
    st, au, sf = src
    return {
        "chunk_id": f"{BATCH}_{n:03d}",
        "batch_id": BATCH,
        "source_title": st,
        "source_file": sf,
        "author": au,
        "domain": domain,
        "concept": concept,
        "summary": summary,
        "usable_principle": principle,
        "sniped_relevance": relevance + GUARD,
        "direct_quotes": quotes,
        "tags": tags,
    }

rows = [
    # ---- Man's Search for Meaning (Frankl) · 4 + synthesis ----
    C(1, FRANKL, "decision-making",
      "The last of the human freedoms: the choice of one's response",
      "Frankl, writing from his survival of the camps, observes that everything can be taken from a person but one thing: the freedom to choose one's attitude and response in any given set of circumstances. Between what happens to you and what you do, even under extreme constraint, a space of choice remains. This is offered soberly, grounded in profound suffering, not as a slogan.",
      "Locate the small space of chosen response between circumstance and reaction; even when conditions cannot be changed, the stance you take toward them can.",
      "For BJ this is a sober reminder that in hard, uncontrollable stretches of the build, the controllable variable is his chosen response and attitude, held with the seriousness Frankl earned, not as motivational gloss.",
      ["the last of the", "to choose one's attitude"],
      ["decision-judgment-meaning", "mans-search-for-meaning", "frankl", "agency", "attitude", "response-under-constraint"]),
    C(2, FRANKL, "operator-doctrine",
      "A why to live: meaning as the thing that sustains the how",
      "Frankl repeats Nietzsche's line that one who has a why to live can bear almost any how, and builds logotherapy on the will to meaning as the primary human drive. Those in the camps who held a reason to live (a person to return to, a work to finish) endured what others could not. Meaning is the load-bearing structure beneath endurance, not a luxury.",
      "Anchor sustained effort in a concrete why (a person, a work, a purpose); the clearer the why, the more difficult a how you can bear.",
      "Helps BJ understand that durable effort in build-mode rests on a real, specific reason rather than willpower alone, while holding the source (Frankl's survival) with care and not flattening it into hustle.",
      ["a why to live", "the will to meaning"],
      ["decision-judgment-meaning", "mans-search-for-meaning", "frankl", "purpose", "why-to-live", "endurance"]),
    C(3, FRANKL, "ethics",
      "Meaning in unavoidable suffering: when the situation cannot be changed",
      "Logotherapy holds that meaning can be found three ways: through work or deeds, through love or encounter, and through the attitude taken toward unavoidable suffering. When a situation truly cannot be changed, the task shifts to how one bears it; in Frankl's words, suffering ceases in some sense to be suffering at the moment it finds a meaning. This is handled with dignity, not as a productivity trick.",
      "Distinguish what can be changed from what must be borne; for the unchangeable, the work is the meaning and dignity you bring to bearing it.",
      "Gives BJ a sober frame for genuinely unchangeable hardship (loss, constraint, setback): the response is meaning and dignity in how it is borne, explicitly NOT a hustle reframe of real pain.",
      ["unavoidable suffering", "finds a meaning"],
      ["decision-judgment-meaning", "mans-search-for-meaning", "frankl", "suffering", "meaning-sources", "dignity"]),
    C(4, FRANKL, "decision-making",
      "Self-transcendence and tragic optimism: meaning is found, not chased",
      "Frankl argues meaning comes from self-transcendence (reaching toward something or someone beyond oneself), and that happiness cannot be pursued directly; it ensues as a side effect of devotion to a cause or person. His tragic optimism is the capacity to say yes to life in spite of the tragic triad of pain, guilt, and death, by finding meaning within them.",
      "Aim at a cause or person beyond yourself and let fulfillment ensue; chasing happiness or success directly tends to make it recede.",
      "Reminds BJ that orienting toward real work and people (not toward the feeling of success itself) is what produces meaning and, indirectly, satisfaction, an orientation for the build that resists empty metric-chasing.",
      ["tragic optimism", "self-transcendence"],
      ["decision-judgment-meaning", "mans-search-for-meaning", "frankl", "self-transcendence", "tragic-optimism", "meaning-found-not-chased"]),
    # ---- Games People Play (Berne) · 4 ----
    C(5, BERNE, "operator-process",
      "Ego states: Parent, Adult, Child",
      "Berne's transactional analysis models each person as shifting among three ego states: the Parent (taught, authority/care patterns absorbed from elders), the Child (felt, the spontaneous or adapted reactions from early life), and the Adult (the here-and-now rational processor of reality). Communication happens between specific states, and the Adult is the state that assesses the actual situation.",
      "Notice which ego state (Parent, Adult, Child) you and the other person are speaking from; deliberately engage the Adult when a clear-headed read is needed.",
      "Gives BJ a lens to catch when a tense exchange (with a client, collaborator, himself) is being driven by a reactive Child or scolding Parent state rather than the Adult, useful for staying level, not for labeling anyone.",
      ["ego state", "Parent", "Adult", "Child"],
      ["decision-judgment-meaning", "games-people-play", "berne", "ego-states", "transactional-analysis", "self-awareness"]),
    C(6, BERNE, "operator-process",
      "Transactions, strokes, and the structuring of time",
      "Social life, in Berne's account, is an exchange of transactions, and people hunger for strokes (units of recognition). To get them, people structure time through rituals, pastimes, activities, games, and intimacy. A transaction is complementary (smooth) when the response comes from the addressed state, and crossed (friction) when it does not.",
      "Read interactions as exchanges of recognition; when a conversation snags, check whether the reply crossed the state you addressed.",
      "Helps BJ see why some exchanges flow and others jar (a crossed transaction), and that people, including collaborators, are partly seeking recognition, useful for designing honest interaction, not for manipulating it.",
      ["strokes", "pastimes"],
      ["decision-judgment-meaning", "games-people-play", "berne", "transactions", "recognition", "interaction-patterns"]),
    C(7, BERNE, "decision-making",
      "Games and ulterior transactions: the hidden payoff",
      "A Berne game is a recurring series of transactions with a concealed (ulterior) motive that leads to a predictable payoff, usually a familiar bad feeling or a confirmed position. Games run below awareness and repeat. Recognizing the pattern (the repeated sequence and the payoff it pays out) is what lets a person decline to play, on either side.",
      "When an interaction keeps reaching the same sour predictable ending, suspect a game with a hidden payoff and name the pattern to yourself so you can opt out.",
      "Lets BJ recognize repeating no-win interaction loops (with himself or others) by their predictable payoff and step out of them, strictly as pattern-awareness, NOT as a way to diagnose or label other people.",
      ["ulterior transaction", "payoff"],
      ["decision-judgment-meaning", "games-people-play", "berne", "games", "ulterior-motive", "pattern-recognition"]),
    C(8, BERNE, "culture",
      "Stepping out: the antithesis and the pull of repeated patterns",
      "Berne notes that every game has an antithesis: a move that refuses the expected next step and breaks the sequence. Games persist because they are learned, socially reinforced, and pay a familiar payoff, so breaking one can be uncomfortable and is often resisted. Awareness, spontaneity, and honest contact are the alternative to a life of games.",
      "To break a recurring game, decline the expected move (the antithesis) and tolerate the discomfort; default social scripts reassert unless consciously interrupted.",
      "For BJ, a pattern for refusing to be drawn into a familiar unproductive dynamic by simply not playing the expected role, and for building relationships on honest contact rather than scripted games, held as awareness not as labeling.",
      ["antithesis", "games"],
      ["decision-judgment-meaning", "games-people-play", "berne", "antithesis", "breaking-patterns", "honest-contact"]),
    # ---- Synthesis ----
    C(9, FRANKL, "operator-doctrine",
      "Synthesis: meaning, agency, and interpersonal-pattern awareness",
      "Across the two sources a single decision-support toolkit emerges: the freedom to choose one's response remains even under constraint, and durable effort rests on a concrete why and on meaning found through work, love, and the dignified bearing of what cannot be changed (Frankl); and social life runs on ego states, recognition, and recurring games whose hidden payoffs can be recognized and declined (Berne). Held as decision-support, these are read as agency, meaning-anchoring, and interaction-pattern awareness for the operator, NOT as therapy, religion, self-help, or a license to diagnose people.",
      "Choose your response, anchor effort in a real why, find meaning in work and the dignified bearing of the unchangeable, and read ego states and recurring games so you can engage from the Adult and opt out of no-win patterns.",
      "A single decision-support lens for BJ's agency and interpersonal awareness that explicitly preserves optionality and dignity: apply what steadies and clarifies, treat the sources with care, diagnose no one, finalize nothing.",
      ["a why to live", "the last of the"],
      ["decision-judgment-meaning", "synthesis", "meaning-and-agency", "interpersonal-patterns", "optionality", "operator-doctrine"]),
]

def sweep(o):
    if isinstance(o, str): return o.replace(DASH, " · ")
    if isinstance(o, list): return [sweep(x) for x in o]
    if isinstance(o, dict): return {k: sweep(v) for k, v in o.items()}
    return o

rows = [sweep(r) for r in rows]

assert len(rows) == 9, len(rows)
ids = [r["chunk_id"] for r in rows]
assert len(ids) == len(set(ids)), "dup chunk_id"
REQ = ["chunk_id","batch_id","source_title","source_file","author","domain","concept","summary","usable_principle","sniped_relevance","direct_quotes","tags"]
for r in rows:
    for k in REQ:
        assert k in r and r[k] not in (None, "", []), (r["chunk_id"], k)
    assert r["batch_id"] == BATCH
    blob = json.dumps(r, ensure_ascii=False)
    assert DASH not in blob, ("em-dash", r["chunk_id"])
    for q in r["direct_quotes"]:
        assert len(q.split()) <= 6, ("quote too long", r["chunk_id"], q)
    assert os.path.isfile(os.path.join(ROOT, EXTRACT, r["source_file"])), r["source_file"]
    assert "NOT a directive" in r["sniped_relevance"] and "CURRENT_OPERATOR_REALITY_BRIEF" in r["sniped_relevance"]

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

from collections import Counter
print(f"wrote {len(rows)} chunks -> {OUT}")
print("domains:", dict(Counter(r["domain"] for r in rows)))
print("sources:", dict(Counter(r["source_title"] for r in rows)))
print("longest quote words:", max(len(q.split()) for r in rows for q in r["direct_quotes"]))
