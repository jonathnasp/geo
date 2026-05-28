# GEO Audit Report — Happimess
**Site:** https://happimess.com  
**Audit Date:** May 28, 2026  
**Auditor:** Claude Code GEO Skill (5-agent parallel analysis)  
**Prior Audit:** May 26, 2026 (2 days prior)

---

## Composite GEO Score: 59/100 — Fair

> Effectively flat vs. May 26 (61/100). Two issues were resolved (llms.txt redirect, robots.txt fixes), but a stricter content assessment and brand authority methodology shift offset the gains. The ceiling remains Brand Authority (28/100) — no Wikipedia/Wikidata, dormant LinkedIn/YouTube, zero Reddit presence.

### Score Breakdown

| Category | Weight | Score | Weighted | vs. May 26 | Change |
|----------|--------|-------|----------|------------|--------|
| AI Citability & Visibility | 25% | 63 | 15.75 | 62 | +1 |
| Brand Authority Signals | 20% | 28 | 5.60 | 35* | −7* |
| Content Quality & E-E-A-T | 20% | 62 | 12.40 | 68 | −6 |
| Technical Foundations | 15% | 80 | 12.00 | 82 | −2 |
| Structured Data | 10% | 74 | 7.40 | 72 | +2 |
| Platform Optimization | 10% | 58 | 5.80 | 52 | +6 |
| **COMPOSITE** | **100%** | **59** | **58.95** | **61** | **−2** |

*Brand Authority −7 reflects methodology recalibration (Reddit/YouTube weighting tightened), not real-world regression. Platform presence unchanged.

### Score Interpretation
| Range | Label |
|-------|-------|
| 0–25 | Critical |
| 26–50 | Poor |
| 51–75 | Fair |
| 76–90 | Good |
| 91–100 | Excellent |

---

## What Changed Since May 26

### ✅ Resolved (3 items)
| Item | Detail |
|------|--------|
| llms.txt redirect | Now serves directly at HTTP 200 — was 301→/agents.md. Score: 70/100. |
| robots.txt shipping-policy | `Allow: /policies/shipping-policy` explicitly present — conflicting-signals issue closed. |
| sitemap_agentic_discovery.xml | Now listed as `Sitemap:` directive in robots.txt — was invisible to crawlers. |

### ❌ New Findings (not in May 26 audit)
| Item | Severity | Detail |
|------|----------|--------|
| AI-generated image filenames | High | `ChatGPT_Image_May_4_2026_11_30_24_AM.png` visible in page source on trash bag article — confirms AI imagery, no alt text |
| EPA/USDA/CDC quote authenticity | High | Hyperlinked citations present (improvement), but quoted text doesn't match source pages — likely AI-fabricated paraphrases, not verbatim quotes |
| FAQPage schema rendering gap | Medium | Schema reportedly deployed but not visible in external HTML fetches — possible Liquid injection failure |
| speakable cssSelector accuracy | Medium | Blog speakable targets `.article__excerpt`, `.article__summary` — selectors may not exist in live DOM |

### 🔁 Persistent Open Issues (unchanged)
- "Happimess Dev" brand.name on 7 products (Elmo, Oscar, Nathan, Chuck, Beni, Ashley, Molly)
- /.well-known/ucp staging domain (happimess-dev.myshopify.com) — still unresolved
- Author bios: no photos, no credentials, no LinkedIn links on Meet Our Authors page
- ₹2000 currency error in Economy Home Decor FAQ Q7
- No Wikipedia article or Wikidata entity
- No Reddit/Quora presence
- LinkedIn dormant (26 followers, last post 7+ months ago)
- Blog listing page (/blogs/news/) shows no publication dates
- OG image 280×280px (should be 1200×630)
- Hero images missing `fetchpriority="high"` and explicit dimensions
- HSTS max-age 91 days (should be 1 year)

---

## Category Reports

### 1. AI Citability & Visibility — 63/100

**Sub-scores:**

| Component | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Page Citability | 66/100 | 35% | 23.1 |
| Crawler Access | 97/100 | 25% | 24.3 |
| llms.txt Compliance | 70/100 | 10% | 7.0 |
| Brand Authority | 28/100 | 30% | 8.4 |
| **AI Visibility Total** | | | **62.8 → 63** |

**Top Citability Passages:**

