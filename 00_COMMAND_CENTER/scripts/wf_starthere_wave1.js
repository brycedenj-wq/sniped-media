export const meta = {
  name: 'starthere-wave1',
  description: 'Certify + distill 61 small/medium docx (<=10 seg) from the start-here folder with full coverage proof',
  phases: [{ title: 'Certify+Distill', detail: 'one reader agent per doc: read all segments, classify honestly, distill + harvest' }]
}

const BASE = '/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/_segments'
const OUT = '/tmp/wave1_out'
const SCHEMA = {
  type: 'object',
  required: ['file_class', 'signal', 'coverage_confirmed', 'segments_read', 'doctrine', 'cert_status'],
  properties: {
    file_class: { type: 'string' },
    signal: { type: 'string' },
    coverage_confirmed: { type: 'boolean' },
    segments_read: { type: 'integer' },
    doctrine: { type: 'string' },
    skills: { type: 'array', items: { type: 'string' } },
    gates: { type: 'array', items: { type: 'string' } },
    workflows: { type: 'array', items: { type: 'string' } },
    prompts: { type: 'array', items: { type: 'string' } },
    tools: { type: 'array', items: { type: 'string' } },
    operating_rules: { type: 'array', items: { type: 'string' } },
    content_ideas: { type: 'array', items: { type: 'string' } },
    contradictions: { type: 'array', items: { type: 'string' } },
    weird_gold: { type: 'array', items: { type: 'string' } },
    cert_status: { type: 'string' },
    notes: { type: 'string' }
  }
}

phase('Certify+Distill')
const docs = typeof args === 'string' ? JSON.parse(args) : args
if (!Array.isArray(docs)) throw new Error('args is not an array: ' + typeof docs)
const results = await parallel(docs.map(([id, name, segs]) => () => {
  const paths = Array.from({ length: segs }, (_, i) => `${BASE}/${id}/seg_${String(i + 1).padStart(3, '0')}.txt`)
  const catcmd = 'cat "' + paths.join('" "') + '"'
  const prompt = `Certify ONE document for an operating system. STEP 1: read EVERY one of these ${segs} segment file(s) COMPLETELY by running this bash command and reading all output:\n${catcmd}\nThey are the full text of "${name}". Read the WHOLE thing before judging its value.\n\nSTEP 2: return the JSON. file_class is one of: high_signal_source, low_signal_source, scrape, transcript, raw_dump, financial_record, artifact, duplicate. signal is high|medium|low. coverage_confirmed = true ONLY if you actually read all ${segs} segment(s). segments_read = how many you read. doctrine = a DENSE, usable distillation of the REAL content (operating rules, numbers, named methods, specific tactics) — strip boilerplate/ads/UI/nav; if the doc is mostly junk say so and keep only the gold. Harvest arrays (each a list of short strings, empty if none): skills, gates, workflows, prompts, tools, operating_rules, content_ideas, contradictions, weird_gold. cert_status='certified' if you read all ${segs} segment(s), else 'partial'. Be brutally honest about low-signal scrapes.\n\nSTEP 3: also persist your answer: run \`mkdir -p ${OUT}\` then write your full JSON to ${OUT}/${id}.json`
  return agent(prompt, { schema: SCHEMA, model: 'haiku', label: `cert:${name.slice(0, 22)}`, phase: 'Certify+Distill' })
    .then(r => r ? { ...r, doc_id: id, name, expected_segs: segs } : null)
})).then(rs => rs.filter(Boolean))

const certified = results.filter(r => r.cert_status === 'certified' && r.coverage_confirmed)
const mismatch = results.filter(r => r.segments_read !== r.expected_segs)
log(`Wave 1 complete: ${results.length}/${docs.length} returned, ${certified.length} certified, ${mismatch.length} coverage-mismatch`)
return { total: docs.length, returned: results.length, certified: certified.length, mismatch: mismatch.map(r => r.name) }
