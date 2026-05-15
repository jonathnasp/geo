# GEO Crawler Access Analysis — Happimess (happimess.com)

**Audit Date:** April 15, 2026
**Scope:** robots.txt, meta robots tags, HTTP headers, AI bot access patterns, sitemap, llms.txt

---

## 1. Crawler Access Map

| Bot Name | Purpose | Current Status | Recommended Status | AI Visibility Impact |
|---|---|---|---|---|
| **GPTBot** | ChatGPT training & retrieval | ALLOWED (via `User-agent: *`) | ALLOWED — confirm explicitly | Products/blog visible to ChatGPT; `/policies/` and `/search` blocked |
| **OAI-SearchBot** | ChatGPT web search (real-time) | ALLOWED (via `User-agent: *`) | ALLOWED — confirm explicitly | Same block pattern as GPTBot |
| **PerplexityBot** | Perplexity AI search | ALLOWED (via `User-agent: *`) | ALLOWED — confirm explicitly | Products/blog indexable; policy pages invisible |
| **ClaudeBot** | Anthropic training & Claude.ai | ALLOWED (via `User-agent: *`) | ALLOWED — confirm explicitly | Full product/content access; policy pages blocked |
| **Google-Extended** | Gemini/Bard training data | ALLOWED (via `User-agent: *`) | ALLOWED — confirm explicitly | Products/blog/pages all crawlable |
| **Googlebot** | Google Search + AI Overviews | ALLOWED (via `User-agent: *`) | ALLOWED — no change needed | Primary indexer; AI Overviews depend on this |
| **Bingbot** | Bing Search + Copilot | ALLOWED (via `User-agent: *`) | ALLOWED — no change needed | Copilot citations depend on Bing index |
| **CCBot** | Common Crawl (AI training datasets) | ALLOWED (via `User-agent: *`) | ALLOWED — no change needed | Feeds many open-weight AI training sets |
| **Applebot** | Apple search + Siri knowledge | ALLOWED (via `User-agent: *`) | ALLOWED — no change needed | Siri product/brand queries |
| **DuckDuckBot** | DuckDuckGo search | ALLOWED (via `User-agent: *`) | ALLOWED — no change needed | Privacy-focused search index |
| **Nutch** | Apache Nutch crawler | FULLY BLOCKED (`Disallow: /`) | BLOCKED — keep as-is | Nutch is often used for scraping; blocking is appropriate |
| **AhrefsBot** | SEO audit tool | ALLOWED with 10s crawl-delay | Acceptable — keep as-is | Not an AI crawler; delay protects server |
| **AhrefsSiteAudit** | SEO audit tool | ALLOWED with 10s crawl-delay | Acceptable — keep as-is | Not an AI crawler |
| **MJ12bot** | Majestic SEO crawler | ALLOWED with 10s crawl-delay | Acceptable — keep as-is | Not an AI crawler |
| **Pinterest** | Pinterest crawler | ALLOWED with 1s crawl-delay | Acceptable — keep as-is | Social discovery |
| **adsbot-google** | Google Ads bot | Limited to non-checkout paths | Keep as-is — correct | Ads-only; checkout blocks are appropriate |

**Key Finding:** All major AI crawlers are implicitly allowed under `User-agent: *`. There are no explicit entries for GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot, or Google-Extended. Implicit allowance works in practice but provides no signal of intent and makes future fine-grained control harder to implement.

---

## 2. robots.txt — Full Current Content

Fetched April 15, 2026 from `https://happimess.com/robots.txt`:

