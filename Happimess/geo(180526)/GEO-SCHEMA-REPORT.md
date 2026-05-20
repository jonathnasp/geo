# GEO Schema Report — Happimess
**URL:** https://happimess.com/  
**Analysis Date:** 2026-05-18  
**Format:** JSON-LD (server-rendered in initial HTML — confirmed Shopify SSR)  

---

## Structured Data Score: 62 / 100 — Fair

All schema blocks are delivered server-side in the initial HTML response. AI crawlers (GPTBot, ClaudeBot, PerplexityBot) that do not execute JavaScript receive all schemas correctly. No rendering risk.

---

## Schema Inventory

| # | Schema Type | Page(s) | Status | Rich Result Eligible | GEO Impact |
|---|-------------|---------|--------|---------------------|-----------|
| 1 | Organization | All pages | ✅ Valid (partial) | N/A | Critical |
| 2 | WebSite + SearchAction | All pages | ✅ Valid (minor) | Yes (Sitelinks search box) | Medium |
| 3 | WebPage | Homepage | ✅ Valid | No | Low |
| 4 | Product | Product pages | ✅ Valid | Yes | High |
| 5 | BreadcrumbList | Products, blog articles | ✅ Valid | Yes | Medium |
| 6 | BlogPosting | Blog articles | ✅ Valid (partial) | Partial | High |
| 7 | Blog | Blog index | ⚠️ Partial | No | Low |
| 8 | FAQPage | FAQ page, product pages | ✅ Valid (restricted) | Restricted† | High |
| 9 | Person (authors) | Blog articles | ⚠️ Partial | N/A | High |
| 10 | Product → aggregateRating | Product pages | ❌ Missing | Blocks rich results | Critical |
| 11 | BreadcrumbList | Homepage, About, FAQ | ❌ Missing | — | Low |

†FAQPage rich results restricted to government/health sites since Aug 2023. Schema retained for AI extraction value.

---

## Detailed Validation

### Schema 1: Organization ✅ Valid (partial)
**Pages:** All pages (injected via `theme.liquid`)

| Property | Status | Value |
|----------|--------|-------|
| @context | ✅ | `"https://schema.org"` |
| @type | ✅ | `"Organization"` |
| @id | ✅ | `"https://happimess.com/#organization"` |
| name | ✅ | `"Happimess"` |
| url | ✅ | `"https://happimess.com"` |
| logo | ✅ | ImageObject with CDN URL |
| description | ✅ | Present |
| telephone | ✅ | `"(917) 261-4961"` |
| email | ✅ | `"hello@happimess.com"` |
| address | ✅ | Full PostalAddress |
| foundingDate | ✅ | `"2020-01-15"` |
| contactPoint | ✅ | Customer service ContactPoint |
| knowsAbout | ✅ | 10 topic strings |
| sameAs | ⚠️ Partial | 6 platforms linked; missing Wikidata, Crunchbase |
| industry | ⚠️ Warning | Not a standard Schema.org property (harmless) |

**Current sameAs (6):** Facebook, Instagram, LinkedIn (`/company/happimesshome/`), Pinterest, YouTube, TikTok  
**Missing from sameAs:** Wikidata Q-number, Crunchbase, BBB (after registration)

---

### Schema 2: WebSite + SearchAction ✅ Valid (minor)
**Pages:** All pages

| Property | Status | Notes |
|----------|--------|-------|
| @type | ✅ | `"WebSite"` |
| name | ✅ | `"Happimess"` |
| potentialAction | ✅ | SearchAction present |
| target | ⚠️ | Uses nested EntryPoint object — Google recommends plain string |
| query-input | ✅ | `"required name=search_term_string"` |
| sameAs | ✅ | 6 platforms linked (redundant with Organization but harmless) |

**Minor fix:** Change `target` from nested EntryPoint to plain string URL template.

---

### Schema 3: WebPage ✅ Valid
**Page:** Homepage

| Property | Status | Notes |
|----------|--------|-------|
| @type | ✅ | `"WebPage"` |
| description | ✅ | Populated (was null in April audit — fixed) |
| name | ⚠️ Warning | `"Home"` — too generic; should be the full page title |
| breadcrumb | ❌ Missing | No BreadcrumbList reference on homepage |
| primaryImageOfPage | ❌ Missing | No featured image declared |

---

### Schema 4: Product ✅ Valid
**Pages:** All product pages

