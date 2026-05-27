# GEO Schema Report — happimess.com
**Generated:** May 26, 2026  
**Scope:** Structured data detection, validation, and generation  
**Pages Audited:** Homepage, Product (Beni, Elmo), Blog (2 posts), FAQ, About, Meet Our Authors

---

## Schema Score: 72 / 100

| Category | Score | Notes |
|----------|-------|-------|
| Coverage — schema types present | 76/100 | Most critical types present; missing AboutPage, HowTo, ItemList |
| Correctness — field values | 58/100 | Critical brand.name bug; articleSection error; missing sameAs on Person |
| Completeness — required + recommended fields | 74/100 | Good on BlogPosting; Product missing dimensions, speakable |
| Consistency — cross-page coherence | 68/100 | Organization description inconsistency; Person fields not propagated |
| AI Discoverability — speakable, entity linking | 65/100 | speakable on blog ✅; missing on product; no citation schema |

**Composite: 72/100** — Fair. Core schemas in place; 3 high-impact fixes needed.

---

## Schema Inventory

### Sitewide (theme.liquid — renders on every page)

| Schema | Status | Assessment |
|--------|--------|-----------|
| WebSite + SearchAction | ✅ Complete | Well-formed; SearchAction target correct |
| Organization | ✅ Present | sameAs 7 platforms ✅; missing founder, Wikidata |

### By Page Type

| Page | Schemas Present | Missing |
|------|----------------|---------|
| Homepage | WebSite, Organization, WebPage | — |
| Product | Product, FAQPage, BreadcrumbList, WebSite, Organization | speakable, additionalProperty, category level in breadcrumb |
| Blog Post | BlogPosting, BreadcrumbList, WebSite, Organization | author.sameAs, author.jobTitle in BlogPosting, citation |
| FAQ Page | FAQPage (8 Q&As), BreadcrumbList, WebSite, Organization | WebPage schema |
| About Page | BreadcrumbList, WebSite, Organization | AboutPage (WebPage subtype), Person schemas |
| Meet Our Authors | Person × 2, BreadcrumbList, WebSite, Organization | sameAs on both Person entities |

---

## Issues — Ranked by Priority

### 🔴 Critical

#### 1. `brand.name: "Happimess Dev"` on Product Schema
**Confirmed on:** Beni (HPM1014x), Elmo (HPM1004A) — likely all HPM10xx SKU range  
**Impact:** Google Shopping, Google AI Overviews, and ChatGPT web search read this as the brand name "Happimess Dev" — not "Happimess". Breaks brand identity on AI product queries, comparison queries, and retailer data feeds.  
**Fix:** Shopify Admin → Products → (each affected product) → change Vendor field from `Happimess Dev` to `Happimess`. No code change needed.

```json
// Current (broken):
"brand": { "@type": "Brand", "name": "Happimess Dev" }

// Fixed:
"brand": { "@type": "Brand", "name": "Happimess" }
```

---

### 🟠 High Priority

#### 2. `articleSection` Incorrect Value on BlogPosting
**Confirmed on:** Best Dual Trash Can article — `"articleSection": "Average Kitchen Trash Can Size"`  
**Impact:** AI systems use articleSection for topical classification. A trash can buying guide categorized under "Average Kitchen Trash Can Size" is a topic mismatch that reduces citation eligibility.  
**Fix:** Update the `articleSection` field in the BlogPosting template to reflect the actual blog category.

```json
// Current (wrong):
"articleSection": "Average Kitchen Trash Can Size"

// Fixed:
"articleSection": "Trash Cans & Trash Management"
```

**For all blog sections, the correct values are:**
- Trash can articles: `"Trash Cans & Trash Management"`
- Bag articles: `"Trash Bags"`
- Kitchen articles: `"Kitchen Organization"`
- Storage/furniture: `"Storage & Organization"`
- Decor/sustainability: `"Home Decor & Sustainability"`

#### 3. Person Schema Missing `sameAs` — Both Authors
**Found on:** meet-our-authors page Person schemas  
**Impact:** Without `sameAs` linking to LinkedIn (or other verified profiles), AI systems cannot disambiguate these authors from other individuals with the same name. Critical for E-E-A-T signals — Google's quality rater guidelines and AI citation systems use sameAs to verify author identity.

