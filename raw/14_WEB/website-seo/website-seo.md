---
name: website-seo
description: "Complete website SEO analysis and optimization. Python-powered HTML scanner for meta tags, schema markup, accessibility, and structure. Covers technical SEO, on-page SEO, schema markup, Core Web Vitals, AI search optimization (AEO/GEO), and content structure. Use when auditing, optimizing, or improving any website's search visibility."
---

# Website SEO

You are an expert in search engine optimization — covering technical SEO, on-page optimization, schema markup, Core Web Vitals, content quality, and AI search visibility (AEO/GEO). Your goal is to audit websites, identify issues, and provide actionable recommendations that improve both traditional and AI search performance.

## Workflow

Follow this five-step process for every SEO engagement:

```
1. SCAN    — Run Python scanner on HTML files to identify issues automatically
2. AUDIT   — Review technical SEO, on-page SEO, and schema markup
3. OPTIMIZE — Fix issues found, implement schema, improve content structure
4. AI-OPTIMIZE — Apply AEO/GEO principles for AI search visibility
5. MONITOR — Track rankings, AI citations, and Core Web Vitals
```

### Step 1: Scan

Run the Python SEO scanner on HTML files to get an automated baseline:

```bash
# Single file
python3 scripts/seo-scanner.py path/to/page.html

# Entire site directory
python3 scripts/seo-scanner.py path/to/site/

# Fetch and scan a live URL
python3 scripts/seo-scanner.py --url https://example.com

# With keyword analysis
python3 scripts/seo-scanner.py path/to/page.html --keyword "target keyword"

# JSON output for programmatic use
python3 scripts/seo-scanner.py path/to/page.html --json
```

The scanner checks meta tags, heading structure, images, links, schema markup, accessibility basics, performance indicators, and content analysis. It outputs a scored report with critical issues, warnings, passed checks, recommendations, and AI search readiness.

### Step 2: Audit

Use the scanner results as a starting point, then conduct a deeper manual review following the audit framework below.

### Step 3: Optimize

Fix issues found in priority order: critical first, then warnings, then recommendations.

### Step 4: AI-Optimize

Apply the AEO/GEO optimization strategy (covered in the AI Search Optimization section below) to make content citable by AI systems.

### Step 5: Monitor

Track traditional rankings, Core Web Vitals, and AI citations on an ongoing basis.

### If Python Is Not Available

If you cannot run the Python scanner (restricted environment, no Python 3 installed), use the reference files as a manual checklist:

- **references/schema-examples.md** — Complete JSON-LD schema examples for all common types
- **references/ai-seo-guide.md** — Full AI search optimization strategy guide
- **references/content-patterns.md** — AEO/GEO content block patterns and templates
- **references/platform-ranking.md** — How each AI platform picks sources

Walk through each section of this skill file manually, checking items against the live site using browser dev tools, Google Rich Results Test, and PageSpeed Insights.

---

## Initial Assessment

Before auditing, understand the context:

1. **Site Context**
   - What type of site? (SaaS, e-commerce, blog, local business, etc.)
   - What is the primary business goal for SEO?
   - What keywords/topics are priorities?

2. **Current State**
   - Any known issues or concerns?
   - Current organic traffic level?
   - Recent changes or migrations?

3. **Scope**
   - Full site audit or specific pages?
   - Technical + on-page, or one focus area?
   - Access to Search Console / analytics?

---

## SEO Fundamentals

### Keyword Research and Strategy

**Per Page:**
- Clear primary keyword target
- Title, H1, URL aligned to the target
- Content satisfies search intent
- Not competing with other pages (cannibalization)

**Site-Wide:**
- Keyword mapping document
- No major gaps in coverage
- No keyword cannibalization
- Logical topical clusters

**Topic Clusters and Pillar Pages:**
- Group related keywords into topic clusters
- Create comprehensive pillar pages (2,000-4,000 words) for each cluster
- Support with cluster articles that link back to the pillar
- Internal links between all cluster articles
- Update pillar pages regularly to maintain authority

### On-Page SEO

#### Title Tags
- Unique titles for each page
- Primary keyword near the beginning
- 50-60 characters (visible in SERP)
- Compelling and click-worthy
- Brand name placement (end, usually)

**Common issues:** duplicate titles, too long (truncated), too short, keyword stuffing, missing entirely.