| Property | Status | Value / Notes |
|----------|--------|--------------|
| @type | ✅ | `"Product"` |
| name | ✅ | Product title |
| description | ✅ | Present and detailed |
| brand.@type | ✅ | `"Brand"` |
| **brand.name** | ✅ **FIXED** | **`"Happimess"`** (was `"Happimess Dev"` — confirmed resolved) |
| offers | ✅ | 11 Offer objects with full detail |
| offers[].price | ✅ | Numeric (not string) |
| offers[].priceCurrency | ✅ | `"USD"` |
| offers[].availability | ✅ | `"https://schema.org/InStock"` |
| offers[].priceValidUntil | ✅ | `"2027-12-31"` |
| offers[].shippingDetails | ✅ | Full OfferShippingDetails with delivery window |
| offers[].hasMerchantReturnPolicy | ✅ | 30-day return policy with all required fields |
| **aggregateRating** | ❌ **Missing** | **Highest-impact gap — blocks rich results and AI product comparisons** |
| review | ❌ Missing | No Review objects |
| gtin / mpn | ❌ Missing | No GTIN, MPN identifiers |
| color | ❌ Missing | Color variants not in schema |

---

### Schema 5: BreadcrumbList ✅ Valid
**Pages:** Product pages, blog articles

| Property | Status | Notes |
|----------|--------|-------|
| @type | ✅ | `"BreadcrumbList"` |
| itemListElement | ✅ | ListItem with position, name, item |
| item URLs | ✅ | Fully qualified absolute URLs |

**Missing pages:** Homepage, About Us, FAQ — add two-level breadcrumb (Home → Page Name).

---

### Schema 6: BlogPosting ✅ Valid (partial)
**Pages:** Blog articles

| Property | Status | Notes |
|----------|--------|-------|
| @type | ✅ | `"BlogPosting"` |
| headline | ✅ | Article title |
| description | ✅ | Article excerpt |
| image | ✅ | ImageObject with URL |
| datePublished | ✅ | ISO 8601 with timezone |
| dateModified | ✅ | ISO 8601 with timezone |
| articleBody | ✅ | Full text present |
| inLanguage | ✅ | `"en-US"` |
| speakable | ✅ | SpeakableSpecification with cssSelector — direct AIO eligibility |
| publisher | ✅ | Organization with logo |
| author | ⚠️ Partial | Names present; see Person schema below |
| articleSection | ❌ Missing | No topic/category declared |
| wordCount | ❌ Missing | Not declared |
| keywords | ❌ Missing | No keyword list |

---

### Schema 7: Blog (index) ⚠️ Partial
**Page:** `/blogs/news`

| Property | Status | Notes |
|----------|--------|-------|
| @type | ✅ | `"Blog"` |
| headline | ✅ | `"From The Mess Experts"` |
| description | ❌ | Empty string `""` — should describe the blog |
| blogPost | ✅ | 14+ BlogPosting summaries |
| BlogPosting[].author | ⚠️ | See Person schema |

---

### Schema 8: FAQPage ✅ Valid (restricted)
**Pages:** `/pages/faqs`, product pages

| Property | Status | Notes |
|----------|--------|-------|
| @type | ✅ | `"FAQPage"` |
| mainEntity | ✅ | 8–10 Question objects |
| Question.name | ⚠️ | All lowercase on some questions — cosmetic only |
| acceptedAnswer | ✅ | All present and non-empty |

**Important note:** Google restricted FAQPage rich results to government/health sites in August 2023. This schema will NOT generate a SERP rich result for happimess.com. However, the semantic Q&A structure is directly parsed by AI models (ChatGPT, Perplexity, ClaudeBot) for answer extraction. **Keep this schema — do not remove.**

---

### Schema 9: Person (authors) ⚠️ Partial
**Pages:** Blog articles

| Author | @id | name | Casing | sameAs | jobTitle | image |
|--------|-----|------|--------|--------|----------|-------|
| Jonathan Yaraghi | `#jonathan-yaraghi` | `"Jonathan Yaraghi"` | ✅ | ❌ | ❌ | ❌ |
| Sandip Hadiya | `#sandip-hadiya` | **`"sandip hadiya"`** | ❌ | ❌ | ❌ | ❌ |

Both author @id values point to `https://happimess.com/pages/meet-our-authors#[anchor]` — this page must exist and resolve correctly for the author entity to be valid.

---

## Complete JSON-LD Fix Library

All snippets below are copy-ready for Shopify Admin → Online Store → Themes → Edit Code.

---

