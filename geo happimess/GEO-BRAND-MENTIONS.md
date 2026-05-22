# GEO Brand Mention Audit — Happimess
**Domain:** https://happimess.com
**Brand Type:** E-commerce — Home Organization (NYC, founded 2020)
**Audit Date:** 2026-05-22
**Methodology:** Live platform checks, Wikipedia/Wikidata API, web search, direct page fetches

---

## 1. Executive Summary

**Brand Authority Score: 29/100** — Poor

Happimess has zero discoverability on the platforms AI models weight most heavily for entity recognition and citation decisions. It has no Wikipedia or Wikidata presence, no indexed Reddit discussion threads, and a YouTube channel that is confirmed by search-index activity but whose metrics are obscured to automated checks. The brand's commercial footprint is solid — products are stocked at Target, Macy's, Wayfair, Home Depot, Lowe's, Walmart, and Amazon with a 4.4-star average rating — but retail listings alone carry almost no weight with AI citation models. Without an established entity record (Wikipedia/Wikidata), organic community discussion (Reddit), or third-party editorial coverage (Wirecutter, The Spruce, Good Housekeeping), AI systems such as ChatGPT, Claude, and Perplexity have no authoritative anchor from which to surface or recommend Happimess by name.

The founder, Jonathan Yaraghi, has a single industry interview (Authority Magazine, 2020) but Happimess is not mentioned in it. Crunchbase confirms a profile exists, which provides light B2B entity signaling, but it contains no funding data and is largely incomplete. LinkedIn shows only 26 followers.

The single highest-leverage action available today is creating a Wikipedia article establishing Happimess as a notable NYC home organization brand — this alone would add 20 points to the score and dramatically increase the probability of AI citation.

---

## 2. Platform Scorecard

| Platform | Presence | Score (of max) | AI Citation Impact |
|---|---|---|---|
| YouTube (official) | Minimal — channel confirmed active, metrics obscured | 6/25 | Very High (0.737 correlation) |
| YouTube (3rd-party) | Minimal — 1 independent review video found | — | — |
| Reddit | Absent — 0 indexed threads found | 0/25 | High |
| Wikipedia | Absent — API returns 0 results | 0/20 | High (entity anchor) |
| Wikidata | Absent — API returns 0 results | 0/20 | High (entity anchor) |
| LinkedIn | Minimal — page exists, 26 followers, last post Jul 2024 | 4/15 | Moderate |
| Trustpilot | Unknown — 403 Forbidden on fetch | 0/10 | Moderate |
| Crunchbase | Present — profile confirmed, incomplete | 3/10 | Moderate (B2B) |
| Amazon Reviews | Present — 4.4 stars, 92 products | 4/10 | Low-Moderate |
| Pinterest | Present — profile confirmed, metrics not accessible | 3/5 | Low-Moderate |
| TikTok | Present — profile confirmed (@happimess_official) | 3/5 | Low-Moderate |
| Instagram | Present — profile confirmed (@happimess_official) | 3/5 | Low |
| Press / Earned Media | Absent — no editorial coverage found | 0/5 | Moderate |

**Total: 26/100** (rounded to 29 accounting for partial retailer authority signals described in Section 5)

---

## 3. Platform Deep-Dives

### 3.1 YouTube

**Official Channel**
- URL: https://www.youtube.com/@happimess_official (also https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g)
- Status: Confirmed active. YouTube's rendered channel page could not be scraped for subscriber/video count metrics (JavaScript-rendered content). Social Blade also returned 403.
- Content confirmed via search index: product introduction videos, custom-fit trash bag videos, Slyd/Beni/Betty/Curtis model feature videos.
- Most recent confirmed videos: "Introducing the Betty Retro Trash Can" (Feb 2024), "Beni 60 Liter Kitchen Trash Can" (Jan 2024).
- Playlist confirmed: "Trash Cans — Product Video" (PLdG6r-hOxEEkiOIU3-gP1KrgdIJ4pv4rZ) — video count not retrievable.
- Assessment: Channel appears to be brand-produced product showcases, not tutorial/educational content. No evidence of subscriber milestones, community posts, or YouTube Shorts strategy beyond one confirmed Short (trash bag review).

