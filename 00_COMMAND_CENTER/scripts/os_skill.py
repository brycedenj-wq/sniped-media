#!/usr/bin/env python3
"""
os_skill.py , the skill activation substrate.

Removes fake capability. A skill counts as ACTIVE only if it meets the full
activation contract (installed, discoverable, trigger, inputs/outputs, tests,
invokable). Everything less is named honestly: INSTALLED_INCOMPLETE, DRAFTED,
or MALFORMED. The registry is the single source of truth.

Commands:
  lint <name|path|--all-installed|--all-drafted|--all>   grade skills
  new <name> "<description>"                              scaffold a born-compliant skill
  install <name|--all-drafted> [--force]                 copy drafted -> installed (safely)
  registry                                               write OS_SKILL_REGISTRY.csv + dashboard
  audit                                                  print tier counts

No third-party deps. Never marks a skill ACTIVE unless all six criteria pass.
"""
import os, sys, re, shutil, csv

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # 00_COMMAND_CENTER
REPO = os.path.dirname(ROOT)                      # AI-Brain-Refinery
INSTALLED_DIR = os.path.join(REPO, ".claude", "skills")
DRAFTED_DIR = os.path.join(REPO, "raw", "_skills")
REGISTRY_CSV = os.path.join(ROOT, "OS_SKILL_REGISTRY.csv")
DASHBOARD_MD = os.path.join(ROOT, "OS_SKILL_DASHBOARD.md")

CONTRACT = ["installed", "discoverable", "trigger", "inputs_outputs", "tests", "invokable"]


def parse_skill(skill_md_path):
    """Return dict: name, description, body, raw, ok(frontmatter parsed)."""
    out = {"name": None, "description": None, "body": "", "raw": "", "fm_ok": False}
    try:
        with open(skill_md_path, "r", encoding="utf-8", errors="replace") as f:
            raw = f.read()
    except Exception:
        return out
    out["raw"] = raw
    # frontmatter between the first two --- fences
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", raw, re.DOTALL)
    if not m:
        out["body"] = raw
        return out
    fm, body = m.group(1), m.group(2)
    out["body"] = body
    out["fm_ok"] = True
    for line in fm.splitlines():
        nm = re.match(r"^name:\s*(.+?)\s*$", line)
        if nm and out["name"] is None:
            out["name"] = nm.group(1).strip().strip('"').strip("'")
        dm = re.match(r"^description:\s*(.+?)\s*$", line)
        if dm and out["description"] is None:
            out["description"] = dm.group(1).strip().strip('"').strip("'")
    return out


def has_header(body, pattern):
    return re.search(r"(?im)^#{1,4}\s*" + pattern, body) is not None


def lint_skill(skill_dir, installed):
    """Return (status, checks dict, info dict). Never ACTIVE unless all 6 pass."""
    name = os.path.basename(skill_dir.rstrip("/"))
    md = os.path.join(skill_dir, "SKILL.md")
    checks = {k: False for k in CONTRACT}
    info = {"name": name, "description": "", "path": md}
    if not os.path.isfile(md):
        return "MALFORMED", checks, info
    sk = parse_skill(md)
    info["description"] = (sk["description"] or "")[:200]
    if not sk["fm_ok"] or not sk["name"]:
        return "MALFORMED", checks, info
    body = sk["body"]
    desc = sk["description"] or ""

    checks["installed"] = installed
    checks["discoverable"] = bool(sk["name"]) and bool(sk["description"])
    # trigger: an invoke/trigger/when-to-use header OR a "use when/at/on/for/this" cue in desc
    checks["trigger"] = (
        has_header(body, r"(invoke\s*when|trigger|when\s*to\s*use|use\s*when)")
        or bool(re.search(r"(?i)\buse\s+(when|at|on|for|this|to)\b", desc))
    )
    has_in = has_header(body, r"inputs?")
    has_out = has_header(body, r"outputs?")
    has_io_combined = has_header(body, r"inputs?\s*(&|/|and|\+)\s*outputs?")
    checks["inputs_outputs"] = (has_in and has_out) or has_io_combined
    # tests: a test/evaluation header with content, OR a sibling test file
    sibling_test = any(
        re.match(r"(?i)^(test|tests).*\.(md|py)$", fn) or fn.lower() == "tests.md"
        for fn in (os.listdir(skill_dir) if os.path.isdir(skill_dir) else [])
    )
    test_header = has_header(body, r"(tests?|evaluation|eval|self-test)")
    test_has_content = False
    if test_header:
        mt = re.search(r"(?im)^#{1,4}\s*(tests?|evaluation|eval|self-test).*?$", body)
        if mt:
            after = body[mt.end():mt.end() + 400].strip()
            test_has_content = len(after) > 10
    checks["tests"] = sibling_test or (test_header and test_has_content)
    # invokable: frontmatter name == dir name, valid kebab-case
    checks["invokable"] = (sk["name"] == name) and bool(re.match(r"^[a-z0-9][a-z0-9-]*$", name))

    if not installed:
        # drafted pool: structurally valid drafts are DRAFTED, else MALFORMED
        structurally_ok = sk["fm_ok"] and sk["name"] and re.match(r"^[a-z0-9][a-z0-9-]*$", name)
        return ("DRAFTED" if structurally_ok else "MALFORMED"), checks, info
    if all(checks[k] for k in CONTRACT):
        return "ACTIVE", checks, info
    return "INSTALLED_INCOMPLETE", checks, info