```
# we use Shopify as our ecommerce platform

#  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#  ┃  Robots & Agent policy                                               ┃
#  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
#  ┃  Checkouts are for humans.                                           ┃
#  ┃  * Automated scraping, "buy-for-me" agents, or any end-to-end flow   ┃
#  ┃    that completes payment without a final human review step is not   ┃
#  ┃    permitted.                                                        ┃
#  ┃  * Legitimate integrators must use the official Checkout Kit:        ┃
#  ┃      https://www.shopify.com/checkout-kit                            ┃
#  ┃                                                                      ┃
#  ┃  Terms of Service: https://www.shopify.com/legal/terms               ┃
#  ┃  Contact: bots@shopify.com                                           ┃
#  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

User-agent: *
Disallow: /a/downloads/-/*
Disallow: /admin
Disallow: /cart
Disallow: /orders
Disallow: /checkouts/
Disallow: /checkout
Disallow: /49129095325/checkouts
Disallow: /49129095325/orders
Disallow: /carts
Disallow: /account
Disallow: /collections/*sort_by*
Disallow: /*/collections/*sort_by*
Disallow: /collections/*+*
Disallow: /collections/*%2B*
Disallow: /collections/*%2b*
Disallow: /*/collections/*+*
Disallow: /*/collections/*%2B*
Disallow: /*/collections/*%2b*
Disallow: */collections/*filter*&*filter*
Disallow: /blogs/*+*
Disallow: /blogs/*%2B*
Disallow: /blogs/*%2b*
Disallow: /*/blogs/*+*
Disallow: /*/blogs/*%2B*
Disallow: /*/blogs/*%2b*
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /policies/
Disallow: /*/policies/
Disallow: /*/*?*ls=*&ls=*
Disallow: /*/*?*ls%3D*%3Fls%3D*
Disallow: /*/*?*ls%3d*%3fls%3d*
Disallow: /search
Disallow: /sf_private_access_tokens
Disallow: /apple-app-site-association
Disallow: /.well-known/shopify/monorail
Disallow: /cdn/wpm/*.js
Disallow: /recommendations/products
Disallow: /*/recommendations/products
Disallow: /products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /collections/*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /*/collections/*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Sitemap: https://happimess.com/sitemap.xml

# Google adsbot ignores robots.txt unless specifically named!
User-agent: adsbot-google
Disallow: /checkouts/
Disallow: /checkout
Disallow: /carts
Disallow: /orders
Disallow: /49129095325/checkouts
Disallow: /49129095325/orders
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /cdn/wpm/*.js
Disallow: /products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /collections/*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /*/collections/*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /sf_private_access_tokens

User-agent: Nutch
Disallow: /

User-agent: AhrefsBot
Crawl-delay: 10
[...full Disallow list identical to User-agent: * block above, omitted for brevity...]
Sitemap: https://happimess.com/sitemap.xml

User-agent: AhrefsSiteAudit
Crawl-delay: 10
[...full Disallow list identical to User-agent: * block above, omitted for brevity...]
Sitemap: https://happimess.com/sitemap.xml

User-agent: MJ12bot
Crawl-delay: 10

User-agent: Pinterest
Crawl-delay: 1
```

**robots.txt Notes:**
- This is the default Shopify-generated robots.txt with the Shopify "Checkouts are for humans" policy header added — a Shopify platform-wide addition, not a custom Happimess configuration.
- The file is syntactically valid.
- No explicit entries for any AI crawler (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, OAI-SearchBot, CCBot).
- Sitemap is correctly referenced: `Sitemap: https://happimess.com/sitemap.xml`

---

## 3. Meta Robots / HTTP Header Findings by Page Type

| Page Type | URL Tested | Meta Robots Tag | Canonical Tag | Hreflang Tags | X-Robots-Tag Header |
|---|---|---|---|---|---|
| Homepage | `https://happimess.com` | Not found | Not found | Not found | Not confirmed |
| Product Page | `https://happimess.com/products/small-step-trash-can` | 404 — page not found | N/A | N/A | N/A |
| Blog Index | `https://happimess.com/blogs/news` | Not found | Not found | Not found | Not confirmed |
| Blog Article | `https://happimess.com/blogs/news/economy-home-decor-2025` | Not found | Not found | Not found | Not confirmed |
| FAQ Page | `https://happimess.com/pages/faqs` | Not found | Not found | Not found | Not confirmed |
| Collections | `https://happimess.com/collections/all` | Not found | Not found | Not found | Not confirmed |
| Policy Page | `https://happimess.com/policies/privacy-policy` | Not found | Not found | Not found | Not confirmed |

**Key Findings:**

1. **No meta robots tags found on any page tested.** This means all pages rely entirely on robots.txt and HTTP header directives for crawler control. The absence of meta robots is not itself a problem — it defaults to `index, follow` — but it means there is no page-level override capability currently implemented.

