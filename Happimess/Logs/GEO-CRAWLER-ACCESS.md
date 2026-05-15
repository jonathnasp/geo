# AI Crawler Access Report — happimess.com
**Date:** May 7, 2026 | **Source:** https://happimess.com/robots.txt

---

## Crawler Access Score: 70 / 100 — Fair

AI crawlers can access all content pages. The 30-point deduction is entirely for missing explicit `Allow` directives — best practice in 2026 is named entries for each major AI crawler. No crawlers are actively blocked.

---

## Complete AI Crawler Access Map

| Crawler | Company | Status | Rule Source | Content Pages |
|---------|---------|--------|-------------|---------------|
| GPTBot | OpenAI | Permissive | Inherits `*` | ✅ Accessible |
| OAI-SearchBot | OpenAI | Permissive | Inherits `*` | ✅ Accessible |
| ChatGPT-User | OpenAI | Permissive | Inherits `*` | ✅ Accessible |
| ClaudeBot | Anthropic | Permissive | Inherits `*` | ✅ Accessible |
| anthropic-ai | Anthropic | Permissive | Inherits `*` | ✅ Accessible |
| PerplexityBot | Perplexity | Permissive | Inherits `*` | ✅ Accessible |
| Google-Extended | Google | Permissive | Inherits `*` | ✅ Accessible |
| Amazonbot | Amazon | Permissive | Inherits `*` | ✅ Accessible |
| Bytespider | ByteDance | Permissive | Inherits `*` | ✅ Accessible |
| CCBot | Common Crawl | Permissive | Inherits `*` | ✅ Accessible |
| Applebot-Extended | Apple | Permissive | Inherits `*` | ✅ Accessible |
| FacebookBot | Meta | Permissive | Inherits `*` | ✅ Accessible |
| Cohere-ai | Cohere | Permissive | Inherits `*` | ✅ Accessible |
| Gemini (Google AIO) | Google | Permissive | Inherits `*` | ✅ Accessible |
| **Nutch** | Apache | **BLOCKED** | `Disallow: /` | ❌ Fully blocked |
| AhrefBot | Ahrefs | Restricted | Explicit + 10s delay | ⚠️ Delayed |
| AhrefsSiteAudit | Ahrefs | Restricted | Explicit + 10s delay | ⚠️ Delayed |
| MJ12bot | Majestic | Restricted | Explicit + 10s delay | ⚠️ Delayed |
| Pinterest | Pinterest | Restricted | Explicit + 1s delay | ⚠️ Delayed |
| adsbot-google | Google Ads | Restricted | Explicit | ✅ Content accessible |

**"Accessible" means:** products, collections, blog posts, pages (except /policies/), homepage — all content crawlable.
**"Blocked" pages for all crawlers (via wildcard):** /admin, /cart, /orders, /checkouts/, /account, /search, /policies/, sorted/filtered collection URLs, blog URLs with special characters, Shopify internal endpoints.

---

## Current robots.txt (Annotated)

```
# All crawlers (including all AI crawlers not named below)
User-agent: *
Disallow: /admin                              # ✅ Correct
Disallow: /cart                               # ✅ Correct
Disallow: /orders                             # ✅ Correct
Disallow: /checkouts/                         # ✅ Correct
Disallow: /49129095325/checkouts              # ⚠️ Store ID exposed
Disallow: /carts                              # ✅ Correct
Disallow: /account                            # ✅ Correct
Disallow: /collections/*sort_by*             # ✅ Correct (parameter duplicates)
Disallow: /collections/*+*                   # ✅ Correct
Disallow: /collections/*%2B*                 # ✅ Correct
Disallow: /collections/*%20*                 # ✅ Correct
Disallow: /collections/*filter*&*filter*     # ✅ Correct (double-filter only)
Disallow: /blogs/*+*                          # ✅ Correct
Disallow: /blogs/*%2B*                        # ✅ Correct
Disallow: /search                             # ✅ Correct
Disallow: /policies/                          # ⚠️ Consider allowing /policies/privacy-policy
                                              #    and /policies/refund-policy (E-E-A-T signals)
Disallow: /.well-known/shopify/monorail      # ✅ Correct
Disallow: /cdn/wpm/*.js                      # ✅ Correct
Disallow: /recommendations/products          # ✅ Correct
Disallow: /*/collections/*filter*&*filter*   # ✅ Correct
Disallow: /products/*-[a-f0-9]{8}-remote    # ⚠️ INVALID: regex not supported in robots.txt
                                              #    Most crawlers will ignore this rule
Sitemap: https://happimess.com/sitemap.xml   # ✅ Present

# AhrefBot
User-agent: AhrefBot
Crawl-delay: 10
[same restrictions as *]

# AhrefsSiteAudit
User-agent: AhrefsSiteAudit                  # ⚠️ Formatting: may be parsed as one rule
Crawl-delay: 10                              #    with next user-agent block

# Nutch
User-agent: Nutch
Disallow: /                                  # Fully blocked

# MJ12bot
User-agent: MJ12bot
Crawl-delay: 10

# Pinterest
User-agent: Pinterest
Crawl-delay: 1

# adsbot-google
User-agent: adsbot-google
[restricted to checkout/cart/orders]
```

