# GEO Audit Report — Happimess
**Site:** https://happimess.com  
**Date:** 2026-05-26  
**Previous Audit:** 2026-05-20  
**Auditor:** Claude Code + 5 parallel GEO subagents  
**Business Type:** E-commerce (Shopify) — Home Organization, Storage, Trash Management

---

## Composite GEO Score: 57/100 (Fair)

> **+6 points from 51/100** since the May 20 audit. The biggest gain is Structured Data (+22) — BlogPosting schema, FAQPage schema, and named-author Person schemas are now deployed across the site. Content quality improved (+6) with external citations (EPA, USDA, CDC) now appearing in blog posts and author names replacing admin usernames. The ceiling is now Brand Authority (35/100): no Wikipedia/Wikidata entity, dormant LinkedIn and YouTube, and zero Reddit community presence.

### Score Breakdown

| Category | Weight | Score | vs. May 20 | Status |
|----------|--------|-------|------------|--------|
| AI Citability & Visibility | 25% | 62/100 | +4 | Fair |
| Brand Authority Signals | 20% | 35/100 | +3 | Poor |
| Content Quality / E-E-A-T | 20% | 52/100 | +6 | Fair |
| Technical Foundations | 15% | 82/100 | +3 | Good |
| Structured Data | 10% | 68/100 | +22 | Fair |
| Platform Optimization | 10% | 52/100 | +3 | Fair |
| **Composite** | | **57/100** | **+6** | **Fair** |

### Score History

| Date | Composite | AI Citability | Brand Authority | Content/E-E-A-T | Technical | Structured Data | Platform |
|------|-----------|--------------|----------------|-----------------|-----------|-----------------|----------|
| 2026-05-18 | 48 | 52 | 28 | 44 | 71 | 62 | 41 |
| 2026-05-20 | 51 | 58 | 32 | 46 | 79 | 46* | 49 |
| 2026-05-26 | **57** | **62** | **35** | **52** | **82** | **68** | **52** |

*May 20 Structured Data was conservative — product/article schemas unverifiable due to 404 on test URL.

### Score Scale
| Range | Status |
|-------|--------|
| 0–25 | Critical |
| 26–50 | Poor |
| 51–75 | Fair |
| 76–90 | Good |
| 91–100 | Excellent |

---

## What Changed Since May 20

### Resolved ✅

| # | Issue | Fix Confirmed |
|---|-------|--------------|
| N1a | About-us page title "About us" (generic) | Now: "About Happimess \| Home Organization Experts, New York" |
| N1b | Meta description missing on `/pages/about-us` | 160-char description now present |
| N1c | Meta description missing on `/pages/faqs` | 155-char description now present |
| N2 | jQuery 3.5.1 render-blocking in `<head>` | `async` attribute added — no longer render-blocking |
| N3 | Poppins font preloaded 3× (duplicate) | Single preload confirmed |
| — | No BlogPosting/Article schema on blog posts | Full BlogPosting schema on all articles: datePublished, dateModified, articleBody, wordCount, speakable |
| — | No FAQPage schema on `/pages/faqs` | FAQPage JSON-LD with 8 Q&A pairs now deployed; also present on product pages |
| — | Admin usernames in blog JSON-LD | "jonathany 2123" / "Asodariya Sumi" replaced with Jonathan Yaraghi and Sandip Hadiya |
| — | No named blog authors | `/pages/meet-our-authors` now exists with Person schema for both authors |
| — | Zero external citations in blog posts | EPA, USDA, and CDC cited in at least 2 recent articles |
| — | robots.txt syntax defect (main block) | `User-agent: *` → adsbot-google transition now clean |
| — | Publication dates not visible | Dates and last-modified timestamps visible on all blog articles |
| — | Organization sameAs incomplete | Crunchbase added; now 7 platforms total |
| — | Shopify `Shopify.shop` dev identifier | `happimess-dev.myshopify.com` appears in page JS (internal only; not user/crawler-facing) |

### Still Open from May 20 ⚠️

