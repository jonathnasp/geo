# GEO Audit Package — happimess.com
**Audit Date:** May 7, 2026 | **Auditor:** Claude Code GEO Skill

---

## Overall GEO Score: 42 / 100

```
██████████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  42/100
                                          ↑ Current          Target 68 ↑
```

| Category | Score | Grade |
|----------|-------|-------|
| AI Citability & Visibility | 45/100 | D |
| Brand Authority Signals | 18/100 | F ← biggest gap |
| Content Quality & E-E-A-T | 38/100 | D |
| Technical Foundations | 68/100 | C+ ← strongest area |
| Structured Data | 52/100 | C |
| Platform Optimization | 41/100 | D |

**AI Platform Readiness:**
| Platform | Score |
|----------|-------|
| Google AI Overviews | 48/100 |
| Bing Copilot | 45/100 |
| Perplexity AI | 44/100 |
| Google Gemini | 36/100 |
| ChatGPT Web Search | 32/100 |

---

## START HERE

**→ [FIXES.md](FIXES.md) — Complete Step-by-Step Fix Guide (25 issues, all actionable)**

This is the single document to work from. Every issue has exact steps, copy-paste code, time estimates, and verification instructions. Work through Phase 1 first — it takes ~3–4 hours and moves the score from 42 to ~50.

---

## Reports Index

### Audit Reports

| File | What It Contains | Score |
|------|-----------------|-------|
| [GEO-AUDIT-REPORT.md](GEO-AUDIT-REPORT.md) | Full composite audit — all scores, all findings, 25-item action plan | 42/100 |
| [GEO-CLIENT-REPORT.md](GEO-CLIENT-REPORT.md) | Executive summary — written for non-technical stakeholders | — |
| [GEO-CITABILITY-SCORE.md](GEO-CITABILITY-SCORE.md) | Passage-level AI citation readiness for homepage | 32/100 |
| [GEO-CRAWLER-ACCESS.md](GEO-CRAWLER-ACCESS.md) | AI crawler access map + robots.txt copy-paste fix | 70/100 |
| [GEO-PLATFORM-OPTIMIZATION.md](GEO-PLATFORM-OPTIMIZATION.md) | Per-platform analysis: AIO, ChatGPT, Perplexity, Gemini, Bing | 41/100 avg |
| [GEO-SCHEMA-REPORT.md](GEO-SCHEMA-REPORT.md) | Schema validation errors + missing schemas + deployment guide | 52/100 |
| [GEO-TECHNICAL-AUDIT.md](GEO-TECHNICAL-AUDIT.md) | SSR, CLS, hreflang, crawlability, security headers | 68/100 |
| [GEO-CONTENT-ANALYSIS.md](GEO-CONTENT-ANALYSIS.md) | E-E-A-T assessment, per-page scoring, AI content signals | 38/100 |

### PDF Report
| File | Description |
|------|-------------|
| [GEO-REPORT.pdf](GEO-REPORT.pdf) | Professional PDF with score gauges, charts, and formatted tables — ready to share |

---

## Deploy-Ready Assets

These files are ready to use without modification (except where `[REPLACE: ...]` is indicated):

### llms.txt
| File | Action |
|------|--------|
| [llms.txt](llms.txt) | Upload this to `https://happimess.com/llms.txt` — replaces the current file that omits all 26 blog posts |

### Schema JSON-LD (Shopify Deployment)

