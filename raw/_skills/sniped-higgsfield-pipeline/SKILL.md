---
name: sniped-higgsfield-pipeline
description: Run a Higgsfield content factory pipeline · MCP setup, 4-stage Content Factory (research / plan / generate / schedule), or Image Pack workflow. Use when user has the Higgsfield MCP installed (or is installing), wants the Content Factory pipeline, or needs Higgsfield Image Pack for SNIPED content velocity.
---

# SNIPED Higgsfield Pipeline Skill

The Higgsfield orchestration skill. Output target: pipeline configured for the specific SNIPED use case.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/HIGGSFIELD_TACTICAL_EXTRACTION.md` · MCP + 4-stage pipeline + Image Pack
2. Memory: `[[sniped-ai-sentiment]]` · what Higgsfield can/can't be used for

## INVOKE WHEN
- Higgsfield MCP installation
- Running the Content Factory pipeline
- Image Pack generation for SNIPED content
- Per-batch permission gate decisions

## OUTPUT
- The specific pipeline / Image Pack configuration
- Permission gate settings
- Cost estimate per batch
- Routing of output (IG creative engine only · never client work)

## REFUSE
- Using Higgsfield for client deliverables (anti-AI rule)
- Generating subjects (identity rule)
- Setting "always allow" globally on credit usage
- Pipeline outputs without permission gate confirmation
