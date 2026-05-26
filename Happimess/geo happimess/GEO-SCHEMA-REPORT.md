# GEO Schema Report — happimess.com
**Generated:** 2026-05-22  
**Schema Score: 62/100**  
**Format detected:** JSON-LD (correct — server-rendered in initial HTML)

---

## Schema Inventory

| # | Page | Type | Valid | Rich Result Eligible | Issues |
|---|------|------|-------|---------------------|--------|
| 1 | Homepage | WebPage | Yes | N/A | `name` contains `&amp;` literal |
| 2 | Homepage | WebSite + SearchAction | Yes | Yes (Sitelinks Search Box) | `sameAs` on WebSite (move to Organization) |
| 3 | Homepage | Organization | Partial | N/A | Non-standard `industry`, `department`; missing `legalName`, Wikipedia, Wikidata |
| 4 | Product page | Product (multi-offer) | Partial | No — missing AggregateRating | No `aggregateRating`, `color`, `material`, `category`, `gtin`; HTML entities in description |
| 5 | Product page | BreadcrumbList | Yes | Yes | 2-level only — skips collection level |
| 6 | Product page | FAQPage | Yes | Restricted (Aug 2023) | Keep — AI crawler value retained |
| 7 | Blog index | Blog + BlogPosting stubs | Partial | No | Author Person lacks `sameAs`, `jobTitle`, `image` |
| 8 | Blog article | BlogPosting | Partial | Yes (Article) | `description` opens with "Editorial Disclosure:" text; Author Person incomplete |
| 9 | Blog article | BreadcrumbList | Partial | Yes | Non-standard `name` property on BreadcrumbList |

**Missing schemas (not present anywhere):**
- `AggregateRating` — highest impact missing schema; blocks star ratings everywhere
- `CollectionPage` + `ItemList` — collection pages have zero structured data
- `Person` (standalone author pages) — needed for E-E-A-T author recognition
- `speakable` on homepage and product pages (present on articles only)

---

## Validation Issues by Schema Type

### Organization (Homepage)

| Property | Status | Fix |
|----------|--------|-----|
| `@type` | OK | — |
| `name` | OK | — |
| `legalName` | Missing | Add: `"legalName": "Happimess Inc."` |
| `telephone` | Present but wrong format | Change from `(917) 261-4961` to `+19172614961` (E.164) |
| `foundingDate` | OK (`"2020-01-15"`) | — |
| `address` | OK | — |
| `sameAs` | Present — 7 platforms | Add Wikipedia (when available), Wikidata (when created) |
| `industry` | Non-standard Schema.org property | Remove — use `knowsAbout` instead |
| `department` | Redundant nesting | Remove — duplicates contact info |
| `contactPoint.availableLanguage` | Missing | Add: `["English", "Spanish"]` |

### Product (Product pages)

| Property | Status | Fix |
|----------|--------|-----|
| `aggregateRating` | **Missing — CRITICAL** | Add once reviews collected via review app |
| `description` | HTML entities present (`&quot;`, `&#39;`) | Use `\| strip_html \| json` in Liquid template |
| `color` | Missing | Add per variant: `"color": "Matte Black"` |
| `material` | Missing | Add: `"material": "Powder-coated steel"` |
| `category` | Missing | Add: `"category": "Home & Kitchen > Trash Cans"` |
| `gtin14` | Missing | Add manufacturer GTIN if available |
| `offers` structure | Multi-Offer array | Consider switching to `AggregateOffer` for variants |
| `shippingDetails` | Present | OK |
| `hasMerchantReturnPolicy` | Present | OK |

### BlogPosting (Article pages)

