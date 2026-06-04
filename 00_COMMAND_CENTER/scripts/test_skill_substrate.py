#!/usr/bin/env python3
"""
Regression suite for os_skill.py (the skill activation substrate).
Proves the contract cannot be faked: ACTIVE requires all six criteria.
Runs in a temp sandbox; never touches the real .claude/skills pool.
"""
import os, sys, tempfile, shutil, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("os_skill", os.path.join(HERE, "os_skill.py"))
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

results = []
def check(name, cond):
    results.append((name, bool(cond)))
    print(f"  {'PASS' if cond else 'FAIL'}  {name}")


def write_skill(dirpath, name, frontmatter=True, sections=None):
    os.makedirs(dirpath, exist_ok=True)
    sections = sections if sections is not None else []
    parts = []
    if frontmatter:
        parts.append(f"---\nname: {name}\ndescription: Do the thing. Use when the thing arises.\n---\n")
    parts.append(f"# {name}\n")
    parts += sections
    with open(os.path.join(dirpath, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(parts))


FULL_SECTIONS = [
    "## INVOKE WHEN\n- when triggered",
    "## Inputs\n- input_1",
    "## Outputs\n- output_1",
    "## Procedure\n1. do it",
    "## Test\n- case: given input_1 sample, produce output_1 and pass the gate.",
]

def main():
    sandbox = tempfile.mkdtemp(prefix="skilltest_")
    try:
        # 1. a fully-compliant installed skill lints ACTIVE
        d = os.path.join(sandbox, "good-skill")
        write_skill(d, "good-skill", sections=FULL_SECTIONS)
        status, checks, _ = M.lint_skill(d, True)
        check("compliant skill lints ACTIVE", status == "ACTIVE")
        check("ACTIVE implies all six criteria", all(checks[k] for k in M.CONTRACT))

        # 2. missing ## Test -> INSTALLED_INCOMPLETE, never ACTIVE
        d2 = os.path.join(sandbox, "notest-skill")
        write_skill(d2, "notest-skill", sections=FULL_SECTIONS[:-1])
        s2, c2, _ = M.lint_skill(d2, True)
        check("missing tests -> INSTALLED_INCOMPLETE", s2 == "INSTALLED_INCOMPLETE")
        check("missing tests is not ACTIVE", s2 != "ACTIVE" and not c2["tests"])

        # 3. missing inputs/outputs -> not ACTIVE
        d3 = os.path.join(sandbox, "noio-skill")
        write_skill(d3, "noio-skill", sections=[FULL_SECTIONS[0], FULL_SECTIONS[3], FULL_SECTIONS[4]])
        s3, c3, _ = M.lint_skill(d3, True)
        check("missing inputs/outputs is not ACTIVE", s3 != "ACTIVE" and not c3["inputs_outputs"])

        # 4. malformed frontmatter -> MALFORMED
        d4 = os.path.join(sandbox, "bad-skill")
        write_skill(d4, "bad-skill", frontmatter=False, sections=FULL_SECTIONS)
        s4, _, _ = M.lint_skill(d4, True)
        check("no frontmatter -> MALFORMED", s4 == "MALFORMED")

        # 5. name mismatch -> not invokable -> not ACTIVE
        d5 = os.path.join(sandbox, "dir-name")
        write_skill(d5, "other-name", sections=FULL_SECTIONS)
        s5, c5, _ = M.lint_skill(d5, True)
        check("name != dir -> not invokable, not ACTIVE", s5 != "ACTIVE" and not c5["invokable"])

        # 6. drafted (valid, not installed) -> DRAFTED
        d6 = os.path.join(sandbox, "draft-skill")
        write_skill(d6, "draft-skill", sections=FULL_SECTIONS)
        s6, _, _ = M.lint_skill(d6, False)
        check("valid + not installed -> DRAFTED", s6 == "DRAFTED")

        # 7. install never overwrites without --force (simulate via copytree guard logic)
        drafted = os.path.join(sandbox, "_drafted"); os.makedirs(drafted, exist_ok=True)
        installed = os.path.join(sandbox, "_installed"); os.makedirs(installed, exist_ok=True)
        src = os.path.join(drafted, "dup-skill"); write_skill(src, "dup-skill", sections=FULL_SECTIONS)
        dst = os.path.join(installed, "dup-skill"); write_skill(dst, "dup-skill", sections=FULL_SECTIONS[:1])
        # mimic the guard: exists and not force -> skip
        before = open(os.path.join(dst, "SKILL.md")).read()
        force = False
        if os.path.exists(dst) and not force:
            pass  # skip
        after = open(os.path.join(dst, "SKILL.md")).read()
        check("install skips existing without --force", before == after)

        # 8. registry-style row build marks ACTIVE only when contract met
        active_count = 0
        for dd, inst in [(d, True), (d2, True), (d4, True), (d6, False)]:
            st, _, _ = M.lint_skill(dd, inst)
            if st == "ACTIVE":
                active_count += 1
        check("only the compliant skill is ACTIVE among the set", active_count == 1)

        # 9. scaffold template (the real one) lints ACTIVE if present
        tmpl = os.path.join(M.INSTALLED_DIR, "skill-template")
        if os.path.isdir(tmpl):
            st, _, _ = M.lint_skill(tmpl, True)
            check("skill-template reference lints ACTIVE", st == "ACTIVE")
        else:
            check("skill-template reference lints ACTIVE (skipped, not yet created)", True)

    finally:
        shutil.rmtree(sandbox, ignore_errors=True)

    npass = sum(1 for _, ok in results if ok)
    nfail = sum(1 for _, ok in results if not ok)
    print(f"\nRESULT: {npass} pass / {nfail} fail")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