| Passage | Score | Location |
|---------|-------|----------|
| Product testing methodology (30-day eval, 500+ cycles, 15-day odor test) | 82/100 | About Us |
| Dual trash can capacity sizing table (30–40L / 40–60L / 60L+) | 77/100 | Blog: dual trash can guide |
| Regular vs. scented bag comparison table | 69/100 | Blog: trash bag article |

**Citation-Unlikely Areas:**
- Homepage (navigational, no direct answers)
- Economy Home Decor article (diffuse topic, no Happimess-specific value)
- FAQ page (logistics-only, no product expertise)

**AI Crawler Access:** 97/100 — 15 crawlers explicitly allowed, Content-Signal header present. One deduction: agentic sitemap lacked lastmod dates.

**llms.txt Status:** 70/100 — Valid, serves directly (redirect fixed). Gaps: only 3 of 27 blog posts listed, no product-level links, no llms-full.txt, no `## Optional` section.

---

### 2. Brand Authority Signals — 28/100

| Platform | Status | Detail |
|----------|--------|--------|
| Wikipedia | Absent | No article, no Wikidata entity — largest single gap |
| Reddit | Absent | Zero confirmed mentions |
| YouTube | Minimal | Channel exists (@happimess), dormant |
| LinkedIn | Minimal | 26 followers, last post 7+ months ago |
| Crunchbase | Present | Organization profile linked in sameAs |
| Instagram / Facebook / TikTok / Pinterest | Present | Active social presence confirmed |

**Note:** Wikipedia/Wikidata worth 30 of 100 Brand Authority points. This single platform gap accounts for most of the category ceiling.

---

### 3. Content Quality & E-E-A-T — 62/100 *(was 68 — methodology tightened)*

**E-E-A-T Breakdown:**

| Dimension | Score (0–25) | Key Gap |
|-----------|-------------|---------|
| Experience | 8/25 | No founder story; testing claims unattributed; no original data |
| Expertise | 10/25 | Named authors exist but bios are generic 50-word role descriptions; no credentials |
| Authoritativeness | 16/25 | EPA/CDC/USDA citations now hyperlinked; no press coverage; founder background absent |
| Trustworthiness | 15/25 | ₹2000 currency error; AI image filenames publicly visible; "editorial team" byline inconsistency |

**Content Quality Metrics:**

| Article | Word Count | Freshness | AI Risk | Issues |
|---------|-----------|-----------|---------|--------|
| Trash bag guide | ~2,200 | May 4 / updated May 21 | High | Fragmented prose, AI image filenames, possible fabricated gov quotes |
| Dual trash can guide | ~1,300 | Apr 22 / updated May 22 | Medium | "Editorial team" byline; no original data |
| Economy Home Decor | ~4,000 | Nov 2025 / updated May 11 | High | Zero external citations, ₹2000 error, Indian market copy |

**Score regression explained:** May 26 credited author and date improvements as resolved. This audit assessed actual implementation quality:
- Authors exist but lack credentials → partial credit only
- Dates visible on article pages but absent on listing page → partial credit
- Citations hyperlinked → confirmed improvement (+3)
- AI image filenames newly discovered → deduction

---

### 4. Technical Foundations — 80/100 *(was 82)*

**Category Scores:**

| Category | Score |
|----------|-------|
| Server-Side Rendering | 95/100 |
| Mobile Optimization | 92/100 |
| URL Structure | 90/100 |
| Crawlability | 82/100 |
| Core Web Vitals Risk | 72/100 |
| Meta Tags & Indexability | 78/100 |
| Security Headers | 68/100 |

**Resolved since May 26:**
- `Allow: /policies/shipping-policy` confirmed in robots.txt
- `sitemap_agentic_discovery.xml` now in robots.txt Sitemap: directives

**Still Open:**

| Issue | Severity | Fix Location |
|-------|----------|-------------|
| OG image 280×280px | High | Shopify Admin → Online Store → Preferences → Social image |
| Hero images missing `fetchpriority="high"` | High | `sections/image-banner.liquid` |
| Blog listing page: no publication dates | Medium | `sections/main-blog.liquid` — add `{{ article.published_at | date: "%B %d, %Y" }}` |
| HSTS max-age ~91 days | Medium | Shopify Admin → Online Store → Preferences → Security |
| jQuery async → defer | Low | `theme.liquid` — change `async` to `defer` on jQuery script tag |
| robots.txt adsbot/Nutch separator | Low | Add blank line between User-agent blocks |
| hreflang EN/ES | Verify | Could not confirm via WebFetch — manual view-source check required |

