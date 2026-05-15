# AI Citability Score — https://happimess.com/
**Date:** May 7, 2026 | **Analysis Type:** Passage-Level AI Citation Readiness

---

## Overall Citability Score: 32 / 100 — Poor

The homepage is a **product grid**, not editorial content. AI systems (ChatGPT, Perplexity, Claude, Google AIO) cite pages that answer questions — this page sells products. The low score is expected and appropriate for a homepage. The real citability opportunity lives at `/blogs/news/`.

---

## Passage-Level Scoring

Passages scored across 5 dimensions (0–100 each):
- **AQ** — Answer Quality: Does this passage directly answer a user question?
- **SC** — Self-Containment: Is the passage useful without surrounding context?
- **SR** — Structural Readability: Is it formatted for AI extraction (lists, tables, clear claims)?
- **SD** — Statistical Density: Does it contain data, numbers, or specific facts?
- **UQ** — Uniqueness: Is this information unavailable elsewhere?

| # | Passage | AQ | SC | SR | SD | UQ | Score |
|---|---------|----|----|----|----|----|----|
| 1 | "Trending Products" grid | 5 | 10 | 15 | 5 | 10 | **9** |
| 2 | "Freshen Up with Scented Trash Liners" promo | 20 | 25 | 20 | 10 | 15 | **18** |
| 3 | Footer contact block (email, phone, hours) | 30 | 80 | 50 | 20 | 5 | **37** |
| 4 | Navigation categories (Trash, Organization, Storage) | 10 | 30 | 40 | 5 | 5 | **18** |
| 5 | "Stay up to date" newsletter CTA | 5 | 10 | 10 | 0 | 5 | **6** |

**Top citable passage: Contact block (37/100)** — the most self-contained, factual content on the homepage. Contact info is the only passage an AI model would quote from this page, and only for a "how do I contact Happimess?" query.

---

## Why the Homepage Cannot Be Cited

| Reason | Detail |
|--------|--------|
| No answer-intent content | The page is a product discovery surface, not a Q&A resource |
| No H2 or H3 topic anchors | Single H1 "Happimess" — no topical signal for AI passage extraction |
| No statistics or data | Product prices are the only numbers; not citable facts |
| No unique insights | Product grids are interchangeable across any e-commerce site |
| No author or expertise signal | No byline, no credentials, no editorial voice |
| Duplicate information | All content appears on product/collection pages in more useful form |

---

## Where Citability Lives on This Site

The homepage is the wrong target for citability optimization. Based on the full audit, here are the high-citability pages:

| Page | Best Block Score | Page Score | Citable? |
|------|----------------|------------|----------|
| `/blogs/news/standard-kitchen-trash-can-size` | 79/100 (size table) | **60/100** | Partially |
| `/blogs/news/best-dual-trash-can-for-kitchen-2026-guide-what-actually-works` | 71/100 (FAQ block) | **60/100** | Partially |
| `/blogs/news/the-guide-to-choosing-the-perfect-kitchen-trash-can` | 54/100 (lid comparison) | **44/100** | Below threshold |
| `/blogs/news/tips-for-organizing-your-kitchen-a-comprehensive-guide` | 50/100 | **43/100** | Not citable |
| **Homepage** | 37/100 (contact block) | **32/100** | Not citable |

**The standard-size post's capacity table (79/100) is the single most citable asset on the entire site.** It maps 4 gallon tiers to height ranges and use cases — self-contained, structured, data-rich.

---

## What Would Make the Homepage Citable

A homepage is rarely cited by AI systems, but there are patterns that push it above the threshold:

### Option A — Add a "Why Happimess?" proof section
A 100–150 word block with specific, verifiable claims:
```
- Ships to all 50 US states; avg delivery 3–5 business days
- 30-day return policy on all products
- Founded 2020, 10,000+ customers served
- Products tested to [X standard] before shipping
- Available in English and Spanish
```
Even if this doesn't get cited verbatim, it improves entity recognition and E-E-A-T for the root domain.

### Option B — Add a condensed FAQ block
3–5 questions that AI users commonly ask:
- "Where does Happimess ship?"
- "What is the return policy?"
- "What size trash can do I need for a kitchen?"
- "Are Happimess products available in stores?"

Pair with FAQPage schema. These will be extractable by Google AIO and Perplexity.

### Option C — Feature a "From our blog" editorial teaser
Pull the top 3 blog post titles and first sentences onto the homepage. This signals topical authority to AI crawlers and creates passage-level citation opportunities at the root domain.

---

## Citability Score by AI Platform

| Platform | Score | Reason |
|----------|-------|--------|
| Google AI Overviews | 10/100 | No passage-extractable content, no schema |
| ChatGPT Web Search | 8/100 | No entity content, no answer blocks |
| Perplexity AI | 12/100 | Contact info could appear in "how to reach Happimess" query |
| Claude | 15/100 | llms.txt provides some entity context |
| Bing Copilot | 10/100 | No structured answers |

---

## Recommendation

**Don't optimize the homepage for citability — optimize the blog pages instead.**

Run `/geo citability https://happimess.com/blogs/news/standard-kitchen-trash-can-size` to get a focused citability analysis of the site's strongest page. That post needs:
1. Direct answer in first paragraph (not buried after context-setting)
2. Source citations on the gallon/height data
3. FAQPage schema wrapping the existing FAQ section
4. Named author with a live bio page

Those four changes would push that post from **60/100 to ~75/100** — into genuine AI citation territory.

---

*Generated by Claude Code GEO Skill — `/geo citability https://happimess.com/`*
*Full audit data: `GEO-AUDIT-REPORT.md`*
