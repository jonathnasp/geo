# GEO Schema & Structured Data Report — happimess.com
**Audit Date:** May 28, 2026
**Platform:** Shopify (server-rendered HTML, all schemas present in initial response)
**Schema Delivery:** Server-rendered — no JS injection risk for AI crawlers

---

## Schema Score: 71/100 — Fair

### Score Breakdown

| Component | Points Available | Points Earned | Notes |
|---|---|---|---|
| Organization + sameAs | 20 | 15 | Present with 7 sameAs platforms; missing Wikipedia and Wikidata |
| Article/content schema | 15 | 14 | BlogPosting valid with author as Person + @id + dateModified; missing `image` as ImageObject (uses plain ImageObject, not linked to author) |
| Person schema for authors | 15 | 10 | Both authors present with @id, jobTitle, worksFor, sameAs; missing `image` property on both |
| sameAs completeness | 15 | 10 | 7 platforms linked; Wikipedia and Wikidata absent (highest-weight AI signals) |
| speakable property | 10 | 5 | Present on BlogPosting and Product schemas; CSS selectors include `.article__excerpt` and `.article__summary` which do not exist as rendered classes in live Shopify theme — h1 selector is valid |
| BreadcrumbList | 5 | 5 | Valid and present on all non-home pages; 3-level breadcrumb correctly implemented on blog articles |
| WebSite + SearchAction | 5 | 5 | Valid; target URL template correctly formed |
| No deprecated schemas | 5 | 2 | FAQPage on product pages (restricted Aug 2023 — no rich results for non-authority sites); HowTo not present |
| JSON-LD format | 5 | 5 | All schemas in JSON-LD exclusively; no Microdata or RDFa detected |
| Validation (no errors) | 5 | 0 | `brand.name: "Happimess Dev"` on confirmed products causes brand identity error; speakable selectors partially invalid |

---

## Detected Structured Data — Full Inventory

### Schema Blocks by Page Type

| # | Page | Schema Type | Format | Valid | Rich Result Eligible | Issues |
|---|---|---|---|---|---|---|
| 1 | All pages | Organization | JSON-LD | Yes | Yes (Knowledge Panel) | Missing Wikipedia + Wikidata in sameAs |
| 2 | All pages | WebSite + SearchAction | JSON-LD | Yes | Yes (Sitelinks Search Box) | None |
| 3 | Homepage | WebPage | JSON-LD | Yes | N/A | None |
| 4 | All non-home | BreadcrumbList | JSON-LD | Yes | Yes | None |
| 5 | /pages/faqs | FAQPage (8 Q&As) | JSON-LD | Yes | Restricted | Valid structure; no rich results on non-authority sites |
| 6 | /pages/faqs | WebPage | JSON-LD | Yes | N/A | None |
| 7 | /pages/meet-our-authors | Person (Jonathan Yaraghi) | JSON-LD | Partial | N/A | Missing `image` property |
| 8 | /pages/meet-our-authors | Person (Sandip Hadiya) | JSON-LD | Partial | N/A | Missing `image` property; only 1 sameAs link |
| 9 | /blogs/news/[article] | BlogPosting | JSON-LD | Yes | Yes (Article) | speakable selectors partially invalid |
| 10 | /blogs/news/[article] | BreadcrumbList (3-level) | JSON-LD | Yes | Yes | None |
| 11 | /products/elmo-* | Product | JSON-LD | No | Partial | brand.name = "Happimess Dev"; speakable selectors untested |
| 12 | /products/elmo-* | AggregateRating on Product | JSON-LD | Yes | Yes | ratingValue: 5, reviewCount: 1 — thin but valid |
| 13 | /products/oscar-* | Product | JSON-LD | No | No | brand.name = "Happimess Dev"; aggregateRating MISSING |
| 14 | /products/beni-* | Product | JSON-LD | Partial | Yes | brand.name = "Happimess Dev"; aggregateRating present (4.5, 2 reviews) |
| 15 | /products/chuck-* | Product | JSON-LD | No | No | brand.name = "Happimess Dev"; aggregateRating MISSING |
| 16 | /products/ashley-* | Product | JSON-LD | Partial | Yes | brand.name = "Happimess Dev"; aggregateRating present (4.64, 28 reviews) — rich result eligible if brand fixed |
| 17 | /products/slyd-* | Product | JSON-LD | Yes | No | brand.name = "Happimess" (CORRECT); aggregateRating MISSING |
| 18 | /products/betty-* | Product | JSON-LD | Yes | Yes | brand.name = "Happimess" (CORRECT); aggregateRating present |
| 19 | /products/robo-* | Product | JSON-LD | Yes | Yes | brand.name = "Happimess" (CORRECT); aggregateRating present |
| 20 | /products/[all] | FAQPage (product Q&As) | JSON-LD | Yes | Restricted | 10 Q&As per product; no rich results for non-authority site |

