#!/usr/bin/env python3
"""
Extract the 5 BATCH_009_EXPANSION sources from raw/02_TIER_1_CANON_BOOKS/sales_positioning/
into 01_KNOWLEDGE_BASE/batches/batch_009_expansion_extracted/.

4 epub via stdlib zipfile + spine-ordered HTML-strip · 1 pdf via pdftotext -layout.
Keyword-substring matching handles the leading-space filenames. No OCR. No new deps.
Does NOT modify raw/. Refuses to overwrite an existing extracted file.
"""

import os, re, subprocess, sys, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path.home() / "AI-Brain-Refinery"
SRC = ROOT / "raw" / "02_TIER_1_CANON_BOOKS" / "sales_positioning"
OUT = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "batch_009_expansion_extracted"
OUT.mkdir(parents=True, exist_ok=True)

# (output_name, keyword to match the raw filename, kind)
TARGETS = [
    ("never_split_the_difference_voss.txt", "Never Split the Difference", "epub"),
    ("eating_the_big_fish_morgan.txt", "Eating the Big Fish", "pdf"),
    ("play_bigger_ramadan_lochhead.txt", "Play Bigger", "epub"),
    ("tribes_godin.txt", "Tribes_ We Need You", "epub"),
    ("competing_against_luck_christensen.txt", "Competing Against Luck", "epub"),
]


def find_raw(keyword):
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
    """Return spine-ordered list of HTML doc names from the epub OPF; fall back to sorted names."""
    names = z.namelist()
    opf = next((n for n in names if n.lower().endswith(".opf")), None)
    htmls = [n for n in names if n.lower().endswith((".xhtml", ".html", ".htm"))]
    if not opf:
        return sorted(htmls)
    try:
        root = ET.fromstring(z.read(opf))
        ns = {"opf": "http://www.idpf.org/2007/opf"}
        manifest = {}
        for item in root.iter():
            if item.tag.endswith("}item") or item.tag == "item":
                iid = item.get("id"); href = item.get("href")
                if iid and href:
                    manifest[iid] = href
        base = os.path.dirname(opf)
        ordered = []
        for it in root.iter():
            if it.tag.endswith("}itemref") or it.tag == "itemref":
                idref = it.get("idref")
                if idref in manifest:
                    href = manifest[idref]
                    full = os.path.normpath(os.path.join(base, href)) if base else href
                    full = full.replace("\\", "/")
                    if full in names:
                        ordered.append(full)
        # append any html docs not captured by the spine
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
            raw = z.read(name).decode("utf-8", "ignore")
        except KeyError:
            continue
        txt = strip_html(raw)
        if txt:
            parts.append(txt)
    return "\n\n".join(parts)


def extract_pdf(path):
    out = subprocess.run(["pdftotext", "-layout", str(path), "-"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit(f"ABORT · pdftotext failed for {path.name}: {out.stderr[:200]}")
    return out.stdout


def main():
    summary = []
    for out_name, keyword, kind in TARGETS:
        dest = OUT / out_name
        if dest.exists():
            raise SystemExit(f"ABORT · refuse to overwrite existing {dest}")
        src = find_raw(keyword)
        text = extract_epub(src) if kind == "epub" else extract_pdf(src)
        wc = len(text.split())
        dest.write_text(text, encoding="utf-8")
        summary.append((out_name, src.name.strip(), kind, wc))
        print(f"  extracted {wc:>7} words -> {out_name}  (from {src.name.strip()[:50]})")
    print(f"\nDONE · {len(summary)} sources extracted into {OUT}")
    total = sum(s[3] for s in summary)
    print(f"total words: {total}")


if __name__ == "__main__":
    main()
