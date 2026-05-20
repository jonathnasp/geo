# GEO Schema Report — Happimess
**Domain:** happimess.com  
**Date:** 2026-05-20  
**Data source:** Schema subagent + Technical subagent (full audit 2026-05-20)

---

## Structured Data Score: 46/100 (Poor)

> Down from 62/100 on May 18 — score revised conservatively because product and article schemas could not be verified (404 on test product URL). The homepage Organization schema is solid. Everything else — BlogPosting, Product, FAQPage, Person, BreadcrumbList, speakable — is either absent or unverified. All missing schemas have ready-to-deploy Liquid templates below.

### Score Breakdown

| Schema | Points Available | Points Earned | Notes |
|--------|-----------------|---------------|-------|
| Organization + sameAs | 20 | 15 | Present; missing Wikipedia, Wikidata, Crunchbase |
| Article / BlogPosting | 15 | 3 | Unverified — possible admin username issues unresolved |
| Person (author) | 15 | 0 | Not confirmed present |
| sameAs completeness | 15 | 10 | 6/9 authority platforms present |
| speakable | 10 | 0 | Absent sitewide |
| BreadcrumbList | 5 | 0 | Absent sitewide |
| WebSite + SearchAction | 5 | 5 | Valid and complete |
| No deprecated schemas | 5 | 5 | None detected |
| JSON-LD format | 5 | 5 | Correct format throughout |
| Validation (no errors) | 5 | 3 | HTML-encoded ampersand in WebPage name |
| **Total** | **100** | **46** | |

---

## Confirmed Present Schemas (Homepage)

### ✅ Schema 1: Organization

**Status:** Good — missing 3 high-authority sameAs platforms

```json
{
  "@type": "Organization",
  "@id": "https://happimess.com/#organization",
  "name": "Happimess",
  "url": "https://happimess.com",
  "description": "[populated]",
  "logo": {"@type": "ImageObject", "url": "[CDN URL]"},
  "telephone": "(917) 261-4961",
  "email": "hello@happimess.com",
  "address": {"@type": "PostalAddress", "streetAddress": "185 Madison Ave", "addressLocality": "New York", "addressRegion": "NY", "postalCode": "10016", "addressCountry": "US"},
  "foundingDate": "2020-01-15",
  "contactPoint": {...},
  "knowsAbout": ["home organization", "storage solutions", ...],
  "areaServed": {"@type": "Country", "name": "United States"},
  "sameAs": [
    "https://www.facebook.com/happimessofficial/",
    "https://www.instagram.com/happimess_official/",
    "https://www.linkedin.com/company/happimesshome/",
    "https://www.pinterest.com/happimess_/",
    "https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g",
    "https://www.tiktok.com/@happimess_official"
  ]
}
```

**Missing sameAs entries to add** (once profiles are created):
```json
"https://twitter.com/happimess_official",
"https://www.crunchbase.com/organization/happimess",
"https://www.wikidata.org/wiki/Q[NUMBER]"
```

### ✅ Schema 2: WebSite + SearchAction

**Status:** Valid — Sitelinks Search Box eligible

```json
{
  "@type": "WebSite",
  "@id": "https://happimess.com/#website",
  "url": "https://happimess.com",
  "name": "Happimess",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {"@type": "EntryPoint", "urlTemplate": "https://happimess.com/search?q={search_term_string}"},
    "query-input": "required name=search_term_string"
  }
}
```

### ⚠️ Schema 3: WebPage (Minor Issues)

**Issue 1:** `name` contains HTML-encoded ampersand: `"Storage Furniture &amp; Kitchen"` should be `"Storage Furniture & Kitchen"`

**Fix in theme.liquid** — find the WebPage schema name property and add a replace filter:
```liquid
"name": "{{ page_title | replace: '&amp;', '&' | escape }}"
```

**Issue 2:** Missing `speakable`, `breadcrumb`, `primaryImageOfPage` — see templates below.

---

## Missing Schemas — Production-Ready Templates

### Template 1: BlogPosting (article.liquid)

