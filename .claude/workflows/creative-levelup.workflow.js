// creative-levelup.workflow.js
// IN-HOUSE v1 EXECUTION RESOURCE for the SNIPED OS.
//
// WHEN IT FIRES: a weak creative input arrives (a thin client concept, a flat campaign
// idea, a generic film idea, a launch story with no engine, a brand or product story that
// reads "mid") and the operator wants the OS to UPGRADE it before any generation spend.
// This is the story-first gate: it runs BEFORE the creative/AI-film pipeline, never after.
//
// INPUTS REQUIRED (args contract):
//   material     (required) the weak concept text, verbatim. If empty -> ASK-HUMAN path.
//   type         (optional) one of: concept | campaign | film | launch_story | brand_story | product_story
//   constraints  (optional) what MUST be preserved: product, taste, identity, budget, channel.
//
// OUTPUT FORMAT: a structured upgrade packet (diagnosis, preserved constraints, 3 divergent
//   upgrades, synthesis, final concept with premise/desire-engine/world/character/visual-language/
//   copy+tagline, an honest adversarial /10 scorecard, and the single NEXT execution step).
//
// QUALITY GATE: the final concept must clear the inline adversarial scorer at >= 8/10 on every
//   axis (story-psychology, taste, emotional-pull, anti-slop). Below 8 on any axis -> verdict
//   REWORK and the packet says exactly what to fix. Mirrors the standing
//   .claude/workflows/adversarial-verify.workflow.js refute-then-synthesize shape.
//
// PROOF / RECEIPT: this is a pre-production thinking harness, not a disk-writing production run,
//   so it does not itself init os_proof_manifest.py. The receipt requirement passes DOWNSTREAM:
//   the moment the chosen next step is a production build, that build runs os_activate.py +
//   os_proof_manifest.py and ends in OS_RECEIPT.md (os_receipt.py), enforced by the Stop hook.
//   The packet states this handoff explicitly so completion cannot be faked.
//
// WHEN TO ASK THE HUMAN: (1) material empty -> return ASK-HUMAN note, do not invent a concept.
//   (2) constraints absent on a client/product/identity task -> the constraints phase flags the
//   unknowns the operator must confirm before generation (it does NOT guess product/identity).
//
// DEPENDS ON (read and cited):
//   - 00_COMMAND_CENTER/scripts/os_doctrine.py  (world_character, copy, visual_grade packs + rules)
//   - 00_COMMAND_CENTER/OS_ELEVATED_AI_FILM_DOCTRINE_2026-06-09.md  (log-line-first, desire engine, authored motion, anti-slideshow)
//   - 00_COMMAND_CENTER/COMMERCIAL_CRAFT_BENCHMARK_V2.md  (format-first classification, payoff, expensive-vs-amateur)
//   - 00_COMMAND_CENTER/scripts/os_activate.py  (the story-first GATE concept: pass story before generation)
//   - intel_status_psychology.md  (status is signaled not stated; desire/aspiration mechanics)
//   - feedback_lineage_doctrine.md  (cultural specificity from inside a lineage, never tourism)
//   - .claude/workflows/adversarial-verify.workflow.js  (the refute-then-synthesize verify shape this reuses)
// EXTERNAL-RESOURCE GAP: current platform-specific generation limits (model hit-rates, moderation
//   quirks, credit costs) are NOT encoded here; the chosen next step pulls them from the live
//   higgsfield / kling skills at build time. This harness stays tool-agnostic on purpose.

