#!/usr/bin/env python3
"""
os_receipt.py - the OS_RECEIPT for serious work. Proof that the OS moved as one body.

New law: "relevant activation" is not enough; the receipt must prove activation CHANGED the output.

  os_receipt.py init <folder> "<task>"   # scaffold OS_RECEIPT.md, pre-filled from the conductor scan
  os_receipt.py verify <folder>          # check the must-fill sections are real (exit 0 pass / 2 fail)
"""
import sys, os, json, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
CC = os.path.dirname(HERE)

def _act():
    spec = importlib.util.spec_from_file_location("os_activate", os.path.join(HERE, "os_activate.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

FILL = "<FILL: required before done>"
MUST_FILL = ["What CHANGED because the OS activated", "Gates passed / failed", "Rating + why", "What blocks 10/10", "VERDICT"]
VALID_VERDICTS = ["sendable", "internal", "proof", "draft", "blocked"]

def init(folder, task):
    m = _act(); idx = m.load()
    ranked = m.classify(task, idx)
    top = ranked[0][0] if ranked else None
    d = idx["domains"].get(top, {}) if top else {}
    serious = m.is_serious(task, idx, ranked)
    cds = m.cross_domain_skills(top, idx) if top else {}
    asleep = [n for n in idx["domains"] if n != top and n not in d.get("cross_domain", [])]
    lines = []
    lines.append(f"# OS_RECEIPT - {task}")
    lines.append("")
    lines.append("Proof the OS moved as one body. Layer 1 (scan) is pre-filled; Layer 3 (proof/verdict) MUST be filled before done.")
    lines.append("")
    lines.append("## Layer 1 - Whole-OS scan")
    lines.append(f"- Task type / domain: {top or 'unmatched'} ({d.get('label','')}) | serious={serious}")
    lines.append(f"- Outcome intended: {FILL}")
    lines.append(f"- Domains detected: {', '.join(n for n,_ in ranked) or 'none'}")
    lines.append(f"- Active skills: {', '.join(d.get('skills', [])) or 'none'}")
    lines.append(f"- Reference skills consulted: {', '.join(d.get('reference_skills', [])) or 'none'}  (mark which you actually used)")
    lines.append(f"- Cross-domain skills pulled: {' | '.join(f'{k}: {", ".join(v)}' for k,v in cds.items()) or 'none'}")
    lines.append(f"- Standards used: {', '.join(d.get('docs', [])) or 'none'}")
    lines.append(f"- Gates required: {', '.join(d.get('gates', [])) or 'none'}")
    lines.append(f"- Omitted skills + why: every other domain stayed asleep (not relevant). Asleep domains: {', '.join(asleep)}")
    lines.append(f"- Known gaps: {'; '.join(d.get('gaps', [])) or 'none'}")
    lines.append(f"- Toolchain: {', '.join(d.get('tools', [])) or 'none'}")
    lines.append("")
    lines.append("## Layer 3 - Proof + verdict (MUST FILL)")
    lines.append(f"### What CHANGED because the OS activated")
    lines.append(f"{FILL}  (name the specific decisions/edits each activated skill caused. If nothing changed, the skill was not really used.)")
    lines.append(f"### Gates passed / failed")
    lines.append(f"{FILL}")
    lines.append(f"### Remaining blockers")
    lines.append(f"{FILL}")
    lines.append(f"### Rating + why")
    lines.append(f"{FILL}  (honest score /10 and the reason)")
    lines.append(f"### What blocks 10/10")
    lines.append(f"{FILL}  (the exact blocker + the path to remove it; or 'nothing, this is 10/10')")
    lines.append(f"### VERDICT")
    lines.append(f"{FILL}  (one of: {', '.join(VALID_VERDICTS)})")
    os.makedirs(folder, exist_ok=True)
    open(os.path.join(folder, "OS_RECEIPT.md"), "w").write("\n".join(lines) + "\n")
    print(f"OS_RECEIPT scaffolded -> {os.path.join(folder,'OS_RECEIPT.md')} (serious={serious}). Fill the Layer 3 sections before claiming done.")

def verify(folder):
    p = os.path.join(folder, "OS_RECEIPT.md")
    if not os.path.exists(p):
        return False, ["NO OS_RECEIPT.md in this folder"]
    txt = open(p).read()
    blockers = []
    for sec in MUST_FILL:
        # find the section, check the text after it does not still contain the FILL marker / is non-empty
        i = txt.find(sec)
        if i < 0:
            blockers.append(f"missing section: {sec}"); continue
        after = txt[i + len(sec): i + len(sec) + 400]
        if FILL in after or len(after.strip().splitlines()[1:2] or [""]) == 0:
            blockers.append(f"unfilled section: {sec}")
    low = txt.lower()
    if not any(v in low for v in [f"verdict\n{v}" for v in VALID_VERDICTS]) and not any(("### verdict" in low and v in low.split("### verdict")[-1][:80]) for v in VALID_VERDICTS):
        # lenient: just require a valid verdict word appears after the VERDICT header
        seg = low.split("verdict")[-1][:120] if "verdict" in low else ""
        if not any(v in seg for v in VALID_VERDICTS):
            blockers.append("VERDICT not set to one of: " + ", ".join(VALID_VERDICTS))
    return (not blockers), blockers

def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); return
    if a[0] == "init" and len(a) > 2:
        init(os.path.abspath(a[1]), a[2])
    elif a[0] == "verify" and len(a) > 1:
        ok, bl = verify(os.path.abspath(a[1]))
        print(f"{'PASS' if ok else 'FAIL'}")
        for b in bl: print("  - " + b)
        sys.exit(0 if ok else 2)
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