**Where to add:** Shopify Admin → Online Store → Themes → Edit Code → `templates/article.liquid` or `sections/article-template.liquid`

Add this `<script>` block inside the `{% block content %}` or at the bottom of the template before `{% endblock %}`:

```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": {{ article.title | json }},
  "description": {{ article.excerpt_or_content | strip_html | strip_newlines | truncate: 200 | json }},
  "url": "{{ shop.url }}/blogs/{{ blog.handle }}/{{ article.handle }}",
  "datePublished": "{{ article.published_at | date: '%Y-%m-%dT%H:%M:%S%z' }}",
  "dateModified": "{{ article.updated_at | date: '%Y-%m-%dT%H:%M:%S%z' }}",
  "wordCount": {{ article.content | strip_html | split: ' ' | size }},
  "image": {
    "@type": "ImageObject",
    "url": "{% if article.image %}{{ article.image.src | img_url: 'master' }}{% else %}https://cdn.shopify.com/s/files/1/0491/2909/5325/files/happimess-logo-ai-file_1.svg?v=1697698531{% endif %}"
  },
  "author": {
    "@type": "Person",
    "name": {% assign display_name = article.metafields.custom.author_display_name %}{% if display_name %}{{ display_name | json }}{% else %}"Happimess Editorial Team"{% endif %},
    "url": "https://happimess.com/pages/about-us",
    "worksFor": {
      "@type": "Organization",
      "name": "Happimess",
      "@id": "https://happimess.com/#organization"
    }
  },
  "publisher": {
    "@type": "Organization",
    "name": "Happimess",
    "@id": "https://happimess.com/#organization",
    "logo": {
      "@type": "ImageObject",
      "url": "https://cdn.shopify.com/s/files/1/0491/2909/5325/files/happimess-logo-ai-file_1.svg?v=1697698531",
      "width": 600,
      "height": 60
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{ shop.url }}/blogs/{{ blog.handle }}/{{ article.handle }}"
  },
  "articleSection": {{ blog.title | json }},
  "inLanguage": "en-US",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": ["h1.article__title", ".article__body > p:first-of-type", ".article__body h2"]
  }
}
</script>
```

**Important notes:**
- `article.excerpt_or_content` — use `article.excerpt` if populated, else fallback to content
- Do NOT use `{{ article.author }}` — this outputs the Shopify admin account name (e.g., "jonathany 2123"). Use the metafield approach above.
- The `speakable` CSS selectors depend on your theme's actual class names — verify against your theme's article template HTML
- The logo CDN URL is confirmed from the homepage schema — update if it changes

---

### Template 2: FAQPage (page.faqs.liquid)

**Where to add:** Shopify Admin → Online Store → Themes → Edit Code → create `templates/page.faqs.json` or find the existing FAQ page template

If no custom FAQ template exists, create one:
1. Go to **Templates** in theme editor
2. Create new template: `page.faqs`
3. Add the JSON-LD script block to it
4. Assign the `/pages/faqs` page to use this template

```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When will my order ship?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Orders that are in-stock ship within 1-2 business days (Monday-Friday). You will receive a tracking confirmation email when your order ships."
      }
    },
    {
      "@type": "Question",
      "name": "I signed up for the welcome email but didn't receive my promo code. What should I do?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The promo code is sent immediately upon signup, but email providers may delay delivery by up to an hour. Check your spam or junk folder if you don't see it within an hour."
      }
    },
    {
      "@type": "Question",
      "name": "I need to make a change to my order. How do I do that?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Post-purchase modifications are not possible once an order is placed. You may request a return label and repurchase the preferred item or configuration."
      }
    },
    {
      "@type": "Question",
      "name": "What is your return policy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Eligible items can be returned within 30 days of receiving your purchase. A $10 per-item return shipping fee applies. Original shipping costs are not refunded. Final sale and made-to-order items are excluded from returns."
      }
    },
    {
      "@type": "Question",
      "name": "My tracking number isn't working. What should I do?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Allow 2-3 business days for tracking updates to appear after receiving your tracking number. Shipping labels are generated before the order leaves the warehouse, so there may be a brief delay before the carrier activates tracking."
      }
    },
    {
      "@type": "Question",
      "name": "What is the wait time for items on the waitlist?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Each product has its own individual restock timeline. Joining the waitlist will trigger an automatic email notification when the item becomes available again."
      }
    },
    {
      "@type": "Question",
      "name": "Do you ship internationally or to Hawaii and Alaska?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Currently we only ship to the 48 contiguous United States. We do not currently ship internationally or to Hawaii and Alaska, though we plan to expand in the future."
      }
    },
    {
      "@type": "Question",
      "name": "Can I cancel or alter my order once I place it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Once placed, orders go immediately to the warehouse for processing. Modifications or cancellations are not possible after an order is placed."
      }
    }
  ]
}
</script>
```

