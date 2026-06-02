#!/usr/bin/env python3
"""
BATCH_009 extraction · advertising / copywriting / persuasion / positioning canon (CORE 18 books).
Per 00_COMMAND_CENTER/BATCH_009_PLAN.md §5.1.

Method: pdftotext -layout (pdf) · stdlib zipfile+HTML-strip (epub) · ebook-convert (mobi).
Sources are pinned to their exact folders (Made to Stick -> sales_positioning copy, not the raw/ root dup).
EXCLUDED / DEFERRED (NOT extracted · 0 chunks): EXPANSION (Never Split, Eating the Big Fish, Play Bigger,
Tribes, Competing Against Luck), Status pair (Status Game, Status and Culture), Confessions (scanned/OCR),
Predictably Irrational (.djvu), Truth-Lies-and-Advertising (review stub), document.pdf (This Is Marketing dup),
Sugarman/Caples/Halbert (absent). No OCR. No new dependencies. In-copyright trade books · extracted text is
INTERNAL chunk-authoring reference only.
"""

import html
import re
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
ADV = ROOT / "raw" / "02_TIER_1_CANON_BOOKS" / "advertising"
SALES = ROOT / "raw" / "02_TIER_1_CANON_BOOKS" / "sales_positioning"
PSY = ROOT / "raw" / "03_TIER_2_CANON_BOOKS" / "persuasion_psych"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "batch_009_extracted"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "BATCH_009_EXTRACTION_LOG.md"
EBOOK_CONVERT = "/opt/homebrew/bin/ebook-convert"
PDFTOTEXT = "/opt/homebrew/bin/pdftotext"

BOOK_FLOOR = 8000  # full-length trade book; below this means broken extraction or a stub

