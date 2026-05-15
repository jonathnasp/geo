# GEO Audit Report — Happimess
**URL:** https://happimess.com/  
**Audit Date:** 2026-05-11  
**Business Type:** E-commerce (Shopify)  
**Platform:** Shopify SSR — server-side rendered, all content in initial HTML  
**Languages:** English (primary) · Spanish (`/es/`)  
**Auditor:** Claude Sonnet 4.6 · 5-agent parallel audit

---

## Composite GEO Score: 42 / 100 — Poor

| Category | Weight | Score | Weighted | Status |
|----------|--------|-------|---------|--------|
| AI Citability & Visibility | 25% | 34 | 8.5 | Poor |
| Brand Authority Signals | 20% | 22 | 4.4 | Critical |
| Content Quality & E-E-A-T | 20% | 42 | 8.4 | Poor |
| Technical Foundations | 15% | 74 | 11.1 | Fair |
| Structured Data | 10% | 61 | 6.1 | Fair |
| Platform Optimization | 10% | 34 | 3.4 | Poor |
| **Composite** | 100% | **42** | — | **Poor** |

> **Score reference:** 0–25 Critical · 26–50 Poor · 51–75 Fair · 76–90 Good · 91–100 Excellent

---

## What's Changed Since Last Audit

Several issues from the prior CLAUDE.md backlog are now **resolved** — confirmed by live site analysis:

| Issue | Prior Status | Current Status |
|-------|-------------|---------------|
| `"Happimess Dev"` in Product brand.name | Open | ✅ Fixed on Betty Retro product — verify globally |
| Organization schema missing sameAs | Open | ✅ Fixed — 6 platforms present in Organization JSON-LD |
| `description: null` in WebPage schema | Open | ✅ Fixed — description present |
| No hreflang EN/ES | Open | ✅ Fixed — EN, ES, x-default all present |
| Meta description missing | Open | ✅ Fixed — 163-char description present |
| `/pages/meet-our-authors` | Unknown | ✅ Page exists (sitemap lastmod 2026-05-11) |
| Admin usernames in blog author JSON-LD | Open | ⚠️ Partially — "sandip hadiya" (lowercase, missing credentials) |
| `/policies/` blocked in robots.txt | Open | ❌ Still blocked |
| No visible publication dates on blog posts | Open | ❌ Still not visible in HTML |

---

## 1. AI Citability & Visibility — 34/100 (Poor)

### Score Breakdown

| Component | Score | Weight | Weighted |
|-----------|-------|--------|---------|
| Citability | 38/100 | 35% | 13.3 |
| Brand Mentions | 22/100 | 30% | 6.6 |
| Crawler Access | 80/100 | 25% | 20.0 |
| llms.txt | 35/100 | 10% | 3.5 |

> Score capped from 43 to 34 due to severe brand authority gap — the primary signal AI models use for entity confidence.

### Citability Assessment

**Page Citability Score: 38/100**

Top citation-ready passages found across 5 pages:

| Passage | Source | Score | Assessment |
|---------|--------|-------|-----------|
| Dual trash can capacity guide (30–40L small / 40–60L most homes / 60L+) | Blog | 73/100 | CITATION-READY |
| Return policy specifics (30 days, $10 fee, 48 states, original packaging) | FAQ | 68/100 | Near citation-ready |
| Shipping time ("ships within 1-2 business days M-F") | FAQ | 67/100 | Near citation-ready |
| Dual trash can selection criteria list | Blog | 59/100 | Moderate |
| About Us brand philosophy statement | About | 39/100 | CITATION-UNLIKELY |
| Homepage product navigation text | Homepage | 29/100 | CITATION-UNLIKELY |

**What's holding citability down:**
- Homepage reads as a product navigation interface, not an authority document — no original claims, no data
- About Us is 250–300 words with zero specifics: no founding year, no team, no measurable outcomes
- All blog content is brand-promotional with zero external citations
- "From The Mess Experts" house byline with no credentials lowers AI confidence in all blog passages

### AI Crawler Access — 80/100

The robots.txt is a standard Shopify file. **No AI-specific rules exist** — all AI crawlers fall under `User-agent: *`.