**Note on FAQPage rich results:** Google restricted FAQPage rich results to government and health sites in August 2023. This schema will NOT generate the accordion-style FAQ rich result in Google SERPs for Happimess. However, it still provides:
- Semantic Q&A structure that AI systems (ChatGPT, Perplexity, Claude) use for content understanding
- Answer extraction signals for Google AI Overviews
- Bing Copilot structured response generation

**Implement it regardless** — the AI citability benefit is real even without the visual rich result.

---

### Template 3: Product Schema (product.liquid)

**Where to add:** Shopify Admin → Online Store → Themes → Edit Code → `templates/product.liquid` or `sections/product-template.liquid`, or a dedicated snippet `snippets/json-ld-product.liquid` (included with `{% render 'json-ld-product' %}`)

```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": {{ product.title | json }},
  "description": {{ product.description | strip_html | strip_newlines | truncate: 500 | json }},
  "url": "{{ shop.url }}{{ product.url }}",
  "sku": {{ product.selected_or_first_available_variant.sku | json }},
  "mpn": {{ product.selected_or_first_available_variant.barcode | json }},
  "brand": {
    "@type": "Brand",
    "name": "Happimess"
  },
  "image": [
    {% for image in product.images limit: 5 %}
      {{ image.src | img_url: 'master' | json }}{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ],
  "offers": {
    "@type": "Offer",
    "url": "{{ shop.url }}{{ product.url }}",
    "priceCurrency": "USD",
    "price": "{{ product.selected_or_first_available_variant.price | money_without_currency }}",
    "priceValidUntil": "{{ 'now' | date: '%Y' | plus: 1 }}-12-31",
    "availability": "{% if product.available %}https://schema.org/InStock{% else %}https://schema.org/OutOfStock{% endif %}",
    "itemCondition": "https://schema.org/NewCondition",
    "seller": {
      "@type": "Organization",
      "name": "Happimess",
      "@id": "https://happimess.com/#organization"
    },
    "shippingDetails": {
      "@type": "OfferShippingDetails",
      "shippingRate": {
        "@type": "MonetaryAmount",
        "value": "0",
        "currency": "USD"
      },
      "deliveryTime": {
        "@type": "ShippingDeliveryTime",
        "businessDays": {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        },
        "handlingTime": {
          "@type": "QuantitativeValue",
          "minValue": 1,
          "maxValue": 2,
          "unitCode": "DAY"
        }
      }
    }
  }{% assign review_count = product.metafields.reviews.rating_count.value | plus: 0 %}{% if review_count > 0 %},
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "{{ product.metafields.reviews.rating.value }}",
    "reviewCount": "{{ product.metafields.reviews.rating_count.value }}",
    "bestRating": "5",
    "worstRating": "1"
  }{% endif %}
}
</script>
```

**Critical fix embedded:** `"brand": {"@type": "Brand", "name": "Happimess"}` — this hardcodes "Happimess" instead of using `{{ product.vendor }}` (which outputs "Happimess Dev" for products where the vendor was set to the dev account name).

**aggregateRating note:** The metafield namespaces `reviews.rating.value` and `reviews.rating_count.value` are for Judge.me. If using a different reviews app:
- **Yotpo:** `yotpo.reviews_average` and `yotpo.reviews_count`
- **Okendo:** `okendo.reviews_average_rating` and `okendo.reviews_count`
- **Loox:** Check Loox documentation for metafield keys
- **Shopify Product Reviews (legacy):** `reviews.rating` and `reviews.rating_count`