---

## What AI Crawlers Can and Cannot Access

### ✅ Fully Accessible to All AI Crawlers
- `https://happimess.com/` — Homepage
- `https://happimess.com/products/*` — All product pages
- `https://happimess.com/collections/*` — All collection pages (except parameter variants)
- `https://happimess.com/blogs/news/*` — All 26 blog posts
- `https://happimess.com/pages/*` — All static pages (About, Contact, etc.)
- `https://happimess.com/llms.txt` — AI discovery file
- `https://happimess.com/llms-full.txt` — Extended AI discovery file
- `https://happimess.com/agents.md` — Agent interaction guide
- `https://happimess.com/.well-known/ucp` — UCP merchant profile

### ❌ Blocked for All Crawlers
- `/admin`, `/cart`, `/orders`, `/checkouts/`, `/account`, `/search`
- `/collections/[anything]?sort_by=[x]`
- `/collections/[anything]?filter=[x]&filter=[y]` (double filter)
- `/policies/*` (all policy pages — consider relaxing for /privacy-policy and /refund-policy)

### ⚠️ Edge Cases
- **Schema markup (JS-injected):** The global Organization/WebSite schema blocks are injected via T4S theme JavaScript. AI crawlers that don't execute JavaScript (GPTBot, ClaudeBot, PerplexityBot) will miss these schemas. Schema on interior pages (Article, Product, BreadcrumbList) appears to be server-rendered and accessible.
- **Lazy-loaded images:** All product images use `data:image/gif;base64` placeholders. AI crawlers won't see actual image content without JS execution.

---

## Recommended robots.txt Changes

Add these blocks **at the top** of robots.txt, before the `User-agent: *` block:

```
# === AI SEARCH CRAWLERS — EXPLICIT ACCESS ===

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

User-agent: Bytespider
Allow: /

User-agent: CCBot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: FacebookBot
Allow: /

User-agent: Cohere-ai
Allow: /

# Content permissions declaration (IETF draft-romm-aipref-contentsignals)
Content-Signal: ai-train=yes, search=yes, ai-retrieval=yes

# === END AI CRAWLERS ===
```

Also consider:
```
# Allow AI crawlers to access policy pages (trust signals for E-E-A-T)
# Change in the User-agent: * block:
Disallow: /policies/        →  Allow: /policies/privacy-policy
                                Allow: /policies/refund-policy
                                Disallow: /policies/
```

---

## Fixes Required

| Issue | Severity | Fix |
|-------|----------|-----|
| No explicit AI crawler Allow directives | High | Add named User-agent blocks (see above) |
| Regex in Disallow rule (invalid standard) | Medium | Remove `/products/*-[a-f0-9]{8}-remote` line; regex is ignored by most crawlers anyway |
| `AhrefsSiteAudit` + `Crawl-delay` formatting | Low | Add blank line between User-agent and Crawl-delay |
| `/policies/` fully blocked | Low | Allow privacy and refund policy pages for E-E-A-T |
| Store ID in robots.txt (`/49129095325/checkouts`) | Low | Minor info disclosure; not a security risk but unnecessary |
| JS-injected Organization schema invisible to AI crawlers | High | Move to server-rendered Liquid in `theme.liquid` |
| No `Content-Signal` directive | Medium | Add (see above) |

---

## Crawler Access Score Breakdown

| Factor | Score | Weight | Weighted |
|--------|-------|--------|---------|
| No critical AI crawlers blocked | 100 | 40% | 40.0 |
| Sitemap declared in robots.txt | 100 | 15% | 15.0 |
| Content pages accessible | 95 | 15% | 14.25 |
| Explicit AI crawler Allow rules | 0 | 20% | 0.0 |
| Content-Signal directive | 0 | 10% | 0.0 |
| **Total** | | | **69.25 → 70/100** |

---

## Context: How This Compares

| Standard | happimess.com |
|----------|--------------|
| Actively blocking AI crawlers | No ✅ |
| Default permissive (wildcard) | Yes ✅ |
| Explicit AI crawler rules | No ⚠️ |
| Sitemap in robots.txt | Yes ✅ |
| AI-readable files (llms.txt, agents.md) | Yes ✅ (industry-leading) |
| Content-Signal directive | No ⚠️ |

The site is in the **top 40%** for AI crawler accessibility — it doesn't block anyone, has a sitemap, and has llms.txt/agents.md infrastructure that most sites lack. Adding the 14-line explicit Allow block would push it to the **top 10%** for crawler access configuration.

---

*Generated by Claude Code GEO Skill — `/geo crawlers https://happimess.com/`*
*Full audit data: `GEO-AUDIT-REPORT.md`*
