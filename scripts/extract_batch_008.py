#!/usr/bin/env python3
"""
BATCH_008 extraction · AI / tech / automation / agency / operating-edge canon

Core: 17 sources (per 00_COMMAND_CENTER/BATCH_008_PLAN.md §2).
  Cluster A · 12 ai_tech canon books (raw/02_TIER_1_CANON_BOOKS/ai_tech/):
    9 epub  -> stdlib zipfile + HTML-strip (spine-ordered)
    2 pdf   -> pdftotext -layout (Network State, Life 3.0)
    1 mobi  -> ebook-convert (The Second Machine Age) · CONDITIONAL stub-check on the
              "Brilliance Audio on MP3-CD" label · defer + flag if it is an audiobook stub
  Cluster B · AI Edge course + operator/agency docs:
    Finding Your Edge.pdf            -> pdftotext -layout  (raw/05_AI_EDGE_COURSE/)
    COURSE WORK 1 thru 2.docx        -> pandoc -f docx -t plain  (raw/05_AI_EDGE_COURSE/)
    AI CHANGED EVERYTHING.docx       -> pandoc  (raw/08_AI_TECH/ai_history_case_studies/)
    sniped_os_knowledge_dump.docx    -> pandoc  (raw/08_AI_TECH/ai_history_case_studies/)
    youtube skool doc.docx           -> pandoc  (raw/10_REFERENCE/_intake_2026-05-18/)

EXCLUDED (already chunked · do NOT touch): claude_for_small_business (B2B),
  Claude Code Superpowers/Plugin/Built an AI SaaS/REMOTION/AI Ops Dashboard PRD (B006).
DISCOVERED EXTRAS + recovery items: NOT in this run (operator decision · 0 chunks).
No OCR. No new dependencies. In-copyright · extracted text is INTERNAL chunk-authoring reference only.
"""

import html
import re
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
AI_LANE = ROOT / "raw" / "02_TIER_1_CANON_BOOKS" / "ai_tech"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "batch_008_extracted"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "BATCH_008_EXTRACTION_LOG.md"
EBOOK_CONVERT = "/opt/homebrew/bin/ebook-convert"
PDFTOTEXT = "/opt/homebrew/bin/pdftotext"
PANDOC = "/opt/homebrew/bin/pandoc"

BOOK_FLOOR = 8000     # a real full-length book; below this means broken extraction or a sample stub
COURSE_FLOOR = 1500   # Finding Your Edge.pdf (course PDF)
DOC_FLOOR = 200       # operator docx
MOBI_STUB_FLOOR = 15000  # Second Machine Age · below -> treat as audiobook-companion stub · DEFER + flag

# Cluster A epub books · (keyword to match the staged filename, outname, author, title)
EPUB_BOOKS = [
    ("Automate This", "automate_this_steiner.txt", "Christopher Steiner", "Automate This (2012)"),
    ("Only Humans Need Apply", "only_humans_need_apply_davenport.txt", "Thomas H. Davenport, Julia Kirby", "Only Humans Need Apply (2016)"),
    ("Power and Prediction", "power_and_prediction_agrawal.txt", "Agrawal, Gans, Goldfarb", "Power and Prediction (2022)"),
    ("Prediction Machines", "prediction_machines_agrawal.txt", "Agrawal, Gans, Goldfarb", "Prediction Machines (2018)"),
    ("Read Write Own", "read_write_own_dixon.txt", "Chris Dixon", "Read Write Own (2024)"),
    ("Human + machine", "human_plus_machine_daugherty.txt", "Paul R. Daugherty, H. James Wilson", "Human + Machine (2018)"),
    ("Co-Intelligence", "co_intelligence_mollick.txt", "Ethan Mollick", "Co-Intelligence (2024)"),
    ("Competing in the Age of AI", "competing_in_the_age_of_ai_iansiti.txt", "Karim R. Lakhani, Marco Iansiti", "Competing in the Age of AI (2020)"),
    ("The Coming Wave", "the_coming_wave_suleyman.txt", "Mustafa Suleyman, Michael Bhaskar", "The Coming Wave (2023)"),
]
# Cluster A pdf books in the ai_tech lane · (keyword, outname, author, title, floor)
AI_PDF_BOOKS = [
    ("The Network State", "the_network_state_srinivasan.txt", "Balaji Srinivasan", "The Network State", BOOK_FLOOR),
    ("life-30", "life_3_0_tegmark.txt", "Max Tegmark", "Life 3.0 (2017)", BOOK_FLOOR),
]
# Cluster A mobi · (keyword, outname, author, title)
MOBI_BOOK = ("The Second Machine Age", "the_second_machine_age_brynjolfsson.txt", "Erik Brynjolfsson, Andrew McAfee", "The Second Machine Age (2014)")