2. **No canonical tags detected on any page tested.** This is a significant gap on a Shopify store that serves both English and Spanish versions of the same pages. Without canonicals, crawlers may treat `/` and `/es/` as duplicate content. Shopify's default theme may inject canonical tags via JavaScript — which AI crawlers that do not execute JavaScript would not see. This needs verification at the raw HTML level.

3. **No hreflang tags found on any page tested.** For a bilingual EN/ES store this creates a language disambiguation problem for all crawlers including AI systems.

4. **Policy pages (e.g., `/policies/privacy-policy`) are accessible and serve full content despite being blocked in robots.txt.** The `Disallow: /policies/` directive tells crawlers not to fetch these pages, but the pages return 200 OK with full content when accessed directly. The robots.txt block is honored voluntarily by compliant crawlers — it is not enforced at the server level.

5. **The tested product URL (`/products/small-step-trash-can`) returned a 404.** This may indicate a slug change or product removal. Product page meta robots behavior could not be confirmed from this specific URL.

---

## 4. Sitemap Status

| Check | Result |
|---|---|
| Referenced in robots.txt | Yes — `Sitemap: https://happimess.com/sitemap.xml` |
| Accessible at `/sitemap.xml` | Yes — returns content |
| Sitemap type | Sitemap Index (8 child sitemaps) |
| Child sitemaps | Products (EN), Pages (EN), Collections (EN), Blogs (EN), Products (ES), Pages (ES), Collections (ES), Blogs (ES) |
| `<lastmod>` dates present | No — no lastmod tags in the index |
| URL count | Unknown (child sitemaps not individually fetched) |
| Target URL in sitemap | Likely yes for homepage; unconfirmed for specific pages |

**Issues:**
- No `<lastmod>` dates in the sitemap index. This weakens freshness signals for all crawlers. Google, Bing, and AI crawlers use lastmod to prioritize recrawling.
- Spanish sitemaps are present (EN/ES split), confirming the bilingual structure — but the absence of hreflang tags in page HTML means the sitemap alone is insufficient for language disambiguation.

---

## 5. llms.txt Status

| Check | Result |
|---|---|
| URL tested | `https://happimess.com/llms.txt` |
| HTTP Status | **404 — Not Found** |
| File exists | No |
| Content | None |

**Impact:** `llms.txt` is an emerging standard (proposed by Answer.AI / Jeremy Howard, 2024) that signals to AI systems which content is available, preferred for citation, and how the site is structured. Without it, AI crawlers must infer site structure from the sitemap and crawled content alone. The absence does not block access but represents a missed opportunity to guide AI citation behavior. OpenAI, Anthropic, and Perplexity crawlers have all shown responsiveness to this file.

---

## 6. Blocked Paths and Their AI Visibility Impact

| Blocked Path | Robots.txt Rule | Page Type | Content Value for AI | Impact Assessment |
|---|---|---|---|---|
| `/policies/` | `Disallow: /policies/` | Privacy Policy, Refund Policy, Terms of Service, Shipping Policy | MEDIUM — Policy pages build trust signals; AI systems (especially for shopping queries) often cite return/shipping policies | **Moderate negative impact.** AI crawlers that respect robots.txt (GPTBot, ClaudeBot, PerplexityBot) will not index these pages. A user asking "What is Happimess's return policy?" in ChatGPT or Perplexity will get no answer from the site's own pages. |
| `/*/policies/` | `Disallow: /*/policies/` | Spanish policy pages | MEDIUM | Same as above for Spanish-language queries. |
| `/search` | `Disallow: /search` | Search results pages | LOW — Search result pages have no unique content; blocking is correct | No impact — correct to block. |
| `/cart`, `/checkout`, `/checkouts/`, `/orders`, `/carts` | Multiple Disallow rules | Transactional pages | NONE — No content value for AI indexing | No impact — correct to block. |
| `/account` | `Disallow: /account` | User account pages | NONE | No impact — correct to block. |
| `/admin` | `Disallow: /admin` | Shopify admin | NONE | No impact — correct to block. |
| `/collections/*sort_by*` | `Disallow: /collections/*sort_by*` | Faceted collection pages | LOW — Duplicate of base collection with sort parameter | No impact — correct to block. |
| `/collections/*filter*&*filter*` | `Disallow: */collections/*filter*&*filter*` | Multi-filter collection pages | LOW | No impact — correct to block. |
| `/recommendations/products` | `Disallow: /recommendations/products` | Product recommendation API endpoint | NONE — JSON API, no human-readable content | No impact — correct to block. |
| `/cdn/wpm/*.js` | `Disallow: /cdn/wpm/*.js` | Shopify Web Pixel Manager scripts | NONE | No impact — correct to block. |
| `/*preview_theme_id*`, `/*preview_script_id*` | Disallow rules | Shopify theme preview URLs | NONE | No impact — correct to block. |

