# GEO Audit Report — Happimess
**URL:** https://happimess.com/  
**Date:** April 14, 2026  
**Business Type:** E-Commerce (Home Organization, Storage, Trash Management)  
**Platform:** Shopify  

---

## Composite GEO Score: 38 / 100 — Poor

> Happimess has a technically sound Shopify foundation but zero deliberate GEO infrastructure.
> The site is essentially invisible to AI search engines today. All core AI visibility primitives are missing.

| Category | Weight | Score | Weighted |
|----------|--------|-------|----------|
| AI Citability & Visibility | 25% | 37 | 9.3 |
| Brand Authority Signals | 20% | 18 | 3.6 |
| Content Quality & E-E-A-T | 20% | 37 | 7.4 |
| Technical Foundations | 15% | 67 | 10.1 |
| Structured Data | 10% | 42 | 4.2 |
| Platform Optimization | 10% | 37 | 3.7 |
| **COMPOSITE GEO SCORE** | **100%** | | **38.3 → 38/100** |

---

## Score Dashboard

```
AI Citability & Visibility    [████████░░░░░░░░░░░░] 37/100  Poor
Brand Authority Signals       [███░░░░░░░░░░░░░░░░░] 18/100  Critical
Content Quality & E-E-A-T     [████████░░░░░░░░░░░░] 37/100  Poor
Technical Foundations         [█████████████░░░░░░░] 67/100  Fair
Structured Data               [█████████░░░░░░░░░░░] 42/100  Poor
Platform Optimization         [████████░░░░░░░░░░░░] 37/100  Poor
─────────────────────────────────────────────────────────────
COMPOSITE GEO SCORE           [████████░░░░░░░░░░░░] 38/100  Poor
```

---

## Platform Readiness

| Platform | Score | Status |
|----------|-------|--------|
| Google AI Overviews | 44/100 | Poor |
| Perplexity AI | 38/100 | Critical |
| Google Gemini | 36/100 | Critical |
| Bing Copilot | 35/100 | Critical |
| ChatGPT Web Search | 31/100 | Critical |

---

## Executive Summary

Happimess is a well-merchandised Shopify e-commerce brand selling home organization and trash management products. The site has clean SSR infrastructure, a bilingual (EN/ES) store, an active blog (~24 posts), and social presence across 5 platforms. These are real strengths.

However, from an AI search perspective, the site does not exist. No `llms.txt` file. No explicit AI crawler permissions. No `sameAs` entity links. No Wikipedia presence. No LinkedIn company page. No named blog authors. No publication dates on any content. A staging artifact (`"Happimess Dev"`) is leaking into production Product schema and poisoning entity recognition across Google, Gemini, and Bing.

The blog produces topically relevant content — the kitchen trash can sizing guide is genuinely citation-ready — but it is surrounded by statistically sparse, AI-pattern prose that AI systems will deprioritize.

The fixes are mostly non-engineering tasks: adding a single file (`llms.txt`), editing a single JSON-LD block (Organization `sameAs`), updating a Shopify theme template (product brand name), creating an author profile page, and adding dates to blog posts. These changes alone could raise the GEO Score by 15–20 points within 30 days.

---

## Critical Issues (Fix Within 1 Week)

### 1. "Happimess Dev" Brand Name in Production Product Schema
**Severity: Critical | Effort: Low | Impact: All platforms**

A staging namespace is being served in production. Every product page on the site contains `"brand": { "name": "Happimess Dev" }` in its JSON-LD Product schema. This causes Google, Gemini, and Bing Copilot to link products to an unrecognized entity ("Happimess Dev") rather than the actual brand.

**Fix:** In the Shopify product template (product.liquid or the JSON-LD snippet), change `"Happimess Dev"` → `"Happimess"`. Search the theme for the string literal and replace all instances.

---

### 2. No llms.txt File
**Severity: Critical | Effort: Low | Impact: All AI platforms**  
**Current Score: 0/100**

