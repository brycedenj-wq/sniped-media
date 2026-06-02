#!/usr/bin/env python3
"""Write DECISION_JUDGMENT_COGNITION_CHUNKS.jsonl · 12 curated chunks from the 2 net-new sources.
Existing domains only · decision-making anchor · no new domain. Em-dash swept + asserted."""
import json, os

ROOT = "/Users/sniper/AI-Brain-Refinery"
OUT = os.path.join(ROOT, "01_KNOWLEDGE_BASE/batches/DECISION_JUDGMENT_COGNITION_CHUNKS.jsonl")
EXTRACT = "01_KNOWLEDGE_BASE/batches/decision_judgment_cognition_extracted"
DASH = chr(0x2014)
BATCH = "DECISION_JUDGMENT_COGNITION"

TFS = ("Thinking, Fast and Slow", "Daniel Kahneman", "thinking_fast_and_slow_kahneman.txt")
NOISE = ("Noise: A Flaw in Human Judgment", "Daniel Kahneman, Olivier Sibony, Cass R. Sunstein", "noise_kahneman_sibony_sunstein.txt")

GUARD = (
    " Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support / pattern-library only, "
    "NOT doctrine and NOT a directive. NOT a directive that BJ become a quant, a rationalist, a behavioral economist, "
    "an investor, or a decision-theory guru. The biases, noise, and judgment-hygiene methods are translated into practical "
    "judgment hygiene, decision process, error-reduction, and operator-awareness patterns for BJ's actual build-mode stage. "
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
    # ---- Thinking, Fast and Slow (Kahneman) · 7 ----
    C(1, TFS, "decision-making",
      "The two systems: fast intuitive System 1, slow effortful System 2",
      "Kahneman models the mind as two systems: System 1 is fast, automatic, associative, and always on (it generates impressions and intuitions); System 2 is slow, effortful, and deliberate but lazy, so it usually endorses System 1's suggestions rather than checking them. Most errors are System 1 jumping to a confident answer that System 2 fails to audit.",
      "Treat your first confident answer as a System 1 draft, not a verdict; deliberately engage System 2 on decisions that matter.",
      "Helps BJ notice when a quick, confident read (of a client, an opportunity, a price) is System 1 and deserves a deliberate second pass before he commits.",
      ["System 1", "System 2", "The Lazy Controller"],
      ["decision-judgment-cognition", "thinking-fast-and-slow", "kahneman", "two-systems", "intuition", "deliberation"]),
    C(2, TFS, "decision-making",
      "Substitution and WYSIATI: answering an easier question on the evidence at hand",
      "When facing a hard question, System 1 quietly substitutes an easier one and answers that instead. It also operates on WYSIATI (what you see is all there is): it builds the most coherent story from available evidence and ignores what is missing, producing confidence that tracks coherence, not completeness.",
      "Ask 'what question am I actually answering?' and 'what evidence is missing?'; confidence built on a tidy story is not evidence of truth.",
      "Reminds BJ that a confident judgment formed from the few facts in front of him (a single client signal, one good shoot) may be substituting an easy question and ignoring absent data.",
      ["What You See is All", "what you see is all"],
      ["decision-judgment-cognition", "thinking-fast-and-slow", "kahneman", "substitution", "wysiati", "coherence"]),
    C(3, TFS, "mental-models",
      "Anchoring: estimates pulled toward whatever number is in view",
      "Any number present before a judgment (even an arbitrary or irrelevant one) drags the estimate toward it. Anchors operate through both deliberate adjustment (insufficient) and System 1 priming, and they work even when people know the anchor is meaningless.",
      "Set the anchor when you can (name your number first); when receiving one, deliberately discard it and estimate from scratch.",
      "Useful for BJ on pricing and negotiation: the first number framed (his rate, a budget mentioned) anchors the whole conversation, so he should set it intentionally rather than react to theirs.",
      ["anchoring"],
      ["decision-judgment-cognition", "thinking-fast-and-slow", "kahneman", "anchoring", "estimation", "pricing-input"]),
    C(4, TFS, "mental-models",
      "Availability, representativeness, and the law of small numbers",
      "System 1 judges probability by ease of recall (availability: vivid or recent events feel more likely) and by resemblance to a stereotype (representativeness), ignoring how common things actually are. The law of small numbers is the tendency to over-trust patterns in tiny samples as if they were real signal.",
      "Distrust judgments driven by what is vivid or what 'fits the type'; ask for the actual frequency and the sample size behind a pattern.",
      "Helps BJ avoid over-reading a vivid recent win/loss or a striking-but-rare case, and avoid drawing conclusions from one or two data points as if they were a trend.",
      ["availability", "representativeness", "law of small numbers"],
      ["decision-judgment-cognition", "thinking-fast-and-slow", "kahneman", "availability", "representativeness", "small-samples"]),
    C(5, TFS, "mental-models",
      "Base-rate neglect and regression to the mean",
      "People judge specific cases by resemblance and ignore base rates (how common the outcome is in the population), and they invent causal stories for what is really regression to the mean: extreme results are followed by more average ones for statistical, not causal, reasons.",
      "Start from the base rate before adjusting for the specific case; expect extremes to regress, and do not build a causal story around the bounce-back.",
      "Keeps BJ from over-explaining a great or terrible result (a viral post, a dead month) as cause-and-effect when it is partly regression, and from ignoring how often outcomes like the one he is forecasting actually happen.",
      ["base rate", "Regression to the Mean"],
      ["decision-judgment-cognition", "thinking-fast-and-slow", "kahneman", "base-rates", "regression-to-the-mean", "causal-illusion"]),
    C(6, TFS, "decision-making",
      "Prospect theory: loss aversion, reference dependence, and framing",
      "Choices are made relative to a reference point, not absolute states, and losses loom larger than equivalent gains (loss aversion, roughly 2:1). Because outcomes are evaluated as gains or losses from a frame, the same choice framed differently (as a loss avoided vs a gain forgone) flips the decision.",
      "Name the reference point and the frame before deciding; reframe a 'loss' as a cost of a chosen goal so loss aversion does not freeze a sound move.",
      "Helps BJ see when fear of a loss (turning down work, spending on the build) is outweighing an equivalent gain, and how the framing of an offer to a client shifts their yes/no.",
      ["loss aversion", "prospect theory"],
      ["decision-judgment-cognition", "thinking-fast-and-slow", "kahneman", "prospect-theory", "loss-aversion", "framing"]),
    C(7, TFS, "operator-process",
      "Overconfidence and the planning fallacy: take the outside view",
      "The inside view (building a forecast from the specifics of your own plan) produces optimistic, overconfident timelines and budgets, the planning fallacy. The remedy is the outside view: look at the base-rate outcomes of a reference class of similar projects, and run a premortem (imagine the failure and explain it) before committing.",
      "Forecast from the reference class of similar efforts, not from your own optimistic plan; run a premortem before a big commitment.",
      "A direct process tool for BJ's build-mode planning: estimate timelines/costs from how similar solo projects actually went, and premortem big bets before committing time or money.",
      ["the planning fallacy", "overconfidence"],
      ["decision-judgment-cognition", "thinking-fast-and-slow", "kahneman", "planning-fallacy", "outside-view", "premortem"]),
    # ---- Noise (Kahneman/Sibony/Sunstein) · 4 ----
    C(8, NOISE, "decision-making",
      "Noise versus bias: two independent sources of error",
      "Error has two components: bias (systematic deviation, the average judgment is off-target in a consistent direction) and noise (unwanted variability, judgments that should be identical scatter). Both add to total error, but noise is largely invisible and ignored because we examine decisions one at a time. The book's refrain: wherever there is judgment, there is noise.",
      "Diagnose error as bias AND noise; reducing inconsistent scatter matters as much as correcting a consistent lean, and noise hides unless you look across many judgments.",
      "Tells BJ that inconsistency in his own repeated judgments (pricing the same job differently on different days, scattered editing/selection calls) is a real, fixable error source, not just occasional bias.",
      ["there is judgment, there", "noise is variability"],
      ["decision-judgment-cognition", "noise", "kahneman-sibony-sunstein", "noise-vs-bias", "judgment-error", "variability"]),
    C(9, NOISE, "systems-thinking",
      "The components of system noise: level, pattern, and occasion",
      "System noise decomposes into level noise (judges differ in their average severity or generosity), pattern noise (stable idiosyncratic reactions to particular cases, the largest component), and occasion noise (the same judge varies with mood, order, fatigue, even the weather). Together they make a 'system' of judges far noisier than anyone assumes.",
      "When several people (or you on different days) judge the same thing, expect and measure level, pattern, and occasion noise rather than trusting any single read.",
      "For BJ this frames why his own and collaborators' judgments of the same work vary, and why a tired or moody pass is occasion noise, not a new truth, useful when reviewing selects or decisions over time.",
      ["level noise", "pattern noise", "occasion noise"],
      ["decision-judgment-cognition", "noise", "kahneman-sibony-sunstein", "system-noise", "occasion-noise", "variability-components"]),
    C(10, NOISE, "operator-process",
      "The noise audit and decision hygiene",
      "You cannot manage noise you have not measured: a noise audit has independent judges rate the same cases and reveals the hidden scatter. The fix is decision hygiene, prevention rules applied before you know which error you are making, such as sequencing information, using shared scales and guidelines, and structuring the judgment.",
      "Measure noise before fixing it, then apply hygiene (sequence the inputs, use a common scale, structure the call) rather than chasing individual mistakes after the fact.",
      "Gives BJ a practical discipline: define a consistent rubric/scale for recurring judgments (which frames make the cut, how to price a job) so the call is structured, not improvised differently each time.",
      ["decision hygiene", "the noise audit"],
      ["decision-judgment-cognition", "noise", "kahneman-sibony-sunstein", "noise-audit", "decision-hygiene", "process"]),
    C(11, NOISE, "operator-process",
      "Mediating assessments and independent judgment before aggregation",
      "Two of the most powerful hygiene tools: decompose a complex decision into a few independent, fact-based mediating assessments and delay the holistic gut call until the end; and gather judgments independently before any discussion (independent judgment preserves the error-cancelling benefit of aggregation, the wisdom of crowds, which premature discussion destroys).",
      "Break a big call into independent sub-judgments scored separately, hold the intuitive verdict until last, and collect estimates independently before discussing so they can be averaged.",
      "For BJ: when evaluating an opportunity or direction, score a few independent factors before the gut yes/no, and get others' takes independently before group talk so consensus does not just echo the loudest first voice.",
      ["mediating assessment", "independent judgment"],
      ["decision-judgment-cognition", "noise", "kahneman-sibony-sunstein", "mediating-assessments", "independence", "aggregation"]),
    # ---- Synthesis ----
    C(12, TFS, "operator-doctrine",
      "Synthesis: the judgment-hygiene toolkit and the optionality guardrail",
      "Across both books a single decision-support toolkit emerges: know that a fast, confident System 1 drafts most judgments and a lazy System 2 rarely audits them; watch the named biases (anchoring, availability, representativeness, base-rate neglect, regression illusions, loss aversion, overconfidence); separate bias from noise and measure both; and apply decision hygiene (the outside view, structured independent judgments, mediating assessments, aggregation). Held as decision-support, these reduce avoidable error without pretending to make the operator perfectly rational, and without becoming a directive to formalize every choice.",
      "Build a lightweight judgment-hygiene habit: slow down on what matters, name the likely bias, check the base rate and the outside view, structure recurring calls, and gather independent inputs before deciding.",
      "A single decision-support lens for BJ's build-mode judgment that explicitly preserves optionality: apply the hygiene that fits the decision's stakes, ignore the rest, finalize nothing.",
      ["wherever there is judgment", "decision hygiene"],
      ["decision-judgment-cognition", "synthesis", "judgment-hygiene", "error-reduction", "optionality", "operator-doctrine"]),
]

def sweep(o):
    if isinstance(o, str): return o.replace(DASH, " · ")
    if isinstance(o, list): return [sweep(x) for x in o]
    if isinstance(o, dict): return {k: sweep(v) for k, v in o.items()}
    return o

rows = [sweep(r) for r in rows]

assert len(rows) == 12, len(rows)
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