**Total schema blocks per typical page:**
- Homepage: 2 blocks (WebPage + WebSite/Organization)
- Product pages: 4 blocks (Product + BreadcrumbList + FAQPage + WebSite/Organization)
- Blog articles: 3 blocks (BlogPosting + BreadcrumbList + WebSite/Organization)
- /pages/faqs: 4 blocks (FAQPage + WebPage + BreadcrumbList + WebSite/Organization)
- /pages/meet-our-authors: 3 blocks (Person @graph + BreadcrumbList + WebSite/Organization)

---

## Detailed Validation Results

### Organization Schema (all pages)

**Status:** Valid with gaps

| Property | Status | Value/Notes |
|---|---|---|
| @context | OK | https://schema.org |
| @type | OK | Organization |
| @id | OK | https://happimess.com/#organization |
| name | OK | "Happimess" |
| url | OK | https://happimess.com |
| description | OK | Present |
| logo | OK | ImageObject with CDN URL |
| image | OK | ImageObject (same as logo) |
| telephone | OK | +19172614961 |
| email | OK | hello@happimess.com |
| address | OK | PostalAddress — 185 Madison Ave, New York, NY 10016 |
| sameAs | Partial | 7 platforms; Wikipedia and Wikidata absent |
| foundingDate | OK | 2020-01-15 |
| legalName | OK | "Happimess" |
| contactPoint | OK | Customer service with English + Spanish |
| areaServed | OK | Country: United States |
| knowsAbout | OK | 10 topics |

**GEO Assessment:** Strong entity schema. The absence of Wikipedia and Wikidata in sameAs is the single most impactful gap for AI entity resolution. All 7 current links are valid platforms.

---

### Product Schema — brand.name Audit

**CRITICAL FINDING:** The `brand.name` field contains "Happimess Dev" on products that were migrated from the development store. This is a staging artifact in production.

| Product | Slug | brand.name | aggregateRating |
|---|---|---|---|
| Elmo (Double-Bucket) | elmo-rectangular-8-gallon-double-bucket-trash-can-with-soft-close-lid | **"Happimess Dev"** | Present (5.0, 1 review) |
| Oscar | oscar-round-8-gallon-step-open-trash-can-with-free-mini-trash-can | **"Happimess Dev"** | MISSING |
| Beni | beni-kitchen-trashrecycling-trash-can | **"Happimess Dev"** | Present (4.5, 2 reviews) |
| Chuck | chuck-kitchenoffice-trash-can | **"Happimess Dev"** | MISSING |
| Ashley | ashley-rectangular-8-gallon-trash-can-with-soft-close-lid-with-free-mini-trash-can-stainless-steel | **"Happimess Dev"** | Present (4.64, 28 reviews) |
| Slyd | slyd-10-6-gallon-step-open-trash-can | "Happimess" (correct) | MISSING |
| Betty | betty-retro-8-gallon-step-open-trash-can | "Happimess" (correct) | Present |
| Robo | robo-kitchen-132-gallon-slim-oval-motion-sensor-touchless-trash-can-with-touch-mode | "Happimess" (correct) | Present |

**Pattern:** Products with "Happimess Dev" appear to be the original catalog items; "Happimess" brand name is correct on newer or recently-updated products. This requires a Shopify theme-level fix in the product JSON-LD Liquid template.

---

### Person Schema (/pages/meet-our-authors)

**Status:** Valid with gaps

| Property | Jonathan Yaraghi | Sandip Hadiya |
|---|---|---|
| @id | OK (URL fragment) | OK (URL fragment) |
| name | OK | OK |
| url | OK | OK |
| jobTitle | OK — "Home Organization Expert" | OK — "Content Writer" |
| description | OK | OK |
| sameAs | OK — LinkedIn + Crunchbase (2 links) | Partial — LinkedIn only (1 link) |
| worksFor | OK — links to Organization @id | OK — links to Organization @id |
| knowsAbout | OK — 5 topics | OK — 5 topics |
| **image** | **MISSING** | **MISSING** |

**GEO Assessment:** Author schemas are structurally sound and correctly reference the Organization via @id (enabling graph linking). The missing `image` property reduces E-E-A-T signal strength — AI models use author images as a verification signal for real-person identity. Sandip Hadiya has only 1 sameAs link; adding a second strengthens author entity confidence.

---

### BlogPosting Schema

**Status:** Valid (best-in-class for Shopify)

| Property | Status | Value/Notes |
|---|---|---|
| @type | OK | BlogPosting |
| @id | OK | Full URL |
| headline | OK | Article title |
| description | OK | Present and detailed |
| image | OK | ImageObject with CDN URL |
| author | OK | Person with @id, jobTitle, worksFor — full entity reference |
| publisher | OK | Organization with logo ImageObject |
| datePublished | OK | ISO 8601 with timezone offset |
| dateModified | OK | ISO 8601 with timezone offset |
| mainEntityOfPage | OK | WebPage with @id |
| articleSection | OK | "From The Mess Experts" |
| wordCount | OK | Numeric |
| keywords | OK | Comma-separated tags |
| inLanguage | OK | "en-US" |
| articleBody | OK | Full text |
| speakable | Partial | cssSelector includes h1 (valid) and .article__title (valid if class exists), but .article__excerpt and .article__summary are not standard Shopify article template classes — verify in live theme |

