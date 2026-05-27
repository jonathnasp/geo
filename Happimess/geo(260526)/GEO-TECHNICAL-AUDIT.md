# GEO Technical Audit — happimess.com
**Generated:** May 26, 2026  
**Platform:** Shopify (SSR) + Cloudflare CDN  
**Scope:** Crawlability, indexability, security, performance, URL structure, mobile, hreflang

---

## Technical Score: 82 / 100

| Category | Score | Status |
|----------|-------|--------|
| Security (HTTPS, headers) | 78/100 | HSTS too short; missing 2 headers |
| Crawlability & Indexability | 85/100 | robots.txt syntax defect; policy pages partially blocked |
| Sitemap | 95/100 | Comprehensive; all sub-sitemaps present |
| URL Structure & Canonicals | 95/100 | Clean canonical chain; proper redirects |
| Mobile Optimization | 98/100 | Viewport set; responsive confirmed |
| Hreflang (EN/ES) | 90/100 | Implemented on all page types ✅ |
| Performance (TTFB/size) | 72/100 | Product HTML 1MB; homepage OG image undersized |
| Open Graph / Social | 75/100 | Homepage OG image 280×280 (too small) |

**Composite: 82/100** — Good. No critical issues; 4 quick fixes close the gap to ~88.

---

## What's Working Well

| Signal | Status | Detail |
|--------|--------|--------|
| HTTPS | ✅ | All pages serve over HTTPS |
| HSTS | ✅ Present | max-age=7,889,238s (~91 days) — present but short |
| HTTP→HTTPS redirect | ✅ 301 | Confirmed permanent redirect |
| www→non-www redirect | ✅ 301 | Confirmed permanent redirect |
| Cloudflare CDN | ✅ | Global edge network; DDoS protection |
| HTTP/3 (QUIC) | ✅ | Alt-Svc: h3=":443" — modern protocol support |
| Canonical tags | ✅ | Present on homepage, product, blog pages |
| Hreflang | ✅ | x-default + en + es on all page types |
| Viewport meta tag | ✅ | `width=device-width, initial-scale=1` |
| Robots.txt | ✅ | 15 AI crawlers explicitly allowed |
| robots.txt AI signal | ✅ | Content-Signal header declaration |
| Sitemap index | ✅ | 9 sub-sitemaps (products, pages, collections, blogs × EN + ES) |
| agentic_discovery sitemap | ✅ | Listed first in sitemap index |
| Lazy loading | ✅ | 24 images on homepage |
| Preconnect hints | ✅ | cdn.shopify.com, fonts.shopifycdn.com, shop.app |
| X-Frame-Options | ✅ | DENY |
| X-Content-Type-Options | ✅ | nosniff |
| X-XSS-Protection | ✅ | 1; mode=block |
| CSP | ✅ | block-all-mixed-content, upgrade-insecure-requests |
| Server-side rendering | ✅ | Full HTML in initial response (Shopify SSR) |
| Open Graph (product) | ✅ | 1200×630 OG image on product pages |

---

## Issues Found

### 🟠 High Priority

#### 1. HSTS `max-age` Below Google Recommendation
**Current:** `strict-transport-security: max-age=7889238` (~91 days)  
**Recommended:** `max-age=31536000` (1 year) — Google's minimum for HSTS preload eligibility  
**Impact:** Google and browsers require 1-year HSTS for preload list inclusion. Preload strengthens HTTPS trust signal.  
**Fix:** In Cloudflare dashboard → SSL/TLS → Edge Certificates → set HSTS max-age to 12 months. Also enable `includeSubDomains` and `preload` directive if applicable.

```
# Target HSTS header:
strict-transport-security: max-age=31536000; includeSubDomains; preload
```

