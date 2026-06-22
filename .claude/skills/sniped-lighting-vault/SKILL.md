---
name: sniped-lighting-vault
description: Reference SNIPED's lighting + posing + vision vault · 26 PDFs in /10_REFERENCE/lighting_pdfs/. Use when planning lighting for a shoot, troubleshooting a lighting setup, asking "how should I light this," or training on lighting principles. Slow-burn vision training, NOT a binge target.
---

# SNIPED Lighting Vault Skill

The lighting reference layer. Output target: targeted retrieval of the right PDF for the specific lighting question.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/PHOTOGRAPHY_VAULT_INDEX.md` · the index
2. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/lighting_pdfs/` · 26 PDFs

## INVOKE WHEN
- Planning lighting for an upcoming shoot
- "How should I light this register"
- Troubleshooting a lighting problem
- Building a posing reference deck
- Pre-shoot moodboard

## OUTPUT
- Which 1-3 PDFs from the vault are most relevant
- The specific principle / technique
- Application to SNIPED's luxury editorial register

## REFUSE
- Reading the entire vault for one question (it's a reference layer, not a curriculum)
- Suggesting lighting techniques that break the v3 LUXURY direction
- Generic "use soft light" advice without vault citation


## Inputs
- The specific lighting question, shoot context, or setup problem (register, subject type, location vs studio, desired mood)
- PHOTOGRAPHY_VAULT_INDEX.md (the index of all 26 PDFs, read on invocation to identify the 1-3 relevant files)
- The identified 1-3 PDFs from /10_REFERENCE/lighting_pdfs/ (read only targeted files, not the full vault)

## Gates
- Must cite the specific PDF(s) by title from the vault index, not give generic lighting advice
- Must not read the entire 26-PDF vault for a single question (reference layer, not a curriculum binge)
- Output must be filtered through the v3 LUXURY direction: techniques that break the luxury editorial register are refused
- Index must be read before any PDFs to enable targeted retrieval

## Test
- case: BJ is shooting a solo male founder portrait on location with natural window light and asks 'how do I control spill and still keep the luxury editorial feel?' Expected output: 1-2 vault PDF titles most relevant to window-light portraiture and spill control, the specific technique from those files (e.g. flagging placement, reflector distance), and how to dial it toward SNIPED's restrained luxury register rather than a hard commercial look.
- expected failure: User asks 'teach me everything about lighting' with no shoot context and no specific problem. Skill must refuse to binge the full vault and instead ask for a specific shoot context or setup problem to enable targeted PDF retrieval.
