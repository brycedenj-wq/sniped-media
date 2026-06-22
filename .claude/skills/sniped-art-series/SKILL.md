---
name: sniped-art-series
description: Reference SNIPED's Art Series direction · 5 photographer studies + the locked aesthetic direction for the SNIPED art lane. Use when planning art series work, evaluating creative direction, or asks about the art lane separate from commercial Reset/Op Kit work.
---

# SNIPED Art Series Skill

The art lane reference. Output target: which photographer study applies + the specific aesthetic move.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/09_ART_SERIES/` · 5 photographer studies (when populated)
2. `/Users/sniper/Downloads/    SNIPED_OS/Study_AnnieLeibovitz.md` · Annie Leibovitz study (in root)
3. `/Users/sniper/Downloads/    SNIPED_OS/Study_GracielaIturbide.md` · Graciela Iturbide study (in root)
4. Memory: `[[sniped-visual-direction-luxury-editorial]]` · the locked register the art lane operates in

## INVOKE WHEN
- Planning Cultural Doc art work
- Direction Stack book art chapters
- "What aesthetic does this art series target"
- Art lane vs commercial lane distinction questions

## OUTPUT
- Which photographer study applies
- The specific technique or aesthetic move
- Application to the SNIPED v3 LUXURY direction

## REFUSE
- Cross-mixing commercial and art lane (different registers)
- Adding new photographer studies ad-hoc (the 5 are locked per `SYSTEM_FINAL_STATUS.md`)
- Treating art series as commercial deliverable (different output target)


## Inputs
- The specific art-lane task or question: a Cultural Doc shoot, Direction Stack book art chapter, or aesthetic direction question
- Any reference to a specific photographer study (Leibovitz, Iturbide, or others from the locked 5)
- Enough context to distinguish art lane from commercial lane (Reset/Op Kit work)

## Gates
- Must consult 09_ART_SERIES/ folder and root Study_*.md files before output
- Must NOT cross-mix commercial and art registers in the same output
- Must NOT add new photographer studies ad-hoc (the 5 are locked per SYSTEM_FINAL_STATUS.md)
- Must NOT treat art series output as a commercial deliverable (different output target, different register)
- Must confirm the task is art lane (Cultural Doc, Direction Stack art chapter) not Reset/Op Kit before proceeding

## Test
- case: User asks: 'For the Cultural Doc chapter on the street-market shoot, what aesthetic direction do we use?' Expected output: specific photographer study citation (e.g., Iturbide for documentary graphic stillness), one concrete technique from that study, and a note on how it fits the v3 luxury direction without crossing into commercial-reset territory.
- expected failure: User asks to add a sixth photographer study (e.g., Vivian Maier) for a new art chapter. Skill must refuse: the 5 studies are locked per SYSTEM_FINAL_STATUS.md. Output names that gate and redirects to the closest existing study.