| Crawler | Status | Notes |
|---------|--------|-------|
| GPTBot | ✅ Allowed (default) | Not named — inherits `*` rules |
| OAI-SearchBot | ✅ Allowed (default) | Not named |
| ClaudeBot | ✅ Allowed (default) | Not named |
| PerplexityBot | ✅ Allowed (default) | Not named |
| Google-Extended | ✅ Allowed (default) | Not named |
| Amazonbot, Bytespider, CCBot, Cohere-ai | ✅ Allowed (default) | Not named |

**Critical blocked path:** `/policies/` — blocks return policy, privacy policy, shipping policy, and terms pages from ALL crawlers including AI bots. These are high-citability trust-signal pages.

**AI crawlers can access:** All products, collections, blog articles, static pages, homepage, sitemap.

### llms.txt — 35/100

**Status:** Both `/llms.txt` AND `/llms-full.txt` exist (both Shopify UCP boilerplate).  
**Format validation:** H1 and blockquote present ✅ | Link format non-standard ❌ (`Label: URL` instead of `[Label](URL): Description`)

**Critical content gaps:**
- Only 2 content links (all-products, search) — no categories, no key pages, no blog articles
- `/pages/about-us`, `/pages/faqs`, `/pages/refill-page`, `/pages/ambassador-program` — all absent
- No blog content references (24 articles, 0 linked)
- No social profile URLs
- No Spanish locale mention
- Shopify "Start your own store" promo link is brand-irrelevant noise

### Brand Authority — 22/100

| Platform | Status | Score | Detail |
|----------|--------|-------|--------|
| Wikipedia | ❌ Absent | 0/30 | No Wikipedia article. Lithuanian nonprofit "HAPPIMESS" (happimess.lt) creates entity confusion risk |
| Reddit | 🟡 Minimal | 4/20 | 2 deal-spam posts (2022–23). No organic discussion in r/homeorganization, r/tidyspaces, or r/declutter |
| YouTube | 🟡 Sparse | 7/15 | Channel `@happimess` exists but appears sparse/inactive. No third-party creator content |
| LinkedIn | ❌ Absent | 1/10 | No Happimess e-commerce company page. `/company/happimess` belongs to Lithuanian nonprofit |
| Industry/Press | 🟡 Minimal | 10/25 | Amazon product presence confirmed (via deal posts). No press, no review platforms |

> **Critical:** A Lithuanian nonprofit shares the "Happimess" name on both Wikipedia and LinkedIn. AI models may confuse or conflate these two entities. Registering a LinkedIn page (`/company/happimess-home` or `/company/happimess-official`) is urgent.

---

## 2. Brand Authority Signals — 22/100 (Critical)

The weakest category and the primary factor suppressing the composite score. See brand mention breakdown above.

**Top 3 brand authority fixes:**

1. **Create Wikidata entity** (free, 30 min) — Wikidata is a primary reference for ChatGPT, Gemini, and Perplexity entity resolution. Once created, add to Organization `sameAs`.
2. **Create LinkedIn company page** (`/company/happimess-home`) — Required for Bing Copilot ecosystem, ChatGPT entity validation, and Gemini Knowledge Graph.
3. **Build organic Reddit presence** — Post genuine value in r/homeorganization, r/tidyspaces, r/malelivingspace (answer questions without selling). AI models weight organic community discussion heavily.

---

## 3. Content Quality & E-E-A-T — 42/100 (Poor)

**E-E-A-T Score: 37/100**

| Dimension | Score | Key Findings |
|-----------|-------|-------------|
| Experience | 6/25 | No founder story, no first-hand testing data, no customer stories with names, no before/after comparisons |
| Expertise | 9/25 | "From The Mess Experts" byline — no credentials, no individual authors, no methodology transparency |
| Authoritativeness | 10/25 | 24-article blog signals topical investment; zero external citations on any page |
| Trustworthiness | 12/25 | HTTPS, visible contact info (email + phone), 30-day return policy; no third-party reviews displayed |

### Page-by-Page Assessment

