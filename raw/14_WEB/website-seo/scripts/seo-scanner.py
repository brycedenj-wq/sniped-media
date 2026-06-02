#!/usr/bin/env python3
"""
SEO Scanner - A comprehensive HTML SEO audit tool.

Scans HTML files for SEO issues including meta tags, heading structure,
images, links, schema markup, accessibility, performance indicators,
and AI search readiness.

Usage:
    python3 seo-scanner.py path/to/file.html
    python3 seo-scanner.py path/to/site/
    python3 seo-scanner.py --url https://example.com
    python3 seo-scanner.py path/to/file.html --keyword "target keyword"
    python3 seo-scanner.py path/to/file.html --json
    python3 seo-scanner.py path/to/file.html --verbose

No external dependencies required - uses Python 3 standard library only.
"""

import argparse
import json
import os
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError


# ---------------------------------------------------------------------------
# HTML Parser
# ---------------------------------------------------------------------------

class SEOHTMLParser(HTMLParser):
    """Custom HTML parser that extracts SEO-relevant data from HTML."""

    def __init__(self):
        super().__init__()
        # Meta tags
        self.title = None
        self.meta_description = None
        self.meta_viewport = None
        self.meta_robots = None
        self.canonical = None
        self.og_tags = {}
        self.twitter_tags = {}

        # Headings
        self.headings = []  # list of (level, text)
        self._current_heading = None
        self._current_heading_text = ""

        # Images
        self.images = []  # list of dicts

        # Links
        self.links = []  # list of dicts

        # Schema / JSON-LD
        self.json_ld_blocks = []
        self._in_json_ld = False
        self._json_ld_buffer = ""

        # Accessibility
        self.html_lang = None
        self.form_inputs = []  # list of dicts
        self.labels = []  # list of for-attribute values
        self.skip_nav_link = False
        self.buttons = []
        self._current_button_text = ""
        self._in_button = False

        # Performance
        self.stylesheets = []
        self.scripts = []
        self.inline_style_count = 0

        # Content
        self._text_chunks = []
        self._in_body = False
        self._in_script = False
        self._in_style = False
        self._in_title = False
        self._title_text = ""

        # General
        self._tag_stack = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        self._tag_stack.append(tag)

        if tag == "html":
            self.html_lang = attr_dict.get("lang")

        elif tag == "body":
            self._in_body = True

        elif tag == "title":
            self._in_title = True
            self._title_text = ""

        elif tag == "meta":
            name = attr_dict.get("name", "").lower()
            prop = attr_dict.get("property", "").lower()
            content = attr_dict.get("content", "")

            if name == "description":
                self.meta_description = content
            elif name == "viewport":
                self.meta_viewport = content
            elif name == "robots":
                self.meta_robots = content
            elif prop == "og:title":
                self.og_tags["og:title"] = content
            elif prop == "og:description":
                self.og_tags["og:description"] = content
            elif prop == "og:image":
                self.og_tags["og:image"] = content
            elif prop == "og:url":
                self.og_tags["og:url"] = content
            elif prop == "og:type":
                self.og_tags["og:type"] = content
            elif name == "twitter:card":
                self.twitter_tags["twitter:card"] = content
            elif name == "twitter:title":
                self.twitter_tags["twitter:title"] = content
            elif name == "twitter:description":
                self.twitter_tags["twitter:description"] = content
            elif name == "twitter:image":
                self.twitter_tags["twitter:image"] = content

        elif tag == "link":
            rel = attr_dict.get("rel", "")
            href = attr_dict.get("href", "")
            if rel == "canonical":
                self.canonical = href
            elif rel == "stylesheet":
                media = attr_dict.get("media", "")
                self.stylesheets.append({
                    "href": href,
                    "media": media,
                })

        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            self._current_heading = level
            self._current_heading_text = ""

        elif tag == "img":
            self.images.append({
                "src": attr_dict.get("src", ""),
                "alt": attr_dict.get("alt"),
                "width": attr_dict.get("width"),
                "height": attr_dict.get("height"),
                "loading": attr_dict.get("loading"),
            })

        elif tag == "a":
            href = attr_dict.get("href", "")
            rel = attr_dict.get("rel", "")
            target = attr_dict.get("target", "")
            self.links.append({
                "href": href,
                "rel": rel,
                "target": target,
                "text": "",
            })
            # Check for skip nav link
            if href.startswith("#") and any(
                kw in href.lower()
                for kw in ["main", "content", "skip"]
            ):
                self.skip_nav_link = True

        elif tag == "script":
            script_type = attr_dict.get("type", "")
            src = attr_dict.get("src", "")
            if script_type == "application/ld+json":
                self._in_json_ld = True
                self._json_ld_buffer = ""
            elif src:
                self.scripts.append({
                    "src": src,
                    "async": "async" in attr_dict,
                    "defer": "defer" in attr_dict,
                })
            self._in_script = True

        elif tag == "style":
            self._in_style = True
            self.inline_style_count += 1

        elif tag == "input":
            input_type = attr_dict.get("type", "text").lower()
            if input_type not in ("hidden", "submit", "button", "reset"):
                self.form_inputs.append({
                    "type": input_type,
                    "id": attr_dict.get("id", ""),
                    "name": attr_dict.get("name", ""),
                    "aria_label": attr_dict.get("aria-label", ""),
                    "aria_labelledby": attr_dict.get("aria-labelledby", ""),
                    "title": attr_dict.get("title", ""),
                })

        elif tag == "label":
            for_attr = attr_dict.get("for", "")
            if for_attr:
                self.labels.append(for_attr)

        elif tag == "button":
            self._in_button = True
            self._current_button_text = ""
            aria_label = attr_dict.get("aria-label", "")
            self.buttons.append({
                "aria_label": aria_label,
                "text": "",
            })

        # Track inline style attributes
        if "style" in attr_dict and tag != "style":
            self.inline_style_count += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
            self.title = self._title_text.strip()

        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self._current_heading is not None:
            text = self._current_heading_text.strip()
            self.headings.append((self._current_heading, text))
            self._current_heading = None
            self._current_heading_text = ""

        elif tag == "a" and self.links:
            # finalize the last link text
            pass

        elif tag == "script":
            if self._in_json_ld:
                self._in_json_ld = False
                try:
                    parsed = json.loads(self._json_ld_buffer)
                    self.json_ld_blocks.append(parsed)
                except (json.JSONDecodeError, ValueError):
                    pass
            self._in_script = False

        elif tag == "style":
            self._in_style = False

        elif tag == "button":
            self._in_button = False
            if self.buttons:
                self.buttons[-1]["text"] = self._current_button_text.strip()

        if self._tag_stack and self._tag_stack[-1] == tag:
            self._tag_stack.pop()

    def handle_data(self, data):
        if self._in_title:
            self._title_text += data

        if self._in_json_ld:
            self._json_ld_buffer += data

        if self._current_heading is not None:
            self._current_heading_text += data

        if self._in_button:
            self._current_button_text += data

        # Capture link text
        if self.links and "a" in self._tag_stack:
            self.links[-1]["text"] += data.strip()

        # Capture body text for content analysis
        if self._in_body and not self._in_script and not self._in_style:
            stripped = data.strip()
            if stripped:
                self._text_chunks.append(stripped)

    def get_body_text(self):
        return " ".join(self._text_chunks)


