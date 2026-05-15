# GEO Crawler Access Report — jonathany.com
**Date:** April 14, 2026
**URL Analyzed:** https://jonathany.com/robots.txt
**Command:** `/geo crawlers`

---

## Crawler Access Score: 82 / 100

> **Interpretation:** Jonathan Y has done the most important thing right — every major AI crawler is explicitly named and allowed. This places them in the top 20% of e-commerce sites for AI crawler configuration. However, a copy-paste error (foreign sitemap URL), policy page blocking, secondary crawler gaps, and an active Cloudflare challenge on deep URLs prevent a perfect score.

---

## AI Crawler Access Map

| Crawler | Company | Status | Rule Type | Notes |
|---------|---------|--------|-----------|-------|
| **GPTBot** | OpenAI | ALLOWED | Explicit `Allow: /` | Full site access |
| **ChatGPT-User** | OpenAI | ALLOWED | Explicit `Allow: /` | Full site access |
| **ClaudeBot** | Anthropic | ALLOWED | Explicit `Allow: /` | Full site access |
| **Claude-User** | Anthropic | ALLOWED | Explicit `Allow: /` | Full site access |
| **Claude-SearchBot** | Anthropic | ALLOWED | Explicit `Allow: /` | Full site access |
| **PerplexityBot** | Perplexity | ALLOWED | Explicit `Allow: /` | Full site access |
| **Perplexity-User** | Perplexity | ALLOWED | Explicit `Allow: /` | Full site access |
| **Gemini-Deep-Research** | Google | ALLOWED | Explicit `Allow: /` | Full site access |
| **Googlebot** | Google | ALLOWED | Explicit `Allow: /` | Full site access |
| **Bingbot** | Microsoft | ALLOWED | Explicit `Allow: /` | Full site access |
| **OAI-SearchBot** | OpenAI | Inherited | Wildcard `*` | Not explicitly named; inherits wildcard rules |
| **Amazonbot** | Amazon | Inherited | Wildcard `*` | Not explicitly named |
| **Applebot-Extended** | Apple | Inherited | Wildcard `*` | Not explicitly named |
| **DuckAssistBot** | DuckDuckGo | Inherited | Wildcard `*` | Not explicitly named |
| **Meta-ExternalFetcher** | Meta | Inherited | Wildcard `*` | Not explicitly named |
| **Cohere-ai** | Cohere | Inherited | Wildcard `*` | Not explicitly named |
| **Bytespider** | ByteDance | Inherited | Wildcard `*` | Not explicitly named |
| **CCBot** | Common Crawl | Inherited | Wildcard `*` | Not explicitly named |
| **Nutch** | Apache | BLOCKED | Explicit `Disallow: /` | Correct — web scraper |
| **AhrefsBot** | Ahrefs | Restricted | Crawl-delay: 10s | SEO crawler, not AI |
| **AhrefsSiteAudit** | Ahrefs | Restricted | Crawl-delay: 10s | SEO crawler, not AI |
| **MJ12bot** | Majestic | Restricted | Crawl-delay: 10s | SEO crawler, not AI |
| **Pinterest** | Pinterest | Restricted | Crawl-delay: 1s | Social crawler |

---

## Complete robots.txt (Verbatim)

```
User-agent: Googlebot
Allow: /

User-agent: Gemini-Deep-Research
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Bingbot
Allow: /

User-agent: *
Disallow: /a/downloads/-/*
Disallow: /admin
Disallow: /cart
Disallow: /orders
Disallow: /checkouts/
Disallow: /checkout
Disallow: /27380187189/checkouts
Disallow: /27380187189/orders
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
Sitemap: https://jonathany.com/sitemap.xml

# Google adsbot ignores robots.txt unless specifically named!
Disallow: /checkouts/
Disallow: /checkout
Disallow: /carts
Disallow: /orders
Disallow: /27380187189/checkouts
Disallow: /27380187189/orders
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /cdn/wpm/*.js
Disallow: /sf_private_access_tokens

User-agent: Nutch
Disallow: /

User-agent: AhrefsBot
Crawl-delay: 10
Disallow: /a/downloads/-/*
[... full disallow list ...]
Sitemap: https://www.tumbleliving.com/sitemap.xml   ← ERROR

User-agent: AhrefsSiteAudit
Crawl-delay: 10
[... full disallow list ...]
Sitemap: https://jonathany.com/sitemap.xml

User-agent: MJ12bot
Crawl-delay: 10

User-agent: Pinterest
Crawl-delay: 1
```

