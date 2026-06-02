#!/usr/bin/env python3
"""
Website Design System Search Tool
==================================
Searches across styles, colors, typography, patterns, and UX rules databases
to generate complete design system recommendations.

Usage:
  python3 search.py "modern SaaS dark"                          # Quick search across all domains
  python3 search.py "modern SaaS dark" --design-system          # Full design system recommendation
  python3 search.py "elegant serif" --domain typography          # Search specific domain
  python3 search.py "accessibility forms" --domain ux            # Search UX rules
  python3 search.py "startup landing" --domain pattern           # Search landing page patterns
  python3 search.py "modern SaaS" --stack nextjs-tailwind        # Stack-specific guidelines
  python3 search.py "modern SaaS" --design-system -f markdown    # Markdown output
  python3 search.py "fintech premium" --design-system -p "Acme"  # Include project name

No external dependencies required — uses only Python 3 standard library.
"""

import argparse
import csv
import math
import os
import sys
import textwrap
from collections import Counter
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"

DOMAIN_FILES = {
    "style": "styles.csv",
    "color": "colors.csv",
    "typography": "typography.csv",
    "pattern": "patterns.csv",
    "ux": "ux-rules.csv",
}

# Columns to search in each domain
SEARCH_COLUMNS = {
    "style": ["name", "description", "keywords", "best_for"],
    "color": ["name", "keywords", "best_for", "mood"],
    "typography": ["name", "keywords", "best_for", "pairing_reason"],
    "pattern": ["name", "description", "keywords", "best_for", "conversion_focus"],
    "ux": ["category", "rule", "description", "priority"],
}

# Display columns per domain
DISPLAY_COLUMNS = {
    "style": ["name", "description", "best_for", "css_properties"],
    "color": ["name", "palette_hex", "mood", "accessibility_notes"],
    "typography": ["name", "heading_font", "body_font", "google_fonts_url", "pairing_reason"],
    "pattern": ["name", "description", "sections", "conversion_focus"],
    "ux": ["id", "category", "rule", "priority", "do_example", "dont_example"],
}

STACK_GUIDELINES = {
    "html-tailwind": {
        "name": "HTML + Tailwind CSS",
        "setup": "Use Tailwind CSS via CDN or PostCSS. Structure with semantic HTML5.",
        "tips": [
            "Use @apply in component classes for repeated patterns",
            "Configure tailwind.config.js with design tokens from the design system",
            "Use Tailwind's color opacity modifier: bg-primary/80",
            "Leverage clamp() with arbitrary values: text-[clamp(1rem,2vw,1.5rem)]",
            "Use container queries with @container for component-level responsive",
        ],
        "component_pattern": "Utility-first classes directly in HTML",
    },
    "nextjs-tailwind": {
        "name": "Next.js + Tailwind CSS",
        "setup": "App Router with Tailwind. Use next/font for font optimization.",
        "tips": [
            "Use next/font to self-host Google Fonts with zero layout shift",
            "Server Components for static design elements, Client for interactive",
            "Use CSS variables in tailwind.config.ts for theme switching",
            "next/image for automatic image optimization and lazy loading",
            "Create a design-tokens.ts with all system values as constants",
        ],
        "component_pattern": "React Server Components + Client Components where needed",
    },
    "nextjs-shadcn": {
        "name": "Next.js + shadcn/ui",
        "setup": "App Router with shadcn/ui components. Customize via CSS variables in globals.css.",
        "tips": [
            "Override shadcn theme in globals.css :root and .dark selectors",
            "Use cn() utility for conditional class merging",
            "Extend shadcn components — don't wrap them in extra divs",
            "Use next/font with CSS variable mode for Tailwind integration",
            "Create compound components that compose shadcn primitives",
        ],
        "component_pattern": "shadcn/ui primitives composed into domain components",
    },
    "react-tailwind": {
        "name": "React + Tailwind CSS",
        "setup": "Vite + React + Tailwind. Use clsx or tailwind-merge for class management.",
        "tips": [
            "Use tailwind-merge to resolve conflicting utilities in components",
            "Create a ui/ folder with base components wrapping Tailwind patterns",
            "Use React.forwardRef for all base UI components",
            "CSS variables in index.css for runtime theme switching",
            "Colocate component styles as Tailwind presets",
        ],
        "component_pattern": "Reusable React components with Tailwind utilities",
    },
    "vue-tailwind": {
        "name": "Vue 3 + Tailwind CSS",
        "setup": "Vite + Vue 3 Composition API + Tailwind. Use VueUse for utilities.",
        "tips": [
            "Use <script setup> with Composition API for clean components",
            "Tailwind classes in template, not <style> scoped blocks",
            "Use v-bind in CSS for reactive style properties",
            "Create composables for shared design logic (useTheme, useBreakpoint)",
            "Headless UI Vue for accessible unstyled component primitives",
        ],
        "component_pattern": "Vue SFC components with Tailwind + Composition API",
    },
    "svelte-tailwind": {
        "name": "SvelteKit + Tailwind CSS",
        "setup": "SvelteKit with Tailwind via PostCSS. Use Svelte stores for theme state.",
        "tips": [
            "Use Svelte's class: directive for conditional classes",
            "Tailwind utilities directly in markup — Svelte keeps it clean",
            "Writable stores for theme/dark mode state management",
            "Use Svelte transitions (fade, slide, fly) aligned with design system timing",
            "Skeleton UI or Melt UI for headless accessible components",
        ],
        "component_pattern": "Svelte components with Tailwind + reactive declarations",
    },
}

