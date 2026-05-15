# Validation Checklist — Happimess GEO Implementation
**Run after each sprint to verify all fixes are live and working**

---

## Tools Reference

| Tool | Purpose | URL |
|------|---------|-----|
| Google Rich Results Test | Schema validation, rich result eligibility | https://search.google.com/test/rich-results |
| Schema.org Validator | Full JSON-LD validation | https://validator.schema.org/ |
| Google Search Console | Crawl errors, hreflang, indexing | https://search.google.com/search-console/ |
| PageSpeed Insights | Core Web Vitals (CLS, LCP, INP) | https://pagespeed.web.dev/?url=https://happimess.com/ |
| Bing Webmaster Tools | Bing crawl, indexing, sitemaps | https://www.bing.com/webmasters/ |
| Hreflang Checker | Bilingual hreflang validation | https://www.aleydasolis.com/english/international-seo-tools/ |
| Security Headers | HTTP security header check | https://securityheaders.com/?q=https://happimess.com/ |
| Lighthouse (Chrome) | Full site audit (DevTools → Lighthouse) | Browser built-in |

---

## Sprint 1 Validation (After Day 5 — Full 5-Day Sprint Check)

### Section 1: Broken Pages Fixed

Run these URL checks. All must return HTTP 200:

```
[ ] https://happimess.com/pages/asodariya-sumi → HTTP 200
[ ] https://happimess.com/pages/faq → HTTP 200 (or redirect to live page)
[ ] https://happimess.com/llms.txt → HTTP 200 with ## Blog & Guides section
[ ] https://happimess.com/robots.txt → HTTP 200 with GPTBot entries at top
```

**How to check HTTP status (no tools):**
- Open each URL in a private browser window
- If the page loads with content = 200
- If you see "Page not found" or blank = still 404

**How to check HTTP status (terminal):**
```bash
curl -o /dev/null -s -w "%{http_code}" https://happimess.com/pages/asodariya-sumi
# Expected: 200

curl -o /dev/null -s -w "%{http_code}" https://happimess.com/pages/faq
# Expected: 200

curl -o /dev/null -s -w "%{http_code}" https://happimess.com/llms.txt
# Expected: 200
```

---

### Section 2: Organization Schema Validation

**Test 1 — Google Rich Results Test:**
1. Go to https://search.google.com/test/rich-results
2. Enter: `https://happimess.com`
3. Click **Test URL**

Expected results:
```
[ ] Organization schema detected
[ ] Zero red errors on Organization block
[ ] telephone: "+19172614961" (no leading space)
[ ] contactType: "customer service" (lowercase)
[ ] NO "servesCuisine" property
[ ] @type: "Organization" (not "LocalBusiness")
```

**Test 2 — Server-rendering check:**
1. View page source: open Chrome → `Ctrl+U`
2. Use Ctrl+F to search for `application/ld+json`
3. The Organization JSON-LD block must appear in the raw HTML source

```
[ ] "Organization" appears in page source HTML
[ ] Schema is NOT inside a <script type="text/javascript"> block
[ ] Schema IS inside a <script type="application/ld+json"> block in <head>
```

**Test 3 — Schema.org Validator:**
1. Copy the Organization JSON-LD from page source
2. Go to https://validator.schema.org/
3. Paste the JSON → Run validation

```
[ ] Zero critical errors
[ ] Zero warnings on @type, telephone, contactType
```

---

### Section 3: robots.txt AI Crawler Check

1. Visit `https://happimess.com/robots.txt`

```
[ ] "User-agent: GPTBot" line present
[ ] "Allow: /" immediately below GPTBot entry
[ ] "User-agent: ClaudeBot" line present
[ ] "User-agent: PerplexityBot" line present
[ ] "User-agent: OAI-SearchBot" line present
[ ] "User-agent: Google-Extended" line present
[ ] NO "Disallow: /products/*-[a-f0-9]{8}-remote" line
[ ] "Allow: /policies/privacy-policy" present
[ ] "Allow: /policies/refund-policy" present
```

---

### Section 4: llms.txt Content Check