| # | Issue | Severity | Status |
|---|-------|----------|--------|
| O1 | `/.well-known/ucp` returns `happimess-dev.myshopify.com` staging URLs | High | **Unresolved** — identical to May 20 finding |
| O2 | `/llms.txt` → 301 redirect to `/agents.md` — not a valid llms.txt spec file | High | **Unresolved** — redirect changed (was serving content directly; now a 301) but still non-compliant |
| O3 | `"Happimess Dev"` in Product JSON-LD `brand.name` on 7 specific products | High | **Partially resolved** — 22/29 trash-can products correct; 7 still show "Happimess Dev" |
| O4 | robots.txt adsbot-google → Nutch block missing blank line | Low | **Partially resolved** — main block fixed; adsbot-google/Nutch transition still has syntax defect |
| O5 | No Wikipedia article or Wikidata entity | High | **Unresolved** |
| O6 | No Reddit / Quora community presence | High | **Unresolved** |
| O7 | LinkedIn dormant (26 followers, last post 7+ months ago) | Medium | **Unresolved** |
| O8 | YouTube channel inactive | Medium | **Unresolved** |
| O9 | No aggregateRating on most products | Medium | **Unresolved** — only 1 product has aggregateRating |
| O10 | Blog listing page (`/blogs/news`) shows no publication dates | Low | **Unresolved** |

### New Issues Found 🆕

| # | Issue | Severity |
|---|-------|----------|
| N1 | External citations paraphrased without hyperlinks — AI models cannot verify source chain | High |
| N2 | No `sameAs` or `image` on Person schemas (Jonathan Yaraghi, Sandip Hadiya) | Medium |
| N3 | BlogPosting `author` object missing `jobTitle` propagation from Person record | Low |
| N4 | `speakable` missing on Product pages (present on BlogPosting only) | Medium |
| N5 | HSTS `max-age` weak at 91 days (7,889,238s) — recommended minimum 1 year | Low |
| N6 | No `Referrer-Policy` or `Permissions-Policy` as HTTP headers (meta-tag only) | Low |
| N7 | FAQ page content is entirely transactional (shipping/returns) — no expertise Q&As | Medium |
| N8 | `sitemap_agentic_discovery.xml` not listed in robots.txt `Sitemap:` directive | Low |
| N9 | jQuery: `async` improved over sync but `defer` is safer for dependency order | Low |
| N10 | Hero images missing `fetchpriority="high"` and explicit width/height (LCP/CLS risk) | Medium |

---

## AI Visibility Analysis

**AI Visibility Score: 55/100**

### Sub-Scores

| Component | Score | Change | Notes |
|-----------|-------|--------|-------|
| AI Citability | 62/100 | +4 | EPA/USDA/CDC citations; article schema with speakable |
| Brand Authority | 35/100 | +3 | Multi-retailer presence; no Wikipedia/Reddit/Wikidata |
| Crawler Access | 97/100 | 0 | 15 AI crawlers explicitly allowed; Content-Signal declared |
| llms.txt Compliance | 20/100 | 0 | File exists but serves agents.md content — not spec-compliant |

### Top Citation-Ready Passages

| Passage | Page | Citability Score |
|---------|------|-----------------|
| Scent recommendation comparison (lemon = kitchen, lavender = bathroom) | Scented bags blog | 78/100 |
| "According to the U.S. Environmental Protection Agency, separating recyclable materials at source reduces contamination" | Dual trash can blog | 76/100 |
| FAQ block: "Are scented trash bags safe for families/pets?" with direct answers | Blog | 74/100 |
| Comparison table: Regular Trash Bags vs Happimess Scented Trash Liners | Blog | 70/100 |

### AI Crawler Access

All 15 major AI crawlers explicitly allowed: GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, anthropic-ai, PerplexityBot, Google-Extended, Amazonbot, CCBot, Applebot-Extended, FacebookBot, Bytespider, cohere-ai, DiffbotBot, YouBot.

`Content-Signal: ai-train=yes, search=yes, ai-retrieval=yes` declared. `sitemap_agentic_discovery.xml` indexes agents.md. Homepage carries `<link rel="ai-instructions" href="/agents.md">` and `<meta name="agents" content="/agents.md">` in `<head>`.

### Brand Mention Presence (35/100)