```json
// Jonathan Yaraghi — add sameAs:
{
  "@type": "Person",
  "@id": "https://happimess.com/pages/meet-our-authors#jonathan-yaraghi",
  "name": "Jonathan Yaraghi",
  "sameAs": [
    "https://www.linkedin.com/in/jonathanyaraghi/",
    "https://www.crunchbase.com/person/jonathan-yaraghi"
  ],
  "jobTitle": "Home Organization Expert",
  ...
}

// Sandip Hadiya — add sameAs:
{
  "@type": "Person",
  "@id": "https://happimess.com/pages/meet-our-authors#sandip-hadiya",
  "name": "Sandip Hadiya",
  "sameAs": [
    "https://www.linkedin.com/in/sandip-hadiya/"
  ],
  "jobTitle": "Content Writer",
  ...
}
```

#### 4. BlogPosting Author Object Missing `jobTitle`
**Found on:** All blog post author objects  
**Current state:** `author` has `@id`, `name`, `url`, `worksFor` — but no `jobTitle`  
**Impact:** jobTitle helps AI systems understand author credentials and expertise level. Google's Helpful Content guidelines weight author credentials.

```json
// Current author object in BlogPosting:
"author": {
  "@type": "Person",
  "@id": "https://happimess.com/pages/meet-our-authors#jonathan-yaraghi",
  "name": "Jonathan Yaraghi",
  "url": "...",
  "worksFor": { ... }
}

// Fixed — add jobTitle:
"author": {
  "@type": "Person",
  "@id": "https://happimess.com/pages/meet-our-authors#jonathan-yaraghi",
  "name": "Jonathan Yaraghi",
  "jobTitle": "Home Organization Expert",
  "url": "...",
  "worksFor": { ... }
}
```

#### 5. Product BreadcrumbList Missing Category Level
**Current:** Home → Product Name (2 levels)  
**Expected:** Home → [Category Collection] → Product Name (3 levels)  
**Impact:** Google and AI systems use BreadcrumbList to understand site hierarchy. Missing the collection level (e.g., "Trash Cans") breaks topical context — a sensor trash can looks orphaned rather than part of a trash can category.

```json
// Current (2 levels):
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "position": 1, "name": "Home", "item": "https://happimess.com" },
    { "position": 2, "name": "Beni 60L Kitchen Trash Can", "item": "https://happimess.com/products/beni-..." }
  ]
}

// Fixed (3 levels) — example for Beni:
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://happimess.com" },
    { "@type": "ListItem", "position": 2, "name": "Trash Cans", "item": "https://happimess.com/collections/trash" },
    { "@type": "ListItem", "position": 3, "name": "Beni 60 Liter/16 Gallon Kitchen Trash/Recycling Trash Can", "item": "https://happimess.com/products/beni-kitchen-trashrecycling-trash-can" }
  ]
}
```

---

### 🟡 Medium Priority

#### 6. Organization Schema Missing `founder`
**Impact:** Founder attribution improves brand entity disambiguation in AI knowledge graphs. Jonathan Yaraghi is already in Person schema — just needs a reference.

```json
// Add to Organization schema in theme.liquid:
"founder": {
  "@type": "Person",
  "@id": "https://happimess.com/pages/meet-our-authors#jonathan-yaraghi",
  "name": "Jonathan Yaraghi"
}
```

#### 7. FAQ Page Missing WebPage Schema
**Current:** FAQPage + BreadcrumbList + Organization  
**Missing:** Standalone `WebPage` node  
**Impact:** WebPage schema with `@id` allows AI to anchor page-level facts (name, description) to a URL. Without it, FAQ page lacks a machine-readable page identity.

```json
// Add to FAQ page template:
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "https://happimess.com/pages/faqs#webpage",
  "url": "https://happimess.com/pages/faqs",
  "name": "Frequently Asked Questions | Happimess",
  "description": "Answers to common questions about Happimess shipping, returns, order changes, and product waitlists.",
  "isPartOf": { "@id": "https://happimess.com/#website" },
  "breadcrumb": { "@id": "https://happimess.com/pages/faqs#breadcrumb" }
}
```

#### 8. About Page Missing `AboutPage` Schema
**Current:** BreadcrumbList + Organization only  
**Missing:** WebPage subtype `AboutPage`  

```json
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "@id": "https://happimess.com/pages/about-us#webpage",
  "url": "https://happimess.com/pages/about-us",
  "name": "About Happimess — Home Organization Brand Founded 2020",
  "description": "Happimess designs home organization, storage furniture, and trash management products. NYC-based brand founded 2020 by Jonathan Yaraghi. Products tested with 30-day evaluation, 500+ pedal cycles.",
  "isPartOf": { "@id": "https://happimess.com/#website" },
  "about": { "@id": "https://happimess.com/#organization" }
}
```

