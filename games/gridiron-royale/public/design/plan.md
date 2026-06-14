# Gridiron Royale · design plan

## Experience formula
The player feels like a highlight-reel superstar because the game constantly puts defenders one well-timed juke away from being left in the dust.

## Profile
- Time: real-time · Space: continuous 3D · Agency: one hero · Conflict: vs system
- Content: authored field + seeded procedural defender waves · Outcome: win/lose per 120s match
- Players: solo · Session: minutes · Engagement: execution (primary), accumulation (secondary)
- Delivery: desktop + mobile + gamepad. Keyboard via physical key codes, touch via virtual stick + buttons, gamepad via Gamepad API. Strings external in strings.js.

## Verbs
- Steer/run (free), Sprint (drains stamina, regenerates), Juke left/right (quick dash, 0.4s untouchable, 1.2s cooldown), Spin (breaks tackles in 2u radius, 3s cooldown).
- Verb development: defenders gain speed and new spawn patterns per touchdown; pickups (cyan stamina orbs, golden footballs) reweight sprint economy.

## Loop
Skydive drop onto the field -> run 80 yards through defender waves -> touchdown (+7, confetti, harder wave) or tackled (lose a down, restart drive). 4 downs lost or 120s clock = match over. 21+ points = MVP CHAMPION celebration. Restart from end screen.

## Uncertainty sources
Execution skill, seeded spawn randomness (lands before decisions: spawns are visible ahead), escalating defender AI.

## Loops signed
- Positive: score -> harder waves (keeps outcome undecided, caps snowball).
- Negative/comeback: each lost down grants +4% player speed ("clutch"); good play still wins because defender escalation outpaces it only at high scores.

## Information map
Everything visible; defenders behind the player get edge arrows. No hidden state.

## Agency metrics (frozen)
Player base speed 10 u/s, sprint 15; defender 8 -> 12.5 by wave; juke dash 6u over 0.25s; tackle radius 1.3u; field 40u wide, drive 80u; stamina 100, sprint drain 30/s, regen 18/s.

## Reference route (smoke)
Title -> tap to drop -> score one TD -> get tackled 4x -> game over screen shows score -> restart returns to title state.

## Entry
Title screen states goal + controls per input method; first meaningful action is one input away (drop-in). On game over: score, best score, current goal (beat it), restart.

## Limits stated honestly
Composition, animation feel and music balance were tuned by heuristics, not human playtesting.
