#!/usr/bin/env python3
"""
Extract the 7 CORE FOUNDER_SECOND_TIER sources from raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/
into 01_KNOWLEDGE_BASE/batches/founder_second_tier_extracted/.

3 epub via stdlib zipfile + spine-ordered HTML-strip · 1 pdf via pdftotext -layout · 3 mobi via
ebook-convert (calibre · already on PATH). Keyword-substring matching. No OCR. No new dependencies.
Does NOT modify raw/. Refuses to overwrite an existing extracted file.
"""

import os, re, subprocess, tempfile, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path.home() / "AI-Brain-Refinery"
SRC = ROOT / "raw" / "03_TIER_2_CANON_BOOKS" / "memoirs_biographies"
OUT = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "founder_second_tier_extracted"
OUT.mkdir(parents=True, exist_ok=True)

# (output_name, keyword, kind)
TARGETS = [
    ("sam_walton_made_in_america.txt", "Sam Walton", "pdf"),
    ("elon_musk_isaacson.txt", "Elon Musk", "epub"),
    ("super_pumped_uber_isaac.txt", "Super Pumped", "epub"),
    ("the_airbnb_story_gallagher.txt", "Airbnb Story", "epub"),
    ("titan_rockefeller_chernow.txt", "Titan_", "mobi"),
    ("the_fish_that_ate_the_whale_cohen.txt", "Fish That Ate the Whale", "mobi"),
    ("pour_your_heart_into_it_schultz.txt", "Pour Your Heart", "mobi"),
]


def find_one(keyword):
    matches = [p for p in SRC.iterdir() if p.is_file() and keyword in p.name]
    if len(matches) != 1:
        raise SystemExit(f"ABORT · expected 1 match for '{keyword}', got {len(matches)}: {[m.name for m in matches]}")
    return matches[0]


def strip_html(raw):
    raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
    raw = re.sub(r"(?i)</p>", "\n", raw)
    raw = re.sub(r"<[^>]+>", " ", raw)
    raw = (raw.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<")
              .replace("&gt;", ">").replace("&#39;", "'").replace("&rsquo;", "'")
              .replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&quot;", '"'))
    raw = re.sub(r"[ \t]+", " ", raw)
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    return raw.strip()


def reading_order(z):
    names = z.namelist()
    opf = next((n for n in names if n.lower().endswith(".opf")), None)
    htmls = [n for n in names if n.lower().endswith((".xhtml", ".html", ".htm"))]
    if not opf:
        return sorted(htmls)
    try:
        root = ET.fromstring(z.read(opf))
        manifest = {}
        for item in root.iter():
            if item.tag.endswith("}item") or item.tag == "item":
                iid, href = item.get("id"), item.get("href")
                if iid and href:
                    manifest[iid] = href
        base = os.path.dirname(opf)
        ordered = []
        for it in root.iter():
            if it.tag.endswith("}itemref") or it.tag == "itemref":
                idref = it.get("idref")
                if idref in manifest:
                    full = os.path.normpath(os.path.join(base, manifest[idref])).replace("\\", "/") if base else manifest[idref]
                    if full in names:
                        ordered.append(full)
        for h in htmls:
            if h not in ordered:
                ordered.append(h)
        return ordered or sorted(htmls)
    except Exception:
        return sorted(htmls)


def extract_epub(path):
    z = zipfile.ZipFile(path)
    parts = []
    for name in reading_order(z):
        try:
            txt = strip_html(z.read(name).decode("utf-8", "ignore"))
        except KeyError:
            continue
        if txt:
            parts.append(txt)
    return "\n\n".join(parts)


def extract_pdf(path):
    out = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit(f"ABORT · pdftotext failed for {path.name}: {out.stderr[:200]}")
    return out.stdout


def extract_mobi(path):
    with tempfile.TemporaryDirectory() as td:
        tmp_txt = Path(td) / "out.txt"
        r = subprocess.run(["ebook-convert", str(path), str(tmp_txt)], capture_output=True, text=True)
        if r.returncode != 0 or not tmp_txt.exists():
            raise SystemExit(f"ABORT · ebook-convert failed for {path.name}: {r.stderr[-300:]}")
        raw = tmp_txt.read_text(encoding="utf-8", errors="ignore")
    raw = re.sub(r"[ \t]+", " ", raw)
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    return raw.strip()


def main():
    summary = []
    for out_name, keyword, kind in TARGETS:
        dest = OUT / out_name
        if dest.exists():
            raise SystemExit(f"ABORT · refuse to overwrite existing {dest}")
        src = find_one(keyword)
        if kind == "epub":
            text = extract_epub(src)
        elif kind == "pdf":
            text = extract_pdf(src)
        else:
            text = extract_mobi(src)
        wc = len(text.split())
        dest.write_text(text, encoding="utf-8")
        summary.append((out_name, src.name.strip(), kind, wc))
        print(f"  {wc:>7} w  {kind:4}  -> {out_name}  (from {src.name.strip()[:44]})")
    print(f"\nDONE · {len(summary)} sources extracted into {OUT}")
    print(f"total words: {sum(s[3] for s in summary)}")


if __name__ == "__main__":
    main()
