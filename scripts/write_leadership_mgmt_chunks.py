#!/usr/bin/env python3
"""Write LEADERSHIP_MGMT_CHUNKS.jsonl · 16 curated chunks · 9 sources.

batch_id: LEADERSHIP_MGMT · chunk_id: LEADERSHIP_MGMT_NNN
The leading-people / team-culture / management-system register · the SECOND of the
four ADJACENT_TIER_2_CLUSTERS sub-lanes. Existing domains only (leadership anchor).
No new domain. `systems` NOT used/grown (route to systems-thinking if needed, not
needed here); `creativity` NOT created. No em-dashes. Curated leadership/operator-
management extraction (NOT a leadership-book chapter summary or corporate playbook).
Decision-neutral: NOT a directive and NOT a SNIPED brand. Guardrail in every chunk.
"""
import json
import os

OUT = os.path.expanduser(
    "~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/LEADERSHIP_MGMT_CHUNKS.jsonl")

CC = ("The Culture Code", "the_culture_code_coyle.txt", "Daniel Coyle")
LTT = ("Leadership in Turbulent Times", "leadership_in_turbulent_times_goodwin.txt", "Doris Kearns Goodwin")
TOR = ("Team of Rivals", "team_of_rivals_goodwin.txt", "Doris Kearns Goodwin")
EO = ("Extreme Ownership", "extreme_ownership_willink_babin.txt", "Jocko Willink and Leif Babin")
DOL = ("The Dichotomy of Leadership", "the_dichotomy_of_leadership_willink_babin.txt", "Jocko Willink and Leif Babin")
MWM = ("Measure What Matters", "measure_what_matters_doerr.txt", "John Doerr")
RC = ("Radical Candor", "radical_candor_scott.txt", "Kim Scott")
TSA = ("Turn the Ship Around!", "turn_the_ship_around_marquet.txt", "L. David Marquet")
HOM = ("High Output Management", "high_output_management_grove.txt", "Andrew S. Grove")

GUARD = (" Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support and "
         "pattern-library only, not doctrine and not a directive: not a directive that BJ "
         "become a management guru, productivity influencer, corporate thought-leader, "
         "leadership coach, military-bro operator, founder-cult CEO, or boss persona. "
         "Leadership and management material is held as team design, decision hygiene, "
         "standards, accountability, operating cadence, and leadership judgment. No final "
         "SNIPED, SNIPED Media, or BASEPLATE direction; photography remains one option among "
         "several.")

