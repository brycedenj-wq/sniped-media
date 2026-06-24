---
name: framework-orchestrator
description: |
  Coordinates multiple installed skills to solve complex, multi-dimensional problems that no single framework can address alone. Identifies which skills apply, sequences them logically, and synthesizes outputs into one structured analysis.
  Use when:
  - a problem spans strategy, operations, finance, and decision-making simultaneously
  - the user asks for comprehensive analysis that requires multiple frameworks
  - a business question has competitive, economic, systemic, and execution dimensions
  - someone says "analyze this situation" or "help me think through this" without specifying a single framework
  - a decision is complex enough that one framework would give an incomplete picture
  - the user asks for a recommendation that requires diagnosing the problem, evaluating options, checking for biases, and designing an implementation plan
  - engineering, operational, or business problems need both technical and strategic analysis
  Keywords: multi-framework, comprehensive analysis, orchestrator, combined analysis, complex problem, strategic analysis, full assessment, cross-framework, integrated analysis
---

# Framework Orchestrator

**Skill ID:** 0.1
**Category:** Meta-Skill (Cross-Framework Coordination)
**Source Document(s):** All project knowledge documents. This skill draws on the complete installed skill library and sequences them based on problem characteristics.

## When to Use

When a problem is too complex or multi-dimensional for any single skill to address adequately. Specifically:

