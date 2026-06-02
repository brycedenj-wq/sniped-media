#!/usr/bin/env python3
"""Author ONWARD_TURNAROUND chunks (single source: Onward, Howard Schultz).

12-field canonical schema. batch_id ONWARD_TURNAROUND. chunk_id ONWARD_TURNAROUND_NNN.
Single source -> source_file onward_schultz.txt. Existing domains only (no new domain).
Short illustrative quotes only (copyright-safe). Em-dash swept to ' · ' defensively.
Every chunk references CURRENT_OPERATOR_REALITY_BRIEF; the closing chunk makes the
identity-optionality guardrail explicit (turnaround patterns are decision-support lenses
only, NOT a directive that BJ return to old SNIPED Media or revive an old brand).
"""
import json
import os

REPO = os.path.expanduser("~/AI-Brain-Refinery")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/ONWARD_TURNAROUND_CHUNKS.jsonl")

TITLE = "Onward: How Starbucks Fought for Its Life without Losing Its Soul"
AUTHOR = "Howard Schultz, Joanne Gordon"
SRC = "onward_schultz.txt"
BID = "ONWARD_TURNAROUND"

# Shared guardrail tail appended to every sniped_relevance value.
GUARD = (
    " Held as a decision-support / pattern-library lens read against "
    "CURRENT_OPERATOR_REALITY_BRIEF, not a directive: BJ is in early ideation/build, "
    "not recovering a scaled company, so this is not a cue to return to old SNIPED Media "
    "or revive an old brand. Does not finalize SNIPED, SNIPED Media, or BASEPLATE "
    "direction; photography remains one option among several."
)