| Platform | Status | Details |
|----------|--------|---------|
| Wikipedia | Absent | No article; no Wikidata entity — largest AI entity-recognition gap |
| Reddit | Absent | Zero indexed threads for "happimess" |
| YouTube | Minimal | Channel exists but appears inactive/very low traffic |
| LinkedIn | Minimal | 26 followers, last post 7+ months ago |
| Retail channels | Strong | Amazon brand store, Home Depot, Wayfair, Macy's, Target, Lowe's, HSN — strong distribution signal |
| Crunchbase | Present | Profile confirmed; added to sameAs |

---

## Platform Optimization

**Platform Optimization Score: 52/100**

| Platform | Score | Change | Key Gap |
|----------|-------|--------|---------|
| Google AI Overviews | 51/100 | +6 | FAQPage schema restricted; needs Article schema with E-E-A-T signals |
| ChatGPT Web Search | 56/100 | +8 | /.well-known/ucp staging domain breaks agentic trust |
| Perplexity AI | 44/100 | +4 | Zero Reddit/community validation; citations not hyperlinked |
| Google Gemini | 49/100 | +2 | No YouTube content; no Knowledge Graph entity |
| Bing Copilot | 58/100 | +3 | No active LinkedIn; no IndexNow; meta descriptions now present |

---

## Technical Foundations

**Technical Score: 82/100** (Good)

| Check | Status | Notes |
|-------|--------|-------|
| Server-Side Rendering | ✅ Pass | Shopify SSR — full HTML in initial response; JSON-LD in `<head>` |
| Meta Tags / Indexability | ✅ Pass | Title, description, OG, Twitter Cards all present and valid |
| Canonical Tags | ✅ Pass | Self-referencing on all tested pages |
| hreflang EN/ES | ✅ Pass | Bidirectional hreflang confirmed; no regression |
| HTTPS / Security | ✅ Pass | TLS via Cloudflare; X-Frame-Options DENY; nosniff |
| Mobile Optimization | ✅ Pass | Responsive grid; proper viewport; srcset on images |
| Sitemap | ✅ Pass | 9 child sitemaps; lastmod timestamps; agentic_discovery sitemap present |
| jQuery render-blocking | ✅ Fixed | `async` attribute added (recommend upgrading to `defer`) |
| Poppins duplicate preload | ✅ Fixed | Single preload confirmed |
| robots.txt AI crawlers | ✅ Pass | 15 crawlers explicitly allowed |
| robots.txt syntax (Nutch block) | ⚠️ Partial | adsbot-google → Nutch still missing blank-line separator |
| llms.txt | ❌ Fail | 301 redirect to agents.md; not a spec-compliant llms.txt |
| /.well-known/ucp | ❌ Fail | Returns happimess-dev.myshopify.com staging URLs |
| HSTS max-age | ⚠️ Weak | 91 days (7,889,238s); recommend 1 year (31,536,000s) |
| Hero image LCP | ⚠️ Risk | No `fetchpriority="high"`; no explicit width/height on hero images |
| Third-party script overhead | ⚠️ Note | 7 async third-party scripts (session recording, UGC gallery, countdown timer) |
| HTTPS canonical consistency | ⚠️ Minor | Homepage canonical has trailing slash; `/es/` canonical does not |

---

## Structured Data

**Schema Score: 68/100** (Fair, +22 vs. May 20)

| Schema Type | Presence | Status |
|-------------|----------|--------|
| Organization + sameAs (7 platforms) | All pages | ✅ Valid — 7 sameAs; Wikipedia/Wikidata absent |
| WebSite + SearchAction | All pages | ✅ Valid |
| WebPage (homepage) | Homepage | ✅ Valid |
| FAQPage | /pages/faqs + product pages | ✅ Valid — rich results restricted for non-authority sites; semantic value for AI |
| BreadcrumbList | All inner pages | ✅ Valid |
| BlogPosting | All blog articles | ✅ Valid — datePublished, dateModified, articleBody, wordCount, speakable |
| Person (authors) | /pages/meet-our-authors | ⚠️ Partial — no sameAs or image |
| Product | Product pages | ⚠️ Error — 7 products have `brand.name: "Happimess Dev"` |
| aggregateRating | 1 of 29 products | ❌ Missing on most products |
| speakable on Products | Product pages | ❌ Missing |