#### 9. Product Schema Missing `speakable`
**Impact:** speakable enables voice search and AI audio retrieval. Google Home, Alexa, and ChatGPT voice interfaces use speakable to select which content to read aloud.

```json
// Add to Product JSON-LD:
"speakable": {
  "@type": "SpeakableSpecification",
  "cssSelector": [".product__title", ".product__description", ".product__price"]
}
```

#### 10. Product Schema Missing `additionalProperty` for Specs
**Impact:** AI comparison queries (e.g., "what size is the Beni trash can?") are answered from Product schema. Dimensions as plain text in description are not machine-readable.

```json
// Add to Product schema:
"additionalProperty": [
  {
    "@type": "PropertyValue",
    "name": "Capacity",
    "value": "60",
    "unitCode": "LTR"
  },
  {
    "@type": "PropertyValue",
    "name": "Height",
    "value": "26.85",
    "unitCode": "INH"
  },
  {
    "@type": "PropertyValue",
    "name": "Width",
    "value": "14.69",
    "unitCode": "INH"
  },
  {
    "@type": "PropertyValue",
    "name": "Depth",
    "value": "22.64",
    "unitCode": "INH"
  },
  {
    "@type": "PropertyValue",
    "name": "Material",
    "value": "Stainless Steel"
  },
  {
    "@type": "PropertyValue",
    "name": "Mechanism",
    "value": "Step Pedal"
  }
]
```

---

### 🟢 Low Priority (Enhancements)