chunks = [
    {
        "concept": "Diagnosing what broke after growth: the commoditization drift",
        "domain": "systems-thinking",
        "summary": (
            "By 2007 Starbucks had begun to fail itself. No single bad decision was to "
            "blame; the damage was slow, quiet, and incremental, like a loose thread "
            "unraveling a sweater. Obsessed with growth, the company took its eye off "
            "operations and drifted from its core. Schultz named it in an internal memo, "
            "'The Commoditization of the Starbucks Experience,' arguing the decisions that "
            "took the chain from 1,000 to 13,000 stores had watered down the product."
        ),
        "usable_principle": (
            "Decline after scale is usually systemic and incremental, not a single failure. "
            "Diagnose the whole system and name the root cause (growth obsession crowding out "
            "the core) before reaching for fixes; symptoms mislead."
        ),
        "sniped_relevance": (
            "The operator's diagnostic discipline: when something underperforms, look for the "
            "slow accumulation of small compromises and the root driver, not one culprit. A "
            "lens for how BJ should audit any system or offer he builds for quiet drift."
        ),
        "direct_quotes": ["\"the watering down of the Starbucks Experience\""],
        "tags": ["root-cause", "drift", "scale", "diagnosis", "commoditization", "turnaround"],
    },
    {
        "concept": "The founder return: re-taking daily control to repair what you built",
        "domain": "founder-psychology",
        "summary": (
            "Schultz had stepped down as CEO in 2000 to become chairman. Watching the "
            "company sink, he concluded that without daily control of the business he was "
            "powerless to stop it, and in January 2008 he surprised many by returning as "
            "CEO. 'Starbucks is in my blood,' he wrote; letting it unravel was not an "
            "option. The return carried the personal weight of a founder accountable for "
            "problems the company had created on his watch as chairman."
        ),
        "usable_principle": (
            "A founder's identity is fused with the thing they built, which is both the fuel "
            "for a turnaround and its hazard. Repair often requires re-taking hands-on control "
            "rather than steering from a distance."
        ),
        "sniped_relevance": (
            "The founder-identity intensity that powers a rescue is the same intensity to watch "
            "in oneself. Relevant to how tightly BJ couples his identity to any venture, and "
            "the difference between strategic distance and hands-on operating control."
        ),
        "direct_quotes": ["\"Starbucks is in my blood\""],
        "tags": ["founder-return", "ownership", "accountability", "identity", "control"],
    },
    {
        "concept": "Resetting standards in public: closing 7,100 stores to retrain",
        "domain": "operator-process",
        "summary": (
            "On a Tuesday in February 2008 Starbucks closed all 7,100 US stores for an "
            "afternoon to retrain 135,000 baristas to pour espresso. It cost millions in "
            "sales and was a public admission that the product was no longer good enough, "
            "a risk no retailer had taken. Schultz judged the admission worth it: 'without "
            "great coffee, we have no reason to exist.' The closure dramatized a standards "
            "reset rather than merely announcing one."
        ),
        "usable_principle": (
            "Restoring standards sometimes requires a costly, visible act that signals "
            "seriousness internally and externally. A credible quality reset is dramatized, "
            "not memo'd; you accept short-term pain and public exposure to re-anchor the core."
        ),
        "sniped_relevance": (
            "Standards as the non-negotiable core: when quality slips, an operator may need a "
            "decisive, visible reset rather than incremental tweaks. A lens on how BJ defines "
            "and defends the irreducible standard of whatever he ships."
        ),
        "direct_quotes": ["\"without great coffee, we have no reason to exist\""],
        "tags": ["standards", "quality-reset", "execution", "bold-move", "signal"],
    },
    {
        "concept": "Repairing brand trust by restoring the experience",
        "domain": "brand",
        "summary": (
            "Schultz traced lost brand magic to small erosions: too-tall automatic espresso "
            "machines that hid the barista's craft and killed theater, the smell of warmed "
            "sandwiches overwhelming coffee aroma, a diluted store ambiance. Repair meant "
            "restoring 'the romance' and the third place, reintroducing craft and aroma "
            "(the Pike Place Roast, even reviving the original brown siren logo) so the "
            "experience, not just the logo, carried the brand."
        ),
        "usable_principle": (
            "Brand trust lives in the texture of the experience, not the marketing. Repairing "
            "it means removing the accreted compromises that quietly degraded the core "
            "experience and re-foregrounding the craft customers can feel."
        ),
        "sniped_relevance": (
            "Brand is the felt experience, not the logo. A lens on how BJ would protect the "
            "experiential core of any offer from efficiency compromises that erode trust over "
            "time."
        ),
        "direct_quotes": ["\"the romance and theater that was in play\""],
        "tags": ["brand-trust", "customer-experience", "craft", "third-place", "repair"],
    },
    {
        "concept": "The Transformation Agenda: a galvanizing, actionable framework",
        "domain": "strategy",
        "summary": (
            "Rather than apologize or cast blame, Schultz introduced a Transformation Agenda: "
            "'Transformation' signaled the scale of change with a positive connotation, "
            "'Agenda' gave an actionable framework. It began as three near-term strategic "
            "pillars (fix the US business as the burning platform, reignite emotional "
            "attachment, make long-term changes) and grew into a comprehensive, "
            "easy-to-understand plan that leaned forward with concrete strategies."
        ),
        "usable_principle": (
            "A turnaround needs a named, forward-leaning framework that balances honesty about "
            "problems with concrete action, sequenced from the burning platform outward. The "
            "naming itself creates immediacy and shared direction."
        ),
        "sniped_relevance": (
            "Naming and sequencing change is itself a leadership act. A lens on how BJ frames "
            "any pivot: lead with a concrete, forward agenda anchored on the most urgent "
            "constraint, not a backward-looking post-mortem."
        ),
        "direct_quotes": ["\"our own version of the Transformation Agenda\""],
        "tags": ["strategy", "framework", "burning-platform", "sequencing", "transparency"],
    },
    {
        "concept": "Focus as discipline: closing 600 stores and slowing growth",
        "domain": "operator-doctrine",
        "summary": (
            "Fixing the US stores was the burning platform (about 70 percent of revenue). "
            "Starbucks immediately slowed new-store openings and resolved to close roughly "
            "600 underperforming US locations with the consequent layoffs, something it had "
            "never done at scale. Schultz weighed the human and reputational fallout but "
            "judged that disciplined contraction and focus on existing stores were required "
            "to restore store-level economics and execution."
        ),
        "usable_principle": (
            "Recovery often means subtraction: deliberately slowing growth and cutting the "
            "weakest units to strengthen the core. The discipline of saying no to the growth "
            "reflex is harder, and more important, than expansion."
        ),
        "sniped_relevance": (
            "Focus by subtraction. A lens on how BJ resists the urge to add surfaces and instead "
            "concentrates on the few units or offers that actually carry the economics, "
            "consistent with the lean-operator constraint."
        ),
        "direct_quotes": ["\"This was our burning platform\""],
        "tags": ["focus", "subtraction", "store-closures", "discipline", "saying-no"],
    },
    {
        "concept": "Innovating from the core: VIA and the rewards platform",
        "domain": "commercial-architecture",
        "summary": (
            "Mid-turnaround Starbucks still built new revenue platforms, but only ones "
            "relevant to the core and values. VIA Ready Brew (years of R&D under Don "
            "Valencia) aimed to create a new premium instant-coffee category from a position "
            "of brand credibility: 'Why not?' The company also finally launched a customer "
            "rewards program off the Starbucks Card. New growth platforms had to be "
            "consistent with the heritage of the company, not random line extensions."
        ),
        "usable_principle": (
            "Even in a turnaround, growth comes from new platforms that extend the core asset "
            "into adjacent categories, not from off-brand extensions. Brand credibility lets "
            "you redefine a category others left mediocre."
        ),
        "sniped_relevance": (
            "New revenue should extend the core competence and brand, not chase unrelated "
            "categories. A lens on how BJ evaluates which adjacent offers genuinely compound "
            "his real skills versus dilute them."
        ),
        "direct_quotes": ["\"Why not?\""],
        "tags": ["innovation", "category-creation", "adjacency", "revenue-platform", "VIA"],
    },
    {
        "concept": "Plan B: permanent cost discipline and Lean operations",
        "domain": "operator-process",
        "summary": (
            "As the 2008 financial crisis hit, the board urged Starbucks to 'go deep' on "
            "costs. The team rebuilt unit economics: roughly $25 million from waste, $75 "
            "million from labor reshaped (not just cut) via Lean techniques that streamlined "
            "baristas' work and matched labor to traffic, and ultimately about $400 million "
            "in permanent costs. District managers shifted from opening stores to improving "
            "existing ones. Schultz cut costs while still investing in the customer experience."
        ),
        "usable_principle": (
            "Durable turnaround economics come from permanent structural cost change (Lean, "
            "rebuilt unit economics) rather than one-time cuts, and you protect "
            "customer-facing investment even while cutting elsewhere."
        ),
        "sniped_relevance": (
            "Operational renewal is structural, not cosmetic: redesign how work is done and "
            "where money goes. A lens for how BJ would engineer lean, repeatable operations "
            "and protect the few investments that touch the customer."
        ),
        "direct_quotes": ["\"Go deep\""],
        "tags": ["cost-discipline", "lean", "unit-economics", "operations", "plan-b"],
    },
    {
        "concept": "Cultural repair: New Orleans and reconnecting partners",
        "domain": "culture",
        "summary": (
            "Against Wall Street pressure to cancel it, Schultz refused to scrap the 2008 "
            "leadership conference and chose New Orleans, a city still recovering from "
            "Katrina, gathering about 10,000 managers. After layoffs and closures had cost "
            "partners' trust, he believed reconnection had to happen in person, not online, "
            "to restore the emotional capital and shared mission that the stores ran on. "
            "Partners also performed service work in the city."
        ),
        "usable_principle": (
            "After cuts, culture must be actively re-grounded, often in person and at real "
            "cost, because operational fixes fail without the people's renewed belief and "
            "trust. Cultural repair is an operating priority, not a soft extra."
        ),
        "sniped_relevance": (
            "When trust is spent, repair it deliberately and in person. A lens for how BJ would "
            "rebuild relationships with collaborators or a team after hard decisions, treating "
            "trust as load-bearing infrastructure."
        ),
        "direct_quotes": ["\"we chose New Orleans\""],
        "tags": ["culture", "trust", "people", "in-person", "morale", "repair"],
    },
    {
        "concept": "Accountability and emotional resilience under public crisis",
        "domain": "founder-psychology",
        "summary": (
            "Leading through the first quarterly loss in company history and relentless media "
            "scrutiny, Schultz balanced humility about missteps with self-assurance about the "
            "ability to self-correct. He told managers, 'I will hold myself to the highest "
            "level of accountability,' while insisting no one could do it alone. Resilience "
            "meant absorbing public criticism and a falling stock price without abandoning "
            "the plan or the company's purpose."
        ),
        "usable_principle": (
            "Turnaround leadership pairs visible personal accountability with steadiness under "
            "public pressure. You own the missteps openly, hold conviction in the plan, and "
            "share the burden rather than carrying or deflecting it alone."
        ),
        "sniped_relevance": (
            "Emotional resilience and owned accountability are operator skills under scrutiny. "
            "A lens for how BJ would hold a line through setbacks without either false bravado "
            "or capitulation, keeping purpose intact."
        ),
        "direct_quotes": ["\"the highest level of accountability\""],
        "tags": ["accountability", "resilience", "humility", "conviction", "leadership"],
    },
    {
        "concept": "Profit with conscience: fighting for life without losing the soul",
        "domain": "ethics",
        "summary": (
            "Schultz framed the whole turnaround around a tension in the subtitle: fighting "
            "for the company's life without losing its soul. Even while cutting $400 million "
            "and closing stores, he refused to abandon health care for part-time partners, "
            "ethically sourced coffee, fair treatment of farmers, and community commitments, "
            "arguing 'no business can do well for its shareholders without first doing well "
            "by all the people its business touches.'"
        ),
        "usable_principle": (
            "Cost discipline and conscience are not opposites; the hard test of a turnaround is "
            "cutting what is bloated while protecting the values and people commitments that "
            "constitute the company's reason to exist."
        ),
        "sniped_relevance": (
            "An ethics lens on hard operating decisions: define in advance which values and "
            "obligations are non-negotiable so cost pressure does not quietly erode them. "
            "Relevant to how BJ would hold integrity while making lean, hard calls."
        ),
        "direct_quotes": ["\"without losing its soul\""],
        "tags": ["ethics", "values", "conscience", "stakeholders", "integrity"],
    },
    {
        "concept": "The turnaround pattern and the optionality guardrail (synthesis)",
        "domain": "operator-doctrine",
        "summary": (
            "Across Onward a repeatable repair pattern emerges: diagnose the systemic root of "
            "post-scale drift, re-take hands-on control, reset the core standard even at "
            "public cost, focus by subtraction, rebuild unit economics structurally, repair "
            "culture and trust in person, innovate only from the core, and protect the soul "
            "throughout. 'Onward' is the ethos that holds it together: do battle and do "
            "business through uncertainty. This is the closing synthesis chunk."
        ),
        "usable_principle": (
            "A durable turnaround sequence: root-cause diagnosis, hands-on control, standard "
            "reset, focus by subtraction, structural economics, cultural and trust repair, "
            "core-adjacent innovation, and protected values, carried by a resilient operating "
            "ethos."
        ),
        "sniped_relevance": (
            "The pattern is diagnostic scaffolding for evaluating options, explicitly NOT a "
            "script. Schultz's repair-a-mature-company arc is the opposite of BJ's early-build "
            "stage, so the value is the discipline of diagnosis and focus, not the act of "
            "reviving an old brand."
        ),
        "direct_quotes": ["\"Onward\""],
        "tags": ["synthesis", "turnaround-pattern", "optionality", "decision-support", "doctrine"],
    },
]


def sweep(s):
    return s.replace(chr(0x2014), " · ").replace(chr(0x2013), "-")


def main():
    if os.path.exists(OUT):
        raise SystemExit(f"REFUSE: {OUT} already exists (delete to rewrite)")
    lines = []
    for i, c in enumerate(chunks, start=1):
        rec = {
            "chunk_id": f"{BID}_{i:03d}",
            "batch_id": BID,
            "source_title": TITLE,
            "source_file": SRC,
            "author": AUTHOR,
            "domain": c["domain"],
            "concept": c["concept"],
            "summary": c["summary"],
            "usable_principle": c["usable_principle"],
            "sniped_relevance": c["sniped_relevance"] + GUARD,
            "direct_quotes": c["direct_quotes"],
            "tags": c["tags"],
        }
        # em-dash sweep across all string fields and string-list fields
        for k, v in rec.items():
            if isinstance(v, str):
                rec[k] = sweep(v)
            elif isinstance(v, list):
                rec[k] = [sweep(x) if isinstance(x, str) else x for x in v]
        lines.append(json.dumps(rec, ensure_ascii=False))
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"wrote {len(lines)} chunks -> {OUT}")


if __name__ == "__main__":
    main()