# ---------------------------------------------------------------------------
# Data Loading
# ---------------------------------------------------------------------------

def load_csv(domain: str) -> list[dict]:
    """Load a CSV file for the given domain."""
    filepath = DATA_DIR / DOMAIN_FILES[domain]
    if not filepath.exists():
        print(f"Error: Data file not found: {filepath}", file=sys.stderr)
        return []
    rows = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# Scoring (TF-IDF-like keyword matching)
# ---------------------------------------------------------------------------

def tokenize(text: str) -> list[str]:
    """Lowercase tokenization with basic cleanup."""
    import re
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\-]", " ", text)
    return [t.strip() for t in text.split() if len(t.strip()) >= 2]


def compute_idf(corpus_tokens: list[list[str]], vocab: set[str]) -> dict[str, float]:
    """Compute inverse document frequency for each term in vocab."""
    n = len(corpus_tokens)
    idf = {}
    for term in vocab:
        doc_count = sum(1 for doc in corpus_tokens if term in doc)
        idf[term] = math.log((n + 1) / (doc_count + 1)) + 1
    return idf


def score_rows(query: str, rows: list[dict], search_cols: list[str], top_n: int = 5) -> list[tuple[dict, float]]:
    """Score rows against query using TF-IDF-like matching. Returns top_n results."""
    query_terms = tokenize(query)
    if not query_terms or not rows:
        return []

    # Build corpus
    corpus_tokens = []
    for row in rows:
        combined = " ".join(row.get(col, "") for col in search_cols)
        corpus_tokens.append(tokenize(combined))

    # IDF
    vocab = set(query_terms)
    idf = compute_idf(corpus_tokens, vocab)

    # Score each row
    scored = []
    for i, doc_tokens in enumerate(corpus_tokens):
        tf_counts = Counter(doc_tokens)
        total = len(doc_tokens) if doc_tokens else 1
        score = 0.0
        for term in query_terms:
            tf = tf_counts.get(term, 0) / total
            # Also check substring matches (partial matching)
            if tf == 0:
                substring_hits = sum(1 for t in doc_tokens if term in t)
                tf = (substring_hits * 0.5) / total
            score += tf * idf.get(term, 1)
        if score > 0:
            scored.append((rows[i], score))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_n]


