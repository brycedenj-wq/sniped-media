#!/usr/bin/env python3
"""
LITERARY_CANON_BLACK extraction · Black literary canon (Morrison · Hurston · Walker)

Source lane: raw/02_TIER_1_CANON_BOOKS/literary_canon_black/
Output: 01_KNOWLEDGE_BASE/batches/literary_canon_black_extracted/<normalized>.txt
Log: 00_COMMAND_CENTER/batch_logs/LITERARY_CANON_BLACK_EXTRACTION_LOG.md

Method:
  - epub-family (the .epub and the .zip-that-is-an-epub): stdlib zipfile + HTML-strip
    (handles the .zip extension cleanly · no rename of raw/ · no new deps).
  - .mobi: ebook-convert (calibre · on PATH) to a temp txt, read back, then remove the temp.
Beloved .pdf is a publisher-blurb / SEO-spam STUB · DEFERRED · NOT extracted (operator decision).
No OCR. No new dependencies. Extracted text is INTERNAL chunk-authoring reference only.
"""

import html
import re
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
LANE = ROOT / "raw" / "02_TIER_1_CANON_BOOKS" / "literary_canon_black"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "literary_canon_black_extracted"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "LITERARY_CANON_BLACK_EXTRACTION_LOG.md"
EBOOK_CONVERT = "/opt/homebrew/bin/ebook-convert"
MIN_WORDS = 5000  # full novels · a tiny result would mean a stub like Beloved

# epub-family sources (zip containers) -> normalized output
EPUB_SOURCES = {
    "Zora Neale Hurston - Their Eyes Were Watching God (2009, HarperCollins e-books) - libgen.li.zip":
        "their_eyes_hurston.txt",
    "[The Color Purple 1 - The Color Purple 1] The Color Purple Collection_ The Color Purple, The Temple of My Familiar, and Possessing the Secr...{Walker, Alice}(2012, Open Road){112044773} libgen.li.epub":
        "color_purple_collection_walker.txt",
}
# mobi source -> normalized output
MOBI_SOURCES = {
    "Toni Morrison - The Bluest Eye (2007, Knopf Doubleday Publishing Group) - libgen.li.mobi":
        "bluest_eye_morrison.txt",
}
# deferred · not extracted
DEFERRED = ["[Beloved Trilogy 1 - Beloved Trilogy 1] Beloved{Toni Morrison}(1987){112430403} libgen.li.pdf (publisher-blurb / SEO-spam STUB · not the novel · re-acquire later)"]

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
    s = NL_RE.sub("\n\n", s)
    return s.strip()


def reading_order(z: zipfile.ZipFile):
    """Best-effort spine order via the OPF; fall back to sorted html names."""
    names = z.namelist()
    opf = next((n for n in names if n.lower().endswith(".opf")), None)
    htmls = [n for n in names if n.lower().endswith((".html", ".xhtml", ".htm"))]
    if not opf:
        return sorted(htmls)
    try:
        opf_txt = z.read(opf).decode("utf-8", "ignore")
        ids = dict(re.findall(r'<item\s+[^>]*id="([^"]+)"[^>]*href="([^"]+)"', opf_txt))
        ids2 = dict(re.findall(r'<item\s+[^>]*href="([^"]+)"[^>]*id="([^"]+)"', opf_txt))
        for k, v in ids2.items():
            ids.setdefault(v, k)
        spine = re.findall(r'<itemref\s+[^>]*idref="([^"]+)"', opf_txt)
        opf_dir = "/".join(opf.split("/")[:-1])
        ordered = []
        for idref in spine:
            href = ids.get(idref)
            if not href:
                continue
            cand = (opf_dir + "/" + href).lstrip("/") if opf_dir else href
            match = next((n for n in htmls if n.endswith(href) or n == cand), None)
            if match and match not in ordered:
                ordered.append(match)
        # append any html not in spine
        for n in sorted(htmls):
            if n not in ordered:
                ordered.append(n)
        return ordered or sorted(htmls)
    except Exception:
        return sorted(htmls)