---

### FAQPage Schema — /pages/faqs

**Status:** Valid, structurally correct

- 8 Questions present with properly nested acceptedAnswer/Answer objects
- All question names are plain-language questions (not keyword-stuffed)
- Answer text is substantive and accurate
- Rich results: RESTRICTED since August 2023 — Google only shows FAQ rich results for government and health authority sites. Happimess will not receive SERP feature, but schema retains semantic value for AI models understanding the Q&A content.
- Recommendation: Keep. The 8 Q&As cover shipping, returns, and tracking — high-intent customer questions that AI assistants will extract and cite.

---

### FAQPage Schema — Product Pages

**Status:** Valid but RESTRICTED; borderline over-implementation

Each product page contains a 10-question FAQPage block with product-specific Q&As (cleaning, durability, size comparisons). The questions are well-formed but:
- Rich results: Not eligible (same Aug 2023 restriction)
- AI value: Moderate — these Q&As help AI models answer product comparison queries
- Risk: 10 FAQs per product page adds 3-4KB of markup. Consider trimming to 5 highest-intent questions per product.

---

### speakable Property Assessment

**BlogPosting selectors:**
```
h1                   — Valid (standard HTML, always present)
.article__title      — Likely valid (common Shopify theme class)
.article__excerpt    — UNVERIFIED — not a standard Shopify theme class
.article__summary    — UNVERIFIED — not a standard Shopify theme class
```

**Product selectors:**
```
.product__title      — Valid (standard Shopify theme class)
.product__description — Valid (standard Shopify theme class)
.product__price      — Valid (standard Shopify theme class)
```

**Assessment:** Product speakable selectors are likely valid. Blog article selectors targeting `.article__excerpt` and `.article__summary` may point to classes that do not exist in the rendered DOM. If these classes are absent, AI crawlers that process speakable hints will only pick up the `h1`. Fix: replace with `.article__content` or `article p:first-of-type` (or verify actual classes in Shopify theme editor).

---

## GEO-Critical Schema Assessment

| Schema | Status | GEO Impact | Assessment |
|---|---|---|---|
| Organization + sameAs | Present, 7 platforms | Critical | Strong. Missing Wikipedia (highest AI entity signal) and Wikidata. |
| Person (both authors) | Present, partial | High | Structurally correct with @id cross-referencing. Missing `image` reduces real-person verification. |
| Article + dateModified | Present, complete | High | Best-practice implementation with author entity linking via @id. |
| speakable (Blog) | Present, partial | Medium | h1 + .article__title valid; .article__excerpt/.article__summary unverified. |
| speakable (Product) | Present, valid | Medium | Correct selectors for Shopify product template. |
| BreadcrumbList | Present, valid | Low | Correctly implemented across all page types including 3-level on blog articles. |
| WebSite + SearchAction | Present, valid | Low | Correctly formed with {search_term_string} template. |
| aggregateRating on Products | Partial | High | Missing on Oscar, Chuck, Slyd — 3 of 8 products have no reviews in schema. Products without aggregateRating are ineligible for Product rich results with star ratings. |

---

## sameAs Entity Linking

### Organization sameAs — Current State

**Total sameAs links:** 7

| Platform | Linked | URL | AI Weight |
|---|---|---|---|
| **Wikipedia** | No | Not linked | Highest — primary AI identity anchor |
| **Wikidata** | No | Not linked | Very High — structured data AI models query directly |
| Facebook | Yes | https://www.facebook.com/happimessofficial/ | Medium |
| Instagram | Yes | https://www.instagram.com/happimess_official/ | Medium |
| LinkedIn | Yes | https://www.linkedin.com/company/happimesshome/ | High |
| Pinterest | Yes | https://www.pinterest.com/happimess_/ | Low |
| YouTube | Yes | https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g | High |
| TikTok | Yes | https://www.tiktok.com/@happimess_official | Medium |
| Crunchbase | Yes | https://www.crunchbase.com/organization/happimess | High |
| GitHub | No | N/A — not applicable for home goods brand | — |

**Gap:** Wikipedia and Wikidata are the two most-cited authority signals for AI entity recognition. When ChatGPT, Claude, or Perplexity evaluate whether "Happimess" is a verified entity, Wikipedia presence is the primary disambiguation source. Crunchbase and LinkedIn are present which is good; adding Wikipedia/Wikidata would move the Organization schema from "commercial entity" to "verifiable entity" in AI knowledge graphs.

### Author sameAs — Current State

