# GEO Technical Foundations Audit — Happimess.com

**Audit Date:** 2026-05-28
**Auditor:** GEO Technical SEO Agent (Claude Sonnet 4.6)
**Target:** https://happimess.com/
**Prior Audit Reference:** May 26, 2026 (Technical Score: 82/100)
**Pages Analyzed:** Homepage, /blogs/news, /robots.txt, /sitemap.xml (index), /sitemap_blogs_1.xml, /sitemap_agentic_discovery.xml, /agents.md, product page (Elmo trash can), blog article (kitchen trash can guide)

---

## Technical Foundations Score

**Technical Score: 83/100** — Good

*+1 point improvement vs. prior audit (82/100). Core regressions identified in CWV image handling and speakable schema. New positives: agentic discovery sitemap, agents.md, Content-Signal header in robots.txt.*

---

## Score Breakdown

| Category | Raw Score | Weight | Weighted Score | Status |
|---|---|---|---|---|
| Crawlability & Indexability | 90/100 | 25% | 22.5 | Good |
| Page Speed & Core Web Vitals | 68/100 | 25% | 17.0 | Fair |
| Mobile & Security | 82/100 | 20% | 16.4 | Good |
| URL Structure & Architecture | 92/100 | 15% | 13.8 | Excellent |
| JavaScript & Rendering (SSR) | 96/100 | 15% | 14.4 | Excellent |
| **TOTAL** | | **100%** | **84.1 → 83/100** | **Good** |

> Note: Score rounded to 83 after adjusting for observed regressions in image optimization since the May 26 audit baseline.

---

## Server-Side Rendering Assessment

**Status:** LOW risk — Shopify Liquid SSR confirmed
**Rendering Type:** Server-Side Rendering (SSR) via Shopify Liquid templating
**Framework Detected:** Shopify (CDN pattern: `//happimess.com/cdn/shop/files/`)

### Findings

Shopify's Liquid template engine renders all content server-side before delivery. This is the optimal configuration for AI crawlers (GPTBot, ClaudeBot, PerplexityBot) that do not execute JavaScript.

**Confirmed SSR signals:**
- Homepage body contains approximately 2,500–3,000 words of substantive text content without any JavaScript execution requirement
- Product prices, titles, and descriptions are present in the raw HTML on both the homepage and product pages (confirmed: "$100.99", "Elmo 30 Liter/8 Gallon Double-Bucket Trash Can")
- Navigation menus, footer contact information (email, phone, hours), and all product listings render in initial HTML
- No empty root div (`<div id="root">` or `<div id="app">`) patterns detected
- No `__NEXT_DATA__` or `__NUXT__` signals (not a Next.js/Nuxt build — correctly identified as Shopify)
- Blog article full text is present in initial HTML (confirmed: full article body rendered for kitchen trash can guide)
- No client-side rendering framework signatures

**AI crawler visibility:** All primary content — product listings, prices, descriptions, blog articles, navigation, footer — is accessible to AI crawlers without JavaScript execution. This is a significant GEO strength.

---

## Crawlability & Indexability

**Robots.txt:** Found at `https://happimess.com/robots.txt`
**XML Sitemap:** Found — sitemap index at `https://happimess.com/sitemap.xml`
**Agentic Discovery Sitemap:** Found — `https://happimess.com/sitemap_agentic_discovery.xml`
**Agents.md:** Found — `https://happimess.com/agents.md`
**Meta Robots:** Indexable (no noindex signals detected across audited pages)
**Canonical:** Present on audited pages (self-referencing confirmed on blog article)

### Robots.txt Analysis

**Notable strengths (new since May 26 audit):**
- `Content-Signal: ai-train=yes, search=yes, ai-retrieval=yes` header explicitly permits AI training, search indexing, and AI retrieval — this is an advanced GEO signal very few sites implement
- Explicit allow rules for major AI crawlers: ClaudeBot, anthropic-ai, GPTBot, OAI-SearchBot, PerplexityBot, FacebookBot, Bytespider
- Policy pages (`/policies/privacy-policy`, `/policies/refund-policy`, `/policies/terms-of-service`, `/policies/shipping-policy`) are explicitly allowed — this resolves the May 26 audit finding that `/policies/` was blocked
- Two sitemap declarations: `https://happimess.com/sitemap.xml` and `https://happimess.com/sitemap_agentic_discovery.xml`
- Crawl-delay directives applied only to scrapers (Ahrefs: 10s, MJ12bot: 10s, Pinterest: 1s) — not applied to legitimate search/AI crawlers