**Summary of AI-Impacting Blocks:**

The only robotted path with meaningful AI visibility impact is `/policies/`. All other blocked paths are transactional, administrative, or duplicate-content URLs where blocking is appropriate and beneficial.

**Recommended Action:** Remove `Disallow: /policies/` and `Disallow: /*/policies/` from robots.txt. Policy pages — particularly the refund policy, shipping policy, and privacy policy — are exactly the type of trust-signal content that AI systems surface when consumers ask shopping-intent questions like "Does Happimess offer free returns?" or "What is Happimess's shipping policy?". Keeping them blocked forfeits this citation opportunity to competitors who have unblocked policy pages.

---

## 7. Ready-to-Deploy robots.txt.liquid Fix

The following is the complete recommended `robots.txt.liquid` for Shopify 2.0. It:
- Removes `Disallow: /policies/` and `Disallow: /*/policies/`
- Adds explicit Allow rules for all major AI crawlers (belt-and-suspenders alongside the wildcard)
- Adds explicit named entries for GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot, Google-Extended with targeted Disallow rules only for checkout/transactional paths
- Retains all existing Shopify-appropriate blocks
- Adds a reference to `llms.txt` once it is deployed
- Preserves the Shopify "Checkouts are for humans" policy header

```liquid
# we use Shopify as our ecommerce platform

#  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#  ┃  Robots & Agent policy                                               ┃
#  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
#  ┃  Checkouts are for humans.                                           ┃
#  ┃  * Automated scraping, "buy-for-me" agents, or any end-to-end flow   ┃
#  ┃    that completes payment without a final human review step is not   ┃
#  ┃    permitted.                                                        ┃
#  ┃  * Legitimate integrators must use the official Checkout Kit:        ┃
#  ┃      https://www.shopify.com/checkout-kit                            ┃
#  ┃                                                                      ┃
#  ┃  Terms of Service: https://www.shopify.com/legal/terms               ┃
#  ┃  Contact: bots@shopify.com                                           ┃
#  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# ---------------------------------------------------------------------------
# AI CRAWLERS — explicitly named for clarity and future control
# Allow: products, collections, pages, blogs, policies
# Disallow: only transactional / checkout paths
# ---------------------------------------------------------------------------

User-agent: GPTBot
Disallow: /a/downloads/-/*
Disallow: /admin
Disallow: /cart
Disallow: /orders
Disallow: /checkouts/
Disallow: /checkout
Disallow: /{{ shop.id }}/checkouts
Disallow: /{{ shop.id }}/orders
Disallow: /carts
Disallow: /account
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /sf_private_access_tokens
Disallow: /.well-known/shopify/monorail
Disallow: /cdn/wpm/*.js
Disallow: /recommendations/products
Disallow: /*/recommendations/products
Allow: /products/
Allow: /collections/
Allow: /pages/
Allow: /blogs/
Allow: /policies/

User-agent: OAI-SearchBot
Disallow: /a/downloads/-/*
Disallow: /admin
Disallow: /cart
Disallow: /orders
Disallow: /checkouts/
Disallow: /checkout
Disallow: /{{ shop.id }}/checkouts
Disallow: /{{ shop.id }}/orders
Disallow: /carts
Disallow: /account
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /sf_private_access_tokens
Disallow: /.well-known/shopify/monorail
Disallow: /cdn/wpm/*.js
Disallow: /recommendations/products
Disallow: /*/recommendations/products
Allow: /products/
Allow: /collections/
Allow: /pages/
Allow: /blogs/
Allow: /policies/

User-agent: PerplexityBot
Disallow: /a/downloads/-/*
Disallow: /admin
Disallow: /cart
Disallow: /orders
Disallow: /checkouts/
Disallow: /checkout
Disallow: /{{ shop.id }}/checkouts
Disallow: /{{ shop.id }}/orders
Disallow: /carts
Disallow: /account
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /sf_private_access_tokens
Disallow: /.well-known/shopify/monorail
Disallow: /cdn/wpm/*.js
Disallow: /recommendations/products
Disallow: /*/recommendations/products
Allow: /products/
Allow: /collections/
Allow: /pages/
Allow: /blogs/
Allow: /policies/

User-agent: ClaudeBot
Disallow: /a/downloads/-/*
Disallow: /admin
Disallow: /cart
Disallow: /orders
Disallow: /checkouts/
Disallow: /checkout
Disallow: /{{ shop.id }}/checkouts
Disallow: /{{ shop.id }}/orders
Disallow: /carts
Disallow: /account
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /sf_private_access_tokens
Disallow: /.well-known/shopify/monorail
Disallow: /cdn/wpm/*.js
Disallow: /recommendations/products
Disallow: /*/recommendations/products
Allow: /products/
Allow: /collections/
Allow: /pages/
Allow: /blogs/
Allow: /policies/

User-agent: Google-Extended
Disallow: /a/downloads/-/*
Disallow: /admin
Disallow: /cart
Disallow: /orders
Disallow: /checkouts/
Disallow: /checkout
Disallow: /{{ shop.id }}/checkouts
Disallow: /{{ shop.id }}/orders
Disallow: /carts
Disallow: /account
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /sf_private_access_tokens
Disallow: /.well-known/shopify/monorail
Disallow: /cdn/wpm/*.js
Disallow: /recommendations/products
Disallow: /*/recommendations/products
Allow: /products/
Allow: /collections/
Allow: /pages/
Allow: /blogs/
Allow: /policies/

# ---------------------------------------------------------------------------
# ALL OTHER CRAWLERS (Googlebot, Bingbot, CCBot, Applebot, DuckDuckBot, etc.)
# ---------------------------------------------------------------------------

User-agent: *
Disallow: /a/downloads/-/*
Disallow: /admin
Disallow: /cart
Disallow: /orders
Disallow: /checkouts/
Disallow: /checkout
Disallow: /{{ shop.id }}/checkouts
Disallow: /{{ shop.id }}/orders
Disallow: /carts
Disallow: /account
Disallow: /collections/*sort_by*
Disallow: /*/collections/*sort_by*
Disallow: /collections/*+*
Disallow: /collections/*%2B*
Disallow: /collections/*%2b*
Disallow: /*/collections/*+*
Disallow: /*/collections/*%2B*
Disallow: /*/collections/*%2b*
Disallow: */collections/*filter*&*filter*
Disallow: /blogs/*+*
Disallow: /blogs/*%2B*
Disallow: /blogs/*%2b*
Disallow: /*/blogs/*+*
Disallow: /*/blogs/*%2B*
Disallow: /*/blogs/*%2b*
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /*/*?*ls=*&ls=*
Disallow: /*/*?*ls%3D*%3Fls%3D*
Disallow: /*/*?*ls%3d*%3fls%3d*
Disallow: /search
Disallow: /sf_private_access_tokens
Disallow: /apple-app-site-association
Disallow: /.well-known/shopify/monorail
Disallow: /cdn/wpm/*.js
Disallow: /recommendations/products
Disallow: /*/recommendations/products
Disallow: /products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /collections/*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /*/collections/*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote

# ---------------------------------------------------------------------------
# RATE-LIMITED BOTS
# ---------------------------------------------------------------------------

# Google adsbot ignores robots.txt unless specifically named!
User-agent: adsbot-google
Disallow: /checkouts/
Disallow: /checkout
Disallow: /carts
Disallow: /orders
Disallow: /{{ shop.id }}/checkouts
Disallow: /{{ shop.id }}/orders
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /cdn/wpm/*.js
Disallow: /products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /collections/*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /*/collections/*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /sf_private_access_tokens

User-agent: Nutch
Disallow: /

User-agent: AhrefsBot
Crawl-delay: 10
Disallow: /a/downloads/-/*
Disallow: /admin
Disallow: /cart
Disallow: /orders
Disallow: /checkouts/
Disallow: /checkout
Disallow: /{{ shop.id }}/checkouts
Disallow: /{{ shop.id }}/orders
Disallow: /carts
Disallow: /account
Disallow: /collections/*sort_by*
Disallow: /*/collections/*sort_by*
Disallow: /collections/*+*
Disallow: /collections/*%2B*
Disallow: /collections/*%2b*
Disallow: /*/collections/*+*
Disallow: /*/collections/*%2B*
Disallow: /*/collections/*%2b*
Disallow: */collections/*filter*&*filter*
Disallow: /blogs/*+*
Disallow: /blogs/*%2B*
Disallow: /blogs/*%2b*
Disallow: /*/blogs/*+*
Disallow: /*/blogs/*%2B*
Disallow: /*/blogs/*%2b*
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /policies/
Disallow: /*/policies/
Disallow: /*/*?*ls=*&ls=*
Disallow: /*/*?*ls%3D*%3Fls%3D*
Disallow: /*/*?*ls%3d*%3fls%3d*
Disallow: /search
Disallow: /sf_private_access_tokens
Disallow: /apple-app-site-association
Disallow: /.well-known/shopify/monorail
Disallow: /cdn/wpm/*.js
Disallow: /recommendations/products
Disallow: /*/recommendations/products
Disallow: /products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /collections/*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /*/collections/*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Sitemap: https://happimess.com/sitemap.xml

User-agent: AhrefsSiteAudit
Crawl-delay: 10
Disallow: /a/downloads/-/*
Disallow: /admin
Disallow: /cart
Disallow: /orders
Disallow: /checkouts/
Disallow: /checkout
Disallow: /{{ shop.id }}/checkouts
Disallow: /{{ shop.id }}/orders
Disallow: /carts
Disallow: /account
Disallow: /collections/*sort_by*
Disallow: /*/collections/*sort_by*
Disallow: /collections/*+*
Disallow: /collections/*%2B*
Disallow: /collections/*%2b*
Disallow: /*/collections/*+*
Disallow: /*/collections/*%2B*
Disallow: /*/collections/*%2b*
Disallow: */collections/*filter*&*filter*
Disallow: /blogs/*+*
Disallow: /blogs/*%2B*
Disallow: /blogs/*%2b*
Disallow: /*/blogs/*+*
Disallow: /*/blogs/*%2B*
Disallow: /*/blogs/*%2b*
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /policies/
Disallow: /*/policies/
Disallow: /*/*?*ls=*&ls=*
Disallow: /*/*?*ls%3D*%3Fls%3D*
Disallow: /*/*?*ls%3d*%3fls%3d*
Disallow: /search
Disallow: /sf_private_access_tokens
Disallow: /apple-app-site-association
Disallow: /.well-known/shopify/monorail
Disallow: /cdn/wpm/*.js
Disallow: /recommendations/products
Disallow: /*/recommendations/products
Disallow: /products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /collections/*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Disallow: /*/collections/*/products/*-[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]-remote
Sitemap: https://happimess.com/sitemap.xml

User-agent: MJ12bot
Crawl-delay: 10

User-agent: Pinterest
Crawl-delay: 1

# ---------------------------------------------------------------------------
# SITEMAPS
# ---------------------------------------------------------------------------

Sitemap: https://happimess.com/sitemap.xml
# Uncomment the line below once llms.txt is deployed:
# llms.txt: https://happimess.com/llms.txt
```

