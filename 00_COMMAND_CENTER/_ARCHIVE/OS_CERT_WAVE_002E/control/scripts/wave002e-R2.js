export const meta = {
  name: 'wave002e-R2',
  description: 'Wave 002-E: whole-read + segment-ledger certify books, extract 5-field doctrine, adversarially verify',
  phases: [
    { title: 'Read', detail: 'one reader per book-part, whole-read, segment ledger + doctrine observations' },
    { title: 'Certify', detail: 'synthesize the 5-field doctrine record per book' },
    { title: 'Verify', detail: 'adversarial verifier spot-checks the record against the real text' },
  ],
}

const BOOKS = [{"slug": "christian_dior_dior_by_dior_the_autobiog", "title": "Christian Dior - Dior by Dior- The Autobiography of Christian Dior - libgen.li.pdf", "parts": 2, "units": [{"part": 1, "file": "/tmp/wave002e/parts/christian_dior_dior_by_dior_the_autobiog_p1.txt", "words": 36626}, {"part": 2, "file": "/tmp/wave002e/parts/christian_dior_dior_by_dior_the_autobiog_p2.txt", "words": 36626}]}, {"slug": "daniel_coyle_the_culture_code_the_secret", "title": "Daniel Coyle - The Culture Code_ The Secrets of Highly Successful Groups (2018, Bantam) -", "parts": 2, "units": [{"part": 1, "file": "/tmp/wave002e/parts/daniel_coyle_the_culture_code_the_secret_p1.txt", "words": 31641}, {"part": 2, "file": "/tmp/wave002e/parts/daniel_coyle_the_culture_code_the_secret_p2.txt", "words": 31640}]}, {"slug": "rick_rubin_the_creative_act_a_way_of_bei", "title": "Rick Rubin - The Creative Act_ A Way of Being (2023, Penguin Publishing Group) - libgen.l", "parts": 2, "units": [{"part": 1, "file": "/tmp/wave002e/parts/rick_rubin_the_creative_act_a_way_of_bei_p1.txt", "words": 23679}, {"part": 2, "file": "/tmp/wave002e/parts/rick_rubin_the_creative_act_a_way_of_bei_p2.txt", "words": 23678}]}, {"slug": "vreeland_diana_d_v_2011_harpercollins_li", "title": "Vreeland, Diana - D.V. (2011, HarperCollins) - libgen.li.epub", "parts": 2, "units": [{"part": 1, "file": "/tmp/wave002e/parts/vreeland_diana_d_v_2011_harpercollins_li_p1.txt", "words": 32492}, {"part": 2, "file": "/tmp/wave002e/parts/vreeland_diana_d_v_2011_harpercollins_li_p2.txt", "words": 32492}]}, {"slug": "airey_david_identity_designed_the_defini", "title": "Airey, David - Identity designed_ the definitive guide to visual branding (2019, Rockport", "parts": 2, "units": [{"part": 1, "file": "/tmp/wave002e/parts/airey_david_identity_designed_the_defini_p1.txt", "words": 27945}, {"part": 2, "file": "/tmp/wave002e/parts/airey_david_identity_designed_the_defini_p2.txt", "words": 27944}]}]

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
log(`002-E wave002e-R2 certified+verified: ${passed.length}/${BOOKS.length}; needs-rework: ${failed.length}`)
return {
  passed: passed.map((r) => ({ slug: r.slug, title: r.title, verdict: r.verdict.coverage_verdict })),
  failed: failed.map((r) => ({ slug: r.slug, title: r.title, verdict: r.verdict && r.verdict.coverage_verdict, issues: r.verdict && r.verdict.issues })),
  records: clean.map((r) => ({ slug: r.slug, title: r.title, rec: r.rec, verdict: r.verdict })),
}
