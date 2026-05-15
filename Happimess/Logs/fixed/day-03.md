# Day 3 — Schema Deployment (Product + Collection + Article + Speakable)
**Date:** May 9, 2026 | **Estimated Time:** 4 hours | **Score Impact:** +6 points (54 → ~60)

---

## Day 3 Goals

Day 3 deploys the four schema templates prepared in this audit package to their correct Shopify theme locations. These are template-level changes — one edit fixes the entire product catalog, all collection pages, and all 26 blog posts simultaneously.

1. **Product schema** — Deploy `schema-product.liquid` snippet: absolute URL fix, `@context` trailing slash fix, AggregateRating wired to review metafields
2. **Collection schema** — Deploy `schema-collection.liquid` snippet: CollectionPage + ItemList on all `/collections/` pages (currently zero schema)
3. **Article schema with speakable** — Deploy `schema-article.liquid` snippet: fixes author URL, adds speakable property for AI assistant readiness
4. **FAQPage schema on blog posts** — Wire FAQ content in key posts to structured data

**Why Day 3?** Schema template deployment is a force-multiplier: one snippet change propagates across 100+ products, 6+ collections, and 26 blog posts. This is the highest ROI code change in the entire roadmap.

**Structured Data Impact:** Schema score moves from 62/100 (after Day 1 fix) to ~75/100. Rich result eligibility improves for products, articles, and collection pages.

---

## FIX-09 — Deploy Product Schema (AggregateRating + Absolute URL + @context Fix)

### Severity
**HIGH** (affects all ~100+ product pages)

### Problem
Current product schema has three errors present on every product page:
1. `@context: "https://schema.org/"` — trailing slash is a validation error
2. `url` field is a **relative path** (e.g., `/products/molly-8-gallon-step-open`), not absolute
3. No `AggregateRating` — star ratings are absent from all product SERPs and Gemini Shopping surfaces

### Why This Is Dangerous
- **No star ratings in Google SERPs:** Missing AggregateRating = no star rating display = lower click-through rate vs competitors who have it.
- **Gemini Shopping invisible:** Google Gemini surfaces products with structured Product schema + AggregateRating. Without it, all 100+ Happimess products are invisible to Gemini Shopping queries.
- **Validation errors:** The `@context` trailing slash and relative `url` cause Google's Rich Results Test to flag errors on every product. Partially valid schema is deprioritized vs clean competitors.

### Current Broken Schema (on all product pages)
```json
{
  "@context": "https://schema.org/",    ← trailing slash = error
  "@type": "Product",
  "url": "/products/product-slug",      ← relative URL = error
  "aggregateRating": {
    "ratingValue": "4.5",               ← string not number = error
    "reviewCount": "120"                ← string not number = error
  }
  // NO AggregateRating wired to real review data
}
```

### How To Fix

**Step 1 — Create the product schema snippet:**
1. Shopify Admin → **Online Store → Themes → Edit code**
2. Under **Snippets**, click **"Add a new snippet"**
3. Name it: `schema-product`
4. Paste the entire content from `schema/schema-product.liquid` (from this audit package)

**The snippet is already prepared and production-ready. Key fixes built in:**

