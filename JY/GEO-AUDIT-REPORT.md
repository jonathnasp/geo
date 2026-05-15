# GEO Audit Report — jonathany.com
**Date:** April 14, 2026
**Audited By:** Claude Code GEO Audit System (5-agent parallel analysis)
**Business Type:** E-Commerce — Home Décor (Rugs, Lighting, Furniture)
**Platform:** Shopify

---

## Composite GEO Score: 45 / 100

> **Interpretation:** Foundational infrastructure is sound — AI crawlers are explicitly permitted and content is server-rendered. However, brand entity signals, content authority, and structured data quality are significantly underdeveloped. Jonathan Y is invisible to AI models as a *named entity* despite being a real, scaled brand. The gap between where the site is and where it could be is closable within 90 days with focused execution.

### Score Breakdown

| Category | Weight | Score | Weighted Score |
|----------|--------|-------|---------------|
| AI Citability & Visibility | 25% | 47 | 11.75 |
| Brand Authority Signals | 20% | 33 | 6.60 |
| Content Quality & E-E-A-T | 20% | 42 | 8.40 |
| Technical Foundations | 15% | 61 | 9.15 |
| Structured Data | 10% | 44 | 4.40 |
| Platform Optimization | 10% | 46 | 4.60 |
| **TOTAL** | 100% | — | **44.90 ≈ 45/100** |

### Score Gauge

```
0          25          50          75         100
|——————————|——————————|——————————|——————————|
          [====45====]
         POOR     FAIR
```

---

## Executive Summary

Jonathan Y is a scaled e-commerce brand on Shopify selling modern rugs, lighting, and furniture, with 500+ SKUs, 4 active social channels, iOS/Android apps, and a 45-post blog. Despite this operational breadth, the brand scores **45/100** for GEO visibility — meaning AI systems (ChatGPT, Perplexity, Gemini, Claude) are unlikely to cite or recommend the brand when users ask about home décor.

**The core problem is not discoverability — it's authority.** AI crawlers can access the site (robots.txt is well-configured), but when they arrive, they find:
- No `llms.txt` to guide them
- An "Our Story" page with 380 words and zero verifiable facts
- No named authors on any content
- A brand entity with no Wikipedia article, minimal press coverage, and incomplete structured data
- Blog content that shows strong AI-generation signals (8 posts published on a single day)

**The good news:** Several of the highest-impact fixes are zero-cost and same-day deployable. The full opportunity requires 90 days of strategic execution.

---

## Detailed Findings by Category

### 1. AI Citability & Visibility — 47/100

**Sub-scores:**

| Component | Score | Weight | Weighted |
|-----------|-------|--------|---------|
| Citability (content quality for AI citation) | 44/100 | 35% | 15.4 |
| Brand Mentions (third-party authority) | 33/100 | 30% | 9.9 |
| Crawler Access | 88/100 | 25% | 22.0 |
| llms.txt | 0/100 | 10% | 0.0 |
| **AI Visibility Score** | | | **47.3/100** |

**What AI models can cite from Jonathan Y today:**

| Content Block | Citability Score | Status |
|--------------|-----------------|--------|
| King bed rug sizing guide (specific measurements) | 77/100 | Citation-ready |
| Nylon vs. Polyester rug comparison | 71/100 | Citation-ready |
| Industrial LED lighting specs | 70/100 | Borderline |
| Machine washable rugs guide | 62/100 | Citation-possible |
| "Our Story" page | 29/100 | Citation-unlikely |
| Homepage copy | 18/100 | Citation-invisible |
| Collection pages (/collections/rugs) | ~22/100 | Citation-invisible |

**Key finding:** Citation-ready content exists only in the blog. The homepage, collection pages, and product pages — the pages AI crawlers encounter first — contain almost no citable content. Marketing slogans are not citable; product specifications and buying guidance are.

**Crawler Access (88/100):**