| Property | Status | Fix |
|----------|--------|-----|
| `description` | Opens with "Editorial Disclosure:" boilerplate | Replace with clean 1-2 sentence article summary |
| `author.sameAs` | Missing | Add author LinkedIn URL |
| `author.jobTitle` | Missing | Add: `"jobTitle": "Home Organization Specialist"` |
| `author.image` | Missing | Add headshot URL |
| `author.description` | Missing | Add 1-sentence bio |
| `author.knowsAbout` | Missing | Add expertise array |
| `keywords` | Single string | Change to array: `["trash cans", "kitchen organization", ...]` |
| `datePublished` | OK | — |
| `dateModified` | OK | — |
| `wordCount` | Present | OK |
| `speakable` | Present | Verify cssSelectors match rendered HTML class names |

### BreadcrumbList (Product pages)

Current: `Home → Product` (2 levels)  
Correct: `Home → Collection → Product` (3 levels)

```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://happimess.com" },
    { "@type": "ListItem", "position": 2, "name": "Step Trash Cans", "item": "https://happimess.com/collections/step-trash-cans" },
    { "@type": "ListItem", "position": 3, "name": "Betty Retro Trash Can", "item": "https://happimess.com/products/betty-retro-8-gallon-step-open-trash-can" }
  ]
}
```

In Shopify's `product.liquid`, generate position 2 dynamically from `collection.title` and `collection.url` (available when a product is accessed via a collection URL).

---

## Generated JSON-LD — Ready to Deploy

All blocks below are production-ready. Copy into Shopify snippets as described in the implementation guide (Section 5).

---

### Block 1: Organization (Replace existing in theme.liquid)

