#!/usr/bin/env python3
"""Write SYSTEMS_THINKING_CHUNKS.jsonl · 12 curated chunks · 4 sources.

batch_id: SYSTEMS_THINKING · chunk_id: SYSTEMS_THINKING_NNN
The systems-literacy / process / media-ecology register · the THIRD of the four
ADJACENT_TIER_2_CLUSTERS sub-lanes. Existing domains only (systems-thinking anchor).
No new domain. Uses `systems-thinking`, NEVER the thin `systems` (6, not grown);
`creativity` NOT created. No em-dashes. Curated systems-literacy/operator-pattern
extraction (NOT a systems-book chapter summary or systems-theory cosplay).
Decision-neutral: NOT a directive and NOT a SNIPED brand. Guardrail in every chunk.
"""
import json
import os

OUT = os.path.expanduser(
    "~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/SYSTEMS_THINKING_CHUNKS.jsonl")

CM = ("The Checklist Manifesto", "the_checklist_manifesto_gawande.txt", "Atul Gawande")
UM = ("Understanding Media", "understanding_media_mcluhan.txt", "Marshall McLuhan")
TIS = ("Thinking in Systems", "thinking_in_systems_meadows.txt", "Donella Meadows")
FD = ("The Fifth Discipline", "the_fifth_discipline_senge.txt", "Peter M. Senge")

GUARD = (" Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support and "
         "pattern-library only, not doctrine and not a directive: not a directive that BJ "
         "become a systems-theory account, productivity influencer, management guru, "
         "consultant, complexity bro, corporate thought-leader, or abstract framework person. "
         "Systems-thinking material is held as execution reliability, environment-awareness, "
         "feedback-loop literacy, leverage-point thinking, and operator judgment. No final "
         "SNIPED, SNIPED Media, or BASEPLATE direction; photography remains one option among "
         "several.")

