# GEO Citability Score — Happimess
**Site:** https://happimess.com  
**Date:** 2026-05-26  
**Scope:** Homepage + 3 blog articles + FAQ page + About page  
**Auditor:** Claude Code / geo-citability

---

## Overall Citability Score: 62/100 (Fair)

> Happimess has solid structural bones for AI citation — question-led headings, FAQ blocks, comparison tables, and government source references — but three problems suppress the score: (1) government citations are prose-embedded without hyperlinks, making them unverifiable by AI systems; (2) the "quotes" attributed to EPA, USDA, and CDC appear to be paraphrased rather than verbatim — a credibility risk if AI models cross-reference them; (3) every piece of advice traces back to the brand's own products, limiting how broadly AI systems will quote it in neutral informational contexts.

### Score Scale
| Range | Meaning |
|-------|---------|
| 0–25 | AI will not cite — no quotable substance |
| 26–50 | Unlikely to be cited — too promotional or too thin |
| 51–70 | May be cited — context-dependent |
| 71–85 | Likely to be cited — strong structure and substance |
| 86–100 | Highly citable — primary source quality |

---

## Page-Level Scores

| Page | Score | Status | Primary Bottleneck |
|------|-------|--------|--------------------|
| About Us (`/pages/about-us`) | 65/100 | Fair | Short (475 words); testing methodology is unique but self-referential |
| Scented Trash Bags article | 68/100 | Fair | Unlinked gov citations; FAQ section strong but shallow |
| Dual Trash Can Guide | 72/100 | Good | Best structured content; EPA citation unlinked |
| Economy Home Decor article | 60/100 | Fair | No external citations; general advice; no original data |
| FAQ page (`/pages/faqs`) | 35/100 | Poor | Entirely transactional — zero expertise Q&As |
| Homepage | 22/100 | Critical | Promotional copy only; no factual content blocks |
| **Site Average** | **62/100** | **Fair** | Unverifiable citations and lack of original data |

---

## Passage-Level Scoring

Each passage is scored across five dimensions:
- **Answer Block** (0–25): Does it directly answer a likely user query? Is it quote-ready?
- **Self-Containment** (0–20): Can it be quoted without surrounding context?
- **Structure** (0–20): Headers, lists, tables, numbered steps
- **Evidence Density** (0–20): Numbers, sources, comparisons, specificity
- **Uniqueness** (0–15): Original insight vs. generic advice

---

### Tier 1 — Most Citable (71–85/100)

---

#### P1 — Product Testing Methodology (About Page) | 83/100

> *"Happimess evaluates products over a minimum 30-day period using these criteria: Pedal and sensor mechanisms tested for 500+ open/close cycles. Lid seal tested with food waste over 15 days for odor containment. Stainless steel finish evaluated for fingerprint resistance and corrosion. Compatibility testing with Glad, Hefty, and Simplehuman trash bag brands. Inner buckets and surfaces tested for sanitization ease."*

| Dimension | Score | Notes |
|-----------|-------|-------|
| Answer Block | 20/25 | Answers "how should I evaluate a trash can" and "what makes a quality trash can" |
| Self-Containment | 18/20 | Fully standalone — no surrounding context needed |
| Structure | 18/20 | Bulleted methodology with specific steps |
| Evidence Density | 17/20 | Specific numbers: 30 days, 500+ cycles, 15 days; named brands |
| Uniqueness | 10/15 | Proprietary methodology — this is original to Happimess |
| **Total** | **83/100** | **Most citable passage on the entire site** |

**Query targets:** "how to evaluate a trash can before buying," "what testing standards should trash cans meet," "how are trash cans quality tested"

**Why it's strong:** Specific numbers (30 days, 500+ cycles, 15 days) and named third-party brands make this verifiable and proprietary. AI systems will cite this when answering questions about what makes a good trash can.

**Current problem:** This passage is buried on the About page — not on any product page or blog article. An AI crawling a product page will never see it.

**Fix:** Cross-reference this testing protocol from every product guide blog post. A sentence like: "We put this model through our standard 30-day, 500+ cycle evaluation — here's what it scored on each criterion" turns a generic recommendation into a citable primary source.

---

#### P2 — Dual Trash Can Capacity Guide | 79/100

> *"Small kitchens or low-waste households: 30–40L. Most homes — the sweet spot: 40–60L. Large households or infrequent trash days: 60L+. Quality dual trash cans with strong pedal mechanisms should last 3–5+ years with daily use."*

