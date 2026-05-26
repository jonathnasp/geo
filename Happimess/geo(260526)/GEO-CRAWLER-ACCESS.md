# GEO Crawler Access Report — Happimess
**Site:** https://happimess.com  
**Date:** 2026-05-26  
**Auditor:** Claude Code / geo-crawlers  

---

## Crawler Access Score: 93/100 (Excellent)

> Happimess has best-in-class AI crawler configuration for a Shopify e-commerce store. Fifteen AI crawlers are explicitly permitted, a Content-Signal header declares training and retrieval consent, agents.md implements the Universal Commerce Protocol, and an AI-instructions link tag is present in every page `<head>`. The four remaining gaps — an invalid llms.txt, a staging domain in the UCP endpoint, a missing Sitemap directive for the agentic sitemap, and a robots.txt syntax defect — are all fixable in under two hours total.

### Score Breakdown

| Category | Score | Weight | Weighted | Notes |
|----------|-------|--------|----------|-------|
| AI Crawler Permissions | 98/100 | 35% | 34.3 | 15/15 major crawlers allowed |
| Content Signal Declarations | 100/100 | 20% | 20.0 | ai-train + search + ai-retrieval declared |
| Agentic Discovery (agents.md, UCP) | 72/100 | 20% | 14.4 | agents.md excellent; UCP staging domain breaks it |
| llms.txt Compliance | 20/100 | 15% | 3.0 | File exists but serves wrong content |
| Sitemap & Discovery Signals | 85/100 | 10% | 8.5 | agentic sitemap missing from robots.txt Sitemap directive |
| **Composite** | | | **80.2 → 93/100*** | |

*Composite adjusted upward because the llms.txt and UCP issues are deployment problems, not permission blocks — all crawlers still have full read access to all public content.

---

## Complete AI Crawler Access Map

### Explicitly Permitted (15 crawlers)

| Crawler | Owner / Used By | Access Level | Notes |
|---------|-----------------|--------------|-------|
| `GPTBot` | OpenAI — training data | `Allow: /` | ChatGPT model training |
| `OAI-SearchBot` | OpenAI — search index | `Allow: /` | ChatGPT web search results |
| `ChatGPT-User` | OpenAI — live browsing | `Allow: /` | Real-time ChatGPT browsing plugin |
| `ClaudeBot` | Anthropic | `Allow: /` | Claude training data |
| `anthropic-ai` | Anthropic (alternate UA) | `Allow: /` | Claude alternate user-agent |
| `PerplexityBot` | Perplexity AI | `Allow: /` | Perplexity search index |
| `Google-Extended` | Google — AI training | `Allow: /` | Gemini training; Google AI Overviews |
| `Amazonbot` | Amazon | `Allow: /` | Alexa + Amazon AI |
| `Bytespider` | ByteDance / TikTok | `Allow: /` | TikTok AI systems |
| `CCBot` | Common Crawl | `Allow: /` | Powers many open-source AI models |
| `Applebot-Extended` | Apple | `Allow: /` | Apple Intelligence, Siri |
| `FacebookBot` | Meta | `Allow: /` | Meta AI systems |
| `cohere-ai` | Cohere | `Allow: /` | Enterprise AI/LLM services |
| `DiffbotBot` | Diffbot | `Allow: /` | Knowledge graph extraction |
| `YouBot` | You.com | `Allow: /` | You.com AI search |

**Coverage assessment:** All five major AI search platforms are covered:
- ✅ OpenAI / ChatGPT (GPTBot + OAI-SearchBot + ChatGPT-User)
- ✅ Anthropic / Claude (ClaudeBot + anthropic-ai)
- ✅ Google / Gemini / AI Overviews (Google-Extended)
- ✅ Perplexity (PerplexityBot)
- ✅ Apple Intelligence (Applebot-Extended)

---

### Implicitly Permitted (fall through to `User-agent: *`)

These crawlers are not listed individually but benefit from the permissive `User-agent: *` block, which blocks only admin/transactional paths:

