# Day 02 — Schema Enrichment + Hreflang + Structured Data Fixes
**Date:** 2026-05-18
**Total estimated time:** ~2.5–3 hours
**Risk level:** Low-Medium — all changes are additive Liquid/JSON-LD; no structural theme changes

---

## Prerequisite

Day-01 tasks should be executed in Shopify Admin before applying Day-02 code. Day-02 is fully independent, however — it can be applied in any order.

---

## Objective

Day-02 closes the six highest-impact **code-level** GEO gaps that remain after Day-01. These are all Liquid theme file edits made in **Shopify Admin → Online Store → Themes → Edit Code**.

No external platform actions required. No Shopify app installs required.

---

## Fixes This Day

| # | Fix | Theme File | Time | Impact |
|---|-----|-----------|------|--------|
| 1 | Add hreflang EN/ES link tags | `layout/theme.liquid` | 20 min | Eliminates duplicate content risk across ~800 URLs; improves all search engine language routing |
| 2 | Add aggregateRating to Product schema | `sections/main-product.liquid` or JSON-LD snippet | 30 min | Unlocks Google Shopping rich results; primary Gemini product comparison signal |
| 3 | Enrich BlogPosting schema (articleSection, wordCount, keywords) | `sections/main-article.liquid` | 20 min | Improves AIO and Gemini content classification; increases structured data score |
| 4 | Enrich Author Person schema (jobTitle, worksFor, description, sameAs) | `sections/main-article.liquid` | 25 min | Strengthens E-E-A-T signals; improves expert entity recognition across all AI platforms |
| 5 | Add BreadcrumbList to Homepage, About Us, FAQ | `layout/theme.liquid` + page templates | 30 min | Fixes 3 pages missing BreadcrumbList; improves navigation schema completeness |
| 6 | Fix Blog index empty description + WebSite SearchAction EntryPoint | `layout/theme.liquid` | 15 min | Fixes 2 low-effort validation issues; improves overall schema quality score |

---

## Expected Outcome

After Day-02, Happimess will have:
- Hreflang annotations on all EN and ES pages (eliminates duplicate content penalty)
- Product pages eligible for Google Shopping rich results via aggregateRating
- Richer BlogPosting schema with content classification signals
- Author schemas with professional credentials for AI entity matching
- BreadcrumbList coverage on all key non-product pages
- Clean WebSite and Blog schema (no empty fields, no nested EntryPoint)

**Estimated score impact:**
- Structured Data: 62 → 72–76 (+10–14 pts)
- Technical Foundations: 71 → 73–75 (+2–4 pts)
- AI Citability: 52 → 56–58 (+4–6 pts)
- Platform Optimization: 41 → 46–52 (+5–11 pts)
- **Composite estimate: +6–8 points**

---

## Files to Edit in Shopify Theme Editor

| Shopify Theme Path | Fix # |
|-------------------|-------|
| `layout/theme.liquid` | 1, 5 (homepage breadcrumb), 6 |
| `sections/main-product.liquid` | 2 |
| `sections/main-article.liquid` | 3, 4 |
| `templates/page.about-us.liquid` OR `sections/main-page.liquid` | 5 |
| `templates/page.faqs.liquid` OR `sections/main-page.liquid` | 5 |

> **Note:** Shopify theme file names vary by theme. The most common variants are listed. Search for the JSON-LD `@type` blocks to locate the correct file if unsure.