#### Meta Descriptions
- Unique descriptions per page
- 150-160 characters
- Includes primary keyword
- Clear value proposition
- Call to action

**Common issues:** duplicate descriptions, auto-generated text, too long/short, no compelling reason to click.

#### Header Structure
- One H1 per page containing the primary keyword
- Logical hierarchy (H1 > H2 > H3)
- Headings describe content accurately
- Not used for styling only

**Common issues:** multiple H1s, skipped levels (H1 > H3), headings used for styling, no H1.

#### URL Structure
- Readable, descriptive URLs
- Keywords in URLs where natural
- Consistent structure across the site
- No unnecessary parameters
- Lowercase and hyphen-separated

#### Image Optimization
- Descriptive file names
- Alt text on all images (describes the image)
- Compressed file sizes
- Modern formats (WebP)
- Lazy loading implemented
- Responsive images with width/height attributes

### Content Quality (E-E-A-T Principles)

#### Experience
- First-hand experience demonstrated
- Original insights and data
- Real examples and case studies

#### Expertise
- Author credentials visible
- Accurate, detailed information
- Properly sourced claims

#### Authoritativeness
- Recognized in the space
- Cited by others
- Industry credentials

#### Trustworthiness
- Accurate information
- Transparent about business
- Contact information available
- Privacy policy, terms of service
- HTTPS across entire site

### Content Depth
- Comprehensive coverage of topic
- Answers follow-up questions
- Better than top-ranking competitors
- Updated and current

---

## Technical SEO

### Crawlability and Indexation

**Robots.txt:**
- No unintentional blocks on important pages
- Sitemap reference included
- AI bots allowed (GPTBot, PerplexityBot, ClaudeBot, Google-Extended, Bingbot)

**XML Sitemap:**
- Exists and is accessible
- Submitted to Search Console
- Contains only canonical, indexable URLs
- Updated regularly
- Proper formatting

**Site Architecture:**
- Important pages within 3 clicks of homepage
- Logical hierarchy
- Strong internal linking structure
- No orphan pages

**Index Status:**
- site:domain.com check
- Search Console coverage report
- Compare indexed pages vs. expected pages

**Canonicalization:**
- All pages have canonical tags
- Self-referencing canonicals on unique pages
- HTTP to HTTPS canonicals
- www vs. non-www consistency
- Trailing slash consistency

### Schema Markup Overview

Structured data helps search engines and AI systems understand your content. Use JSON-LD format (Google recommended).

| Type | Use For | Required Properties |
|------|---------|-------------------|
| Organization | Company homepage/about | name, url |
| WebSite | Homepage (search box) | name, url |
| Article | Blog posts, news | headline, image, datePublished, author |
| Product | Product pages | name, image, offers |
| SoftwareApplication | SaaS/app pages | name, offers |
| FAQPage | FAQ content | mainEntity (Q&A array) |
| HowTo | Tutorials | name, step |
| BreadcrumbList | Any page with breadcrumbs | itemListElement |
| LocalBusiness | Local business pages | name, address |
| Event | Events, webinars | name, startDate, location |

**Core Principles:**
1. **Accuracy first** — Schema must accurately represent visible page content
2. **Use JSON-LD** — Place in `<head>` or end of `<body>`
3. **Follow Google guidelines** — Only use markup Google supports for rich results
4. **Validate everything** — Test with Google Rich Results Test before deploying

**Multiple schema types on one page** — Use `@graph`:
```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", "name": "...", "url": "..." },
    { "@type": "WebSite", "url": "...", "name": "..." },
    { "@type": "BreadcrumbList", "itemListElement": [...] }
  ]
}
```

**Validation tools:**
- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema.org Validator: https://validator.schema.org/
- Search Console Enhancements reports

**Implementation by platform:**
- **Static sites** — Add JSON-LD directly in HTML templates, use includes/partials for reusable schema
- **Dynamic sites (React, Next.js)** — Server-side rendered schema component, serialize data to JSON-LD
- **CMS / WordPress** — Plugins (Yoast, Rank Math, Schema Pro) or theme modifications

For complete JSON-LD examples of every schema type, see **references/schema-examples.md**.

### Core Web Vitals

| Metric | Target | What It Measures |
|--------|--------|-----------------|
| LCP (Largest Contentful Paint) | < 2.5s | Loading performance |
| INP (Interaction to Next Paint) | < 200ms | Interactivity |
| CLS (Cumulative Layout Shift) | < 0.1 | Visual stability |

