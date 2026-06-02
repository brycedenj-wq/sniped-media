#!/usr/bin/env python3
"""Write POLITICAL_THEORY_DISCOURSES_CHUNKS.jsonl from Machiavelli's Discourses on Livy.

12-field canonical schema. Existing domains only (power / operator-doctrine / strategy /
operator-process / leadership / ethics / culture / systems-thinking). NO new domain
(politics / political-theory / republic / statecraft / governance / history / empire NOT
created). Single source. CURATED representative institutional-power / organization-design /
operator-pattern extraction, NOT a chapter-by-chapter political-theory summary. Held as a
decision-support / pattern-library lens, NOT a directive that BJ pursue political power,
build a republic, manipulate people, or copy Machiavelli; the republican and realpolitik
material is translated into org-design / culture / incentive / power-balance patterns and
read as honest analysis, NOT endorsement. Bible held separately and untouched. Every chunk
carries the CURRENT_OPERATOR_REALITY_BRIEF reference + identity-optionality guardrail
(GUARD). Em-dash swept. No master-file writes.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "POLITICAL_THEORY_DISCOURSES_CHUNKS.jsonl"
BATCH = "POLITICAL_THEORY_DISCOURSES"

SRC = ("Discourses on Livy", "Niccolo Machiavelli", "discourses_on_livy_machiavelli.txt")

GUARD = (" Held as a power / institution-design / operator pattern-library lens, read against "
         "CURRENT_OPERATOR_REALITY_BRIEF: a transferable model of organization design, power-balance, "
         "renewal, and incentives, NOT a directive that BJ pursue political power, build a republic, "
         "manipulate people, or copy Machiavelli (the republican and realpolitik material is honest "
         "analysis translated into org-design / culture / incentive patterns, NOT an endorsement of "
         "manipulation or the seizure of power). The Bible remains held separately and untouched. No "
         "final SNIPED, SNIPED Media, or BASEPLATE direction is set here; photography remains one "
         "option among several.")

# (concept, domain, summary, usable_principle, sniped_relevance_core, [quotes], [tags])
ROWS = [
    # ---------- power · 3 (anchor) ----------
    ("Healthy conflict makes good laws: the tumults of Rome",
     "power",
     "Machiavelli's contrarian claim: the constant friction between the Roman senate (the few) and "
     "the plebeians (the many) was not a disease but the source of Rome's best laws and liberty. He "
     "finds 'wise laws in these very tumults which many would thoughtlessly condemn', because the "
     "open clash, kept within institutional bounds, produced laws beneficial to public freedom.",
     "Channeled tension between competing interests strengthens an organization; suppressing all "
     "internal disagreement removes the pressure that produces better rules and balance.",
     "A power-balance lens for BJ: productive, openly-aired disagreement between stakeholders "
     "(within bounds) makes a stronger organization than forced consensus; design for healthy "
     "tension, not silence. Translated to org design, not a political program. Held interpretively.",
     ["wise laws in these very tumults"],
     ["productive-conflict", "checks-and-balances", "tumults", "power", "machiavelli", "discourses-on-livy"]),
    ("A people is wiser and more constant than a prince",
     "power",
     "Against the common view, Machiavelli argues 'a People is wiser and more constant than a "
     "Prince': the broad base, bound by law and shared interest, judges more soundly over time and "
     "is harder to corrupt than a single ruler, and so the many serve as the guardian of liberty "
     "against the ambition of the few.",
     "A broad, informed base is a more durable check and a sounder long-run judge than any single "
     "authority; distributing the guardianship of the core widely protects it from capture.",
     "A power lens for BJ: the broad base (an audience, a community, distributed stakeholders) is a "
     "more constant guardian of the mission than any single gatekeeper; weight its judgment and "
     "guard against capture by a narrow few. Held interpretively.",
     ["wiser and more constant"],
     ["the-many-vs-the-few", "broad-base", "guardian-of-liberty", "power", "machiavelli", "discourses-on-livy"]),
    ("How liberty is lost: ambition, inequality, and the idle gentry",
     "power",
     "Machiavelli holds that free states are corrupted from within by accumulating inequality and "
     "the ambition of the powerful, above all by 'gentlemen' (gentiluomini) who 'live in affluence' "
     "off estates without work and grow hostile to equal liberty. Where such a class entrenches, a "
     "free commonwealth cannot survive; concentrated idle privilege is the solvent of shared power.",
     "Concentrated, unearned privilege and growing inequality quietly dissolve a healthy power-"
     "balance; watch for an entrenched class that extracts without contributing as the leading "
     "indicator of decay.",
     "A power-decay lens for BJ: entrenched, extractive, unearned advantage (in a team, a market, a "
     "platform) corrodes the shared base that keeps a system healthy; treat it as a warning sign, "
     "not a goal. Read as cautionary analysis. Held interpretively.",
     ["to live as gentlemen"],
     ["inequality", "ambition", "corruption-of-power", "power", "machiavelli", "discourses-on-livy"]),
    # ---------- operator-process · 1 ----------
    ("The right to accuse vs calumny: build a lawful release valve",
     "operator-process",
     "Machiavelli prizes the institutional 'right to accuse' (a formal, accountable channel to "
     "charge wrongdoers before the people or a tribunal) as a vent for the 'evil humours' that "
     "otherwise overwhelm a state, while condemning 'calumny' (unaccountable rumor) as purely "
     "corrosive. The same grievance, given a lawful outlet, strengthens; left to whisper, it rots.",
     "Give grievances a legitimate, accountable channel; un-channeled complaint turns into corrosive "
     "rumor and faction. The design choice is the outlet, not the suppression, of conflict.",
     "An operating lens for BJ: build legitimate, accountable channels for complaint and dissent "
     "(feedback, escalation, accountability); grievance with no lawful outlet curdles into rumor and "
     "distrust. Held interpretively.",
     ["the right to accuse", "Calumny is as hurtful"],
     ["grievance-channel", "accountability", "release-valve", "operator-process", "machiavelli", "discourses-on-livy"]),
    # ---------- operator-doctrine · 1 (+ synthesis below) ----------
    ("Return to first beginnings: renew before the drift compounds",
     "operator-doctrine",
     "Machiavelli's law of durability: states, sects, and institutions last only if periodically "
     "'brought back to their first beginnings', the founding excellence that gave them their "
     "reputation and growth. Over time that excellence decays; the organizations that endure are "
     "those whose institutions can renew themselves back to first principles before the rot spreads.",
     "Schedule deliberate renewal back to founding values and standards; durability comes from "
     "periodically returning to first principles, not from never changing or from drifting "
     "indefinitely.",
     "A renewal lens for BJ: build in periodic returns to first principles (the founding standards, "
     "the original quality bar) before drift compounds; the work that lasts is renewed, not left to "
     "decay. Held interpretively.",
     ["back to their first beginnings"],
     ["renewal", "first-principles", "founding-excellence", "operator-doctrine", "machiavelli", "discourses-on-livy"]),
    # ---------- leadership · 1 ----------
    ("The founder must stand alone to establish; institutions then sustain",
     "leadership",
     "Machiavelli concludes that 'he who gives new institutions to a State must stand alone': the "
     "founding act requires a single decisive will, because a committee cannot constitute order. But "
     "the same concentration that founds must then hand off to institutions; a state that depends on "
     "one person does not endure. Founding and sustaining demand opposite things.",
     "Founding requires decisive, even solitary action; durability requires handing that authority "
     "off to institutions. Do not confuse the concentration that starts something with the "
     "distribution that sustains it.",
     "A founder lens for BJ: the build phase needs decisive solo ownership, but anything meant to "
     "last must be handed off to systems and people rather than staying dependent on the founder. "
     "Held interpretively.",
     ["must stand alone"],
     ["founder-vs-maintainer", "decisive-founding", "institutionalize", "leadership", "machiavelli", "discourses-on-livy"]),
    # ---------- strategy · 2 ----------
    ("Adapt to the times or fall: fortune varies because you do not change",
     "strategy",
     "Machiavelli's account of why fortunes rise and fall: success comes when 'his methods suited "
     "with the times', and ruin follows when a man clings to a method whose moment has passed, "
     "because 'times change and he does not change with them'. The cautious man fails in bold times, "
     "the bold man in cautious times; the rare survivor matches mode to moment.",
     "Match your mode of operating to the conditions and change it as they change; the most common "
     "cause of decline is succeeding with one approach and then refusing to adapt when the "
     "environment shifts.",
     "An adaptation lens for BJ: the approach that wins in one phase (or market, or platform moment) "
     "becomes the failure mode in the next; deliberately re-examine and shift your mode as conditions "
     "change. Held interpretively.",
     ["he does not change with them"],
     ["adaptation", "fortune", "match-mode-to-moment", "strategy", "machiavelli", "discourses-on-livy"]),
    ("Conspiracies usually fail: the asymmetry of covert schemes",
     "strategy",
     "Machiavelli's long analysis of conspiracies concludes they are extraordinarily dangerous to "
     "the conspirators: a plot faces 'danger at three stages, before, during, and after', requires "
     "trusting accomplices who may betray, and rarely survives execution. The expected value of "
     "elaborate covert schemes is poor; open, simple action is usually safer and more effective.",
     "Complex covert schemes carry asymmetric downside (exposure, betrayal, failure at any of many "
     "stages); prefer open, simple, robust action over clever conspiratorial plans.",
     "A judgment lens for BJ: elaborate behind-the-scenes maneuvering is fragile and high-risk; "
     "straightforward, open moves usually beat clever schemes. (And a caution against being the "
     "target of one.) Held interpretively, not a tactic to deploy on people.",
     ["danger at three stages"],
     ["conspiracies", "asymmetric-risk", "simplicity", "strategy", "machiavelli", "discourses-on-livy"]),
    # ---------- culture · 1 ----------
    ("Shared belief as cohesion: the instrumental use of civic religion",
     "culture",
     "Machiavelli reads Roman religion functionally: commanders won obedience and courage by "
     "'making use of religion to keep the minds' of their men aligned, and shared rites and oaths "
     "bound the commonwealth together. He values religion here not as faith but as social "
     "technology, the shared belief and ritual that produce cohesion and trust.",
     "Shared belief, ritual, and a common story are real cohesion technology for any group; a strong "
     "shared mission and culture bind people more reliably than rules alone.",
     "A culture lens for BJ: a genuine shared mission, language, and ritual is real organizational "
     "cohesion (read honestly and instrumentally here, not as a faith claim, and the Bible stays a "
     "held anchor, separate). Held interpretively.",
     ["making use of religion"],
     ["shared-belief", "civic-cohesion", "ritual", "culture", "machiavelli", "discourses-on-livy"]),
    # ---------- systems-thinking · 1 (cautionary) ----------
    ("Institutions decay without renewal: corruption as a compounding system",
     "systems-thinking",
     "Machiavelli treats states and institutions as 'mixed bodies' subject to entropy: the founding "
     "excellence is real, but 'in progress of time this excellence' becomes corrupted, slowly and "
     "invisibly, unless the system can renew itself. Decay is not a single failure but a compounding "
     "process; the institutions that last have a built-in mechanism for catching and reversing drift.",
     "Treat institutional decay as a slow, compounding systemic process, not a discrete event; build "
     "the feedback mechanism that detects and reverses drift before it becomes irreversible.",
     "A systems lens for BJ: standards, culture, and quality drift downward by default and compound "
     "invisibly; build the mechanism that catches and reverses the drift (the renewal counterpart to "
     "first-principles return). Held interpretively.",
     ["in progress of time this excellence"],
     ["decay", "compounding-drift", "institutional-entropy", "systems-thinking", "machiavelli", "discourses-on-livy"]),
    # ---------- ethics · 1 (read honestly, not endorsement) ----------
    ("Ends-and-means realism, read honestly: Romulus excused, not blamed",
     "ethics",
     "Machiavelli's most notorious move: judging the founding act of order by its result, he holds "
     "that for the deaths of Remus and Tatius 'Romulus is to be excused rather than blamed', because "
     "the act founded a lasting common good. Read honestly (the Chernow-style reading), this is "
     "descriptive analysis of how founding power actually behaves, NOT an endorsement of murder or "
     "manipulation; BJ's own ethics remain his deliberate choice.",
     "Understand clearly that power and founding often involve hard, morally fraught acts judged by "
     "their results, so you are not naive, while choosing your own ethics deliberately rather than "
     "adopting ruthlessness as a value.",
     "An honest-realism lens for BJ: see how power and founding actually operate so you are not "
     "naive, but this is explicitly NOT a directive to act ruthlessly or manipulate people; the "
     "realpolitik is read as description, and BJ's ethics stay his own choice. Held interpretively.",
     ["excused rather than blamed"],
     ["ends-and-means", "honest-realism", "founding-ethics", "ethics", "machiavelli", "discourses-on-livy"]),
    # ---------- synthesis · 1 ----------
    ("Synthesis: the institutional operating pattern and the optionality guardrail",
     "operator-doctrine",
     "The Discourses yields a portable institution-design pattern: channel conflict through lawful "
     "outlets rather than suppressing it ('wise laws in these very tumults'), balance the few against "
     "the many, renew periodically back to first principles, found decisively but hand off to "
     "institutions, and adapt your mode to the times. It is held as an interpretive pattern library, "
     "NOT doctrine: the republican and realpolitik material informs organization design without "
     "endorsing the pursuit of power or manipulation.",
     "Mine the Discourses for transferable organization-design, power-balance, and renewal patterns "
     "while holding it as interpretation, not doctrine or directive; the value is sharpened "
     "institutional judgment, decoupled from the politics and power-seeking that produced it.",
     "This synthesizes the lane for BJ: an organization-design and power-balance toolkit (channel "
     "conflict, balance power, renew to first principles, found-then-institutionalize, adapt) held "
     "as decision-support against CURRENT_OPERATOR_REALITY_BRIEF, NOT a directive to pursue power, "
     "build a republic, manipulate people, or copy Machiavelli; photography remains one option among "
     "several; no final SNIPED / SNIPED Media / BASEPLATE direction is set.",
     ["wise laws in these very tumults", "one option among several"],
     ["synthesis", "institution-design", "optionality", "operator-doctrine", "machiavelli", "discourses-on-livy"]),
]


def sweep(o):
    if isinstance(o, str):
        return o.replace(chr(0x2014), " · ")
    if isinstance(o, list):
        return [sweep(x) for x in o]
    if isinstance(o, dict):
        return {k: sweep(v) for k, v in o.items()}
    return o


def main():
    title, author, sfile = SRC
    lines = []
    for i, (concept, domain, summary, principle, relevance, quotes, tags) in enumerate(ROWS, 1):
        rec = {
            "chunk_id": f"{BATCH}_{i:03d}",
            "batch_id": BATCH,
            "source_title": title,
            "source_file": sfile,
            "author": author,
            "domain": domain,
            "concept": concept,
            "summary": summary,
            "usable_principle": principle,
            "sniped_relevance": relevance + GUARD,
            "direct_quotes": quotes,
            "tags": tags,
        }
        lines.append(sweep(rec))

    text = "\n".join(json.dumps(r, ensure_ascii=False) for r in lines) + "\n"
    assert chr(0x2014) not in text, "em-dash leaked"
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {len(lines)} chunks -> {OUT}")
    doms, srcs = {}, {}
    for r in lines:
        doms[r["domain"]] = doms.get(r["domain"], 0) + 1
        srcs[r["source_file"]] = srcs.get(r["source_file"], 0) + 1
    print("domains:", json.dumps(doms, ensure_ascii=False))
    print("per-source:", json.dumps(srcs, ensure_ascii=False))
    forb = [d for d in ("politics", "political-theory", "republic", "statecraft",
                        "governance", "history", "empire") if d in doms]
    print("forbidden domains present:", forb or "NONE")
    mx = max(len(q.split()) for r in lines for q in r["direct_quotes"])
    print("longest quote words:", mx)


if __name__ == "__main__":
    main()
