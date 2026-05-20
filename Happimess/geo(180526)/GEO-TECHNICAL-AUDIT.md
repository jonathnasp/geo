# GEO Technical SEO Audit — Happimess
**URL:** https://happimess.com/  
**Platform:** Shopify (SSR)  
**Audit Date:** 2026-05-18  

---

## Technical Score: 71 / 100 — Fair

| Category | Score | Weight | Weighted |
|----------|-------|--------|---------|
| Server-Side Rendering | 95/100 | 25% | 23.75 |
| Crawlability | 82/100 | 15% | 12.30 |
| Indexability | 72/100 | 15% | 10.80 |
| Mobile Optimization | 75/100 | 10% | 7.50 |
| Core Web Vitals Risk | 60/100 | 10% | 6.00 |
| Security Headers | 50/100 | 10% | 5.00 |
| URL Structure | 80/100 | 5% | 4.00 |
| Response & Status | 80/100 | 5% | 4.00 |
| International (hreflang) | 20/100 | 5% | 1.00 |

---

## 1. Server-Side Rendering — 95/100 ✅

**Framework:** Shopify (Liquid templating)  
**Rendering type:** SSR — fully server-rendered HTML

All substantive content is present in the initial HTML response without JavaScript execution:
- Product names, descriptions, prices
- Blog article body text and headings
- FAQ question-answer pairs
- Navigation and category structure

**AI crawler impact:** GPTBot, ClaudeBot, PerplexityBot, and all other AI crawlers that do not execute JavaScript receive the full content. This is the most important positive technical signal for GEO.

**One caveat:** Product images use `data:image/gif;base64` and `data:image/svg+xml` placeholder URIs in the HTML source. The actual CDN image URLs are injected by JavaScript as images enter the viewport. AI crawlers parsing raw HTML will not see product images — they see placeholder data URIs instead. Text content is unaffected.

---

## 2. Crawlability — 82/100 ✅

### robots.txt

**Status:** Well-configured — see `GEO-CRAWLER-ACCESS.md` for full analysis.

Key points:
- 10 AI crawlers explicitly granted `Allow: /`
- Standard Shopify commerce paths blocked (admin, cart, checkout, account)
- Filter parameter variants blocked (`?sort_by`, `+filter`) — prevents duplicate content crawling
- `Content-Signal: ai-train=yes, search=yes, ai-retrieval=yes` present
- Sitemap declared: `https://happimess.com/sitemap.xml`
- `/policies/` blocked with 3 specific Allow overrides for trust pages

**Minor issue:** Policy Allow overrides appear after the `Disallow: /policies/` rule — should appear before for deterministic parser behavior.

### Sitemap

**Status:** Comprehensive, 9 sub-sitemaps, ~826 total URLs

| Sub-sitemap | URLs | Lastmod | Notes |
|-------------|------|---------|-------|
| sitemap_products_1.xml | 332 | ✅ All present | Homepage listed here (Shopify quirk) |
| sitemap_collections_1.xml | 103 | ✅ | EN collections |
| sitemap_pages_1.xml | 15 | ✅ | EN pages |
| sitemap_blogs_1.xml | 26 | ✅ | 26 blog posts |
| es/sitemap_products_1.xml | 181 | ⚠️ First entry missing lastmod | ES products |
| es/sitemap_collections_1.xml | 125 | ✅ | ES collections |
| es/sitemap_pages_1.xml | 15 | ✅ | ES pages |
| sitemap_agentic_discovery.xml | 3 | None | llms.txt, llms-full.txt, agents.md |
| sitemap_index.xml | — | None at index level | Master index (no lastmod on index entries) |

**Total:** ~826 URLs across EN + ES + AI discovery files

**Positive:** All sub-sitemaps include current `lastmod` dates (most recent: May 18, 2026 for products). This is a strong freshness signal for all crawlers.

**Notable:** `sitemap_agentic_discovery.xml` is a custom addition referencing AI discovery files. This is a best-practice forward-looking addition.

**Issue:** Homepage appears inside `sitemap_products_1.xml` — architecturally odd but not harmful. Shopify platform behavior.

---

## 3. Indexability — 72/100 ⚠️

### Meta Robots
No `noindex` directives found on: homepage, `/pages/faqs`, `/blogs/news`, blog articles. All key content pages are indexable.

### Title Tags