`https://happimess.com/llms.txt` returns 404. This file is the primary mechanism for communicating site structure to AI crawlers. Without it, AI models must infer your content from raw crawling — a less reliable process for an e-commerce site.

**Fix:** Create the file below and host it at `https://happimess.com/llms.txt`:

```
# Happimess

> Happimess is a US-based e-commerce brand selling home organization, trash management, storage furniture, and kitchen accessories. Ships to the 48 contiguous US states. Products include step-open and sensor trash cans, dual-compartment recycling bins, storage benches, wicker baskets, shelving units, and cleaning supplies.

## Products

- [Trash Cans](https://happimess.com/collections/trash): Step-open, sensor, push-button, dual-compartment, and outdoor trash can collection.
- [Storage & Organization](https://happimess.com/collections/organization): Baskets, bins, shelving, hampers, and under-bed storage.
- [Storage Furniture](https://happimess.com/collections/storage-furniture): Ottomans, benches, trunks, and side tables with integrated storage.
- [Kitchen & Bathroom](https://happimess.com/collections/kitchen): Dish racks, paper towel holders, toilet paper holders, trays.
- [Wipes & Cleaning](https://happimess.com/collections/wipes): Cleaning wipes and household maintenance products.

## Guides & Blog

- [Choosing the Perfect Kitchen Trash Can](https://happimess.com/blogs/news/the-guide-to-choosing-the-perfect-kitchen-trash-can): Size, lid type, material, and feature guide.
- [Standard Kitchen Trash Can Size](https://happimess.com/blogs/news/standard-kitchen-trash-can-size): Size chart by household type (gallons and inches).
- [Trashcan Maintenance Tips](https://happimess.com/blogs/news/trashcan-maintenance-tips-and-tricks-for-a-fresh-and-odor-free-bin): Cleaning, odor control, and liner guidance.
- [Organization Tips for 2025](https://happimess.com/blogs/news/organization-do-s-and-don-ts-for-2025-practical-tips-for-a-clutter-free-home): Practical home organization guidance.
- [Storage Benches Guide](https://happimess.com/blogs/news/living-room-storage-bench): Buying guide for living room storage seating.

## Company & Policies

- [About Happimess](https://happimess.com/pages/about-us): Mission, brand values, and product philosophy.
- [FAQs](https://happimess.com/pages/faqs): Shipping timelines, return policy, order changes.
- [Return Policy](https://happimess.com/pages/return-policy): 30-day returns, $10 return shipping fee.
- [Shipping Policy](https://happimess.com/pages/shipping-policy): FedEx delivery, 3-5 day transit, 1-2 day fulfillment.
- [Contact](https://happimess.com/pages/contact-us): hello@happimess.com, (917) 261-4961, Mon-Fri 9AM-5PM EST.

## Optional

- [Subscribe & Save](https://happimess.com/pages/refill-page): Subscription program for trash bag refills.
- [Ambassador Program](https://happimess.com/pages/ambassador-program): Brand partnership information.
- [Spanish Language Store](https://happimess.com/es/): Full Spanish-language version.
```

---

### 3. Organization Schema Missing sameAs — Zero Entity Identity
**Severity: Critical | Effort: Low | Impact: ChatGPT, Gemini, Bing, Perplexity**

The Organization schema exists on every page but has no `sameAs` array. AI models use `sameAs` to link a brand entity to its social profiles, Wikipedia, and directories. Without it, every AI model treats Happimess as an unverified, low-confidence entity.

