# GEO Platform Optimization Report — Happimess
**Site:** https://happimess.com  
**Date:** 2026-05-26  
**Auditor:** Claude Code / geo-platform-optimizer  
**Data sources:** Full audit + citability + crawlers + brands + technical analyses (same session)

---

## Platform Optimization Score: 52/100 (Fair)

| Platform | Score | Change vs May 20 | Bottleneck |
|----------|-------|-----------------|------------|
| Google AI Overviews | 51/100 | +6 | Citations unlinked; no author credential depth |
| ChatGPT Web Search | 56/100 | +8 | /.well-known/ucp staging domain; no Wikidata entity |
| Perplexity AI | 44/100 | +4 | Zero Reddit; llms.txt non-compliant; citations unlinked |
| Google Gemini | 49/100 | +2 | No YouTube; no Google Business Profile; no Knowledge Graph |
| Bing Copilot | 58/100 | +3 | LinkedIn dormant; no IndexNow |
| **Composite** | **52/100** | **+3** | **Brand entity + community gaps** |

---

## Platform 1: Google AI Overviews

**Score: 51/100 — Fair**

Google AI Overviews (formerly Search Generative Experience) appears at the top of Google Search for informational and product-research queries, reaching 1.5B users/month. For home goods, it generates AI-written overviews citing sources for queries like "best trash cans for kitchen," "how to reduce kitchen odors," and "what size trash can do I need."

### Signal Audit

| Signal | Status | Details |
|--------|--------|---------|
| FAQPage JSON-LD | ✅ Present | /pages/faqs: 8 Q&As with FAQPage schema; also on product pages |
| BlogPosting schema | ✅ Present | All 27 blog articles; datePublished, dateModified, author, speakable |
| Answer-target paragraph structure | ✅ Good | Blog headings are question-format (H2); opening paragraphs provide direct answers |
| Comparison tables | ✅ Present | "Regular vs. Happimess Scented Trash Liners" in scented bags article |
| External citations | ⚠️ Present but unlinked | EPA, USDA, CDC referenced as prose — no hyperlinks to source documents |
| Author E-E-A-T | ⚠️ Weak | Jonathan Yaraghi and Sandip Hadiya named; no credential depth, no linked LinkedIn |
| Featured snippet optimization | ⚠️ Partial | Some FAQ-format content is AIO-extractable; needs consistent answer-first structure |
| Original data / proprietary research | ❌ Missing | Testing methodology exists but not cross-referenced in articles |
| HowTo schema | ❌ Missing | No step-by-step guides with HowTo JSON-LD |
| FAQPage rich results | ⛔ Restricted | Google restricted FAQPage rich results to government/health authority sites (Aug 2023) — schema has semantic value for AIO but generates no rich snippet |
| Google Business Profile | ❌ Not found | No confirmed GBP listing — no Knowledge Panel in Google Search |

### Why Google AI Overviews Shows Happimess Content

**Likely cited today for:**
- "lemon vs lavender scent trash bag kitchen bathroom" — scented bags comparison table
- "dual trash can capacity 40 liters kitchen" — capacity sizing guide
- "how to keep trash can from smelling" — maintenance tips list

**Not cited today (fixable):**
- "best trash cans for family of 4" — no household-size data in FAQ
- "how to choose a sensor vs pedal trash can" — no comparison content
- "what is the best kitchen trash can under $100" — no price comparison content

### Google AI Overviews Optimization Actions

**Action 1 (HIGH) — Hyperlink all government citations**
The three government references (EPA, USDA, CDC) must link to specific source pages. Google's E-E-A-T evaluation weighs externally verified claims significantly higher than unsourced assertions. For AIO specifically, cited content is more likely to appear in AI-generated overviews when the citations are traceable.

**Action 2 (HIGH) — Standardize answer-first paragraph structure across all blog posts**
Every H2 question heading should be followed by a 40–60 word direct answer as the first sentence of the paragraph. The scented bags article does this partially — systematize it across all 27 articles. Format:
```
## [Question]
[Direct 40-60 word answer.] [Elaboration follows...]
```

**Action 3 (MEDIUM) — Add HowTo schema to maintenance and setup guides**
"How to keep a trash can from smelling" and "How to install custom-fit trash bag liners" map perfectly to HowTo schema. This type of structured procedural content is actively featured in Google AI Overviews for how-to queries.

