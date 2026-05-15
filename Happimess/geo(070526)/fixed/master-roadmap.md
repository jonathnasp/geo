# Happimess GEO Implementation Master Roadmap
**Baseline Audit:** May 7, 2026 | **Current Score:** 42/100 | **90-Day Target:** 68/100

---

## At a Glance

| Sprint | Timeline | Score Impact | Focus |
|--------|----------|-------------|-------|
| Sprint 1 — Critical Fixes | Days 1–5 | 42 → ~68 | Broken infrastructure, schema, content surgery |
| Sprint 2 — Authority Building | Weeks 2–4 | 68 → ~72 | External citations, reviews, research |
| Sprint 3 — Press & Entity | Month 2 | 72 → ~76 | Editorial mentions, Trustpilot, YouTube |
| Sprint 4 — Wikipedia | Month 3 | 76 → ~80+ | Wikipedia notability, Wikidata entry |

---

## Complete Issue Registry

### CRITICAL Priority (Fix Day 1–2)

| ID | Issue | Effort | SEO Impact | GEO Impact | AI Impact | Status |
|----|-------|--------|-----------|-----------|---------|--------|
| C-01 | Author bio page `/pages/asodariya-sumi` returns 404 | 30 min | Critical | Critical | Critical | ☐ |
| C-02 | FAQ page `/pages/faq` returns 404 (linked from every footer) | 15 min | High | High | Medium | ☐ |
| C-03 | `@type: LocalBusiness` instead of `Organization` in global schema | 30 min | Critical | Critical | Critical | ☐ |
| C-04 | 5 additional schema validation errors in global block (telephone space, servesCuisine, contactType, AggregateRating strings) | 15 min | High | High | High | ☐ |
| C-05 | llms.txt lists 0 of 26 blog posts | 45 min | Medium | Critical | Critical | ☐ |
| C-06 | Organization/WebSite schema JS-injected (invisible to AI crawlers) | 30 min | High | Critical | Critical | ☐ |

---

### HIGH Priority (Fix Day 2–3)

| ID | Issue | Effort | SEO Impact | GEO Impact | AI Impact | Status |
|----|-------|--------|-----------|-----------|---------|--------|
| H-01 | No AI crawler explicit Allow directives in robots.txt | 15 min | Medium | High | High | ☐ |
| H-02 | Invalid regex Disallow rule in robots.txt | 5 min | Low | Low | Low | ☐ |
| H-03 | `/policies/` blocked in robots.txt (blocks E-E-A-T trust pages) | 5 min | Medium | Medium | Medium | ☐ |
| H-04 | No LinkedIn company page (Lithuanian nonprofit namespace collision) | 60 min | High | High | High | ☐ |
| H-05 | No IndexNow — Bing index staleness risk | 45 min | Medium | Medium | High | ☐ |
| H-06 | Product schema: `@context` trailing slash + relative `url` | 20 min | High | Medium | Medium | ☐ |
| H-07 | No AggregateRating on any product (blocks star ratings) | 60 min | Critical | Medium | Medium | ☐ |
| H-08 | Collection pages have zero schema (CollectionPage/ItemList absent) | 30 min | High | High | High | ☐ |
| H-09 | Article schema author URL 404 (fixed by C-01, but schema template must also be updated) | 30 min | High | High | High | ☐ |
| H-10 | `speakable` property missing from Article schema | 20 min | Low | High | Critical | ☐ |
| H-11 | FAQPage JSON-LD missing from 8+ posts that already have FAQ content | 2 hrs | High | High | High | ☐ |
| H-12 | Pinterest sameAs uses short URL `pin.it` instead of canonical | 5 min | Low | Medium | Medium | ☐ |

---

### HIGH Priority — Content (Fix Day 4)

| ID | Issue | Effort | SEO Impact | GEO Impact | AI Impact | Status |
|----|-------|--------|-----------|-----------|---------|--------|
| CT-01 | Buying guide at 650 words (critically thin for commercial-intent query) | 4 hrs | Critical | High | High | ☐ |
| CT-02 | Off-topic H3 headings in buying guide (wipes products in trash can guide) | 30 min | High | High | Medium | ☐ |
| CT-03 | All H2 headings in dual-can guide contain emoji (10 of 10) | 20 min | Medium | High | High | ☐ |
| CT-04 | No FTC disclosure on commercial blog posts (5 posts) | 30 min | High | High | Medium | ☐ |
| CT-05 | Blog posts open with context-setting intro (not answer-first) | 2 hrs | High | Critical | Critical | ☐ |
| CT-06 | All 26 posts attributed to "From The Mess Experts" (no named author) | 1 hr | High | High | High | ☐ |
| CT-07 | About page is 200 words with no founders, no team, no methodology | 1 hr | Medium | High | Medium | ☐ |

---

### MEDIUM Priority (Fix Day 5 + Week 2)