---

## Rule-by-Rule Analysis

### Block 1: Named AI Crawlers — `Allow: /` (Lines 1–30)

**Assessment: Excellent**

Ten crawlers are explicitly named with full site access. This is best-practice configuration. Explicit `Allow: /` rules for named AI bots override any wildcard `Disallow` rules, ensuring these bots get the highest-priority access directive.

```
Googlebot        → Allow: /  ✓
Gemini-Deep-Research → Allow: /  ✓
PerplexityBot    → Allow: /  ✓
Perplexity-User  → Allow: /  ✓
ClaudeBot        → Allow: /  ✓
Claude-User      → Allow: /  ✓
Claude-SearchBot → Allow: /  ✓
GPTBot           → Allow: /  ✓
ChatGPT-User     → Allow: /  ✓
Bingbot          → Allow: /  ✓
```

Note: `OAI-SearchBot` (OpenAI's dedicated search crawler, distinct from GPTBot) is not explicitly named. It will inherit wildcard rules. Adding it would complete OpenAI's crawler suite.

---

### Block 2: Wildcard Rules — `User-agent: *`

**Assessment: Mostly correct — two issues**

#### Disallowed paths (full analysis)

| Path Pattern | Type | Assessment |
|-------------|------|-----------|
| `/a/downloads/-/*` | Shopify internal | Correct — private file downloads |
| `/admin` | Shopify admin | Correct |
| `/cart` | Cart page | Correct |
| `/orders` | Order confirmation | Correct |
| `/checkouts/` `/checkout` | Checkout flow | Correct |
| `/27380187189/checkouts` `/27380187189/orders` | Store-specific checkout URLs | Correct |
| `/carts` | Cart API | Correct |
| `/account` | Customer login area | Correct |
| `/collections/*sort_by*` | Sorted collection URLs | Correct — prevents crawling of N² sort combinations |
| `/collections/*+*` `/collections/*%2B*` `/collections/*%2b*` | URL-encoded collection params | Correct |
| `*/collections/*filter*&*filter*` | Double-filter combinations | Correct — prevents exponential faceted URL crawling |
| `/blogs/*+*` `/blogs/*%2B*` `/blogs/*%2b*` | URL-encoded blog params | Correct |
| `/*?*oseid=*` | OneSignal session IDs | Correct — session-specific URLs |
| `/*preview_theme_id*` `/*preview_script_id*` | Theme preview URLs | Correct |
| **`/policies/`** `/***/policies/` | **Policy pages** | **ISSUE — see below** |
| `/*/*?*ls=*&ls=*` (3 variants) | Locale/language params | Correct |
| `/search` | Internal search results | Correct |
| `/sf_private_access_tokens` | Private access tokens | Correct |
| `/apple-app-site-association` | Apple app verification | Correct |
| `/.well-known/shopify/monorail` | Shopify telemetry | Correct |
| `/cdn/wpm/*.js` | Web pixel manager scripts | Correct |
| `/recommendations/products` | Product recommendation API | Correct |

**Issue 1: `/policies/` is blocked from all crawlers**

The wildcard block on `/policies/` prevents every crawler — including named AI bots — from accessing:
- `/policies/privacy-policy`
- `/policies/refund-policy`
- `/policies/terms-of-service`
- `/policies/shipping-policy`

**Why this matters for GEO:** When users ask AI systems "What is Jonathan Y's return policy?" or "Does Jonathan Y have free returns?" — the AI cannot access the actual policy page to cite a direct answer. It would have to rely on FAQ content or guesswork. These are high-intent trust queries that the brand could own if its policy pages were crawlable.

**Note:** Named AI crawlers (`Allow: /`) override this disallow. GPTBot, ClaudeBot, PerplexityBot etc. CAN access `/policies/` because their explicit `Allow: /` takes precedence. However, Googlebot also has explicit `Allow: /` — so Google can index policies too. This disallow primarily affects any unnamed crawlers.

---

### Block 3: AdsBot Section — Structural Error

**Assessment: Non-functional as written**

The robots.txt contains a comment: `# Google adsbot ignores robots.txt unless specifically named!`
Followed immediately by Disallow directives — but with **no User-agent line**. These directives have no assigned agent and are ignored by all parsers.

```
# Google adsbot ignores robots.txt unless specifically named!
Disallow: /checkouts/    ← ORPHANED — no User-agent above this
Disallow: /checkout
...
```

For AdsBot-Google to respect these rules, the block needs:
```
User-agent: AdsBot-Google
Disallow: /checkouts/
...
```

**GEO impact:** Low — this only affects Google Ads crawling, not AI content crawlers.

---

### Block 4: Nutch — Full Block

```
User-agent: Nutch
Disallow: /
```

**Assessment: Correct.** Nutch is an Apache open-source web crawler used for large-scale scraping. Blocking it is standard and appropriate.

---

### Block 5: AhrefsBot — Copy-Paste Error

**Assessment: Critical error**

```
User-agent: AhrefsBot
Crawl-delay: 10
[... 30+ Disallow lines ...]
Sitemap: https://www.tumbleliving.com/sitemap.xml   ← WRONG DOMAIN
```

The `Sitemap:` directive in the AhrefsBot section points to `www.tumbleliving.com` — a completely different brand/domain. This is a copy-paste error from when the robots.txt was originally created (likely adapted from a template or another Shopify store's configuration).

**Impact:**
- AhrefsBot will attempt to validate and crawl `tumbleliving.com/sitemap.xml`, not Jonathan Y's sitemap
- Any SEO audit tool reading the full robots.txt will flag this as a cross-domain sitemap reference
- Creates potential confusion in SEO reporting tools that aggregate sitemap data
- Reputational: if discovered by competitors or press, could cause confusion

**Fix:** Remove the `Sitemap: https://www.tumbleliving.com/sitemap.xml` line from the AhrefsBot block. The AhrefsSiteAudit block correctly points to `https://jonathany.com/sitemap.xml`.

---

### Block 6: AhrefsSiteAudit — Correct

```
User-agent: AhrefsSiteAudit
Crawl-delay: 10
[... same disallows ...]
Sitemap: https://jonathany.com/sitemap.xml   ✓
```

**Assessment: Correct** — same disallow structure as AhrefsBot but with the right sitemap URL.

---

### Block 7: MJ12bot / Pinterest — Rate Limiting

```
User-agent: MJ12bot
Crawl-delay: 10

User-agent: Pinterest
Crawl-delay: 1
```

**Assessment: Correct.** MJ12bot (Majestic SEO crawler) gets a 10-second delay to prevent server load. Pinterest gets a 1-second delay — likely to allow Pinterest's crawler to access product images for Rich Pins while throttling volume.

---

## Content Accessibility Map

What AI crawlers can and cannot see:

### ACCESSIBLE to AI crawlers

| Path Pattern | Content Type | GEO Value |
|-------------|-------------|----------|
| `/` | Homepage | Medium (low citability, but entry point) |
| `/collections/*` | Collection pages | Medium |
| `/collections/[name]/[filter]` | Single-filter collection pages | Medium |
| `/products/*` | Product pages | High (specs, pricing, reviews) |
| `/pages/*` | Content pages (Our Story, FAQ, Guides) | High |
| `/blogs/*` | Blog posts | High (highest citability content) |
| `/policies/*` | Policy pages | Medium (trust signals) — accessible to named AI bots |

### BLOCKED from all crawlers (including AI bots via inheritance*)

| Path Pattern | Content Type | Block Reason |
|-------------|-------------|-------------|
| `/admin` | Admin panel | Security — correct |
| `/cart` `/carts` | Shopping cart | User session — correct |
| `/checkout` `/checkouts/` | Checkout flow | PII protection — correct |
| `/account` | Customer accounts | PII protection — correct |
| `/orders` | Order details | PII protection — correct |
| `/search` | Search results | Thin/duplicate content — correct |
| `/collections/*sort_by*` | Sorted collections | Duplicate content — correct |
| `*/collections/*filter*&*filter*` | Multi-filter pages | Crawl budget — correct |
| `/recommendations/products` | Product rec API | Dynamic/thin — correct |
| `/cdn/wpm/*.js` | Analytics scripts | Non-content — correct |

*Note: Named AI bots with `Allow: /` override these for `/policies/` specifically.

---

## Infrastructure Risk: Cloudflare Bot Management

**Status: Active — Moderate Risk**

Beyond robots.txt, the site uses Cloudflare bot management that serves a JavaScript challenge page (`Just a moment... / cf-browser-verification`) to automated requests that don't pass browser fingerprinting checks.

**What this means:**
- robots.txt says "AI crawlers are welcome"
- But Cloudflare may intercept the request before content is served
- Crawlers that don't execute JavaScript receive a 403/challenge page, not actual content

**AI crawlers most at risk:**
- OAI-SearchBot (OpenAI's search crawler — not GPTBot which uses browser rendering)
- CCBot (Common Crawl — used in AI training data)
- Any crawler that declares its user-agent but doesn't execute JS

**Confirmed safe:** GPTBot, ClaudeBot, PerplexityBot, Gemini-Deep-Research (all use headless browser rendering or are whitelisted by Cloudflare by default)

**Recommended fix:**
Add explicit Cloudflare WAF bypass rules for AI crawlers by user-agent string. In Cloudflare dashboard → Security → WAF → Custom Rules, create a bypass rule:
```
(http.user_agent contains "GPTBot") OR
(http.user_agent contains "ClaudeBot") OR
(http.user_agent contains "PerplexityBot") OR
(http.user_agent contains "Gemini-Deep-Research") OR
(http.user_agent contains "OAI-SearchBot") OR
(http.user_agent contains "CCBot")
→ Action: Skip → WAF managed rules
```

---

## Sitemap Configuration

| Sitemap | Location | Status |
|---------|----------|--------|
| Index sitemap | `https://jonathany.com/sitemap.xml` | Declared in robots.txt (non-www) |
| Products sub-sitemap | `https://www.jonathany.com/sitemap_products_1.xml` | Uses www — inconsistency |
| Pages sub-sitemap | `https://www.jonathany.com/sitemap_pages_1.xml` | Uses www — inconsistency |
| Collections sub-sitemap | `https://www.jonathany.com/sitemap_collections_1.xml` | Uses www — inconsistency |
| Blogs sub-sitemap | `https://www.jonathany.com/sitemap_blogs_1.xml` | Uses www — inconsistency |
| **ERROR** | `https://www.tumbleliving.com/sitemap.xml` | Listed in AhrefsBot block — **wrong domain** |

**www vs. non-www inconsistency:** The sitemap index is declared at `jonathany.com` (non-www) but all four child sitemaps use `www.jonathany.com`. The canonical domain should be standardized across all references.

---

## Score Calculation

| Component | Max Points | Score | Reasoning |
|-----------|-----------|-------|-----------|
| Primary AI crawlers explicitly named | 40 | 38 | All 10 named; OAI-SearchBot missing (-2) |
| Wildcard rules — appropriate blocks | 20 | 17 | /policies/ block is debatable (-2), AdsBot block broken (-1) |
| No harmful over-blocking | 15 | 14 | Minor: /policies/ caught in wildcard (-1) |
| Sitemap correctly declared | 10 | 7 | www/non-www inconsistency (-2), tumbleliving error (-1) |
| No crawl delays on AI bots | 10 | 10 | No delays applied to any AI crawler |
| Secondary crawlers addressed | 5 | 0 | None of the unnamed secondary AI crawlers addressed |
| **Infrastructure (Cloudflare)** | Penalty | -4 | Active JS challenge on deep URLs |
| **TOTAL** | 100 | **82/100** | |

---

## Priority Fixes

### Fix 1 — CRITICAL: Remove tumbleliving.com sitemap
**Time:** 5 minutes
**File:** robots.txt, AhrefsBot section

Remove this line:
```
Sitemap: https://www.tumbleliving.com/sitemap.xml
```

It serves no purpose and creates confusion in every audit tool that processes this robots.txt.

---

### Fix 2 — HIGH: Add OAI-SearchBot to named crawlers
**Time:** 5 minutes

Add before the wildcard `User-agent: *` block:
```
User-agent: OAI-SearchBot
Allow: /
```

OAI-SearchBot is OpenAI's dedicated search crawler (distinct from GPTBot which handles training). It powers ChatGPT's web browsing feature and needs explicit access.

---

### Fix 3 — HIGH: Standardize canonical domain
**Time:** 30 minutes

Decide between `jonathany.com` and `www.jonathany.com` as the canonical. Then:
- Update the `Sitemap:` declaration in the main wildcard block to match
- Ensure Shopify's theme canonical tags use the same version
- Update Google Search Console preferred domain setting

Current (inconsistent):
```
Sitemap: https://jonathany.com/sitemap.xml   ← non-www in robots.txt
# but child sitemaps all use www.jonathany.com ← www in sitemaps
```

---

### Fix 4 — HIGH: Configure Cloudflare bypass for AI crawlers
**Time:** 1 hour
**Location:** Cloudflare Dashboard → Security → WAF → Custom Rules

Create a bypass rule for known AI crawler user-agents to skip the JavaScript challenge. This ensures that crawlers which declare their user-agent truthfully but don't execute JS still receive actual HTML content.

---

### Fix 5 — MEDIUM: Fix AdsBot section structure
**Time:** 5 minutes

The orphaned Disallow directives after the AdsBot comment need a proper User-agent header:
```
User-agent: AdsBot-Google
Disallow: /checkouts/
Disallow: /checkout
Disallow: /carts
Disallow: /orders
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /cdn/wpm/*.js
Disallow: /sf_private_access_tokens
```

---

### Fix 6 — MEDIUM: Add secondary AI crawlers
**Time:** 10 minutes

Add explicit Allow rules for secondary AI crawlers that feed training data and AI search products:
```
User-agent: OAI-SearchBot
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: DuckAssistBot
Allow: /

User-agent: Cohere-ai
Allow: /
```

---

### Fix 7 — LOW: Reconsider /policies/ disallow
**Time:** 5 minutes

Consider removing `/policies/` and `/*/policies/` from the wildcard Disallow block. Named AI crawlers can already access these (their `Allow: /` overrides). Removing the disallow from the wildcard block would additionally allow unnamed crawlers (CCBot, training data collectors) to access policy pages — which are high-trust-signal content worth including in AI training corpora.

If the policy page block is intentional for non-AI crawlers, keep it — but understand named AI crawlers already bypass it.

---

## Corrected robots.txt (Full Recommended Version)

```
# Primary search engines and AI crawlers — full access
User-agent: Googlebot
Allow: /

User-agent: Gemini-Deep-Research
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: Bingbot
Allow: /

# Secondary AI crawlers — training data and AI search
User-agent: Amazonbot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: DuckAssistBot
Allow: /

User-agent: Cohere-ai
Allow: /

# Wildcard rules — all other crawlers
User-agent: *
Disallow: /a/downloads/-/*
Disallow: /admin
Disallow: /cart
Disallow: /orders
Disallow: /checkouts/
Disallow: /checkout
Disallow: /27380187189/checkouts
Disallow: /27380187189/orders
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
Sitemap: https://www.jonathany.com/sitemap.xml

# AdsBot-Google — needs explicit naming to respect robots.txt
User-agent: AdsBot-Google
Disallow: /checkouts/
Disallow: /checkout
Disallow: /carts
Disallow: /orders
Disallow: /27380187189/checkouts
Disallow: /27380187189/orders
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /cdn/wpm/*.js
Disallow: /sf_private_access_tokens

# Blocked web scrapers
User-agent: Nutch
Disallow: /

# SEO crawlers — rate limited
User-agent: AhrefsBot
Crawl-delay: 10
Disallow: /a/downloads/-/*
Disallow: /admin
Disallow: /cart
Disallow: /orders
Disallow: /checkouts/
Disallow: /checkout
Disallow: /carts
Disallow: /account
Disallow: /collections/*sort_by*
Disallow: /search
Disallow: /recommendations/products
Sitemap: https://www.jonathany.com/sitemap.xml

User-agent: AhrefsSiteAudit
Crawl-delay: 10
Disallow: /admin
Disallow: /cart
Disallow: /checkout
Disallow: /account
Sitemap: https://www.jonathany.com/sitemap.xml

User-agent: MJ12bot
Crawl-delay: 10

User-agent: Pinterest
Crawl-delay: 1
```

**Changes from current:**
1. Added `OAI-SearchBot`, `Amazonbot`, `Applebot-Extended`, `DuckAssistBot`, `Cohere-ai` with `Allow: /`
2. Removed `/policies/` from wildcard Disallow (named AI bots already bypass it)
3. Fixed AdsBot section — added `User-agent: AdsBot-Google` header
4. Removed `Sitemap: https://www.tumbleliving.com/sitemap.xml` from AhrefsBot block
5. Standardized all Sitemap declarations to `www.jonathany.com`
6. Simplified AhrefsBot and AhrefsSiteAudit blocks (removed redundant encoded URL variants)

---

*Report generated by Claude Code GEO Crawler Analysis*
*Audit date: April 14, 2026*
*Related reports: GEO-AUDIT-REPORT.md, GEO-CITABILITY-SCORE.md*