**Fix:** Replace the existing thin Organization block in `theme.liquid` with this expanded version:

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://happimess.com/#organization",
  "name": "Happimess",
  "legalName": "Happimess",
  "url": "https://happimess.com",
  "description": "Happimess is a New York-based home organization brand selling trash cans, storage baskets, hampers, wicker trunks, and custom-fit trash bag subscriptions for stylish, clutter-free homes.",
  "foundingDate": "[REPLACE: founding year]",
  "logo": {
    "@type": "ImageObject",
    "url": "https://cdn.shopify.com/s/files/1/0491/2909/5325/files/happimess-logo-ai-file_1.svg?v=1697698531"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "185 Madison Avenue",
    "addressLocality": "New York",
    "addressRegion": "NY",
    "postalCode": "10016",
    "addressCountry": "US"
  },
  "telephone": "(917) 261-4961",
  "email": "hello@happimess.com",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "(917) 261-4961",
    "email": "hello@happimess.com",
    "contactType": "customer support",
    "availableLanguage": "English",
    "areaServed": "US"
  },
  "sameAs": [
    "[REPLACE: LinkedIn company page URL]",
    "[REPLACE: Facebook page URL]",
    "[REPLACE: Instagram profile URL]",
    "[REPLACE: YouTube channel URL]",
    "[REPLACE: Pinterest profile URL]",
    "[REPLACE: TikTok profile URL]",
    "[REPLACE: Crunchbase URL if listed]"
  ]
}
```

---

### 4. Author Identity Leak — "jonathany 2123" / "Asodariya Sumi" in Public Schema
**Severity: Critical | Effort: Low | Impact: Google AIO, Article rich results, E-E-A-T**

Shopify admin usernames are leaking into the public `Article` and `BlogPosting` JSON-LD schema served on every blog post. `"author": { "name": "jonathany 2123" }` and `"Asodariya Sumi"` are visible to all crawlers. This actively undermines E-E-A-T signals — Google's quality raters and AI models will not treat these as credible authors.

**Fix:** In Shopify admin → Blog → Author settings, set proper display names for all contributors. Then update the Article schema template to use the display name, add a `url` pointing to an author bio page (e.g., `/pages/jonathan-y`), and add `sameAs` links to the author's LinkedIn profile.

---

### 5. No Named Authors on Any Blog Content
**Severity: Critical | Effort: Medium | Impact: E-E-A-T, all AI platforms**

The "From The Mess Experts" byline is used across all 24+ blog posts. This brand-level attribution has zero E-E-A-T value. AI models cannot assign credibility to an anonymous brand voice.

**Fix:**
1. Assign real display names to all existing blog posts in Shopify
2. Create an author bio page at `/pages/[author-name]` with: photo, job title, relevant credentials, LinkedIn link
3. Add `Person` schema to the author page with `sameAs` links
4. Retroactively apply real author attribution to all existing posts

---

### 6. Blog Posts Have No Visible Publication Dates
**Severity: Critical | Effort: Low | Impact: Trust, freshness signals, all AI platforms**

No blog post across the entire site displays a publication or last-updated date in visible body content. Dates exist in some Article schema, but not in rendered HTML. AI systems cannot assess content recency for undated content.

**Fix:** In the Shopify blog article template, enable date display: `{{ article.published_at | date: "%B %d, %Y" }}`. Add a "Last Updated" line where articles have been refreshed. Ensure `datePublished` and `dateModified` are both populated in Article JSON-LD.

---

### 7. Hreflang Not Implemented for EN/ES Store
**Severity: Critical | Effort: Medium | Impact: International SEO, Spanish-speaking traffic**

The site has a fully parallel Spanish store at `/es/` but zero `hreflang` tags on any page. This creates duplicate content risk and prevents Google from serving the correct language version to Spanish-speaking users.

**Fix:** Add to every page's `<head>` — both English and Spanish versions:
```html
<link rel="alternate" hreflang="en" href="https://happimess.com/[path]" />
<link rel="alternate" hreflang="es" href="https://happimess.com/es/[path]" />
<link rel="alternate" hreflang="x-default" href="https://happimess.com/[path]" />
```
Use Shopify Markets or a multilingual app (Weglot/Langify) if not already managing translations through them.

---

## High Priority Issues (Fix Within 30 Days)

### 8. Product Schema Missing aggregateRating — Product Rich Results Blocked
All product pages lack `aggregateRating`. This blocks star ratings from appearing in Google Search, Google Shopping, Google AI Overviews, and Perplexity AI product answers. Once customer reviews exist on-platform, this is the highest-ROI schema addition.

**Fix:** Integrate a Shopify review app (Judge.me, Okendo, Yotpo) that generates `aggregateRating` schema automatically, or add it manually:
```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "4.7",
  "reviewCount": "128",
  "bestRating": "5",
  "worstRating": "1"
}
```

---

### 9. No Bing Webmaster Tools Verification / No IndexNow
No `msvalidate.01` meta tag detected. No IndexNow API key. Without Bing WMT, there is no real-time indexing signal, no crawl rate control, and no Shopping feed pathway. Bing Copilot draws heavily from Bing's index.

**Fix:** Go to bing.com/webmasters, add the `msvalidate.01` meta tag to the Shopify theme header, submit `https://happimess.com/sitemap.xml`, and activate IndexNow for instant URL submission on content updates.

