#!/usr/bin/env python3
"""
Extract the 6 CORE MONEY_OWNERSHIP sources into
01_KNOWLEDGE_BASE/batches/money_ownership_extracted/.

5 books (3 pdf via pdftotext, 2 epub via stdlib zipfile + HTML-strip) + 1 docx via pandoc.
Keyword-substring matching handles leading-space filenames. No OCR. No new deps.
Does NOT modify raw/. Refuses to overwrite an existing extracted file.
"""

import os, re, subprocess, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path.home() / "AI-Brain-Refinery"
OUT = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "money_ownership_extracted"
OUT.mkdir(parents=True, exist_ok=True)

INVEST = ROOT / "raw" / "03_TIER_2_CANON_BOOKS" / "investing_finance"

# (output_name, search_dir, keyword, kind)
TARGETS = [
    ("psychology_of_money_housel.txt", INVEST, "Psychology of Money", "pdf"),
    ("essays_of_warren_buffett.txt", INVEST, "Essays of Warren Buffett", "epub"),
    ("the_most_important_thing_marks.txt", INVEST, "most important thing", "pdf"),
    ("king_of_capital_blackstone.txt", INVEST, "King of Capital", "epub"),
    ("the_power_law_mallaby.txt", INVEST, "Power Law", "epub"),
    ("money_wealth_getting_ahead.txt", ROOT / "raw", "Money_Wealth_Getting_Ahead", "docx"),
]


def find_one(folder, keyword):
    matches = [p for p in folder.iterdir() if p.is_file() and keyword in p.name]
    if len(matches) != 1:
        raise SystemExit(f"ABORT · expected 1 match for '{keyword}' in {folder}, got {len(matches)}: {[m.name for m in matches]}")
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


def extract_docx(path):
    out = subprocess.run(["pandoc", "-f", "docx", "-t", "plain", str(path)], capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit(f"ABORT · pandoc failed for {path.name}: {out.stderr[:200]}")
    return out.stdout


def main():
    summary = []
    for out_name, folder, keyword, kind in TARGETS:
        dest = OUT / out_name
        if dest.exists():
            raise SystemExit(f"ABORT · refuse to overwrite existing {dest}")
        src = find_one(folder, keyword)
        if kind == "epub":
            text = extract_epub(src)
        elif kind == "pdf":
            text = extract_pdf(src)
        else:
            text = extract_docx(src)
        wc = len(text.split())
        dest.write_text(text, encoding="utf-8")
        summary.append((out_name, src.name.strip(), kind, wc))
        print(f"  {wc:>7} w  {kind:4}  -> {out_name}  (from {src.name.strip()[:48]})")
    print(f"\nDONE · {len(summary)} sources extracted into {OUT}")
    print(f"total words: {sum(s[3] for s in summary)}")


if __name__ == "__main__":
    main()
