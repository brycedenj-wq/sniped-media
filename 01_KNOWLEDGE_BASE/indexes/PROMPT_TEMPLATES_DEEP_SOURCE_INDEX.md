# PROMPT_TEMPLATES_DEEP source index · 2026-05-19

6 unique source files · 12 chunks · batch_id `PROMPT_TEMPLATES_DEEP`. 8 PDFs staged · 2 md5-duplicates excluded (0 chunks).

## Sources

| # | Extracted file | Chunks referencing it | Original source (canonical) |
|--:|---|---|---|
| 1 | `prompt_template_in_context.txt` | 001, 008, 012 | `raw/10_REFERENCE/_intake_2026-05-19/prompt_templates/Prompt Template - In Context-2.pdf` |
| 2 | `prompt_template_thought_generation.txt` | 002, 010 | `raw/.../Prompt Template - Thought Generation-2.pdf` |
| 3 | `prompt_template_problem_decomposition.txt` | 003 | `raw/.../Prompt Template - Problem Decomposition.pdf` |
| 4 | `prompt_template_self_criticism_basic.txt` | 004 | `raw/.../Prompt Template - Self Criticism (Basic)-3.pdf` |
| 5 | `prompt_template_self_criticism_advanced.txt` | 005, 009 | `raw/.../Prompt Template - Self Criticism (Advanced)-3.pdf` |
| 6 | `prompt_template_combining_techniques.txt` | 006, 007, 011 | `raw/.../Prompt Template - Combining Techniques-3.pdf` |

Source: The AI Edge prompt-technique cheat sheets (2 pages each · 266-420 words). Extracted via `pdftotext -layout` (no OCR · no new deps); promo header/footer lines stripped.

## Excluded duplicates (md5-confirmed · 0 chunks · not extracted)

| Duplicate PDF | Identical to | md5 |
|---|---|---|
| `Prompt Template - Combining Techniques-2.pdf` | `Combining Techniques-3.pdf` | `0f54f23559...` |
| `Prompt Template - Self Criticism (Advanced)-2.pdf` | `Self Criticism (Advanced)-3.pdf` | `d62b67512e...` |

Both remain untouched in `raw/`. They are duplicate copies, not separate intellectual sources.

## Per-chunk concept + domain + source map

| chunk_id | Concept | Domain | source_file |
|---|---|---|---|
| 001 | In-context learning · few-shot prompting | prompt-engineering | in_context |
| 002 | Thought generation · CoT + ThoT | prompt-engineering | thought_generation |
| 003 | Problem decomposition · LtM + PaS + PoTh | prompt-engineering | problem_decomposition |
| 004 | Self-criticism (basic) · SE + SR + COVE | prompt-engineering | self_criticism_basic |
| 005 | Self-criticism (advanced) · S2A + RaR + RE2 | prompt-engineering | self_criticism_advanced |
| 006 | Combining techniques · CoT + decomposition + self-criticism chained | prompt-engineering | combining_techniques |
| 007 | The prompt-technique taxonomy · full abbreviation map | prompt-engineering | combining_techniques |
| 008 | The Task + structured-Prompt scaffold | prompt-engineering | in_context |
| 009 | Self-criticism as a guardrail layer (verify-before-ship) | prompt-engineering | self_criticism_advanced |
| 010 | The reasoning-scaffold family · when CoT vs PaS vs LtM | prompt-engineering | thought_generation |
| 011 | Prompt-writing-agent substrate · the N8N bridge | ai-tooling | combining_techniques |
| 012 | Few-shot vs zero-shot economics · cheapest quality lever | prompt-engineering | in_context |

## Technique abbreviation map (source-faithful)

| Abbrev | Technique | Template |
|---|---|---|
| Few-Shot | In-context examples | In Context Learning |
| CoT | Chain-of-Thought | Thought Generation |
| ThoT | Thread-of-Thought | Thought Generation |
| LtM | Least-to-Most | Problem Decomposition |
| PaS | Plan-and-Solve | Problem Decomposition |
| PoTh | Plan-of-Thought | Problem Decomposition |
| SE | Self-Evaluation | Self-Criticism (Basic) |
| SR | Self-Refine | Self-Criticism (Basic) |
| COVE | Chain-of-Verification | Self-Criticism (Basic) |
| S2A | System-2-Attention | Self-Criticism (Advanced) |
| RaR | Rephrase-and-Respond | Self-Criticism (Advanced) |
| RE2 | Re-reading | Self-Criticism (Advanced) |

## Cross-batch reinforcement summary

This mini-batch is the **prompt-craft CONTENT layer**. It is the craft half of the prompt loop whose implementation half is N8N_AUTOMATION_SYSTEMS Cluster B.

| PTD chunk | Link |
|---|---|
| 011 prompt-writing-agent substrate | N8N_AUTOMATION_SYSTEMS chunks 003-005, 010 (the agent that produces these) |
| 003 decomposition | OPPORTUNITY_MANAGEMENT_TEMPLATES intake (break into scored sub-steps) |
| 008 Task+Prompt scaffold | OMT one-page-card standard container + B7 brief format |
| 009 self-criticism gate | B7 final-review un-delegate-able + executing-with-care |
| all per-technique chunks | BATCH_006 prompt-engineering domain (technique-level extension) |

## Excluded material (NOT chunked)

| Material | Reason |
|---|---|
| `Combining Techniques-2.pdf`, `Self Criticism (Advanced)-2.pdf` | md5-identical duplicates · 0 chunks · untouched in raw/ |
| Promo header/footer (skool.com / "Join My AI & Automation Community") | Stripped at extraction · noise |
| Worked business examples | Kept as illustration inside the technique chunks · the durable signal is the technique |
| AI Edge course BOOKS | Out of scope · queued for BATCH_008 |
| Literary intake sources | Out of scope · not touched |