**Notes on the liquid template:**

- `{{ shop.id }}` resolves to the numeric Shopify store ID (currently `49129095325`). Using the variable is cleaner and future-proof if the store ever migrates.
- The `# llms.txt:` line is a comment — `llms.txt` is not a robots.txt directive and belongs as a separate file, not embedded in robots.txt. The comment is a deployment reminder only.
- AI crawler sections deliberately omit the `Disallow: /policies/` and `Disallow: /*/policies/` rules. The `User-agent: *` section also has these lines removed.
- AhrefsBot and AhrefsSiteAudit retain the `/policies/` Disallow since these are SEO crawlers, not AI citation tools, and keeping them off policy pages reduces unnecessary crawl budget on content that doesn't aid SEO audits.

---

## 8. Implementation Instructions for Shopify

### Step 1: Access robots.txt in Shopify Admin

Shopify 2.0 themes expose robots.txt as a Liquid template. Navigate to:

**Shopify Admin → Online Store → Themes → [Your active theme] → Edit Code**

In the file tree, look under **Templates** for `robots.txt.liquid`. If it does not exist:

1. Click "Add a new template"
2. Select template type: `robots.txt`
3. Shopify will create `robots.txt.liquid` with the default content

### Step 2: Replace the content

Replace the full content of `robots.txt.liquid` with the template from Section 7 above.