| Page | Word Count | Assessment |
|------|-----------|------------|
| Homepage | ~800–1,000 | Mostly product titles — minimal descriptive brand content |
| About Us | ~250–300 | Critical gap — no founder, no founding year, no credentials |
| Blog: Trash Bag article | ~1,800–2,000 | Long-form, appropriate depth, but promotional and uncited |
| Blog: Dual Trash Can guide | ~1,200 | Good structure, adequate depth |
| FAQ | ~400 (8 questions) | Too sparse — missing product knowledge questions |

### AI Content Assessment

Both blog articles reviewed show **likely AI-generated with light editing** signals:
- Generic phrasing ("In today's kitchens," "rigorous testing and quality assurance")
- Perfect structure, thin substance (About Us has correct outline but each section says very little)
- Zero original data across all pages
- Repetitive thesis restatement (core recommendation appears in intro, body, and conclusion)
- No conflict-of-interest disclosure noting that blog "recommendations" are brand-owned products

### Heading Structure Issues

```
Homepage H1:  "Happimess"  — brand name only, not descriptive
About Us H1:  "About us"   — no brand differentiator  
About Us H2:  "welcome to [Logo]"  — only 2 headings on a critical E-E-A-T page
```

Blog articles have well-structured H2/H3 hierarchies (positive signal).

### Topical Authority

- **Breadth:** ~24 articles across trash, organization, storage, kitchen, laundry
- **Gap:** Zero article-to-article internal links — commercial spoke model only (blog → product pages). No topical clustering visible to AI systems.
- **Missing topics:** Composting/food waste separation, trash can sizing guide by room, cleaning/deodorizing guides, eco packaging, competitor comparison guides, product care/maintenance.

### Priority Content Actions

| # | Action | Priority | Impact |
|---|--------|----------|--------|
| 1 | Rewrite About Us to 800+ words: named founder, founding year, origin story, credentials | Critical | All platforms |
| 2 | Replace "From The Mess Experts" with named author + 100-word bio page + Person schema | Critical | AI citation |
| 3 | Add 2–3 external citations per blog article (EPA, consumer research, NAPO data) | High | Perplexity, AIO |
| 4 | Rewrite homepage H1 to descriptive value proposition + add 100–150 word brand description | High | AI citability |
| 5 | Expand FAQ from 8 → 25–30 questions in 4–5 categories | High | Google AIO |
| 6 | Surface publication dates visibly in blog HTML (`{{ article.published_at }}`) | Medium | Freshness |
| 7 | Add conflict-of-interest disclosure to all product recommendation posts | Medium | Trustworthiness |
| 8 | Add article-to-article internal links to build topical clusters | Medium | Topical authority |

---

## 4. Technical Foundations — 74/100 (Fair)

### Score Breakdown

| Category | Score | Status |
|----------|-------|--------|
| Server-Side Rendering | 95/100 | ✅ Excellent — Shopify SSR, all content in initial HTML |
| Meta Tags & Indexability | 72/100 | ⚠️ Mostly good — og:image issues |
| Crawlability | 68/100 | ⚠️ `/policies/` blocked |
| Security Headers | 62/100 | ⚠️ HSTS short, no Referrer-Policy |
| Core Web Vitals Risk | 65/100 | ⚠️ jQuery sync load, Font Awesome CDN |
| Mobile Optimization | 90/100 | ✅ Responsive, correct viewport, srcset |
| URL Structure | 88/100 | ✅ Clean slugs, HTTPS, lowercase |
| Response & Status | 80/100 | ✅ 200 OK, Cloudflare CDN, ETag |

### Key Technical Findings

**✅ Positives:**
- Shopify SSR — GPTBot, ClaudeBot, PerplexityBot see full content without JS execution
- HTTPS enforced, Cloudflare CDN active
- Sitemap index at `/sitemap.xml` with 9 child sitemaps (383 products, 98 collections, 27 blog posts, 15 pages, plus ES mirrors + agentic discovery)
- Canonical self-referencing present on all tested pages
- hreflang EN/ES/x-default present and functioning
- `lang="en"` / `lang="es"` HTML attributes server-set correctly
- `content-language: en-US` / `es-US` response headers present

**❌ Issues:**