# Cluster B · (absolute-relative path, outname, author, title, floor, kind)
CLUSTER_B = [
    ("raw/05_AI_EDGE_COURSE/Finding Your Edge.pdf", "finding_your_edge.txt", "The AI Edge", "Finding Your Edge", COURSE_FLOOR, "pdf"),
    ("raw/05_AI_EDGE_COURSE/COURSE WORK 1 thru 2.docx", "course_work_1_thru_2.txt", "The AI Edge", "AI Edge Course Work 1-2", DOC_FLOOR, "docx"),
    ("raw/08_AI_TECH/ai_history_case_studies/AI CHANGED EVERYTHING.docx", "ai_changed_everything.txt", "SNIPED (operator-authored)", "AI Changed Everything", DOC_FLOOR, "docx"),
    ("raw/08_AI_TECH/ai_history_case_studies/sniped_os_knowledge_dump.docx", "sniped_os_knowledge_dump.txt", "SNIPED (operator-authored)", "SNIPED OS Knowledge Dump", DOC_FLOOR, "docx"),
    ("raw/10_REFERENCE/_intake_2026-05-18/youtube skool doc.docx", "youtube_skool_doc.txt", "SNIPED (operator-authored)", "YouTube / Skool Doc", DOC_FLOOR, "docx"),
]

TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"[ \t\f\v]+")
NL_RE = re.compile(r"\n{3,}")


def strip_html(raw: bytes) -> str:
    s = raw.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style|head)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)</(p|div|h[1-6]|br|li|tr)\s*>", "\n", s)
    s = TAG_RE.sub(" ", s)
    s = html.unescape(s)
    s = WS_RE.sub(" ", s)
    s = "\n".join(line.strip() for line in s.splitlines())
    return NL_RE.sub("\n\n", s).strip()


def reading_order(z):
    names = z.namelist()
    opf = next((n for n in names if n.lower().endswith(".opf")), None)
    htmls = [n for n in names if n.lower().endswith((".html", ".xhtml", ".htm"))]
    if not opf:
        return sorted(htmls)
    try:
        opf_txt = z.read(opf).decode("utf-8", "ignore")
        ids = dict(re.findall(r'<item\s+[^>]*id="([^"]+)"[^>]*href="([^"]+)"', opf_txt))
        for href, idv in re.findall(r'<item\s+[^>]*href="([^"]+)"[^>]*id="([^"]+)"', opf_txt):
            ids.setdefault(idv, href)
        spine = re.findall(r'<itemref\s+[^>]*idref="([^"]+)"', opf_txt)
        ordered = []
        for idref in spine:
            href = ids.get(idref)
            if href:
                match = next((n for n in htmls if n.endswith(href.split("/")[-1])), None)
                if match and match not in ordered:
                    ordered.append(match)
        for n in sorted(htmls):
            if n not in ordered:
                ordered.append(n)
        return ordered or sorted(htmls)
    except Exception:
        return sorted(htmls)


def find_in_lane(lane: Path, keyword: str):
    for p in sorted(lane.iterdir()):
        if keyword.lower() in p.name.lower():
            return p
    return None


