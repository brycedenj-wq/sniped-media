---
name: ai-agent-architecture-wat
description: |
  Builds autonomous AI agent systems using the WAT Framework (Workflows, Agent, Tools) with architecture selection (single agent → sub-agents → agent teams).
  Use when:
  - building autonomous AI systems for business processes
  - deciding between single agents, sub-agents, or agent teams
  - automating multi-step workflows with Claude Code
  - configuring sub-agents with scoped tools and system prompts
  - creating the WAT stack (markdown workflows + modular tools + agent coordinator)
  Keywords: AI agents, WAT framework, Claude Code, sub-agents, agent teams, autonomous agents, agentic workflows, MCP, tool configuration, agent architecture
---

# AI Agent Architecture (WAT Framework)

**Skill ID:** 9.2  
**Category:** AI Systems & Automation  
**Source Document(s):** claude_agents_extracted.docx

## Purpose

Build autonomous AI agent systems using the WAT Framework (Workflows, Agent, Tools) and select the appropriate architecture level (single agent, sub-agents, or agent teams) for any business process.

## When to Use

When a persistent problem resists repeated fix attempts, suggesting the issue is structural rather than personnel-based.

## Instructions

Follow this workflow precisely. Each step is grounded in the source document(s) listed above. Do not skip steps. Do not invent frameworks, models, or terminology not present in the source material. Execute each step in order, using the exact logic and decision criteria documented.

## Workflow

1. Define the business process to automate. Identify where judgment, variability, and multi-step execution are required.
2. Select architecture level: Single agent (isolated tasks), Sub-agents (specialist delegation or parallel execution), or Agent Teams (peer-to-peer collaboration with shared task list).
3. Build Workflows: Create markdown instruction files (SOPs for the AI). These are the behavioral instructions.
4. Build Tools: Create modular Python scripts that perform discrete actions (scrape, analyze, generate). Each tool does one thing.
5. Configure the Agent: Set up Claude Code or the Agent SDK as the coordinator that reads workflows, selects tools, and handles errors.
6. For sub-agents: Create agent markdown files in .claude/agents/ with name, allowed tools, description, and system prompt. Scope tools per agent.
7. For agent teams: Enable shared task lists for peer-to-peer collaboration. Use when tasks require inter-agent consistency.
8. Implement guardrails: Input validation and output checks to prevent error compounding.
9. Create feedback loops: The agent should update its own context files, SOPs, and skills based on corrections.

## Output Format

Produce all of the following deliverables:

- Architecture selection rationale (single/sub-agents/teams)
- Workflow markdown files (SOPs for each process)
- Tool specifications (modular scripts with clear interfaces)
- Agent configuration files with scoped tools and system prompts
- Guardrails specification (input validation, output checks)

## Example Use

User provides context about their specific situation. The skill guides them through each workflow step sequentially, producing all deliverables listed in the Output Format section. Each step builds on the previous one, and no step should be skipped.