# (source, domain, concept, summary, usable_principle, relevance_lead, quotes, tags)
ROWS = [
    # ---- THE CULTURE CODE (Coyle) · 2 ----
    (CC, "culture",
     "Belonging cues and psychological safety build team performance",
     "Coyle argues that high-performing groups are built on safety, not talent: members continuously "
     "exchange belonging cues (proximity, eye contact, attention, turn-taking) that signal we are "
     "connected and safe, producing the state Amy Edmondson calls psychological safety. The felt sense "
     "of safety, not raw skill, is what lets a group cooperate and perform.",
     "Engineer felt safety through repeated small belonging cues; a group that feels safe outperforms a "
     "more talented group that does not.",
     "For BJ this frames team and collaborator performance as a function of felt safety and belonging "
     "signals, a culture-design lens held as analysis, not a directive to run a company.",
     ["belonging cues", "psychological safety"],
     ["belonging", "psychological-safety", "team-culture", "safety", "cooperation"]),

    (CC, "leadership",
     "Build safety and lead the vulnerability loop by going first",
     "In Coyle's three skills (Build Safety, Share Vulnerability, Establish Purpose) the leader seeds "
     "trust by triggering the vulnerability loop: openly admitting fallibility and asking for help, "
     "which signals it is safe for others to do the same. Cooperation is built when someone goes first "
     "and the gesture is reciprocated, not by projecting invulnerable competence.",
     "Go first with candid fallibility (ask for help, admit error) to open the vulnerability loop; "
     "trust is built by reciprocated openness, not by projecting strength.",
     "BJ can lead trust by modeling fallibility first in any collaboration, a relational discipline held "
     "as pattern, not a directive to adopt a boss persona.",
     ["Build Safety", "Vulnerability Loop"],
     ["vulnerability", "trust", "going-first", "reciprocity", "leadership"]),

    # ---- LEADERSHIP IN TURBULENT TIMES (Goodwin) · 1 ----
    (LTT, "leadership",
     "Leadership is developed, and the type must match the moment",
     "Goodwin's study of four presidents finds no single path to leadership: it is forged through "
     "adversity and deliberately developed, not simply innate. She distinguishes types matched to the "
     "moment, transformational (Lincoln), crisis management (Theodore Roosevelt), turnaround (Franklin "
     "Roosevelt), and visionary (Johnson), arguing the situation calls for a particular kind of leading.",
     "Treat leadership as a developed capacity and read the moment to choose the mode it requires "
     "(transformational, crisis, turnaround, or visionary) rather than leading one fixed way.",
     "BJ can hold leadership as learnable and situation-matched (diagnose what the moment needs), a "
     "developmental lens held as analysis, not a directive to seek public office or power.",
     ["No single path", "Transformational Leadership"],
     ["leadership-development", "adversity", "crisis-leadership", "situational", "types"]),

    # ---- TEAM OF RIVALS (Goodwin) · 1 ----
    (TOR, "founder-psychology",
     "Assemble a team of rivals; lead through emotional strength",
     "Goodwin's account of Lincoln shows him appointing his strongest rivals to his cabinet rather than "
     "loyalists, then leading them through emotional strengths: empathy, self-control, the capacity to "
     "absorb blame and share credit, and the magnanimity to hear dissent without insecurity. Surrounding "
     "himself with abler, opposed men was a sign of confidence, not weakness.",
     "Surround yourself with strong, dissenting talent and lead it through emotional control, "
     "credit-sharing, and absorbing blame; security with rivals is a strength, not a risk.",
     "BJ can read welcoming abler rivals and leading through emotional steadiness as a temperament "
     "pattern, held as analysis, not a directive to assemble a cabinet or chase political leadership.",
     ["Team of rivals"],
     ["team-of-rivals", "emotional-intelligence", "dissent", "magnanimity", "temperament"]),

    # ---- EXTREME OWNERSHIP (Willink & Babin) · 2 ----
    (EO, "leadership",
     "Extreme Ownership: the leader owns everything, no bad teams",
     "Willink and Babin's foundational mind-set is Extreme Ownership: the leader owns everything in "
     "their world and has no one else to blame, including failures of subordinates, processes, and "
     "resources. Their corollary, no bad teams only bad leaders, holds that the same people perform "
     "differently under different leadership, so the leader is the variable.",
     "Take total ownership of outcomes including others' failures; treat the leader as the variable "
     "(no bad teams, only bad leaders) rather than blaming circumstances or people.",
     "BJ can apply extreme ownership to his own work (own the outcome, fix the variable he controls) "
     "without it being a directive to command a team or adopt a military persona.",
     ["Extreme Ownership", "No Bad Teams"],
     ["ownership", "accountability", "no-bad-teams", "responsibility", "leadership"]),

    (EO, "operator-doctrine",
     "Decentralized Command and the Laws of Combat",
     "Willink and Babin teach decentralized command: leaders give intent and authority down to the "
     "lowest capable level so the team executes without waiting for orders, governed by the Laws of "
     "Combat (Cover and Move, Simple, Prioritize and Execute, Decentralized Command). Everyone leads at "
     "their level once they understand the why and the priority.",
     "Push authority and decisions down to the people closest to the work, bound by a shared intent and "
     "a clear priority, so execution does not bottleneck on the leader.",
     "BJ can hold decentralized-command and prioritize-and-execute as operating patterns for any team or "
     "collaborator setup, held as method, not a directive to run a unit.",
     ["Decentralized Command", "Cover and Move"],
     ["decentralized-command", "intent", "prioritize-and-execute", "laws-of-combat", "execution"]),

    # ---- THE DICHOTOMY OF LEADERSHIP (Willink & Babin) · 1 ----
    (DOL, "leadership",
     "The dichotomy: balance the opposing forces of leading",
     "The sequel reframes Extreme Ownership as a balancing act: leadership requires equilibrium between "
     "opposing forces, being aggressive but not reckless, disciplined but not rigid, a leader but also a "
     "follower, owning everything yet empowering others. Too much authority makes a team reluctant; too "
     "little leaves it directionless, so the skill is calibrating between extremes.",
     "Hold leadership as a dynamic balance between opposing forces rather than a fixed maxim; most "
     "failures come from taking one true principle too far.",
     "BJ can read leadership choices as calibrations between opposing pulls (own yet empower, push yet "
     "listen), a judgment lens held as analysis, not a directive.",
     ["balance", "opposing forces"],
     ["dichotomy", "balance", "calibration", "opposing-forces", "judgment"]),

    # ---- MEASURE WHAT MATTERS (Doerr) · 2 ----
    (MWM, "operator-process",
     "OKRs: objectives paired with measurable key results",
     "Doerr's OKR system pairs each Objective (a qualitative, meaningful goal) with a few Key Results "
     "(quantitative, time-bound measures that prove the objective is met). The structure links daily "
     "work to the broader mission, makes progress transparent and trackable, and forces clarity about "
     "what done actually looks like.",
     "Pair every meaningful objective with a few measurable, time-bound key results so progress is "
     "transparent and 'done' is defined, not asserted.",
     "BJ can apply objective-plus-measurable-key-results to his own goals and projects, a directly "
     "usable goal-structuring tool.",
     ["objectives and key results", "OKR"],
     ["OKR", "objectives", "key-results", "measurement", "goal-system"]),

    (MWM, "strategy",
     "Focus and commit to priorities; stretch for amazing",
     "Doerr's superpowers include focus and commit to priorities (choose the few objectives that matter "
     "most and say no to the rest) and stretch for amazing (set deliberately ambitious goals that force "
     "new ways of working). The discipline is in the choosing: a short list of true priorities beats a "
     "long list of intentions.",
     "Choose a short list of the few priorities that matter most and commit, then set some goals "
     "deliberately beyond comfortable reach; focus and stretch are both choices.",
     "BJ can use focus-and-commit (few priorities) plus selective stretch goals to allocate limited "
     "build-mode capacity, a prioritization pattern held as analysis.",
     ["Focus and Commit to Priorities", "Stretch for Amazing"],
     ["focus", "prioritization", "commit", "stretch-goals", "strategy"]),

    # ---- RADICAL CANDOR (Scott) · 2 ----
    (RC, "leadership",
     "Radical Candor: care personally and challenge directly",
     "Scott's framework puts two dimensions together: Care Personally (genuine concern for the person) "
     "and Challenge Directly (saying the hard, honest thing about the work). Radical Candor is the "
     "combination; it builds trust and improves the work because the challenge is delivered from "
     "evident care.",
     "Combine genuine care for the person with direct challenge on the work; honesty delivered from care "
     "is what actually helps and builds trust.",
     "BJ can hold care-plus-challenge as a feedback and relationship lens for any collaboration, a "
     "pattern held as analysis, not a directive to manage a staff.",
     ["Care Personally", "Challenge Directly"],
     ["radical-candor", "care", "challenge", "feedback", "leadership"]),

    (RC, "operator-doctrine",
     "The failure modes: ruinous empathy and its cousins",
     "Scott maps what happens when a dimension is missing: caring without challenging is Ruinous Empathy "
     "(the most common, withholding hard truths to be nice), challenging without caring is Obnoxious "
     "Aggression, and neither is Manipulative Insincerity. Naming the failure modes makes it possible to "
     "catch and correct your own drift.",
     "Watch for ruinous empathy (kindness that withholds the truth) as the default failure; name the "
     "failure modes so you can correct toward candor.",
     "BJ can use the failure-mode map to audit his own communication (am I withholding to be nice?), a "
     "self-diagnostic held as method, not a directive.",
     ["Radical Candor", "Ruinous Empathy"],
     ["ruinous-empathy", "failure-modes", "candor", "self-diagnostic", "feedback"]),

    # ---- TURN THE SHIP AROUND! (Marquet) · 2 ----
    (TSA, "operator-doctrine",
     "Leader-Leader: move authority to where the information is",
     "Marquet's intent-based leadership replaces leader-follower with leader-leader: instead of giving "
     "orders, the leader gives control and pushes decisions down to where the information lives. The "
     "language shifts from asking permission to stating intent (the crew says 'I intend to...'), which "
     "forces ownership and thinking at every level.",
     "Move decision authority to where the information actually is and shift the language from "
     "permission-asking to stated intent ('I intend to...') so people own their thinking.",
     "BJ can apply move-authority-to-information and intent-based language to any delegation or "
     "collaboration, a directly transferable operating pattern.",
     ["Leader-Leader", "I Intend To"],
     ["leader-leader", "intent-based", "delegation", "control", "ownership"]),

    (TSA, "leadership",
     "Give control, but only atop competence and clarity",
     "Marquet's three legs are control, competence, and clarity: pushing control down only works when "
     "the team has the technical competence to decide well and organizational clarity about purpose and "
     "standards. He learned that giving control without building competence and clarity first produces "
     "failure, not empowerment.",
     "Before giving control away, build the competence to use it and the clarity of purpose to aim it; "
     "empowerment without competence and clarity backfires.",
     "BJ can hold the control-competence-clarity sequence as a delegation prerequisite, a judgment "
     "pattern held as analysis, not a directive to command.",
     ["give control", "control, competence, clarity"],
     ["give-control", "competence", "clarity", "empowerment", "leadership"]),

    # ---- HIGH OUTPUT MANAGEMENT (Grove) · 2 + synthesis ----
    (HOM, "operator-process",
     "Managerial leverage: a manager's output is the team's output",
     "Grove's central equation is that the output of a manager is the output of the organizational units "
     "under their supervision or influence, so the job is to maximize leverage: spend time on the few "
     "high-leverage activities (training, clear decisions, well-run meetings) that multiply the team's "
     "output rather than on low-leverage busywork.",
     "Judge your work by the output of everything you influence, and concentrate on the few "
     "high-leverage activities that multiply that output.",
     "BJ can apply the output-of-what-you-influence frame and leverage thinking to his own time "
     "allocation, a directly usable operating lens even as a solo operator.",
     ["Managerial Leverage", "output of the organizational units"],
     ["managerial-leverage", "output", "high-leverage", "time-allocation", "operator-process"]),

    (HOM, "decision-making",
     "Grove's decision model: free discussion, clear decision, full support",
     "Grove prescribes a decision process: genuinely free discussion where every view is aired, followed "
     "by a clear decision, followed by full support from everyone regardless of their earlier position. "
     "He also pushes decisions to the lowest level where competence and information meet, separating "
     "open debate from the moment of commitment.",
     "Separate open, genuinely free discussion from the clear decision and the full support that must "
     "follow it; debate hard, then commit together.",
     "BJ can use free-discussion-then-clear-decision-then-full-support as a decision hygiene pattern for "
     "any group choice, held as method.",
     ["free discussion", "clear decision"],
     ["decision-process", "free-discussion", "commitment", "decision-hygiene", "decision-making"]),

    # ---- SYNTHESIS · 1 (attributed to High Output Management) ----
    (HOM, "operator-doctrine",
     "Synthesis: the leadership/operator-management toolkit",
     "Across the nine sources a leadership toolkit emerges: build felt safety and lead the vulnerability "
     "loop (Coyle); develop leadership and match the mode to the moment (Goodwin, Turbulent Times); lead "
     "strong rivals through emotional steadiness (Goodwin, Team of Rivals); take extreme ownership and "
     "decentralize execution (Willink and Babin) while balancing the dichotomies; structure goals as "
     "OKRs and focus on the few priorities (Doerr); pair care with direct challenge (Scott); move "
     "authority to where the information is on competence and clarity (Marquet); and maximize managerial "
     "leverage with disciplined decisions (Grove). It is a pattern-library for team design, accountability, "
     "operating cadence, and leadership judgment.",
     "Combine felt-safety, developed-and-situational leadership, ownership-plus-decentralization, OKRs "
     "and focus, care-plus-challenge, authority-to-information, and managerial leverage into a leadership "
     "toolkit, held as analysis rather than a role to perform.",
     "BJ holds this as team-design, decision-hygiene, and leadership-judgment literacy for his build-mode "
     "stage, NOT a directive to become a manager, a leadership coach, or a boss persona.",
     [],
     ["synthesis", "team-design", "accountability", "operating-cadence", "operator-toolkit"]),
]