# ---------------------------------------------------------------------------
# Output Formatting
# ---------------------------------------------------------------------------

def wrap_text(text: str, width: int = 60) -> str:
    """Wrap text to width."""
    return "\n".join(textwrap.wrap(text, width=width))


def format_ascii_box(title: str, content: str, width: int = 78) -> str:
    """Format content in an ASCII box."""
    lines = []
    border = "+" + "-" * (width - 2) + "+"
    lines.append(border)
    # Title
    title_line = f"| {title}{' ' * (width - 4 - len(title))} |"
    lines.append(title_line)
    lines.append(border)
    # Content
    for line in content.split("\n"):
        if len(line) > width - 4:
            wrapped = textwrap.wrap(line, width=width - 4)
            for w in wrapped:
                lines.append(f"| {w}{' ' * (width - 4 - len(w))} |")
        else:
            lines.append(f"| {line}{' ' * (width - 4 - len(line))} |")
    lines.append(border)
    return "\n".join(lines)


def format_domain_results(domain: str, results: list[tuple[dict, float]], fmt: str = "ascii") -> str:
    """Format search results for a specific domain."""
    if not results:
        return f"No results found in {domain}.\n"

    display_cols = DISPLAY_COLUMNS[domain]
    sections = []

    for rank, (row, score) in enumerate(results, 1):
        if fmt == "markdown":
            parts = [f"### {rank}. {row.get('name', row.get('id', 'N/A'))}"]
            parts.append(f"*Relevance score: {score:.3f}*\n")
            for col in display_cols:
                if col in ("name", "id"):
                    continue
                val = row.get(col, "")
                if val:
                    label = col.replace("_", " ").title()
                    parts.append(f"**{label}:** {val}")
            sections.append("\n".join(parts))
        else:
            parts = [f"  #{rank} {row.get('name', row.get('id', 'N/A'))}  (score: {score:.3f})"]
            for col in display_cols:
                if col in ("name", "id"):
                    continue
                val = row.get(col, "")
                if val:
                    label = col.replace("_", " ").title()
                    parts.append(f"    {label}: {val}")
            sections.append("\n".join(parts))

    return "\n\n".join(sections)


def format_design_system(query: str, all_results: dict, project_name: str = "", fmt: str = "ascii") -> str:
    """Format a complete design system recommendation."""
    # Pick top 1 from each domain for the recommendation
    rec = {}
    for domain, results in all_results.items():
        if results:
            rec[domain] = results[0]

    if fmt == "markdown":
        return _format_design_system_md(query, rec, all_results, project_name)
    else:
        return _format_design_system_ascii(query, rec, all_results, project_name)


