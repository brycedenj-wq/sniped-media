#!/usr/bin/env python3
"""Write MODERN_COMMAND_NAPOLEON_CHUNKS.jsonl from Napoleon: A Life (Andrew Roberts).

12-field canonical schema. Existing domains only (leadership / operator-process /
strategy / power / culture / founder-psychology / systems-thinking / ethics /
operator-doctrine). NO new domain (military / politics / empire / conquest / biography /
history / commander NOT created). Single source. CURATED representative modern-command /
leadership / power / operator-pattern extraction, NOT a chapter-by-chapter biography
summary. Held as a decision-support / pattern-library lens, NOT a directive that BJ copy
Napoleon, seek conquest or status, or build an empire; the over-reach, ego, and collapse
material is cautionary, not aspirational. Bible held separately and untouched. Every
chunk carries the CURRENT_OPERATOR_REALITY_BRIEF reference + identity-optionality
guardrail (GUARD). Em-dash swept. No master-file writes.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "MODERN_COMMAND_NAPOLEON_CHUNKS.jsonl"
BATCH = "MODERN_COMMAND_NAPOLEON"

SRC = ("Napoleon: A Life", "Andrew Roberts", "napoleon_a_life_roberts.txt")

GUARD = (" Held as a leadership / power / strategy / operator pattern-library lens, read "
         "against CURRENT_OPERATOR_REALITY_BRIEF: a transferable model of command, energy, "
         "system-building, and the dynamics of power and over-reach, NOT a directive that BJ "
         "copy Napoleon, seek conquest or status, or build an empire, and not an endorsement "
         "of authoritarianism or war (the over-reach, ego, and collapse material is cautionary, "
         "not aspirational). The Bible remains held separately and untouched. No final SNIPED, "
         "SNIPED Media, or BASEPLATE direction is set here; photography remains one option "
         "among several.")

# (concept, domain, summary, usable_principle, sniped_relevance_core, [quotes], [tags])
ROWS = [
    # ---------- leadership · 4 (anchor) ----------
    ("Make ordinary people feel capable of extraordinary deeds",
     "leadership",
     "Roberts argues Napoleon's central leadership gift was making ordinary soldiers feel they "
     "were capable of extraordinary, history-making deeds; the army followed him even after the "
     "retreat from Moscow, Leipzig, and the fall of Paris. The esprit de corps he built outlasted "
     "even catastrophic defeat.",
     "The deepest leadership lever is making people believe they are capable of more than they "
     "thought; belief and shared mission, not orders, sustain a group through hardship.",
     "A leadership lens for BJ: the work of leading is to make collaborators believe they can do "
     "extraordinary things and feel part of a mission; that belief is what survives setbacks. Held "
     "interpretively.",
     ["extraordinary, history-making deeds"],
     ["inspiration", "esprit-de-corps", "belief", "leadership", "napoleon", "modern-command"]),
    ("Leading from the front: le petit caporal and shared risk",
     "leadership",
     "After the bridge at Lodi, Napoleon's men nicknamed him le petit caporal, the little corporal, "
     "in the old tradition of soldiers teasing a commander they admire. Roberts shows the bond came "
     "from his visible presence and shared exposure to risk, the same pattern (he notes) by which "
     "Caesar's men sang about him.",
     "Loyalty is earned by visibly sharing the risk and hardship you ask of others; presence at the "
     "front, not rank, builds the bond that makes people follow you.",
     "A leadership lens for BJ: visibly carrying the same risk and work you ask of collaborators "
     "earns durable loyalty; presence beats distant command. Held interpretively.",
     ["le petit caporal"],
     ["leading-from-front", "shared-risk", "loyalty", "leadership", "napoleon", "modern-command"]),
    ("Lead by recognition: it is with such baubles that men are led",
     "leadership",
     "Defending the Legion d'Honneur against councillors who called its medals and ribbons baubles "
     "that reintroduced class distinction, Napoleon argued people are moved by honour and "
     "recognition: 'it is with such baubles that men are led.' Roberts stresses he meant this not "
     "cynically but as a real insight that recognition is a motivational system.",
     "Recognition and honour are a real motivational system; visible, meaningful markers of merit "
     "move people more than money or coercion alone, provided they are earned.",
     "A leadership lens for BJ: well-designed recognition (status, credit, meaningful markers of "
     "merit) motivates collaborators and clients powerfully; people are led by honour, not pay "
     "alone. Held interpretively.",
     ["such baubles that men are led"],
     ["recognition", "honour", "motivation", "leadership", "napoleon", "modern-command"]),
    ("Energy, focus, and compartmentalization: drawers in a cupboard",
     "leadership",
     "Roberts describes Napoleon's extraordinary capacity to compartmentalize: he likened his mind "
     "to a cupboard whose drawers he could open and close at will, working on a girls' school "
     "charter on the eve of battle and sleeping by 'closing all the drawers.' Sustained energy plus "
     "the ability to give whole attention to one thing at a time underwrote his output.",
     "The ability to fully open one problem and fully close the others (single-tasking under "
     "pressure, plus deep energy) multiplies what one person can do; scattered attention is the "
     "tax.",
     "A focus lens for BJ as a solo operator: protect the capacity to give whole attention to one "
     "thing at a time and to close the other drawers, rather than running everything at once. Held "
     "interpretively.",
     ["drawers in a cupboard"],
     ["focus", "compartmentalization", "energy", "leadership", "napoleon", "modern-command"]),
    # ---------- operator-process · 3 ----------
    ("Command of detail: one of the most unrelenting micromanagers in history",
     "operator-process",
     "Roberts calls Napoleon 'one of the most unrelenting micromanagers in history': no detail about "
     "his empire was too minute, from a demi-brigade's standard to a corporal's drinking, yet this "
     "obsession with detail coexisted with transforming the legal and political landscape of Europe. "
     "His grasp of detail was the substrate of his authority.",
     "Deep command of the concrete details earns authority and enables big moves; mastery of the "
     "particulars and the grand design are not opposites but reinforce each other (within limits).",
     "An operating lens for BJ: real command of the concrete details of the work underwrites "
     "credibility and lets you move boldly; know the particulars cold. (The shadow side, doing "
     "everything yourself, is the over-reach warning.) Held interpretively.",
     ["most unrelenting micromanagers in history"],
     ["detail", "command-of-particulars", "working-method", "operator-process", "napoleon", "modern-command"]),
    ("Logistics and supply discipline: an army marches on its feet",
     "operator-process",
     "Roberts shows Napoleon's relentless attention to the unglamorous machinery of supply, an "
     "astonishing share of his letters concern boots and rations, and his maxim 'one cannot remain "
     "three minutes without gunpowder.' Though he probably never said 'an army marches on its "
     "stomach,' he knew it indubitably marched on its feet.",
     "The unglamorous supply and logistics layer sets what any campaign can attempt; sustained "
     "attention to provisioning is a leadership act, not a clerical afterthought.",
     "A foundations lens for BJ: the boring backend (cash flow, supply, operations, the basics that "
     "keep the work moving) is the real constraint on the bold plan; load it relentlessly. Held "
     "interpretively.",
     ["three minutes without gunpowder", "marched on its feet"],
     ["logistics", "supply", "operations-foundation", "operator-process", "napoleon", "modern-command"]),
    ("Build durable institutions: my true glory is my Civil Code",
     "operator-process",
     "Napoleon judged his lasting achievement to be not his battles but the Code Napoleon: 'My true "
     "glory is not to have won forty battles . . . what will live for ever, is my Civil Code.' He "
     "chaired 55 of its 107 drafting sessions, testing every provision against 'Is this fair? Is "
     "this useful?', and aimed to 'plant a few masses of granite as anchors in the soil of France.' "
     "The institutions outlasted the conquests by two centuries.",
     "Durable institutions and systems, not victories, are the real legacy; build the clear, fair, "
     "useful structures that keep working long after the founder and the campaigns are gone.",
     "A build lens for BJ: the durable value is in the systems and institutions you construct (clear, "
     "fair, useful, lasting), not the wins; build the granite anchors, not just the battles. Held "
     "interpretively.",
     ["is my Civil Code", "Is this fair? Is this useful?"],
     ["institution-building", "systems", "durable-legacy", "operator-process", "napoleon", "modern-command"]),
    # ---------- strategy · 1 ----------
    ("The operational art: concentrate force on the decisive point",
     "strategy",
     "From his earliest campaign plans Napoleon insisted 'attacks must not be disseminated, but "
     "concentrated,' and that one theatre must be made decisive ('it is Austria that must be "
     "annihilated; that accomplished, Spain and Italy will fall of themselves'). Speed, the central "
     "position, and concentration against the decisive point were the spine of the operational art "
     "Clausewitz would later theorize.",
     "Concentrate force and attention on the single decisive point rather than dispersing across "
     "many fronts; pick the theatre that, if won, makes the rest fall, and move there fast.",
     "A focus lens for BJ (echoing Clausewitz's center of gravity): identify the one decisive lever "
     "and concentrate resources and speed there rather than spreading thin across many small fronts. "
     "Held interpretively.",
     ["disseminated, but concentrated"],
     ["concentration", "decisive-point", "operational-art", "strategy", "napoleon", "modern-command"]),
    # ---------- founder-psychology · 1 ----------
    ("The self-made outsider: the autodidact arriviste who reinvented himself",
     "founder-psychology",
     "Roberts shows the Corsican outsider, mocked by detractors as 'a low-bred upstart,' who made "
     "himself through relentless self-education, as a boy he 'read constantly, especially history "
     "books,' and mastered mathematics for command, then repeatedly reinvented his role (officer, "
     "general, consul, emperor) and embodied careers-open-to-talent in his own meritocratic command.",
     "An outsider can self-make through relentless self-education and serial reinvention; treating "
     "your own role as something to be re-earned and re-defined, not inherited, is a source of drive.",
     "An operator-arc lens for BJ: the self-taught outsider who reinvents his own role resonates "
     "with building from the backend; relentless self-education and reinvention are the engine. Held "
     "as a pattern, not a directive.",
     ["read constantly, especially history books"],
     ["self-made", "autodidact", "reinvention", "founder-psychology", "napoleon", "modern-command"]),
    # ---------- culture · 1 ----------
    ("Self-myth and narrative control: he was not on oath writing bulletins",
     "culture",
     "Roberts is candid that Napoleon was a master of self-myth: he systematically exaggerated enemy "
     "losses and minimized his own in his bulletins (he 'didn't consider himself to be on oath when "
     "writing military bulletins'), shaped his image through the press, and on St Helena dictated a "
     "best-selling memoir that burnished the legend ('What a novel my life has been!'). The narrative "
     "was an instrument of power, echoing Caesar's Commentaries.",
     "Controlling the account of your own work shapes how it is judged and is part of the strategy; "
     "but read self-authored narratives critically, including your own, because the teller is not "
     "under oath.",
     "A narrative lens for BJ: documenting and framing your own work is part of the strategy (the "
     "case study, the record), AND a caution to read all self-promotion, including one's own, "
     "skeptically. Held interpretively.",
     ["What a novel my life"],
     ["self-myth", "narrative-control", "propaganda", "culture", "napoleon", "modern-command"]),
    # ---------- systems-thinking · 1 (cautionary) ----------
    ("The Continental System: a self-defeating policy that boomeranged",
     "systems-thinking",
     "Roberts argues it was 'Colbertian protectionism that brought him down': the Continental System, "
     "Napoleon's attempt to strangle British trade by blockading the continent, damaged precisely his "
     "own strongest supporters (merchants and the middle class), could not be imposed universally, and "
     "was so unworkable that his own soldiers wore uniforms made in Halifax and Leeds. Enforcing it by "
     "force dragged him into Spain and Russia.",
     "A coercive system that fights the underlying incentives tends to boomerang: it harms your own "
     "base, cannot be enforced everywhere, and the effort to impose it draws you into ever-wider "
     "commitments. Model the second-order effects before imposing a blockade.",
     "A systems lens for BJ: a policy that fights real incentives (a heavy-handed rule, a forced "
     "lock-in) often backfires on your own supporters and pulls you into escalating enforcement; "
     "design with incentives, not against them. Read as cautionary. Held interpretively.",
     ["protectionism that brought him down", "uniforms made in Halifax and Leeds"],
     ["self-defeating-system", "second-order-effects", "incentives", "systems-thinking", "napoleon", "modern-command"]),
    # ---------- power · 1 (cautionary) ----------
    ("The appetite that would not relinquish: over-reach and collapse",
     "power",
     "Roberts traces the arc from First Consul to Emperor to exile. Napoleon imagined himself as "
     "Cincinnatus, claiming he had 'acquired more glory than is necessary to be happy,' yet, unlike "
     "Washington, he never relinquished power; his 'insatiable hubris' and the failed 1812 invasion "
     "of Russia, the culminating point past which the advance destroyed itself, brought the whole "
     "edifice down. The inability to stop was the fatal flaw.",
     "Unchecked success erodes the ability to sense the limit; the discipline to consolidate, stop, "
     "or relinquish at the peak is rarer and more valuable than the drive that built the position, "
     "and its absence is what destroys empires.",
     "A power-restraint lens for BJ, read against Washington's and Grant's restraint (HISTORICAL_"
     "BIOGRAPHY) and Alexander's hubris (CLASSICAL_HISTORY): the danger at a peak is the inability "
     "to stop; build in the discipline to consolidate rather than chase endless expansion. Read as "
     "cautionary, NOT a directive to seek power. Held interpretively.",
     ["more glory than is necessary", "insatiable hubris"],
     ["overreach", "relinquishing-power", "hubris", "power", "napoleon", "modern-command"]),
    # ---------- ethics · 1 (cautionary) ----------
    ("The human cost, read honestly: the wars, the surveillance, the slavery",
     "ethics",
     "An honest reading holds the moral debits alongside the achievements: the Napoleonic Wars cost "
     "millions of lives across Europe; he built an 'unprecedentedly efficient surveillance system' "
     "with press censorship; and in 1802 he ordered the reintroduction of slavery in the colonies, "
     "reversing the Revolution's abolition, for commercial and strategic gain. Roberts contests the "
     "proto-Hitler caricature, but the debits are real and must not be glorified.",
     "Judge powerful figures (and yourself) with the full ledger: the admirable capabilities do not "
     "cancel the human cost, and ambition pursued without ethical limit produces real harm. Keep the "
     "moral accounting honest.",
     "An ethics lens for BJ: separate the transferable craft (energy, system-building) from the moral "
     "cost of the conquest it served; admire the method without laundering the harm. The patterns are "
     "decision-support, NOT an endorsement of the man's worst acts. Held interpretively.",
     ["to reintroduce slavery", "unprecedentedly efficient surveillance system"],
     ["human-cost", "authoritarianism", "moral-accounting", "ethics", "napoleon", "modern-command"]),
    # ---------- synthesis · 1 ----------
    ("Synthesis: the modern-command pattern and the optionality guardrail",
     "operator-doctrine",
     "Napoleon: A Life yields a portable modern-command pattern, energy and focus, command of "
     "detail, logistics-first foundations, concentration on the decisive point, recognition as "
     "motivation, and durable institution-building, paired with its stark counter-lesson: the same "
     "drive, unchecked by the discipline to stop or relinquish, produced over-reach (Russia, the "
     "Continental System), authoritarianism, and collapse. The admirable method is separable from "
     "the conquest and harm it served.",
     "Mine the modern-command pattern (energy, system, tempo, recognition, durable institutions) for "
     "transferable judgment, while holding the over-reach, ego, and collapse as the cautionary "
     "counter-lesson; the value is sharpened operator judgment, decoupled from conquest and empire.",
     "This synthesizes the lane for BJ: a build-the-system-and-the-people toolkit held as decision-"
     "support against CURRENT_OPERATOR_REALITY_BRIEF, with the over-reach material as the explicit "
     "cautionary counter-case, NOT a directive to copy Napoleon, seek conquest or status, or build "
     "an empire; photography remains one option among several; no final SNIPED / SNIPED Media / "
     "BASEPLATE direction is set.",
     ["is my Civil Code", "more glory than is necessary"],
     ["synthesis", "modern-command", "optionality", "operator-doctrine", "napoleon", "modern-command"]),
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
    forb = [d for d in ("military", "politics", "empire", "conquest", "biography",
                        "history", "commander") if d in doms]
    print("forbidden domains present:", forb or "NONE")
    mx = max(len(q.split()) for r in lines for q in r["direct_quotes"])
    print("longest quote words:", mx)


if __name__ == "__main__":
    main()