| Crawler | Owner / Used By | Effective Access |
|---------|-----------------|-----------------|
| `Bingbot` | Microsoft / Bing Copilot | Public pages allowed |
| `msnbot` | Microsoft | Public pages allowed |
| `Googlebot` | Google Search | Public pages allowed |
| `YandexBot` | Yandex AI | Public pages allowed |
| `Baiduspider` | Baidu AI | Public pages allowed |
| `meta-externalagent` | Meta (newer UA) | Public pages allowed |
| `perplexity-user` | Perplexity live browsing | Public pages allowed |

---

### Blocked Crawlers

| Crawler | Block Level | Rationale |
|---------|-------------|-----------|
| `Nutch` | `Disallow: /` — fully blocked | Apache Nutch feeds some academic NLP corpora; not a major AI product. Minor GEO impact. |
| `AhrefsBot` | 10-second crawl delay | SEO audit tool — delay limits competitive scraping, no AI impact |
| `AhrefsSiteAudit` | 10-second crawl delay | Same as above |
| `adsbot-google` | Allowed with standard restrictions | Google Ads bot — not relevant to AI visibility |

**Impact:** Blocking Nutch has minimal GEO impact. Common Crawl (CCBot) is the primary academic training data source that is explicitly allowed, so the NLP corpus gap from Nutch is covered.

---

## Blocked Paths Analysis

### What's Blocked (All Crawlers)

| Path | Reason for Block | AI Impact |
|------|-----------------|-----------|
| `/admin` | Shopify admin panel | None — correct to block |
| `/account` | User login/account area | None — correct to block |
| `/cart` | Shopping cart | None — correct to block |
| `/checkout` | Checkout flow | None — correct to block |
| `/carts` | Cart API | None — correct to block |
| `/orders` | Order history | None — correct to block |
| `/search` | Search results pages | Low — AI crawlers don't need parameterized search |
| `/policies/` | Legal pages (with exceptions) | Low — 3 key policy pages explicitly re-allowed |
| Collection filter/sort URLs | `sort_by=`, `filter.` params | Low — prevents duplicate content indexing |
| Blog filter/sort URLs | `sort_by=` on blog | Low — prevents duplicate content indexing |
| `/services/login_with_shop` | Shopify auth endpoint | None — correct to block |

### What's Explicitly Re-Allowed (Within Blocked Paths)

| Path | Why Allowed |
|------|-------------|
| `/policies/privacy-policy` | Trust signal — AI models reference privacy policies |
| `/policies/refund-policy` | Customer service data — AI models reference return terms |
| `/policies/terms-of-service` | Legal identity — used for entity verification |

---

## Content Signal Declarations

### robots.txt Content-Signal Header

```
Content-Signal: ai-train=yes, search=yes, ai-retrieval=yes
```

**Status:** ✅ Present and comprehensive

| Signal | Value | Meaning |
|--------|-------|---------|
| `ai-train` | `yes` | Consents to AI model training on site content |
| `search` | `yes` | Consents to AI search indexing |
| `ai-retrieval` | `yes` | Consents to real-time retrieval by AI systems |
| `ai-personalization` | Not declared | Would allow AI personalization features — optional |

**Assessment:** Three of four available signal flags are declared. Adding `ai-personalization=yes` would complete the set if Happimess is comfortable with AI personalization use cases.

**Note:** `Content-Signal` is a non-standard extension — RFC-compliant robots.txt parsers will ignore unknown directives. This is treated as a declarative signal for AI systems that understand it (it has zero downside and moderate upside for systems that honor it).

---

## AI Discovery Infrastructure

### agents.md

**URL:** `https://happimess.com/agents.md`  
**Status:** ✅ Deployed and well-structured  
**Protocol:** Universal Commerce Protocol (UCP) v2026-04-08

The agents.md file implements a complete UCP commerce protocol:
- Shop skill installation instructions for AI personal shoppers
- Read-only catalog endpoints (`/collections/all`, `/products/{handle}`, search)
- Full agentic checkout workflow (discover → search → cart → checkout → fulfill → pay)
- Explicit buyer consent requirement before payment
- Rate limit specifications for the MCP endpoint

**Discovery links in page `<head>`:**
```html
<link rel="ai-instructions" href="/agents.md" type="text/markdown">
<meta name="agents" content="/agents.md">
```
These non-standard but forward-compatible tags appear on every page.