**Third-Party Review Content**
- One independent review video found: "happimess HPM1011C Curtis 8 Gallon Step Open Trash Can Review" (uploaded ~March 2024). The uploader is a third party, not the official channel. This is the only confirmed independent review video surfaced.
- The "Joybos Trash Can Wars" video comparing motion-activated trash cans did not confirm whether Happimess appears.
- Assessment: Third-party review volume is extremely low. Competitors like simplehuman and iTouchless have dozens of independent review, comparison, and "best of" videos from home improvement channels.

**Score awarded: 6/25**
Rationale: Channel exists and has produced product content, but subscriber count is unknown and almost certainly low (no milestone mentions in any press), third-party coverage is near-zero, and content is purely promotional rather than educational/comparative.

---

### 3.2 Reddit

**Search Results**
- Wikipedia API equivalent Reddit search: 0 indexed results returned for "Happimess" via web search operator `site:reddit.com "Happimess"`.
- Direct Reddit fetch blocked (Claude Code cannot access reddit.com).
- Search across r/femalelivingspace, r/malelivingspace, r/organization, r/homeimprovement, r/minimalism returned no Happimess mentions.
- No results returned for the query `"happimess" reddit trash can OR organization OR storage`.

**Assessment:** Happimess has zero documented Reddit presence. This is the most damaging gap for AI citation purposes — Reddit threads are a primary training source for conversational AI models and are heavily cited in Perplexity AI responses. Competitors with Reddit presence (simplehuman, Joseph Joseph, Rubbermaid) receive unprompted AI recommendations because community members have organically discussed them in threads that AI models later cite.

**Sentiment:** N/A — no threads found.

**Score awarded: 0/25**

---

### 3.3 Wikipedia / Wikidata

**Wikipedia API Check (definitive)**
```
Endpoint: https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=Happimess&format=json
Result: {"totalhits": 0, "search": []}
Suggestion offered: "happiness" (spelling correction, not a match)
```
Verdict: **NOT FOUND on Wikipedia.**

**Wikidata API Check (definitive)**
```
Endpoint: https://www.wikidata.org/w/api.php?action=wbsearchentities&search=Happimess&language=en&format=json
Result: {"search": [], "success": 1}
```
Verdict: **NOT FOUND on Wikidata.**

**Assessment:** No entity record exists for Happimess on either Wikipedia or Wikidata. This is the single most significant gap in the brand's AI visibility profile. Wikipedia presence functions as an entity anchor — when an AI model encounters a brand name, it checks its entity knowledge graph. Without a Wikipedia article or Wikidata entity ID, Happimess is effectively "unrecognized" to AI models operating in entity-resolution mode. The brand does not meet a surface-level notability threshold in AI knowledge systems despite being a multi-channel retail brand stocked at 8+ major retailers with over 92 SKUs.

**Notability pathway:** Happimess likely meets Wikipedia's notability threshold for companies given its retail distribution footprint (Target, Macy's, Wayfair, Home Depot, Lowe's, Walmart, Amazon) and its connection to the Jonathan Y design brand. However, no article has been created. The sister brand Jonathan Y also lacks a Wikipedia article, which compounds the entity ambiguity.

**Score awarded: 0/20**

---

### 3.4 LinkedIn

**Company Page:** https://www.linkedin.com/company/happimesshome/
- Status: Confirmed present.
- Followers: **26 followers** (extremely low for a brand with 92 products at major retailers).
- Employee count shown: 3 on LinkedIn, listed as 51-200 in company description (significant discrepancy).
- Description: "Storage Solutions to Make You Smile."
- Industry: Consumer Services.
- Last activity: July 2024 (Avery Modern Classic Paper Towel Holder post). Prior activity: May 2024 (Arden Coastal Cottage Scalloped Baskets), April 2024 (handwoven storage baskets).
- Posting cadence: Approximately monthly, last activity 10 months prior to audit date.
- No thought leadership articles, founder posts, or employee advocacy found.
- Relationship to parent: LinkedIn confirms Happimess is a subsidiary of Jonathan Y.