**Action 4 (MEDIUM) — Create Google Business Profile**
A verified GBP for the NYC office creates a Knowledge Panel in Google Search that AI Overviews uses as an entity anchor. Even for an e-commerce brand, a GBP establishes the "Happimess" entity in Google's knowledge graph with specific attributes: category (Home Goods Store), location (NYC), website, phone, hours.

**Action 5 (MEDIUM) — Add author `jobTitle` and LinkedIn `sameAs` to BlogPosting schema**
Google's E-E-A-T evaluation for AIO considers whether article authors have verifiable credentials. Adding `"jobTitle": "Home Organization Expert"` and `"sameAs": "[LinkedIn URL]"` to the BlogPosting author object gives Google a signal it can verify.

---

## Platform 2: ChatGPT Web Search

**Score: 56/100 — Fair**

ChatGPT's web browsing (900M+ weekly users) cites sources directly in responses to shopping and informational queries. When a user asks "recommend a good trash can for my NYC apartment," ChatGPT searches the web, finds relevant content, and cites it with source links. For home goods, it competes with Wirecutter, The Spruce, and Amazon product pages for citation.

### Signal Audit

| Signal | Status | Details |
|--------|--------|---------|
| GPTBot access | ✅ Full | `User-agent: GPTBot Allow: /` — explicit |
| OAI-SearchBot access | ✅ Full | `User-agent: OAI-SearchBot Allow: /` — explicit |
| ChatGPT-User access | ✅ Full | `User-agent: ChatGPT-User Allow: /` — explicit |
| agents.md (UCP) | ✅ Deployed | Full UCP v2026-04-08 with Shop skill configuration |
| /.well-known/ucp | ❌ Broken | MCP endpoint references `happimess-dev.myshopify.com` — ChatGPT Shopping fails |
| Wikidata entity | ❌ Absent | No Wikidata Q-entity — ChatGPT cannot perform reliable entity recognition |
| Wikipedia entity | ❌ Absent | No Wikipedia article |
| Meta descriptions | ✅ Present | Key pages now have meta descriptions (fixed since May 20) |
| Content-Signal | ✅ Declared | `ai-train=yes, search=yes, ai-retrieval=yes` |
| ai-instructions link | ✅ Present | `<link rel="ai-instructions" href="/agents.md">` on all pages |
| Author attribution | ⚠️ Partial | Named authors present; no sameAs LinkedIn links |
| Product schema brand.name | ❌ Error on 7 products | `"Happimess Dev"` on elmo, beni, chuck, ashley, oscar, molly, nathan |

### ChatGPT Agentic Commerce Status

ChatGPT Shopping (powered by UCP) is **non-functional** for Happimess due to the staging domain bug:

```
/.well-known/ucp → "endpoint": "https://happimess-dev.myshopify.com/api/ucp/mcp"
```

When a ChatGPT Shopping agent discovers UCP capabilities at `/well-known/ucp` and attempts to connect to the MCP endpoint, it reaches the development store. This results in:
- Cart creation failures
- Price/availability data from dev store (potentially incorrect)
- Transaction trust failure — ChatGPT Shopping may flag the endpoint as unreliable

The agents.md file is correctly deployed and the commerce infrastructure is complete — this is a single configuration bug preventing full agentic commerce functionality.

**Fix:** In Shopify Admin, navigate to the UCP app configuration and change the MCP endpoint URL from `happimess-dev.myshopify.com` to `happimess.com`. This is a one-field edit.

### ChatGPT Optimization Actions

**Action 1 (CRITICAL) — Fix /.well-known/ucp staging domain**
Replace `happimess-dev.myshopify.com` with `happimess.com` in the UCP endpoint configuration. This restores ChatGPT Shopping functionality — the highest-leverage agentic commerce action available. Effort: 15 minutes.

**Action 2 (HIGH) — Create Wikidata entity for Happimess**
Without a Wikidata Q-entity, ChatGPT cannot reliably resolve "Happimess" as a specific entity. Given the brand-name collision problem (6+ unrelated "Happimess" entities on social media), this disambiguation is critical. Fields needed: instance of (business), country (US), headquarters (NYC), founded (2020), official website (happimess.com). Effort: 1–2 hours.