export const meta = {
  name: 'creative-levelup',
  description: 'Take WEAK creative material and upgrade it through the OS doctrine packs before any generation spend. Diagnose why it is weak in doctrine language, lock the constraints to preserve, run 3 divergent upgrades, synthesize the strongest, produce the final concept, adversarially score it /10, and hand off the next execution step.',
  whenToUse: 'A thin client concept, flat campaign idea, generic film idea, or weak launch/brand/product story needs to be elevated before boarding or generating. The story-first gate that sits ABOVE the creative pipeline.',
  phases: [
    { title: 'Diagnose', detail: 'Name why the original is weak in os_doctrine + elevated-film + benchmark language.' },
    { title: 'Constraints', detail: 'Lock what must be preserved: product, taste, identity, budget, channel. Flag unknowns for the operator.' },
    { title: 'Diverge', detail: 'Three parallel upgrades: desire/tension/stakes lens, world+character+lineage lens, luxury-taste+copy/positioning lens.' },
    { title: 'Synthesize', detail: 'Fuse the strongest moves into one version.' },
    { title: 'FinalConcept', detail: 'Premise, desire engine, world, character, visual language, copy/tagline.' },
    { title: 'AdversarialScore', detail: 'Honest /10 across story-psychology, taste, emotional-pull, anti-slop. Refute then verdict.' },
    { title: 'NextStep', detail: 'The single next execution step: hand to creative pipeline / ai-edl / shot list, with the proof handoff.' }
  ]
}

const A = args || {}
const material = (A.material || A.concept || '').trim()
const type = A.type || 'concept'
const constraints = A.constraints || ''

// ASK-HUMAN path: no material = nothing to upgrade. Do not invent.
if (!material) {
  log('creative-levelup: no material supplied.')
  return {
    status: 'ASK_HUMAN',
    note: 'No creative material to upgrade. Re-run with args.material set to the weak concept text (the client concept / campaign idea / film idea / launch or brand or product story you want elevated). Optional: args.type (concept|campaign|film|launch_story|brand_story|product_story) and args.constraints (product, taste, identity, budget, channel that must be preserved).'
  }
}

// Shared doctrine context injected into every agent so the harness moves as one OS body.
// This is the os_doctrine.py "load" direction: feed certified doctrine INTO the moment of creation.
const DOCTRINE = `OS DOCTRINE CONTEXT (apply at the moment of creation, cite by name):
- os_doctrine.py world_character pack: a reason to care beyond "AI consistency works" = tension + stakes + a built-in arc; cultural specificity from INSIDE a lineage, never tourism (feedback_lineage_doctrine.md); status is SIGNALED not stated (intel_status_psychology.md); faceless-safe; a five-second-drawable mark + one color law.
- os_doctrine.py copy pack: one big idea per piece; benefit and meaning not feature lists; write in the world's voice never in bible/spec language; no self-applied hype (world-class, seamless, unlock, elevate, leverage, game-changer, next-level, revolutionary); a complete thought never a fragment; NO em-dashes.
- os_doctrine.py visual_grade pack: quiet-luxury editorial restraint; one disciplined saturated color, everything else neutral; the output must BEAT an honest camera frame; restraint over volume.
- OS_ELEVATED_AI_FILM_DOCTRINE_2026-06-09.md: lock the LOG LINE before a single frame (problem, intention, obstacle, solution); personify ONE; feeling-first; a still + push-in is NOT a film shot; a slideshow of near-stills is the number-one "mid" tell.
- COMMERCIAL_CRAFT_BENCHMARK_V2.md: classify the FORMAT first; every piece needs a PAYOFF; expensive = motivated cuts, pacing contrast, restraint, one owned title system; amateur = monotone, unmotivated, flat catalog product.
- os_activate.py story-first GATE: a serious creative task must pass STORY before any generation spend. This harness IS that gate.
HARD: no em-dashes anywhere. Faceless-safe, no real identity. Stay generic and reusable, no project specifics.`