# ---------------------------------------------------------------------------
# SEO Checks
# ---------------------------------------------------------------------------

class SEOAudit:
    """Performs SEO checks on parsed HTML data."""

    def __init__(self, parser, filename="unknown", keyword=None):
        self.parser = parser
        self.filename = filename
        self.keyword = keyword.lower() if keyword else None
        self.critical = []
        self.warnings = []
        self.passed = []
        self.recommendations = []
        self.ai_readiness = []
        self.details = {}

    def run_all_checks(self):
        self.check_meta_tags()
        self.check_headings()
        self.check_images()
        self.check_links()
        self.check_schema()
        self.check_accessibility()
        self.check_performance()
        self.check_content()
        self.check_ai_readiness()

    # -- Meta Tags ----------------------------------------------------------

    def check_meta_tags(self):
        p = self.parser

        # Title
        if not p.title:
            self.critical.append("Missing title tag")
        elif len(p.title) == 0:
            self.critical.append("Title tag is empty")
        elif len(p.title) > 60:
            self.warnings.append(
                f"Title tag is {len(p.title)} characters (recommended: under 60)"
            )
        else:
            self.passed.append(
                f"Title tag present ({len(p.title)} chars)"
            )

        if p.title and len(p.title) < 20:
            self.warnings.append(
                f"Title tag is only {len(p.title)} characters (may be too short)"
            )

        # Meta description
        if p.meta_description is None:
            self.critical.append("Missing meta description")
            self.recommendations.append(
                "Add meta description (150-160 chars) summarizing page content"
            )
        elif len(p.meta_description) == 0:
            self.critical.append("Meta description is empty")
        elif len(p.meta_description) > 160:
            self.warnings.append(
                f"Meta description is {len(p.meta_description)} characters "
                "(recommended: under 160)"
            )
        elif len(p.meta_description) < 70:
            self.warnings.append(
                f"Meta description is only {len(p.meta_description)} characters "
                "(recommended: 150-160)"
            )
        else:
            self.passed.append(
                f"Meta description present ({len(p.meta_description)} chars)"
            )

        # Viewport
        if p.meta_viewport:
            self.passed.append("Viewport meta tag set correctly")
        else:
            self.critical.append("Missing viewport meta tag (mobile issues)")

        # Canonical
        if p.canonical:
            self.passed.append(f"Canonical URL set: {p.canonical}")
        else:
            self.warnings.append("No canonical URL specified")

        # Open Graph
        og_required = ["og:title", "og:description", "og:image"]
        og_missing = [t for t in og_required if t not in p.og_tags]
        if not og_missing:
            self.passed.append("Open Graph tags present (title, description, image)")
        elif len(og_missing) == len(og_required):
            self.warnings.append("No Open Graph tags found")
            self.recommendations.append(
                "Add Open Graph tags (og:title, og:description, og:image) for social sharing"
            )
        else:
            self.warnings.append(f"Missing Open Graph tags: {', '.join(og_missing)}")

        # Twitter Card
        if p.twitter_tags.get("twitter:card"):
            self.passed.append("Twitter Card tags present")
        else:
            self.warnings.append("No Twitter Card tags found")

        # Robots
        if p.meta_robots:
            robots_lower = p.meta_robots.lower()
            if "noindex" in robots_lower:
                self.warnings.append(
                    f"Page is set to noindex ({p.meta_robots})"
                )
            else:
                self.passed.append(f"Robots meta: {p.meta_robots}")

        self.details["meta"] = {
            "title": p.title,
            "title_length": len(p.title) if p.title else 0,
            "description": p.meta_description,
            "description_length": len(p.meta_description) if p.meta_description else 0,
            "viewport": p.meta_viewport,
            "canonical": p.canonical,
            "robots": p.meta_robots,
            "og_tags": p.og_tags,
            "twitter_tags": p.twitter_tags,
        }

    # -- Headings -----------------------------------------------------------

    def check_headings(self):
        p = self.parser
        h1_tags = [h for h in p.headings if h[0] == 1]

        # H1 count
        if len(h1_tags) == 0:
            self.critical.append("No H1 tag found")
        elif len(h1_tags) == 1:
            self.passed.append("Single H1 tag")
        else:
            self.warnings.append(f"Multiple H1 tags found ({len(h1_tags)})")

        # Empty headings
        empty_headings = [h for h in p.headings if not h[1]]
        if empty_headings:
            levels = [f"H{h[0]}" for h in empty_headings]
            self.warnings.append(f"Empty headings found: {', '.join(levels)}")

        # Heading hierarchy (check for skipping levels)
        if p.headings:
            prev_level = 0
            skip_issues = []
            for level, text in p.headings:
                if prev_level > 0 and level > prev_level + 1:
                    skip_issues.append(f"H{prev_level} jumps to H{level}")
                prev_level = level

            if skip_issues:
                self.warnings.append(
                    f"Heading hierarchy issues: {'; '.join(skip_issues)}"
                )
            elif len(p.headings) > 1:
                self.passed.append("Heading hierarchy is correct (no skipped levels)")

        self.details["headings"] = {
            "total": len(p.headings),
            "h1_count": len(h1_tags),
            "hierarchy": [(f"H{h[0]}", h[1][:80]) for h in p.headings],
        }

    # -- Images -------------------------------------------------------------

    def check_images(self):
        p = self.parser

        if not p.images:
            self.passed.append("No images found (nothing to check)")
            self.details["images"] = {"total": 0}
            return

        no_alt = [img for img in p.images if img["alt"] is None]
        empty_alt = [img for img in p.images if img["alt"] is not None and img["alt"].strip() == ""]
        no_dimensions = [
            img for img in p.images
            if not img["width"] or not img["height"]
        ]

        if no_alt:
            src_list = [img["src"].split("/")[-1] or img["src"] for img in no_alt]
            self.critical.append(
                f"{len(no_alt)} image(s) without alt text"
            )
            self.recommendations.append(
                f"Add alt text to: {', '.join(src_list[:5])}"
                + (f" (and {len(src_list)-5} more)" if len(src_list) > 5 else "")
            )
        else:
            self.passed.append(f"All {len(p.images)} images have alt attributes")

        if no_dimensions:
            self.warnings.append(
                f"{len(no_dimensions)} image(s) missing width/height (CLS risk)"
            )

        lazy_loaded = [img for img in p.images if img.get("loading") == "lazy"]
        if lazy_loaded:
            self.passed.append(f"{len(lazy_loaded)} image(s) use lazy loading")

        self.details["images"] = {
            "total": len(p.images),
            "missing_alt": len(no_alt),
            "empty_alt": len(empty_alt),
            "missing_dimensions": len(no_dimensions),
            "lazy_loaded": len(lazy_loaded),
        }

    # -- Links --------------------------------------------------------------

    def check_links(self):
        p = self.parser

        internal = []
        external = []
        empty_text = []
        nofollow = []
        new_tab_no_rel = []

        for link in p.links:
            href = link.get("href", "")
            rel = link.get("rel", "")
            target = link.get("target", "")
            text = link.get("text", "").strip()

            if not href or href.startswith("#") or href.startswith("javascript:"):
                continue

            if href.startswith("http://") or href.startswith("https://"):
                external.append(link)
            else:
                internal.append(link)

            if not text:
                empty_text.append(link)

            if "nofollow" in rel:
                nofollow.append(link)

            if target == "_blank" and "noopener" not in rel:
                new_tab_no_rel.append(link)

        if internal:
            self.passed.append(f"{len(internal)} internal links found")
        else:
            self.warnings.append("No internal links found")

        if external:
            self.passed.append(f"{len(external)} external links found")

        if empty_text:
            self.warnings.append(
                f"{len(empty_text)} link(s) with no anchor text"
            )

        if new_tab_no_rel:
            self.warnings.append(
                f'{len(new_tab_no_rel)} link(s) open in new tab without rel="noopener"'
            )

        self.details["links"] = {
            "internal": len(internal),
            "external": len(external),
            "empty_text": len(empty_text),
            "nofollow": len(nofollow),
            "new_tab_no_rel": len(new_tab_no_rel),
        }

    # -- Schema Markup ------------------------------------------------------

    def check_schema(self):
        p = self.parser

        if not p.json_ld_blocks:
            self.critical.append("No schema markup found (JSON-LD)")
            self.recommendations.append(
                "Add Article, WebPage, or Organization schema markup"
            )
            self.details["schema"] = {"found": False, "types": []}
            return

        schema_types = []
        for block in p.json_ld_blocks:
            if isinstance(block, dict):
                if "@graph" in block:
                    for item in block["@graph"]:
                        if isinstance(item, dict) and "@type" in item:
                            schema_types.append(item["@type"])
                elif "@type" in block:
                    schema_types.append(block["@type"])

        self.passed.append(
            f"Schema markup found: {', '.join(schema_types)}"
        )

        # Validate basic structure
        for block in p.json_ld_blocks:
            if isinstance(block, dict):
                if "@context" not in block:
                    self.warnings.append(
                        "Schema block missing @context property"
                    )

        self.details["schema"] = {
            "found": True,
            "types": schema_types,
            "block_count": len(p.json_ld_blocks),
        }

    # -- Accessibility ------------------------------------------------------

    def check_accessibility(self):
        p = self.parser

        # html lang
        if p.html_lang:
            self.passed.append(f"html lang attribute present ({p.html_lang})")
        else:
            self.critical.append("Missing html lang attribute")

        # Form inputs without labels
        label_ids = set(p.labels)
        unlabeled = []
        for inp in p.form_inputs:
            input_id = inp.get("id", "")
            has_label = input_id and input_id in label_ids
            has_aria = inp.get("aria_label") or inp.get("aria_labelledby") or inp.get("title")
            if not has_label and not has_aria:
                unlabeled.append(inp)

        if unlabeled:
            self.warnings.append(
                f"{len(unlabeled)} form input(s) without associated labels"
            )
        elif p.form_inputs:
            self.passed.append("All form inputs have labels or ARIA attributes")

        # Buttons without accessible names
        nameless_buttons = [
            b for b in p.buttons
            if not b.get("text", "").strip() and not b.get("aria_label", "").strip()
        ]
        if nameless_buttons:
            self.warnings.append(
                f"{len(nameless_buttons)} button(s) without accessible names"
            )

        # Skip navigation
        if p.skip_nav_link:
            self.passed.append("Skip navigation link detected")
        elif p.links:
            self.warnings.append("No skip navigation link found")

        self.details["accessibility"] = {
            "html_lang": p.html_lang,
            "unlabeled_inputs": len(unlabeled),
            "nameless_buttons": len(nameless_buttons),
            "skip_nav": p.skip_nav_link,
        }

    # -- Performance --------------------------------------------------------

    def check_performance(self):
        p = self.parser

        # Render-blocking stylesheets
        blocking_css = [
            s for s in p.stylesheets
            if not s.get("media") or s["media"] == "all"
        ]
        if blocking_css:
            self.warnings.append(
                f"{len(blocking_css)} stylesheet(s) potentially render-blocking "
                "(no media query)"
            )

        # Scripts without async/defer
        blocking_scripts = [
            s for s in p.scripts
            if not s.get("async") and not s.get("defer")
        ]
        if blocking_scripts:
            src_names = [
                s["src"].split("/")[-1] for s in blocking_scripts
            ]
            self.warnings.append(
                f"{len(blocking_scripts)} script(s) without async or defer"
            )
            if src_names:
                self.recommendations.append(
                    f"Add defer to: {', '.join(src_names[:5])}"
                    + (f" (and {len(src_names)-5} more)" if len(src_names) > 5 else "")
                )
        elif p.scripts:
            self.passed.append("All external scripts use async or defer")

        # Inline styles
        if p.inline_style_count > 10:
            self.warnings.append(
                f"Excessive inline styles detected ({p.inline_style_count} occurrences)"
            )

        # External resource count
        total_external = len(p.stylesheets) + len(p.scripts) + len(
            [img for img in p.images if img.get("src", "").startswith("http")]
        )
        if total_external > 50:
            self.warnings.append(
                f"High number of external resources ({total_external})"
            )

        self.details["performance"] = {
            "stylesheets": len(p.stylesheets),
            "blocking_css": len(blocking_css),
            "scripts": len(p.scripts),
            "blocking_scripts": len(blocking_scripts),
            "inline_styles": p.inline_style_count,
            "external_resources": total_external,
        }

    # -- Content Analysis ---------------------------------------------------

    def check_content(self):
        p = self.parser
        body_text = p.get_body_text()
        words = re.findall(r'\b[a-zA-Z]+\b', body_text.lower())
        word_count = len(words)
        reading_time = max(1, round(word_count / 238))

        self.details["content"] = {
            "word_count": word_count,
            "reading_time_minutes": reading_time,
        }

        if word_count < 300:
            self.warnings.append(
                f"Thin content: only {word_count} words (aim for 300+ for most pages)"
            )
        else:
            self.passed.append(f"Content length: {word_count} words (~{reading_time} min read)")

        # Keyword analysis
        if self.keyword and words:
            kw_lower = self.keyword.lower()
            kw_words = kw_lower.split()

            # Exact phrase count
            exact_count = body_text.lower().count(kw_lower)

            # Density (of the keyword phrase)
            density = (exact_count / max(1, word_count)) * 100

            # Check keyword in title
            kw_in_title = kw_lower in (p.title or "").lower()
            # Check keyword in H1
            h1_texts = [h[1].lower() for h in p.headings if h[0] == 1]
            kw_in_h1 = any(kw_lower in h for h in h1_texts)
            # Check in meta description
            kw_in_desc = kw_lower in (p.meta_description or "").lower()
            # Check in first 100 words
            first_100 = " ".join(words[:100])
            kw_in_first_100 = kw_lower in first_100

            self.details["keyword"] = {
                "keyword": self.keyword,
                "exact_matches": exact_count,
                "density_percent": round(density, 2),
                "in_title": kw_in_title,
                "in_h1": kw_in_h1,
                "in_meta_description": kw_in_desc,
                "in_first_100_words": kw_in_first_100,
            }

            if kw_in_title:
                self.passed.append(f'Keyword "{self.keyword}" found in title')
            else:
                self.warnings.append(f'Keyword "{self.keyword}" not found in title')

            if kw_in_h1:
                self.passed.append(f'Keyword "{self.keyword}" found in H1')
            else:
                self.warnings.append(f'Keyword "{self.keyword}" not found in H1')

            if kw_in_desc:
                self.passed.append(f'Keyword "{self.keyword}" found in meta description')
            elif p.meta_description:
                self.warnings.append(
                    f'Keyword "{self.keyword}" not found in meta description'
                )

            if kw_in_first_100:
                self.passed.append(
                    f'Keyword "{self.keyword}" found in first 100 words'
                )
            else:
                self.warnings.append(
                    f'Keyword "{self.keyword}" not found in first 100 words'
                )

            if density > 3:
                self.warnings.append(
                    f'Keyword density is {density:.1f}% (may be too high, aim for 1-2%)'
                )
            elif exact_count > 0:
                self.passed.append(
                    f'Keyword density: {density:.1f}% ({exact_count} occurrences)'
                )

        # Internal vs external link summary
        internal_count = self.details.get("links", {}).get("internal", 0)
        external_count = self.details.get("links", {}).get("external", 0)
        self.details["content"]["internal_links"] = internal_count
        self.details["content"]["external_links"] = external_count

    # -- AI Search Readiness ------------------------------------------------

    def check_ai_readiness(self):
        p = self.parser

        # FAQ schema
        schema_types = self.details.get("schema", {}).get("types", [])
        has_faq_schema = "FAQPage" in schema_types
        has_howto_schema = "HowTo" in schema_types
        has_article_schema = any(
            t in schema_types for t in ["Article", "BlogPosting", "NewsArticle"]
        )
        has_any_schema = bool(schema_types)

        if has_faq_schema:
            self.ai_readiness.append(("pass", "FAQ schema present (AI Overview opportunity)"))
        else:
            self.ai_readiness.append(("fail", "No FAQ schema (missing AI Overview opportunity)"))

        if has_howto_schema:
            self.ai_readiness.append(("pass", "HowTo schema present"))

        if has_article_schema:
            self.ai_readiness.append(("pass", "Article schema present (helps AI identify content type)"))
        elif not has_any_schema:
            self.ai_readiness.append(("fail", "No schema markup found (AI systems benefit from structured data)"))

        # Structured answer blocks (detect FAQ-like sections, definition patterns)
        body_text = p.get_body_text().lower()
        has_definition = bool(re.search(r'\b(is|are|refers to|means|defined as)\b', body_text[:500]))
        has_faq_section = any(
            "faq" in h[1].lower() or "frequently asked" in h[1].lower()
            for h in p.headings
        )

        if has_faq_section:
            self.ai_readiness.append(("pass", "FAQ section detected in headings"))
        else:
            self.ai_readiness.append(("fail", "No structured FAQ section detected"))

        if has_definition:
            self.ai_readiness.append(("pass", "Definition/answer pattern detected in opening content"))
        else:
            self.ai_readiness.append(("warn", "No clear definition or direct answer in opening content"))

        # Last updated / date signals
        has_date = bool(re.search(
            r'(last\s+updated|published|modified|date)\s*[:\s]\s*\d',
            body_text,
            re.IGNORECASE
        ))
        if has_date:
            self.ai_readiness.append(("pass", "Date/update signal detected in content"))
        else:
            self.ai_readiness.append(("warn", 'No visible "last updated" date detected'))

        # Heading structure for extractability
        if p.headings and not any(
            h[0] == 1 for h in p.headings
        ):
            self.ai_readiness.append(("fail", "Missing H1 (AI systems need clear content hierarchy)"))
        elif len(p.headings) >= 3:
            self.ai_readiness.append(("pass", "Clear heading hierarchy for content extraction"))
        else:
            self.ai_readiness.append(("warn", "Limited heading structure (add more H2/H3 sections)"))

        # Statistics / data patterns
        has_stats = bool(re.search(r'\d+(\.\d+)?%', body_text))
        if has_stats:
            self.ai_readiness.append(("pass", "Statistics/percentages detected in content"))
        else:
            self.ai_readiness.append(("warn", "No statistics or data points detected (add data for AI citability)"))

    # -- Scoring ------------------------------------------------------------

    def calculate_score(self):
        """Calculate a score out of 100."""
        score = 100

        # Critical issues: -8 each
        score -= len(self.critical) * 8

        # Warnings: -3 each
        score -= len(self.warnings) * 3

        # AI readiness fails: -4 each
        ai_fails = [a for a in self.ai_readiness if a[0] == "fail"]
        score -= len(ai_fails) * 4

        # AI readiness warnings: -2 each
        ai_warns = [a for a in self.ai_readiness if a[0] == "warn"]
        score -= len(ai_warns) * 2

        return max(0, min(100, score))

    # -- Output -------------------------------------------------------------

    def format_report(self, verbose=False):
        """Format the audit as a human-readable report."""
        score = self.calculate_score()
        lines = []

        lines.append("")
        lines.append("=" * 51)
        lines.append("  SEO AUDIT REPORT: " + self.filename)
        lines.append("=" * 51)
        lines.append("")
        lines.append(f"  SCORE: {score}/100")
        lines.append("")

        # Critical
        if self.critical:
            lines.append("=== CRITICAL ISSUES (must fix) " + "=" * 20)
            for item in self.critical:
                lines.append(f"  X {item}")
            lines.append("")

        # Warnings
        if self.warnings:
            lines.append("=== WARNINGS " + "=" * 38)
            for item in self.warnings:
                lines.append(f"  ! {item}")
            lines.append("")

        # Passed
        if self.passed:
            lines.append("=== PASSED " + "=" * 40)
            for item in self.passed:
                lines.append(f"  + {item}")
            lines.append("")

        # Recommendations
        if self.recommendations:
            lines.append("=== RECOMMENDATIONS " + "=" * 31)
            for i, item in enumerate(self.recommendations, 1):
                lines.append(f"  {i}. {item}")
            lines.append("")

        # AI Search Readiness
        if self.ai_readiness:
            lines.append("=== AI SEARCH READINESS " + "=" * 27)
            for status, item in self.ai_readiness:
                if status == "pass":
                    lines.append(f"  + {item}")
                elif status == "fail":
                    lines.append(f"  X {item}")
                else:
                    lines.append(f"  ! {item}")
            lines.append("")

        # Verbose details
        if verbose:
            lines.append("=== DETAILED DATA " + "=" * 33)
            lines.append("")

            # Meta details
            meta = self.details.get("meta", {})
            lines.append("  -- Meta Tags --")
            lines.append(f"  Title: {meta.get('title', 'N/A')}")
            lines.append(f"  Title Length: {meta.get('title_length', 0)} chars")
            lines.append(f"  Description: {(meta.get('description') or 'N/A')[:100]}")
            lines.append(f"  Description Length: {meta.get('description_length', 0)} chars")
            lines.append(f"  Viewport: {meta.get('viewport', 'N/A')}")
            lines.append(f"  Canonical: {meta.get('canonical', 'N/A')}")
            lines.append(f"  Robots: {meta.get('robots', 'N/A')}")
            lines.append(f"  OG Tags: {meta.get('og_tags', {})}")
            lines.append(f"  Twitter Tags: {meta.get('twitter_tags', {})}")
            lines.append("")

            # Heading details
            headings = self.details.get("headings", {})
            lines.append("  -- Headings --")
            lines.append(f"  Total: {headings.get('total', 0)}")
            lines.append(f"  H1 Count: {headings.get('h1_count', 0)}")
            for level, text in headings.get("hierarchy", []):
                indent = "    " * (int(level[1]) - 1) if level[0] == "H" else "  "
                lines.append(f"  {indent}{level}: {text}")
            lines.append("")

            # Image details
            images = self.details.get("images", {})
            lines.append("  -- Images --")
            lines.append(f"  Total: {images.get('total', 0)}")
            lines.append(f"  Missing Alt: {images.get('missing_alt', 0)}")
            lines.append(f"  Missing Dimensions: {images.get('missing_dimensions', 0)}")
            lines.append(f"  Lazy Loaded: {images.get('lazy_loaded', 0)}")
            lines.append("")

            # Link details
            link_data = self.details.get("links", {})
            lines.append("  -- Links --")
            lines.append(f"  Internal: {link_data.get('internal', 0)}")
            lines.append(f"  External: {link_data.get('external', 0)}")
            lines.append(f"  Empty Text: {link_data.get('empty_text', 0)}")
            lines.append(f"  Nofollow: {link_data.get('nofollow', 0)}")
            lines.append("")

            # Schema details
            schema = self.details.get("schema", {})
            lines.append("  -- Schema --")
            lines.append(f"  Found: {schema.get('found', False)}")
            lines.append(f"  Types: {', '.join(schema.get('types', []))}")
            lines.append("")

            # Content details
            content = self.details.get("content", {})
            lines.append("  -- Content --")
            lines.append(f"  Word Count: {content.get('word_count', 0)}")
            lines.append(f"  Reading Time: ~{content.get('reading_time_minutes', 0)} min")
            lines.append("")

            # Keyword details
            if "keyword" in self.details:
                kw = self.details["keyword"]
                lines.append("  -- Keyword Analysis --")
                lines.append(f'  Keyword: "{kw.get("keyword")}"')
                lines.append(f"  Exact Matches: {kw.get('exact_matches', 0)}")
                lines.append(f"  Density: {kw.get('density_percent', 0)}%")
                lines.append(f"  In Title: {kw.get('in_title', False)}")
                lines.append(f"  In H1: {kw.get('in_h1', False)}")
                lines.append(f"  In Meta Desc: {kw.get('in_meta_description', False)}")
                lines.append(f"  In First 100 Words: {kw.get('in_first_100_words', False)}")
                lines.append("")

            # Performance details
            perf = self.details.get("performance", {})
            lines.append("  -- Performance --")
            lines.append(f"  Stylesheets: {perf.get('stylesheets', 0)}")
            lines.append(f"  Blocking CSS: {perf.get('blocking_css', 0)}")
            lines.append(f"  Scripts: {perf.get('scripts', 0)}")
            lines.append(f"  Blocking Scripts: {perf.get('blocking_scripts', 0)}")
            lines.append(f"  Inline Styles: {perf.get('inline_styles', 0)}")
            lines.append(f"  External Resources: {perf.get('external_resources', 0)}")
            lines.append("")

            # Accessibility details
            a11y = self.details.get("accessibility", {})
            lines.append("  -- Accessibility --")
            lines.append(f"  HTML Lang: {a11y.get('html_lang', 'N/A')}")
            lines.append(f"  Unlabeled Inputs: {a11y.get('unlabeled_inputs', 0)}")
            lines.append(f"  Skip Nav: {a11y.get('skip_nav', False)}")
            lines.append("")

        return "\n".join(lines)

    def to_json(self):
        """Return audit results as a JSON-serializable dict."""
        return {
            "file": self.filename,
            "score": self.calculate_score(),
            "critical": self.critical,
            "warnings": self.warnings,
            "passed": self.passed,
            "recommendations": self.recommendations,
            "ai_readiness": [
                {"status": s, "message": m} for s, m in self.ai_readiness
            ],
            "details": self.details,
        }


