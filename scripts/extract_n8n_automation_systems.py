#!/usr/bin/env python3
"""
N8N_AUTOMATION_SYSTEMS extraction · 6 n8n workflow JSON exports (The AI Edge)

Source lane: raw/10_REFERENCE/_intake_2026-05-19/automations/
Output: 01_KNOWLEDGE_BASE/batches/n8n_automation_systems_extracted/<normalized>.txt (one per workflow)
Log: 00_COMMAND_CENTER/batch_logs/N8N_AUTOMATION_SYSTEMS_EXTRACTION_LOG.md

Method: stdlib json ONLY · NO new dependencies.
Per workflow, emit a normalized text summary:
  - workflow name (filename + internal)
  - node inventory (type + name + durable non-secret params)
  - trigger nodes
  - AI/model nodes (model + system-prompt excerpt)
  - tool nodes
  - integration nodes (Airtable/Perplexity/httpRequest host)
  - data-flow edges (connections graph)
  - sticky-note documentation (verbatim)
  - credential references BY NAME ONLY

Security: STRIP credential value fields, auth headers, tokens, secrets, pinData.
A literal-secret scan runs over every emitted file; if a secret pattern is detected,
the run HALTS and reports (does not write the offending file as-is).
"""

import json
import re
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
LANE = ROOT / "raw" / "10_REFERENCE" / "_intake_2026-05-19" / "automations"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "n8n_automation_systems_extracted"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "N8N_AUTOMATION_SYSTEMS_EXTRACTION_LOG.md"

# filename -> normalized output name
FILES = {
    "AI Phone Call Assistant - Call Workflow.json": "ai_phone_call_assistant.txt",
    "n8n & RetellAI.json": "n8n_retellai.txt",
    "Master Prompt Agent - Chat Input.json": "master_prompt_agent_chat_input.txt",
    "Master Prompt Agent - Form Submission.json": "master_prompt_agent_form_submission.txt",
    "Prompt Writing Agent - Deep Reasoning Workflow.json": "prompt_writing_agent_deep_reasoning.txt",
    "Prompt Writing Agent - Normal Model Workflow.json": "prompt_writing_agent_normal_model.txt",
}

# secret-looking patterns · used to HALT if anything leaks into output
SECRET_RE = re.compile(
    r"(sk-[A-Za-z0-9]{16,}"          # OpenAI-style
    r"|sk-or-[A-Za-z0-9-]{16,}"      # OpenRouter
    r"|AKIA[0-9A-Z]{12,}"            # AWS
    r"|Bearer\s+[A-Za-z0-9._\-]{16,}"
    r"|key-[A-Za-z0-9]{16,}"
    r"|[A-Za-z0-9_\-]{32,}\.[A-Za-z0-9_\-]{16,}\.[A-Za-z0-9_\-]{16,})"  # JWT-ish
)

# parameter keys whose VALUES must never be emitted
SENSITIVE_KEYS = {
    "credentials", "pindata", "pinData", "authentication", "headerauth",
    "httpheaderauth", "authorization", "token", "apikey", "api_key",
    "secret", "password", "accesstoken", "access_token", "bearertoken",
    "privatekey", "private_key", "clientsecret", "client_secret", "webhookid",
}


def excerpt(s, n=400):
    return " ".join(str(s).split())[:n]


def cred_names(node):
    out = []
    for cid, cval in (node.get("credentials") or {}).items():
        name = cval.get("name", "") if isinstance(cval, dict) else ""
        out.append(f"{cid}/{name}" if name else cid)
    return out


def model_of(node):
    p = node.get("parameters", {}) or {}
    m = p.get("model")
    if isinstance(m, dict):
        return m.get("value") or m.get("mode") or "?"
    return m or "?"


def system_prompt(node):
    p = node.get("parameters", {}) or {}
    opts = p.get("options", {}) or {}
    for v in (opts.get("systemMessage"), p.get("text"),
              p.get("messages") if isinstance(p.get("messages"), str) else None):
        if isinstance(v, str) and v.strip():
            return v
    return ""


def http_host(node):
    p = node.get("parameters", {}) or {}
    url = p.get("url", "")
    if isinstance(url, str) and url:
        # keep host + path shape, strip query string (may carry tokens)
        u = url.split("?")[0]
        return u
    return ""


