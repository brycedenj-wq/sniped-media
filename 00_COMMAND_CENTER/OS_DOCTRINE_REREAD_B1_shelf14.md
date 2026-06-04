## RE-READ SHELF 14

---

### BOOK 1: Prompt Template - Problem Decomposition.pdf

**Coverage:** 1/1 segs complete. Teaching material (Skool community), not primary research.

**Thesis:** Matching task shape to decomposition method (linear, plan-first, principle-driven) produces measurable outputs and forces prioritization over open-ended sprawl.

**Densest Frameworks / Lessons:**

1. **Three decomposition methods.** LtM (Linear-to-Modular) for sequential workflows. PaS (Plan-then-Execute) for complex decisions requiring upfront structure. PoTh (Principle-or-Theme) for systems that organize around doctrine rather than steps.
2. **Outputs over process.** Every step in a well-designed prompt delivers a concrete artifact (audience segment, channel list, budget line), not just reasoning.
3. **Constraint-by-count forces priority.** "Three channels, two improvements" eliminates sprawl. Open-ended brainstorming dilutes. Forced count = forced judgment.
4. **Bidirectional prompt structure.** Some tasks front-load planning (PaS); others build from simple to complex (LtM). Mismatch between task shape and method degrades output quality.
5. **Plan-then-Execute mirrors Standing Order loop.** The PaS bifurcation (plan phase produces structure, execute phase produces deliverables) is structurally identical to SNIPED's session-start protocol.

**SNIPED Application:**
- Direction Stack book launch fits a PaS frame: plan phase defines audience + positioning + channel architecture; execute phase runs the calendar.
- Composite environment rotation = PoTh system design, already validated.
- VIB outreach + LinkedIn comment doctrine = LtM execution after prior PaS audience segmentation.
- New revenue lane evaluation (KOTS, Brand System, Op Kit) = financial planning + risk mitigation pattern.
- Any time a task is handed to Claude Code with unclear method, the LtM/PaS/PoTh routing question should be asked first.

**UPDATES / CONTRADICTS:**
- Strengthens `feedback_execution_governor` (action not report). The framework makes explicit that "plan phase" is still action; it is not the report shape.
- No contradiction with existing doctrine. Adds labeling vocabulary for prompt construction that the OS currently lacks.

---

### BOOK 2: Truth, Lies and Advertising (Jon Steel, via Burns review) - Journal of Advertising 1998

**Coverage:** 1/1 segs complete. Book review (not the original Steel text). Burns/UT Austin via Journal of Advertising, Winter 1998.

**Thesis:** Great advertising emerges from treating the audience as an intelligent partner in meaning-making, using the creative brief as inspiration not specification, and synthesizing instinct + data into insight rather than letting research render verdicts.

**Densest Frameworks / Lessons:**

1. **Consumer as Partner.** Audience moves from subject to co-creator. The ad resonates because they feel heard, not because they were targeted. Applies to every casting, DM, and client touchpoint.
2. **Brief as Doorway.** The creative brief's function is to open possibility space for the creative team, not to close it with requirements. Synthesis of thinking, not checklist. A brief that over-specifies kills serendipity.
3. **Serendipity Principle.** "When baiting a trap with cheese, always leave room for the mouse." Constraint enables unexpected solutions; over-specification prevents them. Simplicity over volume is not a style preference, it is a creative mechanics truth.
4. **Insight Generation Loop.** Multiple signal sources (quantitative data + instinct + cultural observation + audience behavior) converge on a fundamental truth. No single source is the verdict. The nugget emerges from the convergence.
5. **Target Intelligence Assumption.** Assume the audience is smart. Their emotional and behavioral interaction with the work is what makes it great, not their demographic bucket.
6. **Research as Tool, Not Verdict.** Burns' correction of Steel: bad methodology is the problem, not methodology itself. Data generates insight; it does not make the decision. Proof-first operating models sit correctly between Steel's gut-only and Burns' quantitative rigor.
7. **"One doesn't have a great strategy until one has a great ad."** Strategy is validated by execution output, not by planning documents. Docs are hypotheses; proof is confirmation.