| Issue | Severity | Fix |
|-------|----------|-----|
| `/policies/` blocked in robots.txt | High | Remove `Disallow: /policies/` in Shopify Admin |
| jQuery loaded synchronously (render-blocking) | High | Add `defer` to `<script src="jquery...">` in theme.liquid |
| og:image uses HTTP URL (`http://`) | High | Update to HTTPS in Shopify social sharing settings |
| og:image dimensions: 280×280px | High | Replace with 1200×630px image |
| `<meta name="author">` on Spanish pages = `"derecha:15px;"` | Medium | CSS value leaked into meta tag — theme bug to fix |
| Duplicate hreflang declarations (`/es/` vs `/es` trailing slash) | Medium | Unify format across theme and Shopify checkout injection |
| All 383 product sitemap lastmod dates identical (2026-05-11) | Medium | Bulk timestamp reset removes recrawl prioritization signal |
| `Shopify.shop = "happimess-dev.myshopify.com"` in page DOM | Low | Staging artifact visible in source — cosmetic but brand-inconsistent |
| HSTS max-age ~91 days (should be 1 year+) | Low | Extend via Cloudflare HSTS settings |
| Missing Referrer-Policy header | Low | Add via Cloudflare Transform Rules |
| Font Awesome full CSS from CDN (render-blocking) | Low | Subset or self-host |

### Sitemap Details