def summarize(name_file, data):
    nodes = data.get("nodes", []) or []
    conns = data.get("connections", {}) or {}
    L = []
    L.append(f"# n8n workflow · {name_file}")
    L.append(f"internal name: {data.get('name','?')}")
    L.append(f"node count: {len(nodes)}")
    L.append("")

    triggers, ai_nodes, tools, integrations, others = [], [], [], [], []
    all_creds = set()
    sticky = []

    for n in nodes:
        t = n.get("type", "?")
        nm = n.get("name", "")
        for c in cred_names(n):
            all_creds.add(c)
        if t.endswith("stickyNote"):
            content = (n.get("parameters", {}) or {}).get("content", "")
            if content.strip():
                sticky.append(content)
            continue
        tl = t.lower()
        if "trigger" in tl or t.endswith("webhook"):
            triggers.append((t, nm))
        elif t.endswith("agent") or "lmchat" in tl or t.endswith("chainLlm"):
            ai_nodes.append((t, nm))
        elif "tool" in tl:
            tools.append((t, nm))
        elif t.endswith("httpRequest") or t.endswith("airtable") or t.endswith("respondToWebhook") or t.endswith("form"):
            integrations.append((t, nm))
        else:
            others.append((t, nm))

    def block(title, items):
        L.append(f"## {title}")
        if not items:
            L.append("(none)")
        for t, nm in items:
            L.append(f"- {t} :: {nm}")
        L.append("")

    block("Trigger nodes", triggers)

    L.append("## AI / model nodes")
    if not ai_nodes:
        L.append("(none)")
    for n in nodes:
        t = n.get("type", "")
        tl = t.lower()
        if t.endswith("agent") or "lmchat" in tl or t.endswith("chainLlm"):
            sp = system_prompt(n)
            line = f"- {t} :: {n.get('name','')} :: model={model_of(n)}"
            L.append(line)
            if sp:
                L.append(f"    system-prompt: {excerpt(sp, 500)}")
    L.append("")

    block("Tool nodes", tools)

    L.append("## Integration / action nodes")
    if not integrations:
        L.append("(none)")
    for n in nodes:
        t = n.get("type", "")
        if t.endswith("httpRequest"):
            p = n.get("parameters", {}) or {}
            L.append(f"- {t} :: {n.get('name','')} :: method={p.get('method','GET')} url={http_host(n)}")
        elif t.endswith("airtable"):
            p = n.get("parameters", {}) or {}
            base = p.get("base", {}); tbl = p.get("table", {})
            bn = base.get("cachedResultName","") if isinstance(base, dict) else ""
            tn = tbl.get("cachedResultName","") if isinstance(tbl, dict) else ""
            L.append(f"- {t} :: {n.get('name','')} :: base={bn} table={tn} op={p.get('operation','')}")
        elif t.endswith("respondToWebhook") or t.endswith("form"):
            L.append(f"- {t} :: {n.get('name','')}")
    L.append("")

    block("Other nodes", others)

    L.append("## Data-flow edges (connections)")
    if not conns:
        L.append("(none)")
    for src, outs in conns.items():
        targets = []
        for out_type, branches in (outs or {}).items():
            for branch in branches or []:
                for c in branch or []:
                    targets.append(c.get("node", "?"))
        L.append(f"- {src} -> {targets}")
    L.append("")

    L.append("## Credential references (NAMES ONLY)")
    L.append(", ".join(sorted(all_creds)) if all_creds else "(none)")
    L.append("")

    L.append("## Sticky-note documentation (verbatim)")
    if not sticky:
        L.append("(none)")
    for s in sticky:
        L.append("---")
        L.append(s.strip())
    L.append("")

    return "\n".join(L) + "\n"


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    log = ["# N8N_AUTOMATION_SYSTEMS extraction log · 2026-05-19\n",
           "Method: stdlib json · no new dependencies. Credentials reduced to names; pinData/secrets stripped.\n"]
    total_words = 0
    leaks = []
    cred_index = {}

    for fname, outname in FILES.items():
        src = LANE / fname
        out = DEST / outname
        if not src.exists():
            log.append(f"FAIL · source not found: {fname}")
            LOG_PATH.write_text("\n".join(log), encoding="utf-8")
            print("FAIL · missing source")
            return 1
        data = json.loads(src.read_text(encoding="utf-8"))
        text = summarize(fname, data)
        # secret scan BEFORE writing
        hits = SECRET_RE.findall(text)
        if hits:
            leaks.append((outname, len(hits)))
            log.append(f"HALT · secret-like pattern in {outname} ({len(hits)} hits) · NOT writing")
            continue
        out.write_text(text, encoding="utf-8")
        words = len(text.split())
        total_words += words
        # record cred names for the report
        for line in text.splitlines():
            pass
        log.append(f"OK · {fname} -> {outname} · {words} words")

    if leaks:
        log.append("\nFAIL · secret leak detected. Halt. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL · secret leak:", leaks)
        return 1

    # post-write secret scan across all emitted files
    scan_hits = 0
    for outname in FILES.values():
        p = DEST / outname
        if p.exists():
            scan_hits += len(SECRET_RE.findall(p.read_text(encoding="utf-8")))

    log.append("\n## Summary")
    log.append(f"- Sources in: {len(FILES)}")
    log.append(f"- Extracted OK: {sum(1 for o in FILES.values() if (DEST/o).exists())}")
    log.append(f"- Total words: {total_words:,}")
    log.append(f"- Literal-secret scan over emitted files: {scan_hits} hit(s)  ({'CLEAN' if scan_hits==0 else 'REVIEW'})")
    log.append("- Credentials: reduced to provider/name references only · no values emitted.")
    log.append("- pinData: skipped (not extracted).")
    log.append("\nDone.")
    LOG_PATH.write_text("\n".join(log), encoding="utf-8")
    print(f"Extraction complete · {len(FILES)} workflows · {total_words:,} words · secret-scan {scan_hits} hits")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