**SNIPED Application:**
- Direction Stack visual direction docs (Composite Environment Rotation, Lineage Doctrine, Visual Direction LOCK) are briefs-as-doorways. They constrain without killing novelty. Validate them against this standard: do they open or close possibility?
- Casting doctrine + pre-production engagement = consumer-as-partner operationalized. The model trusting the vision IS the trust multiplier.
- Quiet luxury editorial restraint = Serendipity Principle applied. Meisel/Roversi lane is not ascetic preference; it is constraint-enabling-discovery.
- Proof-first doctrine validated. DM quality, scene density, trust signal accumulation = insight loop, not verdict machine.
- Creative direction docs function as briefs. They must inspire the production team, not just satisfy process. Audit every doc: does it move people or check boxes?

**UPDATES / CONTRADICTS:**
- Reinforces `feedback_proof_over_packaging`: strategy confirmed by output, not planning documents.
- Reinforces `feedback_full_os_synthesis_every_answer`: convergence of signal sources beats any single framework.
- Adds a new frame to `intel_trust_mechanics`: consumer/model/client as creative partner (not subject) is a trust multiplier not previously named explicitly.
- Serendipity Principle should be named and added to `feedback_visual_direction_luxury_editorial.md` as the mechanical reason restraint wins.
- No contradiction with existing doctrine. Deepens the trust layer.

---

## CAPABILITY HARVEST

### NEW SKILL CANDIDATES

- **`sniped-prompt-method-router`**: Given a task description, classify it as LtM / PaS / PoTh, output the correct step sequence, and apply constraint-by-count to each step. Invokable at session start or before any complex Claude Code prompt construction.
- **`sniped-brief-audit`**: Pass any SNIPED direction doc (Composite Environment Rotation, Lineage Doctrine, Visual Direction, casting doc) through a doorway-test: does it open possibility or close it? Flag over-specified constraints. Flag under-specified principles. Output a pass/fail + one rewrite recommendation per failed item.
- **`sniped-insight-convergence`**: Multi-source signal synthesis checklist. Given a decision point (new lane, campaign direction, pricing move), pull quantitative signal + instinct note + cultural observation + proof data and force convergence before any action is taken. Prevents single-source verdicts.
- **`sniped-creative-brief-builder`**: Structured prompt template that outputs an inspiration brief (not a spec) for any shoot, campaign, or content chapter. Forces: one audience truth, one constraint set, one doorway sentence. Output is a door-opener, not a requirements doc.

### CONNECTOR / PLUGIN OPPORTUNITIES

- **Notion + Claude Code**: Brief-audit skill reads direction docs directly from Notion pages (Composite Environment Rotation, Lineage Doctrine) and returns doorway-test scores. No manual copy-paste. Routes via `mcp__claude_ai_Notion__notion-fetch`.
- **Airtable**: Insight-convergence loop stores signal sources per decision (quantitative row, instinct row, cultural observation row, proof row) and surfaces convergence gaps. A view with incomplete rows = no decision yet. Routes via `mcp__claude_ai_Airtable__create_records_for_table`.
- **Gmail + Instantly**: Consumer-as-partner principle applied to outreach. Pre-outreach signal read (recent post, shared cultural reference) feeds the opener. Not demographic targeting; behavioral + cultural signal. Routes via `mcp__claude_ai_Gmail__search_threads` for warm contacts, Instantly for cold sequence.
- **Google Drive**: Brief-audit output stored alongside each production doc. Version history shows whether the doc has drifted toward spec (bad) or stayed as doorway (good). Routes via `mcp__claude_ai_Google_Drive__create_file`.

### TOOL-ROUTING UPGRADES

| Task | Current Route | Upgraded Route |
|---|---|---|
| Build a shoot/chapter brief | Manual write | `sniped-creative-brief-builder` skill + Notion MCP publish |
| Classify a new task before prompting | Ad hoc | `sniped-prompt-method-router` (LtM/PaS/PoTh) before any Claude Code session |
| Audit direction doc for over-spec | Manual read | `sniped-brief-audit` skill, Notion fetch, return pass/fail |
| Multi-source decision synthesis | Single-doc review | `sniped-insight-convergence` + Airtable signal rows |
| Pre-outreach signal read | Manual search | Gmail MCP thread search + cultural observation note before Instantly sequence fires |

