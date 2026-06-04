export const meta = {
  name: 'starthere-wave2',
  description: 'Certify + distill 31 giant docx (>10 seg, 1248 segments) , sharded read + per-doc consolidation',
  phases: [
    { title: 'Shard-read', detail: 'haiku readers, ~10 segments each, distill the portion' },
    { title: 'Consolidate', detail: 'sonnet merges a doc\'s shards into one doctrine' }
  ]
}

const BASE = '/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/_segments'
const OUT = '/tmp/wave2_out'
const SHARD = 10

const SHARD_SCHEMA = {
  type: 'object',
  required: ['portion_doctrine', 'segments_read'],
  properties: {
    portion_doctrine: { type: 'string' }, segments_read: { type: 'integer' },
    skills: { type: 'array', items: { type: 'string' } }, gates: { type: 'array', items: { type: 'string' } },
    tools: { type: 'array', items: { type: 'string' } }, prompts: { type: 'array', items: { type: 'string' } },
    operating_rules: { type: 'array', items: { type: 'string' } }, content_ideas: { type: 'array', items: { type: 'string' } },
    contradictions: { type: 'array', items: { type: 'string' } }, weird_gold: { type: 'array', items: { type: 'string' } }
  }
}
const DOC_SCHEMA = {
  type: 'object',
  required: ['file_class', 'signal', 'doctrine', 'cert_status'],
  properties: {
    file_class: { type: 'string' }, signal: { type: 'string' }, doctrine: { type: 'string' },
    cert_status: { type: 'string' }, notes: { type: 'string' }
  }
}

const docs = typeof args === 'string' ? JSON.parse(args) : args
if (!Array.isArray(docs)) throw new Error('args not array')

const results = await parallel(docs.map(([id, name, segs]) => () => {
  const shards = []
  for (let s = 1; s <= segs; s += SHARD) shards.push([s, Math.min(s + SHARD - 1, segs)])
  return parallel(shards.map(([a, b]) => () => {
    const paths = []
    for (let i = a; i <= b; i++) paths.push(`${BASE}/${id}/seg_${String(i).padStart(3, '0')}.txt`)
    const cat = 'cat "' + paths.join('" "') + '"'
    const prompt = `Read segments ${a}-${b} (of ${segs} total) of document "${name}". Run this and read ALL output:\n${cat}\nDistill the REAL content of THIS portion only: operating rules, named methods, numbers, specific tactics, prompts, tools. STRIP boilerplate/ads/UI/nav/repetition. If this portion is mostly junk, say so briefly and keep only any gold. segments_read = ${b - a + 1} if you read them all. Also harvest arrays (skills, gates, tools, prompts, operating_rules, content_ideas, contradictions, weird_gold). Finally run \`mkdir -p ${OUT}\` and write your JSON to ${OUT}/${id}__s${a}.json`
    return agent(prompt, { schema: SHARD_SCHEMA, model: 'haiku', phase: 'Shard-read', label: `${name.slice(0, 14)}:${a}-${b}` })
      .then(r => r ? { ...r, a, b } : null)
  })).then(parts => {
    parts = (parts || []).filter(Boolean)
    const segread = parts.reduce((n, p) => n + (p.segments_read || 0), 0)
    const merged = parts.map((p, i) => `[part ${i + 1}, seg ${p.a}-${p.b}]\n${p.portion_doctrine}`).join('\n\n')
    const prompt = `Consolidate ${parts.length} partial distillations of document "${name}" (${segs} segments total) into ONE coherent, de-duplicated doctrine. Classify file_class (one of: high_signal_source, low_signal_source, scrape, transcript, raw_dump, financial_record, artifact) and signal (high|medium|low) based on the WHOLE doc. cert_status='certified'. Keep only real, usable operating knowledge; drop repetition. Partials:\n\n${merged}\n\nFinally write your JSON to ${OUT}/${id}.json via bash.`
    return agent(prompt, { schema: DOC_SCHEMA, model: 'sonnet', phase: 'Consolidate', label: `merge:${name.slice(0, 18)}` })
      .then(r => r ? { doc_id: id, name, file_class: r.file_class, signal: r.signal, cert_status: r.cert_status, expected_segs: segs, segments_read: segread, shards: parts.length } : { doc_id: id, name, cert_status: 'exception', expected_segs: segs, segments_read: segread, shards: parts.length })
  })
})).then(rs => rs.filter(Boolean))

const mism = results.filter(r => r.segments_read !== r.expected_segs)
log(`Wave 2 complete: ${results.length}/${docs.length} docs, ${mism.length} coverage-mismatch`)
return { docs: results.length, mismatch: mism.map(r => `${r.name}:${r.segments_read}/${r.expected_segs}`), classes: results.map(r => `${r.name}=${r.file_class || '?'}/${r.signal || '?'}`) }
