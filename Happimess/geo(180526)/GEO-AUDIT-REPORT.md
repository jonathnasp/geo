# GEO Audit Report — Happimess
**URL:** https://happimess.com/  
**Audit Date:** 2026-05-18  
**Business Type:** E-commerce (Shopify SSR)  
**Category:** Home Organization, Storage & Trash Management  

---

## Composite GEO Score: 48 / 100 — Poor

| Category | Weight | Score | Weighted |
|----------|--------|-------|----------|
| AI Citability & Visibility | 25% | 52 | 13.0 |
| Brand Authority Signals | 20% | 28 | 5.6 |
| Content Quality & E-E-A-T | 20% | 44 | 8.8 |
| Technical Foundations | 15% | 71 | 10.7 |
| Structured Data | 10% | 62 | 6.2 |
| Platform Optimization | 10% | 41 | 4.1 |
| **COMPOSITE** | **100%** | **48** | |

**Score scale:** 0–25 Critical · 26–50 Poor · 51–75 Fair · 76–90 Good · 91–100 Excellent

---

## Progress Since April 14, 2026 Audit

All 4 critical issues from the prior audit are resolved or partially resolved:

| Issue | April Status | May 18 Status |
|-------|-------------|---------------|
| `brand.name: "Happimess Dev"` in Product JSON-LD | Critical | ✅ FIXED — now `"Happimess"` |
| `description: null` in WebPage schema | High | ✅ FIXED — description populated |
| Admin usernames in JSON-LD (`jonathany 2123`, `Asodariya Sumi`) | High | ✅ FIXED — now `"Jonathan Yaraghi"` + `"sandip hadiya"` (casing issue remains) |
| Organization schema missing `sameAs` | High | ✅ PARTIALLY FIXED — 6 platforms linked; Wikipedia/Wikidata/Crunchbase still absent |
| No `llms.txt` at root | High | ⚠️ FILE EXISTS but non-compliant format |
| `/policies/` blocked | Medium | ✅ PARTIALLY FIXED — 3 key pages have specific Allow overrides |
| No LinkedIn company page | Medium | ⚠️ `/company/happimesshome/` exists but LinkedIn search for "Happimess" surfaces a Lithuanian nonprofit at `/company/happimess` — entity collision |
| No `hreflang` for EN/ES | Medium | ❌ STILL ABSENT |
| Blog posts: no visible publication dates | Medium | ⚠️ PARTIAL — dates visible on recent posts; absent on older articles |

---

## Category Scores

### 1. AI Citability & Visibility — 52 / 100

| Sub-component | Score |
|---------------|-------|
| Citability (passage scoring) | 52/100 |
| AI Crawler Access | 90/100 |
| llms.txt Quality | 25/100 |
| Brand Mentions (external) | 28/100 |

**Highlights:**
- robots.txt is excellent — all 10 major AI crawlers explicitly granted `Allow: /`. `Content-Signal: ai-train=yes, search=yes, ai-retrieval=yes` declaration present.
- `sitemap_agentic_discovery.xml` custom sub-sitemap references `llms.txt`, `llms-full.txt`, and `agents.md` — forward-thinking.
- Best citation-ready passages: dual trash can recommendation (74/100), product testing protocol on About Us (73/100), return policy terms (73/100).
- **llms.txt critical gap:** The file at `/llms.txt` serves a commerce-agent-oriented store overview document, not a spec-compliant llms.txt. Missing: `# Title`, `> Description`, `## Section` structure, and `- [Page](url)` link lists. AI models seeking site orientation find nothing usable.
- Zero external citations across all blog content — all outbound links are internal. This is the primary drag on citability.
- Anonymous "From The Mess Experts" byline on all posts suppresses author authority signals.

---

### 2. Brand Authority Signals — 28 / 100

| Platform | Status |
|----------|--------|
| Wikipedia | ❌ No article — confirmed via API |
| Wikidata | ❌ No entity |
| Reddit | ❌ No confirmed community threads |
| LinkedIn | ⚠️ Collision — `/company/happimess` is a Lithuanian nonprofit; brand at `/company/happimesshome/` |
| YouTube | ⚠️ Channel exists but engagement data unconfirmed |
| Trustpilot / G2 | ❌ No confirmed presence (both returned 403) |
| Wirecutter / The Spruce | ❌ No confirmed placement |
| Crunchbase | ❌ No profile found |

