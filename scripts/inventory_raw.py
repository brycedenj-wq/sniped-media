#!/usr/bin/env python3
"""
Inventory ~/AI-Brain-Refinery/raw without reading file contents.
Classifies by extension + filename heuristics, produces MD + CSV.
"""
import os
import csv
import re
from pathlib import Path
from collections import defaultdict

RAW = Path.home() / "AI-Brain-Refinery" / "raw"
OUT_DIR = Path.home() / "AI-Brain-Refinery" / "indexes"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Type classification by extension
TYPE_MAP = {
    # Books
    ".epub": "book", ".mobi": "book", ".azw3": "book", ".azw": "book",
    # Documents
    ".pdf": "pdf", ".docx": "doc", ".doc": "doc", ".rtf": "doc",
    ".odt": "doc", ".pages": "doc",
    # Markdown / text
    ".md": "markdown", ".markdown": "markdown",
    ".txt": "text", ".text": "text",
    # Spreadsheets
    ".xlsx": "spreadsheet", ".xls": "spreadsheet", ".csv": "spreadsheet",
    ".numbers": "spreadsheet", ".tsv": "spreadsheet",
    # Slides
    ".pptx": "slides", ".ppt": "slides", ".key": "slides",
    # Code
    ".py": "code", ".js": "code", ".ts": "code", ".tsx": "code",
    ".jsx": "code", ".sh": "code", ".bash": "code", ".zsh": "code",
    ".rb": "code", ".go": "code", ".rs": "code", ".html": "code",
    ".css": "code", ".scss": "code", ".json": "code", ".yaml": "code",
    ".yml": "code", ".toml": "code", ".sql": "code", ".swift": "code",
    # Images
    ".png": "image", ".jpg": "image", ".jpeg": "image", ".webp": "image",
    ".gif": "image", ".heic": "image", ".tiff": "image", ".tif": "image",
    ".bmp": "image", ".svg": "image", ".raf": "image", ".cr2": "image",
    ".nef": "image", ".arw": "image", ".dng": "image", ".raw": "image",
    # Audio
    ".mp3": "audio", ".wav": "audio", ".m4a": "audio", ".aac": "audio",
    ".flac": "audio", ".ogg": "audio", ".aif": "audio", ".aiff": "audio",
    # Video
    ".mp4": "video", ".mov": "video", ".mkv": "video", ".avi": "video",
    ".webm": "video", ".m4v": "video", ".wmv": "video", ".flv": "video",
    # Archive
    ".zip": "archive", ".tar": "archive", ".gz": "archive", ".tgz": "archive",
    ".rar": "archive", ".7z": "archive", ".bz2": "archive",
    # Database
    ".db": "database", ".sqlite": "database", ".sqlite3": "database",
    # Design
    ".psd": "design", ".ai": "design", ".sketch": "design", ".fig": "design",
    ".xd": "design", ".indd": "design",
    # System / metadata
    ".ds_store": "system", ".plist": "system", ".lock": "system",
}

EXTRACTION_MAP = {
    "book": "ebook-convert (Calibre) or pandoc → markdown; chunk by chapter",
    "pdf": "pdftotext / pdfplumber for text PDFs; OCR (tesseract/Azure DI) if scanned",
    "doc": "pandoc or python-docx → markdown",
    "markdown": "direct read (no extraction)",
    "text": "direct read (no extraction)",
    "spreadsheet": "pandas / openpyxl → JSON or markdown table",
    "slides": "python-pptx → outline + speaker notes",
    "code": "direct read (no extraction)",
    "image": "DEFER · vision-LM caption + OCR pass when batch is run",
    "audio": "DEFER · whisper transcription",
    "video": "DEFER · whisper transcription + keyframe vision pass",
    "archive": "unzip first, then re-inventory",
    "database": "sqlite3 / pandas dump to CSV",
    "design": "DEFER · export layers / use Figma API if .fig",
    "system": "SKIP (system metadata)",
    "other": "manual review",
}


def classify_type(path: Path) -> str:
    ext = path.suffix.lower()
    return TYPE_MAP.get(ext, "other")


def human_size(n: int) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if n < 1024:
            return f"{n:.1f}{unit}"
        n /= 1024
    return f"{n:.1f}PB"