### Products Still Carrying "Happimess Dev" brand.name

The following 7 products in the trash-cans collection have the Vendor field set to "Happimess Dev" in Shopify Admin. Fix: go to each product → change Vendor to "Happimess".

1. elmo-rectangular-8-gallon-double-bucket-trash-can-with-soft-close-lid
2. beni-kitchen-trashrecycling-trash-can
3. chuck-kitchenoffice-trash-can
4. ashley-rectangular-8-gallon-trash-can-with-soft-close-lid
5. oscar-round-8-gallon-step-open-trash-can-with-free-standing-lid
6. molly-round-8-gallon-step-open-trash-can-with-free-standing-lid
7. nathan-round-8-gallon-step-open-trash-can-with-free-standing-lid

---

## Content Quality / E-E-A-T

**Content Score: 52/100** (Fair, +6 vs. May 20)

| Dimension | Score | Change | Key Finding |
|-----------|-------|--------|-------------|
| Experience | 8/25 | +1 | Gov citations added; zero first-hand testing narratives; unattributed testimonials |
| Expertise | 9/25 | +3 | Named authors now present; no individual credential bios on author page |
| Authoritativeness | 12/25 | +3 | About page improved; no press/awards/certifications |
| Trustworthiness | 17/25 | +2 | Dates visible; contact info complete; no editorial standards page |

### Key Content Findings

- **Authors named but thin:** Jonathan Yaraghi and Sandip Hadiya appear in BlogPosting schema and on meet-our-authors page, but no individual credentials, no photos, no sameAs LinkedIn links. The author page bio is one brief paragraph per person.
- **Citations present but not hyperlinked:** EPA, USDA, CDC referenced in blog prose — but as paraphrased text, not linked to specific source URLs. AI models that validate citations will hit dead ends.
- **FAQ page is transactional only:** 8 Q&As cover shipping, returns, order modification. No expertise Q&As about product selection, home organization, or category knowledge.
- **About page thin:** ~475 words. The testing methodology claim ("30-day evaluation, 500+ cycles") is the strongest authority signal on the site but is not cross-referenced from blog posts.
- **AI-generated content signals:** Hedging language, formulaic listicle structure, uniform neutral tone, and zero original data across blog corpus suggest AI-generated content with light human editing. The government citations are the main differentiating human edit.
- **Blog listing page:** Still no publication dates on `/blogs/news` index — dates only appear inside articles.

---

## Prioritized Action Plan

### Quick Wins (≤2 hours each)

| Priority | Issue | Action | Effort | GEO Impact |
|----------|-------|--------|--------|------------|
| 🔴 1 | `"Happimess Dev"` brand.name on 7 products | In Shopify Admin → Products, change Vendor field from "Happimess Dev" to "Happimess" for each of the 7 listed products | 15 min | High |
| 🔴 2 | Fix `/.well-known/ucp` staging domain | Replace all `happimess-dev.myshopify.com` references in UCP config with `happimess.com` | 30 min | High |
| 🔴 3 | Create spec-compliant `/llms.txt` | Deploy a proper llms.txt per spec at root (separate from agents.md). Content: site name, description blockquote, key page links, blog index, policy links | 45 min | All platforms |
| 🟡 4 | Hyperlink citations in blog posts | Find all EPA, USDA, CDC prose references and add `<a href="[source-url]">` links to specific source pages | 1 hr | +3–4 citability |
| 🟡 5 | Add author LinkedIn sameAs to Person schemas | Add `sameAs: ["[LinkedIn URL]"]` to both Person blocks on meet-our-authors | 20 min | E-E-A-T |
| 🟡 6 | Add author headshot images to Person schemas | Upload author photos to Shopify CDN; add `image.url` to each Person block | 30 min | E-E-A-T |
| 🟡 7 | Fix robots.txt blank line (Nutch block) | Add blank line between `Disallow: /services/login_with_shop` and `User-agent: Nutch` | 5 min | Crawl parity |
| 🟡 8 | Add `sitemap_agentic_discovery.xml` to robots.txt `Sitemap:` directive | Add second `Sitemap:` line: `Sitemap: https://happimess.com/sitemap_agentic_discovery.xml` | 5 min | Agentic discovery |

