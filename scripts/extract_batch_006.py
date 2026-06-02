#!/usr/bin/env python3
"""
BATCH_006 extraction · operator-engine skill layer (rev 2 · two-pass split)

108 sources across 3 raw/ folders:
  - 51 SNIPED skill packs in raw/_skills/ (50 SKILL.md + 1 SKILL_BUILD_QUEUE.md)
  - 50 framework prompt packs in raw/Claude_AI_Skills_50_Upload_Ready (1)/
  -  7 supporting docs in raw/10_REFERENCE/_intake_2026-05-18/
       (4 Claude/AI tool workflows + 1 framework primitive + 2 JSON blueprints)

Output: 01_KNOWLEDGE_BASE/batches/batch_006_extracted/
Log:    00_COMMAND_CENTER/batch_logs/BATCH_006_EXTRACTION_LOG.md

Extraction method per file type:
  .md   (SKILL.md, ai-ops-dashboard-prd.md)  copy verbatim
  .docx (CLAUDE CODE *, Built an AI SaaS, REMOTION) pandoc -t markdown
  .json (2 automation blueprints)            copy verbatim

No OCR. No Whisper. No new dependencies beyond pandoc (already on PATH).
"""

import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
RAW = ROOT / "raw"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "batch_006_extracted"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "BATCH_006_EXTRACTION_LOG.md"

DEST.mkdir(parents=True, exist_ok=True)
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

PANDOC = "/opt/homebrew/bin/pandoc"


# P1 · 50 SNIPED skills · raw/_skills/sniped-*/SKILL.md  +  meta-doc
SNIPED_SKILLS = [
    "sniped-ai-image-tool-pick",
    "sniped-ai-photographer-market",
    "sniped-ai-sentiment",
    "sniped-analog-premium",
    "sniped-art-series",
    "sniped-assistant-task-routing",
    "sniped-blockbuster-strategy",
    "sniped-canonical-truths",
    "sniped-caption-writer",
    "sniped-capture-to-delivery",
    "sniped-company-of-one",
    "sniped-direction-stack",
    "sniped-discovery-to-close",
    "sniped-evoto-skin-pass",
    "sniped-execution-prioritization",
    "sniped-hero-composite-ceiling",
    "sniped-hero-composite-lite",
    "sniped-higgsfield-pipeline",
    "sniped-hit-mechanics",
    "sniped-hospitality-layer",
    "sniped-lean-audit",
    "sniped-leverage-logic",
    "sniped-lighting-vault",
    "sniped-luxury-edit",
    "sniped-monday-cockpit",
    "sniped-new-luxury",
    "sniped-notion-crm-update",
    "sniped-partnership-protocol",
    "sniped-perennial-seller",
    "sniped-photo-theory",
    "sniped-pixieset-gallery",
    "sniped-positioning-phrases",
    "sniped-post-delivery",
    "sniped-post-shoot-same-day",
    "sniped-pre-shoot-prep",
    "sniped-pricing-decision",
    "sniped-production-os",
    "sniped-retoucher-onboarding",
    "sniped-reverse-roadmap",
    "sniped-seedream-prompt",
    "sniped-shoot-day-reset",
    "sniped-shoot-day-strategic-free",
    "sniped-status-psychology",
    "sniped-strategic-implications",
    "sniped-trust-equation",
    "sniped-trust-mechanics",
    "sniped-udemy-ai-accelerants",
    "sniped-udemy-lightroom-rails",
    "sniped-vib-outreach",
    "sniped-wwp-positioning",
]

# P2 · 50-skill prompt pack · raw/Claude_AI_Skills_50_Upload_Ready (1)/*/SKILL.md
FIFTY_PACK = [
    "ai-agent-architecture-wat",
    "ai-code-website-build-pipeline",
    "ai-video-production-pipeline",
    "bad-strategy-audit",
    "business-entity-credit-architecture",
    "business-resilience-audit",
    "calm-authority-voice-calibration",
    "cognitive-bias-audit",
    "cold-email-campaign-architecture",
    "comparative-advantage-resource-allocation",
    "consultative-selling-system",
    "copywriting-rule-of-one-awareness-staging",
    "counter-positioning-diagnosis",
    "create-destroy-strategy-stress-test",
    "creative-resistance-turning-pro",
    "customer-segment-slicing",
    "economic-incentive-policy-analysis",
    "epms-site-analysis",
    "fermi-estimation",
    "framework-orchestrator",
    "freelance-platform-optimization",
    "hoshin-kanri-goal-alignment",
    "industry-dynamics-assessment",
    "lean-transformation-diagnostic",
    "linkedin-growth-lead-generation",
    "market-evaluation-scorecard",
    "meta-business-infrastructure-setup",
    "mom-test-customer-conversation",
    "munger-two-track-decision-analysis",
    "negotiation-leverage-black-swan",
    "photography-business-system",
    "premortem-analysis",
    "preset-sync-export-photo-editing",
    "professional-portrait-direction",
    "prompt-engineering-tcrei",
    "pyramid-structured-communication",
    "revenue-growth-diagnostic",
    "second-brain-code-para",
    "server-farm-commissioning",
    "seven-powers-strategic-position-assessment",
    "shadow-test-pre-launch-validation",
    "signal-noise-forecasting-bayesian",
    "social-media-content-strategy",
    "strategy-kernel-development",
    "success-message-design",
    "superforecasting-workflow",
    "system-analysis-intervention-design",
    "tactical-negotiation-ackerman-empathy",
    "value-stream-improvement-pdca",
    "video-editing-assembly-line",
]

JOBS = []

