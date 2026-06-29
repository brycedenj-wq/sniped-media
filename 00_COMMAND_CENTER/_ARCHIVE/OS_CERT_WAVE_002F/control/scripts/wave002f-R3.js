export const meta = {
  name: 'wave002f-R3',
  description: 'Wave 002-F: whole-read + segment-ledger certify books, extract 5-field doctrine, adversarially verify',
  phases: [
    { title: 'Read', detail: 'one reader per book-part, whole-read, segment ledger + doctrine observations' },
    { title: 'Certify', detail: 'synthesize the 5-field doctrine record per book' },
    { title: 'Verify', detail: 'adversarial verifier spot-checks the record against the real text' },
  ],
}

const BOOKS = [{"slug": "al_ramadan_dave_peterson_christopher_loc", "title": "Al Ramadan, Dave Peterson, Christopher Lochhead, Kevin Maney - Play Bigger_ How Pirates, D", "parts": 2, "units": [{"part": 1, "file": "/tmp/wave002f/parts/al_ramadan_dave_peterson_christopher_loc_p1.txt", "words": 40096}, {"part": 2, "file": "/tmp/wave002f/parts/al_ramadan_dave_peterson_christopher_loc_p2.txt", "words": 40096}]}, {"slug": "chris_dixon_read_write_own_building_the_", "title": "Chris Dixon - Read Write Own_ Building the Next Era of the Internet (2024, Random House) -", "parts": 2, "units": [{"part": 1, "file": "/tmp/wave002f/parts/chris_dixon_read_write_own_building_the__p1.txt", "words": 40532}, {"part": 2, "file": "/tmp/wave002f/parts/chris_dixon_read_write_own_building_the__p2.txt", "words": 40532}]}, {"slug": "daugherty_paul_r_wilson_h_james_human_ma", "title": "Daugherty, Paul R._Wilson, H. James - Human + machine_ reimagining work in the age of AI (", "parts": 2, "units": [{"part": 1, "file": "/tmp/wave002f/parts/daugherty_paul_r_wilson_h_james_human_ma_p1.txt", "words": 29521}, {"part": 2, "file": "/tmp/wave002f/parts/daugherty_paul_r_wilson_h_james_human_ma_p2.txt", "words": 29520}]}, {"slug": "eric_berne_games_people_play_the_basic_h", "title": "Eric Berne - Games People Play_ The Basic Handbook of Transactional Analysis. (1996, Balla", "parts": 2, "units": [{"part": 1, "file": "/tmp/wave002f/parts/eric_berne_games_people_play_the_basic_h_p1.txt", "words": 25137}, {"part": 2, "file": "/tmp/wave002f/parts/eric_berne_games_people_play_the_basic_h_p2.txt", "words": 25136}]}, {"slug": "howard_marks_mastering_the_market_cycle_", "title": "Howard Marks - Mastering the Market Cycle_ Getting the Odds on Your Side (2018, Houghton M", "parts": 2, "units": [{"part": 1, "file": "/tmp/wave002f/parts/howard_marks_mastering_the_market_cycle__p1.txt", "words": 41837}, {"part": 2, "file": "/tmp/wave002f/parts/howard_marks_mastering_the_market_cycle__p2.txt", "words": 41837}]}]

const PART = {
  type: 'object', required: ['slug','part','words_seen','coverage_complete','segments','observations'],
  properties: {
    slug:{type:'string'}, part:{type:'integer'}, words_seen:{type:'integer'},
    coverage_complete:{type:'boolean'},
    segments:{type:'array',minItems:2,maxItems:12,items:{type:'object',required:['section','covers','key_claims'],properties:{section:{type:'string'},covers:{type:'string'},key_claims:{type:'array',items:{type:'string'},minItems:1,maxItems:4}}}},
    observations:{type:'array',items:{type:'string'},minItems:2,maxItems:8},
  },
}
const BOOK = {
  type:'object', required:['slug','segment_count','coverage_complete','operating_principles','patterns_to_steal','traps_to_avoid','applies_in_sniped','does_not_apply'],
  properties:{
    slug:{type:'string'}, segment_count:{type:'integer'}, coverage_complete:{type:'boolean'},
    operating_principles:{type:'array',items:{type:'string'},minItems:3,maxItems:7},
    patterns_to_steal:{type:'array',items:{type:'string'},minItems:2,maxItems:6},
    traps_to_avoid:{type:'array',items:{type:'string'},minItems:1,maxItems:5},
    applies_in_sniped:{type:'array',items:{type:'string'},minItems:1,maxItems:5},
    does_not_apply:{type:'array',items:{type:'string'},minItems:1,maxItems:4},
  },
}
const VERDICT = {
  type:'object', required:['slug','coverage_verdict','pass','evidence'],
  properties:{slug:{type:'string'},coverage_verdict:{type:'string',enum:['whole-read','partial','sampled']},pass:{type:'boolean'},evidence:{type:'string'},issues:{type:'array',items:{type:'string'}}},
}

