#!/usr/bin/env python3
"""
BATCH_005 extraction · photography canon at depth
36 sources across 4 raw/ folders. Tom King The Operator EXCLUDED per operator decision.
8 mp4 photographer films DEFERRED to a future transcription batch.
Output: 01_KNOWLEDGE_BASE/batches/batch_005_extracted/
Log:    00_COMMAND_CENTER/batch_logs/BATCH_005_EXTRACTION_LOG.md

Extraction method per file type (per BATCH_005_PLAN.md §7):
  .md / .txt     → copy
  .docx          → pandoc -t plain
  .epub          → ebook-convert .epub .txt
  .mobi          → ebook-convert .mobi .txt
  .pdf           → pdftotext -layout (text-layer only; OCR-defer if word count < 500)

500-word sanity check: any extracted output under 500 words is flagged OCR-DEFERRED,
not written to the extracted/ folder. ocrmypdf is NOT installed in this environment
and the operator authorized text-layer extraction only.
"""

import shutil
import subprocess
import time
from pathlib import Path

RAW = Path.home() / "AI-Brain-Refinery" / "raw"
DEST = Path.home() / "AI-Brain-Refinery" / "01_KNOWLEDGE_BASE" / "batches" / "batch_005_extracted"
LOG_PATH = Path.home() / "AI-Brain-Refinery" / "00_COMMAND_CENTER" / "batch_logs" / "BATCH_005_EXTRACTION_LOG.md"

DEST.mkdir(parents=True, exist_ok=True)
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

PANDOC = "/opt/homebrew/bin/pandoc"
PDFTOTEXT = "/opt/homebrew/bin/pdftotext"
EBOOK_CONVERT = "/opt/homebrew/bin/ebook-convert"

MIN_WORDS = 500