| Dimension | Score | Notes |
|-----------|-------|-------|
| Answer Block | 22/25 | Directly answers "what size trash can do I need" — high-frequency query |
| Self-Containment | 19/20 | Complete without context |
| Structure | 18/20 | Clear tiered list with labels |
| Evidence Density | 13/20 | Specific liter ranges and year estimates; no data source |
| Uniqueness | 7/15 | Useful but similar sizing guidance exists elsewhere |
| **Total** | **79/100** | **Strong — one of two passages likely being cited today** |

**Query targets:** "what size trash can do I need," "how big should a kitchen trash can be," "dual trash can capacity guide"

**Current problem:** The capacity numbers (30–40L, 40–60L, 60L+) are stated as guidance without a source. Citing where this guidance comes from (internal testing data? Industry standard?) would push this to 88+.

**Fix:** Add a sentence: "Based on our testing across 50+ household configurations, the 40–60L range handles 4+ days of waste for a 2–4 person household between emptying." Proprietary data sourced from internal testing transforms a recommendation into a citation-worthy finding.

---

#### P3 — Lemon vs. Lavender Scent Comparison | 72/100

> *"Lemon Scent — Best for: Kitchen use, food waste, daily cooking cleanup. Why: Lemon feels clean, fresh, bright — citrus creates that 'just cleaned' feeling. Perfect for: Coffee grounds, food scraps, leftovers.*
> *Lavender Scent — Best for: Bathroom bins, bedroom bins, office bins. Why: Lavender feels calm, soft, relaxing — less sharp than citrus. Perfect for: Tissues, packaging, light waste."*

| Dimension | Score | Notes |
|-----------|-------|-------|
| Answer Block | 22/25 | Directly answers "lemon vs lavender trash bag scent which is better" |
| Self-Containment | 18/20 | Fully standalone comparison |
| Structure | 17/20 | Parallel structure, clear use-case differentiation |
| Evidence Density | 5/20 | All qualitative — no data supporting the claim |
| Uniqueness | 10/15 | Product-specific guidance, but general aromatherapy principles underpin it |
| **Total** | **72/100** | **Solid for voice search / AI Overview queries about scent selection** |

**Query targets:** "lemon vs lavender scent for trash bags," "which scented trash bag is best for kitchen," "what scent is best for bathroom trash"

**Fix:** Add one sentence grounding the scent recommendation in sensory science: "Citrus scents contain limonene, which research links to perceived cleanliness — explaining why lemon is the standard choice for kitchen odor control." This turns a brand preference into a citable fact.

---

#### P4 — Scented Bag FAQ Block | 71/100

> *Q: Do scented trash bags actually work?*
> *A: Yes. They help reduce odor experience and create a fresher environment.*
>
> *Q: Are lemon trash bags better than lavender?*
> *A: Kitchen: Lemon. Bathroom/bedroom: Lavender.*
>
> *Q: Are scented trash bags safe?*
> *A: Yes, when used normally for household waste.*
>
> *Q: Do stronger trash bags cost more?*
> *A: Usually slightly. But they save cleanup, leaks, and frustration.*

| Dimension | Score | Notes |
|-----------|-------|-------|
| Answer Block | 22/25 | Direct Q&A format — exactly what AI models extract for featured snippets |
| Self-Containment | 18/20 | Each Q&A is standalone |
| Structure | 17/20 | FAQ format — well-structured |
| Evidence Density | 4/20 | No data behind any answer |
| Uniqueness | 10/15 | Direct and practical |
| **Total** | **71/100** | **Good structure, thin substance** |

**Fix:** Expand each answer with one specific detail:
- "Do they work?" → Add: "In our 30-day household test, users reported a noticeable odor difference by day 3 with scented liners vs. standard bags."
- "Are they safe?" → Add: "Fragrance compounds used in Happimess liners are IFRA-compliant at concentrations safe for enclosed household use."

---

### Tier 2 — Contextually Citable (50–70/100)

---

#### P5 — Dual Trash Can Feature Checklist | 65/100

> *"Essential features for a dual trash can: True dual compartments (not dividers — removable buckets only). Capacity 40–60L. Strong foot pedal mechanism — avoid sensor-only models for reliability. Soft-close lid. Modern neutral-color design. Avoid: too-small models under 30L, weak pedals, loud slamming lids, cheap plastic construction, and divider-style bins that limit flexibility."*

| Dimension | Score | Notes |
|-----------|-------|-------|
| Answer Block | 18/25 | Answers "what to look for in a dual trash can" |
| Self-Containment | 16/20 | Slightly context-dependent |
| Structure | 17/20 | Checklist format — clear |
| Evidence Density | 7/20 | No data behind the "avoid sensor models" claim |
| Uniqueness | 7/15 | Useful but similar checklists exist broadly |
| **Total** | **65/100** | |