// ----------------------------------------------------------------------------
phase('Diagnose')
const DIAG = {
  type: 'object',
  required: ['failures', 'root_cause', 'one_line_verdict'],
  properties: {
    failures: {
      type: 'array',
      description: 'Each named weakness, in doctrine language, cited to the pack/doc it violates.',
      items: {
        type: 'object',
        required: ['failure', 'doctrine_violated'],
        properties: {
          failure: { type: 'string' },
          doctrine_violated: { type: 'string', description: 'e.g. world_character: no tension/stakes/arc; elevated-film: no log line; copy: generic hype; benchmark: no payoff' }
        }
      }
    },
    root_cause: { type: 'string', description: 'The single structural reason it reads weak, not a cosmetic list.' },
    one_line_verdict: { type: 'string' }
  }
}
const diagnosis = await agent(
  `${DOCTRINE}\n\nDIAGNOSE why this ${type} is WEAK. Name each failure in the doctrine's own language and cite the pack/doc it violates. Find the ONE root structural cause (usually: no desire engine, no tension/stakes/arc, tourism not lineage, generic hype copy, slideshow with no payoff, or status stated not signaled). Be specific and honest, no flattery.\n\nMATERIAL:\n${material}`,
  { schema: DIAG, label: 'diagnose', phase: 'Diagnose' }
)

// ----------------------------------------------------------------------------
phase('Constraints')
const CONS = {
  type: 'object',
  required: ['preserve', 'unknowns_for_operator'],
  properties: {
    preserve: {
      type: 'object',
      description: 'What the upgrade MUST keep intact. Pull from args.constraints first, infer the rest conservatively.',
      properties: {
        product: { type: 'string' },
        taste: { type: 'string' },
        identity: { type: 'string' },
        budget: { type: 'string' },
        channel: { type: 'string' }
      }
    },
    unknowns_for_operator: {
      type: 'array',
      description: 'Constraints that CANNOT be safely guessed (exact product, real identity, hard budget). Ask the operator before generation. Do not invent these.',
      items: { type: 'string' }
    }
  }
}
const cons = await agent(
  `${DOCTRINE}\n\nLOCK THE CONSTRAINTS to preserve through the upgrade. The upgrade may reframe the STORY freely but must never silently change a fixed product, the brand taste, a real identity, or the budget/channel. Stated constraints: "${constraints || 'none stated'}". List what to preserve, and separately list the unknowns the operator must confirm (never guess product, identity, or hard budget). Faceless-safe.\n\nMATERIAL:\n${material}`,
  { schema: CONS, label: 'constraints', phase: 'Constraints' }
)

// ----------------------------------------------------------------------------
phase('Diverge')
const UPGRADE = {
  type: 'object',
  required: ['lens', 'premise', 'why_stronger', 'one_risk'],
  properties: {
    lens: { type: 'string' },
    premise: { type: 'string', description: 'The upgraded core idea in 1-2 sentences, in the world voice (not bible language).' },
    desire_or_hook: { type: 'string', description: 'What the audience WANTS or the tension that pulls them in.' },
    why_stronger: { type: 'string', description: 'Cite the doctrine move that makes it stronger.' },
    one_risk: { type: 'string' }
  }
}
const LENSES = [
  { key: 'desire', brief: 'DESIRE / TENSION / STAKES lens. Build a desire engine and a real obstacle. Personify ONE. Add a time/urgency constraint. Give it a built-in arc and a payoff (elevated-film + benchmark). Status is signaled not stated.' },
  { key: 'world', brief: 'WORLD + CHARACTER + LINEAGE lens (os_doctrine world_character). Cultural specificity from INSIDE a lineage, never tourism (feedback_lineage_doctrine.md). A five-second-drawable mark, one color law, a reason to care beyond consistency. Faceless-safe.' },
  { key: 'taste', brief: 'LUXURY / FASHION-TASTE + COPY / POSITIONING lens. Quiet-luxury editorial restraint (visual_grade), one disciplined color. Copy = one big idea, benefit and meaning, world voice, no hype, no em-dash (copy pack). Premium-as-insurance positioning.' }
]
const upgrades = (await parallel(
  LENSES.map(L => () => agent(
    `${DOCTRINE}\n\nProduce ONE divergent UPGRADE of this ${type} through the ${L.brief}\n\nKeep the locked constraints intact: ${JSON.stringify(cons.preserve)}. Diverge hard from the original and from the other lenses, do not hedge to the middle.\n\nORIGINAL MATERIAL:\n${material}\n\nDIAGNOSIS (what to fix): ${diagnosis.one_line_verdict} | root cause: ${diagnosis.root_cause}`,
    { schema: UPGRADE, label: `upgrade:${L.key}`, phase: 'Diverge' }
  ))
)).filter(Boolean)