# 36 approved sources from BATCH_005_PLAN.md §3.
# (src is relative to RAW. out is the normalized basename. tool dispatches the recipe.)
JOBS = [
    # ----- Pri 1 · canonical theory + craft (10) -----
    {"src": "02_TIER_1_CANON_BOOKS/photography/Sontag, Susan - On Photography (2012) - libgen.li.pdf",
     "out": "sontag_on_photography.txt", "tool": "pdf"},
    {"src": "02_TIER_1_CANON_BOOKS/photography/Roland Barthes - Camera Lucida_ Reflections on Photography (1982, Hill and Wang) - libgen.li.epub",
     "out": "barthes_camera_lucida.txt", "tool": "epub"},
    {"src": "02_TIER_1_CANON_BOOKS/photography/Jonathan Day - Robert Frank's 'The Americans' _ The Art of Documentary Photography (2011, Intellect Books) - libgen.li.epub",
     "out": "day_robert_franks_the_americans.txt", "tool": "epub"},
    {"src": "02_TIER_1_CANON_BOOKS/photography/Stephen Shore - The Nature Of Photographs (2007, Phaidon Press) - libgen.li.pdf",
     "out": "shore_nature_of_photographs.txt", "tool": "pdf"},
    {"src": "02_TIER_1_CANON_BOOKS/photography/John Szarkowski - William Eggleston's Guide (2002, The Museum of Modern Art, New York) - libgen.li.pdf",
     "out": "szarkowski_eggleston_guide.txt", "tool": "pdf"},
    {"src": "02_TIER_1_CANON_BOOKS/photography/Michael Freeman - The Photographer's Eye_ Composition and Design for Better Digital Photos (2007, Focal Press) - libgen.li.mobi",
     "out": "freeman_photographers_eye.txt", "tool": "mobi"},
    {"src": "02_TIER_1_CANON_BOOKS/photography/Michael Freeman - The Photographer's Vision_ Understanding and Appreciating Great Photography (2011, Elsevier Science_ Focal Press) - libgen.li.epub",
     "out": "freeman_photographers_vision.txt", "tool": "epub"},
    {"src": "02_TIER_1_CANON_BOOKS/photography/Norma Stevens, Steven M. L. Aronson - Avedon_ Something Personal (2017, Spiegel & Grau) - libgen.li.epub",
     "out": "stevens_avedon_something_personal.txt", "tool": "epub"},
    {"src": "02_TIER_1_CANON_BOOKS/photography/Annie Leibovitz - Annie Leibovitz at Work (2008, Random House) - libgen.li.epub",
     "out": "leibovitz_at_work.txt", "tool": "epub"},
    {"src": "02_TIER_1_CANON_BOOKS/photography/[Voices That Matter] Jay Maisel - Light, Gesture, and Color (2014, New Riders) - libgen.li.epub",
     "out": "maisel_light_gesture_color.txt", "tool": "epub"},

    # ----- Pri 2 · SNIPED Art Series doctrine (19) -----
    {"src": "09_ART_SERIES/Art_Series_1_RichardAvedon.md",      "out": "art_series_1_richard_avedon.md",      "tool": "copy"},
    {"src": "09_ART_SERIES/Art_Series_2_WilliamEggleston.md",   "out": "art_series_2_william_eggleston.md",   "tool": "copy"},
    {"src": "09_ART_SERIES/Art_Series_3_AnnieLeibovitz.md",     "out": "art_series_3_annie_leibovitz.md",     "tool": "copy"},
    {"src": "09_ART_SERIES/Art_Series_4_StephenShore.md",       "out": "art_series_4_stephen_shore.md",       "tool": "copy"},
    {"src": "09_ART_SERIES/Art_Series_5_FredHerzog.md",         "out": "art_series_5_fred_herzog.md",         "tool": "copy"},
    {"src": "09_ART_SERIES/Art_Series_6_RobertFrank.md",        "out": "art_series_6_robert_frank.md",        "tool": "copy"},
    {"src": "09_ART_SERIES/Art_Series_7_JoelMeyerowitz.md",     "out": "art_series_7_joel_meyerowitz.md",     "tool": "copy"},
    {"src": "09_ART_SERIES/Art_Series_8_GracielaIturbide.md",   "out": "art_series_8_graciela_iturbide.md",   "tool": "copy"},
    {"src": "09_ART_SERIES/Art_Series_9_ErnstHaas.md",          "out": "art_series_9_ernst_haas.md",          "tool": "copy"},
    {"src": "09_ART_SERIES/Study_AnnieLeibovitz.md",            "out": "study_annie_leibovitz.md",            "tool": "copy"},
    {"src": "09_ART_SERIES/Study_ErnstHaas.md",                 "out": "study_ernst_haas.md",                 "tool": "copy"},
    {"src": "09_ART_SERIES/Study_FredHerzog.md",                "out": "study_fred_herzog.md",                "tool": "copy"},
    {"src": "09_ART_SERIES/Study_GracielaIturbide.md",          "out": "study_graciela_iturbide.md",          "tool": "copy"},
    {"src": "09_ART_SERIES/Study_JoelMeyerowitz.md",            "out": "study_joel_meyerowitz.md",            "tool": "copy"},
    {"src": "09_ART_SERIES/Study_RichardAvedon.md",             "out": "study_richard_avedon.md",             "tool": "copy"},
    {"src": "09_ART_SERIES/Study_RobertFrank.md",               "out": "study_robert_frank.md",               "tool": "copy"},
    {"src": "09_ART_SERIES/Study_StephenShore.md",              "out": "study_stephen_shore.md",              "tool": "copy"},
    {"src": "09_ART_SERIES/Study_WilliamEggleston.md",          "out": "study_william_eggleston.md",          "tool": "copy"},
    {"src": "09_ART_SERIES/Art_Series.docx",                    "out": "art_series_wrapper.md",               "tool": "pandoc-docx"},

    # ----- Pri 3 · scanned theory + clean transcript (2) -----
    {"src": "10_REFERENCE/photography_scans/257683787-Cartier-Bresson-H-1952-the-Decisive-Moment.pdf",
     "out": "cartier_bresson_decisive_moment.txt", "tool": "pdf"},
    {"src": "10_REFERENCE/photography_scans/713434459-Core-Studio-Public-Lecture-Virgil-Abloh-Insert-Complicated-Title-Here-English.txt",
     "out": "abloh_core_studio_lecture.txt", "tool": "copy"},

    # ----- Pri 4 · GOLD vault text-dense (5) -----
    {"src": "PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /Ernst Haas in Black and White{Jim Hughes_ Alexander Haas_ Ernst Haas}(1992, Bulfinch Press){115446337} libgen.li.pdf",
     "out": "hughes_ernst_haas_black_and_white.txt", "tool": "pdf"},
    {"src": "PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /[Art Education 1989-jul vol. 42 iss. 4] Richard Avedon&_039_s in the American West and Jean-Paul Sartre_ An Existential Approach to Art and Value{Richard M. Dubiel}(1989 July)[10.2307_3193139]{34352628} libgen.li.pdf",
     "out": "dubiel_avedon_american_west_sartre.txt", "tool": "pdf"},
    {"src": "PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /[The American Review of Canadian Studies 2018-sep 24 vol. 48 iss. 4] Fred Herzog_ Modern Color{Talbot, Jacques P.}(2018 September 24)[10.1080_02722011.2018.1493784]{80941078} libgen.li.pdf",
     "out": "talbot_herzog_modern_color.txt", "tool": "pdf"},
    {"src": "PHOTOGRPAHY GOLD BOOKS VIDEOS EVERYTHING /[The Art Book 1994-mar vol. 1 iss. 2] THE AMERICANS{ROBERT FRANK}(1994 March)[10.1111_j.1467-8357.1994.tb00040.x]{16094637} libgen.li.pdf",
     "out": "art_book_1994_robert_frank_americans.txt", "tool": "pdf"},
    {"src": "10_REFERENCE/photography_scans/367490464-Szarkowski-1973-Looking-at-Photographs-pdf.pdf",
     "out": "szarkowski_looking_at_photographs.txt", "tool": "pdf"},
]