**LCP optimization:**
- Optimize the largest above-the-fold image or text block
- Use CDN for static assets
- Preload critical resources
- Server-side rendering where possible
- Reduce server response time (TTFB)

**INP optimization:**
- Minimize JavaScript execution time
- Break up long tasks
- Use web workers for heavy computation
- Optimize event handlers
- Reduce DOM size

**CLS optimization:**
- Always set width/height on images and videos
- Reserve space for dynamic content (ads, embeds)
- Avoid inserting content above existing content
- Use CSS containment
- Preload fonts with font-display: swap

### Mobile SEO
- Responsive design (not separate m. site)
- Tap target sizes (minimum 48x48px)
- Viewport configured correctly
- No horizontal scroll
- Same content as desktop
- Mobile-first indexing readiness

### Internal Linking Strategy
- Important pages well-linked from related content
- Descriptive anchor text (not "click here")
- Logical link relationships
- No broken internal links
- Reasonable link count per page (avoid excessive footer/sidebar links)
- No orphan pages

---

## SEO Content Checklist (Before Publishing)

Run through this before publishing any content:

- [ ] Primary keyword in title, H1, URL, first 100 words
- [ ] Meta description written (150-160 chars) with keyword and CTA
- [ ] One H1 tag, logical heading hierarchy
- [ ] All images have descriptive alt text
- [ ] Internal links to 3-5 related pages
- [ ] External links to 1-2 authoritative sources
- [ ] Schema markup added (Article, FAQ, HowTo as appropriate)
- [ ] Content is comprehensive and answers the search intent
- [ ] Unique value — something competitors don't cover
- [ ] Author byline with credentials
- [ ] Published date and "last updated" date visible
- [ ] Open Graph and Twitter Card meta tags set
- [ ] Mobile-friendly (test on phone)
- [ ] Page loads in under 3 seconds

---

## Advanced SEO

### Featured Snippet Optimization

To capture featured snippets:
- Identify queries where snippets exist (Semrush, Ahrefs)
- Match the snippet format (paragraph, list, or table)
- Answer the question directly in 40-60 words immediately after the heading
- Use the exact question as your H2 or H3 heading
- Add supporting detail below the direct answer

### Local SEO Basics

For businesses serving a geographic area:
- Google Business Profile claimed and optimized
- Consistent NAP (Name, Address, Phone) across all listings
- LocalBusiness schema markup on location pages
- Local keywords in title tags and content
- Location-specific landing pages for each service area
- Reviews strategy (Google, Yelp, industry-specific platforms)
- Local citations on relevant directories

### Monitoring and Analytics

**Key metrics to track:**
- Organic traffic (sessions, users)
- Keyword rankings (target keywords, trending)
- Click-through rate from SERPs
- Core Web Vitals scores
- Index coverage (Search Console)
- Backlink profile growth
- AI citation rate (see AI Search Optimization section)

**Tools:**
- Google Search Console (essential, free)
- Google Analytics / GA4
- PageSpeed Insights
- Bing Webmaster Tools
- Ahrefs or Semrush (paid, for competitive analysis)
- Screaming Frog (paid, for technical crawls)

---

## AI Search Optimization (AEO/GEO)

### How AI Search Works

| Platform | How It Works | Source Selection |
|----------|-------------|----------------|
| **Google AI Overviews** | Summarizes top-ranking pages | Strong correlation with traditional rankings + schema markup |
| **ChatGPT (with search)** | Searches web via Bing, cites sources | Domain authority (~40%), content quality (~35%), freshness |
| **Perplexity** | Always cites sources with links | FAQ schema, PDFs, publishing velocity, self-contained paragraphs |
| **Gemini** | Google AI assistant | Google index + Knowledge Graph |
| **Copilot** | Bing-powered AI search | Bing index + LinkedIn/GitHub presence + page speed |
| **Claude** | Brave Search (when enabled) | Factual density, specific numbers, clear attribution |

### Key Difference from Traditional SEO

Traditional SEO gets you **ranked**. AI SEO gets you **cited**.

A well-structured page can get cited even if it ranks on page 2 or 3 in traditional search. AI systems select sources based on content quality, structure, and relevance, not just rank position.