| File | Deploy To | What It Fixes |
|------|-----------|--------------|
| [schema/schema-organization.json](schema/schema-organization.json) | `layout/theme.liquid` `<head>` | Replaces LocalBusiness with Organization; fixes 4 validation errors |
| [schema/schema-website.json](schema/schema-website.json) | `layout/theme.liquid` `<head>` | Fixed WebSite + SearchAction (server-rendered) |
| [schema/schema-product.liquid](schema/schema-product.liquid) | `snippets/schema-product.liquid` → `product.liquid` | Product + AggregateRating; absolute URLs; site-wide via one template |
| [schema/schema-article.liquid](schema/schema-article.liquid) | `snippets/schema-article.liquid` → `article.liquid` | Article + speakable; fixed author URL |
| [schema/schema-collection.liquid](schema/schema-collection.liquid) | `snippets/schema-collection.liquid` → `collection.liquid` | CollectionPage + ItemList (currently zero schema on collections) |
| [schema/schema-author-person.json](schema/schema-author-person.json) | `/pages/asodariya-sumi` page template | Person schema for the author bio page (fix the 404) |

### Audit Data
| File | Use |
|------|-----|
| [geo-report-data.json](geo-report-data.json) | Source data for the PDF report; reuse with `/geo compare` for monthly tracking |

---

## Critical Issues Summary (Fix These First)