def _format_design_system_ascii(query: str, rec: dict, all_results: dict, project_name: str) -> str:
    """ASCII box format for design system."""
    w = 78
    border = "+" + "=" * (w - 2) + "+"
    thin = "+" + "-" * (w - 2) + "+"
    lines = []

    # Header
    lines.append(border)
    title = f"DESIGN SYSTEM RECOMMENDATION"
    if project_name:
        title = f"DESIGN SYSTEM: {project_name.upper()}"
    lines.append(f"| {title}{' ' * (w - 4 - len(title))} |")
    subtitle = f'Query: "{query}"'
    lines.append(f"| {subtitle}{' ' * (w - 4 - len(subtitle))} |")
    lines.append(border)

    # Style
    if "style" in rec:
        row, score = rec["style"]
        lines.append(thin)
        lines.append(f"|  VISUAL STYLE: {row['name']}{' ' * (w - 19 - len(row['name']))} |")
        lines.append(thin)
        desc = row.get("description", "")
        for dl in textwrap.wrap(f"  {desc}", width=w - 4):
            lines.append(f"| {dl}{' ' * (w - 4 - len(dl))} |")
        css = row.get("css_properties", "")
        if css:
            lines.append(f"|{' ' * (w - 2)}|")
            label = "  CSS: "
            for dl in textwrap.wrap(f"{label}{css}", width=w - 4):
                lines.append(f"| {dl}{' ' * (w - 4 - len(dl))} |")
        avoid = row.get("avoid_with", "")
        if avoid:
            label = f"  Avoid with: {avoid}"
            for dl in textwrap.wrap(label, width=w - 4):
                lines.append(f"| {dl}{' ' * (w - 4 - len(dl))} |")

    # Color
    if "color" in rec:
        row, score = rec["color"]
        lines.append(thin)
        lines.append(f"|  COLOR PALETTE: {row['name']}{' ' * (w - 20 - len(row['name']))} |")
        lines.append(thin)
        palette = row.get("palette_hex", "")
        label = f"  Palette: {palette}"
        for dl in textwrap.wrap(label, width=w - 4):
            lines.append(f"| {dl}{' ' * (w - 4 - len(dl))} |")
        mood = row.get("mood", "")
        if mood:
            label = f"  Mood: {mood}"
            lines.append(f"| {label}{' ' * (w - 4 - len(label))} |")
        acc = row.get("accessibility_notes", "")
        if acc:
            label = f"  A11y: {acc}"
            for dl in textwrap.wrap(label, width=w - 4):
                lines.append(f"| {dl}{' ' * (w - 4 - len(dl))} |")

    # Typography
    if "typography" in rec:
        row, score = rec["typography"]
        lines.append(thin)
        lines.append(f"|  TYPOGRAPHY: {row['name']}{' ' * (w - 17 - len(row['name']))} |")
        lines.append(thin)
        heading = row.get("heading_font", "")
        body = row.get("body_font", "")
        label = f"  Heading: {heading}  |  Body: {body}"
        lines.append(f"| {label}{' ' * (w - 4 - len(label))} |")
        url = row.get("google_fonts_url", "")
        if url:
            label = f"  Fonts: {url}"
            for dl in textwrap.wrap(label, width=w - 4):
                lines.append(f"| {dl}{' ' * (w - 4 - len(dl))} |")
        reason = row.get("pairing_reason", "")
        if reason:
            label = f"  Why: {reason}"
            for dl in textwrap.wrap(label, width=w - 4):
                lines.append(f"| {dl}{' ' * (w - 4 - len(dl))} |")

    # Pattern
    if "pattern" in rec:
        row, score = rec["pattern"]
        lines.append(thin)
        lines.append(f"|  PAGE PATTERN: {row['name']}{' ' * (w - 19 - len(row['name']))} |")
        lines.append(thin)
        desc = row.get("description", "")
        for dl in textwrap.wrap(f"  {desc}", width=w - 4):
            lines.append(f"| {dl}{' ' * (w - 4 - len(dl))} |")
        sections = row.get("sections", "")
        if sections:
            lines.append(f"|{' ' * (w - 2)}|")
            label = "  Sections:"
            lines.append(f"| {label}{' ' * (w - 4 - len(label))} |")
            for section in sections.split(" | "):
                s = f"    - {section.strip()}"
                lines.append(f"| {s}{' ' * (w - 4 - len(s))} |")

    # Top UX Rules
    if "ux" in all_results and all_results["ux"]:
        lines.append(thin)
        label = "  KEY UX RULES"
        lines.append(f"| {label}{' ' * (w - 4 - len(label))} |")
        lines.append(thin)
        for row, score in all_results["ux"][:3]:
            rid = row.get("id", "")
            rule = row.get("rule", "")
            priority = row.get("priority", "")
            label = f"  [{rid}] ({priority}) {rule}"
            for dl in textwrap.wrap(label, width=w - 4):
                lines.append(f"| {dl}{' ' * (w - 4 - len(dl))} |")

    # Alternatives
    lines.append(thin)
    label = "  ALTERNATIVES"
    lines.append(f"| {label}{' ' * (w - 4 - len(label))} |")
    lines.append(thin)
    for domain in ["style", "color", "typography"]:
        if domain in all_results and len(all_results[domain]) > 1:
            alts = [r[0].get("name", "?") for r in all_results[domain][1:4]]
            label = f"  {domain.title()}: {', '.join(alts)}"
            for dl in textwrap.wrap(label, width=w - 4):
                lines.append(f"| {dl}{' ' * (w - 4 - len(dl))} |")

    lines.append(border)
    return "\n".join(lines)