| ID | Issue | Effort | SEO Impact | GEO Impact | AI Impact | Status |
|----|-------|--------|-----------|-----------|---------|--------|
| M-01 | Image lazy-load CLS risk on all pages (placeholder allocates 0px height) | 2 hrs | High | Medium | Low | ☐ |
| M-02 | Homepage H1 is "Happimess" (zero topical keyword signal) | 15 min | High | High | High | ☐ |
| M-03 | Hreflang implementation unconfirmed on bilingual EN/ES site | 30 min | Critical | Medium | Medium | ☐ |
| M-04 | Product URL compound slug typo: `stainless-steelblack` | 10 min | Low | Low | Low | ☐ |
| M-05 | "Related aticles" typo on buying guide page | 5 min | Low | Low | Low | ☐ |
| M-06 | Zero external citations in any blog post | 2 hrs | High | Critical | Critical | ☐ |
| M-07 | BreadcrumbList on product pages uses HTTP not HTTPS | 10 min | Medium | Low | Low | ☐ |
| M-08 | `Article.description` duplicates headline (should be unique summary) | 30 min | Low | Low | Medium | ☐ |
| M-09 | Blog images missing alt text | 2 hrs | Medium | Low | Low | ☐ |
| M-10 | `sameAs` missing: Wikipedia, Wikidata, Crunchbase | Months | Critical | Critical | Critical | ☐ |
| M-11 | `AggregateRating` values as strings not numbers in Organization schema | 5 min | Low | Low | Low | ☐ |

---

### LOW Priority (Month 1–3)

| ID | Issue | Effort | SEO Impact | GEO Impact | AI Impact | Status |
|----|-------|--------|-----------|-----------|---------|--------|
| L-01 | No Trustpilot business profile | 2 hrs + ongoing | High | High | High | ☐ |
| L-02 | No YouTube channel with product demos | 4 hrs + ongoing | Medium | High | High | ☐ |
| L-03 | No original research/proprietary data anywhere | 2–3 weeks | Critical | Critical | Critical | ☐ |
| L-04 | Wikipedia article doesn't exist (needs press mentions first) | 3–6 months | Critical | Critical | Critical | ☐ |
| L-05 | No Wikidata entity (easier than Wikipedia, immediate AI signal) | 2 hrs | High | Critical | Critical | ☐ |
| L-06 | No press mentions or "as seen in" media | 2–3 months | High | High | High | ☐ |
| L-07 | Security headers (CSP, Permissions-Policy) absent | Complex | Low | Low | Low | ☐ |
| L-08 | `fetchpriority="high"` missing on LCP images | 30 min | Medium | Low | Low | ☐ |
| L-09 | No `Content-Signal` header in robots.txt | 5 min | Low | Medium | Medium | ☐ |
| L-10 | Evergreen blog posts not refreshed with updated dates | Ongoing | Medium | Medium | Medium | ☐ |

---

## 90-Day Implementation Timeline

### Sprint 1: Days 1–5 (Critical Infrastructure)
**Goal:** Fix all broken pages, deploy all schema, clean all content errors

```
Day 1 (3.5 hrs) — BROKEN INFRASTRUCTURE
  C-01: Create /pages/asodariya-sumi author page
  C-02: Create /pages/faq page (or redirect)
  C-03: Replace LocalBusiness with Organization schema
  C-04: Fix 5 schema validation errors
  C-05: Deploy improved llms.txt with blog section

Day 2 (3.5 hrs) — TECHNICAL + PLATFORM
  H-01: Add AI crawler Allow directives to robots.txt
  H-02: Remove invalid regex Disallow rule
  H-03: Allow /policies/privacy-policy and /refund-policy
  C-06: Move Organization/WebSite schema from JS to server-rendered
  H-04: Create LinkedIn company page
  H-05: Implement IndexNow + Bing Webmaster Tools

Day 3 (4 hrs) — SCHEMA DEPLOYMENT
  H-06: Deploy schema-product.liquid (absolute URL, @context fix, AggregateRating)
  H-07: Install reviews app, configure metafields
  H-08: Deploy schema-collection.liquid (CollectionPage + ItemList)
  H-09: Deploy schema-article.liquid (fixes author URL, adds speakable)
  H-10: Confirm speakable CSS selectors
  H-11: Add FAQPage JSON-LD to 4 key blog posts

Day 4 (6–8 hrs) — CONTENT SURGERY
  CT-01: Rebuild buying guide (650 → 2,000+ words)
  CT-02: Remove off-topic wipes H3s from buying guide
  CT-03: Remove emojis from all H2s in dual-can guide
  CT-04: Add FTC disclosures to 5 commercial posts
  CT-05: Rewrite openings of 3 key posts (answer-first)
  CT-06: Update all 26 post author fields to "Asodariya Sumi"
  CT-07: Expand About page to 400+ words with methodology

Day 5 (4–5 hrs) — TECHNICAL CLEANUP
  M-01: Fix image CLS (aspect-ratio CSS)
  M-02: Change homepage H1 to keyword text
  M-03: Verify hreflang (check Search Console, fix if needed)
  M-04: Fix product URL slug typo (new products going forward)
  M-05: Fix "Related aticles" typo
  M-06: Add external citations to size guide and buying guide
```