Replace the metafield keys with the correct ones for your installed reviews app before deploying.

---

### Template 4: BreadcrumbList (product + article + collection pages)

**Where to add:** Conditional blocks in `theme.liquid` or page-specific templates. Use Liquid `{% if template == 'product' %}` etc.

**For product pages:**
```liquid
{% if template == 'product' %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "{{ shop.url }}/"
    }{% if collection %},{
      "@type": "ListItem",
      "position": 2,
      "name": {{ collection.title | json }},
      "item": "{{ shop.url }}{{ collection.url }}"
    },{
      "@type": "ListItem",
      "position": 3,
      "name": {{ product.title | json }},
      "item": "{{ shop.url }}{{ product.url }}"
    }{% else %},{
      "@type": "ListItem",
      "position": 2,
      "name": {{ product.title | json }},
      "item": "{{ shop.url }}{{ product.url }}"
    }{% endif %}
  ]
}
</script>
{% endif %}
```

**For blog article pages:**
```liquid
{% if template == 'article' %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "{{ shop.url }}/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": {{ blog.title | json }},
      "item": "{{ shop.url }}/blogs/{{ blog.handle }}"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": {{ article.title | json }},
      "item": "{{ shop.url }}/blogs/{{ blog.handle }}/{{ article.handle }}"
    }
  ]
}
</script>
{% endif %}
```

---

### Template 5: Person Schema (author bio page)

**Where to add:** Create a new page template `templates/page.author.json` and assign it to any author bio pages created at `/pages/author-[name]`

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "REPLACE: Author Full Name",
  "url": "https://happimess.com/pages/author-REPLACE-handle",
  "image": {
    "@type": "ImageObject",
    "url": "REPLACE: CDN URL of author headshot"
  },
  "jobTitle": "REPLACE: e.g., Home Organization Specialist",
  "description": "REPLACE: 2-3 sentence bio with credentials and expertise",
  "knowsAbout": [
    "home organization",
    "storage solutions",
    "kitchen organization",
    "trash management"
  ],
  "worksFor": {
    "@type": "Organization",
    "name": "Happimess",
    "@id": "https://happimess.com/#organization"
  },
  "sameAs": [
    "REPLACE: https://www.linkedin.com/in/author-linkedin",
    "REPLACE: https://twitter.com/author-twitter (if applicable)"
  ]
}
```

**Implementation steps:**
1. Create author bio page in Shopify Admin → Online Store → Pages
2. Set page handle to `author-[firstname-lastname]`
3. Write bio content (credentials, years of experience, areas of expertise)
4. Add person schema as a page-level JSON-LD block in the custom template
5. In `article.liquid` BlogPosting schema, link author.url to this page
6. In the article itself, link the byline text to this page

---

### Template 6: Organization Schema Update (theme.liquid)

**Current sameAs has 6 platforms. When Wikidata/Crunchbase profiles are created, update the sameAs array in theme.liquid:**

Find the Organization schema in `theme.liquid` (search for `"@type": "Organization"`) and add to the sameAs array:

```json
"sameAs": [
  "https://www.facebook.com/happimessofficial/",
  "https://www.instagram.com/happimess_official/",
  "https://www.linkedin.com/company/happimesshome/",
  "https://www.pinterest.com/happimess_/",
  "https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g",
  "https://www.tiktok.com/@happimess_official",
  "https://twitter.com/happimess_official",
  "https://www.crunchbase.com/organization/happimess",
  "https://www.wikidata.org/wiki/QREPLACE"
]
```

**Only add the Wikidata URL after the entity is actually created.** Adding a non-existent URL signals false entity data to AI models.

---

## Implementation Checklist — Shopify Admin Steps

### Step 1: Fix BlogPosting schema (Highest Priority — applies to all 26 articles)

1. Shopify Admin → Online Store → Themes → Edit Code
2. Navigate to `templates/article.liquid` (or `sections/article-template.liquid`)
3. Find any existing JSON-LD `<script type="application/ld+json">` block for articles
4. Replace entirely with Template 1 above
5. Save
6. Test with Google Rich Results Test: `https://search.google.com/test/rich-results?url=https://happimess.com/blogs/news/best-dual-trash-can-for-kitchen-2026-guide-what-actually-works`