// ----------------------------------------------------------------------------
phase('Synthesize')
const SYN = {
  type: 'object',
  required: ['synthesis', 'kept_from_each', 'killed'],
  properties: {
    synthesis: { type: 'string', description: 'The single strongest version, fusing the best move from each lens into one coherent idea.' },
    kept_from_each: { type: 'array', items: { type: 'string' } },
    killed: { type: 'array', items: { type: 'string' }, description: 'Darlings cut because they do not serve the premise (kill via the log line).' }
  }
}
const syn = await agent(
  `${DOCTRINE}\n\nSYNTHESIZE the three upgrades into ONE strongest version. Take the best move from each lens, fuse them coherently, and KILL anything that does not serve the premise (kill darlings via the log line, elevated-film F20). Keep constraints intact: ${JSON.stringify(cons.preserve)}.\n\nUPGRADES:\n${JSON.stringify(upgrades)}`,
  { schema: SYN, label: 'synthesize', phase: 'Synthesize' }
)

// ----------------------------------------------------------------------------
phase('FinalConcept')
const FINAL = {
  type: 'object',
  required: ['premise', 'desire_engine', 'world', 'character', 'visual_language', 'tagline'],
  properties: {
    premise: { type: 'string', description: 'The locked log line: problem, intention to overcome, obstacle, resolution.' },
    desire_engine: { type: 'string', description: 'What the audience wants + the tension/stakes that pull them through.' },
    world: { type: 'string', description: 'The lineage-true world, one color law, five-second mark. Faceless-safe.' },
    character: { type: 'string', description: 'The ONE we personify; status signaled not stated.' },
    visual_language: { type: 'string', description: 'Quiet-luxury editorial grade direction + format (per benchmark), motivated motion not slideshow.' },
    copy: { type: 'array', items: { type: 'string' }, description: 'Two or three lines of on-world copy, no hype, no em-dash, complete thoughts.' },
    tagline: { type: 'string', description: 'One owned line. One big idea. No em-dash.' }
  }
}
const final = await agent(
  `${DOCTRINE}\n\nProduce the FINAL upgraded concept from the synthesis. Fill every field. Copy and tagline must pass the os_doctrine copy pack (complete thought, one big idea, world voice, no hype, no em-dash). Visual language must name the format (COMMERCIAL_CRAFT_BENCHMARK_V2) and specify motivated motion, never slideshow.\n\nSYNTHESIS:\n${JSON.stringify(syn)}\n\nCONSTRAINTS TO PRESERVE: ${JSON.stringify(cons.preserve)}`,
  { schema: FINAL, label: 'final-concept', phase: 'FinalConcept' }
)