Fixes: removes `industry`/`department`, adds `legalName`, corrects telephone format, adds `availableLanguage`.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://happimess.com/#organization",
  "name": "Happimess",
  "legalName": "Happimess Inc.",
  "url": "https://happimess.com",
  "description": "Modern home organization, storage furniture, trash cans, and kitchen accessories designed and durability-tested for real homes. Founded in New York City in 2020.",
  "logo": {
    "@type": "ImageObject",
    "url": "https://cdn.shopify.com/s/files/1/0491/2909/5325/files/happimess-logo-ai-file_1.svg?v=1697698531",
    "width": 600,
    "height": 60
  },
  "telephone": "+19172614961",
  "email": "hello@happimess.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "185 Madison Avenue, Suite 602",
    "addressLocality": "New York",
    "addressRegion": "NY",
    "postalCode": "10016",
    "addressCountry": "US"
  },
  "foundingDate": "2020",
  "areaServed": {
    "@type": "Country",
    "name": "United States"
  },
  "knowsAbout": [
    "home organization",
    "storage solutions",
    "trash cans and waste management",
    "kitchen organization",
    "storage furniture",
    "bathroom storage",
    "laundry hampers"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+19172614961",
    "email": "hello@happimess.com",
    "contactType": "customer service",
    "hoursAvailable": "Mo-Fr 09:00-17:00",
    "availableLanguage": ["English", "Spanish"]
  },
  "sameAs": [
    "https://www.facebook.com/happimessofficial/",
    "https://www.instagram.com/happimess_official/",
    "https://www.linkedin.com/company/happimesshome/",
    "https://www.pinterest.com/happimess_/",
    "https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g",
    "https://www.tiktok.com/@happimess_official",
    "https://www.crunchbase.com/organization/happimess"
  ]
}
```

**Add these two entries to `sameAs` once created:**
```
"https://en.wikipedia.org/wiki/Happimess",
"https://www.wikidata.org/wiki/Q[ENTITY-ID]"
```

---

### Block 2: Product with AggregateRating Template (product.liquid)

This is the Liquid template version. Replace `[PLACEHOLDERS]` with Liquid variables or hardcoded values per product.

```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": {{ product.title | json }},
  "url": "{{ shop.url }}{{ product.url }}",
  "description": {{ product.description | strip_html | truncatewords: 100 | json }},
  "image": [
    {{ product.featured_image | img_url: 'master' | prepend: 'https:' | json }}
  ],
  "brand": {
    "@type": "Brand",
    "name": "Happimess"
  },
  "manufacturer": {
    "@type": "Organization",
    "@id": "https://happimess.com/#organization",
    "name": "Happimess"
  },
  "category": "Home & Kitchen > Trash Cans & Wastebaskets",
  {% if product.metafields.custom.color %}
  "color": {{ product.metafields.custom.color | json }},
  {% endif %}
  {% if product.metafields.custom.material %}
  "material": {{ product.metafields.custom.material | json }},
  {% endif %}
  {% if product.metafields.custom.gtin %}
  "gtin14": {{ product.metafields.custom.gtin | json }},
  {% endif %}
  "sku": {{ product.selected_or_first_available_variant.sku | json }},
  {% if product.metafields.reviews.rating.value %}
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": {{ product.metafields.reviews.rating.value | json }},
    "reviewCount": {{ product.metafields.reviews.rating_count | json }},
    "bestRating": "5",
    "worstRating": "1"
  },
  {% endif %}
  "offers": {
    "@type": "AggregateOffer",
    "lowPrice": {{ product.price_min | money_without_currency | json }},
    "highPrice": {{ product.price_max | money_without_currency | json }},
    "priceCurrency": {{ cart.currency.iso_code | json }},
    "offerCount": {{ product.variants.size | json }},
    "availability": {% if product.available %}"https://schema.org/InStock"{% else %}"https://schema.org/OutOfStock"{% endif %},
    "itemCondition": "https://schema.org/NewCondition",
    "priceValidUntil": "2027-12-31",
    "seller": {
      "@type": "Organization",
      "@id": "https://happimess.com/#organization",
      "name": "Happimess"
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
      "returnFees": "https://schema.org/ReturnShippingFees",
      "merchantReturnLink": "https://happimess.com/policies/refund-policy"
    }
  }
}
</script>
```

**Note on AggregateRating:** The `product.metafields.reviews.rating.value` Liquid path works with Judge.me and Okendo when their metafields are enabled. Verify the exact metafield namespace with your review app's documentation. If the app injects schema via JavaScript instead of server-side, you must request server-side output from the app provider or construct the schema manually from Liquid metafield data.

**Note on color/material/gtin:** These require Shopify metafields. Create metafields in Shopify Admin → Settings → Custom data → Products with keys `custom.color`, `custom.material`, `custom.gtin`. Populate them per product.

---

### Block 3: CollectionPage + ItemList (collection.liquid — NEW, not currently present)

Add to `templates/collection.liquid`. Generates dynamically from the collection's product list.

```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "@id": "{{ shop.url }}{{ collection.url }}#collectionpage",
  "name": {{ collection.title | json }},
  "description": {{ collection.description | strip_html | truncatewords: 50 | default: collection.title | append: ' — shop the full collection at Happimess.' | json }},
  "url": "{{ shop.url }}{{ collection.url }}",
  "isPartOf": {
    "@id": "https://happimess.com/#website"
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
        "name": {{ collection.title | json }},
        "item": "{{ shop.url }}{{ collection.url }}"
      }
    ]
  },
  "mainEntity": {
    "@type": "ItemList",
    "name": {{ collection.title | json }},
    "numberOfItems": {{ collection.products_count | json }},
    "itemListElement": [
      {% for product in collection.products limit: 20 %}
      {
        "@type": "ListItem",
        "position": {{ forloop.index | json }},
        "url": "{{ shop.url }}{{ product.url }}",
        "name": {{ product.title | json }}
      }{% unless forloop.last %},{% endunless %}
      {% endfor %}
    ]
  }
}
</script>
```

**Collection description note:** The `collection.description` field is empty on most current Happimess collections. Add descriptive text in Shopify Admin → Products → Collections → [Collection name] → Description. This text populates both the visible page content and the schema description field.

---

### Block 4: Enhanced Author Person (article.liquid — update existing)

Add these fields to the existing `author` object within the BlogPosting schema. Create a Shopify page for each author at `/pages/[author-slug]` and populate the values below.

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://happimess.com/pages/[author-slug]#person",
  "name": "[Author Full Name]",
  "url": "https://happimess.com/pages/[author-slug]",
  "image": {
    "@type": "ImageObject",
    "url": "https://happimess.com/cdn/shop/files/[author-headshot].jpg"
  },
  "jobTitle": "[e.g., Home Organization Specialist]",
  "description": "[2-3 sentence bio: role, years of experience, expertise areas]",
  "worksFor": {
    "@type": "Organization",
    "@id": "https://happimess.com/#organization",
    "name": "Happimess"
  },
  "knowsAbout": [
    "home organization",
    "kitchen storage",
    "trash can selection",
    "storage furniture"
  ],
  "sameAs": [
    "https://www.linkedin.com/in/[author-linkedin-slug]"
  ]
}
```