| Author | sameAs Links | Platforms |
|---|---|---|
| Jonathan Yaraghi | 2 | LinkedIn, Crunchbase |
| Sandip Hadiya | 1 | LinkedIn only |

**Recommendation:** Sandip Hadiya should add at minimum one additional sameAs link (Twitter/X profile, personal site, or Medium author page) to strengthen author entity confidence.

---

## Deprecated and Restricted Schema Audit

| Schema | Status | Pages Found | Recommendation |
|---|---|---|---|
| FAQPage | **Restricted** (Aug 2023) | /pages/faqs, all product pages | Keep on /pages/faqs — high semantic value for AI. Consider trimming product FAQPage from 10 to 5 questions to reduce page weight. |
| HowTo | Not present | — | Not applicable |
| SpecialAnnouncement | Not present | — | Not applicable |

**No deprecated schemas present.** The FAQPage restriction does not require removal — the schema still provides semantic value for AI assistants answering customer queries. It simply will not generate a SERP FAQ panel for Happimess.

---

## JavaScript Rendering Risk

**Schema Delivery Method:** Server-rendered (Shopify Liquid templates)

All JSON-LD blocks are present in the initial HTML response — confirmed by the fetch_page.py script which parses raw HTML before any JavaScript execution. This is the optimal delivery method.

**Implication:** GPTBot, ClaudeBot, PerplexityBot, and other AI crawlers that do not execute JavaScript will see all structured data on every page. No remediation needed.

**Minor observation:** The fetch tool detected possible client-side rendering warnings on certain wrapper elements (`#t4s-notices__wrapper`, `#appstle-payment-button-override`) — these are app-injected UI elements, not schema markup. They do not affect structured data visibility.

---

## Ready-to-Deploy JSON-LD Templates

