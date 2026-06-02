#!/usr/bin/env python3
"""
OPPORTUNITY_MANAGEMENT_TEMPLATES extraction · AI Edge opportunity-management assets

Sources:
  xlsx: raw/10_REFERENCE/_intake_2026-05-19/opportunity_management/Opp hopper + Biz Case.xlsx
  pptx: raw/10_REFERENCE/_intake_2026-05-19/opportunity_management/Opportunity Card [Example].pptx

Outputs:
  01_KNOWLEDGE_BASE/batches/opportunity_management_templates_extracted/opp_hopper_biz_case.txt
  01_KNOWLEDGE_BASE/batches/opportunity_management_templates_extracted/opportunity_card_example.txt

Log: 00_COMMAND_CENTER/batch_logs/OPPORTUNITY_MANAGEMENT_TEMPLATES_EXTRACTION_LOG.md

Method: stdlib zipfile + xml.etree.ElementTree ONLY · NO new dependencies.
  xlsx: parse workbook.xml (sheet names + order via rId -> sheetN.xml), sharedStrings.xml
        (string table), worksheets/sheetN.xml (cells · resolve t="s" shared-string indices,
        inline t="inlineStr", and numeric/formula cached values). Render per-sheet text grid.
  pptx: iterate ppt/slides/slideN.xml in numeric order, pull <a:t> runs per slide. Ignore media.
No OCR.
"""

import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
LANE = ROOT / "raw" / "10_REFERENCE" / "_intake_2026-05-19" / "opportunity_management"
SRC_XLSX = LANE / "Opp hopper + Biz Case.xlsx"
SRC_PPTX = LANE / "Opportunity Card [Example].pptx"

DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "opportunity_management_templates_extracted"
OUT_XLSX = DEST / "opp_hopper_biz_case.txt"
OUT_PPTX = DEST / "opportunity_card_example.txt"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "OPPORTUNITY_MANAGEMENT_TEMPLATES_EXTRACTION_LOG.md"

MIN_WORDS = 100  # template assets are sparse · low floor

# OOXML namespaces
NS_SS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
NS_REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
NS_PKGREL = "{http://schemas.openxmlformats.org/package/2006/relationships}"
NS_A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def col_to_idx(ref: str) -> int:
    """Cell ref like 'B7' -> zero-based column index."""
    letters = re.match(r"([A-Z]+)", ref).group(1)
    n = 0
    for ch in letters:
        n = n * 26 + (ord(ch) - 64)
    return n - 1


def extract_xlsx(src: Path, out: Path, log: list) -> int:
    z = zipfile.ZipFile(src)

    # shared strings
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        root = ET.fromstring(z.read("xl/sharedStrings.xml"))
        for si in root.findall(f"{NS_SS}si"):
            # concat all <t> descendants (handles rich-text runs)
            txt = "".join(t.text or "" for t in si.iter(f"{NS_SS}t"))
            shared.append(txt)

    # sheet name -> rId, then rId -> target file
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    rid_to_target = {}
    for rel in rels.findall(f"{NS_PKGREL}Relationship"):
        rid_to_target[rel.get("Id")] = rel.get("Target")
    sheets = []  # (name, worksheet_path)
    for sh in wb.find(f"{NS_SS}sheets").findall(f"{NS_SS}sheet"):
        name = sh.get("name")
        rid = sh.get(f"{NS_REL}id")
        target = rid_to_target.get(rid, "")
        path = "xl/" + target.lstrip("/") if not target.startswith("xl/") else target
        sheets.append((name, path))

    lines = ["# Opportunity Hopper + Business Case · The AI Edge (xlsx extraction)\n"]
    for name, path in sheets:
        lines.append(f"\n===== SHEET: {name} =====")
        if path not in z.namelist():
            lines.append("(worksheet xml not found)")
            continue
        ws = ET.fromstring(z.read(path))
        sheet_data = ws.find(f"{NS_SS}sheetData")
        if sheet_data is None:
            lines.append("(empty)")
            continue
        for row in sheet_data.findall(f"{NS_SS}row"):
            cells = {}
            maxcol = -1
            for c in row.findall(f"{NS_SS}c"):
                ref = c.get("r", "")
                if not ref:
                    continue
                ci = col_to_idx(ref)
                t = c.get("t")
                val = ""
                if t == "s":
                    v = c.find(f"{NS_SS}v")
                    if v is not None and v.text is not None:
                        idx = int(v.text)
                        val = shared[idx] if 0 <= idx < len(shared) else ""
                elif t == "inlineStr":
                    isn = c.find(f"{NS_SS}is")
                    if isn is not None:
                        val = "".join(tt.text or "" for tt in isn.iter(f"{NS_SS}t"))
                else:
                    v = c.find(f"{NS_SS}v")
                    if v is not None and v.text is not None:
                        val = v.text
                val = re.sub(r"\s+", " ", val).strip()
                if val:
                    cells[ci] = val
                    maxcol = max(maxcol, ci)
            if cells:
                rowvals = [cells.get(i, "") for i in range(maxcol + 1)]
                lines.append(" | ".join(rowvals))
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    words = len(text.split())
    log.append(f"xlsx OK · {len(sheets)} sheets · {len(shared)} shared strings · {words:,} words -> `{out.name}`")
    return words