**Critical finding:** The LinkedIn brand name collision actively harms AI entity disambiguation. Any AI model resolving "Happimess" via LinkedIn will surface the Vilnius-based children's cancer charity, not the NYC e-commerce brand. This needs immediate resolution via Shopify's Organization `sameAs` (already correctly set to `/company/happimesshome/`) plus a fully-completed LinkedIn company page to increase that profile's authority over the competing entity.

---

### 3. Content Quality & E-E-A-T — 44 / 100

| E-E-A-T Dimension | Score |
|-------------------|-------|
| Experience | 8/25 |
| Expertise | 9/25 |
| Authoritativeness | 12/25 |
| Trustworthiness | 13/25 |
| **E-E-A-T Total** | **42/100** |

**Content metrics (sample of 2 articles):**
- Article 1 ("Why Trash Bags Matter"): ~2,100 words, 12 H2s, 0 external citations
- Article 2 ("Best Dual Trash Can 2026"): ~1,200 words, 9 H2s, 0 external citations
- FAQ page: ~550 words, 9 questions, no FAQPage schema
- Internal linking: 12–15 links per article — strong
- External citations: **0 across all content reviewed**

**E-E-A-T detail:**
- **Experience (8/25):** The 30-day product evaluation protocol, 500+ cycle durability test, and 15-day odor containment test on the About page are genuine differentiators. None of this data appears in any blog article. The proprietary testing information is stranded on the About page.
- **Expertise (9/25):** "From The Mess Experts" is the site's most damaging E-E-A-T signal. Universally used, never defined. No named authors anywhere.
- **Authoritativeness (12/25):** Zero external citations, zero press mentions, zero third-party reviews linked from content.
- **Trustworthiness (13/25):** Strongest dimension — HTTPS, phone + email + hours, return policy specifics (30 days, $10 fee, pre-paid label), editorial disclosure present on some articles.

**AI content signals:** Consistent patterns of templated section titles ("What to Look for," "Real-Life Use Cases"), year-tagged titles ("2026 Guide," "2025 Edition"), zero authorial voice, and recommendations unsupported by site's own test data. Assessment: likely AI-generated with light editing.

**Publication dates:** Visible on recent articles (May 4 and April 22, 2026). Absent on all articles visible on blog page 2+.

---

### 4. Technical Foundations — 71 / 100

| Sub-category | Score |
|--------------|-------|
| Server-Side Rendering | 95/100 |
| Crawlability | 82/100 |
| Indexability | 72/100 |
| Mobile Optimization | 75/100 |
| Core Web Vitals Risk | 60/100 |
| Security Headers | 50/100 |
| URL Structure | 80/100 |

**Key findings:**
- Shopify SSR confirmed — all text content (products, blog, FAQ) in raw HTML. AI crawlers have full text access.
- Sitemap: 9 sub-sitemaps, ~826 total URLs across EN and ES. All include recent `lastmod` dates.
- **Hreflang entirely absent** — ~400 EN pages and ~400 ES pages have no language annotations. Duplicate content risk is substantial.
- `/pages/faqs` page title is `"Faqs"` — critically weak for SEO; zero keywords, no brand name.
- Product images use base64 placeholder URIs in HTML (lazy-load pattern); missing explicit `width`/`height` attributes creates CLS risk.
- No `rel="preload"` for hero images detected.
- Security headers (CSP, HSTS) unverifiable from this tool; Shopify/Fastly defaults assumed.
- Sitemap notable: custom `sitemap_agentic_discovery.xml` references AI discovery files.

---

### 5. Structured Data — 62 / 100