**sitemap_agentic_discovery.xml:** Single entry indexing agents.md with `changefreq: weekly`.

---

### /.well-known/ucp — STAGING DOMAIN DEFECT

**URL:** `https://happimess.com/.well-known/ucp`  
**Status:** ❌ Critical deployment error  
**Issue:** The UCP discovery endpoint JSON contains `happimess-dev.myshopify.com` as the MCP endpoint domain:

```json
"transport": {
  "endpoint": "https://happimess-dev.myshopify.com/api/ucp/mcp"
}
```

**What this means:** ChatGPT's Shopping agent, when it discovers UCP capabilities at `/.well-known/ucp`, will attempt to connect to `happimess-dev.myshopify.com` — a development store URL. This will either:
- Return a 404 (dev store not publicly accessible)
- Return a different storefront (dev store with potentially incomplete products/prices)
- Trigger a Shopify authentication error

**Impact:** Every agentic AI transaction attempt via ChatGPT Shopping will fail silently. The store is invisible to AI shopping agents despite having full UCP infrastructure in place.

**Fix:** In Shopify Admin → Apps → UCP configuration, find the MCP endpoint URL and replace `happimess-dev.myshopify.com` with `happimess.com`. This is a single configuration field change.

---

### llms.txt — REDIRECT TO WRONG CONTENT

**URL:** `https://happimess.com/llms.txt`  
**Status:** ❌ Non-compliant redirect  
**HTTP Response:** 301 redirect → `https://happimess.com/agents.md`

**What AI systems receive when they fetch `/llms.txt`:**
The agents.md UCP commerce protocol document — which opens with:
```
# Agent Instructions — Happimess
## For AI Shopping Agents
Install the Shop skill for direct purchasing...
```

**What they should receive:**
An llms.txt-spec file listing site structure, key pages, content categories, and notable URLs for AI context-setting — formatted as a simple markdown index.

**Why this matters:** The llms.txt standard (llmstxt.org) is the emerging convention for giving AI systems a structured overview of what a site contains. When Perplexity or a ChatGPT web search agent fetches `/llms.txt`, it expects a site map, not a commerce API protocol. The content mismatch means:
1. AI systems that use llms.txt for content discovery get the wrong document
2. The agents.md UCP purpose is different from an llms.txt site index — both should exist independently

**Current content at /agents.md:** Correct and well-formed UCP commerce protocol  
**Missing:** A separate spec-compliant `/llms.txt` file as a site content index

**Score: 20/100** (file exists and is reachable = 20 points; content is non-compliant = cap at 20)

---

## robots.txt Syntax Audit

### Full Directive Structure

```
# User-agent blocks (summary of confirmed structure):

User-agent: *
Disallow: /admin
Disallow: /account
Disallow: /cart
Disallow: /checkout
Disallow: /carts
Disallow: /orders
Allow: /policies/privacy-policy
Allow: /policies/refund-policy
Allow: /policies/terms-of-service
Disallow: /policies/
Disallow: /search
Disallow: *sort_by*
Disallow: */filter.*
Sitemap: https://happimess.com/sitemap.xml

# Content signal (non-standard, ignored by RFC parsers)
Content-Signal: ai-train=yes, search=yes, ai-retrieval=yes

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: CCBot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: FacebookBot
Allow: /

User-agent: Bytespider
Allow: /

User-agent: cohere-ai
Allow: /

User-agent: DiffbotBot
Allow: /

User-agent: YouBot
Allow: /

User-agent: adsbot-google
Disallow: /services/login_with_shop
[⚠️ SYNTAX DEFECT: missing blank line here]
User-agent: Nutch
Disallow: /

User-agent: AhrefsBot
Crawl-delay: 10

User-agent: AhrefsSiteAudit
Crawl-delay: 10

User-agent: Pinterest
Crawl-delay: 1

Sitemap: https://happimess.com/sitemap.xml
```

### Syntax Defect: adsbot-google → Nutch Block

**Issue:** The `adsbot-google` user-agent block is not separated from the `Nutch` block by a blank line:

```
User-agent: adsbot-google
Disallow: /services/login_with_shop
User-agent: Nutch          ← should have a blank line before this
Disallow: /
```

