#!/usr/bin/env python3
"""
BATCH_007 extraction · locked doctrine + SOPs + working drafts + outreach/delivery/content/commercial operator docs

55 sources across 8 raw/ folders:
  - 12 from raw/00_BRIEF/ + 2 from raw/00_BRIEF/templates/ · locked doctrine NEW
  - 13 from raw/05_PRODUCTION/*.md · production SOPs NEW
  -  7 from raw/03_OUTREACH/*.md · outreach SOPs NEW (SOP_assistant.md canonical)
  - 11 from raw/06_DELIVERY/ (2 + 9 email templates) · delivery docs
  -  7 from raw/07_CONTENT/*.md · content docs
  -  3 singletons (01_OFFERS/, 04_CRM/, 13_NETWORK/) · commercial / network

Output: 01_KNOWLEDGE_BASE/batches/batch_007_extracted/
Log:    00_COMMAND_CENTER/batch_logs/BATCH_007_EXTRACTION_LOG.md

Extraction method per BATCH_007_PLAN.md §7: all 55 sources are .md · direct copy
with normalized filenames. No pandoc, no pdftotext, no OCR, no Whisper.
Python stdlib only (shutil.copy2).
"""

import shutil
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
RAW = ROOT / "raw"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "batch_007_extracted"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "BATCH_007_EXTRACTION_LOG.md"

DEST.mkdir(parents=True, exist_ok=True)
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)


# 55 jobs · all .md · copy with normalized filename
JOBS = []

# P1 · Locked doctrine (14 files · 12 from 00_BRIEF/ root + 2 from templates/)
P1_LOCKED_DOCTRINE = [
    ("00_BRIEF/CANONICAL_TRUTHS.md",                       "brief__canonical_truths.md"),
    ("00_BRIEF/THE_SPINE.md",                              "brief__the_spine.md"),
    ("00_BRIEF/THE_LINEAGE_DOCTRINE.md",                   "brief__the_lineage_doctrine.md"),
    ("00_BRIEF/OPERATING_LOCKS_2026-05-12.md",             "brief__operating_locks_2026_05_12.md"),
    ("00_BRIEF/THE_OPERATOR_CODED_DEFINITION.md",          "brief__the_operator_coded_definition.md"),
    ("00_BRIEF/LEAN_EXECUTION_AUDIT.md",                   "brief__lean_execution_audit.md"),
    ("00_BRIEF/MONDAY_COCKPIT.md",                         "brief__monday_cockpit.md"),
    ("00_BRIEF/SATURDAY_BUILD_BRIEF.md",                   "brief__saturday_build_brief.md"),
    ("00_BRIEF/SYSTEM_FINAL_STATUS.md",                    "brief__system_final_status.md"),
    ("00_BRIEF/OPERATOR_QUESTIONS_2026-05-13.md",          "brief__operator_questions_2026_05_13.md"),
    ("00_BRIEF/PARTNERSHIP_PROTOCOL.md",                   "brief__partnership_protocol.md"),
    ("00_BRIEF/recurring_checklists.md",                   "brief__recurring_checklists.md"),
    ("00_BRIEF/templates/monthly_constraint_audit.md",     "brief__monthly_constraint_audit.md"),
    ("00_BRIEF/templates/weekly_review.md",                "brief__weekly_review.md"),
]
for src, out in P1_LOCKED_DOCTRINE:
    JOBS.append({"src": src, "out": out, "tier": "P1_locked_doctrine"})

# P2 · Production SOPs (13)
P2_PRODUCTION_SOPS = [
    ("05_PRODUCTION/casting_call_doctrine_v1.md",          "production__casting_call_doctrine_v1.md"),
    ("05_PRODUCTION/ch02_mimi_production_brief_v1.md",     "production__ch02_mimi_production_brief_v1.md"),
    ("05_PRODUCTION/chapter_intake_v1.md",                 "production__chapter_intake_v1.md"),
    ("05_PRODUCTION/checklist_post_shoot_same_day.md",     "production__checklist_post_shoot_same_day.md"),
    ("05_PRODUCTION/checklist_pre_shoot_day_of.md",        "production__checklist_pre_shoot_day_of.md"),
    ("05_PRODUCTION/composite_environment_rotation_v1.md", "production__composite_environment_rotation_v1.md"),
    ("05_PRODUCTION/lightroom_operating_system.md",        "production__lightroom_operating_system.md"),
    ("05_PRODUCTION/preset_library.md",                    "production__preset_library.md"),
    ("05_PRODUCTION/retoucher_training_notes.md",          "production__retoucher_training_notes.md"),
    ("05_PRODUCTION/SOP_capture_to_delivery.md",           "production__sop_capture_to_delivery.md"),
    ("05_PRODUCTION/SOP_reset_shoot_day.md",               "production__sop_reset_shoot_day.md"),
    ("05_PRODUCTION/SOP_strategic_free.md",                "production__sop_strategic_free.md"),
    ("05_PRODUCTION/track_b_frame_walkthrough.md",         "production__track_b_frame_walkthrough.md"),
]
for src, out in P2_PRODUCTION_SOPS:
    JOBS.append({"src": src, "out": out, "tier": "P2_production_sop"})

