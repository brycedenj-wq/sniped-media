#!/usr/bin/env python3
"""
CULTURE_AND_STATUS extraction · status / culture / symbolic-value theory (2 CORE books).
Per 00_COMMAND_CENTER/CULTURE_AND_STATUS_PLAN.md.

Both are epub · stdlib zipfile + HTML-strip (spine-ordered). No OCR. No new dependencies.
The two held Status-pair books deferred from BATCH_009/BATCH_010. In-copyright trade books ·
extracted text is INTERNAL chunk-authoring reference only.
"""

import html
import re
import zipfile
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
LANE = ROOT / "raw" / "03_TIER_2_CANON_BOOKS" / "persuasion_psych"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "culture_and_status_extracted"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "CULTURE_AND_STATUS_EXTRACTION_LOG.md"

BOOK_FLOOR = 40000  # full-length theory book; below means broken extraction

# (keyword, outname)
CORE = [
    ("The Status Game", "the_status_game_storr.txt"),
    ("Status and Culture", "status_and_culture_marx.txt"),
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


def find_in(folder: Path, keyword: str):
    matches = [p for p in sorted(folder.iterdir()) if keyword.lower() in p.name.lower()]
    return matches[0] if matches else None


def wc(out: Path) -> int:
    return len(out.read_text(encoding="utf-8", errors="ignore").split())


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    log = ["# CULTURE_AND_STATUS extraction log · 2026-05-22\n",
           "Status / culture / symbolic-value theory · 2 CORE books (per CULTURE_AND_STATUS_PLAN.md).\n",
           "Method: stdlib zipfile + HTML-strip (epub, spine-ordered) · no OCR · no new dependencies.\n",
           "In-copyright trade books · extracted text is INTERNAL chunk-authoring reference only.\n"]
    results = {}
    failed = False

    log.append("## Included CORE sources (2)\n")
    for kw, outname in CORE:
        src = find_in(LANE, kw)
        out = DEST / outname
        if src is None:
            log.append(f"FAIL · not found (keyword '{kw}')"); failed = True; continue
        try:
            z = zipfile.ZipFile(src)
            text = ("\n\n".join(p for p in (strip_html(z.read(n)) for n in reading_order(z)) if p)).strip() + "\n"
            out.write_text(text, encoding="utf-8")
        except Exception as e:
            log.append(f"FAIL · epub · {kw}: {str(e)[:120]}"); failed = True; continue
        results[outname] = wc(out)
        flag = "" if results[outname] >= BOOK_FLOOR else f"  WARNING below floor {BOOK_FLOOR}"
        log.append(f"OK · epub · {kw} -> {outname} · {results[outname]:,} words{flag}")
        if results[outname] < BOOK_FLOOR:
            failed = True

    log.append("\n## Out of scope (NOT extracted · 0 chunks)\n"
               "- recovery/acquisition items + BATCH_009 EXPANSION set + memoirs_biographies/ + any other culture/status source")

    log.append("\n## Summary")
    log.append(f"- Included sources extracted OK: {len(results)} of 2 CORE")
    for k, v in results.items():
        log.append(f"  - {k}: {v:,} words")
    log.append(f"- Total words: {sum(results.values()):,}")

    if failed:
        log.append("\nFAIL · a CORE source failed or missed its floor. Halt. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL · extraction · see log"); return 1

    log.append("\nDone.")
    LOG_PATH.write_text("\n".join(log), encoding="utf-8")
    print(f"Extraction complete · {len(results)} of 2 CORE sources · {sum(results.values()):,} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
