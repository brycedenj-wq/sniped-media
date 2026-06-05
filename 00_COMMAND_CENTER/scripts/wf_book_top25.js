export const meta = {
  name: 'book-top25-certify',
  description: 'Certify the Top-25 (next 12) load-bearing books to the segment-ledger standard + chunk audit',
  phases: [{ title: 'Certify', detail: 'single sonnet reader (<=14 seg) or shard+consolidate (>14)' }]
}
const BASE = '/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/_segments'
const OUT = '/tmp/top25_out'
const SINGLE_MAX = 14, SHARD = 10
const SCHEMA = {
  type: 'object',
  required: ['file_class', 'signal', 'coverage_confirmed', 'segments_read', 'doctrine', 'chunk_accuracy', 'cert_status'],
  properties: {
    file_class: { type: 'string' }, signal: { type: 'string' }, coverage_confirmed: { type: 'boolean' },
    segments_read: { type: 'integer' }, doctrine: { type: 'string' },
    supports: { type: 'array', items: { type: 'string' } }, contradictions: { type: 'array', items: { type: 'string' } },
    chunk_accuracy: { type: 'string' }, chunk_accuracy_note: { type: 'string' },
    skill_candidates: { type: 'array', items: { type: 'string' } }, gate_candidates: { type: 'array', items: { type: 'string' } },
    workflow_candidates: { type: 'array', items: { type: 'string' } }, cert_status: { type: 'string' }, notes: { type: 'string' }
  }
}
const SHARD_SCHEMA = { type: 'object', required: ['portion_doctrine', 'segments_read'],
  properties: { portion_doctrine: { type: 'string' }, segments_read: { type: 'integer' } } }

function paths(bid, a, b) { const p = []; for (let i = a; i <= b; i++) p.push(`${BASE}/${bid}/seg_${String(i).padStart(3, '0')}.txt`); return p }
function instr(bid, segs, fulltext) {
  return `STEP 2 , audit the OS's prior distillation. Run: cat /tmp/book_chunks/${bid}.json , the existing concept-chunks made WITHOUT a full read. Judge them against ${fulltext ? 'the full text above' : 'the consolidated distillation'}.
STEP 3 , return JSON: file_class (high/low_signal_source), signal; coverage_confirmed=true only if all ${segs} segments are covered; segments_read=${segs}; doctrine=DENSE usable distillation (named methods/frameworks/rules); supports=OS components (positioning/sales-flow, offer-design, copywriting/voice, discovery/proof-loop, leverage/possibility, capital-allocation/money, photo-theory, composition, decision/systems, status/pricing, hospitality, longevity); contradictions=corrections to OS beliefs or where the book disagrees with how the OS uses it; chunk_accuracy=accurate|partial|misleading + chunk_accuracy_note (specific: captured or missed/distorted?); skill/gate/workflow_candidates=ONLY genuinely executable+repeatable procedures (most empty); cert_status='certified' if all ${segs} read.
STEP 4 , run \`mkdir -p ${OUT}\` and write your full JSON to ${OUT}/${bid}.json`
}

const books = typeof args === 'string' ? JSON.parse(args) : args
if (!Array.isArray(books)) throw new Error('args not array')

phase('Certify')
const results = await parallel(books.map(([bid, segs]) => () => {
  if (segs <= SINGLE_MAX) {
    const cat = 'cat "' + paths(bid, 1, segs).join('" "') + '"'
    const prompt = `Certify a BOOK to the segment-ledger standard. Be rigorous and honest.\nSTEP 1 , read the FULL text. Run and read ALL output:\n${cat}\nThat is all ${segs} segments of "${bid}".\n${instr(bid, segs, true)}`
    return agent(prompt, { schema: SCHEMA, model: 'sonnet', phase: 'Certify', label: `cert:${bid}` })
      .then(r => r ? { ...r, book_id: bid, expected_segs: segs } : { book_id: bid, cert_status: 'exception', expected_segs: segs })
  }
  // sharded
  const shards = []
  for (let s = 1; s <= segs; s += SHARD) shards.push([s, Math.min(s + SHARD - 1, segs)])
  return parallel(shards.map(([a, b]) => () => {
    const cat = 'cat "' + paths(bid, a, b).join('" "') + '"'
    return agent(`Read segments ${a}-${b} of ${segs} of book "${bid}": ${cat}\nDistill the REAL operating content of THIS portion (methods, frameworks, rules), strip filler. segments_read=${b - a + 1} if read all.`,
      { schema: SHARD_SCHEMA, model: 'haiku', phase: 'Certify', label: `${bid}:${a}-${b}` }).then(r => r ? { ...r, a, b } : null)
  })).then(parts => {
    parts = (parts || []).filter(Boolean)
    const segread = parts.reduce((n, p) => n + (p.segments_read || 0), 0)
    const merged = parts.map((p, i) => `[seg ${p.a}-${p.b}] ${p.portion_doctrine}`).join('\n\n')
    const prompt = `Consolidate the full distillation of book "${bid}" (${segs} segments, read in parts below) and certify it.\nFULL DISTILLATION:\n${merged}\n\n${instr(bid, segs, false)}`
    return agent(prompt, { schema: SCHEMA, model: 'sonnet', phase: 'Certify', label: `merge:${bid}` })
      .then(r => r ? { ...r, book_id: bid, expected_segs: segs, segments_read: segread } : { book_id: bid, cert_status: 'exception', expected_segs: segs, segments_read: segread })
  })
})).then(rs => rs.filter(Boolean))

const cert = results.filter(r => r.cert_status === 'certified' && r.segments_read === r.expected_segs)
const mism = results.filter(r => r.segments_read !== r.expected_segs)
log(`Top-25 books: ${cert.length}/${books.length} certified, ${mism.length} mismatch`)
return { certified: cert.length, total: books.length, mismatch: mism.map(r => `${r.book_id}:${r.segments_read}/${r.expected_segs}`),
  chunk_audit: results.map(r => `${r.book_id}=${r.chunk_accuracy || '?'}`), signals: results.map(r => `${r.book_id}=${r.signal || '?'}`) }
