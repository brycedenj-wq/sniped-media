export const meta = {
  name: 'higgs-levelup',
  description: 'Whole-read Higgsfield Cinema Studio / Supercomputer / Marketing Studio video transcripts, extract the photoreal-cinema playbook',
  phases: [
    { title: 'Digest', detail: 'each agent whole-reads its transcripts, extracts realism techniques' },
    { title: 'Synthesize', detail: 'compile the level-up playbook + the Alma realism plan' },
  ],
}
const A = args || {}
const dir = A.dir
const groups = A.groups || []

const EXTRACT_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['feature_area','what_it_is','photoreal_techniques','workflow_steps','settings_models','kill_ai_tells','applies_to_alma'],
  properties: {
    feature_area: { type: 'string', description: 'Cinema Studio / Supercomputer / Marketing Studio / Seedance / general' },
    what_it_is: { type: 'string' },
    photoreal_techniques: { type: 'array', items: { type: 'string' }, description: 'concrete techniques to make AI video indistinguishable from real cinema' },
    workflow_steps: { type: 'array', items: { type: 'string' } },
    settings_models: { type: 'array', items: { type: 'string' }, description: 'specific models, params, resolution, settings named' },
    kill_ai_tells: { type: 'array', items: { type: 'string' }, description: 'how they remove AI tells (signage/text, plastic skin, bad physics, morphing, etc.)' },
    applies_to_alma: { type: 'string', description: 'how this applies to a photoreal 1970s Americana fashion commercial' },
  },
}

phase('Digest')
const digests = await parallel(groups.map((g, i) => () =>
  agent(
    `You are leveling up a film team's Higgsfield skills toward INDISTINGUISHABLE-FROM-REAL cinema (a paying fashion commercial that must never read as AI). Whole-read these transcript file(s) end to end (do NOT skim): ${g.map(id => `${dir}/${id}.txt`).join(', ')}. Use Bash 'cat' or Read on each. Extract every concrete, actionable technique for PHOTOREALISM and high-end cinema with Higgsfield (Cinema Studio, Supercomputer, Marketing Studio, Seedance 2.0, Kling, Nano Banana, Soul, camera/director controls). Focus on: how to make it look real, how to kill AI tells (gibberish signage/text, plastic skin, morphing, bad physics, too-clean look), character/world consistency, the production workflow, and exact models/settings named. Be specific and quote the video where useful. Em-dashes are banned; use commas/periods. Return ONLY the structured object.`,
    { label: `digest:${g.join(',')}`, phase: 'Digest', schema: EXTRACT_SCHEMA, model: 'sonnet' }
  )
))
const valid = digests.filter(Boolean)

phase('Synthesize')
const packet = valid.map((d, i) => `### ${d.feature_area}\nWHAT: ${d.what_it_is}\nPHOTOREAL: ${d.photoreal_techniques.join(' | ')}\nWORKFLOW: ${d.workflow_steps.join(' | ')}\nMODELS/SETTINGS: ${d.settings_models.join(' | ')}\nKILL-TELLS: ${d.kill_ai_tells.join(' | ')}\nALMA: ${d.applies_to_alma}`).join('\n\n')

const playbook = await agent(
  `You are the lead. ${valid.length} agents digested Higgsfield product videos for INDISTINGUISHABLE-FROM-REAL cinema. Synthesize ONE tight, de-duplicated LEVEL-UP PLAYBOOK in markdown for a film team, then a specific plan for an existing 1970s-Americana fashion commercial (Alma Love Club: a woman in a cherry-print bikini around a black Mercedes on an empty Beverly Hills boulevard, day to night) whose current AI cut reads "mid" with tells like gibberish storefront signage. The playbook MUST cover: (1) which Higgsfield features/models to use for max realism and why (Cinema Studio, Supercomputer, Seedance 2.0, etc.), (2) a concrete photoreal generation workflow, (3) a hard checklist to KILL AI tells (signage/text, plastic skin, morphing, physics, over-clean look), (4) prompt/camera/lighting craft for realism, (5) the exact next actions to re-produce the weak Alma beats (especially the establishing street with the fake signage) at indistinguishable-cinema quality. Be concrete and prescriptive, no fluff. Em-dashes banned. Output the markdown document only.\n\nDIGESTS:\n${packet}`,
  { label: 'synthesize-playbook', phase: 'Synthesize', model: 'opus' }
)

return { digestCount: valid.length, playbook }