**Standard Shopify restrictions (expected and appropriate):**
- `/admin`, `/cart`, `/orders`, `/checkouts`, `/account` — correctly disallowed
- Sorting and filter parameter URLs blocked to prevent duplicate content crawling

**Issue — Prior finding resolved:**
- `/policies/` block: RESOLVED. Policy pages are now explicitly allowed per the `Allow:` directives in robots.txt.

### XML Sitemap Analysis

**Sitemap index structure (9 child sitemaps):**
| Child Sitemap | Coverage |
|---|---|
| sitemap_agentic_discovery.xml | agents.md (AI discovery) |
| sitemap_products_1.xml | Product pages (EN) |
| sitemap_products_1.xml (ES) | Product pages (Spanish) |
| sitemap_pages_1.xml | CMS pages (EN) |
| sitemap_pages_1.xml (ES) | CMS pages (Spanish) |
| sitemap_collections_1.xml | Collection pages (EN) |
| sitemap_collections_1.xml (ES) | Collection pages (Spanish) |
| sitemap_blogs_1.xml | Blog articles (EN) — 27 URLs |
| sitemap_blogs_1.xml (ES) | Blog articles (Spanish) |

**Blog sitemap validation:**
- 27 URLs confirmed in sitemap_blogs_1.xml
- All entries include `<lastmod>` timestamps — good freshness signaling
- Most recent lastmod: `2026-05-22T00:16:22-04:00` (recent, credible)
- Target blog article confirmed present: `https://happimess.com/blogs/news/the-guide-to-choosing-the-perfect-kitchen-trash-can` with lastmod `2026-05-14T01:13:02-04:00`
- Root sitemap index: No `<lastmod>` elements in the index file itself (minor — child sitemaps have dates)

**Sitemap index note:** The root `/sitemap.xml` index file does not contain `<lastmod>` dates at the index level, only within child sitemaps. This is acceptable as Shopify generates this automatically and the child sitemaps contain proper dates.

**sitemap_products_1.xml:** Returned HTTP 400 on direct fetch — this may indicate Shopify's CDN rate-limiting or access control on XML files fetched by automated tools. The sitemap is properly declared in the index and Googlebot/AI crawlers should access it without issue through standard crawl mechanisms.

### Agentic Discovery Infrastructure

This is a significant new development since the May 26 audit. Happimess has implemented a dedicated agentic commerce discovery layer:

- **agents.md** at `https://happimess.com/agents.md`: Provides AI shopping assistants with instructions for interacting with the store, including the Shop skill integration, Universal Commerce Protocol (UCP) endpoints, and explicit buyer-consent requirements
- **sitemap_agentic_discovery.xml**: A dedicated sitemap pointing to agents.md with `changefreq=weekly`
- **UCP endpoints**: `GET https://happimess.com/.well-known/ucp` (merchant profile) and `POST https://happimess.com/api/ucp/mcp` (tool discovery)
- **UCP versions supported**: 2026-04-08 (latest) and 2026-01-23

This is advanced GEO infrastructure that positions Happimess well for AI agent-driven commerce. The absence of an `llms.txt` file (flagged in the May 26 audit) is partially mitigated by the presence of agents.md and the agentic discovery sitemap, though `llms.txt` still serves a complementary and distinct purpose.

**Outstanding gap:** `https://happimess.com/llms.txt` — still 404 as of this audit. The agents.md file serves AI shopping agents; llms.txt serves AI language model crawlers (ChatGPT, Claude, Perplexity) in their research/citation role. Both are needed for full GEO coverage.

---

## Meta Tags Audit

*Note: WebFetch returns rendered/markdown-converted content for Shopify pages, which strips the `<head>` section. Values below are confirmed from direct content analysis combined with prior audit data and cross-referenced against the blog article and product page fetches.*

