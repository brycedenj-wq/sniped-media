# OS NAMING LIBRARY , the naming operating doctrine

> Why this exists: the bare-.com namespace is exhausted, clean English words are taken, and random coinages risk sounding fake / SaaS / pharma / legally messy. Naming is now a repeatable OS problem, so it gets an engine + a gate, not a brainstorm. This library is the doctrine those tools encode. Reusable across every brand/product the OS names.

Stack: `OS_NAMING_LIBRARY.md` (this) + `OS_NAME_DECISION_MATRIX.csv` (the rubric) + `scripts/os_naming_engine.py` (generate across lanes) + `scripts/os_name_gate.py` (score + verdict + next legal/domain checks).

## 1. The 8 naming lanes
1. **Suggestive** , hints at the benefit without describing it (Sovra ~ sovereign). Legally strong, marketable. The default premium lane.
2. **Invented / fanciful** , coined, no prior meaning (Onora, Solene). Strongest trademark protection; needs more marketing to seat meaning.
3. **Associative / metaphorical** , borrows a vivid object/world (Vault, Seal, Monolith, Keystone). Rich identity; watch genericness + crowding.
4. **Compound** , two real units fused (Solekeep, Onlymark, Vaultworks). Ownable, clear; can get long.
5. **Foreign / Latin / Greek / Old English root** , derived from solus/unum/signum/monos/sovra/custos/arx/anweald. Premium, timeless, defensible; verify the foreign meaning + global risk.
6. **Sound-symbolic** , chosen for phonetic feel over literal meaning (plosives = strength, /s/+/v/ = premium hush, open /o//a/ = prestige). 
7. **Domain-strategy** , designed around an acquirable address (name + .house/.studio/.co, or a compound that frees the .com).
8. **Suffix architecture** , the entity wrapper: HOUSE / WORKS / STANDARD / ATELIER / & CO / OFFICE / KEEP. "House" fits a premium campaign house; "Standard" and "Keep" reinforce sovereignty/vault.

## 2. Sound-symbolism doctrine (premium register)
- **Plosives** (b, d, g, k, p, t) read decisive, struck, engineered. One hard consonant gives a name a "strike."
- **/s/ and /v/ + open vowels** (o, a) read premium, hushed, old-money (Sovra, Solum, Vesta). Avoid sibilant pile-ups.
- **Two to three syllables, ends on a vowel or soft consonant** = premium and pronounceable. One syllable = bold but crowded. Four+ = it slips.
- **Avoid:** double letters that confuse spelling, silent letters, -ify/-ly/-io/-sy/-ster/-hub/-ly SaaS tells, x/z unless deliberate, anything that reads pharma (-zil, -dra, -xa) or fintech (-pay, -fi, -bit).
- The SOVRA/SOLE world wants: a struck consonant + a hushed premium tail. Engraved-nameplate sound.

## 3. Trademark distinctiveness spectrum (strong -> weak)
fanciful (Kodak) > arbitrary (Apple for computers) > **suggestive (the premium sweet spot)** > descriptive (weak, often unregistrable) > generic (unprotectable). Aim suggestive/invented. A same-name incumbent in a DIFFERENT class (Nice classification) is usually coexistable; same class = confusion = kill. Our class: brand/marketing/design services (likely 35 + 42). Never lock a public name without counsel clearance.

## 4. Domain strategy (post-exhaustion reality)
- Bare 4-6 letter pronounceable .com = effectively all taken. Do NOT require it.
- Acceptable premium paths, in order: (a) `name.house` / `name.studio` (on-brand for a house), (b) coined-compound `.com` (`namehouse.com`), (c) a premium one-word `.co` if budget allows, (d) a distinctive enough coinage that a modifier frees the .com. 
- The address should match the wordmark spoken aloud ("sovra dot house").

## 5. The 14 scoring criteria (see OS_NAME_DECISION_MATRIX.csv for weights + rubric)
big-idea fit · audience fit · memorability · pronunciation · spelling · crowded-bar test · premium feel · distinctiveness · trademark risk · domain path · search uniqueness · visual-identity potential · future-proofing · global-language risk.

The **crowded-bar test**: say the name once, loud, in a noisy room. If it must be spelled, repeated, or explained, it loses points. If three competitors could plausibly own it, it loses points.

## 6. The current brief (SOVRA/SOLE)
- Big idea: **"AI made everyone good. It cannot make anyone the only one."**
- Must express: singularity, sovereignty, proof, vault, seal, category ownership, quiet authority, premium campaign house.
- Register: engraved brass nameplate, private-bank-after-hours, struck-once. Not techy, not soft-luxury, not pharma.

## 7. How to run it
```
python3 scripts/os_naming_engine.py generate --n 120          # candidates across all lanes
python3 scripts/os_naming_engine.py generate --lane foreign    # one lane
python3 scripts/os_name_gate.py score "Sovra" --suffix House   # 14-criteria score + verdict + next checks
python3 scripts/os_name_gate.py batch <namesfile>              # score a list, ranked
```
The gate SCORES heuristically and emits the EXACT domain + trademark queries to run (via the Vercel domain MCP + USPTO/web). It never claims legal clearance , that is counsel's call.