| Page | Current Title | Assessment |
|------|--------------|-----------|
| Homepage | "Trash, Organization, Storage Furniture & Kitchen \| Happimess" | ✅ Good — 56 chars, keyword-rich |
| ES Homepage | "Happimess - Vive con todo lo que amas" | ✅ Adequate — 38 chars |
| /pages/faqs | **"Faqs"** | ❌ Critical weakness — no keywords, no brand name |
| /blogs/news | "From The Mess Experts" | ⚠️ Weak — brand name absent, no category keywords |

### Meta Descriptions
Could not be extracted by the fetch tool (head section stripped). Shopify generates meta descriptions automatically from page content if not manually set. **Action:** Audit all key pages in Shopify Admin → SEO fields and set manual descriptions.

Key pages requiring manual meta descriptions:
- `/pages/faqs` — Current auto-generated likely leads with "Faqs" which is useless
- `/blogs/news` — Should describe the blog's focus and topic breadth
- `/pages/about-us` — Should include company credibility signals (NYC, testing protocol)

### Canonical Tags
Expected present per Shopify default (auto-generates `rel="canonical"` pointing to primary URL). Unverifiable from HTML-converted fetch. **Action:** Spot-check directly on collection pages with filter parameters — canonical should point to the base collection URL, not the filtered variant.

### Hreflang — MISSING (Critical)

**Status:** ❌ Entirely absent — highest-priority technical issue

The site operates a full Spanish mirror at `/es/` covering:
- 181 ES product pages
- 125 ES collection pages  
- 15 ES pages
- Estimated 26 ES blog posts

**None of these pages have hreflang annotations.** Neither on-page meta tags nor sitemap xhtml:link annotations exist.

**Impact:**
1. Google receives two complete versions of every page (~400 EN + ~400 ES) with no language signal
2. Google may consolidate rankings onto one language unpredictably
3. Spanish users may be served English results and vice versa
4. AI models reading both versions without language context may conflate EN/ES content

**Fix — On-Page (theme.liquid):**

Add to `<head>` in `theme.liquid`:

```liquid
{% if request.locale.iso_code == 'en' %}
  <link rel="alternate" hreflang="en" href="{{ canonical_url }}" />
  <link rel="alternate" hreflang="es" href="{{ 'https://happimess.com/es' | append: request.path }}" />
  <link rel="alternate" hreflang="x-default" href="{{ canonical_url }}" />
{% else %}
  <link rel="alternate" hreflang="es" href="{{ canonical_url }}" />
  <link rel="alternate" hreflang="en" href="{{ 'https://happimess.com' | append: request.path | remove: '/es' }}" />
  <link rel="alternate" hreflang="x-default" href="{{ 'https://happimess.com' | append: request.path | remove: '/es' }}" />
{% endif %}
```

**Fix — Sitemaps:**

Shopify's native sitemap does not support hreflang `xhtml:link` annotations. Options:
1. **Shopify SEO app** (SEO Manager, Hreflang Manager, Weglot) — most add hreflang to sitemaps automatically
2. **Custom sitemap** — generate a custom sitemap via a Shopify app proxy that includes xhtml:link annotations

---

## 4. Mobile Optimization — 75/100 ✅

**Status:** Likely optimized (Shopify default)

- Shopify themes use responsive CSS (flexbox/grid) and meet mobile layout requirements by default
- Viewport meta tag expected: `width=device-width, initial-scale=1`
- Button and link touch targets: Shopify default themes meet 44×44px minimum
- Base font size: 16px+ (Shopify default)
- Image lazy-loading: Present (Shopify lazy-load pattern)

**Known mobile-specific concern:** The image dimension gap (see Core Web Vitals below) affects mobile more severely than desktop — layout shifts are more pronounced on slower mobile connections where images load progressively.

---

## 5. Core Web Vitals Risk — 60/100 ⚠️

These are risk indicators from HTML analysis, not measured field data. Verify with PageSpeed Insights at `pagespeed.web.dev`.

### LCP (Largest Contentful Paint) — Medium Risk

- Hero images use `data:image/gif;base64` placeholder URIs in HTML source; actual CDN image URLs are injected by JavaScript
- No `<link rel="preload" as="image">` for the hero image
- Images served from Shopify CDN (Fastly) — generally fast, but no preload means the hero image competes with other resource requests

**Fix:** Identify the primary hero image URL and add to `theme.liquid` `<head>`:
```html
<link rel="preload" as="image" href="[HERO_IMAGE_CDN_URL]" fetchpriority="high">
```
The hero image URL changes with seasonal promotions — consider a Liquid variable: `{{ section.settings.hero_image | image_url: width: 1200 }}`.

