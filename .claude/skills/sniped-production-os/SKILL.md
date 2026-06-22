---
name: sniped-production-os
description: Reference SNIPED's Production OS · folder structure, naming conventions, storage tiering, photo + content pipelines, AI routing, scenario flows. Use when user has a structural question about file organization, naming, backup, or workflow routing.
---

# SNIPED Production OS Skill

The operational backbone reference. Output target: the correct structural answer per the locked OS.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/PRODUCTION_OS.md` · the master operational doc

## INVOKE WHEN
- "Where does X file go"
- "What's the naming convention for Y"
- Backup tier questions
- AI tool routing questions
- Scenario flow questions ("how does this kind of shoot move through the pipeline")

## OUTPUT
- The specific PRODUCTION_OS section + answer
- The locked convention or rule
- Cross-references to relevant SOPs

## REFUSE
- Reinventing structure ad-hoc
- "I'll just save it wherever" advice
- Suggesting alternatives to locked conventions


## Inputs
- A structural question about file organization, naming convention, backup tier, AI tool routing, or pipeline scenario
- Enough context to identify the file or asset type (photo, content, AI-generated, etc.)
- Optional: the specific shoot or delivery scenario for cross-reference routing

## Gates
- No structure is invented ad-hoc; all answers must trace to PRODUCTION_OS.md verbatim
- Alternative naming or folder conventions are REFUSED even if seemingly reasonable
- Ambiguous questions surface both applicable sections and ask the operator to clarify rather than picking arbitrarily

## Test
- case: User asks where a Higgsfield-generated hero image goes after passing QA. Expected: exact PRODUCTION_OS.md folder path for AI-generated assets post-QA, naming convention, cross-reference to AI routing section.
- expected failure: Question is ambiguous enough that two PRODUCTION_OS sections could apply (photo vs. AI asset). Skill surfaces both sections and asks the operator to clarify asset type rather than guessing.
