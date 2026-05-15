# Schema & Structured Data Report — happimess.com
**Date:** May 7, 2026 | **Source:** Full GEO Audit Schema Agent

---

## Schema Scores

| Dimension | Score | Rating |
|-----------|-------|--------|
| Schema Presence | 62/100 | Fair |
| Schema Quality | 44/100 | Poor |
| Rich Result Eligibility | 51/100 | Fair |
| **Overall Schema Score** | **52/100** | **Fair** |

**Key finding:** Schema exists across all page types but contains critical validation errors on every single page. The site is closer to a "fix errors" situation than an "add schema" situation — though both are needed.

---

## Schema Inventory by Page Type

### Homepage — https://happimess.com/

| Schema | Format | Valid | Rich Result | Notes |
|--------|--------|-------|-------------|-------|
| WebPage | JSON-LD (@graph) | Yes | N/A | Present |
| WebSite + SearchAction | JSON-LD (@graph) | Yes (minor) | ✅ Sitelinks Search Box | Functional |
| LocalBusiness | JSON-LD (@graph) | Partial — errors | ⚠️ Local Panel (wrong type) | **Wrong @type** |

⚠️ **JS injection risk:** The LocalBusiness and WebSite @graph blocks appear to be injected by T4S theme JavaScript — not server-rendered. AI crawlers (GPTBot, ClaudeBot, PerplexityBot) that don't execute JavaScript will miss these schemas entirely.

---

### Product Pages — e.g. /products/abrahamus-8-gallon-step-open-trash-can

| Schema | Format | Valid | Rich Result | Notes |
|--------|--------|-------|-------------|-------|
| Product | JSON-LD | Partial — errors | ⚠️ Partially eligible | Relative URL, trailing slash on @context |
| BreadcrumbList | JSON-LD | Partial — errors | ✅ Breadcrumb | HTTP context (not HTTPS), missing collection level |
| FAQPage | JSON-LD | Yes | ❌ Restricted since Aug 2023 | Keep for AI semantic value only |
| WebSite + LocalBusiness | JSON-LD (@graph) | Partial — errors | ⚠️ | Same global errors |

---

### Blog Posts — e.g. /blogs/news/the-guide-to-choosing-the-perfect-kitchen-trash-can

| Schema | Format | Valid | Rich Result | Notes |
|--------|--------|-------|-------------|-------|
| Article | JSON-LD | Partial — errors | ⚠️ Partially eligible | **Author URL returns 404** |
| BreadcrumbList | JSON-LD | Yes | ✅ Breadcrumb | Valid — 3-level (Home > Blog > Post) |
| WebSite + LocalBusiness | JSON-LD (@graph) | Partial — errors | ⚠️ | Same global errors |

---

### Collection Pages — e.g. /collections/trash-can

| Schema | Format | Valid | Rich Result | Notes |
|--------|--------|-------|-------------|-------|
| (none) | — | — | ❌ | Entirely absent |

---

## Validation Errors — Full List

| Error | Severity | Affects | Fix |
|-------|----------|---------|-----|
| `author.url` → 404 (`/pages/asodariya-sumi`) | **Critical** | All 26 blog posts | Create the author page in Shopify |
| `@type: LocalBusiness` (wrong for e-commerce brand) | **Critical** | All pages (global) | Change to `Organization` |
| `telephone: " (917) 261-4961"` (leading space) | **High** | All pages (global) | Remove leading space |
| `Product.url` is relative, not absolute | **High** | All product pages | Prepend `{{ shop.url }}` in Liquid |
| `@context: "https://schema.org/"` trailing slash | **Medium** | Product + BreadcrumbList pages | Remove trailing slash |
| `servesCuisine` on Organization (restaurant-only) | **Medium** | All pages (global) | Remove this property |
| `contactType: "Customer Support"` (wrong enum value) | **Medium** | All pages (global) | Change to `"customer service"` (lowercase) |
| `aggregateRating.reviewCount: "120"` (string not number) | **Medium** | All pages (global) | Remove quotes — must be integer |
| `aggregateRating.ratingValue: "4.5"` (string not number) | **Medium** | All pages (global) | Remove quotes — must be number |
| `BreadcrumbList @context: "http://schema.org/"` (HTTP + slash) | **Medium** | Product BreadcrumbList | Change to `"https://schema.org"` |
| `sameAs` Pinterest uses `pin.it` short URL | **Low** | All pages (global) | Replace with full canonical Pinterest profile URL |
| Article `description` is duplicated text | **Low** | Blog posts | Unique 1–2 sentence summary |
| Author missing `sameAs`, `jobTitle`, `description` | **Medium** | Blog posts | Add to Article + Person schema |
| `Article.speakable` missing | **Medium** | Blog posts | Add speakable property |
| `CollectionPage` schema entirely absent | **High** | All collection pages | Add via `collection.liquid` template |
| `AggregateRating` missing from Product | **Critical** | All product pages | Wire to review app metafields |