# P3 · Outreach SOPs (7 · SOP_assistant.md canonical per operator decision)
P3_OUTREACH_SOPS = [
    ("03_OUTREACH/linkedin_comment_doctrine_v1.md", "outreach__linkedin_comment_doctrine_v1.md"),
    ("03_OUTREACH/SOP_assistant.md",                "outreach__sop_assistant.md"),
    ("03_OUTREACH/SOP_discovery_call.md",           "outreach__sop_discovery_call.md"),
    ("03_OUTREACH/SOP_discovery_to_close.md",       "outreach__sop_discovery_to_close.md"),
    ("03_OUTREACH/SOP_VIB_production.md",           "outreach__sop_vib_production.md"),
    ("03_OUTREACH/VIB_caption_library.md",          "outreach__vib_caption_library.md"),
    ("03_OUTREACH/VIB_figma_spec.md",               "outreach__vib_figma_spec.md"),
]
for src, out in P3_OUTREACH_SOPS:
    JOBS.append({"src": src, "out": out, "tier": "P3_outreach_sop"})

# P4 · Delivery docs (11)
P4_DELIVERY_DOCS = [
    ("06_DELIVERY/SOP_post_delivery.md",                       "delivery__sop_post_delivery.md"),
    ("06_DELIVERY/pixieset_config.md",                         "delivery__pixieset_config.md"),
    ("06_DELIVERY/email_templates/01_pre_shoot_brief.md",      "delivery__email_01_pre_shoot_brief.md"),
    ("06_DELIVERY/email_templates/02_day0_delivery.md",        "delivery__email_02_day0_delivery.md"),
    ("06_DELIVERY/email_templates/03_day7_testimonial.md",     "delivery__email_03_day7_testimonial.md"),
    ("06_DELIVERY/email_templates/04_day19_window_closing.md", "delivery__email_04_day19_window_closing.md"),
    ("06_DELIVERY/email_templates/05_day30_opkit_pitch.md",    "delivery__email_05_day30_opkit_pitch.md"),
    ("06_DELIVERY/email_templates/06_day90_reengagement.md",   "delivery__email_06_day90_reengagement.md"),
    ("06_DELIVERY/email_templates/07_referral_ask.md",         "delivery__email_07_referral_ask.md"),
    ("06_DELIVERY/email_templates/08_booking_confirmation.md", "delivery__email_08_booking_confirmation.md"),
    ("06_DELIVERY/email_templates/09_no_show_or_late_followup.md", "delivery__email_09_no_show_or_late_followup.md"),
]
for src, out in P4_DELIVERY_DOCS:
    JOBS.append({"src": src, "out": out, "tier": "P4_delivery_sop"})

# P5 · Content docs (7)
P5_CONTENT_DOCS = [
    ("07_CONTENT/audience_engine.md",                "content__audience_engine.md"),
    ("07_CONTENT/caption_templates.md",              "content__caption_templates.md"),
    ("07_CONTENT/cultural_documentation_thesis.md",  "content__cultural_documentation_thesis.md"),
    ("07_CONTENT/hook_library.md",                   "content__hook_library.md"),
    ("07_CONTENT/linkedin_pov_bank.md",              "content__linkedin_pov_bank.md"),
    ("07_CONTENT/sniped_content_philosophy.md",      "content__sniped_content_philosophy.md"),
    ("07_CONTENT/sniped_video_philosophy.md",        "content__sniped_video_philosophy.md"),
]
for src, out in P5_CONTENT_DOCS:
    JOBS.append({"src": src, "out": out, "tier": "P5_content_strategy"})

# P6 · Commercial / network singletons (3)
P6_COMMERCIAL = [
    ("01_OFFERS/delivery_architecture_v2.md",          "offers__delivery_architecture_v2.md"),
    ("04_CRM/notion_crm_schemas.md",                   "crm__notion_crm_schemas.md"),
    ("13_NETWORK/access_and_community_architecture.md", "network__access_and_community_architecture.md"),
]
for src, out in P6_COMMERCIAL:
    JOBS.append({"src": src, "out": out, "tier": "P6_commercial_architecture"})


def main():
    log_lines = ["# BATCH_007 extraction log · locked doctrine + SOPs + working drafts · 2026-05-19\n"]
    log_lines.append(f"Total jobs: {len(JOBS)}\n")
    log_lines.append("\n| # | Tier | Source | Out | Status | Words | Notes |")
    log_lines.append("|--:|---|---|---|---|---:|---|")

    ok_count = 0
    fail_count = 0
    for i, job in enumerate(JOBS, 1):
        src = RAW / job["src"]
        out = DEST / job["out"]
        if not src.exists():
            log_lines.append(f"| {i} | {job['tier']} | {job['src']} | {job['out']} | MISSING | 0 | source not found |")
            fail_count += 1
            continue
        if out.exists():
            log_lines.append(f"| {i} | {job['tier']} | {job['src']} | {job['out']} | SKIP | - | already extracted |")
            ok_count += 1
            continue
        try:
            shutil.copy2(src, out)
            text = out.read_text(encoding="utf-8", errors="ignore")
            words = len(text.split())
            log_lines.append(f"| {i} | {job['tier']} | {job['src']} | {job['out']} | OK | {words} | copy OK |")
            ok_count += 1
        except Exception as e:
            log_lines.append(f"| {i} | {job['tier']} | {job['src']} | {job['out']} | FAIL | 0 | {e} |")
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