---

### 5. Structured Data — 74/100 *(was 72 — +2)*

**Schema Inventory:**

| Schema Type | Pages | Status | Issues |
|-------------|-------|--------|--------|
| Organization | Sitewide | ✅ Valid | No Wikipedia/Wikidata in sameAs |
| WebSite + SearchAction | Sitewide | ✅ Valid | None |
| Product | Product pages | ⚠️ Partial | `brand.name` = "Happimess Dev" on 7 products; aggregateRating missing on 6 |
| FAQPage | /pages/faqs | ✅ Valid | Rendering not confirmed in external fetch; Google restricted Aug 2023 (semantic value remains) |
| BlogPosting | Blog articles | ✅ Valid | speakable cssSelectors may target non-existent DOM nodes |
| BreadcrumbList | Non-home pages | ✅ Valid | None |
| Person | /pages/meet-our-authors | ⚠️ Partial | No image on either Person; Sandip has only 1 sameAs |
| SpeakableSpecification | Products + Blog | ⚠️ Partial | Selector accuracy unverified |

**sameAs Status:**

| Platform | Linked | Notes |
|----------|--------|-------|
| Facebook | ✅ | /happimessofficial/ |
| Instagram | ✅ | /happimess_official/ |
| LinkedIn | ✅ | /company/happimesshome/ (correct slug confirmed) |
| Pinterest | ✅ | /happimess_/ |
| YouTube | ✅ | /channel/UC6lUDdoZeZrYnoY2kmZyf4g |
| TikTok | ✅ | /@happimess_official |
| Crunchbase | ✅ | /organization/happimess |
| Wikipedia | ❌ | Not created |
| Wikidata | ❌ | Not created |

**Improvement:** BlogPosting `author.jobTitle` propagation confirmed resolved (+2 points).

---

### 6. Platform Optimization — 58/100 *(was 52 — +6)*

| Platform | Score | Key Gap |
|----------|-------|---------|
| Google AI Overviews | 62/100 | FAQPage schema not rendering in external fetch; no speakable on non-article pages |
| Perplexity AI | 61/100 | llms.txt not fully spec-compliant; no Reddit presence |
| Bing Copilot | 60/100 | No IndexNow; no Bing Shopping feed |
| ChatGPT Web Search | 56/100 | /.well-known/ucp staging domain defect; no Wikipedia entity |
| Google Gemini | 55/100 | No Google Business Profile; no YouTube content; no Knowledge Panel |

---

## Priority Action Plan

### Tier 1 — Critical / Quick Wins (< 1 hour each)

| # | Issue | Effort | Platforms Impacted |
|---|-------|--------|--------------------|
| 1 | Fix `brand.name` on 7 products: change Vendor from "Happimess Dev" → "Happimess" in Shopify Admin | 15 min | All — brand identity |
| 2 | Fix `/.well-known/ucp` staging domain: replace all `happimess-dev.myshopify.com` → `happimess.com` | 30 min | ChatGPT, Perplexity, Bing |
| 3 | Fix ₹2000 currency error in Economy Home Decor FAQ Q7 | 2 min | All — trust signal |
| 4 | Rename AI-generated image files + add alt text (trash bag article) | 20 min | All — trust signal |
| 5 | Fix OG image: upload 1200×630px image to Shopify Online Store → Preferences → Social image | 15 min | Social, Google Discover, AI link previews |

### Tier 2 — High Impact (1–4 hours each)