#### 2. robots.txt Syntax Defect — Missing Blank Line
**Location:** Between `adsbot-google` block and `User-agent: Nutch`  
**Current state (from live robots.txt):**
```
User-agent: adsbot-google
Disallow: ...
Disallow: /services/login_with_shop
↑ NO BLANK LINE HERE ↑
User-agent: Nutch
Disallow: /
```
**RFC 9309 violation:** Each User-agent group must be separated by a blank line. Without it, Nutch's `Disallow: /` may be parsed as part of the adsbot-google group, or the whole block may be misinterpreted.  
**Fix:** Shopify Admin → Online Store → Themes → Edit Code → `robots.txt.liquid` — add blank line between the adsbot-google block ending and `User-agent: Nutch`.

#### 3. Homepage OG Image Undersized (280×280)
**Current:** `og:image:width = 280`, `og:image:height = 280`  
**Required minimum:** 1200×630 pixels for Facebook/LinkedIn/Twitter Cards, Google Discover  
**Impact:** When the homepage is shared on social media, or AI systems extract social preview data, the image renders poorly. Google Discover requires minimum 1200px wide for eligibility.  
**Fix:** In Shopify Admin, upload a 1200×630 social sharing banner for the homepage (or store logo against brand background). Update the homepage `og:image` in theme settings.

#### 4. Product Page HTML Size: ~1MB
**Current:** Product page HTML = 1,047,084 bytes (~1MB)  
**Homepage for comparison:** 524,475 bytes (~512KB)  
**Impact:** Large HTML inflates LCP (Largest Contentful Paint) parse time. Google uses LCP as a Core Web Vitals ranking signal. 1MB HTML is ~2–3× larger than typical Shopify stores.  
**Root cause:** The product page includes 10 product-specific FAQPage entries, the full Organization schema, and likely large inline CSS/JS. The 10-question FAQ schema adds ~3–5KB but the total size suggests additional contributors (embedded JS, large theme CSS, multiple schema blocks).  
**Fix:** 
- Audit inline `<script>` and `<style>` blocks in the product template
- Consider lazy-loading non-visible product variant images
- Move third-party scripts to defer/async loading

---

### 🟡 Medium Priority

#### 5. Missing `Referrer-Policy` Header
**Impact:** Controls what referrer data browsers send when navigating away from the site. Without it, the default "no-referrer-when-downgrade" applies — potentially leaking URL paths to third-party sites.  
**Fix:** Add via Cloudflare or Shopify theme `<head>`:
```html
<meta name="referrer" content="strict-origin-when-cross-origin">
```

#### 6. Missing `Permissions-Policy` Header
**Impact:** Modern security best practice to declare which browser features the site uses. Absence doesn't cause harm but receives a flag in Lighthouse security audits.  
**Fix:** Add via Cloudflare Transform Rules:
```
Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(self)
```

#### 7. Blog Sitemap — 11 Articles with Stale `lastmod` (2021–2023)
**Analysis of blog sitemap lastmod dates:**

| lastmod | Count | Status |
|---------|-------|--------|
| 2026-05-xx | 6 articles | ✅ Fresh |
| 2025-xx-xx | 5 articles | ✅ Acceptable |
| 2024-xx-xx | 3 articles | ⚠️ Getting stale |
| 2023-xx-xx | 5 articles | ❌ Stale |
| 2021-xx-xx | 2 articles | ❌ Very stale |

Oldest articles (2021 lastmod): "From Garment Racks to Wicker Trunks" (2021-01-28), "What Makes Michael Wicker Trunk Storage Special" (2021-05-18).  
**Impact:** Freshness signals affect how often Googlebot revisits. Stale lastmod on quality articles may reduce crawl priority and freshness weighting in AI citation decisions.  
**Fix:** Even minor content updates (add a sentence, update a date reference) refresh the `lastmod` automatically in Shopify. Prioritize refreshing the 5 articles with 2023 lastmod dates.