### INP (Interaction to Next Paint) — Medium Risk

- Shopify themes load multiple third-party scripts (analytics, chat widget, review app)
- JavaScript bundle loading pattern is typical for Shopify themes
- Async/defer patterns unverifiable from fetch

**General Shopify INP guidance:**
- Audit third-party scripts in Shopify Admin → Online Store → Themes → Edit Code → `theme.liquid`
- Defer non-critical scripts (chat widgets, analytics) until after first interaction
- Remove unused Shopify apps — each adds script weight even if not actively used

### CLS (Cumulative Layout Shift) — Medium-High Risk

**Root cause confirmed:** Product images, collection images, and blog images all lack explicit `width` and `height` attributes in the HTML source. When images load from the CDN (replacing the base64 placeholders), they cause layout shift because the browser has not reserved space.

**Fix — Shopify Liquid (apply to all image templates):**

In `product-card.liquid`, `collection-product-grid.liquid`, and `article.liquid`, find `<img>` tags and update:

```liquid
{{- Before -}}
<img src="{{ image | image_url: width: 600 }}" alt="{{ image.alt }}">

{{- After -}}
<img 
  src="{{ image | image_url: width: 600 }}"
  width="{{ image.width }}"
  height="{{ image.height }}"
  loading="lazy"
  alt="{{ image.alt }}"
>
```

Using Shopify's `image.width` and `image.height` object properties ensures the browser reserves the correct aspect ratio before the image loads, eliminating CLS from image loading.

---

## 6. Security Headers — 50/100 ⚠️

HTTP response headers could not be captured from the HTML fetch tool. Assessment based on Shopify/Fastly infrastructure defaults.

| Header | Expected Status | Notes |
|--------|----------------|-------|
| HTTPS | ✅ Confirmed | All URLs are `https://` |
| HTTP → HTTPS redirect | ✅ Expected | Shopify enforces HTTPS by default |
| HSTS (Strict-Transport-Security) | ✅ Expected | Shopify CDN (Fastly) typically sets HSTS |
| X-Content-Type-Options | ✅ Expected | Shopify typically sets `nosniff` |
| X-Frame-Options | ⚠️ Unknown | Not confirmed |
| Content-Security-Policy | ⚠️ Likely absent | Shopify does not set CSP by default |
| Referrer-Policy | ⚠️ Unknown | Not confirmed |
| Permissions-Policy | ⚠️ Unknown | Not confirmed |

**Action:** Run `curl -I https://happimess.com` or use `securityheaders.com` to capture actual headers and identify any missing.

**CSP note:** Content-Security-Policy is absent on most Shopify stores because Shopify's theme app system uses inline scripts that a strict CSP would block. This is an ecosystem limitation, not a Happimess-specific issue. Document it but do not attempt to fix without expert assistance — an incorrect CSP will break Shopify functionality.

---

## 7. URL Structure — 80/100 ✅

| Signal | Status | Notes |
|--------|--------|-------|
| HTTPS everywhere | ✅ Pass | All URLs confirmed https:// |
| Lowercase URLs | ✅ Pass | |
| Hyphens as separators | ✅ Pass | |
| Keyword-rich slugs | ✅ Pass | `/products/abrahamus-8-gallon-step-open-trash-can` — descriptive |
| Clean hierarchy | ✅ Pass | `/products/`, `/collections/`, `/pages/`, `/blogs/news/` — clear 3-level max |
| Session IDs / tracking params | ✅ Pass | None present |
| Filter params blocked | ✅ Pass | Blocked in robots.txt |
| URL length | ⚠️ Warn | Some product slugs exceed 80 chars (auto-generated from full product names) |
| /collections/all | ⚠️ Minor | Generic "all" slug — low keyword value but not harmful |

**Long URL example:** `/products/adaline-1811-classic-farmhouse-handwoven-hyacinth-rectangular-underbed-storage-bin-with-wheels-and-handles` — 115 characters in slug alone. This is a Shopify auto-generation issue; do not shorten without 301 redirect chains (not worth it for existing products).

---

## 8. International SEO — 20/100 ❌

This is the most impactful indexability gap outside of hreflang.

**Current state:**
- EN site: `https://happimess.com/` — full catalog (~476 pages)
- ES site: `https://happimess.com/es/` — full catalog (~321 pages)
- Language signal: None. No hreflang tags. No language meta tags confirmed.

