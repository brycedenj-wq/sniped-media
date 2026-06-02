#!/usr/bin/env python3
"""
LITERARY_CANON_GENERAL extraction · Joyce · Vonnegut · Nabokov · Hosseini · Allen · Gibran

Source lane: raw/02_TIER_1_CANON_BOOKS/literary_canon_general/
Output: 01_KNOWLEDGE_BASE/batches/literary_canon_general_extracted/<normalized>.txt
Log: 00_COMMAND_CENTER/batch_logs/LITERARY_CANON_GENERAL_EXTRACTION_LOG.md

Method:
  - Ulysses (.epub): stdlib zipfile + HTML-strip (spine-ordered)
  - Slaughterhouse-Five / Lolita / As a Man Thinketh (.pdf): pdftotext -layout
  - The Kite Runner (.mobi): ebook-convert (temp txt) · 30k-word floor
  - The Prophet (.lit): ebook-convert (temp txt) · CONDITIONAL (include only if clean text >= 3000 words)
DEFERRED (NOT extracted): Maus I (.cbr · images) + Jonathan Livingston Seagull (.djvu · no djvutxt).
No OCR. No new dependencies. In-copyright · extracted text is INTERNAL chunk-authoring reference only.
"""

import html
import re
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
LANE = ROOT / "raw" / "02_TIER_1_CANON_BOOKS" / "literary_canon_general"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "literary_canon_general_extracted"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "LITERARY_CANON_GENERAL_EXTRACTION_LOG.md"
EBOOK_CONVERT = "/opt/homebrew/bin/ebook-convert"
PDFTOTEXT = "/opt/homebrew/bin/pdftotext"