### Medium-Term (1–2 days each)

| Priority | Issue | Action | Effort | GEO Impact |
|----------|-------|--------|--------|------------|
| 🟡 9 | Create Wikidata entity for Happimess | Create a Wikidata Q-entity: instance of (brand/company), country (US), founded, website, retail channels | 2 hrs | +9 brand authority |
| 🟡 10 | Add expertise Q&As to `/pages/faqs` | Add 8–10 product/category Q&As (trash can sizing, sensor vs. pedal, bag sizing, odor control) alongside existing 8 transactional Q&As | 2 hrs | Google AIO, citability |
| 🟡 11 | Add `speakable` to Product JSON-LD | Add speakable cssSelector block targeting product title, description, price in product.liquid template | 1 hr | ChatGPT shopping |
| 🟡 12 | Propagate author `jobTitle` into BlogPosting schema | Add `"jobTitle": "..."` to the author Person object in blog article liquid template | 30 min | E-E-A-T |
| 🟡 13 | Add publication dates to `/blogs/news` listing | Edit blogs list template to display `article.published_at` on each listing card | 30 min | Freshness signals |
| 🟡 14 | Implement IndexNow via Bing Webmaster Tools | Generate API key; upload key file to Shopify; configure sitemap ping | 1 hr | Bing Copilot |
| 🟡 15 | Switch jQuery from `async` to `defer` | Change `async` → `defer` on jQuery script tag in theme.liquid | 5 min | INP / CWV |
| 🟡 16 | Add `fetchpriority="high"` to hero images | Edit hero banner section template; add attribute + explicit width/height to above-fold images | 1 hr | LCP / CWV |

### Strategic (1–4 weeks)

| Priority | Issue | Action | Effort | GEO Impact |
|----------|-------|--------|--------|------------|
| 🔵 17 | Activate LinkedIn company page | Post 2×/month minimum; complete profile (description, industry, size, location, logo) | Ongoing | +8–10 brand authority |
| 🔵 18 | Add individual author credential bios | Expand meet-our-authors with years of experience, areas of expertise, education, specific recommendations made | 4 hrs | E-E-A-T ceiling |
| 🔵 19 | Seed Reddit presence | Answer real questions in r/organization, r/ZeroWaste, r/homemaking where Happimess products are genuinely relevant | Ongoing | +10–15 brand authority |
| 🔵 20 | Add one original dataset per blog article | Reference the "30-day, 500+ cycle" testing protocol with specific numeric results in product guide posts | Ongoing | Citability anchor |
| 🔵 21 | Add Wikipedia article or strengthen Wikidata | Once Wikidata entity created, gather notability evidence (HSN, Home Depot, press coverage) for eventual Wikipedia article | 1–4 weeks | +15 brand authority |
| 🔵 22 | Add `aggregateRating` to all products | Integrate review platform (Okendo, Judge.me) to generate Product schema ratings | Ongoing | Shopping rich results |

---

## Technical Fixes — Ready-to-Deploy Code

### Fix 1: llms.txt (deploy to Shopify Files → redirect /llms.txt)

```
# Happimess

> Home organization, storage furniture, trash management, and kitchen products — designed to make clutter-free living stylish and accessible. NYC-based, founded 2020.

## Store

- [Homepage](https://happimess.com/): Full product catalog — trash cans, storage bins, organization furniture, kitchen accessories
- [Trash Cans Collection](https://happimess.com/collections/trash): Sensor, pedal, and manual trash cans for kitchen and bathroom
- [Organization](https://happimess.com/collections/organization): Storage bins, drawer organizers, closet solutions
- [Storage Furniture](https://happimess.com/collections/storage-furniture): Shelving, cabinets, and storage units
- [Subscribe & Save](https://happimess.com/pages/refill-page): Subscription refill program for Happimess trash liners

## Information

- [About Us](https://happimess.com/pages/about-us): Brand story, 30-day product testing methodology, NYC team
- [FAQ](https://happimess.com/pages/faqs): Product selection, shipping, returns, and order support
- [Blog](https://happimess.com/blogs/news): 26+ articles on home organization, trash management, kitchen storage, and sustainable living
- [Meet Our Authors](https://happimess.com/pages/meet-our-authors): Content team credentials and expertise areas
- [Ambassador Program](https://happimess.com/pages/ambassador-program): Partner program details

## Policies

- [Return Policy](https://happimess.com/policies/refund-policy): 30-day returns
- [Privacy Policy](https://happimess.com/policies/privacy-policy)
- [Terms of Service](https://happimess.com/policies/terms-of-service)
- [Shipping Policy](https://happimess.com/policies/shipping-policy)

## AI & Agent Access

- [Agent Instructions](https://happimess.com/agents.md): UCP commerce protocol, Shop skill configuration, read-only catalog endpoints
```