#### 11. Organization `sameAs` Missing Wikidata
Once a Wikidata Q-entity is created for Happimess (Priority #4 from prior audit), add to sameAs array:
```json
"sameAs": [
  "https://www.facebook.com/happimessofficial/",
  "https://www.instagram.com/happimess_official/",
  "https://www.linkedin.com/company/happimesshome/",
  "https://www.pinterest.com/happimess_/",
  "https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g",
  "https://www.tiktok.com/@happimess_official",
  "https://www.crunchbase.com/organization/happimess",
  "https://www.wikidata.org/wiki/Q[NEW_ID]"   // ← add after Wikidata creation
]
```

#### 12. BlogPosting Missing `citation` for External Sources
Articles cite EPA/CDC/USDA as prose. Adding structured citation schema makes these machine-readable for AI fact-checkers.

```json
// Add to relevant BlogPosting schemas:
"citation": [
  {
    "@type": "CreativeWork",
    "name": "EPA Sustainable Materials Management",
    "url": "https://www.epa.gov/smm",
    "publisher": {
      "@type": "Organization",
      "name": "U.S. Environmental Protection Agency"
    }
  }
]
```

#### 13. Organization Description Inconsistency
Two different descriptions are in use for Happimess sitewide:
- WebSite: *"Modern trash cans, storage bins, and home organization furniture — designed and durability-tested for real kitchens and small spaces. Ships to 48 U.S. states."*
- Organization/WebPage: *"Discover modern storage, organization, and furniture solutions at Happimess. From bins and baskets to trash cans and trunks, keep your home stylishly clutter-free."*

**Recommendation:** Standardize on the WebSite version — it includes the testing claim and shipping coverage, which are stronger authority signals.

#### 14. `HowTo` Schema Missing on Instructional Blog Posts
Blog posts like "Tips for Organizing Your Kitchen" and "9 Ways to Hide Your Trash Can" are How-To guides but lack HowTo schema. This unlocks Google rich results panels and AI step-extraction.

```json
// Example for "9 Ways to Hide Your Trash Can":
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "9 Ways to Hide Your Trash Can",
  "description": "Practical strategies for concealing kitchen and bathroom trash cans using furniture, cabinetry, and design solutions.",
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "Under-Cabinet Pull-Out",
      "text": "Install a pull-out trash can drawer inside a base cabinet..."
    }
    // ... additional steps
  ]
}
```

#### 15. CollectionPage Schema Missing on Collection Pages
Collection pages (`/collections/trash`, `/collections/sensor-trash-cans`, etc.) have no schema markup. Adding `CollectionPage` + `ItemList` enables AI to understand product taxonomy.

```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "@id": "https://happimess.com/collections/trash#webpage",
  "url": "https://happimess.com/collections/trash",
  "name": "Trash Cans | Happimess",
  "description": "Full trash can collection — sensor, step, dual compartment, push button, indoor/outdoor.",
  "isPartOf": { "@id": "https://happimess.com/#website" }
}
```

---

## Schema Completeness by Type

| Schema Type | Present | Correct | Score | Priority |
|-------------|---------|---------|-------|----------|
| WebSite | ✅ | ✅ | 100/100 | — |
| Organization | ✅ | 85% | 85/100 | Add founder, Wikidata |
| WebPage (homepage) | ✅ | 90% | 90/100 | — |
| Product | ✅ | **55%** | 55/100 | Fix brand.name (CRITICAL) |
| FAQPage (product) | ✅ | 95% | 95/100 | — |
| FAQPage (FAQ page) | ✅ | 90% | 90/100 | Add WebPage wrapper |
| BlogPosting | ✅ | 78% | 78/100 | Fix articleSection, add author.jobTitle+sameAs |
| BreadcrumbList | ✅ | 75% | 75/100 | Add category level on products |
| Person | ✅ | 70% | 70/100 | Add sameAs, image |
| AboutPage | ❌ | 0% | 0/100 | Create schema |
| HowTo | ❌ | 0% | 0/100 | Add to instructional posts |
| CollectionPage | ❌ | 0% | 0/100 | Add to collection pages |

---

## Ready-to-Deploy JSON-LD

### Fix 1 — Product Brand Name (theme edit or Shopify Vendor field)

**Option A (Recommended): Change Vendor in Shopify Admin**  
Shopify Admin → Products → filter by Vendor "Happimess Dev" → bulk edit Vendor to "Happimess"  
This fixes the Vendor field that populates `brand.name` in the Liquid template.

**Option B: Edit product.liquid directly**  
If the Liquid template reads `product.vendor`, no code change is needed after the vendor fix.  
If it's hardcoded, find the JSON-LD snippet and replace `"Happimess Dev"` → `"Happimess"`.

---

### Fix 2 — Organization Schema with Founder (add to theme.liquid)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://happimess.com/#organization",
      "name": "Happimess",
      "legalName": "Happimess",
      "url": "https://happimess.com",
      "foundingDate": "2020-01-15",
      "description": "Modern trash cans, storage bins, and home organization furniture — designed and durability-tested for real kitchens and small spaces. Ships to 48 U.S. states.",
      "telephone": "+19172614961",
      "email": "hello@happimess.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "185 Madison Avenue",
        "addressLocality": "New York",
        "addressRegion": "New York",
        "postalCode": "10016",
        "addressCountry": "US"
      },
      "founder": {
        "@type": "Person",
        "@id": "https://happimess.com/pages/meet-our-authors#jonathan-yaraghi",
        "name": "Jonathan Yaraghi"
      },
      "image": {
        "@type": "ImageObject",
        "url": "https://cdn.shopify.com/s/files/1/0491/2909/5325/files/happimess-logo-ai-file_1.svg?v=1697698531"
      },
      "logo": {
        "@type": "ImageObject",
        "url": "https://cdn.shopify.com/s/files/1/0491/2909/5325/files/happimess-logo-ai-file_1.svg?v=1697698531"
      },
      "sameAs": [
        "https://www.facebook.com/happimessofficial/",
        "https://www.instagram.com/happimess_official/",
        "https://www.linkedin.com/company/happimesshome/",
        "https://www.pinterest.com/happimess_/",
        "https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g",
        "https://www.tiktok.com/@happimess_official",
        "https://www.crunchbase.com/organization/happimess"
      ],
      "areaServed": { "@type": "Country", "name": "United States" },
      "knowsAbout": [
        "home organization", "storage solutions", "trash management",
        "kitchen organization", "bathroom storage", "bedroom organization",
        "living room storage", "office organization",
        "laundry room solutions", "sustainable home products"
      ],
      "contactPoint": [{
        "@type": "ContactPoint",
        "telephone": "+19172614961",
        "email": "hello@happimess.com",
        "contactType": "customer service",
        "availableLanguage": ["English", "Spanish"]
      }]
    }
  ]
}
```

---

### Fix 3 — Person Schema with `sameAs` (meet-our-authors page template)

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
      "description": "Jonathan Yaraghi is a home organization expert and content lead at Happimess, specializing in practical guides for kitchen organization, trash management, and home decor. Founder of Happimess.",
      "sameAs": [
        "https://www.linkedin.com/in/jonathanyaraghi/"
      ],
      "worksFor": {
        "@type": "Organization",
        "@id": "https://happimess.com/#organization",
        "name": "Happimess"
      },
      "knowsAbout": [
        "home organization", "kitchen organization",
        "trash management", "storage solutions", "home decor"
      ]
    },
    {
      "@type": "Person",
      "@id": "https://happimess.com/pages/meet-our-authors#sandip-hadiya",
      "name": "Sandip Hadiya",
      "url": "https://happimess.com/pages/meet-our-authors",
      "jobTitle": "Content Writer",
      "description": "Sandip Hadiya is a content writer at Happimess with a focus on eco-friendly living, home styling, and sustainable organization solutions.",
      "sameAs": [
        "https://www.linkedin.com/in/sandip-hadiya/"
      ],
      "worksFor": {
        "@type": "Organization",
        "@id": "https://happimess.com/#organization",
        "name": "Happimess"
      },
      "knowsAbout": [
        "eco-friendly living", "home styling",
        "sustainable organization", "clutter-free spaces",
        "environmentally conscious living"
      ]
    }
  ]
}
```