1. Visit `https://happimess.com/llms.txt`
2. Use Ctrl+F to search for:

```
[ ] "## Blog & Guides" heading present
[ ] "Standard Kitchen Trash Can Size" blog link present
[ ] "Best Dual Trash Can" blog link present
[ ] "## Product Categories" heading present
[ ] "## Key Pages" heading present
[ ] At least 8 blog post links visible in the Blog & Guides section
```

---

### Section 5: Product Schema Validation

1. Go to Google Rich Results Test
2. Enter a product URL (e.g., `https://happimess.com/products/abrahamus-8-gallon-step-open-trash-can`)

```
[ ] Product schema detected
[ ] "@context": "https://schema.org" (NO trailing slash)
[ ] "url" field is absolute (starts with "https://happimess.com/")
[ ] "offers" array present with price and availability
[ ] "availability": "https://schema.org/InStock" (absolute URL, not "InStock")
[ ] "shippingDetails" present
[ ] "hasMerchantReturnPolicy" present
[ ] If reviews app is installed: "aggregateRating" with numeric ratingValue and reviewCount
[ ] Zero red validation errors
```

---

### Section 6: Collection Schema Validation

1. Go to Google Rich Results Test
2. Enter: `https://happimess.com/collections/trash-can`

```
[ ] CollectionPage schema detected
[ ] ItemList present with at least 5 products
[ ] Each product in ItemList has: name, url, price
[ ] BreadcrumbList present (Home → Collection title)
[ ] Zero errors
```

---

### Section 7: Article Schema Validation

1. Go to Google Rich Results Test
2. Enter: `https://happimess.com/blogs/news/standard-kitchen-trash-can-size`

```
[ ] BlogPosting / Article schema detected
[ ] "author.name": "Asodariya Sumi" (named individual, not "From The Mess Experts")
[ ] "author.url": "https://happimess.com/pages/asodariya-sumi" → resolves HTTP 200
[ ] "datePublished": populated with real date (not empty)
[ ] "dateModified": populated
[ ] "headline": present
[ ] "description": unique content (different from headline)
[ ] "speakable" property present
[ ] "publisher.name": "Happimess"
[ ] BreadcrumbList present (Home → News/Blog → Article title)
[ ] Zero red errors
```

---

### Section 8: FAQPage Schema Check

1. Go to Google Rich Results Test
2. Enter the standard-kitchen-trash-can-size post URL

```
[ ] FAQPage schema detected
[ ] At least 3 questions present
[ ] Each question has "name" and "acceptedAnswer.text"
[ ] Question text matches actual questions in the article
[ ] Answer text matches actual answers in the article
```

---

### Section 9: Content Quality Checks

**Buying Guide** (`/blogs/news/the-guide-to-choosing-the-perfect-kitchen-trash-can`):
```
[ ] Word count > 2,000 words (check in Google Docs or browser extension)
[ ] No H3 headings: "Kitchen Hero", "Mini Wipes", "Heavy Duty Wipes", "Plant Wipes"
[ ] H2: "Trash Cans with Lids..." (title case, no lowercase)
[ ] At least one external citation link present
[ ] Methodology / testing section present
[ ] Comparison table(s) present
[ ] First paragraph contains direct answer with specific measurements (gallons, inches)
[ ] FTC disclosure visible at top of post
```

**Dual Trash Can Guide** (`/blogs/news/best-dual-trash-can-for-kitchen-2026-guide-what-actually-works`):
```
[ ] H2 headings contain NO emoji characters
[ ] All 10 H2s are clean text (no 🗑️, ⚠️, 🔍, etc.)
[ ] First paragraph is answer-first (mentions 50-60L or specific sizes in first sentence)
[ ] FTC disclosure visible at top
```

---

### Section 10: Author Attribution Check

Visit any blog post:
```
[ ] Author name displayed as "Asodariya Sumi" (not "From The Mess Experts")
[ ] Author name is a link to /pages/asodariya-sumi
[ ] /pages/asodariya-sumi is live (HTTP 200) with bio content
[ ] Article schema shows author.name as "Asodariya Sumi"
```

---

### Section 11: Homepage H1 Check

