# How Each AI Platform Picks Sources

Each AI search platform has its own search index, ranking logic, and content preferences. This guide covers what matters for getting cited on each one.

Sources cited throughout: Princeton GEO study (KDD 2024), SE Ranking domain authority study, ZipTie content-answer fit analysis.

---

## Contents
- [The Fundamentals](#the-fundamentals)
- [Google AI Overviews](#google-ai-overviews)
- [ChatGPT](#chatgpt)
- [Perplexity](#perplexity)
- [Microsoft Copilot](#microsoft-copilot)
- [Claude](#claude)
- [Allowing AI Bots in robots.txt](#allowing-ai-bots-in-robotstxt)
- [Where to Start](#where-to-start)

---

## The Fundamentals

Every AI platform shares three baseline requirements:

1. **Your content must be in their index** -- Each platform uses a different search backend (Google, Bing, Brave, or their own). If you're not indexed, you can't be cited.
2. **Your content must be crawlable** -- AI bots need access via robots.txt. Block the bot, lose the citation.
3. **Your content must be extractable** -- AI systems pull passages, not pages. Clear structure and self-contained paragraphs win.

Beyond these basics, each platform weights different signals. Here's what matters and where.

---

## Google AI Overviews

Google AI Overviews pull from Google's own index and lean heavily on E-E-A-T signals (Experience, Expertise, Authoritativeness, Trustworthiness). They appear in roughly 45% of Google searches.

### What Makes Google AI Overviews Different

They already have your traditional SEO signals -- backlinks, page authority, topical relevance. The additional AI layer adds a preference for content with cited sources and structured data. Research shows that including authoritative citations in your content correlates with a 132% visibility boost, and writing with an authoritative (not salesy) tone adds another 89%.

Importantly, AI Overviews don't just recycle the traditional Top 10. Only about 15% of AI Overview sources overlap with conventional organic results. Pages that wouldn't crack page 1 in traditional search can still get cited if they have strong structured data and clear, extractable answers.

### What to Focus On

- **Schema markup is the single biggest lever** -- Article, FAQPage, HowTo, and Product schemas give AI Overviews structured context to work with (30-40% visibility boost)
- Build topical authority through content clusters with strong internal linking
- Include named, sourced citations in your content (not just claims)
- Author bios with real credentials matter -- E-E-A-T is weighted heavily
- Get into Google's Knowledge Graph where possible (an accurate Wikipedia entry helps)
- Target "how to" and "what is" query patterns -- these trigger AI Overviews most often
- Ensure content has clear, extractable answer passages in the first paragraph of each section
- Use comparison tables for any content comparing options or alternatives

---

## ChatGPT

ChatGPT's web search draws from a Bing-based index. It combines this with its training knowledge to generate answers, then cites the web sources it relied on.

### What Makes ChatGPT Different

**Domain authority matters more here than on other AI platforms.** An SE Ranking analysis of 129,000 domains found that authority and credibility signals account for roughly 40% of what determines citation, with content quality at about 35% and platform trust at 25%. Sites with very high referring domain counts (350K+) average 8.4 citations per response, while sites with slightly lower trust scores (91-96 vs 97-100) drop from 8.4 to 6 citations.

**Freshness is a major differentiator.** Content updated within the last 30 days gets cited about 3.2x more often than older content. ChatGPT clearly favors recent information.

**The most important signal is content-answer fit.** A ZipTie analysis of 400,000 pages found that how well your content's style and structure matches ChatGPT's own response format accounts for about 55% of citation likelihood. This is far more important than domain authority (12%) or on-page structure (14%) alone. Write the way ChatGPT would answer the question, and you're more likely to be the source it cites.

### Where ChatGPT Looks Beyond Your Site

- Wikipedia accounts for 7.8% of all ChatGPT citations
- Reddit accounts for 1.8% of ChatGPT citations
- Forbes accounts for 1.1% of ChatGPT citations
- Brand official sites are cited frequently but third-party mentions carry significant weight

### What to Focus On

- Invest in backlinks and domain authority -- it's the strongest baseline signal
- Update competitive content at least monthly
- Structure your content the way ChatGPT structures its answers (conversational, direct, well-organized)
- Include verifiable statistics with named sources
- Clean heading hierarchy (H1 > H2 > H3) with descriptive headings
- Write in a direct, explanatory tone (match how ChatGPT responds)
- Ensure your content is indexed by Bing (submit to Bing Webmaster Tools)

---

## Perplexity

Perplexity always cites its sources with clickable links, making it the most transparent AI search platform. It combines its own index with Google's and runs results through multiple reranking passes -- initial relevance retrieval, then traditional ranking factor scoring, then ML-based quality evaluation that can discard entire result sets if they don't meet quality thresholds.

### What Makes Perplexity Different

It's the most "research-oriented" AI search engine, and its citation behavior reflects that. Perplexity maintains curated lists of authoritative domains (Amazon, GitHub, major academic sites) that get inherent ranking boosts. It uses a time-decay algorithm that evaluates new content quickly, giving fresh publishers a real shot at citation.

### Perplexity's Unique Content Preferences

- **FAQ Schema (JSON-LD)** -- Pages with FAQ structured data get cited noticeably more often. This is one of the strongest platform-specific signals.
- **PDF documents** -- Publicly accessible PDFs (whitepapers, research reports) are prioritized. If you have authoritative PDF content gated behind a form, consider making a version public.
- **Publishing velocity** -- How frequently you publish matters more than keyword targeting. Consistent, high-quality publishing builds domain trust.
- **Self-contained paragraphs** -- Perplexity prefers atomic, semantically complete paragraphs it can extract cleanly. Each paragraph should make sense on its own.
- **Multi-pass quality evaluation** -- Perplexity's ML reranker can discard entire result sets. If your content passes initial retrieval but fails quality evaluation, it won't be cited.

### What to Focus On

- Allow PerplexityBot in robots.txt
- Implement FAQPage schema on any page with Q&A content
- Host PDF resources publicly (whitepapers, guides, reports)
- Add Article schema with publication and modification timestamps
- Write in clear, self-contained paragraphs that work as standalone answers
- Build deep topical authority in your specific niche
- Publish consistently -- velocity matters on this platform
- Include named sources and specific data in every piece of content

---

## Microsoft Copilot

Copilot is embedded across Microsoft's ecosystem -- Edge, Windows, Microsoft 365, and Bing Search. It relies entirely on Bing's index, so if Bing hasn't indexed your content, Copilot can't cite it.

### What Makes Copilot Different

The Microsoft ecosystem connection creates unique optimization opportunities. Mentions and content on LinkedIn and GitHub provide ranking boosts that other platforms don't offer. Copilot also puts more weight on page speed -- sub-2-second load times are a clear threshold.

### What to Focus On

- **Submit your site to Bing Webmaster Tools** -- Many sites only submit to Google Search Console. If you're not in Bing's index, Copilot can't find you.
- **Use IndexNow protocol** for faster indexing of new and updated content. IndexNow is supported by Bing and allows instant notification of content changes.
- **Optimize page speed to under 2 seconds** -- Copilot weights this more heavily than other platforms.
- **Write clear entity definitions** -- When your content defines a term or concept, make the definition explicit and extractable.
- **Build presence on LinkedIn** -- Publish articles, maintain an active company page. LinkedIn content carries extra weight in the Microsoft ecosystem.
- **Build presence on GitHub** if relevant -- Open source projects, documentation, and technical content on GitHub get ranking boosts.
- **Ensure Bingbot has full crawl access** -- Check robots.txt specifically for Bingbot rules.

---

## Claude

Claude uses Brave Search as its search backend when web search is enabled -- not Google, not Bing. This is a completely different index, which means your Brave Search visibility directly determines whether Claude can find and cite you.

### What Makes Claude Different

Claude is extremely selective about what it cites. While it processes enormous amounts of content, its citation rate is very low -- it's looking for the most factually accurate, well-sourced content on a given topic. Data-rich content with specific numbers and clear attribution performs significantly better than general-purpose content.

### What to Focus On

- **Verify your content appears in Brave Search results** -- Search for your brand and key terms at search.brave.com. If you don't appear there, Claude can't find you through web search.
- **Allow ClaudeBot and anthropic-ai user agents in robots.txt** -- These are the two user agents Anthropic uses for crawling.
- **Maximize factual density** -- Specific numbers, named sources, dated statistics. Claude rewards precision over volume.
- **Use clear, extractable structure with descriptive headings** -- Claude looks for content it can pull clean passages from.
- **Cite authoritative sources within your content** -- Don't just make claims; back them up with named sources.
- **Aim to be the most factually accurate source on your topic** -- Claude rewards precision. If there are two articles on the same topic, the one with more specific, verifiable data is more likely to be cited.
- **Include publication and update dates** -- Freshness signals help across all platforms, including Claude.

---

## Allowing AI Bots in robots.txt

If your robots.txt blocks an AI bot, that platform can't cite your content. Here are the user agents to allow:

```
User-agent: GPTBot           # OpenAI -- powers ChatGPT search
User-agent: ChatGPT-User     # ChatGPT browsing mode
User-agent: PerplexityBot    # Perplexity AI search
User-agent: ClaudeBot        # Anthropic Claude
User-agent: anthropic-ai     # Anthropic Claude (alternate)
User-agent: Google-Extended   # Google Gemini and AI Overviews
User-agent: Bingbot          # Microsoft Copilot (via Bing)
Allow: /
```

### Training vs. Search

Some AI bots are used for both model training and search citation. If you want to be cited but don't want your content used for training, your options are limited -- GPTBot handles both for OpenAI. However, you can safely block **CCBot** (Common Crawl) without affecting any AI search citations, since it's only used for training dataset collection.

**Safe to block (training only, no search impact):**
```
User-agent: CCBot
Disallow: /
```

**Do NOT block if you want AI citations:**
```
# These bots power search/citation -- blocking them prevents citation
GPTBot, ChatGPT-User, PerplexityBot, ClaudeBot, anthropic-ai, Google-Extended, Bingbot
```

---

## Where to Start

If you're optimizing for AI search for the first time, focus your effort where your audience actually is.

### Priority 1: Google AI Overviews

They reach the most users (45%+ of Google searches) and you likely already have Google SEO foundations in place.

**Actions:**
1. Add schema markup (Article, FAQPage, HowTo, Product as appropriate)
2. Include cited sources in your content
3. Strengthen E-E-A-T signals (author bios, credentials, original data)
4. Structure content with clear heading hierarchy and extractable answer passages

### Priority 2: ChatGPT

The most-used standalone AI search tool, especially for tech and business audiences.

**Actions:**
1. Ensure you're indexed in Bing (submit to Bing Webmaster Tools)
2. Update competitive content at least monthly
3. Build domain authority through quality backlinks
4. Structure content the way ChatGPT formats its responses

### Priority 3: Perplexity

Especially valuable if your audience includes researchers, early adopters, or tech professionals.

**Actions:**
1. Allow PerplexityBot in robots.txt
2. Add FAQ schema to pages with Q&A content
3. Publish PDF resources publicly
4. Write in clear, self-contained paragraphs

### Lower Priority: Copilot and Claude

Address these after the first three unless your audience skews enterprise/Microsoft (Copilot) or developer/analyst (Claude).

### Actions That Help Everywhere

These optimizations improve citation likelihood across all AI platforms:

1. Allow all AI bots in robots.txt
2. Implement schema markup (FAQPage, Article, Organization at minimum)
3. Include statistics with named sources in your content
4. Update content regularly -- monthly for competitive topics
5. Use clear heading structure (H1 > H2 > H3)
6. Keep page load time under 2 seconds
7. Add author bios with credentials
8. Write self-contained paragraphs that work as standalone answers
9. Use comparison tables instead of prose for "vs" content
10. Include "last updated" dates on all content