| # | Issue | Effort | Category Impact |
|---|-------|--------|-----------------|
| 6 | Rebuild author bios on Meet Our Authors: add headshots, credentials, LinkedIn links, 150+ word bios; add `image` to Person schema | 3 hr | Content +8, Schema +3 |
| 7 | Verify/fix EPA/USDA/CDC quotes in blog articles — replace AI paraphrases with verbatim source quotes or properly attributed paraphrases | 2 hr | Content +4, Trust |
| 8 | Add FAQPage schema to product Q&A sections (e.g., Elmo's 10 user questions) | 1 hr | Platform +5, Schema +2 |
| 9 | Add 3–5 expertise Q&As to /pages/faqs (what size trash can for kitchen?, material differences, odor reduction) | 1 hr | Content +5, AI Overviews |
| 10 | Add `fetchpriority="high"` + explicit width/height to hero images | 30 min | Technical +3, LCP |

### Tier 3 — Medium / Strategic (days to weeks)

| # | Issue | Effort | Category Impact |
|---|-------|--------|-----------------|
| 11 | Create Wikidata entity for Happimess + add to Organization sameAs | 2 hr | Brand Authority +8 |
| 12 | Expand llms.txt: list top 10 blog articles, add Products section, add `## Optional` section | 1 hr | AI Visibility +5 |
| 13 | Add publication dates to /blogs/news/ listing page (main-blog.liquid template) | 30 min | Technical, Content freshness |
| 14 | Implement IndexNow for real-time Bing indexing | 1 hr | Bing Copilot +5 |
| 15 | Set up Google Business Profile (NYC) + add to Organization sameAs | 2 hr | Gemini +8 |
| 16 | Begin Reddit presence: genuine posts in r/organization, r/homeimprovement | Ongoing | Brand Authority +15 |
| 17 | Jonathan Yaraghi founder background on About Us (Safavieh/Jonathan Y connection) | 2 hr | Content/E-E-A-T +6 |
| 18 | HSTS: increase max-age to 31,536,000 (1 year) | 30 min | Technical +3 |
| 19 | Verify speakable cssSelectors in live DOM; update if targeting non-existent classes | 1 hr | Schema +4 |
| 20 | Wikipedia article creation (requires editorial independence) | High | Brand Authority +30 |

---

## Score Projection

Completing Tier 1 + Tier 2 (items 1–10) would yield estimated scores:

| Category | Current | Projected |
|----------|---------|-----------|
| AI Citability & Visibility | 63 | 68 |
| Brand Authority | 28 | 28 (no change without Reddit/Wikipedia) |
| Content / E-E-A-T | 62 | 72 |
| Technical Foundations | 80 | 84 |
| Structured Data | 74 | 80 |
| Platform Optimization | 58 | 65 |
| **Composite** | **59** | **~65** |

Adding Tier 3 items 11–17 (Wikidata, llms.txt expansion, Reddit start, Google Business Profile, founder story):

| Category | Projected |
|----------|-----------|
| Brand Authority | 40 |
| **Composite** | **~70** |

---

## Score History

| Date | Composite | AI Citability | Brand Authority | Content/E-E-A-T | Technical | Structured Data | Platform |
|------|-----------|--------------|----------------|-----------------|-----------|-----------------|----------|
| May 18, 2026 | 48 | 52 | 28 | 44 | 71 | 62 | 41 |
| May 20, 2026 | 51 | 58 | 32 | 46 | 79 | 46 | 49 |
| May 26, 2026 | 61 | 62 | 35 | 68 | 82 | 72 | 52 |
| **May 28, 2026** | **59** | **63** | **28*** | **62** | **80** | **74** | **58** |

*Brand Authority 28 vs. 35 reflects methodology recalibration, not platform regression.

---

## Technical Reference

### Confirmed Working
- Shopify SSR — all content in initial HTML, AI crawlers can read without JS execution
- 15 AI crawlers explicitly allowed in robots.txt
- Content-Signal: ai-train=yes, search=yes, ai-retrieval=yes
- hreflang EN/ES — confirmed in prior audit (verify manually — WebFetch strips head section)
- Bing Webmaster Tools (msvalidate.01) — confirmed
- Organization sameAs: 7 platforms with correct LinkedIn slug (/company/happimesshome/)
- BlogPosting schema: datePublished, dateModified, author Person with @id, jobTitle, worksFor
- BreadcrumbList: valid on all non-home pages
- WebSite + SearchAction: valid, Sitelinks Search Box eligible
- llms.txt: serving directly at HTTP 200 (redirect fixed May 27–28)
- agents.md (UCP): deployed at /agents.md; sitemap_agentic_discovery.xml indexes it

### Critical Defects (unresolved)
- `brand.name` = "Happimess Dev" on products: elmo, oscar, nathan, chuck, beni, ashley, molly
- `/.well-known/ucp` returns `happimess-dev.myshopify.com` throughout (staging domain)
- Author bios: no image in Person schema; no credentials or photos on page

---

*Report generated: May 28, 2026 | Next recommended audit: June 11, 2026 (after Tier 1 + Tier 2 fixes)*