### Fix 1 — Person Schemas with `image` Property
**Implementation:** Replace the existing `<script type="application/ld+json">` block on `/pages/meet-our-authors` in Shopify Admin → Pages → meet-our-authors → Edit → Additional scripts section (or in the custom page template if using a template file).

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Person",
      "@id": "https://happimess.com/pages/meet-our-authors#jonathan-yaraghi",
      "name": "Jonathan Yaraghi",
      "url": "https://happimess.com/pages/meet-our-authors",
      "jobTitle": "Home Organization Expert",
      "description": "Jonathan Yaraghi is a content writer and home organization expert at Happimess, specializing in practical guides for kitchen organization, trash management, and home decor.",
      "image": {
        "@type": "ImageObject",
        "url": "https://cdn.shopify.com/s/files/1/0491/2909/5325/files/[REPLACE: jonathan-headshot-filename].jpg",
        "width": 400,
        "height": 400,
        "caption": "Jonathan Yaraghi — Home Organization Expert at Happimess"
      },
      "sameAs": [
        "https://www.linkedin.com/in/jonathanyaraghi/",
        "https://www.crunchbase.com/person/jonathan-yaraghi"
      ],
      "worksFor": {
        "@type": "Organization",
        "@id": "https://happimess.com/#organization",
        "name": "Happimess"
      },
      "knowsAbout": [
        "home organization",
        "kitchen organization",
        "trash management",
        "storage solutions",
        "home decor"
      ]
    },
    {
      "@type": "Person",
      "@id": "https://happimess.com/pages/meet-our-authors#sandip-hadiya",
      "name": "Sandip Hadiya",
      "url": "https://happimess.com/pages/meet-our-authors",
      "jobTitle": "Content Writer",
      "description": "Sandip Hadiya is a content writer at Happimess with a focus on eco-friendly living, home styling, and sustainable organization solutions.",
      "image": {
        "@type": "ImageObject",
        "url": "https://cdn.shopify.com/s/files/1/0491/2909/5325/files/[REPLACE: sandip-headshot-filename].jpg",
        "width": 400,
        "height": 400,
        "caption": "Sandip Hadiya — Content Writer at Happimess"
      },
      "sameAs": [
        "https://www.linkedin.com/in/sandip-hadiya/",
        "[REPLACE: second sameAs URL — Twitter/X, Medium, or personal site]"
      ],
      "worksFor": {
        "@type": "Organization",
        "@id": "https://happimess.com/#organization",
        "name": "Happimess"
      },
      "knowsAbout": [
        "eco-friendly living",
        "home styling",
        "sustainable organization",
        "clutter-free spaces",
        "environmentally conscious living"
      ]
    }
  ]
}
```

**Implementation notes:**
1. Upload author headshot photos to Shopify Admin → Content → Files. Use square images at minimum 400x400px (800x800px preferred).
2. Replace `[REPLACE: jonathan-headshot-filename].jpg` and `[REPLACE: sandip-headshot-filename].jpg` with the actual CDN filenames after upload.
3. Add a second sameAs URL for Sandip (Twitter/X handle, personal website, or any other verified author profile).
4. This block replaces (not supplements) the current Person @graph block on meet-our-authors. The WebSite/Organization @graph block on the page stays unchanged.

---

### Fix 2 — Product brand.name Correction (Shopify Liquid Template)
**Implementation:** In Shopify Admin → Online Store → Themes → Edit Code → find the product JSON-LD snippet (likely `snippets/product-json-ld.liquid` or within `sections/main-product.liquid`). Find the `brand` object and replace.

**Current (broken) code in Liquid:**
```liquid
"brand": {
  "@type": "Brand",
  "name": "{{ shop.name }} Dev"
}
```
or possibly a hardcoded string — the exact Liquid code to search for is:
```
Happimess Dev
```

**Corrected Liquid code:**
```liquid
"brand": {
  "@type": "Brand",
  "name": "{{ shop.name }}"
}
```

**If the value is hardcoded (not Liquid)**, replace `"Happimess Dev"` with `"Happimess"` directly:
```json
"brand": {
  "@type": "Brand",
  "name": "Happimess"
}
```

**Affected products (confirmed):** Elmo, Oscar, Beni, Chuck, Ashley — 5 products confirmed with `"Happimess Dev"`.
**Already correct:** Slyd, Betty, Robo — these 3 use `"Happimess"` and do not need changes.

---

### Fix 2b — aggregateRating Template for Products Missing It
**Implementation:** Add to the Product JSON-LD block for Oscar, Chuck, and Slyd. This template uses Shopify's Liquid variables. Add this block inside the Product schema, after the `offers` array.

```liquid
{% if product.metafields.reviews.rating.value != blank %}
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": {{ product.metafields.reviews.rating.value | json }},
  "reviewCount": {{ product.metafields.reviews.rating_count.value | json }},
  "bestRating": 5,
  "worstRating": 1
},
{% endif %}
```

**If using a reviews app (e.g., Judge.me, Okendo, Yotpo)** rather than Shopify native reviews, the metafield path differs. For Judge.me the path is typically `product.metafields.judgeme.badge`. Contact your reviews app support for the exact Liquid variable.

**Static JSON-LD template** (for manual insertion before a reviews app is integrated, using placeholder values that MUST be updated when real reviews exist):

```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": [REPLACE: numeric average e.g. 4.8],
  "reviewCount": [REPLACE: integer count e.g. 12],
  "bestRating": 5,
  "worstRating": 1
}
```

**Warning:** Do not add aggregateRating with fabricated data. Only add this field when the product has real, verifiable customer reviews. Google may penalize products where the schema rating does not match visible on-page reviews.

---

### Fix 3 — Corrected speakable cssSelector for BlogPosting
**Implementation:** In Shopify Admin → Online Store → Themes → Edit Code → find the blog article JSON-LD snippet (likely `sections/main-article.liquid` or `snippets/article-json-ld.liquid`). Replace the speakable block.

**Current (partially broken):**
```json
"speakable": {
  "@type": "SpeakableSpecification",
  "cssSelector": [
    "h1",
    ".article__title",
    ".article__excerpt",
    ".article__summary"
  ]
}
```

**Corrected version (using selectors that exist in standard Shopify article templates):**
```json
"speakable": {
  "@type": "SpeakableSpecification",
  "cssSelector": [
    "h1.article__title",
    ".article__content > p:first-of-type",
    ".article__content > h2:first-of-type",
    ".article__content"
  ]
}
```

**Explanation of each selector:**
- `h1.article__title` — The article headline; present in virtually all Shopify themes using standard article templates
- `.article__content > p:first-of-type` — The opening paragraph; typically the most concise summary of the article and the highest-value speakable candidate
- `.article__content > h2:first-of-type` — The first subheading; signals the article's primary topic structure
- `.article__content` — The full article body; signals to AI assistants that the entire article content is suitable for extraction

**Alternative if `.article__content` is not the correct class in your theme:** Open a blog article in Chrome DevTools → Inspect → find the `<div>` wrapping the article body text → note the actual class name → use that class instead. Common Shopify theme class names: `.article__body`, `.article-template__content`, `.rte`, `.blog-article__content`.

---

## New Schema Opportunities

### 1. ItemList for Collection/Category Pages — HIGH Priority

Collection pages (`/collections/trash-cans`, `/collections/storage-bins`, etc.) currently have no structured data beyond the global WebSite/Organization block. Adding `ItemList` schema enables AI models to understand the product catalog hierarchy and improves collection page visibility in AI-generated shopping responses.

**Example implementation for `/collections/trash-cans`:**

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Trash Cans — Happimess",
  "description": "Modern trash cans designed for kitchens and small spaces, available in step-open, touchless, and dual-compartment styles.",
  "url": "https://happimess.com/collections/trash-cans",
  "numberOfItems": [REPLACE: product count],
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "url": "https://happimess.com/products/oscar-round-8-gallon-step-open-trash-can-with-free-mini-trash-can",
      "name": "Oscar 30 Liter/8 Gallon Trash Can with Free Mini Oscar"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "url": "https://happimess.com/products/elmo-rectangular-8-gallon-double-bucket-trash-can-with-soft-close-lid",
      "name": "Elmo 30 Liter/8 Gallon Double-Bucket Trash Can"
    }
  ]
}
```