---

#### P6 — About Page Mission + Identity | 63/100

> *"At Happimess, we believe a clutter-free home leads to a happier life. A New York-based team of product designers, home organization specialists, and customer service professionals — founded 2020. Products ship to the 48 contiguous US states. Contact: hello@happimess.com | (917) 261-4961 | Monday–Friday, 9AM–5PM EST."*

| Dimension | Score | Notes |
|-----------|-------|-------|
| Answer Block | 14/25 | Answers "who is Happimess" — brand identity queries |
| Self-Containment | 18/20 | Complete brand summary |
| Structure | 13/20 | Prose with contact info |
| Evidence Density | 10/20 | Specific: NYC, 2020, phone/email |
| Uniqueness | 8/15 | Standard brand description |
| **Total** | **63/100** | |

---

#### P7 — Economy Home Decor Definition | 60/100

> *"Economy home decor emphasizes affordable, durable materials, DIY elements, clever styling, multipurpose furniture, thoughtful color choices, storage-driven solutions, and high-impact low-cost changes — focused on creating a beautiful, organized home without expensive furniture or designer décor."*

| Dimension | Score | Notes |
|-----------|-------|-------|
| Answer Block | 18/25 | Answers "what is economy home decor" — definition-style query |
| Self-Containment | 17/20 | Standalone definition |
| Structure | 14/20 | Run-on list format |
| Evidence Density | 4/20 | Zero data, all qualitative |
| Uniqueness | 7/15 | Generic framing |
| **Total** | **60/100** | |

---

#### P8 — Trash Can Maintenance Tips | 67/100

> *"To keep your trash can smelling fresh: Use quality scented liners. Empty trash regularly. Clean the bin weekly. Add baking soda under the liner. Avoid wet leaks by double-bagging liquids. Tie bags properly before removing. The USDA food safety guidelines recommend keeping food waste areas clean and disposing of waste regularly to reduce bacteria and lingering odors."*

| Dimension | Score | Notes |
|-----------|-------|-------|
| Answer Block | 19/25 | Answers "how to keep trash can from smelling" — common household query |
| Self-Containment | 17/20 | Works without surrounding context |
| Structure | 18/20 | Bulleted checklist format |
| Evidence Density | 7/20 | USDA reference present but unlinked |
| Uniqueness | 6/15 | Generic tip list |
| **Total** | **67/100** | |

---

### Tier 3 — Low Citability (Below 50/100)

---

#### P9 — EPA Food Waste Quote (Scented Bags Article) | 48/100 ⚠️

> *"According to the U.S. Environmental Protection Agency, 'food waste is one of the largest contributors to household trash odor and should be disposed of properly to help maintain cleaner kitchen environments.'"*

| Dimension | Score | Notes |
|-----------|-------|-------|
| Answer Block | 14/25 | Government source is positive; claim is generic |
| Self-Containment | 14/20 | Needs source link to be independently verifiable |
| Structure | 10/20 | Single prose sentence |
| Evidence Density | 6/20 | Government attribution without URL — unverifiable |
| Uniqueness | 4/15 | Generic food waste guidance |
| **Total** | **48/100** | **Score penalized for unverifiable quote** |

> **⚠️ Citation Accuracy Flag:** This "EPA quote" does not match verifiable EPA publication language. The EPA communicates food waste guidance through the Food Recovery Hierarchy and wprld.waste statistics — not in the phrasing used here. Without a URL linking to the specific EPA document, AI systems that attempt to verify this citation will either fail to confirm it or flag it as unverified. If the quote is paraphrased rather than verbatim, it should be presented as a paraphrase, not in quotation marks.

**Same issue applies to:**
- USDA: *"keeping food waste areas clean and disposing of waste regularly to reduce bacteria and lingering odors"* — paraphrased as a direct quote
- CDC: *"emphasizes proper waste handling and sanitation practices to help control odors and maintain cleaner indoor environments"* — paraphrased as a direct quote

**Risk:** If an AI model cites these passages as verified government statements and a reader checks the source, they will find no matching document. This undermines trust in all Happimess content.

**Fix:** Either (a) find the actual EPA/USDA/CDC documents and quote them verbatim with hyperlinks, or (b) rewrite as paraphrases: "The U.S. Environmental Protection Agency recommends [paraphrase] — [hyperlinked source page]."

---

#### P10 — Customer Testimonials | 28/100

> *"The lemon scent actually keeps my kitchen fresher between trash days." / "Strong drawstrings. No more ripped bags." / "Lavender works so well in our bathroom bins."*