const out = await pipeline(
  BOOKS,
  async (book) => {
    const parts = await parallel(book.units.map((u) => () => agent(
      `Certify a part of a book for the SNIPED OS by WHOLE-READING it. NEVER SAMPLE. This is part ${u.part} of ${book.parts} of "${book.title}".\n` +
      `File: ${u.file} (about ${u.words} words). Read the ENTIRE file start to finish, paging with the Read tool offset/limit until EOF. Do not skim or summarize from prior knowledge.\n` +
      `Emit a segment ledger for THIS part (sections with key_claims from the actual text) and 2-8 observations (operating principles, patterns to steal, traps). coverage_complete=true only if you read the whole part.`,
      { label: `read:${book.slug}#${u.part}`, phase: 'Read', schema: PART, model: 'sonnet' }
    )))
    return { book, parts: parts.filter(Boolean) }
  },
  async ({ book, parts }) => {
    const rec = await agent(
      `Synthesize the SNIPED doctrine record for "${book.title}" from its whole-read part ledgers (read in full across ${book.parts} part(s); do not re-read).\n` +
      `Part ledgers:\n${JSON.stringify(parts)}\n\n` +
      `Produce the 5-field record: operating_principles, patterns_to_steal (concrete moves to lift into SNIPED), traps_to_avoid, applies_in_sniped (specific skills/lanes/decisions), does_not_apply (where it misleads or does not fit a solo AI-augmented creative studio). segment_count = total across parts.`,
      { label: `certify:${book.slug}`, phase: 'Certify', schema: BOOK, model: 'sonnet' }
    )
    return { book, parts, rec }
  },
  async ({ book, parts, rec }) => {
    const files = book.units.map((u) => u.file).join(' , ')
    const v = await agent(
      `Adversarial verifier. Do not trust the readers. Confirm "${book.title}" was genuinely WHOLE-READ across all ${book.parts} part(s), not sampled.\n` +
      `Part files to spot-check: ${files}\n` +
      `Doctrine record:\n${JSON.stringify(rec)}\n\n` +
      `Open 2-3 of the part files, read different regions (start/middle/end). Confirm claims appear in the text, the parts span the whole book, and the atoms are grounded not generic. If any part looks unread or atoms are vague, verdict=sampled/partial. pass=true only for a grounded whole-read.`,
      { label: `verify:${book.slug}`, phase: 'Verify', schema: VERDICT, model: 'sonnet' }
    )
    return { slug: book.slug, title: book.title, rec, verdict: v }
  }
)

const clean = out.filter(Boolean)
const passed = clean.filter((r) => r.verdict && r.verdict.pass && r.verdict.coverage_verdict === 'whole-read')
const failed = clean.filter((r) => !(r.verdict && r.verdict.pass && r.verdict.coverage_verdict === 'whole-read'))
log(`002-F wave002f-R3 certified+verified: ${passed.length}/${BOOKS.length}; needs-rework: ${failed.length}`)
return {
  passed: passed.map((r) => ({ slug: r.slug, title: r.title, verdict: r.verdict.coverage_verdict })),
  failed: failed.map((r) => ({ slug: r.slug, title: r.title, verdict: r.verdict && r.verdict.coverage_verdict, issues: r.verdict && r.verdict.issues })),
  records: clean.map((r) => ({ slug: r.slug, title: r.title, rec: r.rec, verdict: r.verdict })),
}