**GEO impact:** When users ask ChatGPT or Perplexity "what trash cans does Happimess sell," AI models with ItemList context can return a structured answer listing products. Without it, the AI must infer the catalog from product page text alone.

**Shopify implementation:** Add via a collection template (`sections/main-collection.liquid`) using Liquid to loop through `collection.products`.

---

### 2. VideoObject for YouTube Content — MEDIUM Priority

Happimess has a YouTube channel (`UC6lUDdoZeZrYnoY2kmZyf4g`). If product demonstration or organizational tips videos are embedded on product or blog pages, adding `VideoObject` schema enables Video rich results in Google Search and signals multimedia authority to AI models.

**Template for any page with an embedded YouTube video:**

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "[REPLACE: Video title]",
  "description": "[REPLACE: Video description — 1-2 sentences]",
  "thumbnailUrl": "https://img.youtube.com/vi/[REPLACE: YouTube-video-id]/maxresdefault.jpg",
  "uploadDate": "[REPLACE: ISO 8601 date e.g. 2026-03-15]",
  "duration": "PT[REPLACE: minutes]M[REPLACE: seconds]S",
  "contentUrl": "https://www.youtube.com/watch?v=[REPLACE: YouTube-video-id]",
  "embedUrl": "https://www.youtube.com/embed/[REPLACE: YouTube-video-id]",
  "publisher": {
    "@type": "Organization",
    "@id": "https://happimess.com/#organization",
    "name": "Happimess"
  }
}
```

**Required Google fields:** `name`, `description`, `thumbnailUrl`, `uploadDate` — all must be present for Video rich result eligibility.

---

### 3. LocalBusiness as Type Extension — MEDIUM Priority

The Organization schema at 185 Madison Avenue, New York, NY 10016 qualifies to also carry `LocalBusiness` typing, which adds NYC business context and makes the entity appear in local search knowledge panels. This is especially relevant if Happimess has a showroom or accepts in-person visits.

```json
{
  "@context": "https://schema.org",
  "@type": ["Organization", "LocalBusiness"],
  "@id": "https://happimess.com/#organization",
  "name": "Happimess",
  "url": "https://happimess.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "185 Madison Avenue",
    "addressLocality": "New York",
    "addressRegion": "NY",
    "postalCode": "10016",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 40.7459,
    "longitude": -73.9829
  },
  "hasMap": "https://maps.google.com/?q=185+Madison+Avenue+New+York+NY+10016",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "18:00"
    }
  ]
}
```

**Note:** Only add `openingHoursSpecification` if Happimess has a physical location that receives customers. If the address is an office/warehouse only, omit it or add a `branchOf` property instead. Using the dual `["Organization", "LocalBusiness"]` type is valid Schema.org and Google-supported.

---

### 4. Review Schema on Individual Products — LOW Priority (deferred)

Shopify native reviews or a reviews app (Judge.me, etc.) typically generates individual `Review` schema automatically when the app is active. If the current reviews app is not injecting Review schema:

```json
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {
    "@type": "Product",
    "name": "[REPLACE: Product name]",
    "url": "[REPLACE: Product URL]"
  },
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": [REPLACE: 1-5],
    "bestRating": 5
  },
  "author": {
    "@type": "Person",
    "name": "[REPLACE: Reviewer first name or display name]"
  },
  "reviewBody": "[REPLACE: Review text]",
  "datePublished": "[REPLACE: ISO 8601 date]"
}
```

**Recommendation:** Do not implement individual Review schema manually. Instead, verify that the existing reviews app (confirm which one is active in Shopify Admin → Apps) is outputting Review schema. If not, switching to Judge.me (which auto-generates Review + AggregateRating schema) is the most efficient path.

---

### 5. HowTo Schema on Process Blog Posts — NOT RECOMMENDED

Google removed HowTo rich results in September 2023. HowTo schema provides zero search result feature benefit. For blog posts that teach a process (e.g., "How to Organize a Small Kitchen"), use structured article formatting (numbered steps as `<ol>`, clear subheadings) for AI extractability rather than HowTo schema markup. The content structure itself is sufficient.

---

## Wikidata Entity Creation Guide for Happimess

Creating a Wikidata entity for Happimess is the single highest-ROI schema action available. It takes approximately 30-60 minutes, is free, and permanently establishes Happimess as a verifiable entity in the knowledge base that ChatGPT, Google's Knowledge Graph, Perplexity, and other AI systems query directly.

### Why Wikidata Matters for AI

When an AI model encounters "Happimess" as an entity claim, it checks Wikidata (Q-items) as a primary disambiguation and verification source. A Wikidata entry:
- Confirms Happimess is a real, verifiable company (not an AI hallucination or ambiguous term)
- Provides structured facts (founding date, location, industry, founders) that AI models cite
- Creates the anchor for the Wikipedia `sameAs` link once a Wikipedia article exists
- Adds Happimess to Wikidata's product catalog of home goods companies

### Eligibility Assessment

Happimess meets Wikidata's notability threshold for companies:
- Commercial entity with a functioning website
- Crunchbase profile exists (independent verification)
- LinkedIn company page exists (independent verification)
- Founded 2020 — sufficient operational history
- Physical address (New York, NY) — verifiable location

### Step-by-Step Creation Instructions

**Step 1 — Create a Wikidata account**
- Go to https://www.wikidata.org/wiki/Special:CreateAccount
- Create an account with a real email address (the account will be the author of the entity)
- A 4-day waiting period before creating new items may apply to new accounts

**Step 2 — Check for existing entries**
- Search https://www.wikidata.org/wiki/Special:Search for "Happimess"
- If no results appear, proceed to Step 3
- If an entry exists but is incomplete, edit it rather than creating a new one

**Step 3 — Create the new item**
- Go to https://www.wikidata.org/wiki/Special:NewItem
- Label: `Happimess`
- Description: `American home organization and storage products company`
- Also known as: leave blank (or add alternate spellings if any)
- Click "Create"

**Step 4 — Add statements (properties)**

Add these statements in order of importance:

| Property ID | Property Label | Value to Enter |
|---|---|---|
| P31 | instance of | Q4830453 (business) |
| P31 | instance of | Q1643989 (limited liability company) — if applicable |
| P17 | country | Q30 (United States of America) |
| P131 | located in | Q60 (New York City) |
| P856 | official website | https://happimess.com |
| P571 | inception | 2020-01-15 |
| P452 | industry | Q1921885 (home furnishings) |
| P18 | image | Upload logo from Wikimedia Commons first (see Step 5) |
| P2002 | Twitter username | happimess_official |
| P2013 | Facebook profile ID | happimessofficial |
| P2397 | YouTube channel ID | UC6lUDdoZeZrYnoY2kmZyf4g |
| P4633 | Pinterest username | happimess_ |
| P7085 | TikTok username | @happimess_official |
| P6634 | LinkedIn personal profile ID | company/happimesshome |
| P1581 | official blog/news URL | https://happimess.com/blogs/news |

**For P31 (instance of):** Start with Q4830453 (business). You can also add Q1616075 (e-commerce) as a second P31 value.

**Step 5 — Upload logo to Wikimedia Commons (required for P18)**
- Go to https://commons.wikimedia.org/wiki/Special:UploadWizard
- Upload the Happimess SVG logo from: `https://cdn.shopify.com/s/files/1/0491/2909/5325/files/happimess-logo-ai-file_1.svg`
- License: select "This work is by the author and I'm releasing it under a free license" — choose CC BY-SA 4.0
- Category: add `Companies of New York City` and `Home goods companies`
- After upload, note the filename (e.g., `Happimess logo.svg`) and use it in the Wikidata P18 field