```liquid
{% comment %}
  HAPPIMESS — Product Schema (JSON-LD)
  Deploy: Add {% render 'schema-product' %} to sections/main-product.liquid
{% endcomment %}

<script type="application/ld+json">
{
  "@context": "https://schema.org",          ← no trailing slash
  "@type": "Product",
  "@id": "{{ shop.url }}/products/{{ product.handle }}#product",
  "name": "{{ product.title | escape }}",
  "url": "{{ shop.url }}/products/{{ product.handle }}",   ← absolute URL
  "description": "{{ product.description | strip_html | truncatewords: 100 | escape }}",
  "image": [
    {% for image in product.images limit: 5 %}
    "{{ image.src | img_url: 'master' }}"{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ],
  "brand": {
    "@type": "Brand",
    "name": "{{ shop.name }}",
    "@id": "https://happimess.com/#organization"
  },
  "sku": "{{ product.selected_or_first_available_variant.sku | default: product.id | escape }}",
  {% if product.metafields.reviews.rating.value != blank %}
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": {{ product.metafields.reviews.rating.value }},
    "reviewCount": {{ product.metafields.reviews.rating_count.value | default: 0 }},
    "bestRating": 5,
    "worstRating": 1
  },
  {% endif %}
  "offers": [
    {% for variant in product.variants %}
    {
      "@type": "Offer",
      "price": {{ variant.price | money_without_currency | remove: ',' }},
      "priceCurrency": "{{ cart.currency.iso_code }}",
      "availability": "{% if variant.available %}https://schema.org/InStock{% else %}https://schema.org/OutOfStock{% endif %}",
      "url": "{{ shop.url }}/products/{{ product.handle }}?variant={{ variant.id }}",
      "itemCondition": "https://schema.org/NewCondition",
      "seller": {
        "@type": "Organization",
        "@id": "https://happimess.com/#organization"
      },
      "shippingDetails": {
        "@type": "OfferShippingDetails",
        "shippingDestination": {
          "@type": "DefinedRegion",
          "addressCountry": "US"
        },
        "deliveryTime": {
          "@type": "ShippingDeliveryTime",
          "handlingTime": {
            "@type": "QuantitativeValue",
            "minValue": 1,
            "maxValue": 2,
            "unitCode": "d"
          },
          "transitTime": {
            "@type": "QuantitativeValue",
            "minValue": 3,
            "maxValue": 7,
            "unitCode": "d"
          }
        },
        "shippingRate": {
          "@type": "MonetaryAmount",
          "value": "0.00",
          "currency": "USD"
        }
      },
      "hasMerchantReturnPolicy": {
        "@type": "MerchantReturnPolicy",
        "applicableCountry": "US",
        "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
        "merchantReturnDays": 30,
        "returnMethod": "https://schema.org/ReturnByMail",
        "merchantReturnLink": "https://happimess.com/policies/refund-policy"
      }
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ]
}
</script>
```

**Step 2 — Include the snippet in the product template:**
1. Open `sections/main-product.liquid` (or `templates/product.liquid` in older themes)
2. Search for any existing `"@type": "Product"` JSON-LD block
3. **Remove the old Product schema block** (select from `<script type="application/ld+json">` to `</script>`)
4. Add at the bottom of the file, before the closing section tag:

```liquid
{% render 'schema-product' %}
```

**Step 3 — Prerequisite: Reviews app setup:**

The `AggregateRating` block only renders if `product.metafields.reviews.rating.value` is populated. This requires a reviews app:

| App | Cost | Metafield namespace |
|-----|------|---------------------|
| Judge.me | Free tier | `reviews.rating` and `reviews.rating_count` |
| Shopify Product Reviews | Free (native) | `reviews.rating` (check namespace in app settings) |
| Okendo | Paid | `reviews.rating` (configure namespace) |

If no reviews app is installed:
1. Go to Shopify App Store → search `Judge.me Product Reviews`
2. Install free tier
3. Enable auto-publishing of reviews from past orders
4. The `aggregateRating` block will appear automatically once reviews exist

If reviews exist but metafields aren't populated:
- In Judge.me: Settings → Widgets → "Sync to Schema.org" → Enable
- Verify with Shopify Admin → Products → [any product] → Metafields → look for `reviews.rating`

### Files To Edit
```
snippets/schema-product.liquid   (CREATE NEW — paste from audit package)
sections/main-product.liquid     (add {% render 'schema-product' %}, remove old schema)
```

