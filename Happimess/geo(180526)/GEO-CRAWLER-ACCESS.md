# GEO Crawler Access Report — Happimess
**URL:** https://happimess.com/  
**Analysis Date:** 2026-05-18  
**robots.txt:** https://happimess.com/robots.txt  
**Sitemap:** https://happimess.com/sitemap.xml  

---

## Crawler Access Score: 90 / 100 — Good

All primary AI crawlers are explicitly granted full site access. The robots.txt has been proactively configured for the AI search era with named grants, a Content-Signal declaration, and a custom agentic-discovery sitemap. Minor deductions for three secondary crawlers not explicitly named and a `policies/` path ambiguity for non-named bots.

---

## AI Crawler Access Map

### Primary AI Crawlers — All Explicitly Allowed

| Crawler | User-Agent | Rule | Operator | Use Case |
|---------|-----------|------|----------|----------|
| GPTBot | `GPTBot` | `Allow: /` | OpenAI | ChatGPT training + web search |
| OAI-SearchBot | `OAI-SearchBot` | `Allow: /` | OpenAI | ChatGPT real-time search retrieval |
| ChatGPT-User | `ChatGPT-User` | `Allow: /` | OpenAI | ChatGPT browse-on-behalf-of-user |
| ClaudeBot | `ClaudeBot` | `Allow: /` | Anthropic | Claude training + knowledge |
| anthropic-ai | `anthropic-ai` | `Allow: /` | Anthropic | Anthropic secondary agent |
| PerplexityBot | `PerplexityBot` | `Allow: /` | Perplexity | Perplexity AI search indexing |
| Google-Extended | `Google-Extended` | `Allow: /` | Google | Gemini + AI Overviews training |
| Amazonbot | `Amazonbot` | `Allow: /` | Amazon | Alexa + Amazon AI products |
| CCBot | `CCBot` | `Allow: /` | Common Crawl | Open training datasets |
| Applebot-Extended | `Applebot-Extended` | `Allow: /` | Apple | Apple Intelligence training |

**Coverage:** 10/10 tier-1 AI crawlers explicitly granted — full site access with no path restrictions.

---

### Secondary AI Crawlers — Not Explicitly Named (Inherit `User-agent: *`)

| Crawler | User-Agent | Effective Rule | Operator | Risk |
|---------|-----------|----------------|----------|------|
| FacebookBot | `facebookbot` | `User-agent: *` rules | Meta | Llama training; inherits general rules |
| Bytespider | `Bytespider` | `User-agent: *` rules | ByteDance/TikTok | Doubao, Coze AI products |
| Cohere-ai | `cohere-ai` | `User-agent: *` rules | Cohere | Enterprise LLM training |
| DiffBot | `DiffbotBot` | `User-agent: *` rules | Diffbot | AI knowledge graph |
| YouBot | `YouBot` | `User-agent: *` rules | You.com | You.com AI search |

**Effective access for `User-agent: *`:** Broad access — no `Disallow: /` at root. These crawlers can access all content that isn't in the standard blocked paths (admin, cart, checkout, accounts, etc.). The `/policies/` ambiguity (see below) applies to these crawlers.

**Risk level:** Low. No root block, and all standard commerce paths (admin, cart) are appropriately blocked for all bots. The only potential issue is the `/policies/` path behavior.

---

### Blocked/Restricted Crawlers

| Crawler | User-Agent | Rule | Reason |
|---------|-----------|------|--------|
| Nutch | `Nutch` | `Disallow: /` | Aggressive scraper; intentionally blocked |
| AhrefsBot | `AhrefsBot` | Crawl-delay: 10 + same disallows as `*` | Rate-limited SEO tool |
| AhrefsSiteAudit | `AhrefsSiteAudit` | Crawl-delay: 10 + same disallows as `*` | Rate-limited SEO tool |
| MJ12bot | `MJ12bot` | Crawl-delay: 10 | Aggressive crawler rate-limited |
| Pinterest | `Pinterest` | Crawl-delay: 1 | Rate-limited social crawler |
| adsbot-google | `adsbot-google` | Commerce paths blocked | Google Ads bot — correct |