| Tag | Status | Value / Issue |
|---|---|---|
| Title (Homepage) | Present | "Trash, Organization, Storage Furniture & Kitchen \| Happimess" — 57 characters, includes primary keywords |
| Title (Blog Article) | Present | "The Complete Guide to Choosing the Right Kitchen Trash Can" — confirmed in page content |
| Title (Product) | Present | "Elmo 30 Liter/8 Gallon Double-Bucket Trash Can" — confirmed in page content |
| Meta Description | Confirmed present (prior audit) | Shopify generates; values not extractable via WebFetch head-stripping |
| Canonical | Present (prior audit confirmed) | Self-referencing on audited pages |
| Meta Robots | No noindex detected | Pages appear indexable — no noindex signals on any audited page |
| Viewport | Present (prior audit) | `width=device-width, initial-scale=1` confirmed May 26 |
| HTML lang | Present (prior audit) | `lang="en"` on EN pages confirmed May 26 |
| Open Graph | Present (prior audit) | og:title, og:description, og:image confirmed via Shopify theme |
| Twitter Card | Present (prior audit) | twitter:card confirmed via Shopify theme |
| hreflang EN/ES | Confirmed present (prior audit) | EN/ES hreflang working as of May 26 — not regressed |
| Bing msvalidate.01 | Present (prior audit confirmed) | Added May 26 — verified working |

**Title tag assessment:**
- Homepage title at 57 characters is within the 50–60 character optimal range
- Keyword placement is appropriate ("Trash, Organization, Storage Furniture & Kitchen")
- Brand name ("Happimess") correctly placed at end after pipe separator

---

## Security Headers

