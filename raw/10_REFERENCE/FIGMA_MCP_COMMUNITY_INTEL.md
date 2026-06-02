# Figma MCP Community Intel · Brief Reference

Source: `/99_VAULT/_intake_archive_2026-05-12/FIGMA.docx`
Distilled: 2026-05-12

Reddit r/FigmaDesign thread compilation on Claude + Figma MCP integration. Community sentiment + tooling intel from ~April 2026. Not tactical methodology · short reference only.

---

## Tool decision validated

**Official Figma MCP plugin (`mcp__plugin_figma_figma__*`) is the right tool for SNIPED.** Why:

- Goes through Figma Plugin API directly (not REST API)
- No Figma rate limits
- No Claude API limits (uses Claude Code subscription)
- Read + write capabilities
- `use_figma` tool for JS execution in Figma context

This is what built the `SNIPED · VIB Master` file at https://www.figma.com/design/qIu3GAifLsRuWosXdingYZ.

## Alternative MCP tools mentioned (skip)

- "Figma Console MCP" · third-party · unnecessary, official MCP covers the use case
- Custom MCP bridges via curl · per Reddit, "extremely easy to build" but specific to org, low generality
- Plugin-based custom builds · overkill for SNIPED's current scope

## Community sentiment patterns

| Pattern | SNIPED applicability |
|---|---|
| "Junior junior designer without design system context" | NOT applicable · VIB is a simple template, not complex design |
| "Best for prototyping + broad exploration" | Aligned · VIB master IS the prototype that gets duplicated per send |
| "Connect a design system for best results" | Future · build SNIPED design system in Figma at Phase B+ scale |
| "Manual setup outweighs token cost for enterprise" | Not relevant · SNIPED is single-operator, low complexity |
| "AI good at appearance, not maintainable structure underneath" | Mitigated · the VIB spec is explicit + tight, no structural ambiguity |

## Future Figma MCP capabilities to track

Per the doc, the community is exploring:
- Component variant generation (when SNIPED scales to multiple VIB types)
- Design system generation from code/spec
- Multi-page workflows
- Live design iteration with prototyping

For SNIPED Phase 1: single master file + per-prospect duplication is enough. Don't over-engineer.

---

## Cross-references

- `/03_OUTREACH/VIB_figma_spec.md` · the SNIPED-specific spec
- `/_skills/sniped-vib-outreach/` · skill that invokes the VIB build
- Memory: `[[feedback-execution-mode]]` · "stop building, start running"