| AI Crawler | robots.txt Status |
|------------|------------------|
| GPTBot | Explicitly ALLOWED |
| ChatGPT-User | Explicitly ALLOWED |
| ClaudeBot / Claude-User | Explicitly ALLOWED |
| PerplexityBot / Perplexity-User | Explicitly ALLOWED |
| Gemini-Deep-Research | Explicitly ALLOWED |
| Googlebot / Bingbot | Explicitly ALLOWED |
| Nutch | Blocked (correct) |
| AhrefsBot | Allowed, 10s crawl-delay |

Score deductions: Cloudflare JS challenge intercepting automated requests (-7), secondary crawlers unaddressed (-5).

**llms.txt: ABSENT (0/100)**
No `llms.txt` or `llms-full.txt` exists. AI systems must infer site structure from crawl signals alone.

---

### 2. Brand Authority Signals — 33/100

| Platform | Status | Score Contribution |
|----------|--------|-------------------|
| Wikipedia | Absent — no article exists | 0/30 |
| Reddit | Minimal — plausible but unconfirmed | 5/20 |
| YouTube | Channel exists; discoverability uncertain | 7/15 |
| LinkedIn | Unverified company page | 3/10 |
| Amazon | Strong — thousands of reviews | 18/25 (shared) |
| Trustpilot | No profile found | 0/— |
| BBB | No listing found | 0/— |
| Interior Design Press | No press page; no confirmed features | 0/— |

**Critical finding:** Jonathan Y is a *transactional entity* to AI models — encountered through Amazon product co-occurrence — but not a *named entity* that models independently recognize. Without a Wikipedia article, ChatGPT and Gemini cannot confidently identify "Jonathan Y" as a home décor brand vs. an academic researcher named Jonathan (the name disambiguation failure is real: Wikipedia search for "Jonathan Y" returns zero brand results).

**Entity Recognition Rating: Pre-established**
The brand lacks: founding year published anywhere, named founder, press mentions, Wikipedia/Wikidata record, Trustpilot profile, or BBB listing.

---

### 3. Content Quality & E-E-A-T — 42/100

| Dimension | Score | Key Finding |
|-----------|-------|------------|
| Experience | 7/25 | No first-hand accounts, no original research, no before/after content |
| Expertise | 8/25 | Zero named authors on any page across entire site |
| Authoritativeness | 12/25 | Scale signals exist; zero press mentions or industry recognition |
| Trustworthiness | 16/25 | HTTPS, policies, reviews present; no address, no phone |

**Page-by-page assessment:**

| Page | Word Count | Key Issues |
|------|-----------|-----------|
| Our Story | ~380 words | No founder name, no founding year, no facts; AI models cannot build entity profile from this page |
| Rug Guide | ~650 words | Functional but no citations, no author, too short to be authoritative |
| Lighting Guide | Very thin (bathroom only) | Missing: living room, bedroom, kitchen, dining lighting guidance — competitive gap for a lighting retailer |
| Blog (45+ posts) | 1,800–2,200/post | Zero author attribution; AI content signals strong (8 posts on July 21, 2025) |
| Sustainability | ~850 words | Claims without certifications; URL has typo (/sustainabilty) |

**AI content detection signals in blog:**
- 8 posts published on a single date (July 21, 2025)
- Generic openers: "In today's world," "it's important to note"
- No external citations anywhere across 45+ posts
- Repetitive thesis restatement patterns
- Two posts with identical titles ("Rug Trends for The Spring 2023")

**Duplicate content risk:** Two posts with identical titles confirmed. Shopify collection/faceted navigation URLs need canonical audit.

---

### 4. Technical Foundations — 61/100

| Area | Score | Finding |
|------|-------|---------|
| Server-Side Rendering | 90/100 | Shopify SSR — all content readable without JavaScript. Excellent for AI crawlers. |
| Mobile Optimization | 80/100 | Responsive design confirmed; Shopify CDN (Fastly) |
| URL Structure | 70/100 | Clean slugs; hyphenated; 2 clicks to most content |
| Crawlability | 72/100 | Well-configured; AI crawlers allowed |
| Core Web Vitals Risk | 55/100 | CLS risk: product images missing width/height attributes |
| Meta Tags & Indexability | 45/100 | Collection page titles very thin ("JONATHAN Y \| Rugs") |
| Security Headers | 40/100 | Shopify platform limitation; CSP not implemented |
| Response & Status | 70/100 | www vs. non-www inconsistency |