# ---------------------------------------------------------------------------
# File / URL handling
# ---------------------------------------------------------------------------

def read_html_file(filepath):
    """Read HTML content from a file."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def fetch_url(url):
    """Fetch HTML content from a URL using urllib."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (compatible; SEOScanner/1.0; "
            "+https://github.com/seo-scanner)"
        )
    }
    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=15) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(charset, errors="replace")
    except HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except URLError as e:
        print(f"URL Error: {e.reason}", file=sys.stderr)
        sys.exit(1)


def scan_html(html_content, filename="unknown", keyword=None):
    """Parse HTML and run SEO audit."""
    parser = SEOHTMLParser()
    try:
        parser.feed(html_content)
    except Exception as e:
        print(f"Error parsing {filename}: {e}", file=sys.stderr)
        return None

    audit = SEOAudit(parser, filename=filename, keyword=keyword)
    audit.run_all_checks()
    return audit


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="SEO Scanner - Comprehensive HTML SEO audit tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 seo-scanner.py index.html
  python3 seo-scanner.py ./site/
  python3 seo-scanner.py --url https://example.com
  python3 seo-scanner.py index.html --keyword "seo audit"
  python3 seo-scanner.py index.html --json
  python3 seo-scanner.py index.html --verbose
  python3 seo-scanner.py ./site/ --json --keyword "machine learning"
        """,
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="Path to an HTML file or directory of HTML files",
    )
    parser.add_argument(
        "--url",
        help="URL to fetch and scan",
    )
    parser.add_argument(
        "--keyword",
        help="Target keyword for density analysis",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output results as JSON",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed output per check",
    )

    args = parser.parse_args()

    if not args.path and not args.url:
        parser.print_help()
        sys.exit(1)

    audits = []

    # URL mode
    if args.url:
        html = fetch_url(args.url)
        audit = scan_html(html, filename=args.url, keyword=args.keyword)
        if audit:
            audits.append(audit)

    # File or directory mode
    elif args.path:
        target = args.path

        if os.path.isfile(target):
            html = read_html_file(target)
            audit = scan_html(
                html,
                filename=os.path.basename(target),
                keyword=args.keyword,
            )
            if audit:
                audits.append(audit)

        elif os.path.isdir(target):
            html_files = []
            for root, dirs, files in os.walk(target):
                for f in sorted(files):
                    if f.lower().endswith((".html", ".htm")):
                        html_files.append(os.path.join(root, f))

            if not html_files:
                print(f"No HTML files found in {target}", file=sys.stderr)
                sys.exit(1)

            print(f"Found {len(html_files)} HTML file(s) to scan...\n")

            for filepath in html_files:
                html = read_html_file(filepath)
                rel_path = os.path.relpath(filepath, target)
                audit = scan_html(
                    html,
                    filename=rel_path,
                    keyword=args.keyword,
                )
                if audit:
                    audits.append(audit)
        else:
            print(f"Path not found: {target}", file=sys.stderr)
            sys.exit(1)

    # Output
    if not audits:
        print("No audit results to display.", file=sys.stderr)
        sys.exit(1)

    if args.json_output:
        if len(audits) == 1:
            print(json.dumps(audits[0].to_json(), indent=2))
        else:
            results = [a.to_json() for a in audits]
            summary = {
                "files_scanned": len(results),
                "average_score": round(
                    sum(r["score"] for r in results) / len(results), 1
                ),
                "total_critical": sum(len(r["critical"]) for r in results),
                "total_warnings": sum(len(r["warnings"]) for r in results),
                "results": results,
            }
            print(json.dumps(summary, indent=2))
    else:
        for audit in audits:
            print(audit.format_report(verbose=args.verbose))

        # Summary for multi-file scans
        if len(audits) > 1:
            scores = [a.calculate_score() for a in audits]
            total_critical = sum(len(a.critical) for a in audits)
            total_warnings = sum(len(a.warnings) for a in audits)
            avg_score = round(sum(scores) / len(scores), 1)

            print("=" * 51)
            print("  SUMMARY")
            print("=" * 51)
            print(f"  Files scanned: {len(audits)}")
            print(f"  Average score: {avg_score}/100")
            print(f"  Total critical issues: {total_critical}")
            print(f"  Total warnings: {total_warnings}")
            print(f"  Lowest score: {min(scores)}/100")
            print(f"  Highest score: {max(scores)}/100")
            print("")


if __name__ == "__main__":
    main()
