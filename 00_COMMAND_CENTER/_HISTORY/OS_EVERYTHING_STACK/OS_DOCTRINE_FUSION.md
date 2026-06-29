# OS DOCTRINE FUSION , the OS polices its own quality (2026-06-05)
> The operator's standard: the OS must be ONE thing, quality built in, so you never babysit it. Doctrine (the books) is fused into the functions. Built + wired + tested. ACTIVE.

## What is now true (every os_engine run)
1. **Clean at birth.** A world JSON carries a `copy` block of doctrine-clean headlines/subs/captions. The engine prefers it over machine-derivation, so the output is right the first time. (DEED + REMAINS now have copy blocks; doctrine_copy = PASS.)
2. **Auto-fix before render.** The engine runs every copy field through os_doctrine.fix_copy , strips em-dashes + generic hype + tidies , so mechanical failures are repaired silently BEFORE the kit renders.
3. **Never ships weak silently.** What deterministic fixing cannot repair (fragments, bible-language) is FLAGGED needs_rewrite in the ENGINE_MANIFEST. The OS tells you, every run, instead of you catching it later.
4. **Universal, not just copy.** os_doctrine maps 9 domains (copy/visual/world/layout/pricing/distribution/trust/motion/safety), each to its certified sources + rules + a gate. `load` injects doctrine INTO generation; `check`/`gate` verify output.

## The commands (os_doctrine.py)
- `domains` , the 9 fused domains.
- `load <domain>` , the doctrine pack to inject into a generation prompt (proactive quality).
- `check <domain> --text/--asset` , gate an output (deterministic for copy + model rubric for the rest).
- `fix copy --text` , deterministic repair; returns needs_rewrite for what requires real writing taste.
- `gate run` , master gate for a whole run, logged.

## The one honest limit (so this is not overclaimed)
Deterministic code can repair MECHANICAL failures and CATCH taste failures, but it cannot WRITE great copy , that needs the doctrine pack injected at generation (the agent contract below). The system guarantees: nothing weak ships silently, and a well-authored world ships clean automatically. Taste-perfection at birth requires the agent to generate WITH the doctrine loaded.

## THE AGENT CONTRACT (how every generation stays doctrine-correct)
When any agent (or os_engine, or a workflow) GENERATES copy / a grade / a world / a layout:
1. `os_doctrine load <domain>` , inject the pack into the prompt.
2. Generate.
3. `os_doctrine check <domain>` , gate it.
4. If FLAG: regenerate with the pack (proactive loop) until PASS.
5. Log the verdict. No artifact ships without its domain gate.
This is the law that makes the OS move as one thing. It is wired in os_engine for copy; agents apply it for the model-judged domains.
