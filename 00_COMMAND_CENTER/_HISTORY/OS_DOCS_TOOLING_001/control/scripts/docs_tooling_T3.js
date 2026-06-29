export const meta = {
  name: 'docs-tooling-T3',
  description: 'Docs/Tooling T3: whole-read the misc readable docs (project planning notes + a large Blender technique doc), tool-doc record + disposition, adversarial verify.',
  phases: [ { title: 'Read' }, { title: 'Verify' } ],
}
const GROUPS = [[{"slug": "05_production_01_model_sourcing_md", "title": "01_MODEL_SOURCING.md", "repo": "05_PRODUCTION", "path": "/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/post_pipeline/SHOOTS/_TEST_alma-love_proof/DROP_ENGINE_SHOOT_2026-06-06/01_MODEL_SOURCING.md", "read_path": "/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/post_pipeline/SHOOTS/_TEST_alma-love_proof/DROP_ENGINE_SHOOT_2026-06-06/01_MODEL_SOURCING.md", "words": 552}, {"slug": "05_production_02_model_dm_templates_md", "title": "02_MODEL_DM_TEMPLATES.md", "repo": "05_PRODUCTION", "path": "/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/post_pipeline/SHOOTS/_TEST_alma-love_proof/DROP_ENGINE_SHOOT_2026-06-06/02_MODEL_DM_TEMPLATES.md", "read_path": "/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/post_pipeline/SHOOTS/_TEST_alma-love_proof/DROP_ENGINE_SHOOT_2026-06-06/02_MODEL_DM_TEMPLATES.md", "words": 334}, {"slug": "05_production_03_capture_plan_md", "title": "03_CAPTURE_PLAN.md", "repo": "05_PRODUCTION", "path": "/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/post_pipeline/SHOOTS/_TEST_alma-love_proof/DROP_ENGINE_SHOOT_2026-06-06/03_CAPTURE_PLAN.md", "read_path": "/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/post_pipeline/SHOOTS/_TEST_alma-love_proof/DROP_ENGINE_SHOOT_2026-06-06/03_CAPTURE_PLAN.md", "words": 525}, {"slug": "05_production_04_ig_story_plan_md", "title": "04_IG_STORY_PLAN.md", "repo": "05_PRODUCTION", "path": "/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/post_pipeline/SHOOTS/_TEST_alma-love_proof/DROP_ENGINE_SHOOT_2026-06-06/04_IG_STORY_PLAN.md", "read_path": "/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/post_pipeline/SHOOTS/_TEST_alma-love_proof/DROP_ENGINE_SHOOT_2026-06-06/04_IG_STORY_PLAN.md", "words": 334}], [{"slug": "start_here_use_blender_like_this_docx", "title": "use blender like this.docx", "repo": "start here", "path": "/Users/sniper/Downloads/    SNIPED_OS/start here/use blender like this.docx", "read_path": "/var/folders/0c/1tyf4g1n5js6fh04_nnc6_6r0000gn/T/tmpaq4yq_kg.txt", "words": 41116}]]
const TOOLDOC = { type:'object', required:['slug','doc_type','what_it_does','capabilities','limits_or_gotchas','applies_in_sniped','disposition','coverage_complete','evidence'], properties:{ slug:{type:'string'}, doc_type:{type:'string',enum:['tool_capability','setup_guide','api_reference','research_note','artifact_or_misc','project_note']}, what_it_does:{type:'string'}, capabilities:{type:'array',items:{type:'string'}}, limits_or_gotchas:{type:'array',items:{type:'string'}}, applies_in_sniped:{type:'array',items:{type:'string'}}, disposition:{type:'string',enum:['tool_doc_bound','reference_active','misclassified_artifact','project_note_capsule','duplicate','fragment']}, coverage_complete:{type:'boolean'}, evidence:{type:'string'} } }
const GROUP_SCHEMA = { type:'object', required:['records'], properties:{ records:{type:'array',items:TOOLDOC,minItems:1,maxItems:6} } }
const VERDICT = { type:'object', required:['pass','coverage_verdict','evidence'], properties:{ pass:{type:'boolean'}, coverage_verdict:{type:'string',enum:['whole-read','partial','sampled']}, evidence:{type:'string'}, issues:{type:'array',items:{type:'string'}} } }
const out = await pipeline(
  GROUPS,
  async (group, _o, idx) => {
    const list = group.map((d) => `- slug=${d.slug} | ${d.repo}/${d.title} | FILE: ${d.read_path} (~${d.words} words)`).join('\n')
    const recs = await agent(
      `Whole-read each of these ${group.length} document(s) for the SNIPED OS. NEVER SAMPLE: page through each file fully with the Read tool (offset/limit to EOF) before writing its record.\nFiles:\n${list}\n\n` +
      `For EACH file emit one record with its exact slug. doc_type: tool_capability (a how-to/technique doc like the Blender doc), project_note (a specific shoot's planning notes: model sourcing, DM templates, capture plan, IG plan), or artifact_or_misc.\n` +
      `disposition: tool_doc_bound (a real reusable technique/tool doctrine that changes how the OS works, e.g. a substantial Blender how-to); project_note_capsule (project-specific planning material that belongs in a project capsule, NOT permanent OS doctrine, per the project-context firewall); reference_active; misclassified_artifact; fragment.\n` +
      `Fill all fields. coverage_complete=true only if you read the whole file. evidence = a verbatim quote from the actual file.`,
      { label: `read:t3-g${idx}`, phase: 'Read', schema: GROUP_SCHEMA, model: 'sonnet' }
    )
    return { group, recs }
  },
  async ({ group, recs }, _o, idx) => {
    const files = group.map((d) => d.read_path).join(' , ')
    const v = await agent(
      `Adversarial verifier. The QUESTION is whether the READER genuinely whole-read each file and grounded each record. Spot-check 2-3 regions of the larger file(s); confirm evidence quotes appear verbatim and dispositions are correct (a 41k-word Blender how-to is tool_doc_bound; tiny shoot-planning notes are project_note_capsule not OS doctrine).\nFiles: ${files}\nRecords: ${JSON.stringify(recs)}\n\n` +
      `coverage_verdict='whole-read' if records have coverage_complete=true + grounded evidence and your spot-checks confirm grounding. pass=true unless a record is ungrounded.`,
      { label: `verify:t3-g${idx}`, phase: 'Verify', schema: VERDICT, model: 'sonnet' }
    )
    return { recs, verdict: v }
  }
)
const clean = out.filter(Boolean)
const allRecs = clean.flatMap((r)=>(r.recs&&r.recs.records)||[])
log(`T3: ${allRecs.length} records across ${clean.length} groups`)
return { groups: clean.map((r)=>({ records: r.recs&&r.recs.records, verdict: r.verdict })), record_count: allRecs.length }