# (source, domain, concept, summary, usable_principle, relevance_lead, quotes, tags)
ROWS = [
    # ---- THE CHECKLIST MANIFESTO (Gawande) · 2 ----
    (CM, "operator-process",
     "Checklists close the ineptitude gap under complexity",
     "Gawande distinguishes ignorance (we don't know) from ineptitude (we know but fail to apply it "
     "correctly), and argues that in complex work most failure is now ineptitude. A simple checklist of "
     "the known, critical, easily-missed steps catches the predictable lapses, with pause points where "
     "the team stops to verify before proceeding.",
     "For complex, high-stakes work, build a short checklist of the few critical, easily-missed steps "
     "with explicit pause points; most failure is forgetting the known, not lacking knowledge.",
     "BJ can use lightweight checklists with pause points to make his own complex/repeatable work "
     "reliable, a directly usable execution tool, not a directive to systematize everything.",
     ["ineptitude", "pause points"],
     ["checklist", "execution-reliability", "ineptitude", "pause-points", "operator-process"]),

    (CM, "operator-doctrine",
     "DO-CONFIRM vs READ-DO; the checklist empowers the team",
     "Gawande's craft of the checklist: choose DO-CONFIRM (work from memory, then stop and confirm) or "
     "READ-DO (read each step then do it), keep it short and tested, and use it to flatten hierarchy so "
     "anyone can speak up. The checklist is less a script than a discipline that distributes "
     "responsibility and forces communication at the critical moments.",
     "Design the check as DO-CONFIRM or READ-DO to fit the task, keep it lean and tested, and use it to "
     "license everyone to flag a missed step; the tool is really a communication discipline.",
     "BJ can hold the checklist as a team-communication and shared-responsibility discipline (not just "
     "a list), a transferable pattern for any collaboration, held as method.",
     ["DO-CONFIRM", "READ-DO"],
     ["do-confirm", "read-do", "communication", "shared-responsibility", "discipline"]),

    # ---- UNDERSTANDING MEDIA (McLuhan) · 3 ----
    (UM, "culture",
     "The medium is the message: the form shapes us more than the content",
     "McLuhan's central claim is that the medium is the message: the dominant medium of an age reshapes "
     "perception, social organization, and pace of life far more than any particular content it "
     "carries. The effects come from the form and scale a medium introduces, not from the programming "
     "inside it.",
     "Read the medium itself (its form, scale, and bias), not just the content, when judging an effect; "
     "the channel reshapes perception more than the message does.",
     "BJ can attend to how a chosen medium (platform, format) shapes audience and perception independent "
     "of content, a cultural-literacy lens for any visual/communication work, held as analysis.",
     ["medium is the message"],
     ["medium-is-the-message", "form-over-content", "perception", "media-ecology", "culture"]),

    (UM, "systems-thinking",
     "Media as extensions of man and as environment",
     "McLuhan frames each medium as an extension of a human faculty (the wheel extends the foot, print "
     "the eye, electric media the nervous system) that reshapes the whole sensory and social system "
     "around it. A new medium becomes an invisible environment, the ground that quietly reorganizes "
     "everything inside it, so the real effects are systemic and easy to miss.",
     "Treat a new medium or tool as an environment that reorganizes the whole system around it, not as a "
     "neutral add-on; the systemic ground matters more than the figure.",
     "BJ can read new tools (AI, platforms) as environments that reshape the whole system of how he and "
     "others work, a systems-literacy lens held as analysis, not technological determinism to adopt.",
     ["extensions of man"],
     ["extensions-of-man", "environment", "figure-ground", "systemic-effects", "systems-thinking"]),

    (UM, "mental-models",
     "Hot versus cool media and the global village",
     "McLuhan's hot/cool distinction is a lens for reading channels: a hot medium extends one sense in "
     "high definition and asks little participation; a cool medium is low-definition and demands the "
     "audience fill it in. Electric media collapse distance into a participatory global village, "
     "changing how involved and reactive people become.",
     "Classify a channel by how much it asks the audience to participate (hot/low-participation vs "
     "cool/high-participation) to predict its social effect; connectivity raises involvement and "
     "reactivity.",
     "BJ can use the hot/cool lens to choose channels by the participation they invite, a practical "
     "media-reading model held as analysis, not a directive to chase any platform.",
     ["hot media", "global village"],
     ["hot-and-cool", "participation", "global-village", "channel-choice", "mental-models"]),

    # ---- THINKING IN SYSTEMS (Meadows) · 3 + synthesis ----
    (TIS, "systems-thinking",
     "Stocks, flows, and feedback: structure drives behavior",
     "Meadows builds systems literacy from stocks (accumulations) and flows (rates of change) governed "
     "by feedback loops, balancing (goal-seeking) and reinforcing (amplifying). The key insight is that "
     "a system's pattern of behavior over time comes from its own internal structure, not from external "
     "events, so to change behavior you change the structure.",
     "Look past events to the stocks, flows, and feedback loops that generate behavior; a system's "
     "behavior comes from its structure, so change the structure, not the symptom.",
     "BJ can diagnose recurring patterns (in his work, market, or tools) by their underlying structure "
     "rather than reacting to events, a core systems-literacy lens held as analysis.",
     ["stocks and flows", "behavior over time"],
     ["stocks-and-flows", "feedback-loops", "structure-drives-behavior", "systems-thinking", "diagnosis"]),

    (TIS, "systems-thinking",
     "Leverage points: where to intervene in a system",
     "Meadows ranks leverage points, places to intervene in a system, from low to high: tweaking "
     "parameters and buffers is low leverage, while changing information flows, rules, goals, and the "
     "paradigm out of which the system arises is high leverage. The highest-leverage interventions are "
     "the most counterintuitive and the most resisted.",
     "Aim interventions at high-leverage points (rules, goals, the paradigm) rather than parameters; the "
     "biggest leverage is usually the least obvious place people push.",
     "BJ can ask where the real leverage is (goal/rule/paradigm vs knob-tweaking) before spending effort, "
     "a prioritization lens for any system he works within, held as analysis.",
     ["Leverage Points", "Places to Intervene"],
     ["leverage-points", "intervention", "paradigm", "high-leverage", "systems-thinking"]),

    (TIS, "decision-making",
     "Bounded rationality and why we misread systems",
     "Meadows explains that we misjudge systems because of bounded rationality (we act on the limited, "
     "local information we can see), false boundaries, delays, and nonlinearities. We react to events "
     "and recent signals, not to the structure and delays that actually drive outcomes, which produces "
     "overshoot, oscillation, and unintended consequences.",
     "Account for bounded rationality and delays in your own and others' judgment; people act on local "
     "signals, so expect overshoot and lagged effects rather than clean cause and effect.",
     "BJ can treat his and others' judgment as bounded and delay-blind, building in caution about "
     "lagged feedback and local-information blind spots, a decision-hygiene lens held as analysis.",
     ["bounded rationality"],
     ["bounded-rationality", "delays", "misreading-systems", "unintended-consequences", "decision-making"]),

    # ---- THE FIFTH DISCIPLINE (Senge) · 3 ----
    (FD, "systems-thinking",
     "The laws of systems: pushing harder and shifting the burden",
     "Senge's laws of the fifth discipline are systems cautions: the harder you push, the harder the "
     "system pushes back (compensating feedback); the easy fix often shifts the burden to a symptomatic "
     "solution that erodes the real capacity to solve the problem; and cause and effect are not close "
     "in time or space. Quick fixes frequently make the underlying system worse.",
     "Beware compensating feedback (pushing harder backfires) and shifting-the-burden fixes that erode "
     "the real solution; look for the delayed, distant cause rather than the obvious one.",
     "BJ can watch for the harder-you-push and shifting-the-burden traps in his own problem-solving, a "
     "systems-caution lens held as analysis, not a framework to preach.",
     ["harder you push", "Shifting the Burden"],
     ["compensating-feedback", "shifting-the-burden", "quick-fix-trap", "delay", "systems-thinking"]),

    (FD, "operator-doctrine",
     "The learning organization and its five disciplines",
     "Senge's learning organization is built from five disciplines: personal mastery, surfacing mental "
     "models, building shared vision, and team learning, integrated by systems thinking as the fifth "
     "discipline that fuses the others into a whole. The aim is a group that keeps expanding its "
     "capacity to create the results it wants and to learn how to learn together.",
     "Build capacity through the disciplines of personal mastery, examined mental models, shared vision, "
     "and team learning, integrated by systems thinking; treat learning-to-learn as the real asset.",
     "BJ can hold the five-disciplines frame as a model for how he and any collaborators keep learning "
     "and improving together, held as analysis, not a directive to build a corporation.",
     ["learning organization", "fifth discipline"],
     ["learning-organization", "five-disciplines", "shared-vision", "team-learning", "operator-doctrine"]),

    (FD, "mental-models",
     "Surfacing and testing the mental models that drive action",
     "Senge's discipline of mental models is the practice of surfacing the deep assumptions and "
     "generalizations that silently shape how we see and act, then holding them up for examination and "
     "testing rather than treating them as reality. The discipline pairs advocacy with inquiry so beliefs "
     "can be made explicit and revised.",
     "Make your governing assumptions explicit and test them (balance advocating your view with "
     "inquiring into others') instead of mistaking your mental model for reality.",
     "BJ can practice surfacing and testing his own assumptions before acting on them, a directly usable "
     "judgment discipline, held as method.",
     ["Mental Models"],
     ["mental-models", "assumptions", "advocacy-and-inquiry", "ladder-of-inference", "judgment"]),

    # ---- SYNTHESIS · 1 (attributed to Thinking in Systems) ----
    (TIS, "systems-thinking",
     "Synthesis: the systems-literacy operator toolkit",
     "Across the four sources a systems-literacy toolkit emerges: make complex execution reliable with "
     "checklists and pause points (Gawande); read the medium as an environment that reshapes the whole "
     "system, not just its content (McLuhan); see stocks, flows, and feedback so structure (not events) "
     "explains behavior, and aim at high-leverage points while respecting bounded rationality and delays "
     "(Meadows); and watch the laws of systems while building a learning organization through examined "
     "mental models (Senge). It is a pattern-library for execution reliability, environment-awareness, "
     "feedback-loop literacy, and leverage-point thinking.",
     "Combine checklist reliability, medium-as-environment, structure-drives-behavior, leverage-point "
     "thinking, bounded-rationality caution, and examined mental models into a systems-literacy operator "
     "toolkit, held as analysis rather than a framework identity.",
     "BJ holds this as execution-reliability and systems-literacy for his build-mode stage, NOT a "
     "directive to become a systems-theory account, a complexity bro, or an abstract framework person.",
     [],
     ["synthesis", "systems-literacy", "leverage", "feedback", "operator-toolkit"]),
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
            "chunk_id": f"SYSTEMS_THINKING_{i:03d}",
            "batch_id": "SYSTEMS_THINKING",
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

    forbidden = {"systems", "management", "consulting", "service", "creativity",
                 "expertise", "innovation", "productivity", "business", "self-help"}
    used = {r["domain"] for r in rows}
    assert not (used & forbidden), used & forbidden
    assert "systems-thinking" in used and "systems" not in used

    rows = [sweep(r) for r in rows]
    blob = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    assert chr(0x2014) not in blob, "em-dash found in output"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(blob)
    print(f"wrote {len(rows)} chunks to {OUT}")


if __name__ == "__main__":
    main()
