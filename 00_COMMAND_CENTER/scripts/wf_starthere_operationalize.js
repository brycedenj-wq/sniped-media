export const meta = {
  name: 'starthere-operationalize',
  description: 'Convert Start Here docs into callable technique cards tagged by tool family',
  phases: [{ title: 'Extract', detail: 'one agent per doc, schema-validated cards' }],
}

const CARD_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['doc', 'cards', 'note'],
  properties: {
    doc: { type: 'string' },
    note: { type: 'string', description: 'coverage note: what was sampled vs skipped, residual for giants' },
    cards: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['problem','technique','exact_steps','app','tool_family','output_artifact','when_to_use','quality_failure_prevented','gate_it_fixes','source_segment','confidence'],
        properties: {
          problem: { type: 'string', description: 'the concrete problem/symptom this fixes, keyword rich' },
          technique: { type: 'string', description: 'the named technique' },
          exact_steps: { type: 'string', description: 'exact, ordered, executable steps. tool menus/sliders/values where given.' },
          app: { type: 'string', description: 'exact tool/app/model e.g. Photoshop, Lightroom, Higgsfield+Seedance, Figma, Blender, Premiere, After Effects, Instantly' },
          tool_family: { type: 'string', enum: ['higgsfield','adobe','premiere','after_effects','figma','blender','social','money','copy','sales','photo','claude','multi'] },
          model: { type: 'string', description: 'specific model if relevant (Kling 3.0, Seedance, nano banana pro, Firefly Ultra) else empty' },
          inputs_needed: { type: 'string' },
          prompt_pattern: { type: 'string', description: 'reusable prompt template if applicable, else empty' },
          output_artifact: { type: 'string', description: 'what artifact this produces' },
          when_to_use: { type: 'string' },
          when_not: { type: 'string' },
          quality_failure_prevented: { type: 'string', description: 'the specific bad outcome this card prevents' },
          gate_it_fixes: { type: 'string', description: 'which gate this satisfies: elite_art_direction / premium_stack / higgsfield_compliance / motion_edit / buyer_readiness / pricing / client_fit / none' },
          route_it_activates: { type: 'string' },
          example_command: { type: 'string' },
          source_segment: { type: 'string', description: 'approx line range or section heading in the doc' },
          confidence: { type: 'string', enum: ['high','medium','low'] },
        },
      },
    },
  },
}

const BASE = '/Users/sniper/AI-Brain-Refinery/01_KNOWLEDGE_BASE/STARTHERE_SOURCE_ARCHIVE/_extracted_text'
const DOCS = [["series 3 download.txt",918511],["astro claude websites 3x faster.txt",851199],["new hot shit .txt",838784],["high level convos.txt",684626],["series 5 download.txt",378263],["NEXT INFO GRABS.txt",329062],["gary2.0 use.txt",321935],["series 1 download.txt",216177],["youtube skool doc.txt",196895],["SOCIAL MEDIA 3.0 MAY USE.txt",193081],["last lightroom hopefully.txt",189750],["meta everything use.txt",143677],["ai after ramon.txt",137066],["takeover after ramon.txt",134205],["claude thursday 4:23.txt",111895],["last ig growth strat.txt",87796],["LOCATION SCOUTING OG.txt",86849],["mostly Powerhouse-.txt",76124],["sniped figma.txt",73184],["gary thread.txt",70251],["chat Sniped MAster thread.txt",69537],["FASHION KILLA.txt",68456],["claude cowork genius.txt",66376],["claude for small business.txt",66234],["using ai x gumroad x digital products.txt",55649],["MONEY MONEY AND MORE MONEY AND GETTING AHEAD .txt",55213],["FINDING MODELS ANYWHERE OG.txt",52715],["use blender like this.txt",41116],["Gemini.txt",37131],["set up ai.txt",31713],["COURSE WORK 1 thru 2.txt",26754],["PHOTOGRAPHY MONEY GUIDE.txt",24753],["LA PHOTOGRPAHY.txt",24050],["garyvee gameplan.txt",21791],["THREADS.txt",18820],["SOCIAL_MEDIA_3_0_REFERENCE.txt",17190],["branding x clothes gold.txt",14384],["AI CHANGED EVERYTHING.txt",14120],["MOSTLY PHOTOGRPAHY SETS SET DESIGN .txt",13866],["The_Claude_Stack.txt",12145],["The_Platform_Stack.txt",12022],["The_Offer_Stack.txt",11929],["Built an AI SaaS in 20 min.txt",11544],["The_Revenue_Stack.txt",11336],["The_Attention_Stack.txt",10958],["CLAUDE CODE SUPERPOWERS.txt",8800],["legal contracts and service business contracts.txt",8737],["NEW TAKEOVER HANDLE WITH CARE.txt",6794],["The_Direction_Shift_Master_v2.txt",6227],["PHOTO PIONEERS VIDEO TEXT.txt",6203],["sniped_os_knowledge_dump.txt",5811],["The_Adobe_Stack_Manual.txt",4558],["Direction_Stack_90Day_Plan.txt",3514],["The_Operator_Playbook.txt",3406],["CLAUDE CODE PLUGIN.txt",3368],["REMOTION.txt",3164],["Claude_Operating_Manual.txt",2909],["claude_for_small_business_organized.txt",2779],["ICP Definition Worksheet.txt",2614],["THE_REAL_PLAN_Rebrand_Revenue_Execution.txt",2604],["GaryVee_Attention_Operating_System.txt",2532],["Cold_Outreach_Sales_Pipeline_Playbook.txt",2487],["Brand_Builders_Playbook.txt",2380],["Digital_Products_AI_Services_Playbook.txt",2371],["6_Content_Marketing_OS (1).txt",2167],["SNIPED_Chat_Prompts_Reference.txt",2119],["Finding Your Edge.txt",1979],["Copywriting_Playbook.txt",1963],["Photography_Editing_Playbook.txt",1946],["Contracts_Legal_Protection_Playbook.txt",1911],["Pixieset_Operations_Reference.txt",1897],["BIZ EXPENSES.txt",1795],["Photography_Revenue_Playbook.txt",1725],["Higgsfield_AI_Operator_Playbook.txt",1668],["Money_Wealth_Getting_Ahead.txt",1638],["life story.txt",1458],["Weekly Reflections.txt",1399],["Setting Goals.txt",1264],["sniped_context_tools_only.txt",911],["Art_Series.txt",870],["Aesthetic_Statement_v1.txt",634],["Prompt Template - Combining Techniques-2.txt",450],["Prompt Template - Problem Decomposition.txt",347],["Prompt Template - Thought Generation-2.txt",344],["Prompt Template - In Context-2.txt",333]]
const items = DOCS.map(([d, w]) => ({ doc: d, words: w, path: `${BASE}/${d}` }))
log(`extracting cards from ${items.length} Start Here docs`)