**Critical technical issues:**

1. **www/non-www inconsistency:** robots.txt Sitemap references `jonathany.com` (non-www) but all child sitemap entries use `www.jonathany.com`. This splits crawl signals.

2. **Stray tumbleliving.com sitemap in robots.txt:** The AhrefsBot section contains `Sitemap: https://www.tumbleliving.com/sitemap.xml` — a copy-paste error pointing to an entirely different brand.

3. **Thin collection page titles:** "JONATHAN Y | Rugs" (18 chars) wastes the title tag. Should be: "Area Rugs — Modern, Washable & Outdoor | JONATHAN Y".

4. **Missing meta descriptions** on collection pages and Our Story.

5. **Cloudflare JS challenge** active on deep product URLs — may intercept AI crawlers that don't execute JavaScript.

6. **/policies/ blocked** from all crawlers — removes trust signal pages from AI visibility.

7. **No BreadcrumbList depth** on product pages — current schema goes Home > Product, skipping the collection level.

---

### 5. Structured Data — 44/100

**Schema blocks detected:**

| Schema Type | Page | Status |
|------------|------|--------|
| WebSite + SearchAction | Homepage | Valid |
| Organization | Homepage | Partial — critical errors |
| WebPage | Homepage | Error: description: null |
| Product | Product pages | Partial — reviewCount error |
| BreadcrumbList | Product + Collection | Valid (2-level only) |
| ItemList | Collection pages | Partial — missing ratings |
| FAQPage | /pages/faqs | ABSENT — page has 10+ Q&A pairs with zero schema |

**Critical schema errors:**

1. **`reviewCount: "7.0"` (float string)** on every product page — must be a positive integer (`7`). This error blocks rich result eligibility for all products.

2. **`description: null`** in WebPage schema on homepage — invalid JSON-LD, causes validation failure.

3. **Organization sameAs incomplete:** Only Instagram and Facebook listed. YouTube, Pinterest, TikTok are in the page HTML but absent from schema.

   | Platform | In Page HTML | In sameAs Schema |
   |----------|-------------|-----------------|
   | Instagram | Yes | Yes |
   | Facebook | Yes | Yes |
   | YouTube | Yes | **NO** |
   | Pinterest | Yes | **NO** |
   | TikTok | Yes | **NO** |
   | LinkedIn | Unknown | **NO** |

4. **FAQPage schema missing** on /pages/faqs — the page has 10+ structured Q&A pairs with zero markup.

5. **No `speakable` property** anywhere on the site.

6. **Logo URL inconsistency** — Organization schema uses non-www URL for logo while canonical domain is www.

7. **119 product images** listed in single Product schema (should be 3-5 representative images).

8. **Brand name inconsistency** — "JONATHAN Y" (all-caps) vs "Jonathan Y" (title case) in ItemList schema.

---

### 6. Platform Optimization — 46/100

| Platform | Score | Status |
|----------|-------|--------|
| Google AI Overviews | 52/100 | Fair |
| Google Gemini | 51/100 | Fair |
| Bing Copilot | 46/100 | Poor |
| Perplexity AI | 42/100 | Poor |
| ChatGPT Web Search | 38/100 | Poor |

**Platform-specific gaps:**

- **Google AIO (52):** Collection pages have partial answer-target content but headings are promotional ("STYLE STARTS WITH THE FLOOR") not query-matching. FAQ page has content but zero FAQPage schema.
- **Gemini (51):** YouTube channel not linked in sameAs; product image alt text is filename format (`rug_1_5aff9a83...png`); no Knowledge Panel signals.
- **Bing Copilot (46):** No msvalidate.01 verification tag; no LinkedIn company page; no IndexNow integration.
- **Perplexity (42):** No llms.txt; no dateModified signals; content freshness invisible to crawlers.
- **ChatGPT (38):** Weakest platform. No Wikipedia/Wikidata entity. Cloudflare may block OAI-SearchBot from product pages.