---

### Fix 4 — BlogPosting Author with `jobTitle` (blog article template)

In the Liquid template that renders BlogPosting, update the author block:

```liquid
"author": {
  "@type": "Person",
  "@id": "https://happimess.com/pages/meet-our-authors#{{ article.author | handleize }}",
  "name": {{ article.author | json }},
  "jobTitle": {% if article.author == "Jonathan Yaraghi" %}"Home Organization Expert"{% else %}"Content Writer"{% endif %},
  "url": "https://happimess.com/pages/meet-our-authors#{{ article.author | handleize }}",
  "worksFor": {
    "@type": "Organization",
    "name": "Happimess",
    "@id": "https://happimess.com/#organization"
  }
}
```

---

### Fix 5 — AboutPage Schema (about-us page template)

```json
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "@id": "https://happimess.com/pages/about-us#webpage",
  "url": "https://happimess.com/pages/about-us",
  "name": "About Happimess — NYC Home Organization Brand",
  "description": "Happimess designs home organization, storage furniture, and trash management products. NYC-based brand founded 2020. All products tested over 30 days with 500+ pedal cycles before recommendation.",
  "isPartOf": { "@id": "https://happimess.com/#website" },
  "about": { "@id": "https://happimess.com/#organization" },
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://happimess.com" },
      { "@type": "ListItem", "position": 2, "name": "About Us", "item": "https://happimess.com/pages/about-us" }
    ]
  }
}
```

---

## Implementation Checklist

| # | Fix | File to Edit | Effort | Impact |
|---|-----|-------------|--------|--------|
| 1 | Fix `brand.name: "Happimess Dev"` | Shopify Admin → Products (Vendor field) | 15 min | 🔴 Critical |
| 2 | Fix `articleSection` on all blog posts | Blog article Liquid template | 30 min | 🟠 High |
| 3 | Add `sameAs` to both Person schemas | meet-our-authors page template | 15 min | 🟠 High |
| 4 | Add `jobTitle` to BlogPosting author | Blog article Liquid template | 20 min | 🟠 High |
| 5 | Add category level to product breadcrumbs | product.liquid or JSON-LD snippet | 30 min | 🟠 High |
| 6 | Add `founder` to Organization schema | theme.liquid Organization block | 10 min | 🟡 Medium |
| 7 | Add WebPage schema to FAQ page | pages/faqs template | 15 min | 🟡 Medium |
| 8 | Add AboutPage schema | pages/about-us template | 15 min | 🟡 Medium |
| 9 | Add `speakable` to Product schema | product.liquid or JSON-LD snippet | 20 min | 🟡 Medium |
| 10 | Add `additionalProperty` (specs) to Product | product.liquid | 45 min | 🟡 Medium |
| 11 | Add `citation` to blog posts with gov sources | Blog article Liquid template | 1 hr | 🟢 Low |
| 12 | Add `founder.sameAs` (after Wikidata) | theme.liquid after Q-entity created | 5 min | 🟢 Low |
| 13 | Unify Organization description | theme.liquid | 10 min | 🟢 Low |
| 14 | Add HowTo schema to instructional posts | Blog article Liquid template | 2 hrs | 🟢 Low |
| 15 | Add CollectionPage schema | collection.liquid | 45 min | 🟢 Low |

**Total quick wins (fixes 1–5):** ~1.75 hours → Schema score projection: 72 → **84/100**

---

## Validation Tools

- **Google Rich Results Test:** https://search.google.com/test/rich-results
- **Schema.org Validator:** https://validator.schema.org/
- **Bing Markup Validator:** https://www.bing.com/webmasters/markup-validator
- Test each page after changes — especially product, blog, FAQ

---

*Report generated by /geo schema — GEO Skill v2026*
