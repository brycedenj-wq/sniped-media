# OS MASTER CORPUS FUSION
### The corpus is not a library. It is one operating intelligence.
Built: 2026-06-05. This is the top-level doc for how everything Bryce has collected becomes one fused brain.

---

## The mandate

> Do not treat my books, docs, chunks, sources, uploads, frameworks, transcripts, and notes as a library that gets searched occasionally. Fuse the entire corpus into one operating intelligence. Make all of it move as one.

Fusion does NOT mean loading raw books into a context window (impossible and wasteful). It means every source is transformed into a usable law and wired into a brain that thinks through all of it before it acts.

---

## What got fused (real numbers, computed 2026-06-05)

- **60 source families** (1,879 chunks) , the knowledge base
- **66 certified atoms** (intel_* / feedback_* / project_*) , the distilled memory
- **17 doctrine nodes** , the fused concepts
- **12 cross-source fusion edges** , how ideas connect across families
- **126 fusable sources, 100% mapped, 0 orphans**
- Underneath: **3,877 dispositioned sources** in the certification ledger (840 certified + 501 provisional = **1,341 usable**; 2,058 duplicates/derivatives correctly excluded; ~120 pending OCR/read).

Run it yourself:
```
os_corpus_fusion.py coverage      # the percentages
os_corpus_fusion.py orphans       # the leak list (currently 0)
os_doctrine_graph.py nodes        # the 17 fused concepts
os_intelligence_kernel.py compact # the always-on block
os_execution_graph.py graph "<task>"   # the whole brain on one task
```

---

## What "fused" means (every source becomes >=1 of these 16)

A source is only fused if it became at least one of:

1. Doctrine 2. Operating rule 3. Taste rule 4. Strategy principle 5. Creative principle 6. Business principle 7. Production workflow 8. Skill 9. Gate 10. Warning / anti-pattern 11. Decision heuristic 12. Prompt pattern 13. Tool route 14. Proof loop 15. Contradiction to preserve 16. Confidence-labeled knowledge atom

If it became none of those, it is an ORPHAN and lands on the leak list. Current orphans: 0.

---

## The fusion architecture (the files that make it one thing)

| Layer | File | Job |
|---|---|---|
| Always-on kernel | `os_intelligence_kernel.py` / `OS_ALWAYS_ON_KERNEL.md` | the whole corpus as compact laws, injected every task |
| Doctrine graph | `os_corpus_fusion.py` -> `OS_DOCTRINE_GRAPH.json` | nodes + cross-source edges, computed from disk |
| Source map | `os_corpus_fusion.py` -> `OS_SOURCE_TO_DOCTRINE_MAP.csv` | every family/atom -> node(s) + confidence |
| Graph query + tensions | `os_doctrine_graph.py` / `OS_CONTRADICTION_MAP.md` | neighbors + preserved contradictions |
| Doctrine selector | `os_doctrine_router.py` | task -> which doctrines + confidence |
| The capstone | `os_execution_graph.py` | loads kernel + activates nodes/families + checks contradictions + routes + gates + refuses |
| Fusion tests | `OS_TASK_TO_SOURCE_FUSION_TESTS.md` | 15 tasks proving the brain fires the whole corpus |

---

## Source confidence (honest, never faked)

- **CERTIFIED** (a memory intel_/feedback_ atom exists) -> strong doctrine, used at creation.
- **PROVISIONAL** (a knowledge-base chunk family) -> used WITH the label, never crowned.
- **LOW-confidence family** (the 10 big mixed intake batches BATCH_001-010) -> usable, flagged for sub-mapping.
- **RAW / UNREAD / pending** (in the ledger) -> queued potential, not truth.

The fusion layer uses the entire corpus **according to confidence**. It does not pretend pending OCR is certified, and it does not leave certified material unused.

---

## How the brain uses the corpus when it builds

For films, games, campaigns, offers, proof loops, the execution graph (1) injects the always-on kernel, (2) activates the relevant doctrine nodes which pull their real source families and atoms, (3) navigates any preserved contradictions, (4) routes tools, (5) applies gates, (6) defines the artifact, (7) names what it refuses to claim. Verified across 15 tasks. See `OS_TASK_TO_SOURCE_FUSION_TESTS.md`.

---

## Known gaps (honest)

- The **route table is coarser than the fused brain.** Many tasks (film/game pipeline, judge quality, tool-stack, content engine) correctly activate the right nodes/families/contradictions but fall through to `make_campaign_package` because `os_tool_router` lacks dedicated routes. The thinking is right; the execution routing needs expansion. NEXT BUILD.
- **10 LOW-confidence families** (the big mixed batches) are mapped to one node each but need sub-classification into multiple nodes.
- **Games** have no engine route (Unreal/Godot RED). North-star, not yet buildable.
- Pending pile: 79 OCR + 23 full-read + 17 visual + 1 transcription = ~120 sources not yet fused, correctly queued.
