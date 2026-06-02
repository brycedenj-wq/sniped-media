#!/usr/bin/env python3
"""
LITERARY_CANON_DYSTOPIAN extraction · Orwell · Atwood · Huxley

Source lane: raw/02_TIER_1_CANON_BOOKS/literary_canon_dystopian/
Output: 01_KNOWLEDGE_BASE/batches/literary_canon_dystopian_extracted/<normalized>.txt
Log: 00_COMMAND_CENTER/batch_logs/LITERARY_CANON_DYSTOPIAN_EXTRACTION_LOG.md

Method:
  - Animal Farm (.epub): stdlib zipfile + HTML-strip (spine-ordered)
  - The Handmaid's Tale (.mobi): ebook-convert (calibre · temp txt · read · remove) · 30k-word floor
  - Brave New World Revisited (.pdf): pdftotext -layout
No OCR. No new dependencies. Brave New World Revisited is Huxley's 1958 NONFICTION essays (not the novel).
The 2 study guides are absent from the lane (skipped). In-copyright · extracted text is INTERNAL reference only.
"""

import html
import re
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
LANE = ROOT / "raw" / "02_TIER_1_CANON_BOOKS" / "literary_canon_dystopian"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "literary_canon_dystopian_extracted"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "LITERARY_CANON_DYSTOPIAN_EXTRACTION_LOG.md"
EBOOK_CONVERT = "/opt/homebrew/bin/ebook-convert"
PDFTOTEXT = "/opt/homebrew/bin/pdftotext"

EPUB = "[Animal Farm _1] Orwell, George - Animal Farm (1945, Secker & Warburg) - libgen.li.epub"
MOBI = "[The Handmaid's Tale 1 ] Atwood, Margaret - The Handmaid's Tale (2006_2017, Everyman's Library_Anchor Books) - libgen.li.mobi"
PDF = "Aldous Huxley - Brave New World Revisited (2001) - libgen.li.pdf"

OUT_EPUB = "animal_farm_orwell.txt"
OUT_MOBI = "handmaids_tale_atwood.txt"
OUT_PDF = "brave_new_world_revisited_huxley.txt"

HT_FLOOR = 30000   # Handmaid's Tale full-novel floor (per plan section 3)
GEN_FLOOR = 25000  # general floor (Animal Farm novella ~30k · BNW Revisited ~34k)

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
            if not href:
                continue
            match = next((n for n in htmls if n.endswith(href)), None)
            if match and match not in ordered:
                ordered.append(match)
        for n in sorted(htmls):
            if n not in ordered:
                ordered.append(n)
        return ordered or sorted(htmls)
    except Exception:
        return sorted(htmls)


def extract_epub(src, out, log):
    z = zipfile.ZipFile(src)
    parts = [strip_html(z.read(n)) for n in reading_order(z) if z.read(n).strip()]
    text = ("\n\n".join(p for p in parts if p)).strip() + "\n"
    out.write_text(text, encoding="utf-8")
    w = len(text.split())
    log.append(f"OK · epub · Animal Farm -> {out.name} · {w:,} words")
    return w


def extract_mobi(src, out, log):
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "out.txt"
        r = subprocess.run([EBOOK_CONVERT, str(src), str(tmp)], capture_output=True, text=True, timeout=300)
        if r.returncode != 0 or not tmp.exists():
            log.append(f"FAIL · mobi · ebook-convert rc {r.returncode}: {r.stderr.strip()[:200]}")
            return -1
        text = tmp.read_text(encoding="utf-8", errors="ignore")
    text = NL_RE.sub("\n\n", text).strip() + "\n"
    out.write_text(text, encoding="utf-8")
    w = len(text.split())
    log.append(f"OK · mobi · The Handmaid's Tale -> {out.name} · {w:,} words")
    return w


def extract_pdf(src, out, log):
    r = subprocess.run([PDFTOTEXT, "-layout", str(src), str(out)], capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        log.append(f"FAIL · pdf · pdftotext rc {r.returncode}: {r.stderr.strip()[:200]}")
        return -1
    text = NL_RE.sub("\n\n", out.read_text(encoding="utf-8", errors="ignore")).strip() + "\n"
    out.write_text(text, encoding="utf-8")
    w = len(text.split())
    log.append(f"OK · pdf · Brave New World Revisited (NONFICTION essays · not the novel) -> {out.name} · {w:,} words")
    return w


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    log = ["# LITERARY_CANON_DYSTOPIAN extraction log · 2026-05-21\n",
           "Method: stdlib zipfile+HTML-strip (epub) · ebook-convert (mobi) · pdftotext -layout (pdf) · no OCR · no new dependencies.\n",
           "Brave New World Revisited = Huxley 1958 NONFICTION essays (not the novel). In-copyright · extracted text is INTERNAL reference only.\n"]
    results = {}
    failed = False
    floor_fail = []

    log.append("## Usable sources\n")
    # Animal Farm
    src = LANE / EPUB
    if not src.exists():
        log.append(f"FAIL · not found: {EPUB[:50]}"); failed = True
    else:
        try:
            w = extract_epub(src, DEST / OUT_EPUB, log); results[OUT_EPUB] = w
            if w < GEN_FLOOR: floor_fail.append(f"{OUT_EPUB} ({w} < {GEN_FLOOR})")
        except Exception as e:
            log.append(f"FAIL · epub · {e}"); failed = True
    # Handmaid's Tale (30k floor)
    src = LANE / MOBI
    if not src.exists():
        log.append(f"FAIL · not found: {MOBI[:50]}"); failed = True
    else:
        w = extract_mobi(src, DEST / OUT_MOBI, log)
        if w < 0: failed = True
        else:
            results[OUT_MOBI] = w
            if w < HT_FLOOR: floor_fail.append(f"{OUT_MOBI} ({w} < {HT_FLOOR} HT floor)")
            else: log.append(f"   Handmaid's Tale 30k-word floor: PASS ({w:,} >= {HT_FLOOR})")
    # BNW Revisited
    src = LANE / PDF
    if not src.exists():
        log.append(f"FAIL · not found: {PDF[:50]}"); failed = True
    else:
        w = extract_pdf(src, DEST / OUT_PDF, log)
        if w < 0: failed = True
        else:
            results[OUT_PDF] = w
            if w < GEN_FLOOR: floor_fail.append(f"{OUT_PDF} ({w} < {GEN_FLOOR})")

    log.append("\n## Study guides (absent · skipped)\n- 1984 SparkNotes + Fahrenheit 451 Bloom's Critical Interpretations · NOT in lane · 0 chunks (orphaned secondaries · their primaries were not staged)")
    log.append("\n## Summary")
    log.append(f"- Usable sources in: 3 · Extracted OK: {len(results)}")
    for k, v in results.items():
        log.append(f"  - {k}: {v:,} words")
    log.append(f"- Total words: {sum(results.values()):,}")

    if failed or floor_fail:
        log.append(f"\nFAIL · " + ("floor: " + ", ".join(floor_fail) if floor_fail else "extraction issue") + " · Halt. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL", floor_fail or "")
        return 1

    log.append("\nDone.")
    LOG_PATH.write_text("\n".join(log), encoding="utf-8")
    print(f"Extraction complete · {len(results)}/3 · {sum(results.values()):,} words · HT floor PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
