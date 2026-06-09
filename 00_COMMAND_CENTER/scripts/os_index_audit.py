#!/usr/bin/env python3
"""
os_index_audit.py - keeps the activation body COMPLETE.

The bridge only works if the index knows about every resource. As skills, standards, and docs
are added, this audit flags what is NOT yet wired into OS_ACTIVATION_INDEX.json, so the body
stays "ready for anything" instead of drifting back into unused piles.

  os_index_audit.py            # report registered vs unregistered skills + standards docs
"""
import os, json, glob

HERE = os.path.dirname(os.path.abspath(__file__))
CC = os.path.dirname(HERE)
ROOT = os.path.dirname(CC)
INDEX = os.path.join(CC, "OS_ACTIVATION_INDEX.json")

def main():
    idx = json.load(open(INDEX))
    active, reference = set(), set()
    for d in idx["domains"].values():
        active.update(d.get("skills", []))
        reference.update(d.get("reference_skills", []))
    excluded = set(x["skill"] for x in idx.get("intentional_exclusions", []))
    # plugin-only references (not on disk as native skills) - strip the "(plugin)" tag noise
    reference = {r.split(" ")[0] for r in reference}
    registered = active | reference | excluded

    skills = sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(ROOT, ".claude/skills/*/SKILL.md")))
    unreg = [s for s in skills if s not in registered]

    active_on_disk = sorted(s for s in skills if s in active)
    ref_on_disk = sorted(s for s in skills if s in reference and s not in active)
    excl_on_disk = sorted(s for s in skills if s in excluded and s not in active and s not in reference)

    print("=== OS ACTIVATION INDEX AUDIT ===")
    print(f"skills on disk: {len(skills)}")
    print(f"  active (auto-route):        {len(active_on_disk)}")
    print(f"  reference (load on demand): {len(ref_on_disk)}")
    print(f"  intentional exclusions:     {len(excl_on_disk)}")
    print(f"  UNREGISTERED:               {len(unreg)}")
    if unreg:
        print("  -> wire these into a domain or add to intentional_exclusions:")
        for s in unreg:
            print(f"     - {s}")
    else:
        print("  -> 0 dead skills. Every skill is registered (active, reference, or intentionally excluded).")
    # standards coverage
    reg_docs = set()
    for d in idx["domains"].values():
        for doc in d.get("docs", []):
            reg_docs.add(os.path.basename(doc))
    stds = sorted(os.path.basename(p) for p in glob.glob(os.path.join(CC, "_standards/*.md")))
    unreg_docs = [s for s in stds if s not in reg_docs]
    print(f"\nstandards docs on disk: {len(stds)} | referenced by a domain: {len(set(stds) & reg_docs)}")
    if unreg_docs:
        print("  not referenced (ok if cross-cutting/meta): " + ", ".join(unreg_docs))

if __name__ == "__main__":
    main()