**Risk assessment:**
- Google's crawl may *canonicalize* the EN version as the preferred version of all pages, suppressing ES from SERPs
- ES users searching in Spanish may not see the `/es/` pages at all if Google doesn't know they exist for that language context
- AI models encountering both versions may output inconsistent information (mixing EN and ES product descriptions)

**Shopify note:** The `/es/` subdirectory structure is correct for Shopify's international SEO setup. The missing piece is simply the annotation layer (hreflang tags + sitemap annotations).

---

## 9. Page-Specific Issues

### /pages/faqs

| Issue | Severity | Fix |
|-------|----------|-----|
| Title tag: "Faqs" | High | Change to "Frequently Asked Questions \| Happimess" in Shopify Admin → Pages → FAQs → SEO title |
| No FAQPage schema | High | See `GEO-SCHEMA-REPORT.md` Fix 10 |
| No BreadcrumbList | Low | See `GEO-SCHEMA-REPORT.md` Fix 8 |

### /blogs/news

| Issue | Severity | Fix |
|-------|----------|-----|
| Title: "From The Mess Experts" | Medium | Change to "Home Organization Blog \| Happimess" — includes brand name and topic |
| No dates visible in listing | Medium | Update blog-template.liquid to render `published_at` |
| Blog schema description empty | Low | See `GEO-SCHEMA-REPORT.md` Fix 6 |

### Homepage

| Issue | Severity | Fix |
|-------|----------|-----|
| No hero image preload | Low | Add `<link rel="preload">` — see Core Web Vitals section |
| WebPage name: "Home" | Low | Change to full page title in schema |
| No BreadcrumbList | Low | Not standard on homepage — skip |

---

## Priority Actions

| # | Issue | Severity | Effort | Impact |
|---|-------|----------|--------|--------|
| 1 | Add hreflang to `theme.liquid` (EN/ES) | Critical | Medium (2–4 hrs) | All search engines + AI platforms |
| 2 | Install hreflang SEO app for sitemap annotations | Critical | Low (30 min) | Closes sitemap gap |
| 3 | Fix /pages/faqs title tag: "Faqs" → "Frequently Asked Questions \| Happimess" | High | Low (5 min) | AIO, Bing, Google |
| 4 | Add `width` and `height` to all `<img>` tags in theme templates | High | Medium (1–2 hrs) | CLS Core Web Vital |
| 5 | Add `<link rel="preload">` for hero image | Medium | Low (15 min) | LCP Core Web Vital |
| 6 | Fix blog listing title: "From The Mess Experts" → "Home Organization Blog \| Happimess" | Medium | Low (5 min) | SEO, click-through rate |
| 7 | Show publication dates in blog listing | Medium | Low (30 min) | Perplexity, AIO freshness |
| 8 | Verify security headers via securityheaders.com | Low | Low (15 min) | Security assessment only |
| 9 | Fix policy Allow override ordering in robots.txt | Low | Low (5 min) | Unnamed bot clarity |
| 10 | Verify canonical tags on collection pages | Low | Low (15 min) | Duplicate content safety |

---

## Sitemap Submission Checklist

| Search Engine | Status | Action |
|--------------|--------|--------|
| Google Search Console | Unknown | Verify domain; submit `https://happimess.com/sitemap.xml` |
| Bing Webmaster Tools | ❌ Not verified | Verify + submit sitemap (see `GEO-PLATFORM-OPTIMIZATION.md`) |
| Yandex (optional) | Unknown | N/A for US market |

---

## Shopify-Specific Technical Notes

| Topic | Assessment |
|-------|-----------|
| Theme: SSR | ✅ All content in initial HTML — no rendering risk for AI crawlers |
| CDN: Fastly | ✅ Global CDN ensures low TTFB for most crawlers |
| Liquid templates | ✅ Clean URL generation, no dynamic params in canonical URLs |
| App bloat | ⚠️ Unknown — each installed app adds script weight; audit unused apps |
| Theme version | Unknown — if using a deprecated theme (Debut, Brooklyn), upgrade to current Dawn or equivalent |
| Shopify Pages speed | ✅ Shopify infrastructure is generally fast (95th percentile ~1.5s TTFB on Shopify CDN) |

---

*Technical SEO audit conducted 2026-05-18. Output file: GEO-TECHNICAL-AUDIT.md*