### Validation Steps
1. [Google Rich Results Test](https://search.google.com/test/rich-results) → enter a product URL (e.g., `https://happimess.com/products/abrahamus-8-gallon-step-open-trash-can`)
2. Confirm: `@context` is `"https://schema.org"` (no trailing slash)
3. Confirm: `url` field is absolute (`https://happimess.com/products/...`)
4. If reviews app is configured: confirm `aggregateRating` block appears with numeric values
5. No errors on Rich Results Test

### Expected Result
- All 100+ product pages have valid Product schema
- Star ratings visible in Google SERPs (once AggregateRating is populated)
- Products eligible for Gemini Shopping surfaces
- Shipping and return policy structured in schema (merchant trust signals)

---

## FIX-10 — Deploy Collection Schema (Currently Zero Schema)

### Severity
**HIGH** (affects all collection pages — currently no schema)

### Problem
Collection pages (`/collections/trash-can`, `/collections/storage`, etc.) have **no schema markup whatsoever**. These are the pages AI systems surface for "best trash can" and "trash can comparison" queries — and they are completely invisible to structured data parsing.

### Why This Is Dangerous
- **AI product discovery queries blocked:** "Best trash can for kitchen" → AI looks for pages with CollectionPage or ItemList schema. Happimess collections have none → invisible.
- **Gemini Shopping gap:** Google Gemini uses ItemList schema to surface product sets in shopping queries. Zero collections schema = zero collection-level Gemini visibility.
- **Missed rich results:** CollectionPage + ItemList can generate product carousel rich results in SERPs — currently blocked by absent schema.
- **ChatGPT product research:** When users ask ChatGPT "show me trash cans under $50," it looks for structured product data. No schema on collection pages = no structured data to cite.

### Current Broken State
```
GET https://happimess.com/collections/trash-can
Schema present: NONE
```

### How To Fix

**Step 1 — Create the collection schema snippet:**
1. Shopify Admin → **Online Store → Themes → Edit code**
2. Under **Snippets**, click **"Add a new snippet"**
3. Name it: `schema-collection`
4. Paste the entire content from `schema/schema-collection.liquid` (from this audit package)

**The snippet content:**
```liquid
{% comment %}
  HAPPIMESS — CollectionPage + ItemList Schema
  Deploy: {% render 'schema-collection', collection: collection %}
{% endcomment %}

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "@id": "{{ shop.url }}/collections/{{ collection.handle }}#collectionpage",
  "name": "{{ collection.title | escape }}",
  "description": "{% if collection.description != blank %}{{ collection.description | strip_html | truncatewords: 60 | escape }}{% else %}Shop {{ collection.title }} at Happimess — modern home organization and storage solutions.{% endif %}",
  "url": "{{ shop.url }}/collections/{{ collection.handle }}",
  "publisher": {
    "@type": "Organization",
    "@id": "https://happimess.com/#organization"
  },
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "{{ shop.url }}"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "{{ collection.title | escape }}",
        "item": "{{ shop.url }}/collections/{{ collection.handle }}"
      }
    ]
  },
  "mainEntity": {
    "@type": "ItemList",
    "name": "{{ collection.title | escape }}",
    "numberOfItems": {{ collection.products_count }},
    "itemListElement": [
      {% for product in collection.products limit: 20 %}
      {
        "@type": "ListItem",
        "position": {{ forloop.index }},
        "url": "{{ shop.url }}/products/{{ product.handle }}",
        "name": "{{ product.title | escape }}",
        "item": {
          "@type": "Product",
          "name": "{{ product.title | escape }}",
          "url": "{{ shop.url }}/products/{{ product.handle }}",
          "image": "{% if product.featured_image %}{{ product.featured_image.src | img_url: 'master' }}{% endif %}",
          "description": "{{ product.description | strip_html | truncatewords: 30 | escape }}",
          "brand": {
            "@type": "Brand",
            "name": "Happimess"
          },
          "offers": {
            "@type": "Offer",
            "price": {{ product.price | money_without_currency | remove: ',' }},
            "priceCurrency": "{{ cart.currency.iso_code }}",
            "availability": "{% if product.available %}https://schema.org/InStock{% else %}https://schema.org/OutOfStock{% endif %}",
            "url": "{{ shop.url }}/products/{{ product.handle }}"
          }
        }
      }{% unless forloop.last %},{% endunless %}
      {% endfor %}
    ]
  }
}
</script>
```

**Step 2 — Include in the collection template:**
1. Open `sections/main-collection.liquid` (or `templates/collection.liquid`)
2. Add at the bottom before the closing tag:

```liquid
{% render 'schema-collection', collection: collection %}
```

### Files To Edit
```
snippets/schema-collection.liquid   (CREATE NEW — paste from audit package)
sections/main-collection.liquid     (add {% render 'schema-collection', collection: collection %})
```

### Validation Steps
1. [Google Rich Results Test](https://search.google.com/test/rich-results) → `https://happimess.com/collections/trash-can`
2. Should show CollectionPage schema with ItemList containing product names, URLs, and prices
3. No validation errors
4. Verify BreadcrumbList is present

### Expected Result
- All 6+ collection pages have CollectionPage + ItemList schema
- AI product discovery queries can surface Happimess collections
- Collection pages eligible for product carousel rich results in SERPs
- Gemini Shopping collection visibility enabled

---

## FIX-11 — Deploy Article Schema with speakable (Fixes Author 404 + Adds AI Readiness Signal)

### Severity
**HIGH** (affects all 26 blog posts)

### Problem
The existing Article schema has the broken author.url (fixed in Day 1 for the author page, but the schema template itself may still hardcode wrong values). The new template also adds the `speakable` property — a direct signal to AI assistants (Google Assistant, Alexa, Siri) that marks which passages are suitable for voice/AI reading.

### Why This Is Dangerous
- **Author URL:** Even with the author page created on Day 1, if the schema template generates the wrong URL, it's still broken. This fix ensures the template dynamically generates correct URLs from article data.
- **Missing speakable:** AI assistants that read content aloud use `speakable` to identify the key passage. Without it, assistants read arbitrary content.
- **Missing description uniqueness:** Current Article schema duplicates the headline as description — this is a quality signal Google flags.

### How To Fix

**Step 1 — Create the article schema snippet:**
1. Shopify Admin → **Online Store → Themes → Edit code**
2. Under **Snippets**, click **"Add a new snippet"**
3. Name it: `schema-article`
4. Paste the content from `schema/schema-article.liquid` (from this audit package)

**Key sections of the snippet:**

```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "{{ shop.url }}/blogs/{{ blog.handle }}/{{ article.handle }}#article",
  "headline": "{{ article.title | escape }}",
  "description": "{{ article.excerpt_or_content | strip_html | truncatewords: 40 | escape }}",
  "datePublished": "{{ article.published_at | date: '%Y-%m-%dT%H:%M:%S%z' }}",
  "dateModified": "{{ article.updated_at | date: '%Y-%m-%dT%H:%M:%S%z' }}",
  "author": {
    "@type": "Person",
    "name": "{{ article.author | default: 'Happimess Editorial Team' | escape }}",
    "url": "{{ shop.url }}/pages/{{ article.author | handle | default: 'our-team' }}",
    "jobTitle": "Home Organization Expert",
    "worksFor": {
      "@type": "Organization",
      "@id": "https://happimess.com/#organization"
    }
  },
  "publisher": {
    "@type": "Organization",
    "@id": "https://happimess.com/#organization",
    "name": "Happimess",
    "logo": {
      "@type": "ImageObject",
      "url": "https://cdn.shopify.com/s/files/1/0491/2909/5325/files/happimess-logo-ai-file_1.svg?v=1697698531"
    }
  },
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [
      "h1",
      "h2",
      ".article__content > p:first-of-type"
    ]
  }
}
</script>
```

**IMPORTANT — CSS selector verification:**
Before deploying, inspect a live blog post in Chrome DevTools to confirm the correct CSS class names. The selectors `article__content > p:first-of-type` are examples — replace with actual class names from the T4S theme:

1. Go to any blog post on the live site
2. Right-click the article body → Inspect
3. Find the wrapper class around the article content (e.g., `.article-template__content`, `.rte`, `.article-body`)
4. Replace the `cssSelector` array with confirmed class names:

```json
"speakable": {
  "@type": "SpeakableSpecification",
  "cssSelector": [
    "h1.article-template__hero-title",
    ".article-template__hero-description",
    ".article-template__content > p:first-child"
  ]
}
```

**Step 2 — Replace old Article schema in the article template:**
1. Open `sections/main-article.liquid` (or `templates/article.liquid`)
2. Search for existing `"@type": "Article"` or `"@type": "BlogPosting"` JSON-LD block
3. **Remove the old Article schema block**
4. Add at the bottom:

```liquid
{% render 'schema-article', article: article, blog: blog %}
```

**Step 3 — Update blog post author field:**
1. Shopify Admin → **Blog Posts**
2. For each post currently authored "From The Mess Experts": click Edit
3. Scroll to **Author** field
4. Change to: `Asodariya Sumi`
5. Save

This ensures `{{ article.author | handle }}` generates `asodariya-sumi` in the schema, pointing to the live author page created on Day 1.

### Files To Edit
```
snippets/schema-article.liquid    (CREATE NEW — paste from audit package + confirm CSS selectors)
sections/main-article.liquid      (add {% render 'schema-article' %}, remove old Article schema)
Shopify Admin → Blog Posts        (update Author field on all posts to "Asodariya Sumi")
```

### Validation Steps
1. [Google Rich Results Test](https://search.google.com/test/rich-results) → enter a blog post URL
2. Confirm `author.url` resolves without 404 (visit the URL directly)
3. Confirm `speakable.cssSelector` values match elements present in the page HTML
4. Confirm `datePublished` and `dateModified` are populated with real dates (not empty)
5. Confirm `description` is unique (not identical to headline)

### Expected Result
- All 26 blog posts have valid Article schema with live author URL
- `speakable` property signals AI assistant readiness
- Article E-E-A-T author signals active across entire blog
- Rich result eligibility for Article rich results restored

---

## FIX-12 — Add FAQPage Schema to Key Blog Posts

### Severity
**HIGH**

### Problem
Eight or more blog posts already have written FAQ sections. These questions and answers have zero structured data wrapping them. Google AI Overviews and Perplexity extract FAQPage schema explicitly — without it, the FAQ content is invisible to these surfaces even though the content exists.

### Priority Posts with FAQ Content

| Post URL | FAQ Items | Priority |
|----------|-----------|----------|
| `/blogs/news/standard-kitchen-trash-can-size` | 4 items | 1 (highest traffic) |
| `/blogs/news/best-dual-trash-can-for-kitchen-2026-guide-what-actually-works` | 5 items | 2 |
| `/blogs/news/the-guide-to-choosing-the-perfect-kitchen-trash-can` | 3+ items | 3 |
| `/blogs/news/trashcan-maintenance-tips-and-tricks-for-a-fresh-and-odor-free-bin` | 3+ items | 4 |

### How To Fix

**Option A — Individual blog post Additional Scripts (quickest, no code required):**
For each FAQ-containing blog post:
1. Shopify Admin → **Blog Posts → [select post]**
2. Look for **Additional Scripts** or **SEO** section in the post editor
3. If available, paste the FAQPage JSON-LD directly

**Option B — Theme conditional in article.liquid (scales to all posts):**

Add to `snippets/schema-article.liquid` or `sections/main-article.liquid`:

```liquid
{% comment %}FAQ schema — only renders if article has a metafield with FAQ data{% endcomment %}
{% if article.metafields.custom.faq_json != blank %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": {{ article.metafields.custom.faq_json.value }}
}
</script>
{% endif %}
```

Then in Shopify Admin → Blog Posts → [post] → Metafields → add `custom.faq_json` with the JSON array.

**Example FAQPage JSON for Standard Kitchen Trash Can Size post:**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the standard kitchen trash can size?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The standard kitchen trash can size is 10–13 gallons for most households. A 13-gallon can stands approximately 24 inches tall and fits standard kitchen trash bags."
      }
    },
    {
      "@type": "Question",
      "name": "What size trash can do I need for a small kitchen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a small kitchen or single-person household, a 4–8 gallon trash can is typically sufficient. This size fits under most counters and only needs to be emptied every 3–4 days."
      }
    },
    {
      "@type": "Question",
      "name": "How tall is a 13-gallon trash can?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A 13-gallon kitchen trash can typically stands 24–26 inches tall and has a diameter of approximately 11–13 inches. Height varies by model — step-open cans are slightly taller than push-lid designs due to the pedal mechanism."
      }
    },
    {
      "@type": "Question",
      "name": "What size trash bag fits a 13-gallon can?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A 13-gallon trash can uses 13-gallon or large kitchen trash bags. Brands like Glad, Hefty, and Simplehuman all make bags specifically sized for 13-gallon cans. Look for bags labeled 'tall kitchen' — these are designed for this size."
      }
    }
  ]
}
</script>
```

**Example FAQPage JSON for Best Dual Trash Can 2026 post:**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What size dual trash can do I need for my kitchen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For most kitchens, a dual-compartment trash can with a total capacity of 50–60 liters (approximately 13–16 gallons) works well. This provides roughly 30L for general waste and 20–25L for recycling — enough for a household of 2–4 people emptying every 2–3 days."
      }
    },
    {
      "@type": "Question",
      "name": "Are dual trash cans worth it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, dual-compartment trash cans are worth it if your household recycles regularly. They eliminate the need for a second standalone bin, reduce cross-contamination between waste and recycling, and create a single point of waste management at the kitchen counter."
      }
    },
    {
      "@type": "Question",
      "name": "What is the best dual trash can for a small kitchen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a small kitchen, look for a slim dual-compartment design with a total capacity of 30–40 liters. Side-by-side configurations with a narrow footprint (under 14 inches wide) work best in tight spaces. Step-open or push-lid mechanisms are preferred over sensor lids to minimize size."
      }
    }
  ]
}
</script>
```

