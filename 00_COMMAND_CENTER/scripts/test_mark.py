#!/usr/bin/env python3
"""Regression suite for os_mark.py , signature mark-injection must be logged,
non-destructive, and refuse silent/in-place edits. Temp sandbox."""
import os, sys, tempfile, shutil, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("os_mark", os.path.join(HERE, "os_mark.py"))
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)

results = []
def check(name, cond):
    results.append((name, bool(cond))); print(f"  {'PASS' if cond else 'FAIL'}  {name}")

class A:
    def __init__(self, **kw): self.__dict__.update(kw)


def main():
    try:
        from PIL import Image
    except ImportError:
        print("  SKIP: Pillow not installed"); print("RESULT: 0 pass / 0 fail"); return 0
    sb = tempfile.mkdtemp(prefix="marktest_")
    try:
        src = os.path.join(sb, "hero.png")
        Image.new("RGB", (200, 200), (180, 180, 175)).save(src)
        log = os.path.join(sb, "MARK_INJECTION_LOG.csv")
        out = os.path.join(sb, "hero_marked.png")

        # 1. valid injection creates a NEW file and a log row
        rc = M.cmd_inject(A(src=src, out=out, x=100, y=110, radius=3, color="#3c2823",
                            reason="model dropped signature mole; 4 pillars held", log=log))
        check("inject returns 0", rc == 0)
        check("output asset created (new file)", os.path.isfile(out))
        check("source preserved", os.path.isfile(src))
        check("log row written", os.path.isfile(log) and sum(1 for _ in open(log)) == 2)

        # 2. in-place edit refused (output == source)
        rc = M.cmd_inject(A(src=src, out=src, x=10, y=10, radius=2, color="#3c2823", reason="x", log=log))
        check("in-place edit REFUSED (no overwrite of source)", rc == 1)

        # 3. missing reason refused (no silent edit)
        out2 = os.path.join(sb, "hero_marked2.png")
        rc = M.cmd_inject(A(src=src, out=out2, x=10, y=10, radius=2, color="#3c2823", reason="", log=log))
        check("missing reason REFUSED (no silent edit)", rc == 1 and not os.path.isfile(out2))

        # 4. out-of-bounds coords refused
        out3 = os.path.join(sb, "hero_marked3.png")
        rc = M.cmd_inject(A(src=src, out=out3, x=999, y=999, radius=2, color="#3c2823", reason="x", log=log))
        check("out-of-bounds coords REFUSED", rc == 1 and not os.path.isfile(out3))

        # 5. the marked output actually differs from the source pixels
        a = list(Image.open(src).getdata()); b = list(Image.open(out).getdata())
        check("marked image differs from source", a != b)

    finally:
        shutil.rmtree(sb, ignore_errors=True)
    npass = sum(1 for _, ok in results if ok); nfail = sum(1 for _, ok in results if not ok)
    print(f"\nRESULT: {npass} pass / {nfail} fail")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