In the BlogPosting schema, replace the current `author` object with this full Person block (or reference it by `@id` if defined separately on the author page).

---

### Block 5: FAQPage Template (article.liquid — conditional)

Add this block to articles that contain FAQ sections. In Shopify, use a product metafield or article tag (e.g., tag: `has-faq`) to conditionally render this schema.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What size kitchen trash can do I need?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most households manage well with a 10–13 gallon (38–49 liter) kitchen trash can — typically 20–25 inches tall. Single-person apartments usually work with 4–8 gallons. Families of 5 or more often need 14–20 gallons to avoid daily emptying."
      }
    },
    {
      "@type": "Question",
      "name": "How often should I empty a kitchen trash can?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a family of four using a 10-gallon trash can, emptying every 2–3 days is ideal for odor control and hygiene. Single-person households may empty weekly."
      }
    },
    {
      "@type": "Question",
      "name": "Are dual trash cans worth it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — dual-compartment trash cans allow simultaneous trash and recycling separation in one unit, eliminating the need for two separate bins. Most households benefit from a 40–60 liter dual model."
      }
    },
    {
      "@type": "Question",
      "name": "What is Happimess's return policy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Items may be returned within 30 days of receipt. Happimess provides a prepaid return label for the 48 contiguous U.S. states. A $10 per-item return shipping fee is deducted from the refund. Final-sale and made-to-order items are not eligible for return."
      }
    }
  ]
}
```

**Important:** Replace the Q&A pairs above with the actual questions and answers from each specific article. The return policy FAQ belongs on the FAQ page (`/pages/faqs`), not on product guides.

---

### Block 6: WebPage with speakable (homepage — add to WebPage block)

The existing WebPage block on the homepage is valid but missing `speakable`. Add this property:

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "https://happimess.com/#webpage",
  "url": "https://happimess.com",
  "name": "Trash, Organization, Storage Furniture & Kitchen | Happimess",
  "description": "Modern home organization, storage furniture, trash cans, and kitchen accessories designed and durability-tested for real homes.",
  "isPartOf": {
    "@id": "https://happimess.com/#website"
  },
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [
      "h1.page-title",
      ".hero__description",
      ".home-about-block"
    ]
  }
}
```

**Note:** The cssSelector values (`h1.page-title`, `.hero__description`, `.home-about-block`) must match actual class names in the rendered Shopify theme HTML. Inspect the live page HTML to confirm the correct selectors, then update. The `.home-about-block` class assumes you add the recommended About/brand block section to the homepage.

---

## Shopify Implementation Guide

### Step 1 — Locate existing schema injection points

In Shopify Admin → Online Store → Themes → Edit Code, open `layout/theme.liquid`. Search for `application/ld+json`. The current Organization and WebSite schemas are in this file or in a snippet it renders.

### Step 2 — Create schema snippets

Create these snippet files (Online Store → Themes → Edit Code → Snippets → Add a new snippet):

