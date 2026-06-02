#!/usr/bin/env python3
"""
BATCH_010 extraction · lineage + Black culture canon (CORE 7 books).
Per 00_COMMAND_CENTER/BATCH_010_PLAN.md §5.1.

All 7 are epub · stdlib zipfile + HTML-strip (spine-ordered). No OCR. No new dependencies.
HELD / EXCLUDED (NOT extracted · 0 chunks): Status pair (Status Game, Status and Culture),
memoirs_biographies/ folder, The Tanning of America + The Song Machine (already chunked in BATCH_002),
recovery/acquisition items, BATCH_009 EXPANSION set. In-copyright trade books · extracted text is
INTERNAL chunk-authoring reference only.
"""

import html
import re
import zipfile
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
LANE = ROOT / "raw" / "02_TIER_1_CANON_BOOKS" / "culture"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "batch_010_extracted"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "BATCH_010_EXTRACTION_LOG.md"

BOOK_FLOOR = 25000   # full-length trade book; below means broken extraction
LIGHT_FLOOR = 8000   # Supreme Models is image-heavy (~32k words of profiles/captions)

# (keyword, outname, floor)
CORE = [
    ("Big Payback", "the_big_payback_charnas.txt", BOOK_FLOOR),
    ("Dilla Time", "dilla_time_charnas.txt", BOOK_FLOOR),
    ("Decoded", "decoded_jayz.txt", BOOK_FLOOR),
    ("Gucci Mane", "autobiography_of_gucci_mane.txt", BOOK_FLOOR),
    ("Hurricanes", "hurricanes_rick_ross.txt", BOOK_FLOOR),
    ("Empire State of Mind", "empire_state_of_mind_greenburg.txt", BOOK_FLOOR),
    ("Supreme Models", "supreme_models_reynolds.txt", LIGHT_FLOOR),
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
    log = ["# BATCH_010 extraction log · 2026-05-22\n",
           "Lineage + Black culture canon · CORE 7 books (per BATCH_010_PLAN.md §5.1).\n",
           "Method: stdlib zipfile + HTML-strip (epub, spine-ordered) · no OCR · no new dependencies.\n",
           "In-copyright trade books · extracted text is INTERNAL chunk-authoring reference only.\n"]
    results = {}
    failed = False

    log.append("## Included CORE sources (7)\n")
    for kw, outname, floor in CORE:
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
        flag = "" if results[outname] >= floor else f"  WARNING below floor {floor}"
        light = " · LIGHT (image-heavy)" if kw == "Supreme Models" else ""
        log.append(f"OK · epub · {kw} -> {outname} · {results[outname]:,} words{flag}{light}")
        if results[outname] < floor:
            failed = True

    log.append("\n## Held / excluded (NOT extracted · 0 chunks)\n"
               "- Status pair (The Status Game, Status and Culture) · HELD for a future CULTURE_AND_STATUS lane\n"
               "- memoirs_biographies/ folder (~16 founder/media biographies) · HELD for a separate future lane\n"
               "- The Tanning of America (Stoute) + The Song Machine · already chunked in BATCH_002\n"
               "- recovery/acquisition items + BATCH_009 EXPANSION set · out of scope")

    log.append("\n## Summary")
    log.append(f"- Included sources extracted OK: {len(results)} of 7 CORE")
    for k, v in results.items():
        log.append(f"  - {k}: {v:,} words")
    log.append(f"- Total words: {sum(results.values()):,}")

    if failed:
        log.append("\nFAIL · a CORE source failed or missed its floor. Halt. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL · extraction · see log"); return 1

    log.append("\nDone.")
    LOG_PATH.write_text("\n".join(log), encoding="utf-8")
    print(f"Extraction complete · {len(results)} of 7 CORE sources · {sum(results.values()):,} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