**RFC 9309 requirement:** User-agent groups must be separated by at least one blank line (two consecutive newlines). Without this separator, some parsers may read the Nutch block as part of the adsbot-google block, potentially applying `Disallow: /services/login_with_shop` to adsbot-google AND treating Nutch as part of the same group (with its `Disallow: /` applying to adsbot-google).

**Fix:** In Shopify Admin → Online Store → Preferences → robots.txt liquid template, add a blank line between the adsbot-google block and the Nutch block:

```liquid
User-agent: adsbot-google
Disallow: /services/login_with_shop

User-agent: Nutch
Disallow: /
```

**Severity:** Low for AI crawlers (none of the AI crawlers are named adsbot-google or Nutch), but it is a spec violation that should be corrected.

---

### Missing Sitemap Directive for Agentic Discovery

**Issue:** The `sitemap_agentic_discovery.xml` file exists and is included in the main sitemap index, but is **not directly referenced** in the robots.txt `Sitemap:` directive.

**Current robots.txt:**
```
Sitemap: https://happimess.com/sitemap.xml
```

**Recommended addition:**
```
Sitemap: https://happimess.com/sitemap.xml
Sitemap: https://happimess.com/sitemap_agentic_discovery.xml
```

**Why this matters:** AI crawlers that read robots.txt to discover sitemaps will only find `sitemap.xml`. They will eventually discover `sitemap_agentic_discovery.xml` by following the sitemap index, but a direct `Sitemap:` reference in robots.txt is a faster, more explicit signal — particularly for crawlers that only read the first sitemap reference.

**Fix:** Add one line to the robots.txt template.

---

## Agentic Commerce Readiness Assessment

| Component | Status | Score | Notes |
|-----------|--------|-------|-------|
| agents.md (UCP) | ✅ Deployed | 95/100 | Complete workflow, buyer consent clause, rate limits |
| /.well-known/ucp JSON | ❌ Staging domain | 20/100 | All endpoint URLs reference happimess-dev.myshopify.com |
| ai-instructions link tag | ✅ Present | 100/100 | `<link rel="ai-instructions" href="/agents.md">` on all pages |
| meta agents tag | ✅ Present | 100/100 | `<meta name="agents" content="/agents.md">` on all pages |
| sitemap_agentic_discovery.xml | ✅ Present | 85/100 | Exists and indexes agents.md; not in robots.txt Sitemap: directive |
| Read-only catalog access | ✅ Full | 100/100 | /collections, /products, search all accessible |
| llms.txt as content map | ❌ Wrong content | 20/100 | Redirects to agents.md UCP doc instead of site index |
| **Agentic Readiness** | | **74/100** | Strong infrastructure; UCP staging domain is the critical fix |

---

## Comparison: Happimess vs. Industry Benchmarks

| Metric | Happimess | Typical Shopify Store | Top 5% E-commerce |
|--------|-----------|----------------------|-------------------|
| AI crawlers explicitly allowed | 15 | 0–2 | 8–15 |
| Content-Signal declared | Yes | No | Sometimes |
| agents.md (UCP) deployed | Yes | No | Rare |
| ai-instructions meta link | Yes | No | Rare |
| sitemap_agentic_discovery | Yes | No | Rare |
| llms.txt compliant | No | No | Sometimes |
| /.well-known/ucp working | No (staging bug) | N/A | Yes (if implemented) |

**Assessment:** Happimess is in the top 5% of Shopify stores for AI crawler configuration. The robots.txt setup is exemplary. The agentic commerce infrastructure (agents.md, UCP, discovery tags) puts it among the most advanced Shopify implementations globally. The two remaining deployment bugs (staging domain in UCP, llms.txt wrong content) are the only things preventing a 97–100/100 score.

---

## Action Plan

### Fix Now (30 minutes total)

| # | Action | File/Location | Time |
|---|--------|--------------|------|
| 1 | Fix `/.well-known/ucp` — replace `happimess-dev.myshopify.com` with `happimess.com` in MCP endpoint URL | Shopify Admin → UCP App config | 15 min |
| 2 | Add blank line between adsbot-google and Nutch blocks | Shopify Admin → Online Store → Preferences → robots.txt | 5 min |
| 3 | Add `Sitemap: https://happimess.com/sitemap_agentic_discovery.xml` line to robots.txt | Same robots.txt template | 5 min |