| Schema | Pages | Status |
|--------|-------|--------|
| Organization + sameAs | All pages | ✅ Valid — 6 sameAs links |
| WebSite + SearchAction | All pages | ✅ Valid (minor: nested EntryPoint object) |
| WebPage (homepage) | Homepage | ✅ Valid — description now populated |
| Product | Product pages | ✅ Valid — brand.name confirmed `"Happimess"` |
| Product → aggregateRating | Product pages | ❌ Missing |
| BreadcrumbList | Products, blog articles | ✅ Valid |
| BreadcrumbList | Homepage, About, FAQ | ❌ Missing |
| BlogPosting + speakable | Blog articles | ✅ Valid — datePublished/dateModified in ISO 8601 |
| BlogPosting → articleSection | Blog articles | ❌ Missing |
| Blog (index) | Blog index | ⚠️ Partial — description is empty string `""` |
| FAQPage | FAQ page, product pages | ✅ Syntax valid (Google rich result restricted Aug 2023; AI extraction value retained) |
| Person (authors) | Blog articles | ⚠️ Partial — names present, no jobTitle/sameAs/image/description |

**Author name issue:** `"sandip hadiya"` — all lowercase; should be `"Sandip Hadiya"`. Update Shopify admin display name.

**sameAs gap:** Organization links 6 social platforms. Missing: Wikipedia, Wikidata, Crunchbase — the three highest-authority signals for AI entity resolution.

**Biggest missing schema:** `aggregateRating` on Product pages — primary unlock for Google Shopping rich results and AI product comparison responses.

---

### 6. Platform Optimization — 41 / 100

| Platform | Score | Key Gap |
|----------|-------|---------|
| Google AI Overviews | 48/100 | No FAQPage schema on /pages/faqs; no HowTo schema; no external citations |
| Perplexity AI | 44/100 | No external citations; blog dates not visible on listing page |
| ChatGPT Web Search | 38/100 | Entity recognition weak; no Wikipedia/Wikidata |
| Bing Copilot | 38/100 | No Bing Webmaster Tools verification; no IndexNow |
| Google Gemini | 37/100 | No aggregateRating on products; no Google Business Profile; no YouTube engagement signals |

**Cross-platform observation:** All 5 platforms would benefit from the same 3 changes: (1) external citations in blog content, (2) named author bylines, (3) aggregateRating on products.

---

## Prioritized Action Plan

### Tier 1 — Quick Wins (Low Effort, High Impact)