---

### 10. /policies/ Blocked for All Bots
The `robots.txt` blocks `Disallow: /policies/` for all bots. Policy pages (shipping, returns) are frequently cited by AI when answering purchase-intent queries like "does Happimess ship to [location]?" or "what is the return window?"

**Fix:** Add explicit AI crawler entries before the wildcard block:
```
User-agent: GPTBot
Allow: /policies/
Allow: /

User-agent: ClaudeBot
Allow: /policies/
Allow: /

User-agent: PerplexityBot
Allow: /policies/
Allow: /

User-agent: Google-Extended
Allow: /policies/
Allow: /

User-agent: OAI-SearchBot
Allow: /policies/
Allow: /
```

---

### 11. No LinkedIn Company Page (Entity Disambiguation Risk)
A LinkedIn search for "Happimess" surfaces an unrelated Lithuanian nonprofit (happimess.lt). When AI models attempt to resolve the "Happimess" entity, the most structured external data points to the wrong organization.

**Fix:** Create a LinkedIn company page for Happimess.com immediately. Fill out: company name, website URL, industry (Retail/Home Goods), location (New York, US), description, and logo. Then add the LinkedIn URL to the Organization `sameAs` array.

---

### 12. About Us Page Is 200 Words of Generic Copy
The About page has no founding story, no named team, no milestones, no press coverage, no certifications. At ~200 words it is the weakest trust signal on the entire site.

**Fix:** Rebuild the About page to include:
- Founding story with year and origin
- Named founders/team with photos and titles
- Company milestones (year launched, number of products, customers served)
- Any press coverage (logos + links)
- Quality claims backed by evidence (not just stated)
- 800+ words total

---

### 13. Zero External Citations Across All Blog Content
None of the 24+ blog posts contain a single outbound link to an external source. The complete absence of external citations is a strong AI-generated content indicator and reduces credibility for both Google and AI retrieval systems.

**Fix:** Add 2–3 authoritative external citations per blog post. Target: EPA recycling data, NAPO (National Association of Productivity and Organizing Professionals), interior design study data, manufacturer specifications. This is a light editing task across existing posts.

---

### 14. FAQPage Schema Missing from /pages/faqs
The FAQ page exists and contains Q&A content but has no `FAQPage` JSON-LD schema. This is a straightforward AIO trigger.

**Fix:** Add FAQPage schema to the Shopify `/pages/faqs` template wrapping each Q&A in proper `Question`/`Answer` markup.

---

### 15. WebPage Schema Has Null Description on Homepage
`"description": null` in the homepage WebPage schema is an active validation error.

**Fix:** Replace with: `"description": "Happimess is a New York-based home organization brand selling trash cans, storage baskets, hampers, wicker trunks, and custom-fit trash bag subscriptions."`

---

## Medium Priority Issues (Fix Within 90 Days)

### 16. No speakable Property on Any Blog Content
Not a single blog post declares `speakable` sections. This is the direct signal to Google Assistant, AI Overviews, and voice interfaces that content is suitable for reading and summarization.

**Fix:** Add to Article schema in the Shopify article template:
```json
"speakable": {
  "@type": "SpeakableSpecification",
  "cssSelector": ["article h1", "article p:first-of-type", "article h2:first-of-type"]
}
```