// ----------------------------------------------------------------------------
phase('AdversarialScore')
// Reuses the adversarial-verify.workflow.js shape: refute per-axis in parallel, then a verdict.
// A model cannot crown its own work; this is the second-pass hostile read (orchestration law 3).
const AXES = [
  { key: 'story_psychology', lens: 'Does it have a real desire engine, tension, stakes, an arc, a payoff? Or is it still a flat idea with a logo? (elevated-film, benchmark payoff, status_psychology)' },
  { key: 'taste', lens: 'Quiet-luxury restraint or generic and busy? One disciplined color or noise? Owned title system or template? (visual_grade, layout)' },
  { key: 'emotional_pull', lens: 'Would a stranger feel something in the first beat? Is ONE person personified? Or is it abstract/statistical? (elevated-film personify-one, feeling-first)' },
  { key: 'anti_slop', lens: 'Any AI-slop tells: hype copy, em-dashes, bible/spec language, tourism-not-lineage, slideshow of near-stills, status stated not signaled? Hunt them.' }
]
const VERDICT = {
  type: 'object',
  required: ['axis', 'score', 'evidence', 'fix_if_below_8'],
  properties: {
    axis: { type: 'string' },
    score: { type: 'integer', description: 'Honest 0-10. Do not flatter. 8 is the floor to pass.' },
    evidence: { type: 'string' },
    fix_if_below_8: { type: 'string' }
  }
}
const votes = (await parallel(
  AXES.map(ax => () => agent(
    `${DOCTRINE}\n\nADVERSARIAL READ. You did not write this and you want to break it. Score the axis [${ax.key}] honestly 0-10 (8 is the pass floor). Give concrete evidence from the concept and, if below 8, the exact fix.\nAXIS LENS: ${ax.lens}\n\nFINAL CONCEPT:\n${JSON.stringify(final)}`,
    { schema: VERDICT, label: `refute:${ax.key}`, phase: 'AdversarialScore' }
  ))
)).filter(Boolean)

const minScore = votes.reduce((m, v) => Math.min(m, v.score), 10)
const overallVerdict = minScore >= 8 ? 'PASS' : 'REWORK'

// ----------------------------------------------------------------------------
phase('NextStep')
const NEXT = {
  type: 'object',
  required: ['verdict', 'next_step', 'handoff_target', 'proof_handoff'],
  properties: {
    verdict: { type: 'string' },
    next_step: { type: 'string', description: 'The single concrete next action.' },
    handoff_target: { type: 'string', description: 'creative pipeline (banana-pro-director / cinema-worldbuilder) | ai-edl + shot list | copy/layout build | back to rework.' },
    rework_notes: { type: 'array', items: { type: 'string' }, description: 'If REWORK: the exact below-8 fixes to apply before re-running.' },
    proof_handoff: { type: 'string', description: 'State that the production build MUST run os_activate.py + os_proof_manifest.py and end in OS_RECEIPT.md (os_receipt.py), enforced by the Stop hook. End every downstream harness with adversarial-verify.' }
  }
}
const next = await agent(
  `${DOCTRINE}\n\nProduce the NEXT execution step. Verdict is ${overallVerdict} (min axis score ${minScore}/10). If PASS, hand the locked concept to the right builder: film/launch -> shot list + ai-edl + creative pipeline (cinema-worldbuilder / banana-pro-director); brand/product/campaign -> copy/layout/composite build. If REWORK, list the exact below-8 fixes and route back to this harness. Always state the proof handoff: the production build runs os_activate.py + os_proof_manifest.py and ends in OS_RECEIPT.md, and every downstream harness ends with adversarial-verify.\n\nSCORES:\n${JSON.stringify(votes)}\nVERDICT: ${overallVerdict}`,
  { schema: NEXT, label: 'next-step', phase: 'NextStep' }
)

return {
  status: 'COMPLETE',
  type,
  diagnosis,
  constraints: cons,
  upgrades,
  synthesis: syn,
  final_concept: final,
  scorecard: { axes: votes, min_score: minScore, verdict: overallVerdict, floor: 8 },
  next_step: next,
  cited_sources: [
    'os_doctrine.py (world_character, copy, visual_grade packs)',
    'OS_ELEVATED_AI_FILM_DOCTRINE_2026-06-09.md',
    'COMMERCIAL_CRAFT_BENCHMARK_V2.md',
    'os_activate.py (story-first GATE)',
    'intel_status_psychology.md',
    'feedback_lineage_doctrine.md',
    '.claude/workflows/adversarial-verify.workflow.js'
  ]
}

