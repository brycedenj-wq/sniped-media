---
name: os-engagement
description: >
  Run the OS Engagement Protocol: whole-read and distill source docs with proven
  coverage, extract skills, journal decision-deltas, and update the engagement
  dashboard. Use when Bryce says "engage the OS," "run the engagement protocol,"
  "process the next docs," "read the next batch," or asks to advance OS coverage
  before a major strategy question. The standing mission until every source doc is
  read. Protocol: /00_COMMAND_CENTER/OS_ENGAGEMENT_PROTOCOL.md
metadata:
  type: workflow
---

# OS Engagement

Fully engage the OS, one whole-read batch at a time, with proven coverage. No sampling-as-read. No judging importance by title. Protect optionality: this builds the machine, it does not pick the operator's identity.

## State files (00_COMMAND_CENTER)
- `OS_ENGAGEMENT_MANIFEST.csv` , every doc, class (source/derivative/skill), status. The queue and the truth.
- `OS_ENGAGEMENT_DASHBOARD.md` , live counts and percent engaged.
- `OS_ENGAGEMENT_JOURNAL.md` , append-only decision-delta per doc.
- `OS_ENGAGEMENT_PROTOCOL.md` , the standard.

## The batch loop
1. **Pull queue.** From the manifest, take the next N `SOURCE` docs with status `not_read`, sequenced (operating/brief/command-center first, then brand/strategy/transcripts, then canon books, then the rest). Sequencing is not importance; nothing is skipped.
2. **Whole-read.** One agent per doc (or a small bundle), read every line. Segment any doc bigger than one context window; log a coverage line ("read lines 1 to N").
3. **Distill** each doc into a doctrine artifact: what it teaches; what applies to SNIPED / Baseplate / cash / brand / AI; what is rejected; skill candidates; master-doctrine delta.
4. **Extract skills** from any repeatable workflow.
5. **Journal** the decision-delta (what changed, or why nothing did) to `OS_ENGAGEMENT_JOURNAL.md`.
6. **Update** the manifest status to `read` + coverage %, and the dashboard counts.
7. **Roll up** periodically into the master doctrine.

## Throughput
~30 to 50 docs per batch (bundled), or ~350k to 500k words per whole-read run. The 1,145 text sources are ~25 to 40 batches; the 1,216 books are a paced long campaign. Report honest percent engaged every batch.

## Hard rules
- A doc is "used" only if the manifest proves it was read in whole. Preview != read.
- Distill to usable doctrine, never a chunk graveyard.
- Do not let the engine force one identity or lane; surface possibilities, let proof decide.
