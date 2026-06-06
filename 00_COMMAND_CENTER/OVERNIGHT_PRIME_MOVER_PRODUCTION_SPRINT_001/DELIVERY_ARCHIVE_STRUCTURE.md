# 16 DELIVERY + ARCHIVE STRUCTURE , SOLE HOUSE engagement

How a real 72-hour SOLE engagement is packaged, handed off, and archived. One sealed handoff, one change-log, faceless-safe.

## Per-engagement folder (template)
```
SOLE_ENGAGEMENTS/<client_codename>_<YYYYMMDD>/
  00_CLAIM/            The Sole Claim + Positioning Doctrine (the verdict, day 1)
  01_WORLD/            Brand World Bible: stills, color/type/motif tokens
  02_FILM/             Manifesto film master + stems (VO dry, music, SFX) + teaser cut
  03_DECK/             Category Brief deck (PDF + source)
  04_LANDING/          Static site bundle (index.html, /assets, /script.js)
  05_OFFER/            Offer copy + booking layer config
  06_SEAL/             Singular Seal renders + alpha (emboss/watermark) + Sovereign object spec
  99_HANDOFF/          Timestamped manifest + CHANGE_LOG.md + readiness-gate pass receipt
```
Client codename only in folder names (no real client PII in paths). One recut only, logged in CHANGE_LOG.md.

## Handoff rule
A deliverable ships only after it clears `os_max_readiness_gate` and `os_privacy_gate scan` (0 leaks). The 99_HANDOFF manifest lists every file, its sha256, and the gate receipt. Delivered as one sealed package on day four.

## Archive
- Masters + stems retained in the engagement folder; large media mirrored to asset storage (gdrive) under the same codename (TEMP-bridge caution: no account-anchoring writes).
- The Vault Room world templates + Seal are reused across engagements (the house style compounds); only the per-client CLAIM and copy vary.
- This sprint (SOLE HOUSE demo) is the reference engagement: `OVERNIGHT_PRIME_MOVER_PRODUCTION_SPRINT_001/` is the archived golden master.
