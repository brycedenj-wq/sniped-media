# Higgsfield Reusable Mega-Prompts (from Scene_Sequence_Prompts)

Two locked, paste-ready prompts for Nano Banana Pro / Seedance coverage generation. Source: `REFERENCE_LIBRARY/higgsfield_og/Scene_Sequence_Prompts.pdf`. Use with an input reference image attached in the Higgsfield UI. Credit-efficient: each returns full coverage in one generation.

## 1. Cinematic Contact Sheet (3x3, 9 angles of one locked subject)
Best for: getting full shot coverage of a locked character/object/scene from a single reference, in one image. Then animate the panels you want.

```
Analyze the entire movie scene. Identify ALL key subjects present (single person, group/couple, vehicle, or object) and their spatial relationship/interaction. Generate a cohesive 3x3 grid "Cinematic Contact Sheet" featuring 9 distinct camera shots of exactly these subjects in the same environment. Adapt standard cinematic shot types to the content (group stays together; object framed whole):
Row 1 (Establishing): 1. Extreme Long Shot (subjects small in vast environment). 2. Long Shot (complete subjects head-to-toe / wheels-to-roof). 3. Medium Long Shot (knees up, or 3/4 view of object).
Row 2 (Core Coverage): 4. Medium Shot (waist up / central core, focus on interaction). 5. Medium Close-Up (chest up, intimate). 6. Close-Up (tight on face(s) or front of object).
Row 3 (Details & Angles): 7. Extreme Close-Up (macro on a key feature: eyes, hands, logo, texture). 8. Low Angle / Worm's Eye (looking up, imposing/heroic). 9. High Angle / Bird's Eye (looking down).
Strict consistency: same people/objects, same clothes, same lighting across all 9 panels. Depth of field shifts realistically (bokeh in close-ups). Photorealistic textures, consistent cinematic color grade, correct framing for the number of subjects.
```

## 2. 9-Scene Sequence (logical narrative progression from one input)
Best for: turning a one-line scene idea into a coherent 9-beat storyboard with a consistent subject, AI picking the angles.

```
Analyze the input image and identify the main subject(s). Maintain perfect consistency in appearance, proportions, materials, colors, and style across all frames. Read the SCENE INPUT and generate a cinematic 9-scene sequence that progresses logically from start to finish; each frame is the next meaningful moment. The AI chooses all camera angles and framing automatically. Ensure cinematic lighting, consistent color grading, realistic depth of field, and coherent environmental evolution. No repeated shots.
SCENE INPUT: <one-line scene description>
Frame 1: / Frame 2: / Frame 3: / Frame 4: / Frame 5: / Frame 6: / Frame 7: / Frame 8: / Frame 9:
```

## When to use which
- Need every angle of ONE moment/subject → Contact Sheet (#1).
- Need a STORY across time → 9-Scene Sequence (#2).
- Need a finished prompt with locked cinema grammar + diegetic audio → route through the `cinema-worldbuilder` skill instead of freehanding.
- Need a character base / sheet / plate → route through `banana-pro-director`.