def _format_design_system_md(query: str, rec: dict, all_results: dict, project_name: str) -> str:
    """Markdown format for design system."""
    parts = []
    title = "Design System Recommendation"
    if project_name:
        title = f"Design System: {project_name}"
    parts.append(f"# {title}")
    parts.append(f'> Query: "{query}"\n')

    if "style" in rec:
        row, _ = rec["style"]
        parts.append(f"## Visual Style: {row['name']}")
        parts.append(f"{row.get('description', '')}\n")
        css = row.get("css_properties", "")
        if css:
            parts.append(f"```css\n{css}\n```")
        avoid = row.get("avoid_with", "")
        if avoid:
            parts.append(f"**Avoid with:** {avoid}\n")

    if "color" in rec:
        row, _ = rec["color"]
        parts.append(f"## Color Palette: {row['name']}")
        palette = row.get("palette_hex", "")
        parts.append(f"**Palette:** `{palette}`\n")
        parts.append(f"**Mood:** {row.get('mood', '')}\n")
        acc = row.get("accessibility_notes", "")
        if acc:
            parts.append(f"**Accessibility:** {acc}\n")

    if "typography" in rec:
        row, _ = rec["typography"]
        parts.append(f"## Typography: {row['name']}")
        parts.append(f"- **Heading:** {row.get('heading_font', '')}")
        parts.append(f"- **Body:** {row.get('body_font', '')}")
        url = row.get("google_fonts_url", "")
        if url:
            parts.append(f"- **Google Fonts:** [{url}]({url})")
        reason = row.get("pairing_reason", "")
        if reason:
            parts.append(f"\n*{reason}*\n")

    if "pattern" in rec:
        row, _ = rec["pattern"]
        parts.append(f"## Page Pattern: {row['name']}")
        parts.append(f"{row.get('description', '')}\n")
        sections = row.get("sections", "")
        if sections:
            parts.append("**Sections:**")
            for section in sections.split(" | "):
                parts.append(f"1. {section.strip()}")
        conv = row.get("conversion_focus", "")
        if conv:
            parts.append(f"\n**Conversion focus:** {conv}\n")

    if "ux" in all_results and all_results["ux"]:
        parts.append("## Key UX Rules")
        for row, _ in all_results["ux"][:5]:
            rid = row.get("id", "")
            rule = row.get("rule", "")
            priority = row.get("priority", "")
            parts.append(f"- **[{rid}]** ({priority}) {rule}")
            do_ex = row.get("do_example", "")
            if do_ex:
                parts.append(f"  - Do: {do_ex}")
            dont_ex = row.get("dont_example", "")
            if dont_ex:
                parts.append(f"  - Don't: {dont_ex}")
        parts.append("")

    # Alternatives
    parts.append("## Alternatives Considered")
    for domain in ["style", "color", "typography", "pattern"]:
        if domain in all_results and len(all_results[domain]) > 1:
            alts = [f"{r[0].get('name', '?')} ({r[1]:.3f})" for r in all_results[domain][1:4]]
            parts.append(f"- **{domain.title()}:** {', '.join(alts)}")

    return "\n".join(parts)