def run(cmd, timeout=120):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def extract_pdf(src, dst):
    r = run([PDFTOTEXT, "-layout", str(src), str(dst)])
    return r.returncode, r.stderr


def extract_epub_or_mobi(src, dst):
    r = run([EBOOK_CONVERT, str(src), str(dst)], timeout=300)
    return r.returncode, r.stderr


def extract_docx(src, dst):
    r = run([PANDOC, "-f", "docx", "-t", "plain", "--wrap=none", "-o", str(dst), str(src)])
    return r.returncode, r.stderr


def word_count(path):
    try:
        return len(Path(path).read_text(errors="ignore").split())
    except Exception:
        return 0


def main():
    log_lines = ["# BATCH_005 extraction log · " + time.strftime("%Y-%m-%d %H:%M"), ""]
    log_lines.append(f"Source root: `{RAW}`")
    log_lines.append(f"Destination: `{DEST}`")
    log_lines.append(f"Toolchain: pandoc, pdftotext, ebook-convert (calibre)")
    log_lines.append(f"OCR posture: text-layer only · ocrmypdf NOT installed · OCR-defer if < {MIN_WORDS} words")
    log_lines.append("")
    log_lines.append("| # | source | tool | status | extracted bytes | words | output |")
    log_lines.append("|--:|---|---|---|---:|---:|---|")

    ok = fail = ocr_deferred = missing = 0
    deferred = []

    for i, job in enumerate(JOBS, 1):
        src = RAW / job["src"]
        dst = DEST / job["out"]
        if not src.exists():
            log_lines.append(f"| {i} | `{job['src']}` | {job['tool']} | MISSING | - | - | - |")
            missing += 1
            continue

        if job["tool"] == "copy":
            shutil.copy2(src, dst)
            rc, err = 0, ""
        elif job["tool"] == "pandoc-docx":
            rc, err = extract_docx(src, dst)
        elif job["tool"] == "pdf":
            rc, err = extract_pdf(src, dst)
        elif job["tool"] in ("epub", "mobi"):
            rc, err = extract_epub_or_mobi(src, dst)
        else:
            log_lines.append(f"| {i} | `{job['src']}` | {job['tool']} | UNKNOWN_TOOL | - | - | - |")
            fail += 1
            continue

        if rc != 0 or not dst.exists():
            log_lines.append(f"| {i} | `{job['src']}` | {job['tool']} | FAILED | - | - | `{err[:80]}` |")
            fail += 1
            continue

        sz = dst.stat().st_size
        wc = word_count(dst)

        if wc < MIN_WORDS:
            # OCR-defer: remove from extracted/ so it doesn't get chunked
            log_lines.append(f"| {i} | `{job['src']}` | {job['tool']} | OCR-DEFERRED | {sz:,} | {wc:,} | (under {MIN_WORDS} words) |")
            deferred.append({"src": job["src"], "out": job["out"], "words": wc, "bytes": sz})
            try:
                dst.unlink()
            except OSError:
                pass
            ocr_deferred += 1
            continue

        log_lines.append(f"| {i} | `{job['src']}` | {job['tool']} | OK | {sz:,} | {wc:,} | `{job['out']}` |")
        ok += 1

    log_lines.append("")
    log_lines.append(f"**Totals:** {ok} ok · {ocr_deferred} OCR-deferred · {fail} failed · {missing} missing · {len(JOBS)} planned.")
    log_lines.append("")
    if deferred:
        log_lines.append("## OCR-deferred sources (excluded from BATCH_005)")
        log_lines.append("")
        for d in deferred:
            log_lines.append(f"- `{d['src']}` · {d['words']} words from {d['bytes']:,} bytes (under {MIN_WORDS}-word threshold)")
        log_lines.append("")
    LOG_PATH.write_text("\n".join(log_lines))
    print(f"OK     {ok}")
    print(f"OCR    {ocr_deferred}")
    print(f"FAIL   {fail}")
    print(f"MISS   {missing}")
    print(f"LOG    {LOG_PATH}")


if __name__ == "__main__":
    main()