def extract_epub(src: Path, out: Path, log: list) -> int:
    z = zipfile.ZipFile(src)
    parts = []
    for n in reading_order(z):
        txt = strip_html(z.read(n))
        if txt.strip():
            parts.append(txt)
    text = ("\n\n".join(parts)).strip() + "\n"
    out.write_text(text, encoding="utf-8")
    w = len(text.split())
    log.append(f"OK · epub · {src.name[:54]}... -> {out.name} · {w:,} words")
    return w


def extract_mobi(src: Path, out: Path, log: list) -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "out.txt"
        r = subprocess.run([EBOOK_CONVERT, str(src), str(tmp)],
                           capture_output=True, text=True, timeout=300)
        if r.returncode != 0 or not tmp.exists():
            log.append(f"FAIL · mobi · ebook-convert rc {r.returncode}: {r.stderr.strip()[:200]}")
            return -1
        text = tmp.read_text(encoding="utf-8", errors="ignore")
    text = NL_RE.sub("\n\n", text).strip() + "\n"
    out.write_text(text, encoding="utf-8")
    w = len(text.split())
    log.append(f"OK · mobi · {src.name[:54]}... -> {out.name} · {w:,} words")
    return w


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    log = ["# LITERARY_CANON_BLACK extraction log · 2026-05-20\n",
           "Method: stdlib zipfile + HTML-strip (epub-family) · ebook-convert (mobi) · no OCR · no new dependencies.\n",
           "In-copyright novels · extracted text is INTERNAL chunk-authoring reference only.\n"]
    total = 0
    failed = False
    too_small = []

    log.append("## Usable sources\n")
    for fname, outname in EPUB_SOURCES.items():
        src = LANE / fname
        out = DEST / outname
        if not src.exists():
            log.append(f"FAIL · not found: {fname[:60]}"); failed = True; continue
        if out.exists():
            log.append(f"SKIP · {outname} exists"); total += len(out.read_text(encoding='utf-8').split()); continue
        try:
            w = extract_epub(src, out, log)
        except Exception as e:
            log.append(f"FAIL · epub · {e}"); failed = True; continue
        total += w
        if w < MIN_WORDS:
            too_small.append(f"{outname} ({w} words)")

    for fname, outname in MOBI_SOURCES.items():
        src = LANE / fname
        out = DEST / outname
        if not src.exists():
            log.append(f"FAIL · not found: {fname[:60]}"); failed = True; continue
        if out.exists():
            log.append(f"SKIP · {outname} exists"); total += len(out.read_text(encoding='utf-8').split()); continue
        w = extract_mobi(src, out, log)
        if w < 0:
            failed = True; continue
        total += w
        if w < MIN_WORDS:
            too_small.append(f"{outname} ({w} words)")

    log.append("\n## Deferred (NOT extracted · 0 chunks)\n")
    for d in DEFERRED:
        log.append(f"- {d}")
    log.append("\n## Not in lane (excluded)\n- To Kill a Mockingbird (Lee) · not staged in literary_canon_black/ · out of scope for this mini-batch")

    log.append("\n## Summary")
    log.append(f"- Usable sources in: {len(EPUB_SOURCES) + len(MOBI_SOURCES)}")
    log.append(f"- Extracted OK: {sum(1 for o in list(EPUB_SOURCES.values())+list(MOBI_SOURCES.values()) if (DEST/o).exists())}")
    log.append(f"- Deferred (Beloved stub): 1")
    log.append(f"- Total words: {total:,}")
    if too_small:
        log.append(f"- WARNING · below {MIN_WORDS}-word floor: {', '.join(too_small)}")

    if failed or too_small:
        log.append("\nFAIL · extraction issue. Halt. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL · extraction", "· too_small=" + str(too_small) if too_small else "")
        return 1

    log.append("\nDone.")
    LOG_PATH.write_text("\n".join(log), encoding="utf-8")
    print(f"Extraction complete · {sum(1 for o in list(EPUB_SOURCES.values())+list(MOBI_SOURCES.values()) if (DEST/o).exists())}/3 usable · {total:,} words · Beloved deferred")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