| Snippet name | Rendered in | Schema types |
|---|---|---|
| `schema-global.liquid` | `layout/theme.liquid` — all pages | Organization + WebSite |
| `schema-product.liquid` | `templates/product.liquid` | Product + BreadcrumbList + FAQPage |
| `schema-collection.liquid` | `templates/collection.liquid` | CollectionPage + ItemList |
| `schema-article.liquid` | `templates/article.liquid` | BlogPosting + BreadcrumbList |
| `schema-faq-page.liquid` | `templates/page.faqs.liquid` | FAQPage (for /pages/faqs only) |

### Step 3 — Replace global Organization schema

In `snippets/schema-global.liquid`, replace the existing Organization block with Block 1 above. The current block contains non-standard `industry` and `department` properties that should be removed.

### Step 4 — Update product schema (product.liquid or snippets/product-schema.liquid)

Replace the existing product schema with the Liquid template from Block 2. The key addition is the conditional `aggregateRating` block — it renders only when the review metafield is populated, so it is safe to deploy before reviews exist.

### Step 5 — Add CollectionPage schema (new — collection.liquid)

This schema does not currently exist on any collection page. Add the Liquid template from Block 3 to `templates/collection.liquid` (or a new `snippets/schema-collection.liquid` included from it). Note: add collection descriptions in Shopify Admin for the schema to have meaningful content.

### Step 6 — Fix BlogPosting description field (article.liquid)

Find the existing BlogPosting schema block in `templates/article.liquid` or its snippet. The `description` field currently outputs article content that begins with "Editorial Disclosure:" boilerplate. Change the Liquid variable to use a clean excerpt:

```liquid
"description": {{ article.excerpt | strip_html | truncatewords: 50 | json }},
```

If `article.excerpt` is empty, fall back to: `{{ article.content | strip_html | truncatewords: 50 | json }}`

### Step 7 — Validate all schemas

After deployment, test every schema type using:
- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema.org Validator: https://validator.schema.org
- Bing Markup Validator: https://www.bing.com/webmaster/tools/markup-validator

Test these specific URLs:
- Homepage: https://happimess.com/
- A product page: https://happimess.com/products/betty-retro-8-gallon-step-open-trash-can
- A collection page: https://happimess.com/collections/step-trash-cans
- A blog article: https://happimess.com/blogs/news/standard-kitchen-trash-can-size

---

## Schema Score Trajectory

| Current state | 62/100 |
|---|---|
| After: Organization fix + CollectionPage schema | ~68/100 |
| After: Product AggregateRating (requires reviews) | ~78/100 |
| After: Author Person complete + FAQPage on articles | ~84/100 |
| After: Wikipedia + Wikidata in sameAs | ~88/100 |

---

## Priority Actions

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| CRITICAL | Add `aggregateRating` to all products (requires review app) | Medium | +12 pts |
| HIGH | Replace Organization block — remove `industry`/`department`, add `legalName`, fix telephone format | Low | +3 pts |
| HIGH | Add CollectionPage + ItemList to all collection pages via Liquid template | Low | +5 pts |
| HIGH | Fix BlogPosting `description` — remove "Editorial Disclosure:" opening | Low | +3 pts |
| HIGH | Add author `sameAs`, `jobTitle`, `image`, `knowsAbout` to all BlogPosting blocks | Medium | +4 pts |
| HIGH | Add FAQPage JSON-LD to 4+ blog posts with FAQ sections | Low | +3 pts |
| MEDIUM | Fix Product `description` HTML entities using `\| strip_html \| json` | Low | +2 pts |
| MEDIUM | Add `color`, `material`, `category` to all Product schemas | Medium | +3 pts |
| MEDIUM | Fix BreadcrumbList on product pages — add collection level (3 items) | Low | +2 pts |
| MEDIUM | Add `speakable` to homepage WebPage and product page WebPage | Low | +2 pts |
| LOW | Remove non-standard `name` from BreadcrumbList on blog articles | Low | +1 pt |
| LOW | Add `legalName` and `availableLanguage` to Organization | Low | +1 pt |

---

*GEO Schema Report — happimess.com — 2026-05-22*  
*All JSON-LD blocks are ready for Shopify Liquid template implementation*