1. Visit `https://happimess.com`
2. View page source (Ctrl+U)
3. Search for `<h1`

```
[ ] H1 tag content includes keyword text (NOT just "Happimess")
[ ] H1 contains at least one of: "Trash Can", "Storage", "Home Organization"
[ ] Only ONE H1 tag on the page
```

---

### Section 12: Core Web Vitals Check

1. Go to https://pagespeed.web.dev/?url=https://happimess.com/
2. Test both mobile and desktop

```
Desktop:
[ ] CLS < 0.1 (Good) — was "Medium-High risk" in audit
[ ] LCP < 2.5s (Good)
[ ] INP < 200ms (Good)

Mobile:
[ ] CLS < 0.1 (Good)
[ ] No major layout shifts on product images
```

---

### Section 13: Hreflang Check

1. Visit an English blog post page source:
```
[ ] <link rel="alternate" hreflang="en" href="https://happimess.com/..."> present
[ ] <link rel="alternate" hreflang="es" href="https://happimess.com/es/..."> present
[ ] <link rel="alternate" hreflang="x-default" href="https://happimess.com/..."> present
```

2. Google Search Console → International Targeting:
```
[ ] Zero hreflang errors
[ ] Zero "Missing return tag" warnings
```

---

### Section 14: LinkedIn Entity Check

1. Search "Happimess" on LinkedIn:
```
[ ] Happimess US e-commerce company page appears (NOT Lithuanian nonprofit)
[ ] LinkedIn company page shows website: happimess.com
[ ] Company page has logo and description
```

---

### Section 15: Bing Webmaster Tools Check

1. Log into Bing Webmaster Tools:
```
[ ] Site verified (green checkmark)
[ ] sitemap.xml submitted and showing URL count
[ ] No crawl errors for /pages/asodariya-sumi or /pages/faq
[ ] IndexNow: URLs submitted successfully
```

---

## Full GEO Re-Audit (Run After Sprint 1 Complete)

After completing all Day 1–5 fixes, run a full GEO re-audit to measure actual score improvements:

```bash
# In Claude Code terminal:
/geo audit https://happimess.com/
```

**Expected score improvements after Sprint 1:**

| Category | Before | Expected After |
|----------|--------|---------------|
| AI Citability & Visibility | 45/100 | 60–65/100 |
| Brand Authority Signals | 18/100 | 25–30/100 |
| Content Quality & E-E-A-T | 38/100 | 55–65/100 |
| Technical Foundations | 68/100 | 73–78/100 |
| Structured Data | 52/100 | 72–80/100 |
| Platform Optimization | 41/100 | 58–65/100 |
| **Composite GEO Score** | **42/100** | **65–70/100** |

If the re-audit scores are significantly lower than expected, use this checklist to identify which fixes did not take effect:

- Below 60 on Structured Data → Schema snippets not included in templates, or still JS-injected
- Below 55 on Content Quality → Buying guide rebuild incomplete, or author attribution not done
- Below 55 on AI Citability → llms.txt not deployed correctly, or robots.txt missing AI crawler entries
- Below 65 on Technical → Hreflang issue present, or schema still JS-injected

---

## Regression Checks (Ongoing — Run Monthly)

These checks ensure previously fixed issues haven't reverted due to theme updates:

```
Monthly checks:
[ ] https://happimess.com/pages/asodariya-sumi → HTTP 200
[ ] https://happimess.com/pages/faq → HTTP 200
[ ] https://happimess.com/llms.txt → Blog section present
[ ] Google Rich Results Test → homepage → Organization → zero errors
[ ] Schema server-rendered (page source check)
[ ] robots.txt → AI crawler entries present
[ ] No "LocalBusiness" in theme.liquid
[ ] Hreflang errors in Search Console → zero
```

**Why monthly?** Shopify theme updates, app installations, and team edits can revert changes. After any significant Shopify theme update, run the regression checklist before the next sprint.

---

*Validation Checklist — Happimess GEO Implementation | May 2026*
*Reference audit: GEO-AUDIT-REPORT.md (May 7, 2026 baseline)*