| Child Sitemap | URLs | Notes |
|--------------|------|-------|
| sitemap_products_1.xml | 383 + homepage | All lastmod identical — bulk reset |
| sitemap_collections_1.xml | 98 | Accurate date range |
| sitemap_blogs_1.xml | 27 posts | 2021–2026 range, accurate |
| sitemap_pages_1.xml | 15 pages | Includes /pages/meet-our-authors |
| sitemap_agentic_discovery.xml | 3 (llms.txt, llms-full.txt, agents.md) | No lastmod values |
| es/* (4 sitemaps) | Mirror of EN | Spanish variants all crawlable |

---

## 5. Structured Data — 61/100 (Fair)

**Significant update:** Schema implementation is substantially more complete than the quick snapshot suggested. JSON-LD is server-rendered via Shopify SSR — all AI crawlers read it without JS.

### Schema Inventory

| Schema Type | Pages | Status | Issues |
|------------|-------|--------|--------|
| Organization (sitewide) | All pages | ✅ Present, comprehensive | sameAs on WebSite node (non-standard); department node redundant |
| WebSite + SearchAction (sitewide) | All pages | ✅ Present, valid | sameAs should be on Organization only |
| WebPage | Homepage | ✅ Present | Missing BreadcrumbList link, no speakable |
| Product | Product pages | ✅ Present, detailed | No AggregateRating/Review; HTML entities in description; single image |
| BreadcrumbList | Product + Blog | ✅ Present | 2-level only (Home → Product); missing collection middle step |
| Article | Blog posts | ✅ Present | Author lowercase ("sandip hadiya"); no sameAs on author; broken author URL risk |
| FAQPage | /pages/faqs + Product pages | ✅ Present | Rich results restricted since Aug 2023 — semantic value retained |
| Person (author) | Blog posts | ⚠️ Partial | In Article schema only; no sameAs, no jobTitle, no worksFor |
| speakable | Blog posts | ✅ Present | Absent from homepage and product pages |
| BreadcrumbList (homepage) | Homepage | ❌ Missing | — |
| AggregateRating / Review | Products | ❌ Missing | Largest single missing rich result opportunity |

### Organization Schema — Key Finding

The sitewide Organization block is comprehensive and largely correct:
- `name: "Happimess"` ✅
- Address: 185 Madison Ave, New York, NY 10016 ✅
- `foundingDate: "2020-01-15"` ✅
- `sameAs`: Facebook, Instagram, LinkedIn (`/company/happimesshome`), Pinterest, YouTube, TikTok ✅
- `knowsAbout`: 10 relevant topics ✅
- `contactPoint` with telephone + email ✅

**Missing from sameAs:** Wikipedia, Wikidata, Crunchbase — the three highest-authority AI entity resolution signals.

### Product Schema — Key Finding

The `"Happimess Dev"` brand name fix appears applied on at least the Betty Retro product. However: verify globally across all 383 products — the fix may not have propagated to all product types. Check 3–5 random products in Shopify Admin.

Product schema is well-structured with offers, shipping, returns. The critical missing element is **AggregateRating** — required for star ratings in Google Search rich results.

### Article Schema — Key Finding

Author identity issue: JSON-LD shows `"sandip hadiya"` (lowercase) while the HTML `<meta name="author">` shows `"Jonathan Yaraghi"`. These are inconsistent. The author URL `https://happimess.com/pages/meet-our-authors#sandip-hadiya` references a page that appears to exist (in sitemap) but the anchor must be verified as live.

### Ready-to-Deploy Schema Fixes

#### Fix 1: Organization — Remove sameAs from WebSite, remove department node
In `theme.liquid`, split the current combined block:
- `WebSite`: remove `sameAs` array entirely (belongs on Organization only)
- `Organization`: remove the `department` node (ContactPoint already covers this)

#### Fix 2: Add Wikidata to sameAs (once created)
```json
"sameAs": [
  "https://www.facebook.com/happimessofficial/",
  "https://www.instagram.com/happimess_official/",
  "https://www.linkedin.com/company/happimesshome/",
  "https://www.pinterest.com/happimess_/",
  "https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g",
  "https://www.tiktok.com/@happimess_official",
  "https://www.wikidata.org/wiki/[WIKIDATA-ID-WHEN-CREATED]",
  "https://www.crunchbase.com/organization/happimess"
]
```

#### Fix 3: Add AggregateRating to Product schema
```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "[from review app]",
  "reviewCount": "[from review app]",
  "bestRating": "5",
  "worstRating": "1"
}
```
Only add when real review data exists. Do not use placeholder values.

#### Fix 4: Fix Article author
```json
"author": {
  "@type": "Person",
  "@id": "https://happimess.com/pages/meet-our-authors#sandip-hadiya",
  "name": "Sandip Hadiya",
  "jobTitle": "Home Organization Specialist",
  "worksFor": {
    "@type": "Organization",
    "@id": "https://happimess.com/#organization",
    "name": "Happimess"
  },
  "sameAs": ["[Author LinkedIn URL]"]
}
```

#### Fix 5: Add speakable to homepage WebPage block
```json
"speakable": {
  "@type": "SpeakableSpecification",
  "cssSelector": ["h1", ".hero__title", ".hero__subtitle", ".homepage-description"]
}
```

#### Fix 6: Extend BreadcrumbList to 3 levels (Home → Collection → Product)
```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://happimess.com"},
    {"@type": "ListItem", "position": 2, "name": "[Collection Name]", "item": "[Collection URL]"},
    {"@type": "ListItem", "position": 3, "name": "{{ product.title }}", "item": "{{ shop.url }}{{ product.url }}"}
  ]
}
```

### Schema Priority Actions

| # | Action | File | Effort | Impact |
|---|--------|------|--------|--------|
| 1 | Verify "Happimess Dev" fix on ALL products (not just Betty Retro) | Admin review | Low | Critical |
| 2 | Create Wikidata entity + add to Organization sameAs | External + theme.liquid | Low | Entity authority |
| 3 | Add AggregateRating to products (connect review app data) | product.liquid | Medium | Rich results |
| 4 | Fix Article author: capitalize + add worksFor + sameAs | article.liquid | Low | E-E-A-T |
| 5 | Remove sameAs from WebSite node; remove department from Organization | theme.liquid | Low | Schema correctness |
| 6 | Add speakable to homepage WebPage block | theme.liquid | Low | AI assistant readiness |
| 7 | Extend BreadcrumbList to 3 levels on product pages | product.liquid | Low | Navigation context |
| 8 | Fix Product description HTML entities (add `\| strip_html` filter) | product.liquid | Low | Schema cleanliness |
| 9 | Add articleSection, wordCount, keywords to Article schema | article.liquid | Low | Content classification |
| 10 | Create Crunchbase profile + add to sameAs | External + theme.liquid | Low | Brand authority |

---

## 6. Platform Optimization — 34/100 (Poor)

### Platform Readiness Scores

| Platform | Score | Status | Primary Gap |
|----------|-------|--------|-------------|
| Google AI Overviews | 38/100 | Poor | No FAQ rich results (schema restricted), no featured snippet paragraphs, weak H1 |
| Bing Copilot | 36/100 | Poor | No LinkedIn page (Microsoft ecosystem gap), no Bing Webmaster Tools verification |
| Perplexity AI | 33/100 | Poor | No external citations, no visible dates, llms.txt too thin |
| Google Gemini | 32/100 | Poor | No AggregateRating for Shopping Graph, weak About Us entity |
| ChatGPT Web Search | 30/100 | Poor | No Wikipedia/Wikidata entity, no named author, entity confusion with Lithuanian nonprofit |

### Cross-Platform Quick Wins

These 5 actions improve **multiple platforms simultaneously**:

| Action | Platforms Improved |
|--------|------------------|
| Organization JSON-LD with Wikidata/Wikipedia sameAs | ChatGPT, Gemini, Bing, Perplexity |
| Named author + bio page + Person schema | All 5 platforms |
| Visible publication dates on all blog posts | Perplexity, ChatGPT, Google AIO |
| Create LinkedIn company page | Bing, ChatGPT, Gemini |
| Expand llms.txt with key pages + blog index | Perplexity, ChatGPT, Gemini |

### Platform-Specific Actions

**Google AI Overviews:**
- Open each blog article with a 40–60 word direct answer paragraph immediately after the H2 heading
- Replace homepage H1 with: "Home Organization, Storage & Trash Solutions Designed for Real Life"
- Add definition patterns ("A dual trash can is...") for FAQ-style queries

**ChatGPT Web Search:**
- Resolve entity confusion with Lithuanian nonprofit by establishing strong LinkedIn presence
- Add explicit `User-agent: GPTBot / OAI-SearchBot` allow rules to robots.txt

**Perplexity AI:**
- Add visible publication dates to blog index page (currently only in article metadata)
- Each article needs ≥1 cited statistic from an authoritative external source

**Google Gemini:**
- Embed Happimess YouTube product videos on product category pages
- AggregateRating on all products is the highest-ROI Gemini action (Shopping Graph)

**Bing Copilot:**
- Verify site in Bing Webmaster Tools and add `msvalidate.01` meta to theme.liquid
- Implement IndexNow via Shopify app (notifies Bing instantly on new content)

### Content Format Recommendations (All Platforms)

| Format | Recommendation |
|--------|---------------|
| Comparison tables | Add to collection pages and blog articles ("Open Top vs. Step-On Trash Can") |
| FAQ blocks on product pages | 3–5 product-specific Q&As per major product page |
| Definition paragraphs | Open each article section with "X is..." pattern for AIO extraction |
| Ordered lists / HowTo | Structure organization guides as numbered steps with HowTo schema |
| Specification tables | Add dimensions, capacity, material, liner size to all product pages |

---

## Master Priority Action Plan

### Sprint 1: Quick Wins — Shopify Admin / Theme (< 1 hour each)

| # | Action | Where | Platform Impact |
|---|--------|-------|----------------|
| 1 | Verify `"Happimess Dev"` fix is global across all 383 products | Admin product review | Critical — all platforms |
| 2 | Unblock `/policies/` in `robots.txt.liquid` | Admin → Themes → Edit Code | AI crawlers, trust signals |
| 3 | Fix og:image: HTTPS URL, minimum 1200×630px | Admin → Themes → Social sharing | All preview cards |
| 4 | Add `defer` to jQuery `<script>` tag in theme.liquid | theme.liquid | Core Web Vitals / INP |
| 5 | Enhance llms.txt: add key pages, blog index, categories, social URLs, ES locale | Admin → Files | AI crawlers (all platforms) |
| 6 | Fix `<meta name="author">` bug on Spanish pages (`"derecha:15px;"`) | Spanish theme template | Brand professionalism |
| 7 | Create Wikidata entity for Happimess | wikidata.org (external) | ChatGPT, Gemini, entity graph |
| 8 | Create LinkedIn company page (`/company/happimess-home`) | linkedin.com (external) | Bing, ChatGPT, Gemini |

### Sprint 2: Content & Schema (1–3 days)

| # | Action | Where | Impact |
|---|--------|-------|--------|
| 9 | Rewrite About Us: 800+ words, named founder, founding story, credentials | Shopify page editor | E-E-A-T — highest leverage |
| 10 | Replace house byline with named author + bio page + Person schema | theme.liquid + page | All platforms |
| 11 | Surface publication dates in blog article HTML | article.liquid template | Perplexity, ChatGPT, AIO |
| 12 | Add external citations to top 5 blog articles (2–3 per article) | Blog editor | Perplexity, AIO |
| 13 | Fix Article schema: capitalize author name, add worksFor + sameAs | article.liquid | E-E-A-T |
| 14 | Remove sameAs from WebSite node + remove department from Organization | theme.liquid | Schema correctness |
| 15 | Add Wikidata URL to Organization sameAs (after Step 7 above) | theme.liquid | Entity resolution |
| 16 | Fix trailing slash inconsistency in hreflang | theme.liquid | Technical SEO |
| 17 | Unify `<meta name="author">` with JSON-LD author (currently inconsistent) | theme.liquid | Brand trust |

### Sprint 3: Medium-term (1–2 weeks)

| # | Action | Impact |
|---|--------|--------|
| 18 | Add AggregateRating to all product schemas (connect review app) | Rich results, Gemini Shopping |
| 19 | Expand FAQ to 25–30 questions in 4–5 categories | Google AIO |
| 20 | Rewrite homepage H1 to descriptive value proposition + brand description block | AI citability |
| 21 | Add 3–5 product-specific FAQ blocks to major product pages | AIO, rich results |
| 22 | Add speakable to homepage WebPage and product page schemas | AI assistant readiness |
| 23 | Extend BreadcrumbList to 3 levels (Home → Collection → Product) | Navigation context |
| 24 | Add conflict-of-interest disclosures to product recommendation blog posts | Trustworthiness |
| 25 | Verify site in Bing Webmaster Tools + add msvalidate.01 meta | Bing Copilot |
| 26 | Implement IndexNow via Shopify app | Bing/Yandex freshness |
| 27 | Build article-to-article internal links for topical clustering | Topical authority |
| 28 | Create Crunchbase profile + add to sameAs | Brand authority |
| 29 | Add articleSection, wordCount, keywords to Article schema | Content classification |
| 30 | Fix Product description HTML entities (`\| strip_html` filter) | Schema cleanliness |
| 31 | Extend HSTS max-age to 1 year via Cloudflare settings | Security |

---

## Score Projection

| Category | Current | After Sprint 1 | After Sprint 2 | After Sprint 3 |
|----------|---------|---------------|---------------|---------------|
| AI Citability | 34 | 45 | 58 | 68 |
| Brand Authority | 22 | 38 | 48 | 60 |
| Content Quality | 42 | 44 | 62 | 70 |
| Technical | 74 | 80 | 82 | 85 |
| Structured Data | 61 | 65 | 73 | 80 |
| Platform Optimization | 34 | 45 | 58 | 68 |
| **Composite GEO** | **42** | **~52** | **~63** | **~73** |

Sprint 1 alone (quick wins, under a day) moves the site from **Poor → Fair (52)**. All three sprints move it to **Good (73)**.

---

## Appendix: Site Inventory

| Asset | Count/Status |
|-------|-------------|
| Products in sitemap | 383 |
| Collections | 98 |
| Blog articles | 27 (sitemap) / ~24 confirmed |
| Key static pages | 15 (including /pages/meet-our-authors) |
| Languages | EN (primary) + ES (`/es/`) |
| Social platforms | 6 (Facebook, Instagram, LinkedIn, Pinterest, YouTube, TikTok) |
| llms.txt | ✅ Present (Shopify-generated UCP boilerplate) |
| llms-full.txt | ✅ Present |
| agents.md | ✅ Present |
| Schema types in use | WebPage, WebSite, Organization, Product, Article, BreadcrumbList, FAQPage, Person (partial) |
| Shopify theme | "Unsen" / "Ai" v1.6 |
| CDN | Cloudflare |
| Server | Shopify (gcp-asia-southeast1 origin) |

---

*Full GEO Audit · Claude Sonnet 4.6 via `/geo audit` · 2026-05-11 · happimess.com*  
*5 parallel subagents: AI Visibility · Platform Analysis · Technical SEO · Content Quality · Schema Markup*  
*Archive prior report as `GEO-AUDIT-REPORT-[previous-date].md` before running next audit.*