### Step 2: Add FAQPage schema (30 minutes)

1. In theme editor, check if a `page.faqs` template exists
2. If not: Templates → Add template → Page → name it "faqs"
3. Add Template 2 (FAQPage JSON-LD) to the new template
4. Go to Online Store → Pages → find "Frequently Asked Questions" page
5. Change page template to "faqs"
6. Test with Rich Results Test on `/pages/faqs`

### Step 3: Fix Product schema (30 minutes + review app metafield verification)

1. Locate the product JSON-LD in `templates/product.liquid` or a snippet (search for `"brand"` or `"@type": "Product"`)
2. Verify the current `brand.name` value — if it uses `{{ product.vendor }}` and returns "Happimess Dev", replace Template 3
3. Check your reviews app documentation for the correct aggregateRating metafield keys
4. Deploy Template 3 with the correct aggregateRating metafields
5. Test: fetch any product URL and check JSON-LD

### Step 4: Add BreadcrumbList (20 minutes)

1. In `theme.liquid`, find the `</head>` tag
2. Add Template 4 conditional blocks just before `</head>`
3. The `{% if template == 'product' %}` and `{% if template == 'article' %}` conditionals ensure the right breadcrumb appears on the right page type

### Step 5: Create author metafields (for future author attribution)

1. Shopify Admin → Settings → Custom data → Metafields → Articles
2. Create new metafield: namespace `custom`, key `author_display_name`, type `Single line text`
3. Create new metafield: namespace `custom`, key `author_page_url`, type `URL`
4. Go to each blog article → scroll to Metafields section → fill in display name and page URL
5. The BlogPosting template (Template 1) automatically uses these values

---

## Schema Validation Resources

After deploying each schema, validate at:

| Tool | URL | Best For |
|------|-----|---------|
| Google Rich Results Test | search.google.com/test/rich-results | Product, FAQPage, Article validation |
| Schema.org Validator | validator.schema.org | All schema types |
| Bing Markup Validator | bing.com/webmaster/tools/markup-validator | Bing-specific validation |

---

## sameAs Platform Status

| Platform | URL | In Schema | Profile Active |
|----------|-----|-----------|----------------|
| Facebook | /happimessofficial/ | ✅ | Unknown |
| Instagram | /happimess_official/ | ✅ | Active (JS-blocked) |
| LinkedIn | /company/happimesshome/ | ✅ | Stale (26 followers) |
| Pinterest | /happimess_/ | ✅ | Unknown |
| YouTube | /channel/UC6l... | ✅ | Likely empty |
| TikTok | /@happimess_official | ✅ | Unknown |
| Twitter/X | Not in schema | ❌ | Unconfirmed |
| Crunchbase | Not in schema | ❌ | No profile |
| Wikidata | Not in schema | ❌ | No entity |
| Wikipedia | Not in schema | ❌ | No article |

---

## Score Projection After All Templates Deployed

| Component | Current | After Deploy |
|-----------|---------|-------------|
| Organization + sameAs | 15/20 | 16/20 (no change until Wikipedia) |
| Article / BlogPosting | 3/15 | 14/15 |
| Person (author) | 0/15 | 8/15 (partial — if 1 author created) |
| sameAs completeness | 10/15 | 10/15 (no change until Wikipedia) |
| speakable | 0/10 | 8/10 (in BlogPosting template) |
| BreadcrumbList | 0/5 | 5/5 |
| WebSite + SearchAction | 5/5 | 5/5 |
| No deprecated schemas | 5/5 | 5/5 |
| JSON-LD format | 5/5 | 5/5 |
| Validation | 3/5 | 5/5 (ampersand fix) |
| **Total** | **46/100** | **~81/100** |

**+35 points from implementing 5 templates.** This is the highest single-action score improvement available across any GEO category.
