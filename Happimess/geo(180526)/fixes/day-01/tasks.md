# Day 01 — Tasks
**Status:** Pending

---

## Checklist

### Task 1 — Deploy spec-compliant llms.txt
- [ ] Open Shopify Admin → Content → Files
- [ ] Upload `llms.txt` from `geo(180526)/llms.txt` (the new spec-compliant version)
- [ ] Upload `llms-full.txt` from `geo(180526)/llms-full.txt`
- [ ] Verify both files are accessible:
  - `https://happimess.com/llms.txt`
  - `https://happimess.com/llms-full.txt`
- [ ] If direct file serving does not route to the root path, create a Shopify page at handle `llms` with the file content as body text (plain text content type)

**Note:** Shopify's CDN serves uploaded files at `/cdn/shop/files/filename`. For llms.txt to resolve at the root path (`/llms.txt`), it must either be routed via a page redirect or via a Shopify app proxy. If this routing step is not feasible today, prioritize the other 4 tasks and defer routing to a developer session.

---

### Task 2 — Fix FAQ page title
- [ ] Go to Shopify Admin → Online Store → Pages
- [ ] Open the FAQs page
- [ ] Scroll to the SEO section at the bottom
- [ ] Change **Page title** from: `Faqs`
  To: `Frequently Asked Questions | Happimess`
- [ ] Change **Meta description** to:
  `Find answers to common questions about Happimess orders, shipping, returns, and product policies. Ships to 48 contiguous US states.`
- [ ] Click Save

---

### Task 3 — Fix author name casing
- [ ] Go to Shopify Admin → Settings → Users and permissions
- [ ] Find the account for Sandip Hadiya
- [ ] Change display name from `sandip hadiya` to `Sandip Hadiya`
- [ ] Save
- [ ] Verify propagation: view any blog article in source HTML and check the JSON-LD `"author"` block shows `"Sandip Hadiya"` not `"sandip hadiya"`

---

### Task 4 — Show dates on blog listing
- [ ] Go to Shopify Admin → Online Store → Themes → Actions → Edit Code
- [ ] Find the blog listing template (typically `sections/main-blog.liquid` or `templates/blog.liquid`)
- [ ] Locate the article loop (`{% for article in blog.articles %}`)
- [ ] Add the date span as specified in `implementation.md`
- [ ] Save
- [ ] Preview the blog listing at `https://happimess.com/blogs/news` — confirm dates appear under article titles

---

### Task 5 — Fix robots.txt Allow ordering
- [ ] Review current `robots.txt` at `https://happimess.com/robots.txt`
- [ ] If using a Shopify SEO app to manage robots.txt, update rule order in the app
- [ ] If using a custom `robots.txt.liquid` template, reorder rules as specified in `implementation.md`
- [ ] Verify fix: the three Allow rules for `/policies/` pages must appear *before* the `Disallow: /policies/` line
- [ ] Confirm by fetching `https://happimess.com/robots.txt` and checking order

---

## Time Log

| Task | Estimated | Actual | Notes |
|------|-----------|--------|-------|
| 1 — llms.txt deploy | 15 min | | |
| 2 — FAQ title | 5 min | | |
| 3 — Author casing | 5 min | | |
| 4 — Blog dates | 20 min | | |
| 5 — robots.txt | 15 min | | |
| **Total** | **60 min** | | |