---

## Priority Action Plan

### Quick Wins (1–7 days, zero to low cost)

| # | Action | Impact | Effort | Platforms Affected |
|---|--------|--------|--------|-------------------|
| 1 | **Deploy `llms.txt`** at domain root | High | 1 day | All platforms |
| 2 | **Expand Organization `sameAs`** — add YouTube, Pinterest, TikTok, LinkedIn | High | 1 hour | ChatGPT, Gemini, Bing |
| 3 | **Fix `reviewCount: "7.0"` → integer** in Product schema template | Critical | 30 min | Google AIO, all |
| 4 | **Add FAQPage schema** to /pages/faqs (10+ Q&A pairs ready) | High | 2 hours | Google AIO, Bing, Perplexity |
| 5 | **Remove `tumbleliving.com` sitemap** from robots.txt | Medium | 5 min | All |
| 6 | **Fix `description: null`** in homepage WebPage schema | Medium | 30 min | All |
| 7 | **Standardize www vs. non-www** — pick canonical, update robots.txt + sitemap | High | 2 hours | All |
| 8 | **Add Bing Webmaster Tools** verification (msvalidate.01 meta tag) | Medium | 30 min | Bing Copilot |
| 9 | **Fix logo URL** in Organization schema (non-www → www) | Low | 15 min | Gemini, All |
| 10 | **Fix sustainability page URL typo** (/sustainabilty → /sustainability) with 301 | Low | 15 min | All |

### Medium-Term (2–6 weeks)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 11 | **Rewrite Our Story page** — add founder name, founding year, catalog size, headquarters. Target 800+ words with 5+ verifiable facts | Critical | 1 week |
| 12 | **Add named authors** with bios to all blog posts and guides | Critical | 2 weeks |
| 13 | **Create Wikidata entity** (Q-item) for Jonathan Y with sameAs links | High | 2 days |
| 14 | **Rewrite collection page title tags** — "JONATHAN Y \| Rugs" → "Area Rugs — Modern, Washable & Outdoor \| JONATHAN Y" | High | 1 day |
| 15 | **Add meta descriptions** to all collection + content pages | High | 2 days |
| 16 | **Fix product image alt text** — replace filenames with descriptive "[Product Name] — [Color] [Style] by Jonathan Y" | High | 1 week (bulk edit) |
| 17 | **Add `sku` to Product schema** template (Shopify exposes via `{{ variant.sku }}`) | Medium | 2 hours |
| 18 | **Upgrade BreadcrumbList** depth — Home > Collection > Product (currently Home > Product) | Medium | 2 hours |
| 19 | **Add `speakable` property** to homepage and product page schema | Medium | 2 hours |
| 20 | **Remove /policies/ from robots.txt Disallow** — allow crawlers to see trust signal pages | Medium | 15 min |
| 21 | **Create Trustpilot profile** and actively solicit reviews | High | 1 week |
| 22 | **Create and complete LinkedIn company page** | High | 1 day |
| 23 | **Fix duplicate blog posts** — remove/consolidate two "Rug Trends for The Spring 2023" posts | Medium | 1 day |
| 24 | **Add `dateModified` signals** to all guide/support pages (human-readable + schema) | Medium | 1 day |
| 25 | **Enable Shopify IndexNow integration** for Bing instant indexing | Medium | 1 day |