**Important:** Do not use the Shopify "Edit robots.txt" shortcut in the Preferences panel — that is a limited editor. Use the full Edit Code interface for the complete template replacement.

### Step 3: Verify the change

After saving:
1. Visit `https://happimess.com/robots.txt` in a browser
2. Confirm the new AI crawler sections (GPTBot, ClaudeBot, etc.) are present
3. Confirm `Disallow: /policies/` is gone from the `User-agent: *` block
4. Use Google Search Console → URL Inspection to test `https://happimess.com/policies/privacy-policy` — it should now show as "Allowed to crawl"

### Step 4: Deploy llms.txt (separate task)

The robots.txt fix above does not deploy `llms.txt`. That requires a separate step:

1. Create `llms.txt` content (use the `/geo-llmstxt` skill to generate it)
2. Upload to **Shopify Admin → Content → Files** → Upload File
3. Note the CDN URL Shopify assigns (format: `https://cdn.shopify.com/s/files/...`)
4. Create a Shopify page at a custom URL, or use a URL redirect in **Admin → Online Store → Navigation → URL Redirects** to redirect `/llms.txt` → the CDN URL

The redirect method is the simplest: set a 301 from `/llms.txt` to the Shopify Files CDN URL. AI crawlers will follow the redirect.

### Step 5: Add lastmod dates to sitemap (optional, moderate effort)