---

### 17. No Review Platform Presence
Trustpilot shows 0 reviews. SmartCustomer (formerly Sitejabber) shows 0 reviews. No Google Business Profile reviews visible. AI models answering "is Happimess legit?" or "Happimess reviews" will find a vacuum and may exclude the brand from purchase recommendations.

**Fix:**
1. Claim and complete Google Business Profile (185 Madison Ave, New York)
2. Set up a Trustpilot profile
3. Add a post-purchase review request email sequence
4. Surface review counts on product pages via a Shopify review app

---

### 18. Blog Content Lacks Statistical Density
4 of 7 blog articles reviewed contain zero statistics, market data, or measurable claims. AI models overwhelmingly favor and cite content with specific numbers.

**Fix:** For each existing article, add:
- One market statistic (cited)
- One measurable recommendation with a specific number
- A date/recency anchor ("as of 2025...")

The kitchen trash can size guide demonstrates the right pattern — replicate it across all content.

---

### 19. No Buying Guide / Comparison Content
None of the blog content uses the comparison format that ChatGPT Web Search and Bing Copilot most reliably cite for product queries. There are no "Best [X] of 2025" articles or "Happimess vs. [competitor]" pages.

**Fix:** Create 2–3 structured comparison articles:
- "Best Step-On Trash Cans 2025: Tested and Compared"
- "Best Wicker Storage Baskets: 5 Options Compared by Material and Size"

---

### 20. Paginated Collection Pages Have Generic Titles
`/collections/all?page=2` has the title `"Products – Page 2"` — no brand name, no keywords.

**Fix:** In the Shopify collection template, add dynamic page numbers to the title: `All Products – Page 2 | Happimess`.

---

### 21. ItemList Protocol-Relative and Relative URLs — Invalid Schema
Collection page ItemList schema uses protocol-relative image URLs (`//happimess.com/cdn/...`) and relative product URLs (`/products/...`). Both are invalid per Schema.org spec.

**Fix:** In the Shopify collection template, ensure URL output uses the `| prepend: shop.secure_url` or `| absolute_url` Liquid filter.

---

### 22. Duplicate Product Schema Blocks
The Product schema block renders twice on every product page (once in `<head>`, once in body). Not harmful, but adds page weight.

**Fix:** Audit theme templates to identify which snippet generates the duplicate and remove one instance.

---

### 23. Sitemap Child Files Return 400 Errors
Direct fetch of `sitemap_products_1.xml` and `sitemap_pages_1.xml` returned HTTP 400 errors. Possible Cloudflare/CDN blocking.

**Fix:** Verify accessibility via Google Search Console → Sitemaps. Check Cloudflare rules for any WAF rules blocking `.xml` file fetches by non-browser agents.

---

## Strategic Actions (90+ Days)

### 24. Wikipedia Entity Creation
Wikipedia presence is worth 30 points in the brand authority model — the single highest-value individual signal for AI entity recognition. Building a defensible Wikipedia article requires: 3–5 citations in third-party publications (Business Insider, Forbes Home, Apartment Therapy, Wirecutter).

**Approach:** Pursue HARO/Qwoted contributions from a named team member; pitch a home organization gift guide to a high-DA publication; target a product roundup mention in a major home goods outlet.

---

### 25. Content Cluster Architecture
The blog has ~24 posts but no hub-and-spoke structure. Posts don't interlink, there are no pillar pages, and each post is siloed with a single tag.

**Approach:** Designate one pillar page per category (e.g., "The Complete Guide to Kitchen Trash Cans"), create 6–8 spoke articles that interlink to and from it, and implement Shopify blog tags as navigable taxonomy.

---

### 26. Experience-Layer Content Creation
The most impactful long-term E-E-A-T investment: 3–5 genuine first-person experience pieces that cannot be AI-generated — customer transformation stories with before/after photos, a product testing methodology post, or a "how we design our trash cans" behind-the-scenes piece.

---

## Generated Assets

### A. Ready-to-Deploy llms.txt
See Critical Issue #2 above — full file content provided.

