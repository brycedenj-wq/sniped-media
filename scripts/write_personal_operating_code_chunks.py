#!/usr/bin/env python3
"""
PERSONAL_OPERATING_CODE chunker · The 88 Laws Of The Masculine Mindset (John Winters)

Reads 01_KNOWLEDGE_BASE/batches/personal_operating_code_extracted/88_laws_winters.txt and
emits PERSONAL_OPERATING_CODE_CHUNKS.jsonl with the canonical 12-field schema.

Target: 9 chunks (range 7-10 per plan §4 · content density supports 9).
Domains per plan §5: 7 operator-doctrine + 2 operator-process (no NEW domain).

INCLUDE/EXCLUDE discipline per plan §10 + operator brief:
  INCLUDE: ownership, discipline, mission, code, time control, consistency,
           execution, composure, resourcefulness, self-audit, mindset-as-software.
  EXCLUDE (NOT chunked): Law 18 (Fitness/Health), Law 33 (Meat/Diet), Law 61
           (Testosterone), and the gender-war / dating / body-image framing
           throughout. The 88-law source uses a masculine-mindset rhetorical
           register; this chunker extracts ONLY the gender-neutral operator-doctrine
           substrate and reframes it for the SNIPED operating system.

Em-dash sweep (Unicode U+2014) applied to output.
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
EXTRACTED = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "personal_operating_code_extracted"
OUT_JSONL = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "PERSONAL_OPERATING_CODE_CHUNKS.jsonl"

BATCH_ID = "PERSONAL_OPERATING_CODE"
AUTHOR = "John Winters"
SOURCE_TITLE = "The 88 Laws Of The Masculine Mindset · John Winters"
SOURCE_FILE = "88_laws_winters.txt"

chunks = []


def add_chunk(num, domain, concept, summary, usable_principle, sniped_relevance, direct_quotes, tags):
    chunks.append({
        "chunk_id": f"{BATCH_ID}_{num:03d}",
        "batch_id": BATCH_ID,
        "source_title": SOURCE_TITLE,
        "source_file": SOURCE_FILE,
        "author": AUTHOR,
        "domain": domain,
        "concept": concept,
        "summary": summary,
        "usable_principle": usable_principle,
        "sniped_relevance": sniped_relevance,
        "direct_quotes": direct_quotes,
        "tags": tags,
    })


# ---------------------------------------------------------------------------
# Chunk 1 · Ownership (Laws 1, 2, 10, 35, 87)
# ---------------------------------------------------------------------------
add_chunk(
    num=1,
    domain="operator-doctrine",
    concept="Ownership · radical self-responsibility as the first operating axiom",
    summary=(
        "Winters opens with the ownership axiom (Law 1): take full responsibility for everything in "
        "your life, good and bad. Even what is not your fault is still your responsibility, because "
        "responsibility is where control lives. The complement (Law 10) is the refusal to complain · "
        "complaint is the surrender of agency. Law 35 (you are entitled to nothing) and Law 87 "
        "(understand cause and effect) close the loop: the operator owns the inputs and accepts "
        "the outputs. Blame-shifting to external events or other people is the default failure mode "
        "the axiom is designed to override."
    ),
    usable_principle=(
        "Own everything · even what is not your fault is your responsibility, because responsibility "
        "is where control lives. Refuse to complain; complaint surrenders agency. Expect no "
        "entitlement; trace cause to effect. The operator owns the inputs and accepts the outputs."
    ),
    sniped_relevance=(
        "Prescriptive primary-source backing for the SNIPED operator-coded identity claim (B7 "
        "THE_OPERATOR_CODED_DEFINITION + un-delegate-ables ledger). The radical-responsibility axiom "
        "is the operationalized form of the un-delegate-ables: the operator owns methodology, final "
        "review, pricing, named-subject relationships · no blame-shift, no delegation of the load-bearing work."
    ),
    direct_quotes=[
        "Even if something is not your fault it's still your responsibility.",
        "Take control of your thoughts, your actions, and your physical reality. When you make this shift one very important thing happens. You are now in control.",
    ],
    tags=[
        "88-laws", "winters", "personal-operating-code", "operator-doctrine",
        "ownership", "radical-responsibility", "internal-locus-of-control", "operator-axiom",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 2 · Discipline (Laws 37, 13, 63)
# ---------------------------------------------------------------------------
add_chunk(
    num=2,
    domain="operator-doctrine",
    concept="Discipline · self-discipline as the default state, not the occasional effort",
    summary=(
        "Winters frames self-discipline (Law 37) as the foundational operating condition, not a "
        "willpower event. Law 13 (you are never on vacation) extends discipline into a permanent "
        "state · the operator does not clock out of their standards. Law 63 (the small things "
        "define you) locates discipline in the micro-decisions, not the grand gestures. Discipline "
        "is the compounding of small correct choices made when no one is watching."
    ),
    usable_principle=(
        "Treat self-discipline as the default state, not an occasional willpower spend. Never fully "
        "clock out of your standards. The small things define the operator · discipline lives in the "
        "micro-decisions made when no one is watching, not the grand gestures."
    ),
    sniped_relevance=(
        "Prescriptive complement to INTELLECTUAL_ARTIST_FRAME_001 (MJ rehearsal-as-default · "
        "descriptive). Backs the SNIPED Saturday-build + Sunday-rest + Monday-cockpit cadence (B7 "
        "recurring_checklists + MONDAY_COCKPIT) and feedback_repetition_over_novelty (LOCKED "
        "2026-05-12 · architecture is built, reps are the next 90 days)."
    ),
    direct_quotes=[
        "Self Discipline Should Be your default state.",
        "The Small Things Define You.",
    ],
    tags=[
        "88-laws", "winters", "personal-operating-code", "operator-doctrine",
        "discipline", "daily-rep-cadence", "non-negotiable-conditions", "rehearsal-as-default",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 3 · Mission obsession (Laws 22, 21, 49, 3, 20)
# ---------------------------------------------------------------------------
add_chunk(
    num=3,
    domain="operator-doctrine",
    concept="Mission obsession · single-thread focus · the mission is priority 1, everything else is priority 2",
    summary=(
        "Winters prescribes obsession with the mission (Law 22) as the organizing principle. Law 20 "
        "operationalizes it: allocate 90% of your time to the mission · the mission is always "
        "number one, everything else is number two. Law 21 (be rational and focused) and Law 49 "
        "(where focus goes, energy flows) reinforce the single-thread discipline. Law 3 (become the "
        "hero of your own story) frames the mission as a narrative the operator authors, not a job "
        "they accept."
    ),
    usable_principle=(
        "Make the mission priority 1; everything else is priority 2. Allocate ~90% of time to the "
        "mission. Where focus goes, energy flows · protect the single thread. Author the mission as "
        "your story rather than accepting an externally-assigned job."
    ),
    sniped_relevance=(
        "Backs the SNIPED single-thread discipline · B7 MONDAY_COCKPIT one-thing-that-must-happen "
        "filter + B4 100Q 2026 win conditions + B2 Bryar/Carr single-threaded leadership. The 90%-on-"
        "mission allocation is the prescriptive form of the SNIPED Year-10 reverse-roadmap focus + "
        "project_sniped_meta_thesis (photography is the 2026 moat · run the proof, do not generalize prematurely)."
    ),
    direct_quotes=[
        "Make your mission in life your number 1 priority, everything else must be number 2.",
        "Allocate your time so that your mission is 90% of your time.",
    ],
    tags=[
        "88-laws", "winters", "personal-operating-code", "operator-doctrine",
        "mission-obsession", "single-thread-focus", "90-percent-on-mission", "one-thing-that-matters",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 4 · Code (Laws 29, 68, 88)
# ---------------------------------------------------------------------------
add_chunk(
    num=4,
    domain="operator-doctrine",
    concept="Code · a self-imposed constitution of principles that should never be broken",
    summary=(
        "Winters prescribes living by a code (Law 29): a personal constitution, a set of principles "
        "that should never be broken. The code can be inspired by religion, philosophy, or assembled "
        "from multiple sources and experiences · the source is the operator's choice, but the "
        "existence of a code is non-negotiable. Without a code, the stream of life carries you "
        "wherever it flows. Law 68 (be guided by principles) and Law 88 (choose to be a warrior) "
        "frame the code as a chosen identity, not an inherited one."
    ),
    usable_principle=(
        "Build a personal constitution · a set of principles that should never be broken. Assemble "
        "it deliberately from chosen sources. Without a code, the stream of life carries you. The "
        "code is a chosen identity, not an inherited default."
    ),
    sniped_relevance=(
        "Structural backing for the SNIPED CANONICAL_TRUTHS (B7 · 12 truths that override on conflict) "
        "+ OPERATING_LOCKS (B7 · 10 locked decisions). The pattern Winters prescribes (self-imposed "
        "rules that override drift) is exactly the SNIPED canonical-truth frame · the 12 truths ARE "
        "the operator's constitution. Pairs with B6 sniped-canonical-truths skill."
    ),
    direct_quotes=[
        "You basically need a constitution for your own life, a set of principles. These principles should never be broken.",
        "Most people in the world walk around without a code or set of guidelines that could steer them through life. So the stream of life just takes them and they go with the flow.",
    ],
    tags=[
        "88-laws", "winters", "personal-operating-code", "operator-doctrine",
        "code", "self-imposed-rules", "rules-as-identity", "canonical-truths-pattern", "personal-constitution",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 5 · Time control (Laws 20, 12, 17) · operator-process
# ---------------------------------------------------------------------------
add_chunk(
    num=5,
    domain="operator-process",
    concept="Time control · time as the greatest commodity · audit it, allocate it, protect it",
    summary=(
        "Winters frames time as the greatest commodity (Law 20): once gone, you never get it back. "
        "The prescription is an explicit time audit · look back over the previous 4 weeks and account "
        "for where time went. Law 12 (become selfish with your time) is the protection discipline · "
        "guard time against low-value claims. Law 17 (sacrifice short-term for long-term) is the "
        "allocation discipline · spend time against compounding outcomes, not immediate comfort."
    ),
    usable_principle=(
        "Audit your last 4 weeks to see where time actually went. Guard time selfishly against "
        "low-value claims. Allocate against compounding long-term outcomes, not short-term comfort. "
        "Time is the one commodity you never get back."
    ),
    sniped_relevance=(
        "Operator-process backing for the SNIPED time-budget cadence · B7 MONDAY_COCKPIT (one-thing-"
        "that-must-happen) + SATURDAY_BUILD_BRIEF (protected build day) + recurring_checklists "
        "(Sunday rest). The 4-week time audit is the prescriptive form of the SNIPED monthly_constraint_"
        "audit + weekly_review templates (B7). The 90%-on-mission allocation (chunk 3) is the time-"
        "control discipline applied."
    ),
    direct_quotes=[
        "Time is our greatest commodity. Once it's gone, you never get it back.",
        "Go sit down and look back over your previous 4 weeks.",
    ],
    tags=[
        "88-laws", "winters", "personal-operating-code", "operator-process",
        "time-control", "time-as-currency", "4-week-time-audit", "time-as-finite-asset",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 6 · Consistency (Laws 55, 40, 41, 73, 17)
# ---------------------------------------------------------------------------
add_chunk(
    num=6,
    domain="operator-doctrine",
    concept="Consistency · the compound-arc thesis · it's not one thing, it's the accumulation",
    summary=(
        "Winters prescribes consistency (Law 55) as the multiplier. Law 40 (it's not one thing, "
        "it's everything · the accumulation) is the compound-arc thesis · greatness is the sum of "
        "consistent small inputs, not a single breakthrough. Law 41 (learn patience) and Law 73 "
        "(build momentum) frame the time dimension · consistency compounds into momentum, momentum "
        "compounds into outcomes. Law 17 (sacrifice short-term for long-term) is the trade that "
        "makes consistency possible."
    ),
    usable_principle=(
        "Consistency is the multiplier · it's not one thing, it's the accumulation. Build momentum "
        "through patient repetition. Sacrifice short-term comfort for the long-term compound arc. "
        "Greatness is the sum of consistent small inputs, not a single breakthrough."
    ),
    sniped_relevance=(
        "Prescriptive backing for the SNIPED perennial-seller logic (B3 Holiday · build for the "
        "long-tail) + feedback_repetition_over_novelty (LOCKED 2026-05-12) + INTELLECTUAL_ARTIST_FRAME_006 "
        "(MJ depth-over-churn · descriptive). The compound-arc thesis maps directly to the SNIPED "
        "Year-10 reverse-roadmap + the perennial-seller positioning (B7 SYSTEM_FINAL_STATUS Year-10 destination)."
    ),
    direct_quotes=[
        "Become Consistent.",
        "It's Not One Thing, Its everything.",
    ],
    tags=[
        "88-laws", "winters", "personal-operating-code", "operator-doctrine",
        "consistency", "compound-arc", "build-momentum", "long-game-thesis", "patience",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 7 · Execution (Laws 53, 31, 67, 78, 83)
# ---------------------------------------------------------------------------
add_chunk(
    num=7,
    domain="operator-doctrine",
    concept="Execution · ship over plan · boldly-executed beats perfectly-planned",
    summary=(
        "Winters prescribes execution over deliberation (Law 53): any plan boldly executed beats "
        "inaction · nothing happens until someone moves. 500 great ideas are useless until "
        "implemented · the people who had the Tinder/Facebook/Uber idea but did not act got nothing. "
        "Law 31 (who dares wins), Law 67 (actions speak louder than words), Law 78 (never quit), and "
        "Law 83 (go on the offense) reinforce the bias-to-action register · the operator is judged "
        "on what ships, not on what is conceived."
    ),
    usable_principle=(
        "Ship over plan · a boldly-executed imperfect plan beats a perfect plan that never moves. "
        "Ideas are worthless until implemented. Bias to action; go on the offense; never quit. The "
        "operator is judged on output, not on conception."
    ),
    sniped_relevance=(
        "Prescriptive backing for B4 Lock 10 (architecture is correct · execution is the only "
        "frontier · architecture refinement banned) + B7 LEAN_EXECUTION_AUDIT (named-recommendation "
        "queue · ship-this-week) + feedback_max_default (every task ships max depth by default). "
        "The 'ideas are worthless until implemented' frame is the prescriptive form of the SNIPED "
        "repetition-over-novelty discipline."
    ),
    direct_quotes=[
        "Any plan no matter how poorly conceived, boldly executed is better than inaction.",
        "You can have 500 great ideas but they will all be useless until they get implemented and turned into reality.",
    ],
    tags=[
        "88-laws", "winters", "personal-operating-code", "operator-doctrine",
        "execution", "ship-over-plan", "bias-to-action", "lock-10-companion", "never-quit",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 8 · Composure (Laws 15, 30, 81, 19, 52) · operator-process
# ---------------------------------------------------------------------------
add_chunk(
    num=8,
    domain="operator-process",
    concept="Composure · master your emotions · become water · the un-shaken operating state",
    summary=(
        "Winters prescribes emotional mastery (Law 15) as a precondition for clear operating. Law 30 "
        "(become water · the Bruce Lee adaptability frame) is the flexibility discipline · the "
        "composed operator adapts to the container without losing form. Law 81 (maintain your "
        "composure) names the state directly. Law 19 (humor in the face of adversity) and Law 52 "
        "(suffering is your teacher) reframe pressure as input rather than threat. Composure is the "
        "regulated state from which good decisions are made."
    ),
    usable_principle=(
        "Master your emotions before you operate · the regulated state is the precondition for clear "
        "decisions. Become water · adapt to the container without losing form. Maintain composure "
        "under pressure; reframe suffering as a teacher and adversity as input, not threat."
    ),
    sniped_relevance=(
        "Operator-process backing for the SNIPED hospitality layer (B3 Guidara · the composed host) "
        "+ INTELLECTUAL_ARTIST_FRAME_004 (MJ no-off-night discipline · performing composed even when "
        "sick). Composure under client-pressure + shoot-day-pressure is the un-delegate-able operator "
        "state · pairs with B7 SOP_capture_to_delivery SLA-risk notification discipline (stay composed, "
        "notify within 24 hours, commit to the new locked date)."
    ),
    direct_quotes=[
        "Maintain Your Composure.",
        "Become Water.",
    ],
    tags=[
        "88-laws", "winters", "personal-operating-code", "operator-process",
        "composure", "state-management", "emotional-regulation", "become-water", "no-off-night",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 9 · Mindset-as-software + resourcefulness + self-audit (meta) · Laws 36, 85, 77, 76, 23, 38, 34
# ---------------------------------------------------------------------------
add_chunk(
    num=9,
    domain="operator-doctrine",
    concept="Mindset-as-software · the mind is constantly programming · install the operating state deliberately + resourcefulness + self-audit",
    summary=(
        "Winters frames the mind as software (Law 36: your mind is constantly programming itself · "
        "Law 85: your mindset is your operating system). The prescription: install the state "
        "deliberately rather than letting default conditioning run. Law 77 (frame reality in your "
        "favor) and Law 76 (visualize) are the input-control tools. Law 23 (become resourceful) is "
        "the problem-solving frame · find a way regardless of conditions. Law 38 (constantly evaluate "
        "your progress) and Law 34 (confront your demons) are the self-audit loop · the operator "
        "runs a continuous feedback cycle on their own programming."
    ),
    usable_principle=(
        "Treat mindset as installable software · the mind programs itself constantly, so install the "
        "operating state deliberately rather than running default conditioning. Frame reality in your "
        "favor; visualize the target. Be resourceful · find a way regardless of conditions. Run a "
        "continuous self-audit loop · evaluate progress, confront the weak points, re-install."
    ),
    sniped_relevance=(
        "The meta-chunk that holds the cluster together. Mindset-as-software is the operating-system "
        "metaphor the SNIPED brain itself runs on (the AI-Brain-Refinery corpus IS BJ's installed "
        "operating state). The self-audit loop maps to B7 LEAN_EXECUTION_AUDIT + monthly_constraint_"
        "audit + weekly_review templates. Resourcefulness pairs with feedback_max_default + B7 "
        "operator-engineering principles (system over inspiration). Connects to INTELLECTUAL_ARTIST_"
        "FRAME as the prescriptive meta-frame above MJ's descriptive craft account."
    ),
    direct_quotes=[
        "Your Mind is Constantly programming itself.",
        "Your Mindset Is Your operating system.",
    ],
    tags=[
        "88-laws", "winters", "personal-operating-code", "operator-doctrine",
        "mindset-as-software", "self-audit", "resourcefulness", "frame-reality", "operator-feedback-loop",
    ],
)


# ===========================================================================
# Write JSONL + em-dash sweep
# ===========================================================================

def main():
    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSONL.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    print(f"Wrote {len(chunks)} chunks to {OUT_JSONL}")

    em_char = chr(0x2014)
    text = OUT_JSONL.read_text(encoding="utf-8")
    em_count = text.count(em_char)
    if em_count:
        print(f"WARNING: {em_count} em-dashes in output. Sweeping.")
        text = text.replace(em_char, " · ")
        OUT_JSONL.write_text(text, encoding="utf-8")
    else:
        print("No em-dashes in output.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