function cap(words) {
  if (words > 200000) return 15
  if (words > 50000) return 10
  if (words > 8000) return 7
  return 4
}

const results = await pipeline(
  items,
  (it) => {
    const N = cap(it.words)
    const huge = it.words > 120000
    const sampling = huge
      ? `This doc is ${it.words} words (large). You CANNOT read it all (Read caps ~25k tokens/call and errors above). Read in windows with offset/limit (about 1200 lines per call). Sample to COVER the whole doc: read the opening, several evenly-spaced middle windows, and the end. Prioritize technique-dense regions (step lists, settings, prompt formulas, exact menu paths). In "note", state which line ranges you sampled and that deeper residual extraction is QUEUED.`
      : `Read the whole doc (use offset/limit windows of ~1200 lines if needed to stay under the 25k-token Read cap).`
    return agent(
      `You convert an operator's how-to doc into CALLABLE technique cards for a one-person AI-native campaign house OS. This is operating SOURCE CODE, not a summary.

DOC: ${it.doc}
PATH: ${it.path}
APPROX WORDS: ${it.words}

${sampling}

Extract up to ${N} of the HIGHEST-VALUE, DISTINCT, CONCRETE technique cards. A card must be an executable technique with exact steps and a specific tool, never a vibe or a restated principle. If the doc is mostly chat noise / motivation / duplicated content, return fewer cards (even zero) and say so in note. Do NOT invent steps not supported by the doc.

For each card fill the schema fully:
- problem: keyword-rich symptom statement (what goes wrong) so the OS can match it on a failed gate
- technique: the named move
- exact_steps: ordered, executable, with concrete menu paths / sliders / values when the doc gives them
- app + tool_family (pick from the enum) + model if relevant
- prompt_pattern: a reusable template if the doc gives one, else empty
- output_artifact, when_to_use, when_not, quality_failure_prevented
- gate_it_fixes: which OS gate it satisfies (elite_art_direction / premium_stack / higgsfield_compliance / motion_edit / buyer_readiness / pricing / client_fit / none)
- source_segment: approx line range or heading
- confidence

tool_family routing guide: Higgsfield/Seedance/Kling/Soul/nano-banana/WAN/Veo/upscale -> higgsfield. Photoshop/Lightroom/Firefly/Camera Raw/Express/Evoto -> adobe. Premiere/timeline/cutting/transitions -> premiere. After Effects/motion graphics/kinetic type -> after_effects. Figma/design system/deck -> figma. Blender/3D/render -> blender. IG/reels/hooks/attention/posting/algorithm -> social. offers/pricing/revenue/value-equation -> money. headlines/captions/body copy/story -> copy. cold outreach/DMs/pipeline/ICP/objections -> sales. posing/lighting/location/moodboard/wardrobe/models -> photo. Claude Code/MCP/agents/SaaS-build -> claude. cross-tool pipeline -> multi.

Return ONLY the structured object.`,
      { label: `extract:${it.doc.slice(0, 28)}`, phase: 'Extract', schema: CARD_SCHEMA }
    ).catch(() => ({ doc: it.doc, cards: [], note: 'extraction failed' }))
  }
)

const clean = results.filter(Boolean)
const totalCards = clean.reduce((s, r) => s + (r.cards ? r.cards.length : 0), 0)
log(`done: ${totalCards} cards from ${clean.length} docs`)
return { perDoc: clean, totalCards }