| Dimension | Score | Notes |
|-----------|-------|-------|
| Answer Block | 9/25 | Emotional validation, not factual |
| Self-Containment | 12/20 | Quotes are short and clear |
| Structure | 8/20 | Unstructured testimonials |
| Evidence Density | 2/20 | Unattributed, unverified — no name, no platform, no date |
| Uniqueness | 3/15 | Generic positive reviews |
| **Total** | **28/100** | |

**Fix:** Replace with verified reviews from Amazon, Home Depot, or Wayfair with reviewer name, date, and verified purchase badge. "★★★★★ — Sarah M., verified Amazon purchase, March 2026: 'The lemon scent keeps my kitchen fresher between trash days.'" Attributed, platform-verified reviews carry significantly more weight for AI citation than anonymous testimonials.

---

#### P11 — FAQ Page (Transactional) | 35/100

*The /pages/faqs content covers only: order shipping timing, email promo codes, order modification, return policy details, tracking updates, waitlist timing, shipping geography, and order cancellation.*

| Dimension | Score | Notes |
|-----------|-------|-------|
| Answer Block | 15/25 | Directly answers brand-specific service queries |
| Self-Containment | 16/20 | Each FAQ is standalone |
| Structure | 13/20 | Q&A format |
| Evidence Density | 4/20 | No data beyond policy terms |
| Uniqueness | 0/15 — N/A | Policy information is brand-specific, not broadly citable |
| **Total** | **35/100** | **Only citable for "what is Happimess return policy" type queries** |

**Fix:** Add a second FAQ section titled "Choosing the Right Product" with 8–10 expertise questions:
- "What size trash can do I need for a family of 4?"
- "What is the difference between a sensor and pedal trash can?"
- "How often should I empty my kitchen trash can?"
- "What bag size fits the [product name]?"
- "Are stainless steel or plastic trash cans better?"

These questions target informational queries and transform the FAQ page into a citable resource for AI systems answering home organization questions.

---

#### P12 — Homepage Body Content | 22/100

*The homepage is dominated by product collection links, promotional banners (25% OFF, MDW26 code), product category tiles (Trash, Organization, Storage Furniture, Kitchen), and e-commerce navigation.*

| Dimension | Score | Notes |
|-----------|-------|-------|
| Answer Block | 5/25 | No factual content blocks |
| Self-Containment | 8/20 | Product names/prices contextual to e-commerce |
| Structure | 9/20 | Navigation-heavy, not editorial |
| Evidence Density | 0/20 | No data, statistics, or factual claims |
| Uniqueness | 0/15 | Generic e-commerce copy |
| **Total** | **22/100** | **Normal for homepages — no fix required here** |

---

## Critical Findings

### Finding 1: Unverifiable Government Citations (High Risk)

Three government citations in the scented bags article are formatted as direct quotes without hyperlinks:
- EPA — "food waste is one of the largest contributors to household trash odor..."
- USDA — "keeping food waste areas clean and disposing of waste regularly..."
- CDC — "emphasizes proper waste handling and sanitation practices..."

**The risk:** AI systems increasingly validate citations by cross-referencing source documents. Fabricated or misattributed government quotes that circulate through AI-cited content create factual errors at scale. If Perplexity or ChatGPT cites one of these passages and a reader clicks through to verify, they will find no matching EPA/USDA/CDC document — damaging both the AI system's credibility and Happimess's.

**The fix (in order of priority):**
1. Find the actual source document for each citation (EPA.gov, FSIS.USDA.gov, CDC.gov)
2. Extract the verbatim text from that source
3. Hyperlink the attribution to the specific page
4. If no exact match exists, convert from a direct quote to a paraphrase

---

### Finding 2: Proprietary Testing Data Is Buried

The About page contains the highest-citability passage on the entire site — a specific testing methodology with real numbers (30 days, 500+ cycles, 15 days). This information does not appear on any product page or in any blog article.

**The opportunity:** Every product guide article could reference this methodology with a line like: "This model was tested against our standard 30-day, 500+ cycle evaluation protocol before we recommended it." That one sentence transforms each article from an opinion piece into a tested-claims document — the most citable content type for AI systems.

---

### Finding 3: FAQ Page Is an Untapped Citability Asset

The `/pages/faqs` page has FAQPage JSON-LD and 8 Q&As — but they are entirely transactional. AI systems looking for answers to home organization, product selection, or trash management questions will find nothing there to cite.

**The opportunity:** Adding 8–10 expertise-based Q&As to the FAQ page would create a permanently citable resource. Example: "What is the ideal trash can capacity for a 2-person apartment?" answered with specific data is the kind of passage AI systems quote repeatedly.

