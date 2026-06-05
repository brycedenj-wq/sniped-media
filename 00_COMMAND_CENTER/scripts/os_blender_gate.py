#!/usr/bin/env python3
"""
os_blender_gate.py , the security gate for Blender MCP (which runs LLM-generated code UNGATED).

The Blender MCP's own docs warn it executes generated Python with no guards. So the OS NEVER lets it
touch anything but a sandbox. Every proposed Blender action/path passes this gate first: allowed paths
only, no OS-root writes, no private-repo traversal, no credential paths, no destructive ops, and
per-action confirmation for anything beyond a harmless test scene. Every check is logged.

  os_blender_gate.py check-path <path>
  os_blender_gate.py check-action --kind read|create|modify|export|delete|python --path <p> [--code "..."] [--test]
  os_blender_gate.py audit
  os_blender_gate.py policy

This gate is the contract. If/when the Blender MCP is wired, every action routes through it. Until
then it documents + enforces the rule on any Blender work.
"""
import os, sys, csv, time, json, argparse, re

CC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SANDBOX = os.path.join(CC, "OS_PRIME_MOVER_ACTIVATION_001", "05_SECURITY_AND_MCP", "blender_sandbox")
LOG = os.path.join(SANDBOX, "BLENDER_GATE_LOG.csv")
DENY_PATH_TOKENS = [".ssh", ".aws", ".env", "credential", "secret", "id_rsa", ".git/", "/.config/",
                    "password", "token", "/Library/Keychains", ".npmrc", ".netrc"]
DESTRUCTIVE_CODE = [r"\bos\.remove\b", r"\bshutil\.rmtree\b", r"\bos\.unlink\b", r"\brm\s+-rf",
                    r"\bsubprocess\b", r"\bsocket\b", r"\burllib\b", r"\brequests\b", r"open\([^)]*['\"]w",
                    r"\bbpy\.ops\.wm\.quit", r"\beval\(", r"\bexec\("]

def path_ok(p):
    ap = os.path.abspath(os.path.expanduser(p))
    in_sandbox = ap.startswith(os.path.abspath(SANDBOX))
    token = next((t for t in DENY_PATH_TOKENS if t in ap.lower()), None)
    return in_sandbox and not token, ("in_sandbox" if in_sandbox else "OUTSIDE SANDBOX") + (f" / DENY:{token}" if token else "")

def code_ok(code):
    if not code: return True, "no code"
    hits = [pat for pat in DESTRUCTIVE_CODE if re.search(pat, code)]
    return (not hits), ("clean" if not hits else f"DESTRUCTIVE/NET: {hits}")

def check_action(kind, path, code, is_test, log=True):
    reasons = []
    pok, pr = path_ok(path) if path else (True, "no path")
    cok, cr = code_ok(code)
    reasons.append(f"path:{pr}"); reasons.append(f"code:{cr}")
    verdict = "ALLOW"
    if kind == "delete": verdict = "DENY"; reasons.append("delete is never allowed")
    if not pok: verdict = "DENY"
    if not cok: verdict = "DENY"
    if verdict == "ALLOW" and not is_test and kind in ("create", "modify", "export", "python"):
        verdict = "CONFIRM"; reasons.append("beyond test scene -> needs per-action human confirm")
    if log:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        new = not os.path.exists(LOG)
        with open(LOG, "a", newline="") as f:
            w = csv.writer(f)
            if new: w.writerow(["ts", "kind", "path", "verdict", "reasons", "is_test"])
            w.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), kind, path or "", verdict, "; ".join(reasons), is_test])
    return verdict, reasons

POLICY = {
  "sandbox_only": SANDBOX, "deny": ["delete", "OS-root writes", "private-repo traversal", "credential paths",
  "network/subprocess in generated code", "eval/exec", "Blender quit"],
  "allow_in_sandbox": ["read sandbox", "create test scene", "render a frame", "export to sandbox"],
  "confirm_required": "any create/modify/export/python beyond a harmless test scene",
  "always": ["log every action", "artifact proof required", "no credential access", "no OS root writes"],
}

def main():
    ap = argparse.ArgumentParser(prog="os_blender_gate.py"); sub = ap.add_subparsers(dest="cmd")
    cp = sub.add_parser("check-path"); cp.add_argument("path")
    ca = sub.add_parser("check-action"); ca.add_argument("--kind", required=True); ca.add_argument("--path", default="")
    ca.add_argument("--code", default=""); ca.add_argument("--test", action="store_true")
    sub.add_parser("audit"); sub.add_parser("policy")
    a = ap.parse_args()
    if a.cmd == "check-path":
        ok, r = path_ok(a.path); print(f"{'ALLOW' if ok else 'DENY'}: {r}"); return 0 if ok else 1
    if a.cmd == "check-action":
        v, r = check_action(a.kind, a.path or None, a.code or None, a.test)
        print(f"BLENDER GATE: {v}"); [print(f"  - {x}") for x in r]; return 0 if v == "ALLOW" else (2 if v == "CONFIRM" else 1)
    if a.cmd == "policy": print(json.dumps(POLICY, indent=2)); return 0
    if a.cmd == "audit":
        if os.path.exists(LOG): print(open(LOG).read())
        else: print("no blender actions logged")
        return 0
    ap.print_help(); return 0

if __name__ == "__main__": sys.exit(main())
