---
name: sniped-ai-image-tool-pick
description: Pick the right AI image tool for a specific SNIPED task · Seedream 5.0/4.5, Higgsfield Soul, Nano Banana Pro, Firefly, ChatGPT image gen, Photoshop Generative Fill with Reference Image. Use when user has a generation/edit task and isn't sure which tool to reach for.
---

# SNIPED AI Image Tool Pick Skill

The tool-routing skill. Output target: clear pick with the reasoning.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/AI_IMAGE_TOOLS_TACTICAL_EXTRACTION.md` · the tool-to-task matrix
2. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/SEEDREAM_TACTICAL_EXTRACTION.md`
3. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/HIGGSFIELD_TACTICAL_EXTRACTION.md`
4. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/PHOTOSHOP_GENERATIVE_FILL_REFERENCE_IMAGE_EXTRACTION.md`

## INVOKE WHEN
- "Which AI tool should I use for X"
- Starting an AI-assisted task
- Comparing tools for a specific job

## OUTPUT
- The recommended tool
- Why (per the tool-to-task matrix)
- Backup option if primary fails
- Specific prompt template / settings (delegate to specific skill: seedream-prompt, higgsfield-pipeline)

## REFUSE
- Recommending tools for tasks that violate identity rule
- Generic "try them all" advice
- Tools that don't fit SNIPED's locked direction


## Inputs
- Specific generation or editing task described: subject type, required fidelity, editing vs. net-new generation, identity constraints (required)
- Whether an existing asset is the starting point (i2i / inpainting / expand) or net-new generation
- SNIPED direction constraint context so the refusal gate can fire on off-direction tasks

## Gates
- Mandatory reads before output: AI_IMAGE_TOOLS_TACTICAL_EXTRACTION.md, SEEDREAM_TACTICAL_EXTRACTION.md, HIGGSFIELD_TACTICAL_EXTRACTION.md, PHOTOSHOP_GENERATIVE_FILL_REFERENCE_IMAGE_EXTRACTION.md
- Identity rule gate: refuse tasks involving unlicensed celebrity likeness or AI-generated client subjects
- No generic advice gate: refuse 'try them all' responses; every output names one primary and one backup with task-specific reasoning
- SNIPED direction gate: refuse tools that do not fit SNIPED's locked direction even if technically capable

## Test
- case: Operator needs a product-locked editorial still of Alma suit on an AI body for IG, starting from the real isolated suit cutout PNG. Expected: primary = Higgsfield Cinema Studio Element (alma-suit-real-isolated) + character with reasoning citing element-lock garment law, backup = Seedream 5.0 nano_banana 2-image edit, prompt stub ('describe only scene/pose/camera/light; never name the garment'), delegate detail to /sniped-higgsfield-pipeline.
- expected failure: Operator requests a tool pick for generating a photorealistic portrait of a named celebrity for client-facing campaign material. Skill refuses: 'Cannot recommend: unlicensed celebrity likeness violates the SNIPED identity rule. Describe the task using an owned character or synthetic subject.'