def discover(dirpath):
    if not os.path.isdir(dirpath):
        return []
    out = []
    for n in sorted(os.listdir(dirpath)):
        d = os.path.join(dirpath, n)
        if os.path.isdir(d) and os.path.isfile(os.path.join(d, "SKILL.md")):
            out.append(d)
    return out


def cmd_lint(args):
    targets = []
    if "--all-installed" in args or "--all" in args:
        targets += [(d, True) for d in discover(INSTALLED_DIR)]
    if "--all-drafted" in args or "--all" in args:
        targets += [(d, False) for d in discover(DRAFTED_DIR)]
    named = [a for a in args if not a.startswith("--")]
    for a in named:
        if os.path.isdir(a):
            targets.append((a, INSTALLED_DIR in os.path.abspath(a)))
        else:
            di = os.path.join(INSTALLED_DIR, a)
            dd = os.path.join(DRAFTED_DIR, a)
            if os.path.isdir(di):
                targets.append((di, True))
            elif os.path.isdir(dd):
                targets.append((dd, False))
            else:
                print(f"  ??  {a} , not found")
    if not targets:
        print("usage: os_skill.py lint <name|--all-installed|--all-drafted|--all>")
        return 0
    rows = []
    for d, installed in targets:
        status, checks, info = lint_skill(d, installed)
        missing = [k for k in CONTRACT if not checks[k]]
        rows.append((info["name"], status, missing))
        tag = {"ACTIVE": "OK ", "INSTALLED_INCOMPLETE": "INC", "DRAFTED": "DFT", "MALFORMED": "BAD"}.get(status, "???")
        miss = "" if status == "ACTIVE" else "  missing: " + ",".join(missing)
        print(f"  [{tag}] {info['name']:<34} {status}{miss}")
    return 0


