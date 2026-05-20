# GEO Audit Report
## Happimess — happimess.com
**Prepared by:** Sandip / IS GEO  
**Date:** May 18, 2026  
**Platform:** Shopify (E-commerce)  
**Category:** Home Organization, Storage & Trash Management

---

# Overall Score: 48 / 100 — Poor

> **What this means:** Happimess has strong technical bones and one best-in-class signal (AI crawler access), but is currently invisible to AI search engines where it matters most — brand authority, content credibility, and platform-specific optimization. The gap between 48 and 70 is closeable in 30–60 days with focused effort on the issues in this report.

---

## Score Breakdown

| Category | Score | Benchmark | Status |
|----------|-------|-----------|--------|
| AI Citability & Visibility | 52 / 100 | 70+ | ⚠️ Fair |
| Brand Authority Signals | 28 / 100 | 60+ | ❌ Critical |
| Content Quality & E-E-A-T | 44 / 100 | 65+ | ❌ Poor |
| Technical Foundations | 71 / 100 | 75+ | ⚠️ Fair |
| Structured Data | 62 / 100 | 75+ | ⚠️ Fair |
| Platform Optimization | 41 / 100 | 60+ | ❌ Poor |
| **COMPOSITE** | **48 / 100** | **70+** | **❌ Poor** |

**Score scale:** 0–25 Critical · 26–50 Poor · 51–75 Fair · 76–90 Good · 91–100 Excellent

---

## What's Working Well

### ✅ AI Crawler Access — 90 / 100 (Excellent)
This is Happimess's strongest signal and a direct competitive advantage.

- **10 major AI crawlers explicitly allowed** in robots.txt: GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, anthropic-ai, PerplexityBot, Google-Extended, Amazonbot, CCBot, and Applebot-Extended all have `Allow: /`
- **`Content-Signal: ai-train=yes, search=yes, ai-retrieval=yes`** declared — one of the few e-commerce sites actively signaling AI permission intent via the IETF draft standard
- **Custom `sitemap_agentic_discovery.xml`** sub-sitemap referencing llms.txt, llms-full.txt, and agents.md — a forward-thinking addition most competitors have not made
- **UCP/MCP commerce protocol** at `/agents.md` and `/api/ucp/mcp` — agentic purchasing infrastructure already in place

### ✅ Server-Side Rendering — 95 / 100 (Excellent)
All product names, descriptions, blog content, and FAQ answers are present in the raw HTML before any JavaScript runs. Every AI crawler that visits Happimess receives the complete content — no rendering gap. This is the single most important technical signal for AI discoverability, and Shopify delivers it by default.

### ✅ Site Structure — 80 / 100 (Good)
- Clean URL hierarchy: `/products/`, `/collections/`, `/pages/`, `/blogs/news/`
- Comprehensive sitemap: 9 sub-sitemaps, ~826 URLs, all with current `lastmod` dates
- HTTPS enforced sitewide
- Shopify CDN (Fastly) ensures fast global TTFB

### ✅ Structured Data Foundation — 62 / 100 (Fair, improving)
Since the April 2026 audit, four critical schema issues have been resolved:
- `brand.name` now correctly shows `"Happimess"` (was `"Happimess Dev"` — a staging artifact in production)
- `WebPage description` populated (was `null`)
- Author names updated (`"Jonathan Yaraghi"` replacing `"jonathany 2123"`)
- Organization `sameAs` now includes 6 social platform links

### ✅ Testing Methodology — Differentiated Content Asset
Happimess's product evaluation process is the brand's most unique and credible claim:
- **30-day minimum real-household use** before any product enters the catalog
- **500+ open/close cycles** for mechanism durability testing
- **15-day lid-seal odor containment** testing with actual food waste
- **Liner compatibility testing** with Glad, Hefty, and Simplehuman
- Products failing any criterion are excluded — resulting in a curated catalog