# Heuristic patterns for usefulness scoring
HIGH_PATTERNS = [
    r"libgen", r"\bSNIPED\b", r"BRIEF", r"OPERATING_BRIEF",
    r"CANONICAL", r"SPINE", r"DOCTRINE", r"PLAYBOOK",
    r"Stack\.docx", r"_Stack", r"Manifesto", r"INDEX\.md",
    r"Direction[_ ]Stack", r"Trust", r"Pricing", r"Hospitality",
    r"Strateg", r"Positioning", r"\bOp\b", r"OPERATING",
    r"Study_", r"Art_Series", r"STYLIST",
    r"Naval", r"Berger", r"Holiday", r"Enns", r"Maister",
    r"Almanack", r"Perennial", r"Trading[_ ]Up", r"Status[_ ]Anxiety",
    r"Win[_ ]Without[_ ]Pitching", r"Trusted[_ ]Advisor",
    r"Hospitality", r"Blockbuster", r"Hit[_ ]Makers",
    r"Company[_ ]of[_ ]One", r"Elephant[_ ]in[_ ]the[_ ]Brain",
    r"Photograph", r"Pricing[_ ]Creativity",
]
MEDIUM_PATTERNS = [
    r"Reference\.docx", r"_Reference", r"Manual",
    r"chat ", r"thread", r"context", r"figma",
    r"PHOTOGRAPHY", r"PHOTOGRPAHY",
    r"OUTREACH", r"CRM", r"PRODUCTION", r"DELIVERY",
    r"CONTENT", r"REFERENCE", r"NETWORK", r"WEB",
    r"OFFERS", r"CONTRACTS", r"BOOK", r"VAULT",
    r"Aesthetic", r"Brand", r"Identity", r"Naming",
]
LOW_PATTERNS = [
    r"\.DS_Store", r"\.localized", r"\.lock",
    r" copy\.", r" \(1\)\.", r" \(2\)\.",
    r"Thumbs\.db",
]
DEFER_TYPES = {"image", "audio", "video", "design", "archive"}
SKIP_TYPES = {"system"}


def score_usefulness(path: Path, ftype: str) -> str:
    name = path.name
    rel = str(path.relative_to(RAW))
    if ftype in SKIP_TYPES:
        return "low"
    if any(re.search(p, name, re.IGNORECASE) for p in LOW_PATTERNS):
        return "low"
    if ftype in DEFER_TYPES:
        return "unknown"  # need vision/audio review to score
    if any(re.search(p, rel, re.IGNORECASE) for p in HIGH_PATTERNS):
        return "high"
    if any(re.search(p, rel, re.IGNORECASE) for p in MEDIUM_PATTERNS):
        return "medium"
    if ftype in {"book", "doc", "markdown", "pdf", "code", "spreadsheet"}:
        return "medium"
    return "unknown"


def priority(path: Path, ftype: str, useful: str, size: int) -> int:
    """Lower number = higher priority."""
    if useful == "high" and ftype in {"markdown", "doc", "text"}:
        return 1
    if useful == "high" and ftype in {"book", "pdf"} and size < 20_000_000:
        return 2
    if useful == "high":
        return 3
    if useful == "medium" and ftype in {"markdown", "doc", "text", "code"}:
        return 4
    if useful == "medium":
        return 5
    if useful == "unknown" and ftype in DEFER_TYPES:
        return 8
    if useful == "low":
        return 9
    return 6


def needs_ocr_or_transcription(path: Path, ftype: str, size: int) -> bool:
    if ftype in {"audio", "video"}:
        return True
    if ftype == "image" and size > 50_000:  # not a thumbnail
        return True
    if ftype == "pdf" and size > 50_000_000:  # large PDF likely scanned
        return True
    return False


def notes_for(path: Path, ftype: str, useful: str, size: int) -> str:
    notes = []
    name = path.name
    if " copy." in name or re.search(r" \(\d+\)\.", name):
        notes.append("likely duplicate")
    if ftype == "pdf" and size > 100_000_000:
        notes.append("very large PDF · check if scanned vs text")
    if "libgen" in name.lower():
        notes.append("libgen book · canonical knowledge source")
    if ftype == "image" and size > 5_000_000:
        notes.append("high-res image · vision pass when batched")
    if name.startswith("."):
        notes.append("hidden/system file")
    if "_archive" in str(path.relative_to(RAW)):
        notes.append("archived · low priority unless needed")
    if "_inbox" in str(path.relative_to(RAW)):
        notes.append("inbox · check for unprocessed intake")
    return "; ".join(notes)


# ---- Walk filesystem ----
records = []
for root, dirs, files in os.walk(RAW):
    # don't descend into system dirs
    dirs[:] = [d for d in dirs if d not in {".git", "node_modules", "__pycache__"}]
    for f in files:
        p = Path(root) / f
        try:
            size = p.stat().st_size
        except OSError:
            continue
        ftype = classify_type(p)
        useful = score_usefulness(p, ftype)
        prio = priority(p, ftype, useful, size)
        rel = str(p.relative_to(RAW))
        records.append({
            "path": rel,
            "ext": p.suffix.lower(),
            "type": ftype,
            "size_bytes": size,
            "size_human": human_size(size),
            "usefulness": useful,
            "extraction": EXTRACTION_MAP.get(ftype, "manual review"),
            "priority": prio,
            "needs_ocr_transcription": needs_ocr_or_transcription(p, ftype, size),
            "notes": notes_for(p, ftype, useful, size),
        })