### Fix 2: Organization sameAs — add Wikidata once Q-entity created (theme.liquid)

```json
"sameAs": [
  "https://www.facebook.com/happimessofficial/",
  "https://www.instagram.com/happimess_official/",
  "https://www.linkedin.com/company/happimesshome/",
  "https://www.pinterest.com/happimess_/",
  "https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g",
  "https://www.tiktok.com/@happimess_official",
  "https://www.crunchbase.com/organization/happimess",
  "https://www.wikidata.org/wiki/[REPLACE-WITH-QNUMBER]"
]
```

### Fix 3: Product Vendor field (Shopify Admin — no code change needed)

In Shopify Admin → Products → search each product name → Vendor field: change "Happimess Dev" → "Happimess"

Affected SKU range: HPM10xx products — elmo, beni, chuck, ashley, oscar, molly, nathan.

### Fix 4: Person sameAs for authors (meet-our-authors page template)

```json
{
  "@type": "Person",
  "@id": "https://happimess.com/pages/meet-our-authors#jonathan-yaraghi",
  "name": "Jonathan Yaraghi",
  "jobTitle": "Content Writer and Home Organization Expert",
  "image": { "@type": "ImageObject", "url": "[REPLACE: CDN headshot URL]" },
  "sameAs": ["[REPLACE: Jonathan's LinkedIn URL]"],
  "worksFor": { "@type": "Organization", "@id": "https://happimess.com/#organization" },
  "knowsAbout": ["home organization", "kitchen organization", "trash management", "storage solutions"]
}
```

---

## Appendix — Platform Scores Detail

### Google AI Overviews: 51/100
- Content Structure: 26/40 — FAQ Q&As in HTML; comparison tables present; FAQPage schema restricted for non-authority sites
- Source Authority: 15/30 — Gov citations in 2 posts; no Wikipedia entity; no editorial inbound links
- Technical Signals: 10/30 — FAQPage and BlogPosting JSON-LD confirmed; no HowTo schema

### ChatGPT Web Search: 56/100
- Entity Recognition: 14/35 — No Wikipedia/Wikidata; retail presence (Amazon, Home Depot) provides indirect confirmation
- Content Preferences: 29/40 — Factual blog content; gov citations; agents.md present; missing author credential depth
- Crawler Access: 25/25 — OAI-SearchBot, ChatGPT-User, GPTBot all explicitly allowed

### Perplexity AI: 44/100
- Community Validation: 4/30 — No Reddit, Quora, Trustpilot. Retailer reviews present but not community discussion.
- Source Directness: 17/30 — Gov citations present but unlinked; no original research or proprietary data
- Content Freshness: 16/20 — Publication and update dates visible on articles
- Technical Access: 7/20 — PerplexityBot allowed; no spec-compliant llms.txt

### Google Gemini: 49/100
- Google Ecosystem: 15/35 — No YouTube content; no Google Business Profile confirmed; no Google News
- Knowledge Graph: 10/30 — No Wikipedia; no Knowledge Panel. Google Pay merchant entry confirmed.
- Content Quality: 24/35 — Deep blog articles (1,200–3,000 words); topical clustering around trash/organization

### Bing Copilot: 58/100
- Bing Index Signals: 18/30 — msvalidate.01 confirmed; no IndexNow; sitemap current
- Content Preferences: 23/30 — Professional tone; direct answers; meta descriptions now present
- Microsoft Ecosystem: 5/20 — No active LinkedIn (primary Bing Copilot entity signal); no Microsoft integrations
- Technical Signals: 12/20 — Shopify SSR; clean sitemap; mobile-optimized
