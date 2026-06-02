# CLAUDE_OPERATOR_DOCS source index · 2026-05-22

5 source files · 26 chunks · batch_id `CLAUDE_OPERATOR_DOCS`. NO NEW domain. The 2 synthesis chunks (025-026) cite a representative real source file.

## Sources

| # | Extracted file | Title | Chunks | Original source |
|--:|---|---|---|---|
| 1 | `claude_operating_manual.txt` | The Claude Operating Manual | 001-005, 025 (6) | `raw/Claude_Operating_Manual.docx` |
| 2 | `the_claude_stack.txt` | The Claude Stack (Stack series Vol. V) | 006-012, 026 (8) | `raw/The_Claude_Stack (1).docx` |
| 3 | `claude_cowork_genius.txt` | Claude Cowork Genius (walkthrough) | 013-016 (4) | `raw/claude cowork genius.docx` |
| 4 | `ai_after_ramon.txt` | AI After Ramon (founder walkthrough) | 017-021 (5) | `raw/ai after ramon.docx` |
| 5 | `using_ai_x_gumroad_digital_products.txt` | Using AI x Gumroad x Digital Products | 022-024 (3 · light) | `raw/using ai x gumroad x digital products.docx` |

Extracted via `pandoc -f docx -t plain` · no OCR · no new dependencies · 275,333 words total (INTERNAL chunk-authoring reference only).

## Deferred / excluded / rerouted (0 chunks)

| Item | Status |
|---|---|
| `astro claude websites 3x faster.docx` | DEFERRED · web-page scrape (853k words "Super Carl" landing-page boilerplate · filename/content mismatch) · 0 chunks |
| `MORE CLAUDE 5.docx` | DEFERRED · Anthropic Help Center / release-notes scrape · stale · archived (`99_VAULT`) · 0 chunks |
| `ai after ramon copy.docx` | EXCLUDED · byte-identical duplicate (md5 `4e9fd4f2…`) of `ai after ramon.docx` · 0 chunks |
| `document.pdf` | EXCLUDED · Seth Godin, "This is Marketing" (2018) · marketing book · REROUTED to BATCH_009 · 0 chunks |
| `index.html` | EXCLUDED · "AI Ops Dashboard" build artifact · 0 extractable text · overlaps BATCH_006 PRD · 0 chunks |

## Per-chunk concept + domain + source map

| chunk_id | Concept | Domain | source |
|---|---|---|---|
| 001 | Context architecture, not prompting skill | meta-doctrine | operating_manual |
| 002 | Claude is an OS you configure, not a chatbot | ai-tooling | operating_manual |
| 003 | Workspaces are the unit of organization | operator-process | operating_manual |
| 004 | Skills are reusable automation packages | automation-blueprint | operating_manual |
| 005 | The AI needs better information, not better instructions | prompt-engineering | operating_manual |
| 006 | The operating layer that lets one person run all four Stacks | strategy | claude_stack |
| 007 | AI as force multiplier roughly doubles throughput | strategy | claude_stack |
| 008 | Projects and persistent context | ai-tooling | claude_stack |
| 009 | Claude Code in a terminal: workspace-based work | ai-tooling | claude_stack |
| 010 | Skills are atoms, commands are molecules, skills compound | automation-blueprint | claude_stack |
| 011 | Commands are one-liner automations | operator-process | claude_stack |
| 012 | Sub-agents and agent teams: hub-and-spoke delegation | operator-process | claude_stack |
| 013 | Claude desktop's three modes: chat, co-work, code | ai-tooling | cowork_genius |
| 014 | Copy-pasting in chat is terrible for real work | meta-doctrine | cowork_genius |
| 015 | Co-work mode runs real work without technical skills | operator-process | cowork_genius |
| 016 | Let the AI produce the artifact, not just describe it | ai-tooling | cowork_genius |
| 017 | AI makes a business better, cheaper, faster, less risky | strategy | ai_after_ramon |
| 018 | Commoditized vs differentiated automations | client-application | ai_after_ramon |
| 019 | Drop AI into an existing, working sales process | client-application | ai_after_ramon |
| 020 | Use AI to take risk out of the business | strategy | ai_after_ramon |
| 021 | Automate the workflow you understand best first | operator-process | ai_after_ramon |
| 022 | Decouple authoring from publishing (digital-asset library) | strategy | gumroad |
| 023 | Profit-first publishing: demand over creative expression | strategy | gumroad |
| 024 | Validate a niche against competitor earnings first | client-application | gumroad |
| 025 | SYNTHESIS · context architecture is the meta-lever | meta-doctrine | operating_manual (synthesis) |
| 026 | SYNTHESIS · the practical HOW under BATCH_008 augmentation | strategy | claude_stack (synthesis) |

## NO new domain

All seven domains used (strategy, ai-tooling, operator-process, client-application, meta-doctrine, automation-blueprint, prompt-engineering) pre-exist in the corpus and were on the operator-approved list for this mini-batch.

## Cross-batch reinforcement summary

| Chunk(s) | Link |
|---|---|
| 001-005, 025 context architecture | BATCH_006 Claude Code primitives (the practice layer over them) |
| 005 context-beats-prompting | PROMPT_TEMPLATES_DEEP (reframes prompt craft · lane stays PTD's) |
| 010-012 skills / commands / sub-agents | BATCH_006 skills + N8N_AUTOMATION_SYSTEMS (Claude-side complement) |
| 017-021 AI-in-a-real-business | BATCH_008 augmentation canon + OPPORTUNITY_MANAGEMENT_TEMPLATES |
| 022-024 productized-IP monetization | future BATCH_009 / monetization lane (light coverage here) |
| 026 synthesis | BATCH_008 (the WHY) ↔ this mini-batch (the daily HOW) |

## Copyright-safe quote discipline

`direct_quotes` are SHORT illustrative lines only (longest 19 words). 13 of 26 chunks carry a quote; 13 paraphrase. Operator-authored / synthesized sources; extracted full text is internal reference.

## Excluded material (NOT chunked)

| Material | Reason |
|---|---|
| astro claude websites scrape | Web boilerplate noise · deferred |
| MORE CLAUDE 5 release-notes scrape | Stale · archived · deferred |
| ai after ramon copy | Byte-identical duplicate |
| document.pdf ("This is Marketing") | Marketing book · rerouted to BATCH_009 |
| index.html | Build artifact · 0 text · B006 overlap |
| Long passages of source text | Not reproduced · short illustrative quotes only |