def cmd_new(args):
    if len(args) < 1:
        print('usage: os_skill.py new <name> "<description with Use when... trigger>"')
        return 1
    name = args[0]
    if not re.match(r"^[a-z0-9][a-z0-9-]*$", name):
        print(f"  refused: '{name}' is not valid kebab-case")
        return 1
    desc = args[1] if len(args) > 1 else f"Run the {name} procedure. Use when the {name} task arises in the OS."
    if "use when" not in desc.lower() and "use at" not in desc.lower() and "use on" not in desc.lower():
        desc = desc.rstrip(".") + ". Use when this task arises."
    dest = os.path.join(INSTALLED_DIR, name)
    if os.path.exists(dest):
        print(f"  refused: {name} already exists (use a new name)")
        return 1
    os.makedirs(dest, exist_ok=True)
    content = f"""---
name: {name}
description: {desc}
---

# {name}

One-line statement of what this skill produces.

## INVOKE WHEN
- the trigger condition that should route here
- "natural language phrase the operator might say"

## Inputs
- input_1 , what it is and where it comes from
- input_2 , optional

## Outputs
- output_1 , the artifact this skill produces
- a one-line receipt of what was done

## Procedure
1. step one
2. step two
3. run the gate(s), then emit the output

## Gates
- the quality/safety gate(s) this skill must pass before emitting output

## Test
- case: given <input_1 = sample>, the skill should produce <output_1 shape> and pass <gate>.
- expected failure: given a missing input_1, the skill refuses and asks for it.
"""
    with open(os.path.join(dest, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(content)
    status, checks, info = lint_skill(dest, True)
    print(f"  created {name} -> {status}")
    if status != "ACTIVE":
        print("  WARNING: scaffold did not lint ACTIVE: missing " +
              ",".join(k for k in CONTRACT if not checks[k]))
    return 0


def cmd_install(args):
    force = "--force" in args
    named = [a for a in args if not a.startswith("--")]
    if "--all-drafted" in args:
        srcs = discover(DRAFTED_DIR)
    else:
        srcs = []
        for a in named:
            d = os.path.join(DRAFTED_DIR, a)
            if os.path.isdir(d):
                srcs.append(d)
            else:
                print(f"  skip: {a} not found in drafted pool")
    if not srcs:
        print("usage: os_skill.py install <name|--all-drafted> [--force]")
        return 0
    installed = skipped = refused = 0
    for src in srcs:
        name = os.path.basename(src)
        md = os.path.join(src, "SKILL.md")
        sk = parse_skill(md)
        # structural gate: parseable frontmatter, name present + matches dir, kebab-case
        if not (sk["fm_ok"] and sk["name"] and sk["name"] == name and re.match(r"^[a-z0-9][a-z0-9-]*$", name)):
            print(f"  REFUSED (malformed): {name}")
            refused += 1
            continue
        dest = os.path.join(INSTALLED_DIR, name)
        if os.path.exists(dest) and not force:
            print(f"  SKIP (exists): {name}")
            skipped += 1
            continue
        if os.path.exists(dest) and force:
            shutil.rmtree(dest)
        shutil.copytree(src, dest)
        status, checks, _ = lint_skill(dest, True)
        print(f"  installed: {name} -> {status}")
        installed += 1
    print(f"\n  installed={installed} skipped={skipped} refused={refused}")
    return 0


def build_registry_rows():
    rows = []
    for d in discover(INSTALLED_DIR):
        status, checks, info = lint_skill(d, True)
        rows.append({
            "name": info["name"], "installed": "yes", "status": status,
            "missing": "|".join(k for k in CONTRACT if not checks[k]),
            "source": "installed", "description": info["description"],
        })
    installed_names = {r["name"] for r in rows}
    for d in discover(DRAFTED_DIR):
        status, checks, info = lint_skill(d, False)
        if info["name"] in installed_names:
            continue  # already represented by its installed copy
        rows.append({
            "name": info["name"], "installed": "no", "status": status,
            "missing": "|".join(k for k in CONTRACT if not checks[k]),
            "source": "drafted", "description": info["description"],
        })
    rows.sort(key=lambda r: (r["status"] != "ACTIVE", r["name"]))
    return rows


def cmd_registry(args):
    rows = build_registry_rows()
    with open(REGISTRY_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["name", "installed", "status", "missing", "source", "description"])
        w.writeheader()
        for r in rows:
            w.writerow(r)
    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    active = counts.get("ACTIVE", 0)
    inc = counts.get("INSTALLED_INCOMPLETE", 0)
    dft = counts.get("DRAFTED", 0)
    bad = counts.get("MALFORMED", 0)
    total = len(rows)
    lines = [
        "# OS SKILL DASHBOARD (auto-generated by os_skill.py registry)",
        "",
        "> 'Active' means the full activation contract is met. Anything less is named honestly.",
        "",
        f"- **ACTIVE: {active}** , installed + discoverable + trigger + inputs/outputs + tests + invokable",
        f"- **INSTALLED_INCOMPLETE: {inc}** , installed + invokable but missing >=1 contract criterion",
        f"- **DRAFTED: {dft}** , valid but not installed",
        f"- **MALFORMED: {bad}** , fails structural parse",
        f"- **TOTAL tracked: {total}**",
        "",
        "Source of truth: `OS_SKILL_REGISTRY.csv`. Upgrade path: add `## Inputs`, `## Outputs`, and a real `## Test` to move INSTALLED_INCOMPLETE -> ACTIVE (each upgrade ships its own test).",
        "",
        "## INSTALLED_INCOMPLETE (top of the upgrade backlog)",
    ]
    inc_rows = [r for r in rows if r["status"] == "INSTALLED_INCOMPLETE"]
    for r in inc_rows[:80]:
        lines.append(f"- `{r['name']}` , missing: {r['missing']}")
    if not inc_rows:
        lines.append("- (none)")
    lines.append("")
    lines.append("## ACTIVE")
    act_rows = [r for r in rows if r["status"] == "ACTIVE"]
    for r in act_rows:
        lines.append(f"- `{r['name']}`")
    if not act_rows:
        lines.append("- (none yet , the contract is honest; build the upgrades)")
    with open(DASHBOARD_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  wrote {REGISTRY_CSV} ({total} rows)")
    print(f"  wrote {DASHBOARD_MD}")
    print(f"  ACTIVE={active} INSTALLED_INCOMPLETE={inc} DRAFTED={dft} MALFORMED={bad}")
    return 0


def cmd_audit(args):
    rows = build_registry_rows()
    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print("  SKILL POOL (honest tiering):")
    for k in ["ACTIVE", "INSTALLED_INCOMPLETE", "DRAFTED", "MALFORMED"]:
        print(f"    {k:<22} {counts.get(k, 0)}")
    print(f"    {'TOTAL':<22} {len(rows)}")
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cmd, args = sys.argv[1], sys.argv[2:]
    handlers = {"lint": cmd_lint, "new": cmd_new, "install": cmd_install,
                "registry": cmd_registry, "audit": cmd_audit}
    if cmd not in handlers:
        print(f"unknown command: {cmd}")
        print(__doc__)
        return 1
    return handlers[cmd](args)


if __name__ == "__main__":
    sys.exit(main())