---

## Missing Schemas — Priority List

| Priority | Schema | Page Type | Impact |
|----------|--------|-----------|--------|
| Critical | Organization (replace LocalBusiness) | All pages | Entity recognition, Knowledge Panel |
| Critical | AggregateRating on Product | Product pages | Star ratings in SERPs |
| Critical | Person (live author page + schema) | Blog + author pages | E-E-A-T for all content |
| High | speakable on Article | Blog posts | AI assistant readiness |
| High | CollectionPage + ItemList | /collections/ pages | AI product discovery |
| High | sameAs: Wikipedia, Wikidata, Crunchbase | Homepage (Organization) | AI entity recognition |
| Medium | Product.color, material, additionalProperty | Product pages | AI comparison queries |
| Medium | gtin / mpn on Product | Product pages | Google Shopping identity |
| Medium | Brand (standalone) | Homepage | Connects product Brand to Organization |
| Medium | VideoObject | Blog posts (if videos added) | Multi-format entity signal |
| Low | ItemList on blog index | /blogs/news/ | Content taxonomy for AI |

---

## sameAs Status

Current sameAs links in schema (6 platforms):

| Platform | Linked | URL | Valid |
|----------|--------|-----|-------|
| Facebook | ✅ | https://www.facebook.com/happimessofficial/ | Yes |
| Instagram | ✅ | https://www.instagram.com/happimess_official/ | Yes |
| LinkedIn | ✅ | https://www.linkedin.com/company/happimesshome/ | Yes |
| Pinterest | ✅ | https://pin.it/6USD9wO | ⚠️ Short URL — replace |
| YouTube | ✅ | https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g | Yes |
| TikTok | ✅ | https://www.tiktok.com/@happimess_official | Yes |
| Wikipedia | ❌ | Not linked (doesn't exist yet) | — |
| Wikidata | ❌ | Not linked (doesn't exist yet) | — |
| Crunchbase | ❌ | Not linked (unknown if exists) | — |

---

## Rich Result Eligibility Summary

| Rich Result Type | Status | Blocker |
|-----------------|--------|---------|
| Sitelinks Search Box | ✅ Eligible | None |
| Product Rich Result | ⚠️ Partially eligible | No AggregateRating; relative URL in `url` field |
| Article Rich Result | ⚠️ Partially eligible | Author URL is 404 |
| Breadcrumb | ✅ Eligible (blog) | None on blog posts |
| Breadcrumb | ⚠️ Partially eligible (product) | HTTP context, missing collection level |
| FAQ Rich Result | ❌ Restricted | Google restricted FAQPage to gov/health sites (Aug 2023) — keep for AI semantic value |
| Local Panel | ❌ Wrong type | LocalBusiness instead of Organization |
| Knowledge Panel | ❌ Insufficient | No Organization schema with Wikipedia sameAs |
| Star Ratings | ❌ Missing | No AggregateRating on Product |

---

## Deployment Files

The following JSON-LD files are ready to deploy. See the `/schema/` subfolder:

| File | Purpose | Deploy Location |
|------|---------|----------------|
| `schema-organization.json` | Replace LocalBusiness on all pages | `theme.liquid` `<head>` — server-rendered |
| `schema-website.json` | WebSite + SearchAction (fixed) | `theme.liquid` `<head>` — server-rendered |
| `schema-product.liquid` | Product schema template | `snippets/schema-product.liquid` → include in `product.liquid` |
| `schema-article.liquid` | Article + BreadcrumbList + speakable | `snippets/schema-article.liquid` → include in `article.liquid` |
| `schema-collection.liquid` | CollectionPage + ItemList | `snippets/schema-collection.liquid` → include in `collection.liquid` |
| `schema-author-person.json` | Person schema for author page | `pages/asodariya-sumi` page template |
| `schema-breadcrumb-product.liquid` | Fixed BreadcrumbList for products | `snippets/schema-breadcrumb-product.liquid` |

---

## Implementation Order

1. **Global fix first** — Replace LocalBusiness with Organization in `theme.liquid` (fixes 8 validation errors site-wide in one edit)
2. **Author page** — Create `/pages/asodariya-sumi` and add Person schema (fixes Article schema E-E-A-T on all 26 blog posts)
3. **Product schema** — Deploy `schema-product.liquid` snippet to `product.liquid` (AggregateRating + absolute URL fix)
4. **Collection schema** — Deploy `schema-collection.liquid` to `collection.liquid` (new — currently no schema on collections)
5. **Article speakable** — Add speakable property to Article schema in `article.liquid`

Validate all changes at: https://search.google.com/test/rich-results

---

*Generated by Claude Code GEO Skill — `/geo schema https://happimess.com/`*
*Full audit data: `GEO-AUDIT-REPORT.md`*