def extract_pptx(src: Path, out: Path, log: list) -> int:
    z = zipfile.ZipFile(src)
    slides = sorted(
        [n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)],
        key=lambda n: int(re.search(r"(\d+)", n).group(1)),
    )
    media = [n for n in z.namelist() if n.startswith("ppt/media/")]
    lines = ["# Opportunity Card template · The AI Edge (pptx extraction · text runs only · media ignored)\n"]
    for sn in slides:
        root = ET.fromstring(z.read(sn))
        runs = []
        for t in root.iter(f"{NS_A}t"):
            txt = re.sub(r"\s+", " ", (t.text or "")).strip()
            if txt:
                runs.append(txt)
        idx = int(re.search(r"(\d+)", sn).group(1))
        lines.append(f"\n===== SLIDE {idx} =====")
        lines.extend(runs)
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    words = len(text.split())
    log.append(f"pptx OK · {len(slides)} slides · {len(media)} media files ignored · {words:,} words -> `{out.name}`")
    return words


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    log = ["# OPPORTUNITY_MANAGEMENT_TEMPLATES extraction log · 2026-05-19\n",
           "Method: stdlib zipfile + xml.etree.ElementTree · no new dependencies.\n"]

    failed = False
    w_xlsx = w_pptx = 0

    if not SRC_XLSX.exists():
        log.append(f"FAIL · xlsx not found: {SRC_XLSX}"); failed = True
    elif OUT_XLSX.exists():
        log.append(f"SKIP · {OUT_XLSX.name} exists · refusing overwrite")
        w_xlsx = len(OUT_XLSX.read_text(encoding='utf-8').split())
    else:
        try:
            w_xlsx = extract_xlsx(SRC_XLSX, OUT_XLSX, log)
        except Exception as e:
            log.append(f"FAIL · xlsx exception: {e}"); failed = True

    if not SRC_PPTX.exists():
        log.append(f"FAIL · pptx not found: {SRC_PPTX}"); failed = True
    elif OUT_PPTX.exists():
        log.append(f"SKIP · {OUT_PPTX.name} exists · refusing overwrite")
        w_pptx = len(OUT_PPTX.read_text(encoding='utf-8').split())
    else:
        try:
            w_pptx = extract_pptx(SRC_PPTX, OUT_PPTX, log)
        except Exception as e:
            log.append(f"FAIL · pptx exception: {e}"); failed = True

    log.append("\n## Summary")
    log.append(f"- Sources in: 2 (1 xlsx + 1 pptx)")
    log.append(f"- Extracted OK: {(0 if failed else 2)}")
    log.append(f"- xlsx words: {w_xlsx:,}")
    log.append(f"- pptx words: {w_pptx:,}")
    log.append(f"- xlsx output: `{OUT_XLSX.relative_to(ROOT)}`")
    log.append(f"- pptx output: `{OUT_PPTX.relative_to(ROOT)}`")

    if failed or w_xlsx < MIN_WORDS or w_pptx < MIN_WORDS:
        log.append("\nFAIL · halt. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL · extraction")
        return 1

    log.append("\nDone.")
    LOG_PATH.write_text("\n".join(log), encoding="utf-8")
    print(f"Extraction complete · xlsx {w_xlsx:,} words · pptx {w_pptx:,} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