No major competitor in the home organization space publishes this level of testing detail. This is the highest-value E-E-A-T signal the brand possesses.

---

## What Needs Fixing

### ❌ Brand Authority — 28 / 100 (Critical)

This is the most impactful gap. AI models (ChatGPT, Gemini, Perplexity) resolve brand identity by cross-referencing multiple authoritative sources. Happimess currently has:

| Signal | Status | Impact |
|--------|--------|--------|
| Wikipedia | ❌ No article | AI models treat unknown brands cautiously |
| Wikidata | ❌ No entity | No structured entity anchor for AI disambiguation |
| Press coverage | ❌ None confirmed | Wikipedia notability, Perplexity citations |
| Trustpilot / BBB | ❌ Not listed | Third-party trust corroboration |
| Crunchbase | ❌ No profile | Business entity verification |
| LinkedIn | ⚠️ Name collision | **Critical:** `/company/happimess` = Lithuanian nonprofit; brand's correct URL is `/company/happimesshome/` — AI models searching LinkedIn for "Happimess" surface the wrong entity |

**The LinkedIn collision is an active problem.** Any AI system using LinkedIn to verify "Happimess" finds a children's cancer charity in Vilnius, Lithuania (est. 2016) under the primary slug — not the NYC home organization brand. This actively harms entity disambiguation across ChatGPT and Bing Copilot.

**90-day brand authority path:**

| Milestone | Projected Score |
|-----------|----------------|
| Current | 28/100 |
| Wikidata + Crunchbase + BBB + Trustpilot registration | ~38/100 |
| 50+ Trustpilot reviews + active LinkedIn | ~48/100 |
| 1–2 press placements (The Spruce / Apartment Therapy) | ~62/100 |
| Wikipedia article (requires press coverage first) | ~78/100 |

---

### ❌ Content E-E-A-T — 44 / 100 (Poor)

**The gap in one sentence:** Happimess has proprietary testing data that no competitor can replicate, and it appears on exactly one static About page — never in the buying guides where it would drive citation decisions.

| E-E-A-T Dimension | Score | Primary Issue |
|-------------------|-------|--------------|
| Experience | 55/100 | Testing data exists but not surfaced in articles |
| Expertise | 40/100 | No named authors on any article |
| Authoritativeness | 35/100 | Zero external citations, zero press mentions |
| Trustworthiness | 55/100 | Good policies/contact; no review platform |

**Anonymous authorship is the single highest-leverage fix.** Every article is attributed to "From The Mess Experts" or "Happimess editorial team." This is invisible to AI models evaluating author authority. Adding "Written by Jonathan Yaraghi, Founder" to the top 10 articles — a 2-hour change — immediately connects the Person schema already in the site's JSON-LD to the content it's supposed to describe.

**External citations:** Of 6 articles reviewed in depth, only 1 contains an external citation (NKBA Kitchen Planning Guidelines, in the kitchen trash can guide). The other 25 blog posts contain zero outbound links to sources. AI models rank content higher for citation when it references authoritative external data.

**Article quality distribution:**

| Quality Level | Articles | Example |
|--------------|---------|---------|
| ⭐⭐⭐⭐⭐ Excellent | 1 | Complete Kitchen Trash Can Guide (2,800 words, NKBA cited, 4 comparison tables) |
| ⭐⭐⭐⭐ Good | 2 | Best Dual Trash Can 2026, Why Trash Bags Matter |
| ⭐⭐⭐ Fair | ~12 | Storage bench, kitchen organization guides |
| ⭐⭐ Weak | ~8 | Older product-adjacent articles |
| ⭐ Critical | ~3 | Eco articles under 500 words, unsupported claims |

---

### ❌ Platform Optimization — 41 / 100 (Poor)