### Fix 1: Organization — Add Wikidata + Crunchbase to sameAs
**File:** `theme.liquid`  
**Priority:** High | **Effort:** 5 min

```json
"sameAs": [
  "https://www.facebook.com/happimessofficial/",
  "https://www.instagram.com/happimess_official/",
  "https://www.linkedin.com/company/happimesshome/",
  "https://www.pinterest.com/happimess_/",
  "https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g",
  "https://www.tiktok.com/@happimess_official",
  "https://www.crunchbase.com/organization/happimess",
  "https://www.wikidata.org/wiki/[REPLACE: Q-number after creating Wikidata entity]"
]
```

---

### Fix 2: Product — aggregateRating
**File:** `product.liquid` (inside the Product JSON-LD block)  
**Priority:** Critical | **Effort:** 30 min (+ review app setup)

**Option A — Dynamic from review app metafields (recommended):**
```liquid
{% if product.metafields.reviews.rating %}
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "{{ product.metafields.reviews.rating.value }}",
  "reviewCount": "{{ product.metafields.reviews.rating_count.value }}",
  "bestRating": "5",
  "worstRating": "1"
},
{% endif %}
```

**Option B — Static placeholder (use only if reviews exist):**
```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "4.7",
  "reviewCount": "24",
  "bestRating": "5",
  "worstRating": "1"
}
```

**Note:** Do not add a static aggregateRating without real review data — Google will penalize fake review schema. Enable the review app's JSON-LD output first, collect at least 5 reviews, then activate.

---

### Fix 3: Person Schema — Jonathan Yaraghi (enriched)
**File:** `theme.liquid` (add as sitewide entity) or `article.liquid` (add inline)  
**Priority:** High | **Effort:** 15 min

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://happimess.com/pages/meet-our-authors#jonathan-yaraghi",
  "name": "Jonathan Yaraghi",
  "url": "https://happimess.com/pages/meet-our-authors#jonathan-yaraghi",
  "jobTitle": "[REPLACE: e.g. Founder & CEO]",
  "worksFor": {
    "@type": "Organization",
    "@id": "https://happimess.com/#organization",
    "name": "Happimess"
  },
  "image": {
    "@type": "ImageObject",
    "url": "[REPLACE: Absolute URL to author headshot, e.g. https://cdn.shopify.com/s/files/.../jonathan-yaraghi.jpg]"
  },
  "description": "[REPLACE: e.g. Jonathan Yaraghi is the founder of Happimess, a New York City-based home organization brand. He evaluates every product through Happimess's 30-day testing protocol before it reaches customers.]",
  "sameAs": [
    "[REPLACE: https://www.linkedin.com/in/jonathan-yaraghi-profile]"
  ],
  "knowsAbout": [
    "home organization",
    "storage solutions",
    "trash management",
    "interior design",
    "e-commerce"
  ]
}
```

---

### Fix 4: Person Schema — Sandip Hadiya (fix casing + enrich)
**File:** `theme.liquid` or `article.liquid`  
**Priority:** Medium | **Effort:** 10 min  

**Immediate fix (5 min):** In Shopify Admin → Settings → Account, find the Sandip Hadiya account and change the display name from `sandip hadiya` to `Sandip Hadiya`. This propagates to all existing blog post schemas automatically.

**Full enrichment:**
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://happimess.com/pages/meet-our-authors#sandip-hadiya",
  "name": "Sandip Hadiya",
  "url": "https://happimess.com/pages/meet-our-authors#sandip-hadiya",
  "jobTitle": "[REPLACE: e.g. Head of Content & GEO]",
  "worksFor": {
    "@type": "Organization",
    "@id": "https://happimess.com/#organization",
    "name": "Happimess"
  },
  "image": {
    "@type": "ImageObject",
    "url": "[REPLACE: Absolute URL to author headshot]"
  },
  "description": "[REPLACE: e.g. Sandip Hadiya leads content strategy at Happimess, specializing in home organization, storage solutions, and GEO optimization.]",
  "sameAs": [
    "[REPLACE: LinkedIn profile URL]"
  ]
}
```

---

### Fix 5: WebSite SearchAction — Fix EntryPoint
**File:** `theme.liquid`  
**Priority:** Low | **Effort:** 5 min

Replace the current nested EntryPoint `target` with a plain string:

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://happimess.com/#website",
  "url": "https://happimess.com",
  "name": "Happimess",
  "description": "Modern storage, organization, and furniture solutions. From bins and baskets to trash cans and trunks, keep your home stylishly clutter-free.",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://happimess.com/search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

