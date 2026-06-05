# OS KNOWLEDGE-TO-CAPABILITY DASHBOARD
### Sprint 001 result. Source of truth for what is converted vs queued vs discarded.
2026-06-05.

## Start Here (operating source code)
| metric | count |
|---|---|
| docs classified (zero unclassified) | 114 |
| USED (converted to operating behavior) | 25 |
| QUEUED (real how-to, not yet converted, reason+priority logged) | 72 |
| DISCARDED (duplicate / low-signal, reason logged) | 17 |
| technique cards in library | 223 (29 builtin + 194 converted this sprint) |
| docs that yielded cards this sprint | 19 of 20 (sniped_figma agent returned 0; covered by builtin fig_ cards) |

## Capability wiring
| layer | state |
|---|---|
| gates updated (self-solve wired) | os_premium_stack_gate, os_elite_gate |
| gates available to fix | os_postproduction_gate, os_motion_qa, os_privacy_gate, os_vision_gate |
| routes cards activate | mcp.adobe.* (PS/LR/Premiere/Firefly), mcp.figma, blender, mcp.higgsfield.*, local.ffmpeg |
| scripts created this arc | os_howto_extract, os_technique_cards, os_starthere_convert, os_premium_stack_gate, os_elite_gate |
| card library file | scripts/os_technique_cards.py (builtin) + TECHNIQUE_CARDS.json (converted) |
| matrices | OS_STARTHERE_TO_OPERATING_CODE_MATRIX.csv, OS_STARTHERE_CLASSIFICATION.csv, OS_BOOK_TO_DOCTRINE_MATRIX.csv |

## Books (doctrine fuel)
| category | count |
|---|---|
| FULLY_OPERATIONALIZED (doctrine atoms / gates exist) | 5 |
| QUEUED_FOR_DOCTRINE_EXTRACTION (chunked, not yet doctrine) | 19 |
| LOW_PRIORITY_REFERENCE_ONLY | 14 |
| total audited families | 38 |

## Proof the OS uses it (run any)
```
os_technique_cards.py solve "poster feels template"      -> fig_design_system (sniped_figma)
os_technique_cards.py solve "image crop is weak"         -> ff_gen_expand (Adobe Stack)
os_technique_cards.py solve "edit pacing weak"           -> pr_pacing (series_3)
os_technique_cards.py solve "background feels fake"      -> gemini_photo background mask (Gemini PHOTO YAP)
os_technique_cards.py solve "skin looks AI"              -> ps light-integration / frequency separation (series_3)
```

## Remaining blockers
- 72 Start Here docs QUEUED (priority-ranked) , next batches.
- 19 books QUEUED for doctrine extraction (from KB chunks, raw epub not needed).
- solve keyword-matching is rough on a few queries ("underused Adobe cloud") , tune synonyms.
- sniped_figma re-run (agent yielded 0).

## Next batch (priority 1 first)
Money/offer/copy families: cold_outreach (done 11), series 2 pricing doctrine, The_Offer/Revenue/Attention_Stack, MONEY docs. Then remaining Lightroom/posing/lighting OG docs. Then the 19 queued books -> doctrine atoms.