def format_stack_guidelines(stack_key: str, fmt: str = "ascii") -> str:
    """Format stack-specific guidelines."""
    if stack_key not in STACK_GUIDELINES:
        available = ", ".join(STACK_GUIDELINES.keys())
        return f"Unknown stack: {stack_key}\nAvailable stacks: {available}"

    g = STACK_GUIDELINES[stack_key]

    if fmt == "markdown":
        lines = [f"## Stack Guidelines: {g['name']}", ""]
        lines.append(f"**Setup:** {g['setup']}\n")
        lines.append(f"**Component Pattern:** {g['component_pattern']}\n")
        lines.append("**Tips:**")
        for tip in g["tips"]:
            lines.append(f"- {tip}")
        return "\n".join(lines)
    else:
        content = f"Setup: {g['setup']}\n\nComponent Pattern: {g['component_pattern']}\n\nTips:"
        for tip in g["tips"]:
            content += f"\n  - {tip}"
        return format_ascii_box(f"Stack: {g['name']}", content)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Website Design System Search Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
        Examples:
          python3 search.py "modern SaaS dark"                          # Quick search
          python3 search.py "modern SaaS dark" --design-system          # Full recommendation
          python3 search.py "elegant serif" --domain typography         # Typography search
          python3 search.py "accessibility forms" --domain ux           # UX rules search
          python3 search.py "SaaS" --stack nextjs-shadcn                # Stack guidelines
          python3 search.py "fintech" --design-system -f markdown       # Markdown output
          python3 search.py "AI tool" --design-system -p "Acme AI"      # With project name

        Domains: style, color, typography, pattern, ux
        Stacks: html-tailwind, nextjs-tailwind, nextjs-shadcn, react-tailwind, vue-tailwind, svelte-tailwind
        """),
    )
    parser.add_argument("query", help="Search keywords (e.g. 'modern SaaS dark premium')")
    parser.add_argument("--design-system", action="store_true", help="Generate complete design system recommendation")
    parser.add_argument("--domain", choices=list(DOMAIN_FILES.keys()), help="Search a specific domain")
    parser.add_argument("--stack", choices=list(STACK_GUIDELINES.keys()), help="Get stack-specific guidelines")
    parser.add_argument("-f", "--format", choices=["ascii", "markdown"], default="ascii", help="Output format (default: ascii)")
    parser.add_argument("-p", "--project", default="", help="Project name for the design system")
    parser.add_argument("-n", "--top", type=int, default=5, help="Number of results per domain (default: 5)")

    args = parser.parse_args()

    output_parts = []

    if args.design_system:
        # Search all domains
        all_results = {}
        for domain in DOMAIN_FILES:
            rows = load_csv(domain)
            results = score_rows(args.query, rows, SEARCH_COLUMNS[domain], top_n=args.top)
            all_results[domain] = results

        output_parts.append(format_design_system(args.query, all_results, args.project, args.format))

        if args.stack:
            output_parts.append("")
            output_parts.append(format_stack_guidelines(args.stack, args.format))

    elif args.domain:
        # Search specific domain
        rows = load_csv(args.domain)
        results = score_rows(args.query, rows, SEARCH_COLUMNS[args.domain], top_n=args.top)

        if args.format == "markdown":
            output_parts.append(f"## {args.domain.title()} Results for \"{args.query}\"\n")
        else:
            output_parts.append(format_ascii_box(
                f"{args.domain.upper()} SEARCH: \"{args.query}\"",
                f"Found {len(results)} results"
            ))
            output_parts.append("")

        output_parts.append(format_domain_results(args.domain, results, args.format))

        if args.stack:
            output_parts.append("")
            output_parts.append(format_stack_guidelines(args.stack, args.format))

    elif args.stack:
        output_parts.append(format_stack_guidelines(args.stack, args.format))

    else:
        # Quick search across all domains — show top 3 from each
        for domain in DOMAIN_FILES:
            rows = load_csv(domain)
            results = score_rows(args.query, rows, SEARCH_COLUMNS[domain], top_n=3)
            if results:
                if args.format == "markdown":
                    output_parts.append(f"## {domain.title()}\n")
                else:
                    output_parts.append(f"--- {domain.upper()} ---")
                output_parts.append(format_domain_results(domain, results, args.format))
                output_parts.append("")

    print("\n".join(output_parts))


if __name__ == "__main__":
    main()
