# Day 02 — Tasks
**Status:** Ready — all code in `implementation.md`

---

## Checklist

### Task 1 — Add hreflang EN/ES (layout/theme.liquid)

- [ ] Open Shopify Admin → Online Store → Themes → Actions → Edit Code
- [ ] Open `layout/theme.liquid`
- [ ] Find the closing `</head>` tag
- [ ] Paste the hreflang Liquid snippet (from `implementation.md` Fix 1) directly above `</head>`
- [ ] Save
- [ ] Verify on English homepage: view source → search `hreflang` → confirm 3 link tags (en, es, x-default)
- [ ] Verify on Spanish page (`https://happimess.com/es/`): view source → confirm hreflang tags with reversed en/es

**Acceptance criteria:**
```
<link rel="alternate" hreflang="en" href="https://happimess.com/" />
<link rel="alternate" hreflang="es" href="https://happimess.com/es/" />
<link rel="alternate" hreflang="x-default" href="https://happimess.com/" />
```

---

### Task 2 — Add aggregateRating to Product schema

- [ ] Open `sections/main-product.liquid` (or the file that contains `"@type": "Product"` JSON-LD)
- [ ] Find the JSON-LD `<script type="application/ld+json">` block containing `"@type": "Product"`
- [ ] Locate the closing `}` of the Product object (before `</script>`)
- [ ] Add the aggregateRating object as specified in `implementation.md` Fix 2
- [ ] Save
- [ ] Verify: view source on any product page → search `aggregateRating` → confirm it renders with ratingValue and reviewCount
- [ ] Test with Google Rich Results Test: `https://search.google.com/test/rich-results`

**Acceptance criteria:**
Product schema contains `"aggregateRating"` with valid `@type`, `ratingValue`, `reviewCount`, `bestRating`, `worstRating`.

**Note on review data:** If Judge.me, Yotpo, or Okendo is installed, use the metafield path from `implementation.md`. If no review app is installed, use the static fallback values (4.5 / 1) until reviews are live — this is better than no aggregateRating.

---

### Task 3 — Enrich BlogPosting schema

- [ ] Open `sections/main-article.liquid` (or the file containing `"@type": "BlogPosting"` JSON-LD)
- [ ] Find the existing BlogPosting JSON-LD block
- [ ] Add `articleSection`, `wordCount`, and `keywords` fields as specified in `implementation.md` Fix 3
- [ ] Save
- [ ] Verify: view source on any blog article → search `articleSection` → confirm presence

**Acceptance criteria:**
BlogPosting schema contains `articleSection`, `wordCount`, and `keywords` fields.

---

### Task 4 — Enrich Author Person schema

- [ ] In the same `sections/main-article.liquid` file, find the `"@type": "Person"` block in the author object
- [ ] Replace the minimal name-only Person schema with the enriched version from `implementation.md` Fix 4
- [ ] Save
- [ ] Verify: view source on a blog article by Sandip Hadiya → confirm `jobTitle`, `worksFor`, `description`, `sameAs` in the author block
- [ ] Verify: view source on a blog article by Jonathan Yaraghi → confirm different enriched data for that author

**Acceptance criteria:**
Both `"Sandip Hadiya"` and `"Jonathan Yaraghi"` author schemas include `jobTitle`, `worksFor` (with Happimess as Organization), `description`, and `sameAs` array.

---

### Task 5 — Add BreadcrumbList to Homepage, About Us, FAQ

- [ ] **Homepage:** In `layout/theme.liquid` or `templates/index.liquid`, add homepage BreadcrumbList (code in `implementation.md` Fix 5a)
- [ ] **About Us:** In the About Us page template or section, add About BreadcrumbList (code in `implementation.md` Fix 5b)
- [ ] **FAQ page:** In the FAQ page template or section, add FAQ BreadcrumbList (code in `implementation.md` Fix 5c)
- [ ] Save each file after editing
- [ ] Verify: Google Rich Results Test on homepage, About, and FAQ pages → BreadcrumbList found

**Finding the right template:**
- Go to Shopify Admin → Online Store → Pages → About Us → click the page
- In the top-right corner, note the template (e.g., "page.about-us") — this is the template file name
- In Theme Editor → Templates → find `page.about-us.liquid` or `page.about-us.json`

**Acceptance criteria:**
Each page has a valid BreadcrumbList with `@id` URL and item name.

---

### Task 6 — Fix Blog index description + WebSite SearchAction

- [ ] Open `layout/theme.liquid`
- [ ] Find the Blog schema block (search `"@type": "Blog"`)
- [ ] Fix empty `"description"` as specified in `implementation.md` Fix 6a
- [ ] Find the WebSite schema block (search `"@type": "WebSite"`)
- [ ] Fix the nested EntryPoint in SearchAction as specified in `implementation.md` Fix 6b
- [ ] Save
- [ ] Verify: validate with `https://validator.schema.org/` — confirm no warnings for these two schemas

**Acceptance criteria:**
- Blog schema has a non-empty description string
- WebSite SearchAction uses a plain URL string `target` (not a nested EntryPoint object)

---

## Time Log

| Task | Estimated | Actual | Status | Notes |
|------|-----------|--------|--------|-------|
| 1 — hreflang | 20 min | | ⏳ Pending | |
| 2 — aggregateRating | 30 min | | ⏳ Pending | |
| 3 — BlogPosting fields | 20 min | | ⏳ Pending | |
| 4 — Person schema | 25 min | | ⏳ Pending | |
| 5 — BreadcrumbList | 30 min | | ⏳ Pending | |
| 6 — Blog + SearchAction | 15 min | | ⏳ Pending | |
| **Total** | **~2h 20m** | | | |