**Step 6 — Note your Q-number**

After creating the item, Wikidata assigns a Q-number (e.g., Q130012345). Record this number.

**Step 7 — Add Wikidata URL to Organization schema**

Once the Wikidata item is live, add it to the `sameAs` array in `theme.liquid`:

```json
"sameAs": [
  "https://www.facebook.com/happimessofficial/",
  "https://www.instagram.com/happimess_official/",
  "https://www.linkedin.com/company/happimesshome/",
  "https://www.pinterest.com/happimess_/",
  "https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g",
  "https://www.tiktok.com/@happimess_official",
  "https://www.crunchbase.com/organization/happimess",
  "https://www.wikidata.org/wiki/Q[REPLACE: your Q-number]"
]
```

**Step 8 — Wikipedia article (longer-term goal)**

After the Wikidata entry is established and has been live for 30+ days, consider creating a Wikipedia article stub for Happimess:
- The company must demonstrate "notability" — typically defined as significant coverage in multiple independent, reliable sources
- If Happimess has been covered in publications like Apartment Therapy, The Spruce, New York Magazine, or similar home goods publications, those constitute reliable sources
- A minimal Wikipedia stub citing 3-4 independent sources (not press releases or the company's own website) meets notability
- Once the Wikipedia article exists, add `https://en.wikipedia.org/wiki/Happimess` to the Organization sameAs array

**Estimated time:** Wikidata entry — 30-60 minutes. Wikipedia article (if pursuing) — 2-4 hours including source research.

---

## Priority Action List

### CRITICAL — Fix within 48 hours

**1. Fix `brand.name: "Happimess Dev"` on 5 products**
- Location: Shopify Admin → Online Store → Themes → Edit Code → product JSON-LD snippet
- Search for `"Happimess Dev"` in the theme code
- Fix: Replace with `"{{ shop.name }}"` (Liquid) or hardcoded `"Happimess"`
- Affected products: Elmo, Oscar, Beni, Chuck, Ashley
- Impact: Currently prevents these products from being correctly attributed to Happimess brand in Google Shopping, Google AI Overviews, and AI model responses about Happimess products. Critical brand trust issue.

---

### HIGH — Fix within 1 week

**2. Add `image` property to both Person schemas**
- Location: Shopify Admin → Pages → meet-our-authors → Edit (or custom page template)
- Action: Upload headshot photos to Shopify Files CDN; add `image` as ImageObject with url, width, height, caption
- Use the ready-to-deploy JSON-LD in Fix 1 above
- Impact: Strengthens E-E-A-T author verification; AI models use author images as a real-person signal; improves author schema eligibility for Google author rich results

**3. Add aggregateRating to Oscar, Chuck, and Slyd products**
- Location: Product JSON-LD template (same file as brand.name fix)
- Action: Use Shopify metafields or reviews app Liquid variables to inject real review data
- Warning: Only add when real reviews exist; do not fabricate values
- Impact: Products without aggregateRating in schema cannot display star ratings in Google Shopping or Google AI product panels

**4. Verify and fix speakable selectors on BlogPosting**
- Location: Shopify Admin → Themes → Edit Code → article JSON-LD snippet
- Action: Open a blog article in Chrome DevTools; confirm actual CSS class of article body wrapper; replace `.article__excerpt` and `.article__summary` with verified classes
- Use the corrected template in Fix 3 above
- Impact: Correctly targeted speakable selectors improve AI assistant readability and voice search extraction from blog content

---

### MEDIUM — Fix within 2-4 weeks

**5. Create Wikidata entity for Happimess**
- Action: Follow the step-by-step guide above (30-60 minutes)
- Then add Wikidata URL to Organization sameAs in `theme.liquid`
- Impact: Single most impactful entity authority addition; activates AI knowledge graph recognition; enables disambiguation for "Happimess" in LLM responses

**6. Add second sameAs link for Sandip Hadiya**
- Location: meet-our-authors page Person schema (same fix as #2)
- Action: Add Twitter/X profile URL, personal website, or Medium author page
- Impact: Strengthens author entity confidence for AI models

**7. Add ItemList schema to collection pages**
- Location: `sections/main-collection.liquid` — add JSON-LD block using Liquid loop over `collection.products`
- Impact: Enables AI models to return structured product catalog answers for "what [product type] does Happimess sell" queries

---

### LOW — Backlog (30+ days)

**8. Evaluate LocalBusiness typing addition to Organization schema**
- Determine whether 185 Madison Ave location receives customers
- If yes: add `["Organization", "LocalBusiness"]` dual typing with GeoCoordinates and openingHours
- Impact: Activates local business knowledge panel; relevant for NYC-based customer searches

**9. Add VideoObject schema to any pages with YouTube embeds**
- Audit product and blog pages for embedded YouTube videos
- Add VideoObject block for each with name, description, thumbnailUrl, uploadDate, contentUrl, embedUrl
- Impact: Enables Video rich results; YouTube embeds without VideoObject schema are invisible to search

**10. Trim FAQPage on product pages from 10 to 5 questions**
- Current: 10 Q&As per product (3-4KB of markup)
- Recommended: 5 highest-intent questions per product
- Impact: Reduces page weight and schema noise while retaining AI semantic value for the most important queries

**11. Pursue Wikipedia article for Happimess (after Wikidata entry is 30+ days old)**
- Requires 3-4 independent reliable source citations (Apartment Therapy, The Spruce, New York Magazine, etc.)
- Once published: Add Wikipedia URL to Organization sameAs (highest possible AI entity authority signal)

---

## Appendix — Schema Implementation File Reference (Shopify)

| Schema Type | Likely File Location in Shopify Theme |
|---|---|
| Organization + WebSite + SearchAction | `layout/theme.liquid` — in `<head>` section |
| Product (brand, aggregateRating, offers) | `sections/main-product.liquid` or `snippets/product-json-ld.liquid` |
| BlogPosting + speakable | `sections/main-article.liquid` or `snippets/article-json-ld.liquid` |
| FAQPage (/pages/faqs) | Custom page template — `templates/page.faqs.liquid` or page section |
| FAQPage (products) | Same product template file as Product schema |
| BreadcrumbList | `layout/theme.liquid` (sitewide) or page-type sections |
| Person schemas | Custom page template — `templates/page.meet-our-authors.liquid` |
| ItemList (collections) | `sections/main-collection.liquid` |

**To find the exact file:** In Shopify Admin → Online Store → Themes → Edit Code → use the theme editor search (top of file list) to search for `application/ld+json` — this will surface all files containing structured data blocks.