| Platform | Score | Top Fix |
|----------|-------|---------|
| Google AI Overviews | 48/100 | FAQPage schema on `/pages/faqs`, external citations |
| Perplexity AI | 44/100 | Show blog dates on listing, add external citations |
| ChatGPT Web Search | 38/100 | Wikidata entity creation, Crunchbase profile |
| Bing Copilot | 38/100 | Verify in Bing Webmaster Tools, submit sitemap |
| Google Gemini | 37/100 | `aggregateRating` on products, Google Business Profile |

**The `aggregateRating` absence is a critical Gemini and Google Shopping gap.** Product star ratings are the primary visual differentiator in AI-generated product comparison responses. Without Schema.org `aggregateRating` on Product pages, Happimess products cannot appear with star ratings in Gemini recommendations or AI Overviews even when products have reviews in the Shopify review app.

---

### ⚠️ Technical — 71 / 100 (Fair)

Technical foundations are acceptable but have two medium-priority issues:

**Hreflang completely absent (Critical):**
The site runs full EN and ES catalogs (~400 pages each) with no language annotations. Google receives ~800 pages and cannot determine which language to surface to which user. This creates duplicate content risk and means Spanish-speaking users may be served English results and vice versa.

Fix: Add to `theme.liquid` `<head>`:
```liquid
{% if request.locale.iso_code == 'en' %}
  <link rel="alternate" hreflang="en" href="{{ canonical_url }}" />
  <link rel="alternate" hreflang="es" href="https://happimess.com/es{{ request.path }}" />
  <link rel="alternate" hreflang="x-default" href="{{ canonical_url }}" />
{% else %}
  <link rel="alternate" hreflang="es" href="{{ canonical_url }}" />
  <link rel="alternate" hreflang="en" href="{{ 'https://happimess.com' | append: request.path | remove: '/es' }}" />
  <link rel="alternate" hreflang="x-default" href="{{ 'https://happimess.com' | append: request.path | remove: '/es' }}" />
{% endif %}
```

**CLS risk from missing image dimensions:**
All product, collection, and blog images lack `width` and `height` attributes. When images load from the CDN, they cause layout shift. Fix in `product-card.liquid` and `article.liquid`:
```liquid
<img 
  src="{{ image | image_url: width: 600 }}"
  width="{{ image.width }}"
  height="{{ image.height }}"
  loading="lazy"
  alt="{{ image.alt }}"
>
```

---

### ⚠️ llms.txt — Non-Compliant (High Priority)

**Status:** File exists at `https://happimess.com/llms.txt` but serves a commerce-agent store overview document, not a spec-compliant llms.txt.

The llms.txt standard requires: `# Title` → `> description blockquote` → `## Section` headers → `- [Title](URL): Description` link lists. The current file has none of this structure. AI models reading llms.txt for site orientation find a commerce API document.

**Ready-to-deploy compliant versions** of both `llms.txt` and `llms-full.txt` are in this audit folder. Upload via: Shopify Admin → Content → Files → upload both files → set up URL rewrites to serve at `/llms.txt` and `/llms-full.txt`.

---

## Complete Action Plan

### Week 1 — Quick Wins (Total: ~3 hours)

These are the highest ROI actions available. Each takes under 30 minutes and affects multiple platforms.

| # | Action | Where | Time | Impact |
|---|--------|-------|------|--------|
| 1 | Deploy spec-compliant `llms.txt` | Shopify Admin → Files | 15 min | All AI platforms |
| 2 | Fix FAQ page title: "Faqs" → "Frequently Asked Questions \| Happimess" | Shopify Admin → Pages → SEO | 5 min | Google AIO, Bing |
| 3 | Fix author name: "sandip hadiya" → "Sandip Hadiya" | Shopify Admin → Users | 5 min | Schema quality |
| 4 | Add blog publication dates to listing template | `blog-template.liquid` | 30 min | Freshness signals |
| 5 | Create Crunchbase company profile | crunchbase.com | 15 min | Brand authority |
| 6 | Register on BBB | bbb.org | 15 min | Trust signals |
| 7 | Update LinkedIn `/company/happimesshome/`: add domain, logo, description clarifying "happimess.com — NYC brand" | LinkedIn | 20 min | Entity disambiguation |
| 8 | Verify in Bing Webmaster Tools + submit sitemap | bing.com/webmasters | 20 min | Bing Copilot |