| # | Issue | Impact | Fix | Time |
|---|-------|--------|-----|------|
| 1 | Author page `/pages/asodariya-sumi` → 404 | Voids E-E-A-T on all 26 blog posts | [FIX-01](FIXES.md#fix-01-create-the-author-bio-page-404--live) | 30 min |
| 2 | FAQ page `/pages/faq` → 404 | Broken link in every page footer | [FIX-02](FIXES.md#fix-02-fix-the-faq-page-404--live) | 15 min |
| 3 | Organization schema wrong type + 4 errors | Blocks Knowledge Panel; pollutes entity data | [FIX-03](FIXES.md#fix-03-fix-the-organization-schema-4-validation-errors) | 30 min |
| 4 | llms.txt lists 0 of 26 blog posts | AI systems classify site as storefront only | [FIX-04](FIXES.md#fix-04-upload-the-improved-llmstxt) | 10 min |
| 5 | No AI crawler Allow rules in robots.txt | Missing explicit AI cooperation signal | [FIX-05](FIXES.md#fix-05-add-ai-crawler-allow-rules-to-robotstxt) | 15 min |
| 6 | No LinkedIn company page | No entity anchor for ChatGPT or Bing Copilot | [FIX-06](FIXES.md#fix-06-create-linkedin-company-page) | 60 min |
| 7 | No IndexNow / Bing Webmaster Tools | Bing index always stale | [FIX-07](FIXES.md#fix-07-implement-indexnow--bing-webmaster-tools) | 45 min |

**These 7 fixes take ~3–4 hours and move the score from 42 → ~50.**

---

## All 25 Issues — Quick Reference

| Fix | Issue | Phase | Time | Report |
|-----|-------|-------|------|--------|
| [FIX-01](FIXES.md#fix-01-create-the-author-bio-page-404--live) | Author page 404 | 1 | 30 min | [Content](GEO-CONTENT-ANALYSIS.md) |
| [FIX-02](FIXES.md#fix-02-fix-the-faq-page-404--live) | FAQ page 404 | 1 | 15 min | [Content](GEO-CONTENT-ANALYSIS.md) |
| [FIX-03](FIXES.md#fix-03-fix-the-organization-schema-4-validation-errors) | Organization schema errors | 1 | 30 min | [Schema](GEO-SCHEMA-REPORT.md) |
| [FIX-04](FIXES.md#fix-04-upload-the-improved-llmstxt) | llms.txt missing blog posts | 1 | 10 min | [Crawlers](GEO-CRAWLER-ACCESS.md) |
| [FIX-05](FIXES.md#fix-05-add-ai-crawler-allow-rules-to-robotstxt) | No AI crawler Allow rules | 1 | 15 min | [Crawlers](GEO-CRAWLER-ACCESS.md) |
| [FIX-06](FIXES.md#fix-06-create-linkedin-company-page) | No LinkedIn company page | 1 | 60 min | [Platforms](GEO-PLATFORM-OPTIMIZATION.md) |
| [FIX-07](FIXES.md#fix-07-implement-indexnow--bing-webmaster-tools) | No IndexNow / Bing tools | 1 | 45 min | [Platforms](GEO-PLATFORM-OPTIMIZATION.md) |
| [FIX-08](FIXES.md#fix-08-add-faqpage-schema-to-blog-posts) | No FAQPage schema on 8+ posts | 2 | 2–3 hr | [Schema](GEO-SCHEMA-REPORT.md) |
| [FIX-09](FIXES.md#fix-09-deploy-product-schema-to-all-product-pages) | No AggregateRating on products | 2 | 1 hr | [Schema](GEO-SCHEMA-REPORT.md) |
| [FIX-10](FIXES.md#fix-10-deploy-collectionpage-schema-currently-zero-schema) | No schema on collection pages | 2 | 30 min | [Schema](GEO-SCHEMA-REPORT.md) |
| [FIX-11](FIXES.md#fix-11-deploy-article-schema-with-speakable-to-blog-posts) | Article schema has 404 author URL | 2 | 1 hr | [Schema](GEO-SCHEMA-REPORT.md) |
| [FIX-12](FIXES.md#fix-12-move-global-schema-from-javascript-to-server-rendered) | Schema JS-injected (AI crawlers miss it) | 2 | 30 min | [Technical](GEO-TECHNICAL-AUDIT.md) |
| [FIX-13](FIXES.md#fix-13-fix-image-cls-layout-shift) | Image CLS — no dimensions on img tags | 2 | 1–2 hr | [Technical](GEO-TECHNICAL-AUDIT.md) |
| [FIX-14](FIXES.md#fix-14-change-homepage-h1-to-keyword-bearing-text) | Homepage H1 is brand name only | 2 | 15 min | [Platforms](GEO-PLATFORM-OPTIMIZATION.md) |
| [FIX-15](FIXES.md#fix-15-rebuild-the-buying-guide-650--2000-words) | Buying guide only 650 words | 3 | 3–4 hr | [Content](GEO-CONTENT-ANALYSIS.md) |
| [FIX-16](FIXES.md#fix-16-remove-emojis-from-all-h2-headings) | Emojis in all 10 H2 headings | 3 | 20 min | [Content](GEO-CONTENT-ANALYSIS.md) |
| [FIX-17](FIXES.md#fix-17-add-ftc-disclosure-to-commercial-blog-posts) | No FTC disclosure on commercial posts | 3 | 30 min | [Content](GEO-CONTENT-ANALYSIS.md) |
| [FIX-18](FIXES.md#fix-18-rewrite-blog-post-openings-answer-first-structure) | Blog posts bury the direct answer | 3 | 2–3 hr | [Platforms](GEO-PLATFORM-OPTIMIZATION.md) |
| [FIX-19](FIXES.md#fix-19-add-named-author-attribution-site-wide) | Anonymous "From The Mess Experts" byline | 3 | 1 hr | [Content](GEO-CONTENT-ANALYSIS.md) |
| [FIX-20](FIXES.md#fix-20-claim-trustpilot-business-profile) | No Trustpilot profile | 4 | 2 hr | [Audit](GEO-AUDIT-REPORT.md) |
| [FIX-21](FIXES.md#fix-21-add-source-citations-to-key-blog-posts) | Zero external citations in blog | 4 | 2–3 hr | [Platforms](GEO-PLATFORM-OPTIMIZATION.md) |
| [FIX-22](FIXES.md#fix-22-create-youtube-channel) | No YouTube presence | 4 | Ongoing | [Platforms](GEO-PLATFORM-OPTIMIZATION.md) |
| [FIX-23](FIXES.md#fix-23-publish-original-research-article) | No original data/research | 4 | 2–3 wks | [Content](GEO-CONTENT-ANALYSIS.md) |
| [FIX-24](FIXES.md#fix-24-verify-hreflang-implementation) | Hreflang implementation unconfirmed | 4 | 30 min | [Technical](GEO-TECHNICAL-AUDIT.md) |
| [FIX-25](FIXES.md#fix-25-build-toward-wikipedia-notability) | No Wikipedia / Wikidata entity | 4 | 3–6 mo | [Audit](GEO-AUDIT-REPORT.md) |

---

## Key Findings at a Glance

### What's Working (Don't Break)
- ✅ Shopify server-side rendering — all content accessible to AI crawlers without JS
- ✅ llms.txt + agents.md + UCP/MCP infrastructure — top 5% of Shopify stores for agentic readiness
- ✅ sitemap_agentic_discovery.xml — automatically surfaces AI files to search engines
- ✅ Bilingual site (EN + ES) — multilingual indexing advantage for Gemini
- ✅ 26 blog posts with real topical coverage
- ✅ Product + Article schema present (needs fixes, not a rebuild)
- ✅ WebSite + SearchAction schema — Sitelinks Search Box eligible

### What's Broken (Fix Immediately)
- ❌ `/pages/asodariya-sumi` → 404 (author page for all blog posts)
- ❌ `/pages/faq` → 404 (linked in every page footer)
- ❌ Organization schema: 4 validation errors on every page
- ❌ 0 of 26 blog posts listed in llms.txt
- ❌ No named authors — "From The Mess Experts" has zero credential value
- ❌ No explicit AI crawler Allow rules in robots.txt
- ❌ No LinkedIn company page — LinkedIn "Happimess" returns a Lithuanian nonprofit

### What's Missing (Add in Priority Order)
- ⬜ AggregateRating on Product schema → star ratings in SERPs
- ⬜ FAQPage schema on 8+ posts that already have FAQ content written
- ⬜ CollectionPage + ItemList schema on collection pages
- ⬜ speakable property on Article schema
- ⬜ External citations in blog posts (zero across 26 posts)
- ⬜ IndexNow implementation for Bing Copilot freshness
- ⬜ Trustpilot profile (brand authority)
- ⬜ Wikipedia/Wikidata entity (long-term)

---

## Score Roadmap

| Phase | Fixes | Time | Score |
|-------|-------|------|-------|
| Baseline | — | — | **42/100** |
| Phase 1 | FIX-01 to FIX-07 | Day 1 (~4 hr) | **~50/100** |
| Phase 2 | FIX-08 to FIX-14 | Week 1 (~7 hr) | **~56/100** |
| Phase 3 | FIX-15 to FIX-19 | Week 2 (~8 hr) | **~62/100** |
| Phase 4 | FIX-20 to FIX-25 | Month 1–3 | **~68/100** |

---

## Quick Reference: External Tools

| Tool | Purpose |
|------|---------|
| [Google Rich Results Test](https://search.google.com/test/rich-results) | Validate schema after every deployment |
| [Google Search Console](https://search.google.com/search-console/) | Hreflang errors, crawl coverage, AIO performance |
| [PageSpeed Insights](https://pagespeed.web.dev/?url=https://happimess.com/) | Core Web Vitals (CLS, LCP, INP) |
| [Bing Webmaster Tools](https://www.bing.com/webmasters/) | Bing index coverage, IndexNow setup |
| [Security Headers](https://securityheaders.com/?q=https://happimess.com/) | Verify HTTPS security headers |
| [Hreflang Testing Tool](https://www.aleydasolis.com/english/international-seo-tools/hreflang-tags-generator-tool/) | Validate EN/ES hreflang implementation |
| [Trustpilot Business](https://business.trustpilot.com) | Claim/create brand review profile |
| [Wikidata New Item](https://www.wikidata.org/wiki/Special:NewItem) | Create entity entry when notability is established |

---

*GEO Audit Package for https://happimess.com/*
*Audited May 7, 2026 | Generated by Claude Code GEO Skill*
*25 issues identified | Estimated 90-day score improvement: 42 → 68*
