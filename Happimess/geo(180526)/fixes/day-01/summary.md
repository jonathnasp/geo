# Day 01 — Critical Indexing Fixes
**Date:** 2026-05-18  
**Total estimated time:** ~60 minutes  
**Risk level:** Low — all changes are additive or Shopify Admin UI edits

---

## Objective

Fix the highest-impact indexing issues that cost AI citation opportunities today. Every fix in Day 01 is either a file upload, a Shopify Admin form field change, or a single Liquid template line. No theme architecture is touched.

---

## Fixes This Day

| # | Fix | Where | Time | Why It Matters |
|---|-----|-------|------|----------------|
| 1 | Deploy spec-compliant `llms.txt` | Shopify Files | 15 min | All AI models read llms.txt for site orientation. Current file is a commerce-agent document, not spec-compliant. ChatGPT, Claude, and Perplexity find nothing usable. |
| 2 | Fix FAQ page title: `"Faqs"` → `"Frequently Asked Questions \| Happimess"` | Shopify Admin → Pages | 5 min | "Faqs" has zero search keywords and zero brand signal. Googlebot, Bingbot, and every AI crawler uses the title tag to classify page relevance. |
| 3 | Fix author name casing: `"sandip hadiya"` → `"Sandip Hadiya"` | Shopify Admin → Settings | 5 min | Author name appears in every blog article's JSON-LD schema. Lowercase name fails AI entity-matching for this author's Person schema. |
| 4 | Show publication dates on blog listing | `blog.liquid` theme file | 20 min | Blog listing page shows no dates on article cards. Perplexity and Google AIO weight content freshness heavily. The listing page is often the entry point for AI crawlers indexing the content catalog. |
| 5 | Fix `robots.txt` Allow override ordering for `/policies/` | Shopify robots.txt app or theme | 15 min | Current `robots.txt` has `Allow` rules for specific policy pages *after* the `Disallow: /policies/` rule. Per RFC 9309, order matters for strict parsers. Unnamed crawlers may block the three policy pages with explicit Allow overrides. |

---

## Outcome

After Day 01, Happimess will have:
- A spec-compliant llms.txt that all 10+ AI crawlers can parse correctly
- An FAQ page correctly titled for keyword relevance
- All blog article schemas with properly cased author name
- A blog listing page that shows article dates (freshness signal for Perplexity, AIO)
- A robots.txt with correct rule ordering for policy pages

**Estimated score impact:** +3–4 points on AI Citability, +2 points on Platform Optimization (Perplexity freshness signal)
