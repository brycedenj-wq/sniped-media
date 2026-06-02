# CLASSICAL_STRATEGY source index · 2026-05-24

batch_id `CLASSICAL_STRATEGY` · 18 chunks · 4 sources · per-source attribution · NO new domain (`strategy` anchor). The first lane of the sequenced CLASSICAL_STRATEGY_OPERATING_CANON.

## Sources

| source_file | source_title | author | format | chunks |
|---|---|---|---|---:|
| `the_prince_machiavelli.txt` | The Prince | Niccolo Machiavelli | pdf | 4 |
| `on_war_clausewitz.txt` | On War | Carl von Clausewitz | pdf | 5 (incl synthesis 017) |
| `meditations_marcus_aurelius.txt` | Meditations | Marcus Aurelius | epub | 5 (incl synthesis 018) |
| `landmark_caesar.txt` | The Landmark Julius Caesar (Web Essays) | Robert B. Strassler (ed.) | pdf | 4 |

## Chunk map

| chunk_id | domain | concept |
|---|---|---|
| CLASSICAL_STRATEGY_001 | power | Feared versus loved: be feared without being hated (Machiavelli) |
| CLASSICAL_STRATEGY_002 | power | The fox and the lion: combine cunning with force (Machiavelli) |
| CLASSICAL_STRATEGY_003 | strategy | Rely on your own arms, not mercenaries (Machiavelli) |
| CLASSICAL_STRATEGY_004 | ethics | Realpolitik read honestly: effect over intention, timing of hard and soft moves (Machiavelli) |
| CLASSICAL_STRATEGY_005 | strategy | War as the continuation of politics by other means (Clausewitz) |
| CLASSICAL_STRATEGY_006 | mental-models | Friction: why everything in war is harder than it looks (Clausewitz) |
| CLASSICAL_STRATEGY_007 | mental-models | The center of gravity: concentrate against the decisive point (Clausewitz) |
| CLASSICAL_STRATEGY_008 | strategy | The culminating point and the strength of the defensive (Clausewitz) |
| CLASSICAL_STRATEGY_009 | mindset | The dichotomy of control: govern your judgments, not externals (Marcus Aurelius) |
| CLASSICAL_STRATEGY_010 | operator-doctrine | Duty and the present: do the work in front of you (Marcus Aurelius) |
| CLASSICAL_STRATEGY_011 | mindset | Nothing external can hinder the inner citadel (Marcus Aurelius) |
| CLASSICAL_STRATEGY_012 | mindset | Memento mori: impermanence as a source of clarity and proportion (Marcus Aurelius) |
| CLASSICAL_STRATEGY_013 | leadership | Command, audacity, and calculated risk (Caesar) |
| CLASSICAL_STRATEGY_014 | strategy | Clemency as strategy: clementia that made his position credible (Caesar) |
| CLASSICAL_STRATEGY_015 | operator-process | Control your own narrative: the Commentaries as self-account (Caesar) |
| CLASSICAL_STRATEGY_016 | leadership | The bond with his soldiers: loyalty earned through shared stake (Caesar) |
| CLASSICAL_STRATEGY_017 | strategy | Synthesis: the classical-strategy operating pattern (cross-source) |
| CLASSICAL_STRATEGY_018 | operator-doctrine | Synthesis: pattern-library discipline and the optionality guardrail (cross-source) |

## Domain distribution (existing domains only · NO new domain)

| domain | chunks |
|---|---:|
| strategy (anchor) | 5 |
| mindset | 3 |
| power | 2 |
| mental-models | 2 |
| operator-doctrine | 2 |
| leadership | 2 |
| ethics | 1 |
| operator-process | 1 |

`philosophy`, `statecraft`, `war`, `history`, `politics`, `military`, `empire` were NOT created or used. `strategy` anchors; the Stoic material routes to `mindset` + `operator-doctrine` + `ethics` (NOT a `philosophy` domain); Clausewitz's war-theory routes to `strategy` + `mental-models` + `leadership` (NOT a `war` domain); Caesar's command routes to `leadership` + `strategy` + `operator-process` (NOT `military`/`empire`/`history`). `mental-models` (a thin domain at count 1) grows by 2 to 3.

## Notes

- Two synthesis chunks: 017 (strategy · cross-source · the classical-strategy operating pattern, citing On War) and 018 (operator-doctrine · the interpretive-lens discipline + the optionality guardrail, citing Meditations).
- Per-source attribution; per-source counts Prince 4 / On War 5 / Meditations 5 / Caesar 4 (within the 4-5 target; the two synthesis chunks cite On War and Meditations respectively).
- **CURATED, not exhaustive:** 18 chunks from ~597,690 combined words · representative strategy/operator patterns, not chapter-by-chapter.
- **Honest, non-endorsing reading:** the Machiavelli realpolitik chunk (004) is explicitly read as analysis of how power behaves, NOT a directive for ruthless tactics; Caesar's Commentaries chunk (015) names them frankly as propaganda.
- **Meditations is treated as SECULAR operator-discipline (mindset / operator-doctrine), NOT a faith lane**; the Bible was not touched.
- Every chunk references CURRENT_OPERATOR_REALITY_BRIEF and carries the identity-optionality guardrail (strategy/power/operator pattern-library only · NOT a directive · Machiavelli/Clausewitz not a mandate for ruthless power · Meditations secular). The brief is NOT a chunked source.
- Excluded (0 chunks): Art of War + 48 Laws + 33 Strategies (already BATCH_002), Book of Five Rings (djvu), the Bible, and all deferred strategy_history / other-cluster sources.