# (folder, keyword, outname, kind, floor)
CORE = [
    # advertising / copywriting (5)
    (ADV, "Scientific Advertising", "scientific_advertising_hopkins.txt", "pdf", 5000),
    (ADV, "Cashvertising", "cashvertising_whitman.txt", "epub", BOOK_FLOOR),
    (ADV, "Whipple", "hey_whipple_squeeze_this_sullivan.txt", "pdf", BOOK_FLOOR),
    (ADV, "Breakthrough Advertising", "breakthrough_advertising_schwartz.txt", "pdf", BOOK_FLOOR),
    (ADV, "copywriter", "copywriters_handbook_bly.txt", "mobi", BOOK_FLOOR),
    # persuasion / customer psychology (5)
    (PSY, "Influence (Harper", "influence_cialdini.txt", "pdf", BOOK_FLOOR),
    (PSY, "Pre-Suasion", "presuasion_cialdini.txt", "epub", BOOK_FLOOR),
    (PSY, "Contagious", "contagious_berger.txt", "mobi", BOOK_FLOOR),
    (PSY, "Choice Factory", "the_choice_factory_shotton.txt", "epub", BOOK_FLOOR),
    (PSY, "Alchemy", "alchemy_sutherland.txt", "epub", BOOK_FLOOR),
    # positioning / offers / memorability / market education (8)
    (SALES, "This Is Marketing", "this_is_marketing_godin.txt", "pdf", BOOK_FLOOR),
    (SALES, "Purple Cow", "purple_cow_godin.txt", "pdf", 5000),
    (SALES, "Differentiate or Die", "differentiate_or_die_trout.txt", "pdf", BOOK_FLOOR),
    (SALES, "Obviously Awesome", "obviously_awesome_dunford.txt", "epub", BOOK_FLOOR),
    (SALES, "100M Offers", "100m_offers_hormozi.txt", "epub", BOOK_FLOOR),
    (SALES, "100M Leads", "100m_leads_hormozi.txt", "epub", BOOK_FLOOR),
    (SALES, "Made to Stick", "made_to_stick_heath.txt", "pdf", BOOK_FLOOR),
    (SALES, "StoryBrand", "building_a_storybrand_miller.txt", "mobi", BOOK_FLOOR),
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


def extract_epub(src: Path, out: Path):
    z = zipfile.ZipFile(src)
    text = ("\n\n".join(p for p in (strip_html(z.read(n)) for n in reading_order(z)) if p)).strip() + "\n"
    out.write_text(text, encoding="utf-8")


def extract_pdf(src: Path, out: Path):
    r = subprocess.run([PDFTOTEXT, "-layout", str(src), str(out)], capture_output=True, text=True, timeout=300)
    if r.returncode != 0:
        raise RuntimeError(f"pdftotext rc {r.returncode}")
    out.write_text(NL_RE.sub("\n\n", out.read_text(encoding="utf-8", errors="ignore")).strip() + "\n", encoding="utf-8")


def extract_calibre(src: Path, out: Path):
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "o.txt"
        r = subprocess.run([EBOOK_CONVERT, str(src), str(tmp)], capture_output=True, text=True, timeout=420)
        if r.returncode != 0 or not tmp.exists():
            raise RuntimeError(f"ebook-convert rc {r.returncode}: {r.stderr.strip()[:120]}")
        out.write_text(NL_RE.sub("\n\n", tmp.read_text(encoding="utf-8", errors="ignore")).strip() + "\n", encoding="utf-8")


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    log = ["# BATCH_009 extraction log · 2026-05-22\n",
           "Advertising / copywriting / persuasion / positioning canon · CORE 18 books (per BATCH_009_PLAN.md §5.1).\n",
           "Method: pdftotext -layout (pdf) · stdlib zipfile+HTML-strip (epub) · ebook-convert (mobi) · no OCR · no new dependencies.\n",
           "In-copyright trade books · extracted text is INTERNAL chunk-authoring reference only.\n"]
    results = {}
    failed = False

    log.append("## Included CORE sources (18)\n")
    for folder, kw, outname, kind, floor in CORE:
        src = find_in(folder, kw)
        out = DEST / outname
        if src is None:
            log.append(f"FAIL · not found (keyword '{kw}' in {folder.name})"); failed = True; continue
        try:
            if kind == "epub":
                extract_epub(src, out)
            elif kind == "pdf":
                extract_pdf(src, out)
            else:  # mobi / azw3
                extract_calibre(src, out)
        except Exception as e:
            log.append(f"FAIL · {kind} · {kw}: {str(e)[:120]}"); failed = True; continue
        results[outname] = wc(out)
        flag = "" if results[outname] >= floor else f"  WARNING below floor {floor}"
        log.append(f"OK · {kind} · {kw} -> {outname} · {results[outname]:,} words{flag}")
        if results[outname] < floor:
            failed = True

    log.append("\n## Deferred (NOT extracted · 0 chunks)\n"
               "- Confessions of an Advertising Man (Ogilvy) · scanned image-only PDF · OCR-blocked · re-acquire text edition\n"
               "- Predictably Irrational (Ariely) · `.djvu` · no djvutxt · format-blocked\n"
               "- EXPANSION set (Never Split the Difference, Eating the Big Fish, Play Bigger, Tribes, Competing Against Luck) · operator-deferred\n"
               "- Status pair (The Status Game, Status and Culture) · routed to a future culture/status lane")
    log.append("\n## Excluded (NOT extracted · 0 chunks)\n"
               "- document.pdf · byte-identical duplicate of the named This Is Marketing · dedupe\n"
               "- Truth, Lies and Advertising · a 1,455-word journal book-review (not the Jon Steel book)")
    log.append("\n## Absent (re-acquisition flags · 0 chunks)\n"
               "- Sugarman (Adweek Copywriting Handbook), Caples (Tested Advertising Methods), Halbert (Boron Letters)")

    log.append("\n## Summary")
    log.append(f"- Included sources extracted OK: {len(results)} of 18 CORE")
    for k, v in results.items():
        log.append(f"  - {k}: {v:,} words")
    log.append(f"- Total words: {sum(results.values()):,}")

    if failed:
        log.append("\nFAIL · a CORE source failed or missed its floor. Halt. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL · extraction · see log"); return 1

    log.append("\nDone.")
    LOG_PATH.write_text("\n".join(log), encoding="utf-8")
    print(f"Extraction complete · {len(results)} of 18 CORE sources · {sum(results.values()):,} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
