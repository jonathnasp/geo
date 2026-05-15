# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository tracks **GEO (Generative Engine Optimization) audit reports and documentation** for **Happimess** — a Shopify e-commerce store selling home organization, storage, and trash management products (happimess.com). The actual storefront lives in Shopify's admin panel; this repo is a documentation and audit-tracking workspace.

There is no build system, test runner, or package manager. No `npm install`, no `make`, no CI pipeline.

## Repository Contents

- `GEO-AUDIT-REPORT.md` — Latest GEO audit. Always the canonical source for current scores, issues, and sprint priorities. Check here before acting on any issue listed below.

When new audit runs happen, keep `GEO-AUDIT-REPORT.md` as the current report and archive the previous one as `GEO-AUDIT-REPORT-YYYY-MM-DD.md`. To re-run a full audit, use the `/geo-audit` skill pointed at `https://happimess.com`.

## Store Context

- **Platform:** Shopify (SSR — all content in initial HTML, good for AI crawlers)
- **Languages:** English (primary) + Spanish (`/es/` subdirectory)
- **Blog:** ~24 articles, 1,200–3,500 words each, at `/blogs/news/`
- **Key pages:** `/pages/about-us`, `/pages/faqs`, `/pages/refill-page` (subscription), `/pages/ambassador-program`
- **Social presence:** 5 platforms (LinkedIn company page does not yet exist)

## GEO Work Conventions

### Making Shopify Theme Changes

All schema/template fixes happen in Shopify Admin → Online Store → Themes → Edit Code. Key files:
- `product.liquid` or the JSON-LD snippet — for product schema fixes (e.g., `"Happimess Dev"` → `"Happimess"`)
- `theme.liquid` — for sitewide Organization schema and sameAs links
- Custom page templates for FAQ, About, blog article schemas

### llms.txt

Deploy to `https://happimess.com/llms.txt` by uploading through Shopify Admin → Online Store → Files, then redirect via a Shopify page at the `/llms.txt` route or through a custom app proxy.

### Priority Order for GEO Fixes

From the current audit, prioritize in this order:
1. **Critical issues first** — fixes with Low effort and All-platform impact (e.g., brand name in schema, llms.txt, sameAs)
2. **Content E-E-A-T** — author bios, publication dates, external citations on blog posts
3. **Platform-specific** — Google AI Overviews (FAQ schema), Bing (Webmaster Tools verification), Perplexity (content depth)

### Scoring Reference

GEO scores use a 0–100 scale:
- 0–25: Critical
- 26–50: Poor
- 51–75: Fair
- 76–90: Good
- 91–100: Excellent

Composite score is weighted: AI Citability 25%, Brand Authority 20%, Content Quality 20%, Technical Foundations 15%, Structured Data 10%, Platform Optimization 10%.

## Open Issues (as of April 14, 2026 audit — verify against current report)

| # | Issue | Effort | Impact |
|---|-------|--------|--------|
| 1 | `"Happimess Dev"` in Product JSON-LD `brand.name` — staging artifact in production | Low | Critical |
| 2 | No `llms.txt` at root (404) | Low | All platforms |
| 3 | Organization schema missing `sameAs` social profile URLs | Low | Brand authority |
| 4 | `description: null` in WebPage schema | Low | All platforms |
| 5 | No `hreflang` tags for EN/ES | Medium | Duplicate content |
| 6 | `/policies/` blocked in robots.txt | Low | Crawlability |
| 7 | Blog posts have no visible publication dates | Medium | Freshness signals |
| 8 | Admin usernames in JSON-LD (`jonathany 2123`, `Asodariya Sumi`) — need brand author names | Low | Brand trust |
| 9 | No LinkedIn company page | Medium | Brand authority |

Always check `GEO-AUDIT-REPORT.md` for the current status of these — items may have been resolved since this file was last updated.