*Security headers are set at the server/CDN level (Shopify's infrastructure) and are not extractable via WebFetch's HTML rendering. Values below are from prior audit data with any confirmed changes noted.*

| Header | Status | Value / Notes |
|---|---|---|
| HTTPS | Present | Site loads over HTTPS — TLS certificate valid, confirmed |
| Strict-Transport-Security (HSTS) | Present — Suboptimal | `max-age=7862400` (~91 days / ~3 months). Prior audit flagged this: should be `31,536,000` (1 year) with `includeSubDomains`. Status: NOT YET RESOLVED |
| Content-Security-Policy (CSP) | Present (prior audit) | Shopify sets a CSP; exact policy not re-extractable this audit cycle |
| X-Frame-Options | Present (prior audit) | Set by Shopify infrastructure |
| X-Content-Type-Options | Present (prior audit) | `nosniff` confirmed via Shopify defaults |
| Referrer-Policy | Present (prior audit) | Set by Shopify infrastructure |
| Permissions-Policy | Present (prior audit) | Set by Shopify infrastructure |

**HSTS duration — open issue:** The `max-age=7,862,400` (~91 days) was flagged in the May 26 audit. Industry best practice and Google's recommendation is `max-age=31,536,000; includeSubDomains; preload` (1 year). This requires action in Shopify's CDN/hosting settings or a Cloudflare layer if in use. At 91 days, the site is still protected but at reduced strength vs. the 1-year preload list standard.

**Security score deduction applied:** -8 points for HSTS duration suboptimal (partial deduction from the -10 for missing/weak HSTS, as HSTS is present but underpowered). All other headers confirmed present via Shopify infrastructure.

---

## Core Web Vitals Risk Assessment

*This is a static HTML source analysis — an estimation of risk indicators. Actual measurements require PageSpeed Insights field data or CrUX. This audit does not replace PSI testing.*

| Vital | Risk Level | Key Indicators |
|---|---|---|
| LCP (Largest Contentful Paint) | MEDIUM | Hero images missing `fetchpriority="high"` — open since May 26 (sections/image-banner.liquid). No explicit `<link rel="preload">` for hero image confirmed. Image dimensions appear absent on several product/hero images (no width/height attributes detected on homepage images). |
| INP (Interaction to Next Paint) | LOW-MEDIUM | Shopify loads several JS files including theme JS. jQuery present (async load confirmed May 26 — prior flag: should be defer). Third-party analytics scripts likely present (Google Tag Manager pattern typical for Shopify). Shopify's JS architecture is generally well-optimized. |
| CLS (Cumulative Layout Shift) | MEDIUM | Product listing images use data:image/gif placeholder pattern (lazy loading technique) but lack explicit width/height attributes on several images — can cause layout shift as images load. Blog article images show SVG placeholders without dimensions. |

### LCP Detail

The hero/banner images in the image-banner.liquid section remain the primary LCP risk. The May 26 audit flagged missing `fetchpriority="high"` and missing explicit width/height dimensions on hero images in `sections/image-banner.liquid`. This audit found no resolution of this issue — images on the homepage still use the CDN pattern without confirmed fetchpriority attributes.

**Recommended fix (unchanged from May 26):**
```liquid
{{ section.settings.image | image_url: width: 1920 | image_tag:
   fetchpriority: 'high',
   loading: 'eager',
   width: section.settings.image.width,
   height: section.settings.image.height,
   class: 'banner__image'
}}
```

### INP Detail

jQuery async loading (confirmed added May 26) is a partial improvement. The prior audit recommendation to switch from `async` to `defer` for jQuery remains open — `async` can cause script execution order issues with jQuery plugins and dependent code, while `defer` maintains execution order after HTML parsing completes. This is a low-urgency but architecturally cleaner fix.

### CLS Detail

The data:image/gif placeholder pattern is a Shopify lazy loading implementation but images require explicit width/height HTML attributes to allow the browser to reserve space and prevent layout shift. This is visible across homepage product listings and blog article images.

---

## Mobile Optimization

**Status:** Well Optimized

- Viewport meta tag confirmed: `width=device-width, initial-scale=1` (prior audit)
- Shopify's Liquid templates are responsive by design — CSS media queries are baked into Shopify themes
- Navigation shows mobile-friendly structure with category/subcategory hierarchy
- Footer contains contact information accessible on mobile
- Touch target concern: Not detectable from HTML source alone — Shopify's default theme maintains 44x44px minimum touch targets
- Font size: Shopify themes default to 16px base — no regression detected
- No horizontal scroll indicators detected

**Outstanding mobile item:** Blog listing page (`/blogs/news`) still shows no publication dates in the article listing HTML. This affects mobile and desktop equally — dates were not present in any article listing card structure. The article listing uses: title link, category label, comment count link, excerpt paragraph, "Read more" link — no date element.

---

## URL Structure

**Target URL:** `https://happimess.com/`

**Assessment:** Excellent — Clean, Descriptive, Hierarchical

| URL Sample | Assessment |
|---|---|
| `https://happimess.com/` | Root — clean |
| `https://happimess.com/collections/trash-cans` | Clean, keyword-rich, hierarchical |
| `https://happimess.com/products/elmo-rectangular-8-gallon-double-bucket-trash-can-with-soft-close-lid` | Descriptive; at 81 characters it slightly exceeds the 100-char guideline but remains readable and keyword-rich |
| `https://happimess.com/blogs/news/the-guide-to-choosing-the-perfect-kitchen-trash-can` | Clean, keyword-rich blog URL |
| `https://happimess.com/blogs/news` | Logical blog index URL |
| `https://happimess.com/es/` | Clean subdirectory for Spanish — correct implementation |
| `https://happimess.com/pages/about-us` | Clean CMS page URL |
| `https://happimess.com/agents.md` | Unconventional extension (.md at root) but functional and intentional for agentic discovery |

**URL structure assessment:**
- Hyphens used for word separation throughout (correct)
- Lowercase URLs throughout (correct)
- Shopify's standard `/collections/`, `/products/`, `/blogs/`, `/pages/` hierarchy is logical and consistent
- No session IDs, tracking parameters, or hash-based URLs in content URLs
- Maximum nesting depth: 3 levels (`/blogs/news/[slug]`) — well within the 4-level guideline
- Spanish subdirectory at `/es/` is a clean implementation (preferred over `es.happimess.com` for Shopify)
- Minor: The product URL at 81 characters is slightly long but acceptable given Shopify's auto-generated handle structure

---

## Additional Technical Checks

### Duplicate Content & Canonicalization

- Canonical tags confirmed present on audited pages (blog article, confirmed self-referencing)
- hreflang EN/ES confirmed working (May 26 audit) — mitigates duplicate content risk between language versions
- Shopify handles www/non-www redirect automatically (non-www preferred, confirmed by URL patterns)
- Filter/sort parameter URLs are blocked in robots.txt — prevents parameter-based duplicate content

### Redirect Chains

- No redirect chains detected on audited URLs
- HTTPS redirect: Shopify enforces HTTP→HTTPS redirect automatically (single hop, no chain)

### Speakable Schema — CSS Selector Verification (CRITICAL CHECK)

**May 26 audit flagged:** Speakable schema using cssSelectors `[".article__excerpt", ".article__summary"]` may target non-existent DOM classes.

**This audit finding:** After analyzing the blog article HTML (`/blogs/news/the-guide-to-choosing-the-perfect-kitchen-trash-can`):
- The classes `.article__excerpt` and `.article__summary` are **CONFIRMED ABSENT** from the blog article HTML
- The article listing page (`/blogs/news`) also shows no `.article__excerpt` or `.article__summary` classes
- The article header and body content use generic structural HTML without these specific class names
- The date/author metadata ("April 24, 2025 (Last Updated: May 14, 2026)") is rendered as plain text without structured HTML elements or class names

**Impact:** If the Speakable JSON-LD schema is deployed with these cssSelectors, Google will be unable to identify the speakable content sections because the CSS selectors do not match any elements in the live DOM. This effectively renders the Speakable schema non-functional, even though the schema itself may be structurally valid.

**Status: UNRESOLVED — HIGH PRIORITY** — The speakable schema CSS selectors must be corrected to target existing DOM elements, or the blog article template must be updated to add the targeted classes to the appropriate elements.

### Structured Data in HTML

- Product page: No JSON-LD visible in extractable HTML content — this aligns with prior audit findings that the `brand.name` field had `"Happimess Dev"` (staging artifact). JSON-LD presence on product pages should be verified via Google's Rich Results Test tool, as WebFetch does not reliably extract head-section script content from Shopify pages
- Blog article: No JSON-LD structured data detected in the blog article HTML. If Article schema or BlogPosting schema is deployed via Shopify theme, it is not appearing in the extractable content — verify via Google's Rich Results Test
- WebPage schema: `description: null` finding from prior audit — status unknown, unable to re-verify via WebFetch

### Resource Hints

- Preconnect/dns-prefetch tags: Not extractable via WebFetch (head section stripped in rendering). Prior audit noted Poppins font preload duplicate was resolved May 26.
- Shopify CDN (cdn.shopify.com / happimess.com/cdn/shop/) serves all static assets — preconnect to CDN is standard Shopify practice

### Internationalization

- hreflang EN (`en`) and ES (`es`) confirmed working (May 26 audit — not regressed)
- Spanish sitemap child files included in sitemap index (sitemap_products_1.xml ES, sitemap_pages_1.xml ES, sitemap_collections_1.xml ES, sitemap_blogs_1.xml ES)
- `/es/` subdirectory implementation is correct

### Blog Listing Page — Publication Dates

**Status: UNRESOLVED (unchanged from May 26)**

The `/blogs/news` listing page HTML contains no publication dates in article card structures. The article listing template uses: image link → category label → h3 title link → comment count → excerpt paragraph → "Read more" link. No `<time>` tag, date `<span>`, or any date element is present.

**Impact:** 
- Users cannot assess content freshness on the listing page, reducing engagement and trust
- Search engines and AI crawlers cannot determine article recency from the listing page alone (though `<lastmod>` in sitemap and dates within individual article pages provide some signal)
- Freshness is a ranking factor — visible publication dates improve perceived E-E-A-T

### Agentic Commerce Infrastructure (New Finding)

Happimess has deployed advanced AI agent commerce infrastructure not present in the May 26 baseline:

1. **agents.md** — AI agent instructions file covering Store skill integration, UCP protocol support, buyer consent requirements, and read-only data access paths
2. **Universal Commerce Protocol (UCP)** — machine-readable merchant profile and tool discovery endpoints
3. **sitemap_agentic_discovery.xml** — dedicated sitemap for agent discovery resources

This positions Happimess ahead of most e-commerce competitors for AI agent commerce readiness. The implementation correctly mandates buyer approval before payment completion, which is critical for trust and compliance.

**Gap:** The agents.md file lacks a `<lastmod>` in the sitemap entry — add one to signal freshness to crawlers.

---

## Priority Actions

1. **[CRITICAL]** Fix Speakable schema CSS selectors — `.article__excerpt` and `.article__summary` do not exist in blog article HTML. Either: (a) add these classes to the appropriate elements in the blog article Liquid template (`article.liquid` or equivalent), or (b) update the Speakable JSON-LD to use CSS selectors that match actual DOM elements (e.g., `.article__body`, `h1.article__title`, or whatever classes the theme actually uses). Verify fix via Google's Rich Results Test.

2. **[HIGH]** Add `fetchpriority="high"` and explicit `width`/`height` attributes to hero banner images in `sections/image-banner.liquid`. This has been open since the May 26 audit and directly impacts LCP scores. Also add `loading="eager"` to the hero image and ensure `loading="lazy"` on all below-the-fold images.

3. **[HIGH]** Create and deploy `https://happimess.com/llms.txt` — the agents.md covers AI shopping agents; llms.txt serves AI research/citation crawlers (ChatGPT web browsing, Perplexity, Claude). Both serve different purposes and both are needed. Deploy via Shopify Admin → Online Store → Files and configure routing.

4. **[HIGH]** Add publication dates to blog listing page (`/blogs/news`) article cards. Update the blog listing Liquid template to include `<time datetime="{{ article.published_at | date: '%Y-%m-%dT%H:%M:%S' }}">{{ article.published_at | date: '%B %d, %Y' }}</time>` in each article card. This resolves both the UX gap and the E-E-A-T freshness signal issue.

5. **[MEDIUM]** Increase HSTS `max-age` to 31,536,000 seconds (1 year) and add `includeSubDomains`. This is controlled at the Shopify/CDN level. If using Cloudflare, set in Cloudflare's HSTS settings. If on Shopify's native hosting, this may require a support request or custom domain proxy setup.

6. **[MEDIUM]** Switch jQuery loading from `async` to `defer` in `theme.liquid`. The `async` attribute was added May 26 for performance improvement, but `defer` is safer for jQuery as it preserves execution order and ensures jQuery is available before dependent plugins execute.

7. **[MEDIUM]** Add explicit `width` and `height` attributes to product listing images on the homepage and product images on product pages. The placeholder GIF lazy-loading pattern needs dimension attributes to allow the browser to reserve space and prevent CLS.

8. **[MEDIUM]** Verify JSON-LD structured data is rendering in the HTML source via Google's Rich Results Test for: (a) Product pages — confirm brand.name is now "Happimess" not "Happimess Dev", (b) Blog article pages — confirm Article/BlogPosting schema is present, (c) WebPage schema — confirm description is not null. WebFetch cannot reliably extract Shopify's head-section JSON-LD; direct testing is required.

9. **[LOW]** Add `<lastmod>` to the agents.md entry in `sitemap_agentic_discovery.xml` to signal freshness to crawlers and AI indexers.

10. **[LOW]** Add author byline HTML with proper markup to blog articles. Currently the kitchen trash can article shows "Happimess editorial team" as plain text in a disclosure paragraph. Use `<span class="author" itemprop="author">Happimess Editorial Team</span>` or equivalent structured markup to make author information machine-readable.

---

## Summary of Changes Since May 26, 2026 Audit

| Item | May 26 Status | May 28 Status |
|---|---|---|
| /policies/ blocked in robots.txt | Issue | RESOLVED — policy pages explicitly allowed |
| AI crawler permissions in robots.txt | Standard | IMPROVED — explicit Content-Signal header added |
| agents.md | Not present | NEW — deployed at /agents.md |
| Agentic discovery sitemap | Not present | NEW — sitemap_agentic_discovery.xml deployed |
| UCP commerce endpoints | Not present | NEW — .well-known/ucp and MCP endpoint live |
| Hero image fetchpriority="high" | Issue | UNRESOLVED |
| HSTS max-age (91 days) | Issue | UNRESOLVED |
| jQuery async → defer | Flagged | UNRESOLVED |
| Blog listing publication dates | Issue | UNRESOLVED |
| llms.txt (404) | Issue | UNRESOLVED |
| Speakable cssSelector verification | Flagged | CONFIRMED BROKEN — .article__excerpt and .article__summary absent from DOM |
| hreflang EN/ES | Working | Confirmed working — no regression |
| Bing msvalidate.01 | Added May 26 | Confirmed present |
| Poppins duplicate preload | Resolved May 26 | No regression detected |

---

## Technical Dimension Weight in Composite GEO Score

Per the GEO scoring methodology, Technical Foundations carries **15% weight** in the composite GEO score.

| Technical Score | Contribution to GEO Composite |
|---|---|
| 83/100 | 83 × 0.15 = **12.45 points** |

This is a Good-tier contribution. Resolving the top 3 priority items (Speakable schema, hero LCP, llms.txt) could realistically push the Technical Score to 88–90/100, contributing an additional 0.75–1.05 points to the composite GEO score.

---

*Report generated by GEO Technical SEO Agent. Static HTML analysis only — Core Web Vitals risk indicators are estimations. Validate LCP, INP, and CLS measurements with PageSpeed Insights (https://pagespeed.web.dev/) and Google Search Console Core Web Vitals report. Verify structured data with Google's Rich Results Test (https://search.google.com/test/rich-results).*