### B. Organization Schema with sameAs
See Critical Issue #3 above — full JSON-LD provided.

### C. Article Schema with speakable + Author Identity
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "[REPLACE: article URL]"
  },
  "headline": "[REPLACE: Article title]",
  "description": "[REPLACE: 150-character summary]",
  "image": { "@type": "ImageObject", "url": "[REPLACE: featured image URL]" },
  "datePublished": "[REPLACE: ISO 8601 date]",
  "dateModified": "[REPLACE: ISO 8601 date]",
  "articleSection": "[REPLACE: e.g. Home Organization]",
  "keywords": "[REPLACE: comma-separated keywords]",
  "inLanguage": "en-US",
  "author": {
    "@type": "Person",
    "name": "[REPLACE: Author real full name]",
    "url": "[REPLACE: https://happimess.com/pages/author-name]",
    "jobTitle": "[REPLACE: e.g. Home Organization Editor]",
    "worksFor": { "@type": "Organization", "name": "Happimess", "url": "https://happimess.com" },
    "sameAs": ["[REPLACE: LinkedIn profile URL]"],
    "knowsAbout": ["home organization", "storage solutions", "trash management"]
  },
  "publisher": {
    "@type": "Organization",
    "name": "Happimess",
    "url": "https://happimess.com",
    "logo": { "@type": "ImageObject", "url": "https://cdn.shopify.com/s/files/1/0491/2909/5325/files/happimess-logo-ai-file_1.svg?v=1697698531" }
  },
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": ["article h1", "article p:first-of-type", "article h2:first-of-type"]
  }
}
```

### D. Product Schema with aggregateRating
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[REPLACE: Product name]",
  "url": "[REPLACE: https://happimess.com/products/slug]",
  "image": ["[REPLACE: absolute HTTPS image URL]"],
  "description": "[REPLACE: product description]",
  "sku": "[REPLACE: SKU]",
  "brand": { "@type": "Brand", "name": "Happimess" },
  "category": "[REPLACE: e.g. Trash Cans]",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "[REPLACE: e.g. 4.7]",
    "reviewCount": "[REPLACE: e.g. 128]",
    "bestRating": "5",
    "worstRating": "1"
  },
  "offers": {
    "@type": "Offer",
    "price": "[REPLACE: price]",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "url": "[REPLACE: product URL]",
    "seller": { "@type": "Organization", "name": "Happimess" }
  }
}
```

---

## Prioritized Action Plan

### Sprint 1 — This Week (Est. 4–6 hours total)

| # | Action | Effort | Impact | Platforms |
|---|--------|--------|--------|-----------|
| 1 | Fix "Happimess Dev" → "Happimess" in Product schema | 30 min | Critical | Google, Gemini, Bing |
| 2 | Create and deploy `llms.txt` | 1 hr | +10 pts | All AI |
| 3 | Add `sameAs` to Organization schema | 30 min | +5 pts | ChatGPT, Gemini, Bing, Perplexity |
| 4 | Add explicit AI crawler rules to `robots.txt` | 30 min | +8 pts | All AI |
| 5 | Fix `"description": null` in WebPage schema | 15 min | Low | Google |
| 6 | Verify site in Bing Webmaster Tools + submit sitemap | 30 min | High | Bing Copilot |
| 7 | Fix author display names in Shopify admin (remove usernames) | 30 min | Critical | All AI |

### Sprint 2 — This Month (Est. 8–12 hours)

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 8 | Enable publication dates on all blog posts | 1 hr | High |
| 9 | Rebuild About Us page (founder story, team, milestones) | 3 hr | High |
| 10 | Add FAQPage schema to /pages/faqs | 2 hr | High |
| 11 | Add `aggregateRating` schema (after setting up review app) | 2 hr | High |
| 12 | Create LinkedIn company page | 30 min | High |
| 13 | Implement hreflang for EN/ES | 2 hr | Critical |
| 14 | Fix ItemList absolute URLs in collection schema | 1 hr | Medium |