def sweep(obj):
    em = chr(0x2014)
    if isinstance(obj, str):
        return obj.replace(em, " · ")
    if isinstance(obj, list):
        return [sweep(x) for x in obj]
    if isinstance(obj, dict):
        return {k: sweep(v) for k, v in obj.items()}
    return obj


def main():
    rows = []
    for i, (src, domain, concept, summary, principle, rel, quotes, tags) in enumerate(ROWS, 1):
        title, sfile, author = src
        r = {
            "chunk_id": f"LEADERSHIP_MGMT_{i:03d}",
            "batch_id": "LEADERSHIP_MGMT",
            "source_title": title,
            "source_file": sfile,
            "author": author,
            "domain": domain,
            "concept": concept,
            "summary": summary,
            "usable_principle": principle,
            "sniped_relevance": rel + GUARD,
            "direct_quotes": quotes,
            "tags": tags,
        }
        rows.append(r)

    for r in rows:
        for q in r["direct_quotes"]:
            assert len(q.split()) <= 6, f"quote too long in {r['chunk_id']}: {q}"

    forbidden = {"management", "consulting", "service", "systems", "creativity",
                 "expertise", "innovation", "productivity", "business", "self-help"}
    used = {r["domain"] for r in rows}
    assert not (used & forbidden), used & forbidden

    rows = [sweep(r) for r in rows]
    blob = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    assert chr(0x2014) not in blob, "em-dash found in output"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(blob)
    print(f"wrote {len(rows)} chunks to {OUT}")


if __name__ == "__main__":
    main()