EPUB = ("James Joyce - Ulysses (2000, Penguin Group) - libgen.li.epub", "ulysses_joyce.txt")
PDFS = [
    ("Kurt Vonnegut - Slaughterhouse-Five - libgen.li.pdf", "slaughterhouse_five_vonnegut.txt", 20000),
    ("Nabokov, Vladimir - Lolita (Vladimir Nabokov) - libgen.li.pdf", "lolita_nabokov.txt", 40000),
    ("JAMES_ALLEN-AS_A_MAN_THINKETH.pdf", "as_a_man_thinketh_allen.txt", 4000),
]
MOBI = ("Khaled Hosseini - The Kite Runner (2004, Riverhead Trade) - libgen.li.mobi", "the_kite_runner_hosseini.txt", 30000)
LIT = ("Kahlil Gibran - The Prophet (1973) - libgen.li.lit", "the_prophet_gibran.txt", 3000)
DEFERRED = [
    "Maus I.cbr (Art Spiegelman · RAR of comic images · no text layer · no OCR per rules · DEFERRED)",
    "Richard Bach - Jonathan Livingston Seagull ... .djvu (no djvutxt · calibre cannot read djvu · DEFERRED)",
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
                match = next((n for n in htmls if n.endswith(href)), None)
                if match and match not in ordered:
                    ordered.append(match)
        for n in sorted(htmls):
            if n not in ordered:
                ordered.append(n)
        return ordered or sorted(htmls)
    except Exception:
        return sorted(htmls)


def w(out):
    return len(out.read_text(encoding="utf-8", errors="ignore").split())


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    log = ["# LITERARY_CANON_GENERAL extraction log · 2026-05-21\n",
           "Method: stdlib zipfile+HTML-strip (epub) · pdftotext -layout (pdf) · ebook-convert (mobi + .lit) · no OCR · no new dependencies.\n",
           "In-copyright · extracted text is INTERNAL chunk-authoring reference only.\n"]
    results = {}
    failed = False
    notes = []

    log.append("## Included sources\n")
    # Ulysses epub
    src = LANE / EPUB[0]; out = DEST / EPUB[1]
    if not src.exists():
        log.append(f"FAIL · not found: {EPUB[0][:50]}"); failed = True
    else:
        z = zipfile.ZipFile(src)
        text = ("\n\n".join(p for p in (strip_html(z.read(n)) for n in reading_order(z)) if p)).strip() + "\n"
        out.write_text(text, encoding="utf-8"); results[EPUB[1]] = w(out)
        log.append(f"OK · epub · Ulysses -> {EPUB[1]} · {results[EPUB[1]]:,} words")

    # PDFs
    for fname, outname, floor in PDFS:
        src = LANE / fname; out = DEST / outname
        if not src.exists():
            log.append(f"FAIL · not found: {fname[:50]}"); failed = True; continue
        r = subprocess.run([PDFTOTEXT, "-layout", str(src), str(out)], capture_output=True, text=True, timeout=180)
        if r.returncode != 0:
            log.append(f"FAIL · pdf · {fname[:40]} rc {r.returncode}"); failed = True; continue
        out.write_text(NL_RE.sub("\n\n", out.read_text(encoding="utf-8", errors="ignore")).strip() + "\n", encoding="utf-8")
        results[outname] = w(out)
        flag = "" if results[outname] >= floor else f"  WARNING below floor {floor}"
        log.append(f"OK · pdf · {fname[:40]} -> {outname} · {results[outname]:,} words{flag}")
        if results[outname] < floor:
            failed = True

    # Kite Runner mobi (30k floor)
    src = LANE / MOBI[0]; out = DEST / MOBI[1]
    if not src.exists():
        log.append(f"FAIL · not found: {MOBI[0][:50]}"); failed = True
    else:
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / "o.txt"
            r = subprocess.run([EBOOK_CONVERT, str(src), str(tmp)], capture_output=True, text=True, timeout=300)
            if r.returncode == 0 and tmp.exists():
                out.write_text(NL_RE.sub("\n\n", tmp.read_text(encoding="utf-8", errors="ignore")).strip() + "\n", encoding="utf-8")
                results[MOBI[1]] = w(out)
                if results[MOBI[1]] >= MOBI[2]:
                    log.append(f"OK · mobi · The Kite Runner -> {MOBI[1]} · {results[MOBI[1]]:,} words · 30k floor PASS")
                else:
                    log.append(f"FAIL · mobi · The Kite Runner -> {results[MOBI[1]]:,} words < 30k floor"); failed = True
            else:
                log.append(f"FAIL · mobi · ebook-convert rc {r.returncode}"); failed = True

    # The Prophet .lit (CONDITIONAL)
    src = LANE / LIT[0]; out = DEST / LIT[1]
    log.append("\n## Conditional source\n")
    if not src.exists():
        log.append(f"DEFER · The Prophet .lit not found"); notes.append("Gibran .lit: not found · deferred")
    else:
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / "o.txt"
            r = subprocess.run([EBOOK_CONVERT, str(src), str(tmp)], capture_output=True, text=True, timeout=300)
            if r.returncode == 0 and tmp.exists():
                cand = NL_RE.sub("\n\n", tmp.read_text(encoding="utf-8", errors="ignore")).strip() + "\n"
                cw = len(cand.split())
                if cw >= LIT[2]:
                    out.write_text(cand, encoding="utf-8"); results[LIT[1]] = cw
                    log.append(f"OK · lit · The Prophet -> {LIT[1]} · {cw:,} words · CONDITIONAL INCLUDE (>= {LIT[2]})")
                    notes.append(f"Gibran .lit: ebook-convert SUCCEEDED · {cw:,} words · INCLUDED")
                else:
                    log.append(f"DEFER · lit · The Prophet converted to only {cw} words (< {LIT[2]}) · NOT included")
                    notes.append(f"Gibran .lit: conversion yielded only {cw} words · DEFERRED")
            else:
                log.append(f"DEFER · lit · ebook-convert rc {r.returncode}: {r.stderr.strip()[:150]} · NOT included")
                notes.append(f"Gibran .lit: ebook-convert FAILED (rc {r.returncode}) · DEFERRED")

    log.append("\n## Deferred (NOT extracted · 0 chunks)\n")
    for d in DEFERRED:
        log.append(f"- {d}")
    log.append("\n## Absent / held (NOT in lane · 0 chunks)\n- Maus II (broken/zero-byte download · not staged)\n- Russian-author mobi ([Part 1 ] Шерман, Алекси · uncertain provenance · held)")

    log.append("\n## Summary")
    log.append(f"- Included sources extracted OK: {len(results)}")
    for k, v in results.items():
        log.append(f"  - {k}: {v:,} words")
    log.append(f"- Total words: {sum(results.values()):,}")
    for n in notes:
        log.append(f"- {n}")

    if failed:
        log.append("\nFAIL · an included source failed or missed its floor. Halt. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL · extraction"); return 1

    log.append("\nDone.")
    LOG_PATH.write_text("\n".join(log), encoding="utf-8")
    print(f"Extraction complete · {len(results)} included sources · {sum(results.values()):,} words")
    print("Gibran:", notes[-1] if notes else "n/a")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