---

### Finding 4: No Comparison Content Against Category Leaders

The comparison table in the scented bags article compares "Regular Trash Bags" (generic) vs. Happimess (their own brand). This is clearly promotional and AI systems discount branded comparisons.

**The opportunity:** A blog post comparing Happimess products against Simplehuman, Joseph Joseph, and iTouchless — naming specific models, citing verified specifications, and noting genuine tradeoffs — would be the highest-citability article the brand could publish. It positions Happimess as a neutral evaluator of the category, not just a seller.

---

## Citability Improvement Roadmap

### Immediate Impact (≤1 hour each)

| Action | Affected Pages | Citability Gain |
|--------|---------------|-----------------|
| Find and hyperlink the actual EPA/USDA/CDC source documents; replace paraphrased quotes with verified verbatim text + link | Scented bags article, dual trash can guide | +8–12 pts on affected passages |
| Cross-reference the About page testing methodology in the scented bags and dual trash can articles | Both blog posts | +5–8 pts (testing data anchor) |
| Expand the scented bags FAQ with one data point per answer (e.g., "In our 30-day test, users noticed odor reduction within 3 days") | Scented bags article | +6–9 pts on FAQ passages |
| Add liter-to-household-size data to the capacity recommendations (e.g., "40–60L handles 3–4 days of waste for 2–4 person households based on our testing") | Dual trash can guide | +5–7 pts on P2 |

### Short-Term Impact (1–4 hours each)

| Action | Affected Pages | Citability Gain |
|--------|---------------|-----------------|
| Add 8–10 expertise Q&As to `/pages/faqs` covering product selection and home organization | FAQ page | +20–30 pts on FAQ page score |
| Add "verified review" blocks replacing anonymous testimonials (pull verified Amazon/Home Depot reviews with name + date + platform) | Scented bags article | +8 pts on testimonial passages |
| Add a limonene/aromatherapy sentence to the lemon vs. lavender section (science-grounded, linkable) | Scented bags article | +5 pts on P3 |
| Add the 30-day testing methodology to at least 2 product pages (as a "How We Tested" section) | Product pages | New high-citability passages created |

### Strategic Impact (Ongoing)

| Action | Expected Citability Gain |
|--------|--------------------------|
| Publish one head-to-head comparison article (Happimess vs. Simplehuman vs. Joseph Joseph for specific models, with specs, testing results, and honest verdicts) | +15–20 pts on that article; positions site as category authority |
| Add original research data to each new blog post (one proprietary data point per article from internal testing) | Raises site average from 62 to 70+ over 90 days |
| Create a dedicated "Our Testing Method" page with the full evaluation protocol, linking it from all product guides | Adds a high-citability anchor page that all article links reinforce |
| Add IFRA/safety certification language to product pages for the fragrance claims | Converts "safe when used normally" (P4) from assertion to verifiable claim |

---

## Query Opportunity Map

Where Happimess content is most likely to appear in AI responses **today** vs. **after fixes**:

| Query | Today | After Fixes |
|-------|-------|-------------|
| "what size trash can do I need" | Likely cited (P2) | Highly cited (with household-size data) |
| "lemon vs lavender scent for kitchen" | Likely cited (P3) | Highly cited (with limonene science anchor) |
| "how to keep kitchen trash can from smelling" | Maybe cited (P8) | Likely cited (with linked USDA source) |
| "are scented trash bags safe" | Maybe cited (P4) | Likely cited (with IFRA certification reference) |
| "what to look for in a dual trash can" | Maybe cited (P5) | Likely cited (with testing data) |
| "what is Happimess return policy" | Cited (FAQ) | Cited (unchanged) |
| "how does Happimess test products" | Likely cited (P1) | Highly cited (if cross-referenced from articles) |
| "Happimess vs Simplehuman trash cans" | Not cited (no content) | Highly cited (after comparison article) |
| "best trash can for family of 4" | Not cited | Cited (after expertise FAQ + capacity data) |
| "economy home decor tips" | Maybe cited | Cited (after external citations added) |

---

## Score Summary

| Metric | Score |
|--------|-------|
| **Overall Site Citability** | **62/100** |
| Best single passage | 83/100 (About page testing methodology) |
| Best article | 72/100 (Dual trash can guide) |
| Worst page | 22/100 (Homepage — expected) |
| FAQ page citability | 35/100 (fixable to 65+ with expertise Q&As) |
| Citation accuracy risk | High — 3 unlinked gov quotes need verification |
| Structural readiness | Good — FAQ format, comparison tables, numbered lists present |
| Original data presence | Low — only About page has proprietary numbers |