# P1: SKILL_BUILD_QUEUE meta-doc
JOBS.append({
    "src": "_skills/SKILL_BUILD_QUEUE.md",
    "out": "_skills__skill_build_queue.md",
    "tool": "copy",
    "tier": "P1_meta",
})

# P1: 50 SNIPED skills
for name in SNIPED_SKILLS:
    JOBS.append({
        "src": f"_skills/{name}/SKILL.md",
        "out": f"_skills__{name.replace('-', '_')}.md",
        "tool": "copy",
        "tier": "P1_sniped_skill",
    })

# P2: 50-skill prompt pack
for name in FIFTY_PACK:
    JOBS.append({
        "src": f"Claude_AI_Skills_50_Upload_Ready (1)/{name}/SKILL.md",
        "out": f"claude50__{name.replace('-', '_')}.md",
        "tool": "copy",
        "tier": "P2_claude50",
    })

# P3 · Claude / AI tool workflows (4)
JOBS.extend([
    {"src": "10_REFERENCE/_intake_2026-05-18/CLAUDE CODE SUPERPOWERS.docx",
     "out": "intake__claude_code_superpowers.md", "tool": "docx", "tier": "P3_tooling"},
    {"src": "10_REFERENCE/_intake_2026-05-18/CLAUDE CODE PLUGIN.docx",
     "out": "intake__claude_code_plugin.md", "tool": "docx", "tier": "P3_tooling"},
    {"src": "10_REFERENCE/_intake_2026-05-18/ai-ops-dashboard-prd.md",
     "out": "intake__ai_ops_dashboard_prd.md", "tool": "copy", "tier": "P3_tooling"},
    {"src": "10_REFERENCE/_intake_2026-05-18/Built an AI SaaS in 20 min.docx",
     "out": "intake__built_an_ai_saas_in_20_min.md", "tool": "docx", "tier": "P3_tooling"},
])

# P4 · Automation blueprints + framework primitive (3)
JOBS.extend([
    {"src": "10_REFERENCE/_intake_2026-05-18/REMOTION.docx",
     "out": "intake__remotion.md", "tool": "docx", "tier": "P4_automation"},
    {"src": "10_REFERENCE/_intake_2026-05-18/automations/AI Content Strategy Generator - Lead Magnet.json",
     "out": "intake__automation_ai_content_strategy_generator.json", "tool": "copy", "tier": "P4_automation"},
    {"src": "10_REFERENCE/_intake_2026-05-18/automations/Blueprint - ElevenLabs Agent That Calls & Qualifies Leads.json",
     "out": "intake__automation_elevenlabs_voice_agent.json", "tool": "copy", "tier": "P4_automation"},
])


def run_docx(src: Path, out: Path) -> tuple[bool, str, int]:
    try:
        result = subprocess.run(
            [PANDOC, "-f", "docx", "-t", "markdown", "--wrap=none", "-o", str(out), str(src)],
            capture_output=True, text=True, timeout=120,
        )
        if result.returncode != 0:
            return False, f"pandoc returncode {result.returncode}: {result.stderr.strip()[:200]}", 0
        words = len(out.read_text(encoding="utf-8", errors="ignore").split())
        return True, "pandoc OK", words
    except Exception as e:
        return False, f"exception: {e}", 0


def run_copy(src: Path, out: Path) -> tuple[bool, str, int]:
    try:
        shutil.copy2(src, out)
        text = out.read_text(encoding="utf-8", errors="ignore")
        words = len(text.split())
        return True, "copy OK", words
    except Exception as e:
        return False, f"exception: {e}", 0


def main():
    log_lines = ["# BATCH_006 extraction log · operator-engine skill layer · 2026-05-18\n"]
    log_lines.append(f"Total jobs: {len(JOBS)}\n")
    log_lines.append("\n| # | Tier | Source | Out | Tool | Status | Words | Notes |")
    log_lines.append("|--:|---|---|---|---|---|---:|---|")

    ok_count = 0
    fail_count = 0
    for i, job in enumerate(JOBS, 1):
        src = RAW / job["src"]
        out = DEST / job["out"]
        if not src.exists():
            log_lines.append(f"| {i} | {job['tier']} | {job['src']} | {job['out']} | {job['tool']} | MISSING | 0 | source not found |")
            fail_count += 1
            continue
        if out.exists():
            log_lines.append(f"| {i} | {job['tier']} | {job['src']} | {job['out']} | {job['tool']} | SKIP | - | already extracted |")
            ok_count += 1
            continue
        if job["tool"] == "docx":
            ok, note, words = run_docx(src, out)
        elif job["tool"] == "copy":
            ok, note, words = run_copy(src, out)
        else:
            ok, note, words = False, f"unknown tool: {job['tool']}", 0
        status = "OK" if ok else "FAIL"
        log_lines.append(f"| {i} | {job['tier']} | {job['src']} | {job['out']} | {job['tool']} | {status} | {words} | {note} |")
        if ok:
            ok_count += 1
        else:
            fail_count += 1

    log_lines.append("")
    log_lines.append(f"## Summary")
    log_lines.append(f"- Total jobs: {len(JOBS)}")
    log_lines.append(f"- Extracted OK: {ok_count}")
    log_lines.append(f"- Failed/Missing: {fail_count}")
    log_lines.append("")
    log_lines.append("Done.")

    LOG_PATH.write_text("\n".join(log_lines), encoding="utf-8")
    print(f"Extraction complete · OK={ok_count} · FAIL={fail_count} · jobs={len(JOBS)}")
    print(f"Log: {LOG_PATH}")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