---

### Month 1 — High-Impact Technical & Content (Total: ~12–16 hours)

| # | Action | Where | Time | Impact |
|---|--------|--------|------|--------|
| 9 | Add hreflang to `theme.liquid` | Shopify theme editor | 2–4 hrs | EN/ES duplicate resolution |
| 10 | Install hreflang SEO app for sitemap annotations | Shopify App Store | 30 min | Closes sitemap gap |
| 11 | Add named bylines to top 10 articles | Shopify Admin → Blog | 2 hrs | E-E-A-T, citability |
| 12 | Create `/pages/meet-our-authors` with Jonathan Yaraghi bio | Shopify Admin → Pages | 2 hrs | Author credibility |
| 13 | Enable review app's Schema.org output for `aggregateRating` | Review app settings | 30 min | Gemini, AIO, Shopping |
| 14 | Add 2–3 external citations to top 5 blog articles | Blog articles | 2 hrs | Citability, AIO |
| 15 | Create Wikidata entity for Happimess | wikidata.org | 1 hr | Entity resolution |
| 16 | Register on Trustpilot; send review requests to past customers | business.trustpilot.com | 1 hr + ongoing | Third-party authority |
| 17 | Add `width`/`height` to all img tags in theme templates | product-card.liquid, article.liquid | 1–2 hrs | Core Web Vitals CLS |
| 18 | Create Google Business Profile (NYC) | business.google.com | 30 min | Gemini, Knowledge Panel |

---

### Months 2–3 — Strategic Content & Authority

| # | Action | Time | Impact |
|---|--------|------|--------|
| 19 | Publish "Products We Evaluated But Didn't Add — And Why" article | 4–6 hrs | Highest-citability original content |
| 20 | Add "Why We Recommend This" callout blocks to all 10 buying guides (cross-link testing protocol from About page) | 3–4 hrs | E-E-A-T reinforcement |
| 21 | Expand FAQ page: add 6–8 high-intent questions (trash can sizing, material, bag compatibility) | 1–2 hrs | FAQPage schema value, AIO |
| 22 | Pitch 2 press placement stories to The Spruce and/or Apartment Therapy | Ongoing | Wikipedia prerequisite, Perplexity |
| 23 | Set up HARO/Connectively alerts for "home organization," "kitchen organization," "trash can" | 30 min | Long-term press acquisition |
| 24 | Enrich author Person schemas: add `jobTitle`, `worksFor`, `description`, `sameAs` for both authors | 1–2 hrs | Schema completeness |

---

## Platform-Specific Readiness

### Google AI Overviews — 48 / 100
**Status:** Occasionally cited for trash-specific queries  
**To improve:** FAQPage schema on `/pages/faqs` (full JSON-LD in `GEO-SCHEMA-REPORT.md`), external citations in buying guides, named author bylines, `aggregateRating` on products.

### Perplexity AI — 44 / 100
**Status:** May surface for long-tail home organization queries  
**To improve:** Show publication dates in blog listing (Perplexity weights freshness heavily), add external citations to articles, increase Reddit presence in `r/organization` and `r/homeorganization`.

### ChatGPT Web Search — 38 / 100
**Status:** Brand likely unrecognized as entity; products may appear in general queries  
**To improve:** Wikidata entity creation is the fastest path to ChatGPT entity recognition. Crunchbase profile provides corroborating business signal.

### Bing Copilot — 38 / 100
**Status:** Not verified in Bing Webmaster Tools  
**To improve:** Verify site in Bing WMT (30 min), submit `https://happimess.com/sitemap.xml`, enable IndexNow for near-realtime URL submission. Fix FAQ page title. Add hreflang.