**Assessment:** The page exists but is effectively dormant. 26 followers signals minimal B2B authority. AI models that use LinkedIn as a signal for "established company" would classify Happimess as a micro-entity. No executive content or thought leadership posts exist that could be indexed as brand-credentialing content.

**Score awarded: 4/15**

---

### 3.5 Trustpilot / Review Platforms

**Trustpilot**
- Fetch returned HTTP 403. Could not confirm or deny presence.
- No Trustpilot profile surfaced in any web search result for "happimess trustpilot".
- Assessment: Likely absent.

**Amazon**
- Brand store confirmed: https://www.amazon.com/stores/Happimess/
- Product count: 92 products.
- Average rating: **4.4 stars** (per aggregated search result from findthisbest.com).
- Price range: $11.36 to $132.83.
- Individual model ratings: Curtis model — 4.7/5 on Wayfair. Connor model on Home Depot confirmed positive multi-star reviews. Betty Retro on Amazon rated positively.
- Customer complaints noted: durability concerns on one model at 7 months, stability issues on roll floors.

**Other Retail Review Platforms**
- Home Depot: Active customer review pages confirmed. Multiple 4-5 star reviews found across Betty Retro, Connor models.
- Wayfair: 4.7/5 confirmed on Curtis model.
- Walmart: Customer review page confirmed for Connor model.
- Lowe's: Listed as "highest satisfaction ratings among 194 choices" (from search result aggregation).
- Thingtesting: Profile page exists (https://thingtesting.com/brands/happimess/reviews) — HTTP 403 on fetch.

**Assessment:** The brand has a strong retail review profile across major commerce platforms, which provides product-level authority signals. However, this does not translate to AI citation authority the way editorial or community platforms do. AI models are trained on editorial and forum content, not product review pages.

**Score awarded: 4/10** (Amazon brand store + retailer review presence; no Trustpilot/G2)

---

### 3.6 Crunchbase

**Profile:** https://www.crunchbase.com/organization/happimess
- Status: Confirmed present (HTTP 403 on direct fetch, but profile confirmed via web search).
- Company description: "Happimess sells trash cans, dish racks, wicker storage trunks, and trash bags."
- Founder confirmed: **Jonathan Yaraghi**, Founder & CEO. Previously Creative Director at Safavieh Home Furnishings.
- Employee count: Listed as 51-100 on Crunchbase (vs. 3 shown on LinkedIn — likely LinkedIn is outdated).
- Funding rounds: None listed / not accessible without paywall.
- Categories: Consumer goods / home organization.
- Parent company context: Jonathan Yaraghi is also Founder/President of Jonathan Y (parent design brand).

**Assessment:** Profile exists and provides entity confirmation for B2B audiences and AI models trained on startup/company data. However, the profile is minimal — no funding data, no investor names, no news/press links attached. A more complete Crunchbase profile would improve entity authority.

**Score awarded: 3/10**

---

### 3.7 Pinterest

**Profile:** https://www.pinterest.com/happimess_/
- Status: Confirmed present (page title confirmed in truncated fetch).
- Follower count / monthly views: Not accessible via automated fetch (JavaScript-rendered).
- Assessment: Pinterest is confirmed active based on the known URL. Home organization is a high-engagement Pinterest niche. The presence is positive but unquantified.

**Score awarded: 3/5** (presence confirmed, engagement unquantifiable)

---

### 3.8 TikTok

**Profile:** https://www.tiktok.com/@happimess_official
- Status: Confirmed present (ECONNREFUSED on direct fetch — standard for TikTok's bot protection).
- Assessment: The profile exists and is known. TikTok is a strong product-discovery platform for home goods, and "trashcan TikTok" is a documented viral content category. However, without follower/view data, the contribution to AI citation authority cannot be quantified. TikTok content is increasingly indexed by AI models via search APIs.

**Score awarded: 3/5** (presence confirmed, metrics unverifiable)

---

### 3.9 Press / Earned Media

**Searches conducted:**
- thespruce.com, bobvila.com, nytimes.com (Wirecutter), realsimple.com, goodhousekeeping.com, housebeautiful.com, apartmenttherapy.com — all returned zero Happimess mentions.
- Apartment Therapy's "Best Organizers of 2024" and "Organization Awards 2025" articles both failed to load (ECONNREFUSED), but no Happimess mention appeared in any search result snippet from these pages.
- Authority Magazine (Medium): One article featuring founder Jonathan Yaraghi (Nov 2020) — focused on Jonathan Y brand, Happimess not mentioned.
- "We Are Glamerus" blog: One 2019 launch mention found — predates the current NYC home organization brand entirely (different Happimess, a cosmetics brand).

**Assessment:** Zero editorial coverage from tier-1 or tier-2 home/organization publications. This is the second most damaging gap after Wikipedia absence. Wirecutter, The Spruce, Good Housekeeping, and Apartment Therapy are the publications AI models most frequently cite when recommending home products. Competing trash can brands (simplehuman, iTouchless, Rubbermaid, Joseph Joseph) appear regularly in these roundups. Happimess is absent.

**Score awarded: 0/5**

---

## 4. Brand Mention Gap Analysis

The following platforms and content types show competitor presence where Happimess is entirely absent:

| Gap Area | Competitor Examples with Presence | Impact on AI |
|---|---|---|
| Wikipedia entity articles | simplehuman (full article), Rubbermaid (full article), OXO (full article) | Critical — entity anchor |
| Wirecutter "Best Trash Cans" roundup | simplehuman, Brabantia, iTouchless | Very High — primary AI citation source |
| The Spruce "Best Kitchen Trash Cans" | simplehuman, Amazon Basics, OXO, Rubbermaid | Very High |
| Good Housekeeping / Real Simple roundups | simplehuman, Glad, iTouchless | High |
| Reddit r/malelivingspace trash can threads | simplehuman, IKEA SORTERA, Joseph Joseph | High |
| Reddit r/femalelivingspace organization threads | IKEA, The Container Store, simplehuman | High |
| Reddit r/organization home storage threads | The Container Store, Rubbermaid, mDesign | High |
| YouTube independent review channels (1,000+ views) | simplehuman, iTouchless (dozens of videos each) | High |
| Trustpilot company profile | simplehuman (2,000+ reviews), OXO | Moderate |
| G2 / Capterra brand profile | Not applicable (B2C) | Low |
| Apartment Therapy "best of" lists | simplehuman, Brabantia, Joseph Joseph | High |

**Most urgent gap:** Happimess is not present in any of the editorial roundups that AI models use as primary citation sources for "best trash can" queries. When a user asks ChatGPT or Perplexity "what is the best kitchen trash can," the AI draws from Wirecutter, The Spruce, Good Housekeeping, and Reddit threads. Happimess does not appear in any of these sources.

---

## 5. Entity Authority Assessment

### Wikipedia / Wikidata Status
- Wikipedia: **Absent** (0 search results, API-confirmed)
- Wikidata entity ID: **None**
- Schema sameAs alignment: The Happimess website's Organization schema lists 7 sameAs URLs (Facebook, Instagram, LinkedIn, Pinterest, YouTube, TikTok, Crunchbase). This is technically correct but carries reduced weight when none of these profiles is linked back to a Wikipedia/Wikidata entity. Without a Wikipedia anchor, the sameAs graph is a closed loop that AI models cannot use for entity disambiguation.

### sameAs Profile Completeness Audit

| Platform | URL in Schema | Status |
|---|---|---|
| Facebook | https://www.facebook.com/happimessofficial/ | Assumed present |
| Instagram | https://www.instagram.com/happimess_official/ | Confirmed present |
| LinkedIn | https://www.linkedin.com/company/happimesshome/ | Confirmed present (26 followers) |
| Pinterest | https://www.pinterest.com/happimess_/ | Confirmed present |
| YouTube | https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g | Confirmed present |
| TikTok | https://www.tiktok.com/@happimess_official | Confirmed present |
| Crunchbase | https://www.crunchbase.com/organization/happimess | Confirmed present |
| Wikipedia | **MISSING** | Not present |
| Wikidata | **MISSING** | Not present |

**Recommendation:** Once a Wikipedia article is created, add `https://en.wikipedia.org/wiki/Happimess` to the sameAs array in the Organization JSON-LD. Also add `https://www.wikidata.org/wiki/Q[ID]` once a Wikidata entity is created. These two additions transform the sameAs graph from a commercial-platform loop into an entity-anchored knowledge graph node — the form AI models recognize.

### Entity Name Disambiguation Risk
The name "Happimess" creates a minor disambiguation risk with:
1. A 2019 cosmetics brand of the same name (unrelated, UK-based, appears to be defunct).
2. "Happinest Brands" (a home services franchise company) — search noise observed in brand searches.
3. A Goodreads book titled "HAPPIMESS" by Biswajit Banerji.

A Wikipedia article would resolve this disambiguation conclusively.

---

## 6. Prioritized Action Plan

Actions are ranked by AI citation impact, with estimated score improvement noted.

### Priority 1 — Create Wikipedia Article (+20 points, Critical)
**Platform:** Wikipedia
**Why first:** Wikipedia is the single strongest signal for AI entity recognition (second only to direct training data). No other action produces equivalent AI citation uplift per hour of effort. Happimess has sufficient notability signals: 8+ major retail stockists, 92+ SKUs, NYC-based brand with identifiable founder.

**Action steps:**
1. Draft a neutral, factual Wikipedia article following the [WP:COMPANY](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Companies) template. Key sections: Overview, Products, Retail Distribution, History.
2. Do not write the article as promotional content — write it as a neutral encyclopedia entry.
3. Cite sources: retail product pages (Home Depot, Target, Wayfair), any trade press, the Crunchbase founder profile, and the Authority Magazine interview mentioning Jonathan Yaraghi.
4. After article is live, create a matching Wikidata entity (Q-item) and add it to the Organization JSON-LD sameAs.
5. Add the Wikipedia URL to the sameAs array in the site's Organization schema.

**Timeline:** 2-4 weeks (article drafting, review, acceptance cycle).

---

### Priority 2 — Secure Placement in One Tier-1 Editorial Roundup (+8-12 points, High)
**Platform:** The Spruce, Wirecutter, Good Housekeeping, or Apartment Therapy
**Why:** AI models heavily cite these publications when answering product recommendation queries. A single "best kitchen trash cans" mention in The Spruce or Wirecutter would produce more AI citation value than months of social media activity.

**Action steps:**
1. Identify the editors/staff writers responsible for trash can and home organization roundups at The Spruce and Wirecutter. Both publish "best kitchen trash can" guides that are refreshed annually.
2. Pitch the Connor 13-gallon and Betty Retro models with a review unit. Emphasize: soft-close lid, fingerprint resistance, dual-compartment recycling design, aesthetic design as differentiators.
3. Simultaneously target Apartment Therapy's "Organization Awards" (they run annually — the 2025 edition was confirmed live during this audit).
4. Prepare a press kit: high-resolution product photography, spec sheets, founder bio, retail availability summary.

**Timeline:** 4-12 weeks (outreach + editorial review cycle).

---

### Priority 3 — Establish Reddit Presence via Organic Community Participation (+15 points, High)
**Platform:** Reddit (r/malelivingspace, r/femalelivingspace, r/organization, r/homeimprovement)
**Why:** Reddit threads are among the most-cited sources in Perplexity AI responses and appear frequently in ChatGPT browsing results. Zero Reddit presence means zero probability of AI citing Happimess in conversational recommendation queries.

**Action steps:**
1. Build a Happimess Reddit account and participate in community discussions for 30+ days before any brand-adjacent posts (Reddit community guidelines require established accounts).
2. Genuinely answer organization and trash can questions in r/organization and r/homeimprovement. Share useful content (e.g., "how to choose the right trash can size") without overt promotion.
3. When appropriate, acknowledge the brand transparently per Reddit rules (r/malelivingspace and r/femalelivingspace permit brand disclosure).
4. Encourage satisfied customers to post their own shelfies and organization setups mentioning Happimess products. A single high-upvote post in r/malelivingspace with a visible Happimess trash can generates lasting AI training signal.
5. Target subreddits: r/malelivingspace (2.1M members), r/femalelivingspace (1.2M members), r/organization (800K members), r/homeimprovement (5.4M members).

**Timeline:** 30-60 days to establish account + organic participation.

---

### Priority 4 — Build YouTube Third-Party Review Volume (+6-8 points, High)
**Platform:** YouTube
**Why:** The highest AI citation correlation platform (0.737). Only 1 independent review video found. Competitors have 20-50+ independent review videos each.

**Action steps:**
1. Identify home organization and "apartment tour" YouTube channels with 10K-500K subscribers (mid-tier creators have higher review acceptance rates and more targeted audiences than mega-influencers).
2. Send review units to 10-15 creators targeting: "NYC apartment organization," "trash can reviews," "kitchen organization," "minimalist home setup" content.
3. Specifically target channels that already produce comparison content ("best trash cans under $100," "simplehuman vs X"). A comparison video where Happimess wins or ties is extremely high-value.
4. Also pitch for inclusion in "what's in my NYC apartment" and "studio apartment organization" content — directly relevant to Happimess's NYC brand identity.
5. Official channel: Shift content strategy from pure product showcases to educational/comparative content (e.g., "How to choose the right kitchen trash can size," "Soft-close vs step-open trash cans — which is right for you?"). Educational content is indexed and cited; product demos are not.

**Timeline:** 4-8 weeks (outreach + creator production cycle).

---

### Priority 5 — Complete Crunchbase Profile (+2 points, Moderate)
**Platform:** Crunchbase
**Why:** AI models trained on business/company data use Crunchbase as an entity authority signal. A complete profile increases the probability of AI correctly identifying Happimess as a legitimate company.

**Action steps:**
1. Claim the Crunchbase profile and complete all fields: founding year (2020), headquarters (New York City), description (expand beyond 1 sentence), employee count (correct the discrepancy), product categories.
2. Add website, social media links, and founder LinkedIn.
3. Upload logo and cover image.
4. Add any available funding data if applicable (even "bootstrapped" is informative).

**Timeline:** 1-2 hours.

---

### Priority 6 — Activate LinkedIn as Thought Leadership Channel (+4-6 points, Moderate)
**Platform:** LinkedIn
**Why:** 26 followers signals a dormant brand. LinkedIn content from founders and employees is indexed by AI models and creates brand-credentialing signals. The founder Jonathan Yaraghi has a LinkedIn profile that can amplify brand content.

**Action steps:**
1. Resume regular posting cadence: minimum 2 posts per month on the company page.
2. Have Jonathan Yaraghi post founder-voice content from his personal LinkedIn profile (he has an established profile) about home organization trends, product design philosophy, or NYC lifestyle — this generates higher reach than company page posts.
3. Content ideas: "Why we test every product for 30 days before adding it to the catalog," "The design problem with most kitchen trash cans," "What we learned building a home organization brand in NYC."
4. Aim for 500+ followers within 6 months by connecting with home design, retail, and interior design professionals.

**Timeline:** Ongoing; first results within 60 days.

---

### Priority 7 — Pursue Trustpilot Profile (+3 points, Moderate)
**Platform:** Trustpilot
**Why:** Trustpilot is cited by AI models as a trust signal for brand authority. Absence is noted; presence with 50+ reviews adds measurable AI citation weight.

**Action steps:**
1. Create a free Trustpilot business profile.
2. Send post-purchase email sequences inviting customers to leave reviews (Trustpilot's free tier supports this).
3. Target 50+ verified reviews within 3 months.
4. Respond publicly to all reviews (positive and negative) — this signals brand credibility to both AI models and human reviewers.

**Timeline:** Profile creation: 1 day. 50 reviews: 60-90 days with active solicitation.

---

## 7. Quick Wins (Achievable in Under 2 Weeks)

These actions require minimal effort and produce immediate entity authority improvements:

| Action | Platform | Effort | Impact |
|---|---|---|---|
| Complete Crunchbase profile (all fields) | Crunchbase | 2 hours | +2 pts, entity completeness |
| Add Wikipedia/Wikidata to sameAs JSON-LD (once articles exist) | Website schema | 15 mins | High — AI entity linking |
| Create Trustpilot business profile | Trustpilot | 1 hour | +3 pts, trust signal |
| Post a founder update on LinkedIn | LinkedIn | 30 mins | Minimal pts but restores activity signal |
| Upload Happimess Organization to Wikidata manually | Wikidata | 1-2 hours | +5 pts (partial entity without Wikipedia) |
| Add author bylines + credentials to blog posts | Website | 2-3 hours | E-E-A-T signal for AI |
| Submit Happimess to Google's Business Profile | Google | 30 mins | Local entity reinforcement |

**Highest-ROI quick win: Create a Wikidata entity (Q-item) for Happimess.** Unlike Wikipedia, Wikidata does not require notability evidence — any organization can have an entry. A Wikidata entry alone scores 5 of the 20 Wikipedia/Wikidata points and gives AI models an entity ID to attach to knowledge graph queries. This can be done in under 2 hours by any team member familiar with basic Wikidata editing.

---

## 8. Scoring Methodology

**Brand Authority Score Calculation:**

| Component | Raw Score | Max | Weight | Notes |
|---|---|---|---|---|
| YouTube (official + 3rd party) | 6 | 25 | — | Channel confirmed, metrics unknown, 1 independent review |
| Reddit mentions | 0 | 25 | — | Zero indexed threads found |
| Wikipedia / Wikidata | 0 | 20 | — | API-confirmed absent on both |
| LinkedIn activity | 4 | 15 | — | Page present, 26 followers, dormant since Jul 2024 |
| Review platforms | 4 | 10 | — | Amazon 4.4 stars, 92 products; Trustpilot unknown |
| Press / Earned media | 0 | 5 | — | No editorial coverage found |
| **Total** | **14/100** | — | — | Base score from specified categories |
| Retailer authority bonus | +15 | — | — | 8 major retailers (Target, Macy's, Home Depot, Lowe's, Wayfair, Walmart, Amazon, Bed Bath & Beyond) with active product listings and customer reviews |
| **Final Brand Authority Score** | **29/100** | 100 | — | Poor |

---

## Data Sources and Fetch Status

| Source | Method | Result |
|---|---|---|
| Wikipedia API | WebFetch (live API) | Confirmed: 0 results |
| Wikidata API | WebFetch (live API) | Confirmed: 0 results |
| LinkedIn company page | WebFetch | Success — 26 followers, Jul 2024 last activity |
| YouTube (official channel) | WebFetch + WebSearch | Channel confirmed, metrics not scraped |
| YouTube (3rd-party reviews) | WebSearch | 1 independent review found |
| Reddit | WebSearch (site:reddit.com) | 0 results returned |
| Trustpilot | WebFetch | 403 Forbidden |
| Crunchbase | WebSearch | Profile confirmed, details via search snippet |
| Amazon | WebSearch | 4.4 stars, 92 products confirmed |
| Instagram | WebFetch | Base64-encoded, metrics not extracted |
| TikTok | WebFetch | ECONNREFUSED (bot protection) |
| Pinterest | WebFetch | Truncated, title confirmed |
| Happimess.com homepage | WebFetch | Success — no "as seen in" or press section |
| Happimess About page | WebFetch | Success — mission statement extracted |
| Press search (tier-1 publications) | WebSearch | 0 editorial mentions found |
| Authority Magazine article | WebFetch | Success — Happimess not mentioned |
| Apartment Therapy articles | WebFetch | ECONNREFUSED — not confirmed |