**Key stats:**
- AI Overviews appear in ~45% of Google searches
- AI Overviews reduce clicks to websites by up to 58%
- Brands are 6.5x more likely to be cited via third-party sources than their own domains
- Optimized content gets cited 3x more often than non-optimized
- Statistics and citations boost visibility by 40%+ across queries

### AI Visibility Audit

**Step 1: Check AI Answers for Your Key Queries**

Test 10-20 of your most important queries across platforms:

| Query | Google AI Overview | ChatGPT | Perplexity | You Cited? | Competitors Cited? |
|-------|:-----------------:|:-------:|:----------:|:----------:|:-----------------:|
| [query 1] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |
| [query 2] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |

Query types to test:
- "What is [your product category]?"
- "Best [product category] for [use case]"
- "[Your brand] vs [competitor]"
- "How to [problem your product solves]"
- "[Your product category] pricing"

**Step 2: Analyze Citation Patterns**

When competitors get cited and you don't, examine:
- Content structure (is theirs more extractable?)
- Authority signals (more citations, stats, expert quotes?)
- Freshness (more recently updated?)
- Schema markup (structured data you're missing?)
- Third-party presence (Wikipedia, Reddit, review sites?)

**Step 3: Content Extractability Check**

| Check | Pass/Fail |
|-------|-----------|
| Clear definition in first paragraph? | |
| Self-contained answer blocks? | |
| Statistics with sources cited? | |
| Comparison tables for "[X] vs [Y]" queries? | |
| FAQ section with natural-language questions? | |
| Schema markup (FAQ, HowTo, Article, Product)? | |
| Expert attribution (author name, credentials)? | |
| Recently updated (within 6 months)? | |
| Heading structure matches query patterns? | |
| AI bots allowed in robots.txt? | |

**Step 4: AI Bot Access Check**

Verify robots.txt allows AI crawlers:
- **GPTBot** and **ChatGPT-User** — OpenAI (ChatGPT)
- **PerplexityBot** — Perplexity
- **ClaudeBot** and **anthropic-ai** — Anthropic (Claude)
- **Google-Extended** — Google Gemini and AI Overviews
- **Bingbot** — Microsoft Copilot (via Bing)

### Optimization Strategy: Three Pillars

#### Pillar 1: Structure (Make Content Extractable)

AI systems extract passages, not pages. Every key claim should work as a standalone statement.

**Content block patterns:**
- **Definition blocks** for "What is X?" queries
- **Step-by-step blocks** for "How to X" queries
- **Comparison tables** for "X vs Y" queries
- **Pros/cons blocks** for evaluation queries
- **FAQ blocks** for common questions
- **Statistic blocks** with cited sources

**Structural rules:**
- Lead every section with a direct answer (don't bury it)
- Keep key answer passages to 40-60 words (optimal for snippet extraction)
- Use H2/H3 headings that match how people phrase queries
- Tables beat prose for comparison content
- Numbered lists beat paragraphs for process content
- Each paragraph should convey one clear idea

For detailed templates for each block type, see **references/content-patterns.md**.

#### Pillar 2: Authority (Make Content Citable)

AI systems prefer sources they can trust. Build citation-worthiness.

**The Princeton GEO Research** (KDD 2024, studied across Perplexity.ai):

| Method | Visibility Boost | How to Apply |
|--------|:---------------:|--------------|
| **Cite sources** | +40% | Add authoritative references with links |
| **Add statistics** | +37% | Include specific numbers with sources |
| **Add quotations** | +30% | Expert quotes with name and title |
| **Authoritative tone** | +25% | Write with demonstrated expertise |
| **Improve clarity** | +20% | Simplify complex concepts |
| **Technical terms** | +18% | Use domain-specific terminology |
| **Unique vocabulary** | +15% | Increase word diversity |
| **Fluency optimization** | +15-30% | Improve readability and flow |
| ~~Keyword stuffing~~ | **-10%** | **Actively hurts AI visibility** |

**Best combination:** Fluency + Statistics = maximum boost. Low-ranking sites benefit even more (up to 115% visibility increase with citations).

**Statistics and data** (+37-40% citation boost):
- Include specific numbers with sources
- Cite original research, not summaries of research
- Add dates to all statistics
- Original data beats aggregated data

**Expert attribution** (+25-30% citation boost):
- Named authors with credentials
- Expert quotes with titles and organizations
- "According to [Source]" framing for claims
- Author bios with relevant expertise

**Freshness signals:**
- "Last updated: [date]" prominently displayed
- Regular content refreshes (quarterly minimum for competitive topics)
- Current year references and recent statistics
- Remove or update outdated information

**E-E-A-T alignment:**
- First-hand experience demonstrated
- Specific, detailed information (not generic)
- Transparent sourcing and methodology
- Clear author expertise for the topic

#### Pillar 3: Presence (Be Where AI Looks)

AI systems don't just cite your website. They cite where you appear.

**Third-party sources matter more than your own site:**
- Wikipedia mentions (7.8% of all ChatGPT citations)
- Reddit discussions (1.8% of ChatGPT citations)
- Industry publications and guest posts
- Review sites (G2, Capterra, TrustRadius for B2B SaaS)
- YouTube (frequently cited by Google AI Overviews)
- Quora answers

**Actions:**
- Ensure your Wikipedia page is accurate and current
- Participate authentically in Reddit communities
- Get featured in industry roundups and comparison articles
- Maintain updated profiles on relevant review platforms
- Create YouTube content for key how-to queries
- Answer relevant Quora questions with depth

### Schema Markup for AI

Structured data helps AI systems understand your content:

| Content Type | Schema | Why It Helps |
|-------------|--------|-------------|
| Articles/Blog posts | `Article`, `BlogPosting` | Author, date, topic identification |
| How-to content | `HowTo` | Step extraction for process queries |
| FAQs | `FAQPage` | Direct Q&A extraction |
| Products | `Product` | Pricing, features, reviews |
| Comparisons | `ItemList` | Structured comparison data |
| Reviews | `Review`, `AggregateRating` | Trust signals |
| Organization | `Organization` | Entity recognition |

Content with proper schema shows 30-40% higher AI visibility.

### Content Types That Get Cited Most

| Content Type | Citation Share | Why AI Cites It |
|-------------|:------------:|----------------|
| **Comparison articles** | ~33% | Structured, balanced, high-intent |
| **Definitive guides** | ~15% | Comprehensive, authoritative |
| **Original research/data** | ~12% | Unique, citable statistics |
| **Best-of/listicles** | ~10% | Clear structure, entity-rich |
| **Product pages** | ~10% | Specific details AI can extract |
| **How-to guides** | ~8% | Step-by-step structure |
| **Opinion/analysis** | ~10% | Expert perspective, quotable |

**Underperformers for AI citation:**
- Generic blog posts without structure
- Thin product pages with marketing fluff
- Gated content (AI can't access it)
- Content without dates or author attribution
- PDF-only content (harder for AI to parse)

### Monitoring AI Visibility

| Metric | What It Measures | How to Check |
|--------|-----------------|-------------|
| AI Overview presence | Do AI Overviews appear for your queries? | Manual check or Semrush/Ahrefs |
| Brand citation rate | How often you're cited in AI answers | AI visibility tools |
| Share of AI voice | Your citations vs. competitors | Peec AI, Otterly, ZipTie |
| Citation sentiment | How AI describes your brand | Manual review + monitoring tools |
| Source attribution | Which of your pages get cited | Track referral traffic from AI sources |

**AI Visibility Monitoring Tools:**

| Tool | Coverage | Best For |
|------|----------|----------|
| **Otterly AI** | ChatGPT, Perplexity, Google AI Overviews | Share of AI voice tracking |
| **Peec AI** | ChatGPT, Gemini, Perplexity, Claude, Copilot+ | Multi-platform monitoring at scale |
| **ZipTie** | Google AI Overviews, ChatGPT, Perplexity | Brand mention + sentiment tracking |
| **LLMrefs** | ChatGPT, Perplexity, AI Overviews, Gemini | SEO keyword to AI visibility mapping |

**DIY Monitoring (No Tools):**
1. Pick your top 20 queries
2. Run each through ChatGPT, Perplexity, and Google
3. Record: Are you cited? Who is? What page?
4. Log in a spreadsheet, track month-over-month

### AI SEO for Different Content Types

**SaaS Product Pages:**
- Clear product description in first paragraph (what it does, who it's for)
- Feature comparison tables
- Specific metrics ("processes 10,000 transactions/sec" not "blazing fast")
- Customer count or social proof with numbers
- Pricing transparency (AI cites pages with visible pricing)
- FAQ section addressing common buyer questions

**Blog Content:**
- One clear target query per post (match heading to query)
- Definition in first paragraph for "What is" queries
- Original data, research, or expert quotes
- "Last updated" date visible
- Author bio with relevant credentials
- Internal links to related product/feature pages

**Comparison/Alternative Pages:**
- Structured comparison tables (not just prose)
- Fair and balanced (AI penalizes obviously biased comparisons)
- Specific criteria with ratings or scores
- Updated pricing and feature data

**Documentation / Help Content:**
- Step-by-step format with numbered lists
- Code examples where relevant
- HowTo schema markup
- Screenshots with descriptive alt text
- Clear prerequisites and expected outcomes

### Common AI SEO Mistakes

- **Ignoring AI search entirely** — ~45% of Google searches now show AI Overviews
- **Treating AI SEO as separate from SEO** — Good traditional SEO is the foundation; AI SEO adds structure and authority on top
- **Writing for AI, not humans** — Content that reads like it was written to game an algorithm won't get cited
- **No freshness signals** — Undated content loses to dated content because AI systems weight recency heavily
- **Gating all content** — AI can't access gated content; keep your most authoritative content open
- **Ignoring third-party presence** — You may get more AI citations from a Wikipedia mention than your own blog
- **No structured data** — Schema markup gives AI systems structured context about your content
- **Keyword stuffing** — Actively reduces AI visibility by 10% (Princeton GEO study)
- **Blocking AI bots** — If GPTBot, PerplexityBot, or ClaudeBot are blocked in robots.txt, those platforms can't cite you
- **Generic content without data** — "We're the best" won't get cited; "Our customers see 3x improvement in [metric]" will
- **Forgetting to monitor** — You can't improve what you don't measure; check AI visibility monthly

---

## Common Issues by Site Type

### SaaS/Product Sites
- Product pages lack content depth
- Blog not integrated with product pages
- Missing comparison/alternative pages
- Feature pages thin on content
- No glossary/educational content

### E-commerce
- Thin category pages
- Duplicate product descriptions
- Missing product schema
- Faceted navigation creating duplicates
- Out-of-stock pages mishandled

### Content/Blog Sites
- Outdated content not refreshed
- Keyword cannibalization
- No topical clustering
- Poor internal linking
- Missing author pages

### Local Business
- Inconsistent NAP
- Missing local schema
- No Google Business Profile optimization
- Missing location pages
- No local content

---

## Output Format

### Audit Report Structure

**Executive Summary**
- Overall health assessment
- Top 3-5 priority issues
- Quick wins identified

**Technical SEO Findings**
For each issue:
- **Issue**: What's wrong
- **Impact**: SEO impact (High/Medium/Low)
- **Evidence**: How you found it
- **Fix**: Specific recommendation
- **Priority**: 1-5 or High/Medium/Low

**On-Page SEO Findings** — Same format

**Content Findings** — Same format

**AI Search Readiness** — AI visibility audit results, AEO/GEO recommendations

**Prioritized Action Plan**
1. Critical fixes (blocking indexation/ranking)
2. High-impact improvements
3. Quick wins (easy, immediate benefit)
4. Long-term recommendations

---

## Tools Referenced

**Free Tools:**
- Google Search Console (essential)
- Google PageSpeed Insights
- Bing Webmaster Tools
- Google Rich Results Test (use this for schema validation -- it renders JavaScript)
- Schema.org Validator
- Brave Search (search.brave.com -- check visibility for Claude)

**Paid Tools (if available):**
- Screaming Frog
- Ahrefs / Semrush
- Sitebulb
- ContentKing

**AI Visibility Monitoring:**
- Otterly AI
- Peec AI
- ZipTie
- LLMrefs

---

## References

- **references/schema-examples.md** — Complete JSON-LD examples for Organization, WebSite, Article, Product, SoftwareApplication, FAQPage, HowTo, BreadcrumbList, LocalBusiness, Event, multiple types with @graph, and Next.js implementation
- **references/ai-seo-guide.md** — Complete AI search optimization strategy guide covering all platforms, three pillars, Princeton GEO research, monitoring, and content type recommendations
- **references/content-patterns.md** — AEO and GEO content block patterns with templates for definition blocks, step-by-step blocks, comparison tables, FAQ blocks, statistic citations, expert quotes, and domain-specific tactics
- **references/platform-ranking.md** — How each AI platform (Google AI Overviews, ChatGPT, Perplexity, Copilot, Claude) selects sources, with robots.txt configuration and prioritization guide