### Sprint 3 — This Quarter (Strategic)

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 15 | Add external citations to all 24+ blog posts | 4 hr | High |
| 16 | Create 2–3 structured comparison/buying guide articles | 6 hr | High |
| 17 | Add `speakable` to all Article schema | 2 hr | Medium |
| 18 | Build author bio pages with Person schema | 3 hr | High |
| 19 | Set up Trustpilot + Google Business Profile | 2 hr | High |
| 20 | Investigate and fix sitemap child file 400 errors | 1 hr | Medium |
| 21 | Build content cluster architecture (pillar + spokes) | 8 hr | High |
| 22 | Create 3 experience-layer content pieces | 6 hr | High |

---

## Technical SEO Score Detail

| Sub-Category | Score | Status |
|---|---|---|
| Server-Side Rendering (Shopify) | 95/100 | Excellent |
| Mobile Optimization | 80/100 | Good |
| URL Structure | 82/100 | Good |
| Response & Status Codes | 80/100 | Good |
| Crawlability | 70/100 | Fair |
| Core Web Vitals Risk | 60/100 | Medium Risk |
| Meta Tags & Indexability | 55/100 | Needs Work |
| Security Headers | 40/100 | Poor |

**Technical Score: 67/100 — Fair**

> Note: Shopify's native SSR is a genuine competitive advantage for AI crawlability. All core content (product data, blog text, schema) is present in the initial HTML response — no JavaScript execution required. AI crawlers see everything.

---

## AI Visibility Score Detail

| Component | Score | Notes |
|---|---|---|
| Citability | 38/100 | 2 citation-ready passages; statistical desert elsewhere |
| Brand Mentions | 18/100 | No Wikipedia, no LinkedIn, no Trustpilot |
| Crawler Access | 72/100 | Wildcard allows access; AI bots not explicitly named |
| llms.txt | 0/100 | File does not exist |

**AI Visibility Score: 37/100 — Poor**

**Top citation-ready passages (already on site):**
1. Kitchen trash can size table (4 tiers: gallons / inches / use case) — Score: 71/100
2. Marco dual-bucket product specs (dimensions in metric + imperial) — Score: 71/100
3. Kitchen trash can FAQ pairs (family size + emptying frequency) — Score: 67/100
4. Shipping/Returns FAQ (specific days and fee figures) — Score: 65/100

---

## What's Working (Strengths)

| Strength | Impact |
|----------|--------|
| Shopify SSR — all content in initial HTML | AI crawlers can read everything |
| Clean URL structure (keyword-rich slugs) | Good crawlability + topical signals |
| Active blog (~24 posts, 1,200–3,500 words each) | Content surface area for AI citation |
| Bilingual store (EN + ES with separate sitemaps) | Market reach, language signals |
| WebSite + SearchAction schema (valid) | Sitelinks Search Box eligible |
| BreadcrumbList on product/blog pages | Navigation context for AI |
| Active presence on 5 social platforms | Foundation for brand mentions |
| AI-powered product recommendation tool | Differentiated feature |
| Subscription product line | Unique content angle |
| Sitemap in robots.txt | Crawler discovery |

---

## Scoring Methodology

| Category | Weight | Inputs |
|----------|--------|--------|
| AI Citability & Visibility | 25% | Passage scoring (7 blocks), crawler access, llms.txt, brand mentions |
| Brand Authority Signals | 20% | Wikipedia, Reddit, YouTube, LinkedIn, Trustpilot, press coverage |
| Content Quality & E-E-A-T | 20% | Experience, Expertise, Authoritativeness, Trustworthiness, freshness |
| Technical Foundations | 15% | SSR, CWV, mobile, security, crawlability, hreflang |
| Structured Data | 10% | Schema inventory, validation, completeness, rich result eligibility |
| Platform Optimization | 10% | Google AIO, ChatGPT, Perplexity, Gemini, Bing Copilot |

---

*Report generated by GEO Audit Tool · 5 parallel analysis agents · happimess.com · April 14, 2026*
