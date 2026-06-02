#!/usr/bin/env python3
"""Write OPERATING_FOUNDER_OPERATIONS_CHUNKS.jsonl from the 4 curated systems/process books.

The Goal (Goldratt) + Reengineering the Corporation (Hammer/Champy) + The E-Myth Revisited
(Gerber) + Built to Sell (Warrillow). 12-field canonical schema. Existing domains only
(operator-process / operator-doctrine / systems-thinking / strategy / commercial-architecture /
founder-psychology). NO new domain (startup / entrepreneurship / founder / business /
operations / scaling / product-development NOT created or used). CURATED representative
operations/operator-system pattern extraction, NOT a chapter-by-chapter business-book
summary. Held as transferable operating systems for BJ's actual build-mode stage, NOT a
directive that BJ become a startup founder, VC-style operator, software CEO, agency owner,
franchise owner, or sellable-business flipper, and NOT a mandate to raise VC, hyperscale,
build software, franchise everything, or optimize the soul out of the work. Bible held
separately and untouched. Every chunk carries the CURRENT_OPERATOR_REALITY_BRIEF reference
+ identity-optionality guardrail (GUARD). Em-dash swept. No master-file writes.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "OPERATING_FOUNDER_OPERATIONS_CHUNKS.jsonl"
BATCH = "OPERATING_FOUNDER_OPERATIONS"

GOAL = ("The Goal", "Eliyahu M. Goldratt", "the_goal_goldratt.txt")
REE = ("Reengineering the Corporation", "Michael Hammer and James Champy", "reengineering_hammer_champy.txt")
EMYTH = ("The E-Myth Revisited", "Michael E. Gerber", "emyth_revisited_gerber.txt")
BTS = ("Built to Sell", "John Warrillow", "built_to_sell_warrillow.txt")

GUARD = (" Held as an operating / founder operations pattern-library lens, read against "
         "CURRENT_OPERATOR_REALITY_BRIEF: a transferable model of operating systems (constraints, "
         "process design, work-on-the-business, owner-independence), NOT a directive that BJ become a "
         "startup founder, a VC-style operator, a software CEO, an agency owner, a franchise owner, or "
         "a sellable-business flipper, and NOT a mandate to raise venture capital, hyperscale, build "
         "software, franchise everything, or optimize the soul out of the work. The methods are "
         "decoupled from the manufacturing/small-business context that produced them and applied to "
         "BJ's actual build-mode stage. The Bible remains held separately and untouched. No final "
         "SNIPED, SNIPED Media, or BASEPLATE direction is set here; photography remains one option "
         "among several.")

# (source_tuple, concept, domain, summary, usable_principle, sniped_relevance_core, [quotes], [tags])
ROWS = [
    # ---------- The Goal · 4 + synthesis ----------
    (GOAL,
     "Know the goal and its measures: throughput, inventory, operational expense",
     "operator-doctrine",
     "Goldratt's first move is brutal clarity about the objective: 'the goal of a manufacturing "
     "organization is to make money,' and everything else is a means. He reduces it to three "
     "measures, throughput (the rate the system generates money through sales), inventory (money "
     "tied up), and operational expense (money spent to turn inventory into throughput), and judges "
     "every action by whether it moves those.",
     "Define the single real goal and the few measures that actually track it, then judge every "
     "action against those measures rather than against local busyness or proxy metrics.",
     "A clarity lens for BJ: name the one real goal of the work and the few numbers that actually "
     "track it (money in, money tied up, money spent), and judge activity against those, not against "
     "feeling busy. Held interpretively.",
     ["the goal is to make money", "throughput, inventory, operational expense"],
     ["goal-clarity", "throughput", "measures", "operator-doctrine", "the-goal", "operating-founder-operations"]),
    (GOAL,
     "Dependent events and statistical fluctuations: the chain underperforms its parts",
     "systems-thinking",
     "The Goal's core insight is that 'dependent events' (steps that must happen in sequence) "
     "combined with 'statistical fluctuations' (normal variation in each step) cause a system to "
     "deliver less than the sum of its parts: delays accumulate and gains do not, so a chain of "
     "good performers still underperforms. Local efficiency is not system performance.",
     "In any chain of dependent steps with variation, the system delivers less than the parts "
     "suggest because delays accumulate while early gains are lost; optimize the whole flow, not "
     "each step.",
     "A systems lens for BJ: a workflow of dependent steps (capture, edit, deliver) underperforms "
     "the sum of its fast parts because variation and waiting compound; manage the end-to-end flow, "
     "not each step's local speed. Held interpretively.",
     ["dependent events", "statistical fluctuations"],
     ["dependent-events", "variation", "flow", "systems-thinking", "the-goal", "operating-founder-operations"]),
    (GOAL,
     "The constraint governs throughput: an hour lost at the bottleneck is lost for the whole system",
     "systems-thinking",
     "Goldratt shows the system's output is set by its single binding constraint (the bottleneck): "
     "'an hour lost at a bottleneck is an hour out of the entire system,' while an hour saved at a "
     "non-bottleneck is a mirage. The constraint, not effort everywhere, determines what the whole "
     "produces.",
     "Find the one binding constraint that actually limits output and protect/improve it; effort "
     "spent anywhere else feels productive but does not increase what the system delivers.",
     "A leverage lens for BJ as a solo operator: identify the one true bottleneck in the work (often "
     "your own time/attention) and protect it; speeding up everything else is wasted motion if the "
     "constraint is untouched. Held interpretively.",
     ["an hour lost at a bottleneck"],
     ["constraint", "bottleneck", "leverage", "systems-thinking", "the-goal", "operating-founder-operations"]),
    (GOAL,
     "The five focusing steps: a process of ongoing improvement",
     "operator-process",
     "Goldratt's theory of constraints reduces to a repeatable cycle: identify the constraint, decide "
     "how to exploit it (wring maximum output from it), subordinate everything else to that decision, "
     "elevate the constraint (add capacity), and then repeat, because the constraint moves. "
     "Improvement is a continuous loop focused on whatever currently limits the system.",
     "Run the constraint-focused improvement loop (identify, exploit, subordinate, elevate, repeat) "
     "rather than improving everything at once; the bottleneck always moves, so improvement is "
     "ongoing, not one-time.",
     "An improvement-process lens for BJ: repeatedly find the current limiting step, get the most out "
     "of it, organize the rest around it, then expand it, and re-check, instead of scattering "
     "improvement effort everywhere. Held interpretively.",
     ["exploit the bottlenecks", "Subordinate everything else"],
     ["five-focusing-steps", "theory-of-constraints", "ongoing-improvement", "operator-process", "the-goal", "operating-founder-operations"]),
    # ---------- Reengineering the Corporation · 3 ----------
    (REE,
     "Reengineering: fundamental rethinking and radical redesign for dramatic improvement",
     "operator-process",
     "Hammer and Champy define reengineering as 'the fundamental rethinking and radical redesign of "
     "business processes to achieve dramatic improvements' in cost, quality, service, and speed. It "
     "is deliberately not incremental: dramatic improvement, they argue, 'demands blowing up the "
     "old' rather than tuning it.",
     "When a process is fundamentally broken, redesign it from the ground up for a step-change rather "
     "than tuning the existing one; incremental fixes to a bad design only entrench it.",
     "A redesign lens for BJ: when a workflow is fundamentally inefficient, rethink it from scratch "
     "for a step-change rather than optimizing the broken version; reserve this for processes that "
     "are genuinely broken, not everything. Held interpretively.",
     ["fundamental rethinking and radical redesign", "blowing up the old"],
     ["reengineering", "radical-redesign", "step-change", "operator-process", "reengineering", "operating-founder-operations"]),
    (REE,
     "Process orientation: organize work around outcomes, not tasks",
     "operator-process",
     "The central reengineering shift is from task/function thinking to process thinking: 'work is "
     "best organized around outcomes' and end-to-end processes, not fragmented departmental tasks. "
     "Hammer's blunt slogan, 'Don't automate, obliterate,' warns against speeding up a broken "
     "process instead of redesigning it around the outcome the customer actually wants.",
     "Organize work around the end-to-end outcome the customer wants, not around handoffs between "
     "specialized tasks; and do not automate a broken process, redesign it around the outcome first.",
     "A process lens for BJ: design the whole client journey around the outcome (a delivered result) "
     "rather than around disconnected steps, and fix the design before adding tools/automation on "
     "top of a broken flow. Held interpretively.",
     ["organized around outcomes", "Don't Automate, Obliterate"],
     ["process-orientation", "outcomes", "anti-automation-of-waste", "operator-process", "reengineering", "operating-founder-operations"]),
    (REE,
     "The clean-sheet test: redesign from the outcome, not the legacy",
     "strategy",
     "Reengineering insists on disregarding existing structures and procedures, asking 'if I were "
     "recreating this today, given what I know and the technology I have, what would it look like?' "
     "rather than paving the existing cow path. The discipline is to design from the desired outcome "
     "backward, not forward from how things are currently done.",
     "Periodically ask the clean-sheet question (if I were starting this today from scratch, how "
     "would I do it?) and design backward from the outcome, rather than inheriting the current way by "
     "default.",
     "A first-principles lens for BJ: periodically redesign a workflow as if starting fresh today "
     "(given current tools/AI) instead of inheriting how it has always been done; design from the "
     "outcome backward. Held interpretively.",
     ["blowing up the old"],
     ["clean-sheet", "first-principles", "outcome-backward", "strategy", "reengineering", "operating-founder-operations"]),
    # ---------- The E-Myth Revisited · 3 ----------
    (EMYTH,
     "Work ON your business, not IN it",
     "operator-doctrine",
     "Gerber's central prescription: the owner must 'go to work on your business rather than in it,' "
     "spending time building the system that does the work rather than only doing the work. The "
     "business is the product to be engineered; doing the technical work yourself all day is what "
     "keeps a small operation stuck and owner-dependent.",
     "Reserve deliberate time to build the system that does the work (working ON it), not only to do "
     "the work (working IN it); otherwise you stay the bottleneck and the operation cannot grow "
     "beyond your hours.",
     "A leverage lens for BJ as a solo operator: protect time to build repeatable systems (templates, "
     "workflows, the backend) rather than spending every hour doing the deliverable, so the work is "
     "not permanently capped by your hands. Held interpretively.",
     ["Working On Your Business", "rather than in it"],
     ["work-on-not-in", "systematize", "owner-leverage", "operator-doctrine", "e-myth", "operating-founder-operations"]),
    (EMYTH,
     "The Fatal Assumption: being good at the work is not running the business",
     "founder-psychology",
     "Gerber names 'the Fatal Assumption': the technician who is excellent at the craft assumes that "
     "because he understands the technical work, he can run a business that does that work. The two "
     "are different skills; the assumption traps the owner in a job that owns him. He frames the "
     "owner as three people in conflict, Technician, Manager, and Entrepreneur.",
     "Being excellent at the craft is a different skill from building the business around it; "
     "recognize the Technician/Manager/Entrepreneur split in yourself and deliberately develop the "
     "roles the craft alone does not teach.",
     "A self-awareness lens for BJ: skill at the craft (the photography, the engineering) is not the "
     "same as building the operating system around it; consciously work the manager/builder roles, "
     "not only the technician role, so the work does not enslave you. Held interpretively.",
     ["the Fatal Assumption"],
     ["fatal-assumption", "technician-trap", "roles", "founder-psychology", "e-myth", "operating-founder-operations"]),
    (EMYTH,
     "The franchise prototype: build it as if it must run without you",
     "operator-process",
     "Gerber's thinking tool is the 'Franchise Prototype': design the operation as if it had to be "
     "replicated as a turn-key system that runs predictably without the founder present, documenting "
     "how every part works. He stresses the genius is the Business Format Franchise (the system), not "
     "franchising itself; the point is a systematized, owner-independent operation.",
     "Build the operation as a documented, turn-key system that could in principle run without you, "
     "even if you never replicate it; systematizing for owner-independence is the goal, not "
     "franchising per se.",
     "A systems lens for BJ: design the work as if it had to run without you (documented workflows, "
     "repeatable standards), which frees and de-risks the operation, held strictly as a thinking "
     "tool, NOT a directive to actually franchise. Held interpretively.",
     ["the Franchise Prototype"],
     ["franchise-prototype", "turn-key", "owner-independence", "operator-process", "e-myth", "operating-founder-operations"]),
    # ---------- Built to Sell · 3 ----------
    (BTS,
     "Owner-independence: build a business that runs without you (a job vs an asset)",
     "commercial-architecture",
     "Warrillow's thesis: the most valuable, 'sellable business' is one that runs 'without you,' the "
     "owner. A business utterly dependent on the founder is really a job, not an asset; designing for "
     "owner-independence is what turns effort into something that has standalone value, whether or "
     "not it is ever sold.",
     "Design so the operation can run without you; owner-independence is what converts a job into an "
     "asset with standalone value, valuable in itself even if a sale never happens.",
     "An asset lens for BJ: build toward an operation that does not depend on you personally for "
     "every outcome, because that is the difference between owning a job and owning something with "
     "value, read as build-quality, NOT a directive to flip a business. Held interpretively.",
     ["a sellable business", "without you"],
     ["owner-independence", "asset-vs-job", "standalone-value", "commercial-architecture", "built-to-sell", "operating-founder-operations"]),
    (BTS,
     "Specialize and productize: one teachable, repeatable service",
     "strategy",
     "Warrillow's path to owner-independence is to specialize in one thing done well, turn it into a "
     "standardized, teachable, repeatable process, and say no to off-process work. A generic "
     "do-everything shop is unsellable and owner-dependent; a specialized, productized service "
     "becomes referable, scalable, and runnable by others.",
     "Specialize in one thing and turn it into a standardized, teachable, repeatable process, saying "
     "no to off-process work; a productized specialty is referable and runnable without the founder, "
     "where a generic do-everything offering is not.",
     "A focus lens for BJ: a specialized, productized offering (one thing, done to a documented "
     "standard) is more referable and less owner-dependent than a do-anything service; saying no to "
     "off-process work is the cost of that focus. Held interpretively.",
     ["specialize", "say no to other work"],
     ["specialize", "productize", "standardized-service", "strategy", "built-to-sell", "operating-founder-operations"]),
    (BTS,
     "Recurring revenue and standardized process: the architecture of a durable operation",
     "commercial-architecture",
     "Warrillow stresses building recurring revenue (predictable, repeat income you can count on) on "
     "top of a standardized service process, so the operation has stable cash flow and does not "
     "restart from zero each month. Predictable revenue plus a documented process is the financial "
     "and operating backbone of a business that is durable and not founder-fragile.",
     "Engineer for predictable, recurring revenue on top of a standardized process, so the operation "
     "does not reset to zero each cycle and is not fragile to the founder's continuous selling.",
     "A durability lens for BJ: favor structures that produce predictable, recurring income on a "
     "standardized process (retainers, repeat work, productized packages) over one-off scrambles, so "
     "the operation is stable rather than month-to-month fragile. Held interpretively.",
     ["recurring revenue", "standardized your service"],
     ["recurring-revenue", "predictable-income", "operating-backbone", "commercial-architecture", "built-to-sell", "operating-founder-operations"]),
    # ---------- synthesis · 1 ----------
    (GOAL,
     "Synthesis: the operations toolkit and the optionality guardrail",
     "operator-doctrine",
     "The four books yield one operations toolkit: get brutally clear on the goal and find the single "
     "constraint that limits it (Goldratt), redesign the process from the outcome backward rather "
     "than tuning the broken version (Hammer/Champy), work ON the system so the operation is not "
     "owner-trapped (Gerber), and build owner-independence on a standardized, recurring-revenue "
     "process (Warrillow). It is held as an interpretive operating toolkit, NOT a command to "
     "franchise, flip, or optimize the soul out of the work.",
     "Combine constraint-focus, outcome-backward process redesign, work-on-the-system, and "
     "owner-independence into one operating toolkit, held as decision-support and decoupled from the "
     "manufacturing/small-business context that produced it.",
     "This synthesizes the lane for BJ: a portable operations toolkit (find the constraint, redesign "
     "from the outcome, build systems so the work is not capped by your hands, design for "
     "owner-independence and recurring revenue) held as decision-support against "
     "CURRENT_OPERATOR_REALITY_BRIEF, NOT a directive to franchise, flip a business, hyperscale, or "
     "optimize the soul out of the craft; photography remains one option among several; no final "
     "SNIPED / SNIPED Media / BASEPLATE direction is set.",
     ["the goal is to make money", "one option among several"],
     ["synthesis", "operations-toolkit", "optionality", "operator-doctrine", "the-goal", "operating-founder-operations"]),
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
    lines = []
    for i, (src, concept, domain, summary, principle, relevance, quotes, tags) in enumerate(ROWS, 1):
        title, author, sfile = src
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
    forb = [d for d in ("startup", "entrepreneurship", "founder", "business",
                        "operations", "scaling", "product-development") if d in doms]
    print("forbidden domains present:", forb or "NONE")
    mx = max(len(q.split()) for r in lines for q in r["direct_quotes"])
    print("longest quote words:", mx)


if __name__ == "__main__":
    main()
