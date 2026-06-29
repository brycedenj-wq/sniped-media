export const meta = {
  name: 'docs-tooling-T1-retry',
  description: 'Docs/Tooling T1 retry (failed-only 12 docs): whole-read tool docs, tool-doc record + disposition, corrected adversarial verify.',
  phases: [ { title: 'Read' }, { title: 'Verify' } ],
}
const GROUPS = [[{"slug": "unreal_mcp_main_editor_tools_md", "title": "editor_tools.md", "repo": "unreal-mcp-main", "path": "/Users/sniper/Downloads/    SNIPED_OS/unreal-mcp-main/Docs/Tools/editor_tools.md", "words": 412}, {"slug": "unreal_mcp_main_node_tools_md", "title": "node_tools.md", "repo": "unreal-mcp-main", "path": "/Users/sniper/Downloads/    SNIPED_OS/unreal-mcp-main/Docs/Tools/node_tools.md", "words": 913}, {"slug": "unreal_mcp_main_blueprint_tools_md", "title": "blueprint_tools.md", "repo": "unreal-mcp-main", "path": "/Users/sniper/Downloads/    SNIPED_OS/unreal-mcp-main/Docs/Tools/blueprint_tools.md", "words": 1038}, {"slug": "unreal_mcp_main_actor_tools_md", "title": "actor_tools.md", "repo": "unreal-mcp-main", "path": "/Users/sniper/Downloads/    SNIPED_OS/unreal-mcp-main/Docs/Tools/actor_tools.md", "words": 609}, {"slug": "unreal_mcp_main_copilot_instructions_md", "title": "copilot-instructions.md", "repo": "unreal-mcp-main", "path": "/Users/sniper/Downloads/    SNIPED_OS/unreal-mcp-main/.github/copilot-instructions.md", "words": 216}, {"slug": "video_use_main_poster_html", "title": "poster.html", "repo": "video-use-main", "path": "/Users/sniper/Downloads/    SNIPED_OS/video-use-main/poster.html", "words": 1692}], [{"slug": "video_use_main_equations_md", "title": "equations.md", "repo": "video-use-main", "path": "/Users/sniper/Downloads/    SNIPED_OS/video-use-main/skills/manim-video/references/equations.md", "words": 705}, {"slug": "video_use_main_graphs_and_data_md", "title": "graphs-and-data.md", "repo": "video-use-main", "path": "/Users/sniper/Downloads/    SNIPED_OS/video-use-main/skills/manim-video/references/graphs-and-data.md", "words": 482}, {"slug": "video_use_main_visual_design_md", "title": "visual-design.md", "repo": "video-use-main", "path": "/Users/sniper/Downloads/    SNIPED_OS/video-use-main/skills/manim-video/references/visual-design.md", "words": 651}, {"slug": "video_use_main_rendering_md", "title": "rendering.md", "repo": "video-use-main", "path": "/Users/sniper/Downloads/    SNIPED_OS/video-use-main/skills/manim-video/references/rendering.md", "words": 651}, {"slug": "video_use_main_animation_design_thinking_md", "title": "animation-design-thinking.md", "repo": "video-use-main", "path": "/Users/sniper/Downloads/    SNIPED_OS/video-use-main/skills/manim-video/references/animation-design-thinking.md", "words": 1117}, {"slug": "video_use_main_animations_md", "title": "animations.md", "repo": "video-use-main", "path": "/Users/sniper/Downloads/    SNIPED_OS/video-use-main/skills/manim-video/references/animations.md", "words": 959}]]
const TOOLDOC = { type:'object', required:['slug','doc_type','what_it_does','capabilities','limits_or_gotchas','applies_in_sniped','disposition','coverage_complete','evidence'], properties:{ slug:{type:'string'}, doc_type:{type:'string',enum:['tool_capability','setup_guide','api_reference','research_note','artifact_or_misc']}, what_it_does:{type:'string'}, capabilities:{type:'array',items:{type:'string'}}, limits_or_gotchas:{type:'array',items:{type:'string'}}, applies_in_sniped:{type:'array',items:{type:'string'}}, disposition:{type:'string',enum:['tool_doc_bound','reference_active','misclassified_artifact','duplicate','fragment']}, coverage_complete:{type:'boolean'}, evidence:{type:'string'} } }
const GROUP_SCHEMA = { type:'object', required:['records'], properties:{ records:{type:'array',items:TOOLDOC,minItems:1,maxItems:6} } }
const VERDICT = { type:'object', required:['pass','coverage_verdict','evidence'], properties:{ pass:{type:'boolean'}, coverage_verdict:{type:'string',enum:['whole-read','partial','sampled']}, evidence:{type:'string'}, issues:{type:'array',items:{type:'string'}} } }
const out = await pipeline(
  GROUPS,
  async (group, _o, idx) => {
    const list = group.map((d) => `- slug=${d.slug} | ${d.repo}/${d.title} | FILE: ${d.path} (~${d.words} words)`).join('\n')
    const recs = await agent(
      `Whole-read each of these ${group.length} tool/MCP documentation files for the SNIPED OS. NEVER SAMPLE: open and read EACH file fully with the Read tool before writing its record.\nFiles:\n${list}\n\nFor EACH file emit one record with its exact slug. doc_type and disposition per the schema (tool_doc_bound real tool/capability/setup doc; reference_active context-only; misclassified_artifact build output like poster.html or copilot-instructions or terms; fragment empty stub). Fill all fields. coverage_complete=true only if you read the whole file. evidence = a short verbatim quote from the actual file.`,
      { label: `read:t1r-g${idx}`, phase: 'Read', schema: GROUP_SCHEMA, model: 'sonnet' }
    )
    return { group, recs }
  },
  async ({ group, recs }, _o, idx) => {
    const files = group.map((d) => d.path).join(' , ')
    const v = await agent(
      `Adversarial verifier for tool-doc records. The QUESTION is: did the READER genuinely whole-read each file and ground each record in it? It is NOT how many files you personally re-open.\n` +
      `Spot-check 2-3 of these files; confirm the evidence quotes appear verbatim and the dispositions are correct.\nFiles: ${files}\nRecords: ${JSON.stringify(recs)}\n\n` +
      `Return coverage_verdict='whole-read' if every record has coverage_complete=true with a grounded evidence quote AND your spot-checks confirm grounding (this is the expected pass). Return 'partial'/'sampled' ONLY if a record is ungrounded, thin, or an evidence quote does not appear in its file. pass=true unless a record is actually ungrounded.`,
      { label: `verify:t1r-g${idx}`, phase: 'Verify', schema: VERDICT, model: 'sonnet' }
    )
    return { recs, verdict: v }
  }
)
const clean = out.filter(Boolean)
const allRecs = clean.flatMap((r) => (r.recs && r.recs.records) || [])
log(`T1-retry: ${allRecs.length} records across ${clean.length} groups`)
return { groups: clean.map((r)=>({ records: r.recs && r.recs.records, verdict: r.verdict })), record_count: allRecs.length }