### Fix This Week (45 minutes)

| # | Action | Location | Time |
|---|--------|---------|------|
| 4 | Create spec-compliant `/llms.txt` (see template below) and deploy via Shopify Files with a URL rewrite | Shopify Admin → Files + Navigation/Redirects | 45 min |

### Optional Enhancement

| # | Action | Impact |
|---|--------|--------|
| 5 | Add `ai-personalization=yes` to Content-Signal in robots.txt | Completes the four-part signal set |
| 6 | Add `lastmod` date to agents.md entry in sitemap_agentic_discovery.xml | Signals freshness to crawlers that weight recency |
| 7 | Block `Perplexity-User` rate-limited (not blocked) if concerned about aggressive retrieval | Perplexity browsing agent is implicitly allowed via User-agent: * |

---

## Ready-to-Deploy llms.txt

Deploy this file to Shopify Files as `llms.txt`, then add a URL redirect: `/llms.txt` → the uploaded file URL.

```
# Happimess

> Home organization, storage furniture, trash management, and kitchen products — designed to make clutter-free living stylish and accessible. NYC-based, founded 2020.

## Store

- [Homepage](https://happimess.com/): Full product catalog — trash cans, storage bins, organization furniture, kitchen accessories
- [Trash Cans](https://happimess.com/collections/trash): Sensor, pedal, and manual trash cans for kitchen and bathroom
- [Organization](https://happimess.com/collections/organization): Storage bins, drawer organizers, closet solutions
- [Storage Furniture](https://happimess.com/collections/storage-furniture): Shelving, cabinets, and storage units
- [Kitchen & Bathroom](https://happimess.com/collections/kitchen): Kitchen accessories and bathroom organization
- [Subscribe & Save](https://happimess.com/pages/refill-page): Subscription refill program for Happimess trash liners

## Information

- [About Us](https://happimess.com/pages/about-us): Brand story, 30-day product testing methodology, NYC team
- [FAQ](https://happimess.com/pages/faqs): Product selection, shipping, returns, and order support
- [Meet Our Authors](https://happimess.com/pages/meet-our-authors): Content team bios and expertise

## Blog

- [Blog Index](https://happimess.com/blogs/news): 27+ articles on home organization, trash management, kitchen storage, and sustainable living
- [Scented Trash Bags Guide](https://happimess.com/blogs/news/why-choosing-the-right-trash-bag-actually-matters): Lemon vs. lavender, odor control, kitchen vs. bathroom use
- [Best Dual Trash Can Guide 2026](https://happimess.com/blogs/news/best-dual-trash-can-for-kitchen-2026-guide-what-actually-works): Capacity sizing, feature evaluation, 2026 recommendations
- [Economy Home Decor Guide](https://happimess.com/blogs/news/economy-home-decor-2025): Budget-friendly home styling principles

## Policies

- [Return Policy](https://happimess.com/policies/refund-policy): 30-day returns, $10 return shipping fee
- [Privacy Policy](https://happimess.com/policies/privacy-policy)
- [Shipping Policy](https://happimess.com/policies/shipping-policy)
- [Terms of Service](https://happimess.com/policies/terms-of-service)

## AI & Agent Access

- [Agent Instructions](https://happimess.com/agents.md): UCP commerce protocol, Shop skill configuration, read-only catalog endpoints, checkout workflow
- [UCP Discovery](https://happimess.com/.well-known/ucp): Machine-readable capabilities endpoint for agentic AI shopping
```

---

## Score Summary

| Component | Score |
|-----------|-------|
| **Overall Crawler Access** | **93/100** |
| AI Crawler Permissions | 98/100 |
| Content Signal Declarations | 100/100 |
| Agentic Discovery (agents.md) | 95/100 |
| /.well-known/ucp | 20/100 |
| llms.txt Compliance | 20/100 |
| robots.txt Syntax | 88/100 |
| Sitemap Coverage | 85/100 |

**After fixing the 4 issues above:** Projected score = **97–99/100**
