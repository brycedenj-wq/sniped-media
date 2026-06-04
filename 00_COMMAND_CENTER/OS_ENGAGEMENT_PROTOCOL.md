# THE OS ENGAGEMENT PROTOCOL

The mission is not to build one idea. The mission is to genuinely engage the entire OS, every doc read in whole and distilled, before any "full OS" answer is trusted. Until a doc passes read-and-distill, it does not count as used. No exceptions, no sampling-as-read, no judging importance by title.

Governing principle (above all): **protect optionality. Do not determine the throne before the kingdom exists.** The OS does not decide who the operator is. It builds the machine that lets any direction be tested, and lets identity emerge from proof. (See `feedback_possibility_engine_optionality`.)

---

## THE STANDARD

1. **Inventory everything.** A full manifest of every doc, book, transcript, skill, source folder, and artifact. (Done: `OS_ENGAGEMENT_MANIFEST.csv`, 3,809 doc-type files.)
2. **Read coverage must be proven.** Per doc: word/page count, line or segment range, coverage percent. A doc is not "used" unless the manifest proves it was read.
3. **No sampling claims.** Grep/skim/sample is labeled PREVIEW. It never counts as read, used, or engaged.
4. **Distill, do not chunk-graveyard.** Every fully read doc becomes a usable doctrine artifact: what it teaches, what applies to SNIPED / Baseplate / cash / brand / AI systems, what is rejected, what becomes a skill, what is added to the master doctrine.
5. **Skill extraction.** A repeatable workflow in a doc becomes a skill or SOP, not just a summary.
6. **Master doctrine.** Distilled doctrines roll up into one loadable master doctrine, carried into future answers by default.
7. **Decision journal.** Log what changed because of each doc. If nothing changed, say why.
8. **Only then, major strategy.** Once the OS is genuinely engaged, any big question (money, SNIPED, Baseplate, clothing, product, offer, system) runs through a system that is processed, distilled, routed, and alive, not a slice in costume.

---

## THE PIPELINE (per doc)

```
INVENTORY  -> CLASSIFY (source / derivative / skill)
   derivative (chunk outputs, .bak/.prev, batch extracts, session logs) = SKIP, already generated from a source
   skill = register, do not re-read as prose
   source = QUEUE for whole-read
WHOLE-READ (segment if larger than one context window; every line; coverage line logged)
   -> DISTILL to a doctrine artifact (teaches / applies / rejects / skill-candidate / master-doctrine delta)
   -> EXTRACT any repeatable workflow into a skill
   -> JOURNAL the decision delta (what changed, or why nothing did)
   -> UPDATE manifest status to READ + coverage %, UPDATE dashboard
ROLL UP periodically -> MASTER DOCTRINE
```

Whole-read of a large doc = segment into context-sized pieces, one agent reads each piece completely, a coverage manifest confirms no segment skipped (proven on `new world.docx`: 16/16 segments, lines 1 to ~4201 each).

---

## SCALE AND THROUGHPUT (the honest math)

- SOURCE docs to whole-read: **2,361** (1,145 text docs = ~4.46M words; 1,216 books/binaries = roughly 80M to 100M words).
- The text-doc layer is the tractable near-term campaign. The 1,216-book layer is the long pole and is a sustained burn, not a session.
- One whole-read workflow run handles roughly 350k to 500k words (about 16 segments). At that rate: the text layer is on the order of 10 to 14 runs; the book layer is many dozens of runs and is paced over time.
- Sequencing is NOT importance-judgment. Nothing is skipped. Order is for throughput; every source is eventually read in whole.
- Priority order for sequencing (value of early coverage, not a claim of importance): (1) operating + brief + command-center sources, (2) brand / strategy / transcript sources, (3) the already-summarized canon books (verify the prior distillation against a real whole-read), (4) the remaining book library.

---

## THE DASHBOARD

`OS_ENGAGEMENT_DASHBOARD.md`, updated every batch: total docs, fully read, partially read, not read, doctrines created, skills extracted, gaps found, next docs in queue, percent engaged (by docs and by words). The number stays honest even when it is small. A true 2% beats a fake 100%.

## DECISION JOURNAL

`OS_ENGAGEMENT_JOURNAL.md`, append-only: per doc, the decision delta. The journal is the proof the OS is alive, not just read.