---

### Sprint 2: Week 2 (Content Authority)

| Task | Effort | Impact |
|------|--------|--------|
| Add external citations to all key blog posts (NKBA, manufacturer data, consumer research) | 2–3 hrs | High |
| Add `gtin`/`mpn` to Product schema for Google Shopping identity | 1 hr | Medium |
| Add `color`, `material`, `additionalProperty` to Product schema for AI comparison queries | 2 hrs | Medium |
| Fix BreadcrumbList HTTP → HTTPS on product pages | 30 min | Low |
| Update `Article.description` to unique summaries (not duplicate headlines) | 1 hr | Low |
| Add alt text to all blog post images | 2 hrs | Medium |
| Add `ItemList` schema to blog listing page (`/blogs/news/`) | 30 min | Medium |

---

### Sprint 3: Month 1–2 (External Authority)

| Task | Effort | Impact |
|------|--------|--------|
| Claim Trustpilot business profile + collect 25+ reviews | 2 hrs setup + ongoing | High |
| Create YouTube channel with 5 product/tutorial videos | 4 hrs setup + filming | High |
| Commission customer survey (100+ responses) + publish original research | 2–3 weeks | Critical |
| Pitch survey findings to Apartment Therapy, The Spruce, Real Simple | Ongoing | Critical |
| Create Wikidata entity for Happimess | 2 hrs | High |
| Complete LinkedIn company page (team, posts, descriptions) | 2 hrs | Medium |

---

### Sprint 4: Month 3 (Wikipedia Notability)

| Task | Dependency | Impact |
|------|-----------|--------|
| Confirm 2–3 reliable third-party sources about Happimess | Press mentions from Sprint 3 | Critical |
| Submit Wikipedia article | Third-party sources required | Critical |
| Add Wikipedia + Wikidata URLs to Organization `sameAs` | Wikipedia article exists | Critical |
| Update Crunchbase listing | Can do now | High |

---

## Business Impact by Issue Category

| Category | Issues Fixed | Revenue Impact | Brand Impact |
|----------|-------------|---------------|-------------|
| Broken 404 pages (C-01, C-02) | 2 issues | Medium — reduces bounce/abandon | High — brand credibility |
| Schema errors (C-03, C-04, H-06, H-07) | 6 issues | High — star ratings drive CTR | High — Knowledge Panel eligibility |
| AI crawler access (C-06, H-01) | 2 issues | Medium — long-term organic | Critical — all AI platforms |
| llms.txt (C-05) | 1 issue | Medium — AI discovery | Critical — ChatGPT/Perplexity citation |
| Content quality (CT-01 to CT-07) | 7 issues | High — commercial intent pages | High — E-E-A-T |
| External authority (L-01 to L-06) | 6 issues | Low-medium (long-term) | Critical — AI entity recognition |

---

## Score Projection by Sprint

```
Sprint 1 (Day 1–5)   ████████████████████░░░  68/100  → Target achieved
Sprint 2 (Week 2)    █████████████████████░░  72/100
Sprint 3 (Month 1-2) ██████████████████████░  76/100
Sprint 4 (Month 3)   ███████████████████████  80/100

Baseline:            ████████░░░░░░░░░░░░░░░  42/100
```

---

## Dependencies Map

```
C-01 (author page) ──────────────┐
                                 ├─► H-09 (Article schema author URL)
                                 └─► CT-06 (author attribution site-wide)

C-03 (Organization schema) ──────┐
                                 ├─► C-06 (server-rendered schema)
                                 └─► H-12 (sameAs Pinterest fix)

H-04 (LinkedIn page) ──────────► C-03 (update LinkedIn URL in sameAs)

L-01 (Trustpilot) ─────────────► L-04 (Wikipedia notability requirement #1)
L-03 (Original research) ──────► L-06 (press mentions — using research as hook)
L-06 (Press mentions) ─────────► L-04 (Wikipedia notability requirement #2)
```

---

## Validation Schedule

| Checkpoint | When | Tool |
|------------|------|------|
| Organization schema clean | After Day 1 | Google Rich Results Test |
| Author page live | After Day 1 | curl / browser |
| FAQ page live | After Day 1 | Browser |
| AI crawlers in robots.txt | After Day 2 | View source |
| Schema server-rendered | After Day 2 | View page source (Ctrl+U) |
| Product schema valid | After Day 3 | Google Rich Results Test |
| Collection schema valid | After Day 3 | Google Rich Results Test |
| Article schema + speakable | After Day 3 | Google Rich Results Test |
| Buying guide 2,000+ words | After Day 4 | Word count check |
| CLS improved | After Day 5 | PageSpeed Insights |
| Hreflang confirmed | After Day 5 | Google Search Console |
| Full 5-day score validation | End of Week 1 | Re-run GEO audit |

---

*Master Roadmap — Happimess GEO Implementation | May 2026*
*Reference: GEO-AUDIT-REPORT.md (baseline audit May 7, 2026)*