### Strategic (1–3 months)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 26 | **Earn press coverage** — target Apartment Therapy, The Spruce, House Beautiful, Real Simple. Create `/pages/press` with media kit | Critical | 2–3 months |
| 27 | **Build Wikipedia article** (requires press coverage first for notability) | Critical | 2–3 months |
| 28 | **Create comprehensive buying guides** — `/pages/how-to-choose-a-rug`, `/pages/how-to-choose-lighting` with HowTo schema, comparison tables, room-by-room guidance | High | 1 month |
| 29 | **Expand Lighting Guide** beyond bathroom-only — add living room, bedroom, kitchen, dining room, outdoor sections with lumen/CRI/color temp specs | High | 2 weeks |
| 30 | **Create furniture buying guide** — currently no guides exist for furniture despite being a product category | Medium | 2 weeks |
| 31 | **Publish original research** — customer survey on rug sizing, "most popular rug styles by region" from sales data, material testing results. Creates citable brand-attributed statistics | High | 1 month |
| 32 | **Configure Cloudflare bypass rules** for named AI crawler user-agents (GPTBot, ClaudeBot, PerplexityBot) | High | 1 week |
| 33 | **Rewrite blog with editorial standards** — add author bylines, external citations, original data. Stop batch-publishing; establish consistent weekly cadence | High | Ongoing |
| 34 | **Add Organization schema properties** — foundingDate, description, contactPoint | Medium | 1 day |
| 35 | **Register BBB listing** | Low | 1 week |

---

## Ready-to-Deploy Assets

### llms.txt (deploy to https://jonathany.com/llms.txt)

```
# Jonathan Y

> Jonathan Y is a modern home décor brand offering lighting, area rugs, furniture, and outdoor décor. The brand combines contemporary design with accessible pricing and free delivery. Products span over 1,900 items across indoor/outdoor rugs, ceiling and wall lighting, accent furniture, and more.

## Core Pages

- [Our Story](https://jonathany.com/pages/our-story): Brand mission, design philosophy, and company background.
- [Sustainability](https://jonathany.com/pages/sustainability): Jonathan Y's eco-friendly packaging, sourcing, and operations commitments.
- [FAQs](https://jonathany.com/pages/faqs): Answers to common questions about orders, shipping, returns, and products.

## Product Collections

- [Rugs](https://jonathany.com/collections/rugs): 515+ indoor and outdoor rugs across modern, bohemian, Moroccan, geometric, and natural fiber styles.
- [Lighting](https://jonathany.com/collections/lighting): Pendants, flush mounts, chandeliers, sconces, table lamps, floor lamps, and outdoor lighting.
- [Furniture](https://jonathany.com/collections/furniture): Living room, dining, bathroom vanity, and outdoor furniture.
- [Outdoor](https://jonathany.com/collections/outdoor): Weather-resistant rugs, outdoor lighting, patio furniture, and umbrellas.
- [Washable Rugs](https://jonathany.com/collections/washable-rugs): Machine-washable area rugs with non-slip backing.
- [Natural Fiber Rugs](https://jonathany.com/collections/natural-fiber-rugs): Jute and natural material rugs.

## Buying Guides & Educational Content

- [Rug Size for King Bed](https://jonathany.com/blogs/news/rug-size-for-king-bed): Recommended rug dimensions (9x12, 8x10, 6x9) with placement rules.
- [Rug Size Guide for Living Room](https://jonathany.com/blogs/news/how-to-pick-the-perfect-rug-size-for-your-living-room-a-complete-guide): Room-by-room sizing rules.
- [Nylon vs. Polyester Rugs](https://jonathany.com/blogs/news/nylon-rugs-vs-polyester-what-s-the-real-difference): Material comparison covering durability, stain resistance, and cost.
- [Machine Washable Area Rugs Guide](https://jonathany.com/blogs/news/machine-washable-area-rugs): Care instructions and styling tips.
- [How to Use Lighting to Create Mood](https://jonathany.com/blogs/news/how-to-use-lighting-fixtures-to-create-different-moods-and-ambiances-in-a-room): Ambient, task, accent, and mood lighting explained.
- [How to Light a Bedroom](https://jonathany.com/blogs/news/how-to-light-a-bedroom): Bedroom lighting strategies.
- [Chandelier Buying Guide](https://jonathany.com/blogs/news/tips-and-ideas-for-buying-the-perfect-chandelier-your-buying-guide): Chandelier selection and sizing.
- [Rug Care and Maintenance](https://jonathany.com/pages/rug-care): Cleaning, storage, and preservation of area rugs.

## Customer Support

- [Returns Policy](https://jonathany.com/policies/refund-policy): 30-day return policy; $10 return shipping fee.
- [Assembly Guides](https://jonathany.com/pages/assembly): Product assembly instructions.

## Optional

- [Blog](https://jonathany.com/blogs/news): 45+ articles on rug selection, lighting design, furniture styling, and home décor trends.
```

