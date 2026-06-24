---
name: prompt-engineering-tcrei
description: |
  Designs effective AI prompts using the TCREI framework (Task, Context, References, Evaluate, Iterate) and advanced techniques (chaining, chain-of-thought, tree-of-thought, adversarial validation, meta-prompting).
  Use when:
  - writing prompts for Claude or other AI tools and getting inconsistent results
  - delegating tasks to AI and needing reliable, high-quality output
  - building AI-powered workflows or automation pipelines
  - learning or teaching prompt engineering techniques
  - optimizing existing prompts through iteration and meta-prompting
  Keywords: prompt engineering, TCREI, chain of thought, few-shot, prompt chaining, tree of thought, meta-prompting, AI prompting, context engineering
---

# Prompt Engineering (TCREI + Advanced Techniques)

**Skill ID:** 9.1  
**Category:** AI Systems & Automation  
**Source Document(s):** Prompt_Engineering_Knowledge_Extraction.docx

## Purpose

Design effective AI prompts using the foundational TCREI framework and advanced techniques (chaining, chain-of-thought, tree-of-thought, adversarial validation, meta-prompting) to maximize output quality.

## When to Use

When building AI-powered workflows, automations, or systems that need to operate reliably at scale.

## Instructions

Follow this workflow precisely. Each step is grounded in the source document(s) listed above. Do not skip steps. Do not invent frameworks, models, or terminology not present in the source material. Execute each step in order, using the exact logic and decision criteria documented.

## Workflow

1. Define the Task: Use action verbs. Be specific about the deliverable.
2. Provide Context: Include all relevant background, constraints, audience, and domain details. More context = fewer hallucinations.
3. Supply References: Provide 2-10 examples of desired output (few-shot prompting). Show, don't just describe.
4. Evaluate the output: Assess format, factual accuracy, tone, and completeness against your criteria.
5. Iterate using four methods: (1) revisit framework components, (2) simplify into shorter sentences, (3) rephrase using analogous tasks, (4) introduce constraints to narrow focus.
6. For complex tasks, apply advanced techniques: Prompt Chaining (feed output as input to next prompt), Chain of Thought (explain reasoning step-by-step), Tree of Thought (explore multiple reasoning paths), Adversarial Validation (competing outputs critiqued by judge persona).
7. Use Meta-Prompting: Feed your draft prompt to the AI with instructions to critique and improve it. Run iteratively.

## Output Format

Produce all of the following deliverables:

- A structured prompt following TCREI framework
- Reference examples for few-shot learning
- Iteration log showing progressive prompt improvements
- Final optimized prompt with technique selection rationale

## Example Use

User provides context about their specific situation. The skill guides them through each workflow step sequentially, producing all deliverables listed in the Output Format section. Each step builds on the previous one, and no step should be skipped.