### Files To Edit
```
For each blog post — one of:
  A: Shopify Admin → Blog Posts → [post] → Additional Scripts
  B: snippets/schema-article.liquid (add metafield conditional)
  C: theme.liquid (add page.handle conditionals for each specific post)
```

### Validation Steps
1. [Google Rich Results Test](https://search.google.com/test/rich-results) → standard-kitchen-trash-can-size post
2. FAQPage rich result should appear (Google Note: FAQPage rich results restricted to health/gov since Aug 2023 for general results, but schema still has strong AI semantic value)
3. Check that questions and answers match the page content exactly

### Expected Result
- FAQ content structured for AI extraction on 4+ blog posts
- Google AIO and Perplexity can extract specific Q&A pairs for user queries
- FAQ schema feeds AI assistant knowledge for trash can sizing queries

---

## Day 3 Completion Checklist

```
[ ] snippets/schema-product.liquid created with production-ready template
[ ] sections/main-product.liquid includes {% render 'schema-product' %}
[ ] Old Product JSON-LD block removed from product template
[ ] Google Rich Results Test → product page → no errors, absolute URL, no trailing slash
[ ] snippets/schema-collection.liquid created
[ ] sections/main-collection.liquid includes {% render 'schema-collection' %}
[ ] Google Rich Results Test → /collections/trash-can → CollectionPage + ItemList present
[ ] snippets/schema-article.liquid created with confirmed CSS selectors for speakable
[ ] sections/main-article.liquid includes {% render 'schema-article' %}
[ ] Old Article JSON-LD block removed from article template
[ ] All blog posts author updated from "From The Mess Experts" to "Asodariya Sumi"
[ ] Google Rich Results Test → blog post → author.url resolves, speakable present
[ ] FAQPage JSON-LD added to standard-kitchen-trash-can-size post
[ ] FAQPage JSON-LD added to best-dual-trash-can-2026 post
[ ] Reviews app installed and configured (Judge.me or equivalent)
```

---

## Day 3 Score Impact Projection

| Category | After Day 2 | After Day 3 |
|----------|-------------|-------------|
| Structured Data | 62/100 | 75/100 (+13) |
| Content Quality / E-E-A-T | 44/100 | 50/100 (+6) |
| Platform Optimization | 50/100 | 55/100 (+5) |
| **Composite GEO Score** | **~54/100** | **~60/100** |