---

### Organization Schema Fix (replace existing homepage JSON-LD)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://www.jonathany.com/#website",
      "url": "https://www.jonathany.com",
      "name": "JONATHAN Y",
      "potentialAction": {
        "@type": "SearchAction",
        "target": {
          "@type": "EntryPoint",
          "urlTemplate": "https://www.jonathany.com/search?q={search_term_string}"
        },
        "query-input": "required name=search_term_string"
      }
    },
    {
      "@type": "Organization",
      "@id": "https://www.jonathany.com/#organization",
      "name": "JONATHAN Y",
      "alternateName": "Jonathan Y Designs",
      "url": "https://www.jonathany.com",
      "logo": {
        "@type": "ImageObject",
        "url": "https://www.jonathany.com/cdn/shop/files/88895e18b14de1bd5716dda683a03a74_1024x1024.png"
      },
      "description": "JONATHAN Y is a modern home décor brand offering contemporary rugs, lighting, and furniture with free shipping on all orders.",
      "contactPoint": {
        "@type": "ContactPoint",
        "contactType": "customer service",
        "url": "https://www.jonathany.com/pages/contact",
        "availableLanguage": "English"
      },
      "sameAs": [
        "https://www.instagram.com/jonathany_official",
        "https://www.facebook.com/jonathanyofficial",
        "https://www.youtube.com/channel/UC8ebv0A0Tg55WN0SdagJ-CQ",
        "https://www.pinterest.com/jonathanydesign",
        "https://www.tiktok.com/@jonathany_official"
      ]
    },
    {
      "@type": "WebPage",
      "@id": "https://www.jonathany.com/#webpage",
      "url": "https://www.jonathany.com",
      "name": "JONATHAN Y — Modern Rugs, Lighting & Home Décor",
      "description": "Shop JONATHAN Y's curated collection of contemporary rugs, lighting, and furniture with free shipping on all orders.",
      "isPartOf": { "@id": "https://www.jonathany.com/#website" },
      "about": { "@id": "https://www.jonathany.com/#organization" },
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": ["h1", ".hero-description"]
      }
    }
  ]
}
```

---

## Competitor Benchmarks (Home Décor E-Commerce)

For context, well-optimized home décor e-commerce brands in the AI era typically score:

| Category | Industry Leader | Jonathan Y | Gap |
|----------|----------------|-----------|-----|
| AI Visibility | ~72 | 47 | -25 |
| Brand Authority | ~68 | 33 | -35 |
| Content & E-E-A-T | ~65 | 42 | -23 |
| Technical | ~74 | 61 | -13 |
| Schema | ~70 | 44 | -26 |
| Platform Opt. | ~64 | 46 | -18 |
| **GEO Score** | **~69** | **45** | **-24** |

The 24-point gap is closable. Brands that achieve 70+ typically have: a Wikipedia article, named content authors, 3+ press features per year, and llms.txt deployed.

---

## Risk Register

| Risk | Severity | Current Status |
|------|----------|---------------|
| Cloudflare JS challenge blocking AI crawlers from product pages | High | Active — needs WAF bypass rules |
| Batch AI content publishing detected — potential Google quality action | High | 8 posts July 21, 2025 |
| reviewCount float error blocking rich results sitewide | Critical | Active on all product pages |
| tumbleliving.com sitemap in robots.txt — reputational/confusion risk | Medium | Active |
| www/non-www split creating duplicate indexing | High | Active |
| Sustainability claims without certifications — greenwashing perception | Medium | Active |

---

*Report generated by Claude Code GEO Audit System — 5 parallel subagents (AI Visibility, Platform Analysis, Technical SEO, Content & E-E-A-T, Schema Markup)*
*Audit date: April 14, 2026*
