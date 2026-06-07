# OS STORY + PSYCHOLOGY OPERATIONALIZATION DASHBOARD

Built 2026-06-07. Makes the storytelling/psychology/narrative corpus think INSIDE the OS - cards the OS loads and gates against before any commercial edit, campaign, deck, caption, script, offer, or buyer-facing asset. Not passive chunks.

## Sources scanned (by content, not filename)
| Source | Type | Disposition | Why | Affects |
| --- | --- | --- | --- | --- |
| `Storytelling game.docx` (Callaway, 1B+ views) | story structure / hooks / rhythm / tone / direction | **USED** | 6 operational techniques, directly editable | story + hook + caption + editing libraries |
| `Things Fall Apart` (Achebe) | character / world / archetype / tragic arc | **USED** | character-with-governing-trait + world-rules-then-break + proverb compression | character/world + narrative + copy libraries |
| SNIPED corpus skills (hit-mechanics/Thompson, status-psychology, new-luxury/Silverstein, trust-equation, hospitality, blockbuster) | psychology / buyer / status | **USED (referenced)** | already-canon frameworks wired as card sources | psychology + buyer-desire libraries |
| OS_COMMERCIAL_CRAFT_CARDS.json | editing craft | **USED (composes)** | story layer sits alongside craft layer, both auto-load | reference gate |
| Remaining book corpus (hundreds) | mixed | **QUEUED** | not yet carded; top underused listed below | future card extraction |

## Cards created
16 story-intelligence cards in `story_psychology_layer/STORY_INTELLIGENCE_CARDS.json`. Each has problem / when / story principle / psychology principle / application / bad-output-prevented / gate / source / Alma example.

## Libraries (VIEWS over the one card store, not piles)
8 libraries via `os_story_gate.py libraries`:
STORYTELLING_OPERATOR (5) · PSYCHOLOGY_OPERATOR (4) · COMMERCIAL_NARRATIVE (5) · ATTENTION_HOOK (3) · CHARACTER_AND_WORLD (3) · BUYER_DESIRE (3) · CAPTION_AND_COPY (4) · VISUAL_STORY_EDITING (5).

## Gates created
- **STORY_GATE** (`os_story_gate.py gate`): 9 proof questions - tension, feeling, desire/status, hook, payoff, character/world, withhold/reveal, sequence logic (but/therefore), source cards. No edit/deck/caption/campaign is "strong" until all answered.

## Routers updated
- `os_library.py` PROJECTS now auto-load **STORY_PSYCHOLOGY_LAYER** for: video_campaign, social_rollout, photo_post, still_range, brand_ip_system, offer, ad, deck, film. Verified: `os_library.py load video_campaign` surfaces the 16-card layer + the gate command in the manifest.
- `os_story_gate.py load <type>` returns the exact card-libraries for video_campaign / social_rollout / photo_post / still_range / brand_ip_system / offer / deck / client_package.

## Acceptance tests
12/12 prompts return card + source + library + gate + application + next action. Proof: `story_psychology_layer/ACCEPTANCE_TEST_PROOF.md`.

## Alma Love implications
Full application: `story_psychology_layer/ALMA_LOVE_STORY_LAYER.md`. Headline: the reel premise is "the suit survives the chaos" (poise vs malfunctioning luxury); arc is but/therefore not and-then; hook is the lens-swipe or speaker-drag interruption; payoff is the held seated poster; iPhone chaos + Canon luxury are both required; pretty-but-tensionless shots get cut.

## Top underused books/frameworks (queue for next carding pass)
- The deeper persuasion/copy corpus (beyond the 6 Callaway techniques).
- Berger/Dyer photo-theory (taken vs made image) -> visual-story cards.
- Perennial-seller / blockbuster economics -> offer/rollout cards.
- Full Achebe character/tragedy mechanics -> more character/world cards.

## Remaining gaps
- Only 16 cards carded so far (proof-of-concept depth); the corpus supports hundreds.
- STORY_GATE is a checklist + resolver, not yet an automated pass/fail score on a finished file (next: wire into os_reference_gate as a story sub-score).
- Achebe used at principle level (character/world/proverb), not passage-cited line by line.

## Command to use this layer
```
python3 00_COMMAND_CENTER/scripts/os_library.py load <project_type>     # auto-loads STORY_PSYCHOLOGY_LAYER
python3 00_COMMAND_CENTER/scripts/os_story_gate.py load <project_type>  # the exact story/psych cards
python3 00_COMMAND_CENTER/scripts/os_story_gate.py ask "<your problem>" # card + source + next action
python3 00_COMMAND_CENTER/scripts/os_story_gate.py gate                 # the 9-question STORY GATE
```