def wc(out: Path) -> int:
    return len(out.read_text(encoding="utf-8", errors="ignore").split())


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    log = ["# BATCH_008 extraction log · 2026-05-22\n",
           "AI / tech / automation / agency / operating-edge canon · 17 core sources.\n",
           "Method: stdlib zipfile+HTML-strip (epub) · pdftotext -layout (pdf) · ebook-convert (mobi) · pandoc (docx) · no OCR · no new dependencies.\n",
           "In-copyright · extracted text is INTERNAL chunk-authoring reference only.\n"]
    results = {}
    failed = False
    notes = []
    deferred = []

    log.append("## Cluster A · 9 epub books (stdlib zipfile + HTML-strip)\n")
    for keyword, outname, author, title in EPUB_BOOKS:
        src = find_in_lane(AI_LANE, keyword)
        out = DEST / outname
        if src is None:
            log.append(f"FAIL · not found (keyword '{keyword}')"); failed = True; continue
        try:
            z = zipfile.ZipFile(src)
            text = ("\n\n".join(p for p in (strip_html(z.read(n)) for n in reading_order(z)) if p)).strip() + "\n"
            out.write_text(text, encoding="utf-8")
            results[outname] = wc(out)
            flag = "" if results[outname] >= BOOK_FLOOR else f"  WARNING below floor {BOOK_FLOOR}"
            log.append(f"OK · epub · {title} -> {outname} · {results[outname]:,} words{flag}")
            if results[outname] < BOOK_FLOOR:
                failed = True
        except Exception as e:
            log.append(f"FAIL · epub · {title}: {str(e)[:120]}"); failed = True

    log.append("\n## Cluster A · 2 pdf books (pdftotext -layout)\n")
    for keyword, outname, author, title, floor in AI_PDF_BOOKS:
        src = find_in_lane(AI_LANE, keyword)
        out = DEST / outname
        if src is None:
            log.append(f"FAIL · not found (keyword '{keyword}')"); failed = True; continue
        r = subprocess.run([PDFTOTEXT, "-layout", str(src), str(out)], capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            log.append(f"FAIL · pdf · {title} rc {r.returncode}"); failed = True; continue
        out.write_text(NL_RE.sub("\n\n", out.read_text(encoding="utf-8", errors="ignore")).strip() + "\n", encoding="utf-8")
        results[outname] = wc(out)
        flag = "" if results[outname] >= floor else f"  WARNING below floor {floor}"
        log.append(f"OK · pdf · {title} -> {outname} · {results[outname]:,} words{flag}")
        if results[outname] < floor:
            failed = True

    log.append("\n## Cluster A · 1 mobi (ebook-convert · CONDITIONAL stub-check)\n")
    keyword, outname, author, title = MOBI_BOOK
    src = find_in_lane(AI_LANE, keyword)
    out = DEST / outname
    if src is None:
        log.append(f"DEFER · mobi · {title} not found"); deferred.append(f"{title}: not found")
    else:
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / "o.txt"
            r = subprocess.run([EBOOK_CONVERT, str(src), str(tmp)], capture_output=True, text=True, timeout=420)
            if r.returncode == 0 and tmp.exists():
                cand = NL_RE.sub("\n\n", tmp.read_text(encoding="utf-8", errors="ignore")).strip() + "\n"
                cw = len(cand.split())
                if cw >= MOBI_STUB_FLOOR:
                    out.write_text(cand, encoding="utf-8"); results[outname] = cw
                    log.append(f"OK · mobi · {title} -> {outname} · {cw:,} words · stub-check PASS (>= {MOBI_STUB_FLOOR}) · real text, not an audiobook stub")
                    notes.append(f"Second Machine Age mobi: {cw:,} words · real text · INCLUDED")
                else:
                    log.append(f"DEFER · mobi · {title} converted to only {cw} words (< {MOBI_STUB_FLOOR}) · audiobook-companion stub · NOT included")
                    deferred.append(f"Second Machine Age mobi: only {cw} words · audiobook-companion stub · DEFERRED · re-acquire an ebook edition")
            else:
                log.append(f"DEFER · mobi · ebook-convert rc {r.returncode}: {r.stderr.strip()[:150]} · NOT included")
                deferred.append(f"Second Machine Age mobi: ebook-convert FAILED (rc {r.returncode}) · DEFERRED")

    log.append("\n## Cluster B · AI Edge course + operator/agency docs\n")
    for relpath, outname, author, title, floor, kind in CLUSTER_B:
        src = ROOT / relpath
        out = DEST / outname
        if not src.exists():
            log.append(f"FAIL · not found: {relpath}"); failed = True; continue
        if kind == "pdf":
            r = subprocess.run([PDFTOTEXT, "-layout", str(src), str(out)], capture_output=True, text=True, timeout=300)
            ok = r.returncode == 0
        else:  # docx via pandoc
            r = subprocess.run([PANDOC, "-f", "docx", "-t", "plain", str(src), "-o", str(out)], capture_output=True, text=True, timeout=300)
            ok = r.returncode == 0 and out.exists()
        if not ok:
            log.append(f"FAIL · {kind} · {title} rc {r.returncode}: {r.stderr.strip()[:120]}"); failed = True; continue
        out.write_text(NL_RE.sub("\n\n", out.read_text(encoding="utf-8", errors="ignore")).strip() + "\n", encoding="utf-8")
        results[outname] = wc(out)
        flag = "" if results[outname] >= floor else f"  WARNING below floor {floor}"
        log.append(f"OK · {kind} · {title} -> {outname} · {results[outname]:,} words{flag}")
        if results[outname] < floor:
            failed = True

    log.append("\n## Excluded (already chunked · 0 chunks · NOT touched)\n"
               "- claude_for_small_business (organized + legacy) · B2B_POSITIONING_CLAUDE_OPERATOR\n"
               "- Claude Code Superpowers / Plugin / Built an AI SaaS / REMOTION / AI Ops Dashboard PRD · BATCH_006")
    log.append("\n## Discovered extras + recovery items (NOT in this run · 0 chunks)\n"
               "- Loose AI/Claude docs (claude cowork genius, The_Claude_Stack, Claude_Operating_Manual, astro claude websites, using ai x gumroad, MORE CLAUDE 5, ai after ramon, document.pdf, index.html) · operator decision · DEFERRED\n"
               "- Recovery items (Beloved, Maus I, Jonathan Livingston Seagull, Maus II, Russian-author mobi) · OUT of scope")

    log.append("\n## Summary")
    log.append(f"- Included sources extracted OK: {len(results)} of 17 core")
    for k, v in results.items():
        log.append(f"  - {k}: {v:,} words")
    log.append(f"- Total words: {sum(results.values()):,}")
    for n in notes:
        log.append(f"- {n}")
    if deferred:
        log.append("- DEFERRED:")
        for d in deferred:
            log.append(f"  - {d}")

    if failed:
        log.append("\nFAIL · a core source failed or missed its floor. Halt. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL · extraction · see log"); return 1

    log.append("\nDone.")
    LOG_PATH.write_text("\n".join(log), encoding="utf-8")
    print(f"Extraction complete · {len(results)} of 17 core sources · {sum(results.values()):,} words")
    if deferred:
        print("DEFERRED:", "; ".join(deferred))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