records.sort(key=lambda r: (r["priority"], -r["size_bytes"]))

# ---- Write CSV ----
csv_path = OUT_DIR / "FILE_INVENTORY.csv"
with csv_path.open("w", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=[
        "path", "ext", "type", "size_bytes", "size_human",
        "usefulness", "extraction", "priority",
        "needs_ocr_transcription", "notes",
    ])
    writer.writeheader()
    for r in records:
        writer.writerow(r)

# ---- Aggregates ----
total_files = len(records)
total_bytes = sum(r["size_bytes"] for r in records)
by_type = defaultdict(lambda: {"count": 0, "bytes": 0})
by_useful = defaultdict(lambda: {"count": 0, "bytes": 0})
for r in records:
    by_type[r["type"]]["count"] += 1
    by_type[r["type"]]["bytes"] += r["size_bytes"]
    by_useful[r["usefulness"]]["count"] += 1
    by_useful[r["usefulness"]]["bytes"] += r["size_bytes"]

largest_20 = sorted(records, key=lambda r: -r["size_bytes"])[:20]

best_first_25 = [
    r for r in sorted(records, key=lambda r: (r["priority"], -r["size_bytes"]))
    if r["usefulness"] == "high" and r["type"] not in DEFER_TYPES
][:25]

needs_ocr = [r for r in records if r["needs_ocr_transcription"]]
skip_or_defer = [
    r for r in records
    if r["usefulness"] == "low"
    or r["type"] in DEFER_TYPES
    or r["type"] in SKIP_TYPES
]

# ---- Write Markdown ----
md_path = OUT_DIR / "FILE_INVENTORY.md"
lines = []
lines.append("# FILE_INVENTORY · ~/AI-Brain-Refinery/raw")
lines.append("")
lines.append(f"Generated by `scripts/inventory_raw.py` · {total_files} files · "
             f"{human_size(total_bytes)}")
lines.append("")
lines.append("## Type breakdown")
lines.append("")
lines.append("| Type | Count | Total size |")
lines.append("|------|------:|-----------:|")
for t in sorted(by_type, key=lambda k: -by_type[k]["count"]):
    lines.append(f"| {t} | {by_type[t]['count']} | {human_size(by_type[t]['bytes'])} |")
lines.append("")
lines.append("## Usefulness breakdown")
lines.append("")
lines.append("| Usefulness | Count | Total size |")
lines.append("|------------|------:|-----------:|")
for u in ["high", "medium", "unknown", "low"]:
    if u in by_useful:
        lines.append(f"| {u} | {by_useful[u]['count']} | {human_size(by_useful[u]['bytes'])} |")
lines.append("")
lines.append("## Full inventory (sorted by priority, then size desc)")
lines.append("")
lines.append("| Pri | Path | Type | Size | Useful | Extraction | OCR/Transcribe | Notes |")
lines.append("|----:|------|------|-----:|--------|-----------|:--:|-------|")
for r in records:
    path_disp = r["path"].replace("|", "\\|")
    notes_disp = r["notes"].replace("|", "\\|")
    extr_disp = r["extraction"].replace("|", "\\|")
    lines.append(
        f"| {r['priority']} | `{path_disp}` | {r['type']} | "
        f"{r['size_human']} | {r['usefulness']} | {extr_disp} | "
        f"{'Y' if r['needs_ocr_transcription'] else ''} | {notes_disp} |"
    )

md_path.write_text("\n".join(lines))

# ---- Print analytics for the user ----
print(f"TOTAL_FILES={total_files}")
print(f"TOTAL_SIZE={human_size(total_bytes)}")
print(f"TOTAL_BYTES={total_bytes}")
print()
print("=== LARGEST 20 ===")
for r in largest_20:
    print(f"  {r['size_human']:>10}  [{r['type']:<10}] {r['path']}")
print()
print("=== BEST FIRST 25 (high usefulness, not defer-type) ===")
for r in best_first_25:
    print(f"  pri={r['priority']} [{r['type']:<10}] {r['size_human']:>10}  {r['path']}")
print()
print(f"=== OCR/TRANSCRIPTION NEEDED ({len(needs_ocr)}) ===")
for r in needs_ocr[:30]:
    print(f"  [{r['type']:<6}] {r['size_human']:>10}  {r['path']}")
if len(needs_ocr) > 30:
    print(f"  ... and {len(needs_ocr)-30} more")
print()
print(f"=== SKIP / DEFER ({len(skip_or_defer)}) ===")
defer_by_type = defaultdict(int)
for r in skip_or_defer:
    defer_by_type[r["type"]] += 1
for t, c in sorted(defer_by_type.items(), key=lambda x: -x[1]):
    print(f"  {t:<10} {c}")
