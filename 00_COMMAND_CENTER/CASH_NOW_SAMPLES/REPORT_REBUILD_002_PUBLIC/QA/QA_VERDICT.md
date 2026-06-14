# QA VERDICT · Cash Now Sample 002 · 2026-06-12

## Builder/judge separation honored
Builder (this session) built; verdicts came from two fresh-context agents who never saw the build process.

## Round 1 · hostile judge (full source-truth audit, fresh context)
- Read the full extracted source text and the full rebuild HTML line by line.
- Numbers audit: every phone, fax, address, dollar figure, date, time estimate, and regulation/section/form citation matched the source exactly. Zero hard factual errors.
- VERDICT: FAIL on the strict bar: 7 low-severity overreaches/meaning-shifts (blanket "Nothing." cost claim; "Every fact" completeness overclaim; advisory note made imperative; invented 1-8 numbering on Line 10 chips; GEN instruction stated as assertion; unsourced "one clear rule each" editorial; territory $6,536 threshold scoped imprecisely) + 2 dropped framing lines (IRC section-reference note; "Do I Need an EIN?" pointer).
- Clarity finding: for "I need an EIN for my new LLC this week," the rebuild is genuinely faster (method cards with speed labels vs buried mid-column 8pt text). Not prettier-but-less-usable, except the items above.
- Public-safety finding: no PII, no third-party content, zero IRS insignia in the rebuild (markup contains no images at all), attribution + not-IRS disclaimer on cover, footers, page 12 box, and spread header.
- Spread finding: caption present; all 4 pairs content-matched (subset-matches, inherent to a 7-to-12 page expansion); no mismatched pair.

## Fix round (single round, source-truth compliance, not polish)
All 7 discrepancies + 2 dropped lines fixed in after/ein_guide_master.html; PDF re-printed; spread rebuilt.

## Round 2 · hostile re-verification (second fresh-context agent)
- VERDICT: PASS. All 9 fixes confirmed against the source; no new drift introduced by the edits; em-dash sweep clean (including lookalike codepoints); re-rendered pages show no layout breakage.

## Final gate results (per PASS_FAIL_CARD)
- cold_pick fresh judge: RUN (two independent agents) · final PASS
- source-true zero-drift: PASS after fix round (round 1 found zero hard factual errors; overreaches corrected)
- usability improved: PASS (judge's concrete finding above)
- public-domain verified + third-party stripped: PASS (U.S. gov work, 17 U.S.C. 105; no third-party content existed; no IRS insignia in rebuild)
- one sitting <=3h: PASS (~13:12 to ~13:47, under 40 minutes)
- 0 credits / $0: PASS (curl + Chrome + pdftoppm + ImageMagick only)
- attribution line present: PASS (cover, every footer, page 12 notice, spread header)
- print + phone clean: print verified at 150dpi renders; phone-size verification NOT separately run (noted as residual)
- operator-would-show-publicly: PENDING OPERATOR (PASS does not mean publish; public use is a separate approval)

## Honest cautions carried forward
1. The spread caption "same facts, 3 days, $300" states the OFFER's turnaround and price (Menu B terms), not this build's actual time (~40 min). The caption is an offer claim by operator order; flagged so it is never misread as a build fact.
2. Phone/mobile legibility of the rebuilt PDF was not separately gated; desktop/print renders only.
3. Two optional judge suggestions NOT taken (would be a polish loop): add a table of contents; restore Rev. Rul. pin-cites (unnecessary once the "every fact" claim was removed).