### EVALUATION GATES

- **Brief-as-doorway gate**: Before any direction doc ships, ask: does this open or close possibility for the production team? If it answers every question, it is a spec, not a brief. Fail = rewrite.
- **Insight-convergence gate**: Before any strategic decision (new lane, pricing move, campaign direction), confirm at least three signal sources have been consulted (data, instinct, proof). Single-source decisions are blocked.
- **Constraint-count gate**: Any prompt, brief, or planning doc that uses open-ended lists ("channels," "improvements," "options") must receive a count constraint before execution. No count = no output.
- **Decomposition-method gate**: Before a complex Claude Code prompt is written, classify the task as LtM/PaS/PoTh. Mismatched method = degraded output. Gate forces classification first.
- **Consumer-intelligence gate**: Any copy, DM, caption, or brief that talks down to the audience or treats them as a demographic bucket fails this gate. Rewrite assumes the reader is smart and reads subtlety.

### DECISION UPGRADES

- **New lane evaluation**: Use PaS frame. Plan phase: cost structure + revenue streams + risk. Execute phase: first proof action + bookkeeping note. Never execute without completing plan phase first.
- **Direction doc review**: Run brief-audit gate on every doc before production week. A doc that has drifted to spec kills serendipity on set.
- **Outreach timing**: Do not fire Instantly sequence without a consumer-as-partner signal read (one behavioral or cultural note per contact). Demographic-only targeting is the wrong mode.
- **Strategy validation**: "One doesn't have a great strategy until one has a great ad." Any planning document claiming strategic authority must be stress-tested against actual output proof. If no proof exists, the doc is a hypothesis, labeled as such.

### DOCTRINE / MEMORY UPGRADES

**Promoted to doctrine (new additions):**

1. **Serendipity Principle (new named rule):** Constraint enables unexpected solutions; over-specification prevents them. Applies to every direction doc, brief, and prompt. Add to `feedback_visual_direction_luxury_editorial.md` as the mechanical reason restraint wins. Wording: "Doctrine enables discovery. Constraint is not limitation; it is the trap that leaves room for the mouse."

2. **Consumer/Subject/Client as Creative Partner:** The model, client, and audience are partners in meaning-making, not subjects or targets. This upgrades `intel_trust_mechanics` from a delivery/relationship frame to a co-creation frame. Named addition: "Partner Architecture."

3. **Prompt Method Router as operating default:** Before any multi-step Claude Code task, classify as LtM/PaS/PoTh. This is not optional; mismatched method degrades output quality predictably.

4. **Brief-as-Doorway standard for all direction docs:** Every SNIPED production/direction doc is audited against this: does it open or close possibility? Spec-drift is a failure mode, not a quality marker.

**Strengthened (existing doctrine, now harder):**

- `feedback_proof_over_packaging`: "One doesn't have a great strategy until one has a great ad" is a quotable crystallization of this rule. Add it as the reference anchor.
- `feedback_full_os_synthesis_every_answer`: Multi-source insight convergence (data + instinct + cultural signal + proof) is now explicitly the synthesis method, not just "read the whole OS."
- `intel_trust_mechanics`: Partner architecture is the missing upstream layer. Trust is not just signals and anti-patterns; it starts at whether the other party is treated as a partner or a subject.

**No contradictions with existing doctrine found.** Both sources deepen and sharpen without displacing locked rules.

---

**Shelf 14 net verdict:** Two short sources, both high-leverage. The Steel/Burns review is the stronger find; it adds Serendipity Principle, Partner Architecture, and Brief-as-Doorway as three doctrine-grade upgrades. The decomposition template adds operational vocabulary (LtM/PaS/PoTh) that upgrades how prompts are constructed. Neither source touches identity or locks a lane.