- The user presents a business situation that touches strategy, operations, economics, decision quality, and execution simultaneously.
- The user asks broad questions like "analyze my business," "what should I do about this situation," "help me think through this decision," or "give me a full assessment."
- A question requires diagnosis (what's happening), evaluation (what are the options), decision support (which option is best), and implementation design (how to execute).
- The user describes a problem that has interconnected causes spanning competitive dynamics, internal systems, team execution, and financial structure.
- An engineering or technical problem also has business, operational, and strategic dimensions.

This skill does NOT replace individual skills. It sequences and combines them. If the user's request clearly maps to a single skill, use that skill directly instead.

## Instructions

The Framework Orchestrator is a coordination layer. It reads the user's problem, selects the relevant installed skills, executes them in a logical sequence, and synthesizes their outputs into one coherent analysis. It does not invent new frameworks  -  it composes existing ones.

The orchestrator follows a fixed five-phase sequence. Not every phase requires every skill. The orchestrator selects only the skills that are relevant to the specific problem, skipping those that add no value.

**Default skill preferences (use when multiple skills could apply):**

- For diagnosing what's happening → System Analysis & Intervention Design (3.1)
- For evaluating competitive position → 7 Powers Assessment (1.4) or Strategy Kernel (1.1)
- For tracing consequences of a decision → Economic Incentive & Policy Analysis (17.1)
- For checking decision quality → Cognitive Bias Audit (2.1) or Munger Two-Track Analysis (19.1)
- For designing the response → Strategy Kernel Development (1.1)
- For planning execution → Value Stream Improvement (18.1) or Hoshin Kanri (18.2)
- For estimating unknowns → Fermi Estimation (2.4) or Superforecasting (2.3)
- For validating assumptions → Mom Test (4.1) or Shadow Test (4.4)
- For communicating the result → Pyramid Communication (5.2) or SUCCESs Message Design (5.1)

Follow the workflow precisely. Each step is grounded in the source document(s) listed above. Do not skip steps. Do not invent frameworks, models, or terminology not present in the source material. Execute each step in order, using the exact logic and decision criteria documented.

## Workflow

1. **Receive and classify the problem.** Read the user's full request. Determine the problem type: strategic (competitive position, market entry, business model), operational (process, efficiency, quality, execution), financial (revenue, pricing, resource allocation), decision-critical (high-stakes choice under uncertainty), technical/engineering (data center, systems, infrastructure), or hybrid (multiple types). Most complex problems are hybrid.

2. **Select applicable skills.** Based on the problem classification, identify which installed skills are relevant. List them explicitly. For each selected skill, state in one sentence why it applies to this problem. Do not select skills that add no analytical value  -  relevance is the filter, not completeness.

3. **Sequence the skills into phases.** Arrange selected skills into the five-phase execution order below. A skill may appear in only one phase. Not every phase needs a skill  -  skip empty phases.

   - **Phase A  -  Diagnose:** Understand what is actually happening. Preferred skills: System Analysis (3.1) for mapping structure and feedback loops, Strategy Kernel (1.1) for naming the challenge, Lean Diagnostic (18.3) for operational assessment.
   - **Phase B  -  Evaluate:** Assess the competitive, economic, and market dimensions. Preferred skills: 7 Powers Assessment (1.4) for competitive durability, Economic Incentive Analysis (17.1) for consequence tracing, Comparative Advantage (17.2) for resource allocation, Market Evaluation (4.3) for opportunity scoring.
   - **Phase C  -  Decide:** Choose among options with maximum rigor. Preferred skills: Cognitive Bias Audit (2.1) for debiasing, Munger Two-Track Analysis (19.1) for multidisciplinary rigor, Premortem (2.2) for risk surfacing, Superforecasting (2.3) for probability estimation.
   - **Phase D  -  Design:** Build the strategic and operational response. Preferred skills: Strategy Kernel (1.1) for the Diagnosis → Guiding Policy → Coherent Action structure, Value Stream Improvement (18.1) for process design, Hoshin Kanri (18.2) for goal alignment.
   - **Phase E  -  Communicate:** Structure the output for the audience. Preferred skills: Pyramid Communication (5.2) for logical structure, SUCCESs Message Design (5.1) for memorability, Calm Authority Voice (5.3) for credibility.

4. **Execute each phase.** Run each selected skill's workflow against the user's problem. Produce the skill's specified outputs. Between phases, carry forward the key findings as inputs to the next phase. Specifically:
   - Phase A outputs (diagnosis, system map, named challenge) become inputs to Phase B.
   - Phase B outputs (competitive assessment, incentive map, resource analysis) become inputs to Phase C.
   - Phase C outputs (debiased evaluation, probability estimates, risk register) become inputs to Phase D.
   - Phase D outputs (strategy kernel, action plan, process design) become inputs to Phase E.

5. **Synthesize into a single structured analysis.** Combine all phase outputs into one document using the Pyramid Principle structure: governing thought at the top, key findings organized by phase, supporting detail beneath each finding. Resolve any contradictions between frameworks explicitly  -  if the 7 Powers assessment and the Economic Incentive analysis point in different directions, name the tension and recommend how to resolve it.

6. **Deliver the Orchestrated Analysis.** Present the final output using the format specified below. End with explicit next steps: what the user should do first, what requires further investigation, and which individual skills to run in more depth if needed.

## Output Format

Deliver the following structured document:

- **Situation Summary** (2-3 sentences): What the user asked and what type of problem this is.
- **Skills Applied** (bullet list): Which skills were used and why, in execution order.
- **Phase A  -  Diagnosis**: System map, named challenge, or operational assessment. The "what's actually happening" section.
- **Phase B  -  Evaluation**: Competitive position, economic dynamics, market assessment. The "what forces are at work" section.
- **Phase C  -  Decision Support**: Bias check results, risk register, probability estimates. The "what could go wrong and how confident should we be" section.
- **Phase D  -  Strategic & Operational Design**: The strategy kernel (Diagnosis → Guiding Policy → Coherent Action), process improvements, goal alignment. The "what to do" section.
- **Phase E  -  Key Message**: The governing thought and 2-3 key takeaways structured for the user's audience.
- **Tensions & Tradeoffs**: Where frameworks disagreed and how the conflict was resolved.
- **Next Steps**: First action, open questions requiring further investigation, and which individual skills to run at full depth.

Omit any phase that was not relevant to the problem. Do not pad with empty sections.

## Example Use

User: "We're a 50-person SaaS company growing 40% YoY but our margins are shrinking, our biggest competitor just raised $100M, and our engineering team is burning out. What should we do?"

Orchestrator response:

**Skills Applied:**
- System Analysis (3.1)  -  map the interconnected dynamics of growth, margin erosion, competitive pressure, and burnout
- 7 Powers Assessment (1.4)  -  evaluate whether the company has durable competitive power before the competitor scales
- Economic Incentive Analysis (17.1)  -  trace the second-order effects of potential responses (price cuts, hiring spree, feature race)
- Cognitive Bias Audit (2.1)  -  check for loss aversion (overreacting to competitor funding) and planning fallacy (underestimating timeline to fix margins)
- Strategy Kernel (1.1)  -  build the Diagnosis → Guiding Policy → Coherent Action
- Value Stream Improvement (18.1)  -  diagnose the engineering process for waste and overburden causing burnout

**Phase A  -  Diagnosis:** The system map reveals a reinforcing loop: growth → hiring pressure → onboarding overhead → reduced velocity → more hours per feature → burnout → attrition → more hiring pressure. The competitor's funding is an external shock but the internal system is the binding constraint.

**Phase B  -  Evaluation:** 7 Powers scan shows Switching Costs (moderate  -  existing customer integrations) but no Scale Economies or Network Effects. The competitor's capital advantage will erode switching costs within 18 months if they undercut on price. Economic incentive analysis shows a feature race would accelerate margin erosion without building durable power.

**Phase C  -  Decision Support:** Bias audit flags loss aversion (competitor funding feels like an emergency but the internal system is the real threat) and planning fallacy (the team's estimate for the platform rewrite is likely 2x actual). Premortem surfaces: "We hired 20 people in 6 months, none were productive for 4 months, and 3 senior engineers quit from the chaos."

**Phase D  -  Design:** Strategy Kernel: Diagnosis = "We are in a chain-link problem where engineering velocity is the bottleneck, and growth is making it worse, not better." Guiding Policy = "Stabilize the engineering system before scaling further. Build switching cost depth rather than racing on features." Coherent Actions = (1) Freeze hiring for 90 days, (2) Run value stream mapping on the engineering pipeline to eliminate the top 3 wastes, (3) Invest in integration depth with top 20 customers to deepen switching costs.

**Phase E  -  Key Message:** "Our biggest threat isn't the competitor's $100M  -  it's our own engineering system collapsing under growth. Stabilize first, deepen the moat second, and let the competitor burn cash on a feature race we refuse to join."

**Tensions:** The 7 Powers assessment suggests urgency (switching cost window is closing) while the operational diagnosis demands slowing down (stabilize before scaling). Resolution: a 90-day stabilization sprint focused specifically on the activities that deepen switching costs (customer integrations), not on general operational cleanup.

**Next Steps:** (1) Run Value Stream Improvement (18.1) at full depth on the engineering pipeline this week. (2) Run the full 7 Powers scorecard against the funded competitor to quantify the switching cost timeline. (3) Validate the "integration depth" hypothesis with 5 Mom Test conversations (4.1) with your largest customers.
