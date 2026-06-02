# Claude Capabilities 2026 · Tactical Extraction

Source: `/99_VAULT/_intake_archive_2026-05-12/MORE CLAUDE 5.docx`
Distilled: 2026-05-12

Anthropic's release notes Jan-Apr 2026. Maps Claude / Claude Code / Claude Cowork capability surface as of mid-2026. Use to understand what's actually available in the Claude ecosystem before designing SNIPED workflows.

---

## Active Claude models (as of April 2026)

| Model | Released | Use case |
|---|---|---|
| **Claude Opus 4.7** | 2026-04-16 | Most capable. Best for complex coding, long-running tasks, vision. This skill is Opus 4.7. |
| Claude Opus 4.6 | 2026-02-05 | Previous flagship. Smart but superseded by 4.7. |
| Claude Sonnet 4.6 | 2026-02-17 | Most capable Sonnet. 1M token context window in beta. |
| Claude Haiku 4.5 | 2025-10-01 | Fast, light. For simple tasks. |

SNIPED implication: when launching automated workflows (Phase B+), Opus 4.7 for strategic work, Sonnet 4.6 for content velocity, Haiku 4.5 for high-volume low-stakes tasks.

---

## Claude Cowork (now GA on macOS + Windows)

Released GA 2026-04-09. The collaborative workspace product. Key features:
- Available via Claude Desktop
- Analytics API + usage analytics
- OpenTelemetry support
- Role-based access for Enterprise plans

SNIPED relevance · LOW in Phase 1 (solo operator). Reconsider at Phase B if hiring + collaboration tools needed.

---

## Claude Code (the CLI you're using right now)

Major 2026 updates:
- **Skills system** · custom skills via SKILL.md (this is what we built today · 28 skills in `/SNIPED_OS/_skills/`)
- **Plugins marketplace** · launched Feb 2026 with admin controls
- **MCP support** · the protocol Higgsfield uses to integrate with Claude (per `HIGGSFIELD_TACTICAL_EXTRACTION.md`)
- **Memory layer** · persistent memory across sessions (this is `~/.claude/projects/-Users-sniper/memory/`)
- **Computer use** · research preview, Claude can navigate/click on screen (Pro/Max only)
- **Scheduled tasks** · cron-like recurring tasks in Cowork

SNIPED implication · highly relevant. The skills system + memory layer + MCP are what make the SNIPED_OS portable across sessions.

---

## Memory updates (Feb 2026)

Memory now available for free users (previously paid only). Memory includes:
- Chat history search
- Import/export memory
- Persistent context across sessions

SNIPED has been using this since the project started (see `~/.claude/projects/-Users-sniper/memory/MEMORY.md` · 25+ files).

---

## Claude for Excel + PowerPoint (Feb-Mar 2026)

Add-ins available. Cross-context (Claude in Excel knows what happened in PowerPoint). Supports skills + plugins. LLM gateway support for Bedrock / Vertex / Foundry.

SNIPED implication · MEDIUM. Useful for:
- SNIPED CRM (Excel) review and updates
- Op Kit / Brand System pitch decks (PowerPoint)
- Defer activation until Phase B (current solo cadence doesn't need it)

---

## Computer Use (research preview)

Claude can open files, run dev tools, point/click, navigate UI · no setup. Pro/Max only.

SNIPED implication · TESTABLE for automation. Could potentially run:
- Lightroom imports on a schedule
- Pixieset gallery uploads
- Notion CRM data entry
- Higgsfield image generation pipelines (alternative to MCP)

Phase B trigger: test once SNIPED has surplus capacity. Phase 1: not worth the setup cost.

---

## Scheduled Tasks in Cowork (Feb 25, 2026)

Cron-like recurring + on-demand tasks in Claude Cowork.

SNIPED relevance · USE NOW potential:
- Weekly Monday cockpit review (read `MONDAY_COCKPIT.md`, surface week's 3 outcomes)
- Daily VIB outreach prep (draft 2-3 DMs from pipeline)
- Quarterly Constraint Audit reminder
- Backup verification (90-day reminder per `SYSTEM_FINAL_STATUS.md` Action 10)

Setup cost: ~30 min to configure all of the above.

---

## Interactive Apps (Mar 25, 2026)

Claude mobile can connect to fully interactive apps · live charts, sketches, shareable assets rendered in conversation.

SNIPED implication · LOW. Mobile-first workflow not current priority.

---

## Claude Design (Apr 17, 2026 · Anthropic Labs)

New product. Lets you collaborate with Claude on visual outputs · designs, prototypes, slides, one-pagers.

SNIPED implication · MEDIUM. Could be useful for:
- Op Kit pitch deck design
- Direction Stack book layout
- Carrd page mockups
- VIB caption library visual templates

Defer to Phase B unless specific need arises.

---

## Self-serve Enterprise plans (Feb 12, 2026)

Any organization can purchase Enterprise without Sales conversation. Single seat type covers Claude + Claude Code + Cowork.

SNIPED implication · NOT RELEVANT in Phase 1. Solo operator. Pro plan covers all current needs. Phase B+ if team grows.

---

## Capability decision tree for SNIPED

| Need | Use |
|---|---|
| Strategic copilot, memory, skills | Claude Code (this CLI) on Opus 4.7 |
| Tactical drafting (captions, emails, batch) | Claude Desktop on Sonnet 4.6 |
| High-volume low-stakes (rename batch, simple cleanup) | Claude Haiku 4.5 |
| Recurring scheduled tasks | Claude Cowork (when activated · Phase B+) |
| Computer automation | Computer Use research preview (Phase B+) |
| Visual collaboration | Claude Design (Phase B+) |
| Excel CRM work | Claude for Excel add-in (low priority) |
| Pitch deck design | Claude for PowerPoint (low priority) |

---

## What's NOT yet released (as of April 2026)

Worth tracking · these may unlock new SNIPED workflows when released:
- Long-form video gen native to Claude (currently external · Higgsfield/Seedance)
- Native image gen comparable to GPT Image (currently external · Firefly/Seedream/Nano Banana)
- Audio gen / voice cloning (currently external · ElevenLabs)

When/if Claude ships native image gen at SNIPED's quality bar, the `HIGGSFIELD_TACTICAL_EXTRACTION` and `SEEDREAM_TACTICAL_EXTRACTION` workflows would consolidate.

---

## Cross-references

- `/10_REFERENCE/HIGGSFIELD_TACTICAL_EXTRACTION.md` · MCP integration with Higgsfield
- `/_skills/` · the 28 SNIPED skills built using the Claude Code skills system
- `/00_BRIEF/PRODUCTION_OS.md` Section 4 · AI tool stack
- Memory: `[[feedback-execution-mode]]` · session protocol leveraging memory layer