**Note:** Nutch is correctly blocked (it's an aggressive scraper with no AI search use case). The AhrefsBot/Majestic rate-limiting is appropriate and doesn't affect AI crawler access.

---

## robots.txt Full Analysis

### Structure

```
# AI SEARCH CRAWLERS — EXPLICIT ACCESS GRANT
[10 named AI crawlers with Allow: /]

# Content permissions declaration
Content-Signal: ai-train=yes, search=yes, ai-retrieval=yes

# SHOPIFY DEFAULT RULES
User-agent: *
[Standard commerce path disallows]

# Specific Allow overrides for trust pages
User-agent: *
Allow: /policies/privacy-policy
Allow: /policies/refund-policy
Allow: /policies/terms-of-service

# Rate-limited crawlers
[AhrefsBot, MJ12bot, Pinterest]

Sitemap: https://happimess.com/sitemap.xml
```

**Organization:** Excellent. Named AI crawlers placed first and clearly commented. Standard Shopify defaults follow. Trust page overrides at the end.

---

### Standard Shopify Disallows (Applied to `User-agent: *`)

These correctly block non-content paths from all crawlers:

```
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
Disallow: /collections/*+*  (and %2B, %2b variants)
Disallow: */collections/*filter*&*filter*
Disallow: /blogs/*+*  (and %2B, %2b variants)
Disallow: /*?*oseid=*
Disallow: /*preview_theme_id*
Disallow: /*preview_script_id*
Disallow: /policies/          ← see note below
Disallow: /*/policies/
Disallow: /search
Disallow: /apple-app-site-association
Disallow: /.well-known/shopify/monorail
Disallow: /cdn/wpm/*.js
Disallow: /recommendations/products
Disallow: /*/recommendations/products
Disallow: /services/login_with_shop
```

**Assessment of each:**

| Path | Blocked | GEO Assessment |
|------|---------|----------------|
| `/admin`, `/cart`, `/orders`, `/checkout`, `/account` | ✅ Correct | Commerce internals — should be blocked |
| `/collections/*sort_by*`, filter params | ✅ Correct | Prevents duplicate content from faceted navigation |
| `/blogs/*+*`, `%2B` variants | ✅ Correct | Prevents URL injection variants |
| `/search` | ✅ Correct | Blocks low-value search result pages |
| `/*preview_theme_id*` | ✅ Correct | Blocks Shopify preview URLs |
| `/recommendations/products` | ✅ Correct | Dynamic endpoint, no standalone value |
| `/cdn/wpm/*.js` | ✅ Correct | JavaScript bundles — not content |
| `/apple-app-site-association` | ✅ Correct | App association file — not indexable content |
| `/policies/` | ⚠️ See note | Blocked in general rules; 3 key pages have Allow overrides |

---

### The /policies/ Issue — Detailed Analysis

**Current configuration:**
```
# In User-agent: * section:
Disallow: /policies/

# At end of file (separate User-agent: * block):
Allow: /policies/privacy-policy
Allow: /policies/refund-policy
Allow: /policies/terms-of-service
```

**For the 10 named AI crawlers** (GPTBot, ClaudeBot, etc.): These crawlers received explicit `Allow: /` in their own user-agent blocks. The "most specific rule wins" principle means `Allow: /` overrides `Disallow: /policies/` for named bots. **These crawlers have full access to all policy pages.**

**For unnamed crawlers** (FacebookBot, Bytespider, Cohere-ai, etc.): These inherit `User-agent: *` rules. The three specific `Allow` overrides at the end of the file should protect privacy-policy, refund-policy, and terms-of-service. However, behavior depends on the crawler's parser: Google's spec says the most specific path wins; some crawlers process rules top-to-bottom (where the later `Allow` overrides the earlier `Disallow`). The behavior is technically ambiguous for strict top-to-bottom parsers.

**Remaining blocked policy pages for unnamed crawlers:**
- `/policies/shipping-policy` — blocked
- `/policies/contact-information` — blocked
- Any other policy subdirectories

**Recommendation:** Move all three policy `Allow` overrides to the top of the `User-agent: *` block (before the `Disallow: /policies/` line) to ensure deterministic behavior across all parsers. Alternatively, change `Disallow: /policies/` to `Disallow: /policies/privacy-policy-draft` (or whatever you actually need to block) and allow the rest.

---

### Content-Signal Declaration

```
Content-Signal: ai-train=yes, search=yes, ai-retrieval=yes
```

**What this does:** This is an emerging IETF draft standard (`draft-romm-aipref-contentsignals`) for declaring content permissions in robots.txt. It explicitly signals:

| Signal | Value | Meaning |
|--------|-------|---------|
| `ai-train` | yes | Site consents to use of content for AI model training |
| `search` | yes | Site consents to AI-powered search indexing and answer generation |
| `ai-retrieval` | yes | Site consents to real-time retrieval and citation by AI systems |
| `ai-personalization` | (not declared) | Not applicable for e-commerce |

**Assessment:** This is a forward-thinking, proactive declaration. Very few sites have added this signal. It sends a clear consent signal to AI operators beyond the crawler-specific Allow/Disallow rules. The omission of `ai-personalization` is appropriate — not relevant for a commerce site.

**Recommendation:** No changes needed. This is best-practice.

---

### Agentic Discovery Sitemap

The sitemap index includes a custom sub-sitemap:
```
https://happimess.com/sitemap_agentic_discovery.xml
```

This sitemap references three AI discovery assets:
- `https://happimess.com/llms.txt`
- `https://happimess.com/llms-full.txt`
- `https://happimess.com/agents.md`

**Assessment:** Excellent forward-thinking addition. By including AI discovery files in the sitemap, crawlers that process sitemaps before `robots.txt` will discover these resources. This is the correct way to surface AI-oriented files to crawlers. Note: the content quality of `llms.txt` is a separate issue (see GEO-CITABILITY-SCORE.md for analysis of the non-compliant format) — but the discovery mechanism is correct.

---

## Path-Level Access Summary

| Path | Named AI Crawlers | Unnamed Crawlers | Notes |
|------|-------------------|-----------------|-------|
| `/` (homepage) | ✅ Allowed | ✅ Allowed | Full access |
| `/products/*` | ✅ Allowed | ✅ Allowed | All product pages |
| `/collections/*` | ✅ Allowed | ✅ Allowed | Base collection URLs |
| `/collections/*sort_by*` | ✅ Allowed¹ | ❌ Blocked | Faceted navigation — correctly blocked |
| `/blogs/news/*` | ✅ Allowed | ✅ Allowed | All blog articles |
| `/blogs/news` | ✅ Allowed | ✅ Allowed | Blog index |
| `/pages/*` | ✅ Allowed | ✅ Allowed | About Us, FAQs, etc. |
| `/policies/privacy-policy` | ✅ Allowed | ✅ Allowed | Specific Allow override |
| `/policies/refund-policy` | ✅ Allowed | ✅ Allowed | Specific Allow override |
| `/policies/terms-of-service` | ✅ Allowed | ✅ Allowed | Specific Allow override |
| `/policies/` (other) | ✅ Allowed¹ | ⚠️ Ambiguous | Named bots have `Allow: /`; unnamed inherit `Disallow: /policies/` |
| `/es/*` | ✅ Allowed | ✅ Allowed | Spanish subdirectory — full access |
| `/admin` | ❌ Blocked | ❌ Blocked | Correct |
| `/cart`, `/checkout` | ❌ Blocked | ❌ Blocked | Correct |
| `/account`, `/orders` | ❌ Blocked | ❌ Blocked | Correct |
| `/search` | ❌ Blocked | ❌ Blocked | Correct |
| `/llms.txt` | ✅ Allowed | ✅ Allowed | In sitemap_agentic_discovery.xml |
| `/agents.md` | ✅ Allowed | ✅ Allowed | In sitemap_agentic_discovery.xml |

¹ Named AI crawlers received blanket `Allow: /` which overrides all path-level Disallow rules.

---

## Crawlable Content Inventory

Based on sitemap analysis, the following content is accessible to all AI crawlers:

| Content Type | Count | Path |
|-------------|-------|------|
| English products | 332 | `/products/*` |
| English collections | 103 | `/collections/*` |
| English pages | 15 | `/pages/*` |
| English blog posts | 26 | `/blogs/news/*` |
| Spanish products | 181 | `/es/products/*` |
| Spanish collections | 125 | `/es/collections/*` |
| Spanish pages | 15 | `/es/pages/*` |
| AI discovery files | 3 | `/llms.txt`, `/llms-full.txt`, `/agents.md` |
| **Total** | **~800** | |

**Important:** All content is Shopify SSR (server-side rendered). AI crawlers that do not execute JavaScript (GPTBot, ClaudeBot, PerplexityBot) receive full text content in the initial HTML response. No JavaScript rendering required to access any substantive content.

---

## Missing Crawler Declarations

The following crawlers are not explicitly named in robots.txt and inherit `User-agent: *` rules:

| Crawler | Operator | Priority | Recommended Action |
|---------|----------|----------|-------------------|
| `FacebookBot` | Meta (Llama) | Medium | Add `User-agent: FacebookBot` / `Allow: /` |
| `Bytespider` | ByteDance | Medium | Add `User-agent: Bytespider` / `Allow: /` |
| `cohere-ai` | Cohere | Low | Add `User-agent: cohere-ai` / `Allow: /` |
| `DiffbotBot` | Diffbot | Low | Add `User-agent: DiffbotBot` / `Allow: /` |
| `YouBot` | You.com | Low | Add `User-agent: YouBot` / `Allow: /` |

These crawlers currently have effective access via `User-agent: *` (no root Disallow), but explicit grants would:
1. Eliminate ambiguity around the `/policies/` path behavior
2. Future-proof against accidental lockout if Shopify ever changes default rules
3. Demonstrate proactive AI-first posture to all platforms

---

## Recommended robots.txt Additions

Add the following block immediately after the existing named AI crawler section:

```
# SECONDARY AI CRAWLERS
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
```

And move the `/policies/` Allow overrides inside the `User-agent: *` block, *before* the `Disallow: /policies/` line:

```
User-agent: *
# Trust page exceptions — must come before the /policies/ Disallow
Allow: /policies/privacy-policy
Allow: /policies/refund-policy
Allow: /policies/terms-of-service
# Standard Shopify disallows
Disallow: /admin
Disallow: /cart
...
Disallow: /policies/
...
```

---

## Score Calculation

| Factor | Score | Weight | Notes |
|--------|-------|--------|-------|
| Tier-1 AI crawlers explicitly allowed | 100 | 50% | All 10 named with `Allow: /` |
| Content-Signal declaration present | 100 | 15% | ai-train, search, ai-retrieval all yes |
| SSR content delivery | 100 | 15% | Shopify SSR — no JS rendering required |
| Secondary crawlers coverage | 60 | 10% | 5 unnamed crawlers inherit `User-agent: *` |
| /policies/ path clarity | 70 | 10% | 3 key pages rescued; other policy pages ambiguous for unnamed bots |
| **Weighted Score** | **90/100** | | |

---

## Summary Table

| Crawler | Access | Explicitly Named |
|---------|--------|-----------------|
| GPTBot | ✅ Full | ✅ Yes |
| OAI-SearchBot | ✅ Full | ✅ Yes |
| ChatGPT-User | ✅ Full | ✅ Yes |
| ClaudeBot | ✅ Full | ✅ Yes |
| anthropic-ai | ✅ Full | ✅ Yes |
| PerplexityBot | ✅ Full | ✅ Yes |
| Google-Extended | ✅ Full | ✅ Yes |
| Amazonbot | ✅ Full | ✅ Yes |
| CCBot | ✅ Full | ✅ Yes |
| Applebot-Extended | ✅ Full | ✅ Yes |
| FacebookBot | ✅ Effective | ❌ No |
| Bytespider | ✅ Effective | ❌ No |
| Cohere-ai | ✅ Effective | ❌ No |
| DiffbotBot | ✅ Effective | ❌ No |
| YouBot | ✅ Effective | ❌ No |
| Nutch | ❌ Blocked | ✅ Yes (intentional) |

---

## Priority Actions

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 1 | Move `/policies/` Allow overrides to *before* the `Disallow: /policies/` line within `User-agent: *` | 5 min | Eliminates parser ambiguity for unnamed bots |
| 2 | Add 5 secondary AI crawlers (FacebookBot, Bytespider, cohere-ai, DiffbotBot, YouBot) with explicit `Allow: /` | 10 min | Closes coverage gap; future-proofs against Shopify default changes |
| 3 | Rewrite `/llms.txt` to spec-compliant format | 1 hour | The discovery mechanism is correct; the file content needs fixing (see GEO-CITABILITY-SCORE.md) |

**Overall assessment:** Happimess robots.txt is in the top tier for AI crawler access. The explicit grants, Content-Signal declaration, and agentic sitemap represent best-practice GEO configuration. The two remaining items (policy path ordering, secondary crawler grants) are minor polish on an already excellent setup.

---

*Crawler access analysis conducted 2026-05-18. Output file: GEO-CRAWLER-ACCESS.md*