**Action 3 (MEDIUM) — Fix "Happimess Dev" brand.name on 7 products**
Product schema errors on the 7 affected products affect ChatGPT's shopping recommendations. When ChatGPT Shopping reads a Product schema with `"brand": {"name": "Happimess Dev"}`, it may display or cite the brand as "Happimess Dev" rather than "Happimess" — a trust-eroding artifact in AI-generated recommendations.

**Action 4 (MEDIUM) — Add author sameAs LinkedIn to BlogPosting schema**
ChatGPT's content citation preference weights verifiable author identity. Adding `sameAs: ["https://www.linkedin.com/in/[jonathan-linkedin-slug]"]` to the BlogPosting author object gives ChatGPT a signal it can cross-reference.

---

## Platform 3: Perplexity AI

**Score: 44/100 — Poor (Weakest Platform)**

Perplexity (500M+ monthly queries) is the most stringent citability platform — it prioritizes recent, sourced, community-validated content. It relies heavily on Reddit threads, academic papers, and authoritative editorial sources. For home goods queries, it cites The Spruce, Apartment Therapy, Wirecutter, and Reddit discussions. Happimess lacks a footprint in all of these.

### Signal Audit

| Signal | Status | Details |
|--------|--------|---------|
| PerplexityBot access | ✅ Full | `User-agent: PerplexityBot Allow: /` — explicit |
| llms.txt | ❌ Non-compliant | 301 redirect to agents.md — Perplexity's content discovery gets UCP protocol |
| Reddit presence | ❌ Zero | No indexed Reddit threads mentioning Happimess |
| Quora presence | ❌ Not confirmed | No Quora activity found |
| Trustpilot | ❌ Not found | No Trustpilot profile |
| External linked citations | ❌ Missing | EPA/USDA/CDC referenced as prose, not hyperlinked |
| Publication dates | ✅ Present | Blog articles show pub date + last-modified in HTML |
| Content freshness | ✅ Good | Recent articles (May 2026) with update timestamps |
| Content depth | ✅ Good | 1,200–3,000 words per article |
| Original data / research | ❌ Missing | No proprietary statistics or primary research data |
| Community discussion | ❌ Zero | No Reddit, Quora, or forum discussions found |

### Why Perplexity Score Is Lowest

Perplexity's citation algorithm uniquely weights:

1. **Community validation** (Reddit, Quora, forums) — 0 presence for Happimess
2. **Source verification chain** — citations that link to real documents, which AI can follow
3. **Freshness with attribution** — content with visible dates AND author names
4. **External authority anchors** — content that cites government or academic sources with links

Happimess has made progress on items 3 and 4 (dates visible, gov citations present) but the citations are prose-only without links (Perplexity cannot verify them) and item 1 remains completely unaddressed.

### Perplexity Optimization Actions