---

### Fix 6: Blog Index — Fix Empty Description
**File:** `blog.liquid` or Shopify Admin → Online Store → Blog (SEO description field)  
**Priority:** Low | **Effort:** 5 min

```json
"description": "Expert advice, buying guides, and home organization tips from the Happimess team — covering trash can selection, storage solutions, kitchen organization, and sustainable living."
```

---

### Fix 7: BlogPosting — Add Missing Properties
**File:** `article.liquid` (inside the BlogPosting JSON-LD block)  
**Priority:** Medium | **Effort:** 30 min (one-time template edit, applies to all articles)

Add these three properties to the BlogPosting schema:

```liquid
"articleSection": "{{ article.tags | join: ', ' }}",
"wordCount": {{ article.content | strip_html | split: ' ' | size }},
"keywords": "{{ article.tags | join: ', ' }}"
```

---

### Fix 8: BreadcrumbList — About Us and FAQ Pages
**File:** `page.about-us.liquid` and `page.faqs.liquid` (or the page template)  
**Priority:** Low | **Effort:** 10 min

Add to both pages:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://happimess.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "{{ page.title }}",
      "item": "{{ canonical_url }}"
    }
  ]
}
</script>
```

---

### Fix 9: WebPage — Fix Homepage name property
**File:** `theme.liquid` or `index.liquid`  
**Priority:** Low | **Effort:** 5 min

Change:
```json
"name": "Home"
```
To:
```json
"name": "Trash Cans, Storage Furniture & Home Organization | Happimess"
```

---

### Fix 10: FAQPage for /pages/faqs — Complete Block
**Already provided in:** `GEO-PLATFORM-OPTIMIZATION.md`

The complete FAQPage JSON-LD block with all 8 Q&A pairs verbatim is in the Platform Optimization report. Deploy to the FAQ page template.

---

## Schema Implementation Order

| Priority | Fix | File | Time | Impact |
|----------|-----|------|------|--------|
| 1 | aggregateRating on products (after enabling review app) | `product.liquid` | 30 min | Critical — unlocks Google Shopping rich results |
| 2 | Fix author casing: `sandip hadiya` → `Sandip Hadiya` | Shopify Admin → Account | 5 min | High — propagates to all blog schemas |
| 3 | Add Wikidata + Crunchbase to Organization sameAs | `theme.liquid` | 5 min | High — entity disambiguation |
| 4 | Enrich Person schemas (jobTitle, image, sameAs) | `theme.liquid` | 15 min | High — expertise signals |
| 5 | Add articleSection + wordCount + keywords to BlogPosting | `article.liquid` | 30 min | Medium |
| 6 | Fix Blog index description (empty string) | Blog admin | 5 min | Low |
| 7 | Fix WebSite SearchAction EntryPoint | `theme.liquid` | 5 min | Low |
| 8 | Fix WebPage name from "Home" to full title | `index.liquid` | 5 min | Low |
| 9 | Add BreadcrumbList to About Us and FAQ pages | Page templates | 10 min | Low |

---

## Schema Validation Resources

Test implemented schemas before deploying to production:

| Tool | URL | What to Test |
|------|-----|-------------|
| Google Rich Results Test | search.google.com/test/rich-results | Product, BlogPosting, FAQPage, BreadcrumbList |
| Schema.org Validator | validator.schema.org | All schema types |
| Bing Markup Validator | bing.com/webmaster/tools | Bing-specific schema processing |
| JSON-LD Playground | json-ld.org/playground | JSON-LD syntax validation |

---

## Progress vs. April 2026 Audit

| Issue | April | May 18 |
|-------|-------|--------|
| `brand.name: "Happimess Dev"` | Critical | ✅ Fixed — `"Happimess"` confirmed |
| `description: null` in WebPage | High | ✅ Fixed — description populated |
| Admin usernames in JSON-LD | High | ✅ Fixed — real names present |
| Organization missing sameAs | High | ✅ Partially fixed — 6 platforms; Wikidata/Crunchbase pending |
| aggregateRating missing | High | ❌ Still missing |
| Author casing error | Medium | ❌ `"sandip hadiya"` still lowercase |
| Author enrichment (jobTitle, sameAs) | Medium | ❌ Not yet done |
| BlogPosting articleSection/keywords | Low | ❌ Not yet done |
| BreadcrumbList on About/FAQ | Low | ❌ Not yet done |

---

*Schema analysis conducted 2026-05-18. Output file: GEO-SCHEMA-REPORT.md*