#### 8. `policies/shipping-policy` Still Blocked in robots.txt
**Current state:** Explicit Allow added for privacy-policy, refund-policy, terms-of-service — but `shipping-policy` is not explicitly allowed and falls under the broad `Disallow: /policies/` rule.  
**Impact:** AI crawlers reading the shipping policy for delivery information (shipping duration, coverage area) may be blocked. This is GEO-relevant content — shipping times appear in product Q&A on Perplexity and Google AIO.  
**Fix:** Add to robots.txt:
```
Allow: /policies/shipping-policy
```

---

### 🟢 Low Priority

#### 9. HSTS `preload` Directive Not Set
After extending max-age to 1 year (Fix #1), add `preload` and submit to the HSTS Preload List (hstspreload.org). This hard-codes HTTPS-only into browsers permanently for happimess.com.

#### 10. `sitemap_agentic_discovery.xml` Missing `lastmod`
**Current:**
```xml
<loc>https://happimess.com/sitemap_agentic_discovery.xml</loc>
```
**Missing:** `<lastmod>` entry — signals when agents.md was last updated.  
**Fix:** Add `<lastmod>2026-04-08</lastmod>` (or the actual last update date) to this sitemap entry.

#### 11. OG `article:published_time` Missing on Blog Posts
Standard for article-type pages: adds `article:author`, `article:published_time`, `article:modified_time` OG properties. These are separate from the BlogPosting JSON-LD.

---

## Performance Summary

| Metric | Value | Assessment |
|--------|-------|-----------|
| DNS lookup | 18ms | ✅ Excellent |
| TCP connect | 99ms | ✅ Good |
| TLS handshake | 170ms | ✅ Good |
| TTFB (homepage) | 370ms | ✅ Good (< 800ms threshold) |
| TTFB (product) | 378ms | ✅ Good |
| TTFB (blog) | 356ms | ✅ Good |
| Total load (homepage) | 687ms | ✅ Good |
| Total load (product) | 1.1s | ⚠️ Monitor LCP |
| Total load (blog) | 586ms | ✅ Good |
| Homepage HTML size | 524KB | ⚠️ Large |
| Product HTML size | 1,047KB | ❌ Very large |
| Blog HTML size | ~400KB | ✅ Acceptable |
| CDN edge (tested from BOM) | gcp-asia-southeast1 | ✅ |
| Shopify processing time | 64ms | ✅ Excellent (server-side) |

---

## Security Headers Audit

| Header | Present | Value | Assessment |
|--------|---------|-------|-----------|
| HTTPS | ✅ | — | ✅ |
| HSTS | ✅ | max-age=7,889,238 | ⚠️ Too short (~91 days) |
| X-Frame-Options | ✅ | DENY | ✅ |
| X-Content-Type-Options | ✅ | nosniff | ✅ |
| X-XSS-Protection | ✅ | 1; mode=block | ✅ |
| Content-Security-Policy | ✅ | upgrade-insecure-requests | ✅ (partial) |
| Referrer-Policy | ❌ | — | ⚠️ Missing |
| Permissions-Policy | ❌ | — | ⚠️ Missing |
| X-Permitted-Cross-Domain-Policies | ✅ | none | ✅ |
| X-Download-Options | ✅ | noopen | ✅ |

---

## Crawlability Assessment

| Page Type | robots.txt | Sitemap | Indexable |
|-----------|-----------|---------|-----------|
| Homepage | ✅ Allow | ✅ | ✅ |
| Product pages | ✅ Allow | ✅ | ✅ |
| Blog posts | ✅ Allow | ✅ 27 in sitemap | ✅ |
| Collection pages | ✅ Allow (clean URLs) | ✅ | ✅ |
| /pages/about-us | ✅ Allow | ✅ | ✅ |
| /pages/faqs | ✅ Allow | ✅ | ✅ |
| /policies/privacy-policy | ✅ Explicit Allow | ✅ | ✅ |
| /policies/refund-policy | ✅ Explicit Allow | ✅ | ✅ |
| /policies/terms-of-service | ✅ Explicit Allow | ✅ | ✅ |
| /policies/shipping-policy | ❌ Blocked by /policies/ | ✅ | ❌ |
| /cart, /checkout, /admin | ✅ Blocked | — | ❌ (correct) |
| /collections/?sort_by= | ✅ Blocked (facets) | — | ❌ (correct) |
| /search | ✅ Blocked | — | ❌ (correct) |

---

## Sitemap Analysis

| Sitemap | Status | Coverage |
|---------|--------|---------|
| sitemap.xml (index) | ✅ | 9 sub-sitemaps |
| sitemap_agentic_discovery.xml | ✅ | agents.md entry |
| sitemap_products_1.xml | ✅ | All products (HPM10xx range) |
| sitemap_pages_1.xml | ✅ | All custom pages |
| sitemap_collections_1.xml | ✅ | All collections |
| sitemap_blogs_1.xml | ✅ | 27 articles + image data |
| /es/ Spanish sitemaps (×4) | ✅ | Full ES mirror |

**Blog sitemap freshness — most recent 6 articles by lastmod:**
1. `2026-05-22` — Best Dual Trash Can 2026 Guide
2. `2026-05-21` — Why Choosing the Right Trash Bag Actually Matters
3. `2026-05-15` — Standard Kitchen Trash Can Size
4. `2026-05-14` — Guide to Choosing the Perfect Kitchen Trash Can
5. `2026-05-11` — Living Room Storage Bench
6. `2026-05-11` — Average Kitchen Trash Can Size / Economy Home Decor

---

## Hreflang Implementation

Confirmed present on **all page types** (homepage, product, blog):

```html
<link rel="alternate" hreflang="x-default" href="https://happimess.com/[path]">
<link rel="alternate" hreflang="en"         href="https://happimess.com/[path]">
<link rel="alternate" hreflang="es"         href="https://happimess.com/es/[path]">
```

**Status:** ✅ Fully implemented — this was Issue #5 from the prior audit baseline (May 14). Now resolved.  
**Remaining gap:** No `hreflang="en-US"` or `hreflang="es-419"` locale-specific tags — the current `en` and `es` codes are correct per spec; locale codes are optional.

---

## Quick Fix Checklist

| # | Fix | Where | Effort |
|---|-----|-------|--------|
| 1 | Extend HSTS max-age to 31536000 (1 year) | Cloudflare SSL settings | 5 min |
| 2 | Fix robots.txt blank line defect (adsbot-google → Nutch) | Shopify robots.txt.liquid | 5 min |
| 3 | Upload 1200×630 homepage OG image | Shopify Theme Settings → Social image | 10 min |
| 4 | Add `Allow: /policies/shipping-policy` to robots.txt | Shopify robots.txt.liquid | 2 min |
| 5 | Add Referrer-Policy meta tag to theme `<head>` | theme.liquid | 5 min |
| 6 | Refresh stale 2021–2023 blog articles (minor edits) | Shopify Blog posts | 30 min |
| 7 | Add `<lastmod>` to agentic_discovery sitemap entry | sitemap_agentic_discovery.xml | 5 min |

**Total time for all 7 fixes: ~1 hour → Score projection: 82 → ~89/100**

---

## Confirmed Resolved (vs Prior Audits)

| Issue | Prior Status | Current Status |
|-------|-------------|----------------|
| hreflang EN/ES tags | ❌ Missing (May 14) | ✅ Implemented on all pages |
| AI crawlers explicit allow | ❌ Missing (May 18) | ✅ 15 crawlers in robots.txt |
| Content-Signal declaration | ❌ Missing (May 18) | ✅ Present in robots.txt |
| Organization sameAs | ❌ Missing (May 14) | ✅ 7 platforms |
| Policy pages access | ❌ All blocked | ✅ 3 key policies explicitly allowed |
| HTTPS/TLS | ✅ | ✅ Unchanged |

---

*Report generated by /geo technical — GEO Skill v2026*