### Google Gemini — 37 / 100
**Status:** No product star ratings in AI recommendations  
**To improve:** `aggregateRating` schema on all Product pages is the single highest-impact Gemini fix. Google Business Profile creates the Google Knowledge Panel pathway. YouTube engagement improvement helps Gemini (YouTube is a Google property).

---

## Deployed Files (Ready to Use)

The following files have been created in this audit folder and are ready to deploy to the Shopify store:

| File | Destination | Deploy Via |
|------|------------|-----------|
| `llms.txt` | `https://happimess.com/llms.txt` | Shopify Admin → Content → Files |
| `llms-full.txt` | `https://happimess.com/llms-full.txt` | Shopify Admin → Content → Files |

**Complete JSON-LD code** for the following is in `GEO-SCHEMA-REPORT.md`:
- Organization `sameAs` update (add Crunchbase, Wikidata)
- Product `aggregateRating` Liquid snippet
- Full FAQPage schema (all 8 Q&A pairs)
- Enriched Person schemas for Jonathan Yaraghi and Sandip Hadiya
- BlogPosting additions (`articleSection`, `wordCount`, `keywords`)
- BreadcrumbList for About Us and FAQ

**hreflang Liquid code** is in `GEO-TECHNICAL-AUDIT.md` (paste into `theme.liquid` `<head>`)

---

## Score Projection

| Timeline | Actions | Projected Score |
|----------|---------|----------------|
| Current | — | 48 / 100 |
| Week 1 (quick wins) | llms.txt, FAQ title, bylines, dates, Crunchbase, Bing WMT | ~54 / 100 |
| Month 1 | + hreflang, aggregateRating, author bios, citations, Wikidata | ~62 / 100 |
| Month 3 | + press placement, content improvements, review platform | ~70 / 100 |
| 6 months | + Wikipedia article, sustained content, Reddit presence | ~78 / 100 |

---

## Report Index

All source documents from this audit are in the same folder:

| File | Contents |
|------|---------|
| `GEO-AUDIT-REPORT.md` | Composite scores, priority action plan, JSON-LD snippets |
| `GEO-CITABILITY-SCORE.md` | Per-page citability scores, best passages, scoring breakdown |
| `GEO-CRAWLER-ACCESS.md` | robots.txt analysis, full AI crawler access map |
| `llms.txt` | Spec-compliant llms.txt — ready to deploy |
| `llms-full.txt` | Comprehensive version — all 26 articles + developer access |
| `GEO-BRAND-MENTIONS.md` | Platform-by-platform brand authority, LinkedIn collision detail |
| `GEO-PLATFORM-OPTIMIZATION.md` | Per-platform scores, FAQPage JSON-LD, Bing setup, Wikidata guide |
| `GEO-SCHEMA-REPORT.md` | Full schema audit, all 10 JSON-LD fixes ready to paste |
| `GEO-TECHNICAL-AUDIT.md` | Technical SEO, hreflang code, CLS fix, sitemap analysis |
| `GEO-CONTENT-ANALYSIS.md` | E-E-A-T scoring, article quality breakdown, content roadmap |
| `GEO-CLIENT-REPORT.md` | **This file** — consolidated deliverable |

---

## Key Numbers to Remember

| Metric | Value |
|--------|-------|
| Overall GEO Score | **48 / 100** |
| AI Crawlers with full access | **10 / 10** |
| Articles with external citations | **1 / 26** |
| Articles with named author | **0 / 26** |
| Pages with hreflang | **0 / ~826** |
| Brand authority score | **28 / 100** |
| Potential score in 90 days | **~70 / 100** |

---

*GEO Audit conducted 2026-05-18. All 10 sub-analyses complete. Next audit recommended: 2026-08-18, or after Tier 1 + Tier 2 actions are complete.*