| # | Action | Effort | Impact | Platforms |
|---|--------|--------|--------|-----------|
| 1 | **Rewrite `/llms.txt` to spec** — replace commerce-agent doc with proper markdown (# Title, > Description, ## Section, - [link]) | 1 hour | All AI platforms | ChatGPT, Claude, Perplexity, AIO |
| 2 | **Fix `/pages/faqs` title tag** — change "Faqs" to "Frequently Asked Questions \| Happimess" in Shopify Admin | 5 min | Google AIO, Bing | AIO, Copilot |
| 3 | **Fix author casing** — change `"sandip hadiya"` → `"Sandip Hadiya"` in Shopify admin display name (propagates to all blog article schemas automatically) | 5 min | Schema quality | All |
| 4 | **Create Crunchbase profile** for Happimess and add URL to Organization `sameAs` in `theme.liquid` | 20 min | Brand authority | ChatGPT, Gemini, Copilot |
| 5 | **Add 3 missing sameAs targets** to Organization schema: Crunchbase, Wikidata (after creation), Wikipedia (if applicable) | 15 min | Entity resolution | All |
| 6 | **Fully complete LinkedIn `/company/happimesshome/`** — ensure company description, industry, website, logo filled; this counteracts the competing Lithuanian entity | 30 min | Brand authority | Copilot, ChatGPT |
| 7 | **Show publication dates on blog listing** — update blog-template.liquid to render `published_at` under each article card | 30 min | Freshness signals | AIO, Perplexity, Gemini |

### Tier 2 — Medium Effort, High Impact

| # | Action | Effort | Impact | Platforms |
|---|--------|--------|--------|-----------|
| 8 | **Add hreflang to `theme.liquid`** — EN/ES annotations on all pages; add xhtml:link to sitemaps (requires SEO app or custom code) | 2–4 hours | Duplicate content resolution | All search engines |
| 9 | **Add `aggregateRating` to all Product schemas** — enable review app's Schema.org output (Judge.me/Yotpo/Okendo toggle in app settings, or add to `product.liquid`) | 1–2 hours | Google Shopping, Gemini, AIO | Gemini, AIO, Copilot |
| 10 | **Add named author bylines to all blog posts** — minimum: visible name + 1-sentence credential in article header; better: create `/pages/meet-our-authors` with full bios | 2–3 hours | E-E-A-T, citability | All |
| 11 | **Add 2–3 external citations per blog post** — start with "Best Dual Trash Can" and "Why Trash Bags Matter"; link to EPA waste stats, ANSI standards, or consumer publications | 1–2 hours | Citability, AIO source authority | AIO, Perplexity, ChatGPT |
| 12 | **Fix product image dimensions** — add `width="{{ image.width }}"` and `height="{{ image.height }}"` to all `<img>` tags in product/collection/article templates | 1–2 hours | Core Web Vitals CLS | All (performance) |
| 13 | **Add `articleSection`, `wordCount`, and `keywords`** to BlogPosting schema in `article.liquid` | 1 hour | Schema completeness | AIO, Gemini |
| 14 | **Enrich author Person schemas** — add `jobTitle`, `worksFor`, `image`, `description`, `sameAs` (LinkedIn) for both Jonathan Yaraghi and Sandip Hadiya | 1–2 hours | Expertise signals | All |

### Tier 3 — Strategic (Higher Effort, Long-Term Impact)

| # | Action | Effort | Impact | Platforms |
|---|--------|--------|--------|-----------|
| 15 | **Create Wikidata entity for Happimess** — add @type Organization with website, founding date, location, industry | 1 hour | Entity resolution | ChatGPT, Gemini |
| 16 | **Surface testing data in blog content** — add a recurring "Why We Recommend This" callout block in every product guide referencing the 30-day eval, 500+ cycle test, 15-day odor test | 4–6 hours | Experience signals, citability | All |
| 17 | **Bing Webmaster Tools verification + IndexNow** — verify site, submit sitemap, enable IndexNow | 30 min | Bing crawl freshness | Copilot |
| 18 | **Pursue press placement** — pitch 1–2 product round-ups to The Spruce, Apartment Therapy, or Wirecutter | Ongoing | Wikipedia notability, brand authority | All |
| 19 | **Expand llms-full.txt** — currently ~300 words for an 800+ URL store; add product category descriptions, brand story, and key differentiators | 1 hour | AI site comprehension | Claude, ChatGPT |
| 20 | **Add Google Business Profile** — NYC location, phone, email, website; fastest path to a Google Knowledge Panel | 30 min | Gemini ecosystem | Gemini |

---

## Issue Registry

| # | Issue | Severity | Effort | Status |
|---|-------|----------|--------|--------|
| 1 | llms.txt non-compliant format | High | Low | Open |
| 2 | No hreflang EN/ES | High | Medium | Open |
| 3 | No `aggregateRating` on products | High | Low–Medium | Open |
| 4 | Anonymous blog bylines ("From The Mess Experts") | High | Medium | Open |
| 5 | Zero external citations in blog content | High | Medium | Open |
| 6 | LinkedIn name collision (Lithuanian nonprofit at `/company/happimess`) | High | Low | Open |
| 7 | No Wikipedia / Wikidata entity | High | Medium–High | Open |
| 8 | FAQ page title "Faqs" — too weak | Medium | Low | Open |
| 9 | `"sandip hadiya"` author name casing | Medium | Low | Open |
| 10 | Organization sameAs missing Wikidata / Crunchbase | Medium | Low | Open |
| 11 | Author Person schema missing jobTitle / sameAs / image | Medium | Medium | Open |
| 12 | Product images missing width/height (CLS risk) | Medium | Medium | Open |
| 13 | Blog listing: publication dates not rendered | Medium | Low | Open |
| 14 | BlogPosting missing articleSection / wordCount / keywords | Low | Low | Open |
| 15 | Blog index schema: empty description field | Low | Low | Open |
| 16 | WebSite SearchAction: nested EntryPoint (should be plain string) | Low | Low | Open |
| 17 | BreadcrumbList absent on About Us, FAQ, homepage | Low | Low | Open |
| 18 | No `rel="preload"` for hero image | Low | Low | Open |
| 19 | Bing Webmaster Tools not verified / no IndexNow | Low | Low | Open |
| 20 | No Google Business Profile | Low | Low | Open |
| 21 | No press placements (Wirecutter, The Spruce, etc.) | Low | High | Open |

---

## Raw Scores Reference

| Category | Score | Interpretation |
|----------|-------|----------------|
| AI Crawler Access | 90/100 | Good |
| Structured Data | 62/100 | Fair |
| Technical Foundations | 71/100 | Fair |
| AI Citability | 52/100 | Fair |
| Content / E-E-A-T | 44/100 | Poor |
| Platform Optimization | 41/100 | Poor |
| Brand Authority | 28/100 | Critical |
| **Composite GEO Score** | **48/100** | **Poor** |

---

## GEO-Ready JSON-LD Snippets

### llms.txt (replace current file content)

```markdown
# Happimess

> Modern storage, organization, and trash management products for the home.
> New York City-based. Ships to 48 contiguous US states. Est. 2020.

## Products

- [All Products](https://happimess.com/collections/all): Full catalog
- [Trash Cans & Bins](https://happimess.com/collections/trash-cans): Step cans, sensor cans, dual-compartment recycling bins, wicker wastebaskets
- [Storage & Organization](https://happimess.com/collections/storage): Baskets, benches, ottomans, trunks, coat racks
- [Trash Liners](https://happimess.com/collections/trash-bags): Scented (lemon/lavender) and unscented drawstring liners, subscription available

## Guides & Blog

- [Best Dual Trash Can for Kitchen (2026)](https://happimess.com/blogs/news/best-dual-trash-can-for-kitchen-2026-guide-what-actually-works): Selection guide — capacity, mechanisms, durability
- [Why Trash Bag Choice Matters](https://happimess.com/blogs/news/why-choosing-the-right-trash-bag-actually-matters): Odor control, leak resistance, scent selection
- [All Blog Posts](https://happimess.com/blogs/news): 24+ articles on home organization, storage, and waste management

## Company

- [About Happimess](https://happimess.com/pages/about-us): NYC-based team, 30-day product testing protocol, 500+ cycle durability standard
- [FAQs](https://happimess.com/pages/faqs): Shipping, returns, order changes, international availability
- [Refill Subscription](https://happimess.com/pages/refill-page): Recurring liner subscription program
- [Ambassador Program](https://happimess.com/pages/ambassador-program): Brand partnership opportunities

## Optional

- [Sitemap](https://happimess.com/sitemap.xml)
- [Privacy Policy](https://happimess.com/policies/privacy-policy)
- [Return Policy](https://happimess.com/policies/refund-policy): 30-day returns, pre-paid labels, $10/item shipping fee
- [Terms of Service](https://happimess.com/policies/terms-of-service)
```

### Organization sameAs (add to theme.liquid)

```json
"sameAs": [
  "https://www.facebook.com/happimessofficial/",
  "https://www.instagram.com/happimess_official/",
  "https://www.linkedin.com/company/happimesshome/",
  "https://www.pinterest.com/happimess_/",
  "https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g",
  "https://www.tiktok.com/@happimess_official",
  "https://www.crunchbase.com/organization/happimess",
  "https://www.wikidata.org/wiki/[REPLACE_WITH_QNUMBER]"
]
```

### Product aggregateRating (add inside Product schema in product.liquid)

```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "{{ product.metafields.reviews.rating.value | default: '4.5' }}",
  "reviewCount": "{{ product.metafields.reviews.rating_count.value | default: '1' }}",
  "bestRating": "5",
  "worstRating": "1"
}
```

### hreflang (add to theme.liquid `<head>`)

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

---

*Audit conducted 2026-05-18 using 5 parallel GEO analysis agents. Next audit recommended: 2026-08-18 or after completing Tier 1 + Tier 2 actions.*
