export const meta = {
  name: 'book-top10-certify',
  description: 'Certify the Top-10 load-bearing books to the full segment-ledger standard + chunk-accuracy audit',
  phases: [{ title: 'Certify', detail: 'one sonnet reader per book: read all segments, distill, audit prior chunks' }]
}
const BASE = '/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/_segments'
const OUT = '/tmp/top10_out'
const SCHEMA = {
  type: 'object',
  required: ['file_class', 'signal', 'coverage_confirmed', 'segments_read', 'doctrine', 'chunk_accuracy', 'cert_status'],
  properties: {
    file_class: { type: 'string' }, signal: { type: 'string' },
    coverage_confirmed: { type: 'boolean' }, segments_read: { type: 'integer' },
    doctrine: { type: 'string' },
    supports: { type: 'array', items: { type: 'string' } },
    contradictions: { type: 'array', items: { type: 'string' } },
    chunk_accuracy: { type: 'string' },
    chunk_accuracy_note: { type: 'string' },
    skill_candidates: { type: 'array', items: { type: 'string' } },
    gate_candidates: { type: 'array', items: { type: 'string' } },
    workflow_candidates: { type: 'array', items: { type: 'string' } },
    cert_status: { type: 'string' }, notes: { type: 'string' }
  }
}
const books = typeof args === 'string' ? JSON.parse(args) : args
if (!Array.isArray(books)) throw new Error('args not array')

phase('Certify')
const results = await parallel(books.map(([bid, segs]) => () => {
  const paths = []
  for (let i = 1; i <= segs; i++) paths.push(`${BASE}/${bid}/seg_${String(i).padStart(3, '0')}.txt`)
  const cat = 'cat "' + paths.join('" "') + '"'
  const prompt = `Certify a BOOK to the segment-ledger standard. This is reliability work, be rigorous and honest.

STEP 1 , read the FULL text. Run and read ALL output:
${cat}
That is all ${segs} segments of the book "${bid}". Read the whole thing.

STEP 2 , audit the OS's PRIOR distillation. Run:
cat /tmp/book_chunks/${bid}.json
Those are the existing concept-chunks the OS made WITHOUT a full read. Judge them against the full text.

STEP 3 , return JSON:
- file_class (high_signal_source / low_signal_source), signal (high/medium/low).
- coverage_confirmed = true ONLY if you read all ${segs} segments. segments_read = ${segs} if you did.
- doctrine = a DENSE, usable distillation of the book's real operating knowledge (named methods, frameworks, specific rules). Not a summary of fluff.
- supports = which OS components this book backs (pick from: positioning/sales-flow, offer-design, copywriting/voice, discovery/proof-loop, leverage/possibility, capital-allocation/money, photo-theory/AI-defense, composition/set-design, decision/systems).
- contradictions = corrections to common OS beliefs, or internal tensions, or where the book disagrees with how the OS uses it. Empty if none.
- chunk_accuracy = one of: accurate / partial / misleading. chunk_accuracy_note = 1-2 lines: did the prior chunks capture the book, or miss/distort the core? Be specific.
- skill_candidates / gate_candidates / workflow_candidates = ONLY genuinely executable+repeatable procedures (chunk-to-skill rule). Empty if the book is pure knowledge (most will be empty). Do NOT invent skills.
- cert_status = 'certified' if you read all ${segs} segments, else 'partial'.

STEP 4 , persist: run \`mkdir -p ${OUT}\` then write your full JSON to ${OUT}/${bid}.json`
  return agent(prompt, { schema: SCHEMA, model: 'sonnet', phase: 'Certify', label: `cert:${bid}` })
    .then(r => r ? { ...r, book_id: bid, expected_segs: segs } : { book_id: bid, cert_status: 'exception', expected_segs: segs })
})).then(rs => rs.filter(Boolean))

const cert = results.filter(r => r.cert_status === 'certified' && r.coverage_confirmed && r.segments_read === r.expected_segs)
const mism = results.filter(r => r.segments_read !== r.expected_segs)
log(`Top-10 books: ${cert.length}/${books.length} certified, ${mism.length} coverage-mismatch`)
return {
  certified: cert.length, total: books.length,
  mismatch: mism.map(r => `${r.book_id}:${r.segments_read}/${r.expected_segs}`),
  chunk_audit: results.map(r => `${r.book_id}=${r.chunk_accuracy || '?'}`),
  signals: results.map(r => `${r.book_id}=${r.signal || '?'}`)
}