**Action 1 (HIGH) — Deploy spec-compliant llms.txt**
The generated `llms.txt` file (from today's `/geo llmstxt` session) is ready to deploy. Perplexity uses llms.txt for content discovery prioritization — serving the correct file at `/llms.txt` tells Perplexity which pages to prioritize for citation (blog articles, FAQ, About) vs. which to deprioritize (collection pages, checkout). Effort: 45 minutes to deploy.

**Action 2 (HIGH) — Convert prose citations to hyperlinked references**
Every instance of "According to the U.S. Environmental Protection Agency..." must become:
```html
According to the <a href="https://www.epa.gov/recycle/recycling-basics">U.S. Environmental Protection Agency</a>...
```
Perplexity follows citation chains to verify claims. Unlinked citations score as unverified assertions. Note: verify the actual EPA source document before linking — the current "quote" text may not match any EPA publication exactly. Effort: 2–3 hours to find, verify, and link all citations.

**Action 3 (HIGH) — Add original data point to flagship articles**
The single highest-value content upgrade for Perplexity is adding one piece of proprietary primary data to each article. The About page testing methodology (30-day, 500+ cycles) is an unused resource — reference it explicitly: "In our 30-day testing of 12 trash can models, 4 of 12 pedal mechanisms showed wear before day 20 — here's what we found." A specific data point with specific numbers makes content citable as a primary source rather than a secondary summary.

**Action 4 (MEDIUM) — Build authentic Reddit community presence**
This cannot be rushed, but a 6-month plan:
- Month 1–2: Make genuine helpful contributions in r/organization and r/ZeroWaste without self-promotion
- Month 3–4: Answer specific product questions where Happimess products are genuinely relevant
- Month 5–6: If a natural opportunity arises, a genuine "I work at Happimess and we made this guide" disclosure in relevant threads
Effort: 1–2 hours/week, 6+ month timeline. Impact: +15–20 pts Brand Authority, +8–10 pts Perplexity score.

**Action 5 (MEDIUM) — Add original data section to the dual trash can guide**
This article is the strongest candidate for Perplexity citation because it already cites an EPA source. Adding a data section — "We tested 8 dual-compartment models over 30 days; here's how they scored on pedal durability, odor containment, and ease of cleaning" — would make it Perplexity-citable as a primary testing source rather than an opinion piece.

---

## Platform 4: Google Gemini

**Score: 49/100 — Poor**

Google Gemini integrates with Google Search and is used for multimodal queries, shopping assistance, and conversational answers within Google's ecosystem. Gemini uniquely benefits from Google's own data: YouTube, Google Business Profile, Google Shopping, and the Knowledge Graph. Happimess is absent from all four.

### Signal Audit

| Signal | Status | Details |
|--------|--------|---------|
| Google-Extended access | ✅ Full | `User-agent: Google-Extended Allow: /` — explicit |
| Shopify SSR | ✅ Confirmed | Full HTML in initial response — Googlebot sees all content |
| Knowledge Graph entity | ❌ Absent | No Wikipedia/Wikidata → no Knowledge Panel → no Gemini entity |
| Google Business Profile | ❌ Not found | No GBP listing confirmed — no map presence |
| YouTube channel content | ❌ Minimal | Official channel exists; no confirmed published videos |
| Google Shopping presence | ✅ Indirect | Products appear in Google Shopping via Home Depot, Amazon, Target feeds |
| Google Pay merchant | ✅ Present | Google Pay merchant ID in UCP config: `16708973830884969730` |
| BlogPosting schema | ✅ Present | datePublished, dateModified, author with Person schema |
| Internal topical clustering | ✅ Moderate | 27 blog articles on related home organization topics |
| Schema sameAs — Google entities | ❌ Missing | No GBP URL, no YouTube channel URL, no Google Scholar in sameAs |

### Google Gemini Optimization Actions

**Action 1 (HIGH) — Create Google Business Profile**
A verified GBP is Gemini's primary anchor for brand entity recognition. Even for a pure e-commerce brand (no walk-in store), a GBP creates:
- A verified business entity in Google's Knowledge Graph
- A Google Knowledge Panel in search results
- A signal that Gemini uses for conversational brand queries ("tell me about Happimess")
- A sameAs anchor that links the happimess.com domain to a Google-verified entity

**Setup:** Google Business Profile at business.google.com. Use the NYC office address (185 Madison Avenue, NY 10016). Category: "Home Goods Store" or "Storage Organization". This is free and takes approximately 30 minutes + verification (postcard or phone, 1–5 days).

**Action 2 (HIGH) — Add YouTube channel URL to Organization sameAs**
The YouTube channel (@happimess_official) is confirmed. Adding `"https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g"` to the Organization sameAs array (it should already be there based on the audit) connects the channel to the brand entity. Additionally, embedding YouTube videos (once created) on product and blog pages creates direct Google content signals.

**Action 3 (HIGH) — Create Wikidata entity → Google Knowledge Graph**
Wikidata is directly ingested by Google Knowledge Graph. A Wikidata Q-entity for Happimess creates:
- A Knowledge Graph entry visible to Gemini
- A disambiguation node that separates "Happimess (home organization)" from "Happimess Cosmetics"
- A sameAs anchor for the Organization schema

**Action 4 (MEDIUM) — Publish 3+ YouTube videos and embed on blog posts**
Gemini is Google's multimodal AI — it indexes and cites YouTube content more aggressively than any other AI platform. A "How to choose the right trash can" 90-second video embedded on the trash can guide blog post creates:
- Direct Google video indexing signal
- An additional entity anchor in Google's knowledge base
- Potential for video results to appear in Google AI Overviews alongside article citations

**Action 5 (MEDIUM) — Add GBP URL to Organization sameAs once created**
After creating the Google Business Profile, the GBP URL (`https://www.google.com/maps/place/[URL]`) should be added to the Organization sameAs array in theme.liquid. This explicitly links the website entity to the Google-verified business entity.

---

## Platform 5: Bing Copilot

**Score: 58/100 — Fair (Strongest Platform)**

Bing Copilot (formerly Bing Chat) uses Microsoft's Prometheus AI model, which integrates Bing Search with GPT-4. It generates conversational answers to shopping and informational queries, heavily weighting Bing-indexed content, verified Bing Webmaster Tools sites, and LinkedIn (a Microsoft property) for commercial entity verification.

### Signal Audit

| Signal | Status | Details |
|--------|--------|---------|
| Bingbot access | ✅ Via `User-agent: *` | Allowed through general wildcard |
| Bing Webmaster Tools | ✅ Verified | msvalidate.01 meta tag confirmed present |
| IndexNow | ❌ Not implemented | No IndexNow key file or meta tag found |
| LinkedIn company page | ⚠️ Dormant | Page exists at /company/happimesshome; 26 followers; 7+ month inactivity |
| Sitemap | ✅ Current | 9 child sitemaps; lastmod timestamps current (May 2026) |
| Meta descriptions | ✅ Present | FAQs, About Us now have meta descriptions (fixed since May 20) |
| Shopify SSR | ✅ Confirmed | Full HTML in initial response |
| Structured data | ✅ Good | Organization, BlogPosting, FAQPage, BreadcrumbList confirmed |
| Content quality | ✅ Good | Professional tone; direct answers; comparison tables |
| Microsoft Clarity | Not checked | Bing's user behavior analytics — not confirmed as installed |

### Why Bing Copilot Scores Highest

Bing Copilot's edge over the other platforms reflects:
1. Bing Webmaster Tools verification is confirmed (technical baseline)
2. Shopify SSR means Bingbot receives full page content on first crawl
3. Meta descriptions are now present — Bing Copilot uses these as page summaries
4. Structured data is strong — Organization, BlogPosting, and FAQPage schemas
5. Content length and quality are solid for shopping queries

What prevents a higher score:
1. LinkedIn is dormant — Bing Copilot's strongest commercial entity signal for brands
2. No IndexNow — Bing must wait for Bingbot recrawl rather than receiving instant URL push on content updates
3. Product schema errors on 7 products ("Happimess Dev")

### Bing Copilot Optimization Actions

**Action 1 (HIGH) — Activate LinkedIn posting**
LinkedIn is a Microsoft property. Bing Copilot uses LinkedIn company page signals as the primary commercial entity verification for brands. A company page with recent activity, complete About section, and 100+ followers significantly outperforms a dormant page. Minimum viable plan: 2 posts/month for 60 days + complete all profile fields (description, industry, size, specialties).

**Action 2 (HIGH) — Implement IndexNow**
IndexNow allows instant URL submission to Bing when content is published or updated. Given Happimess's active blog cadence (3+ new articles/month, frequent lastmod updates), IndexNow ensures Bing indexes updates within hours rather than days. Setup:
1. Generate a key at bing.com/indexnow
2. Upload the key file to Shopify Files (e.g., `abc123.txt`)
3. Add the key meta tag to theme.liquid: `<meta name="indexnow-key" content="abc123">`
4. Optionally integrate with Bing Webmaster Tools for automated submission
Effort: 30–45 minutes.

**Action 3 (MEDIUM) — Fix "Happimess Dev" product schema**
Bing Copilot's product recommendation responses use Product schema brand.name for display. A response recommending the "elmo" trash can would show "Happimess Dev" as the brand — undermining trust in the AI recommendation.

**Action 4 (LOW) — Install Microsoft Clarity**
Clarity (Microsoft's free behavior analytics) provides user behavior data to Bing and can influence Bing's content quality scoring for the site. It also integrates with Bing Webmaster Tools. Shopify installation via a script tag in theme.liquid.

---

## Cross-Platform Priority Matrix

Actions ordered by combined impact across all 5 platforms:

### Must-Do This Week (≤1 hour each, affects 3+ platforms)

| # | Action | Platforms Affected | Est. Score Gain |
|---|--------|-------------------|-----------------|
| 1 | Fix `/.well-known/ucp` staging domain (15 min) | ChatGPT, Bing | +4–6 pts composite |
| 2 | Fix 7 products with `"Happimess Dev"` brand.name (15 min in Shopify Admin) | ChatGPT, Google AIO, Bing | +3–4 pts |
| 3 | Deploy spec-compliant `llms.txt` from today's generated file (45 min) | Perplexity, ChatGPT, Gemini | +3–5 pts |
| 4 | Add blank line between adsbot-google and Nutch in robots.txt (5 min) | All crawlers | +1 pt |
| 5 | Add `sitemap_agentic_discovery.xml` to robots.txt Sitemap: directive (5 min) | All crawlers | +1 pt |

### Do This Month (2–4 hours each, high cross-platform impact)

| # | Action | Platforms Affected | Est. Score Gain |
|---|--------|-------------------|-----------------|
| 6 | Create Wikidata Q-entity for Happimess (2 hrs) | ChatGPT, Gemini, Perplexity, Bing | +8–12 pts Brand Authority |
| 7 | Hyperlink all EPA/USDA/CDC citations to source documents (2 hrs) | Google AIO, Perplexity, ChatGPT | +4–6 pts Citability |
| 8 | Create Google Business Profile (30 min + verification) | Gemini, Google AIO | +5–7 pts Gemini |
| 9 | Implement IndexNow (45 min) | Bing Copilot | +3–4 pts Bing |
| 10 | Activate LinkedIn — 2 posts/month, complete profile (ongoing) | Bing Copilot, ChatGPT | +4–6 pts (60-day lag) |

### Do Next Quarter (strategic, high long-term impact)

| # | Action | Platforms Affected | Est. Score Gain |
|---|--------|-------------------|-----------------|
| 11 | Publish 3 YouTube product videos + embed on blog posts | Gemini, Google AIO | +5–8 pts Gemini |
| 12 | Pitch The Spruce / Apartment Therapy for "best trash cans" roundup | All platforms | +10–15 pts Brand Authority |
| 13 | Seed authentic Reddit community presence | Perplexity, ChatGPT | +10–15 pts Perplexity |
| 14 | Add original testing data to flagship articles | All platforms | +5–8 pts Citability |

---

## Score Projection After Quick Wins (Actions 1–5)

| Platform | Current | After Quick Wins | After Full Month | Ceiling (90 days) |
|----------|---------|-----------------|-----------------|-------------------|
| Google AI Overviews | 51 | 53 | 60 | 70 |
| ChatGPT Web Search | 56 | 63 | 68 | 78 |
| Perplexity AI | 44 | 47 | 55 | 65 |
| Google Gemini | 49 | 51 | 58 | 70 |
| Bing Copilot | 58 | 60 | 66 | 75 |
| **Composite** | **52** | **55** | **61** | **72** |

---

## Platform Feature Coverage Matrix

| Feature | Google AIO | ChatGPT | Perplexity | Gemini | Bing |
|---------|-----------|---------|------------|--------|------|
| AI crawler access | ✅ | ✅ | ✅ | ✅ | ✅ |
| Shopify SSR | ✅ | ✅ | ✅ | ✅ | ✅ |
| Webmaster verification | ✅ | N/A | N/A | ✅* | ✅ |
| Organization schema | ✅ | ✅ | ✅ | ✅ | ✅ |
| BlogPosting schema | ✅ | ✅ | ✅ | ✅ | ✅ |
| FAQPage schema | ✅ | ✅ | ✅ | ✅ | ✅ |
| Product schema (clean) | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Meta descriptions | ✅ | ✅ | ✅ | ✅ | ✅ |
| agents.md (UCP) | N/A | ✅ | N/A | N/A | N/A |
| /.well-known/ucp (working) | N/A | ❌ | N/A | N/A | N/A |
| llms.txt (compliant) | ➖ | ⚠️ | ❌ | ➖ | ➖ |
| Wikidata entity | ⚠️ | ❌ | ⚠️ | ❌ | ⚠️ |
| Wikipedia article | ❌ | ❌ | ❌ | ❌ | ❌ |
| Reddit community presence | ❌ | ❌ | ❌ | ❌ | ❌ |
| LinkedIn active | ❌ | ⚠️ | ❌ | ❌ | ❌ |
| YouTube content | ❌ | ❌ | ❌ | ❌ | ❌ |
| Google Business Profile | ❌ | N/A | N/A | ❌ | ❌ |
| IndexNow | N/A | N/A | N/A | N/A | ❌ |
| Linked external citations | ❌ | ❌ | ❌ | ❌ | ❌ |
| Original research data | ❌ | ❌ | ❌ | ❌ | ❌ |

*Google Search Console verified

✅ Present | ⚠️ Partial/Issue | ❌ Missing/Broken | ➖ Not applicable | N/A Not a signal for this platform