Shopify's default sitemap does not include `<lastmod>` dates. To add them requires either:
- A third-party Shopify SEO app (e.g., SEO Manager, Plug in SEO) that regenerates the sitemap with dates
- A custom `sitemap.xml.liquid` template (advanced)

This is lower priority than the robots.txt and llms.txt fixes but worth scheduling in a future sprint.

---

## 9. Priority Action Items

| Priority | Action | Effort | Expected Impact |
|---|---|---|---|
| 1 — CRITICAL | Remove `Disallow: /policies/` from robots.txt (both `User-agent: *` and `User-agent: */`) | 10 min | Policy pages become citable by all AI crawlers — directly enables "What is Happimess's return/shipping policy?" answers in ChatGPT, Perplexity, Gemini |
| 2 — HIGH | Add explicit AI crawler sections (GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, Google-Extended) per template in Section 7 | 15 min | Explicit intent signals; enables granular future control without silent wildcard reliance |
| 3 — HIGH | Deploy `llms.txt` at `https://happimess.com/llms.txt` | 1–2 hours | Guides AI citation priorities; signals preferred brand description and key pages to AI systems |
| 4 — MEDIUM | Add `<link rel="canonical">` tags to all page templates (Shopify theme.liquid / page templates) | 2–4 hours | Resolves EN/ES duplicate content ambiguity for all crawlers |
| 5 — MEDIUM | Add `<link rel="alternate" hreflang="en" ...>` and `<link rel="alternate" hreflang="es" ...>` tags | 2–4 hours | Correct language serving for multilingual queries across all crawlers |
| 6 — LOW | Add `<lastmod>` dates to XML sitemap | 4–8 hours (app or custom template) | Improves recrawl prioritization for fresh content; helps blog posts get re-indexed after updates |

---

*Report generated: April 15, 2026*
*Source data: Live fetches from happimess.com*
*File: D:\Marketing\Happimess\GEO-CRAWLER-ACCESS.md*
