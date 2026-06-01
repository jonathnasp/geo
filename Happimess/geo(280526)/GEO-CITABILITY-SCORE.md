# GEO Citability Score — happimess.com
**Original Audit:** May 28, 2026
**This Recheck:** May 28, 2026 — full 6-page live crawl #3
**Methodology:** Passage-level scoring per geo-citability rubric (5 dimensions, weighted)

---

## Overall Citability Score: 79/100 — Good *(up from 71)*

> **2 more fixes confirmed live:** FIX 8 (5 product Q&As on FAQ page) and FIX 9 (Liner Bags section on Dual Guide). Combined +8 points. FAQ page alone jumped 32 → 71. **All remaining fixes are schema-only** — no content changes needed. Schema adds ~5 pts to composite.

### Score Trajectory

| Check | Score | Change | What moved it |
|-------|-------|--------|---------------|
| Original audit | 66/100 | — | Baseline |
| Check 2 — Standard Size improved | 68/100 | +2 | Word count + height data |
| Check 3 — FIX 3 + FIX 4 + FIX 7 | 71/100 | +3 | Founder attribution, EPA stat, household table |
| **Check 4 — FIX 8 + FIX 9 (now)** | **79/100** | **+8** | 5 product Q&As on FAQ, liner section on Dual Guide |
| After all remaining schema fixes | ~84/100 | +5 | FIX 1+2+5+6+8schema+BONUS A+B |
| After new articles | ~88/100 | +4 | Smell guide + placement guide |

---

## Section 1 — Complete Fix Status (Live-Verified)

| Fix | Description | Status | Evidence |
|-----|-------------|--------|----------|
| FIX 1 | Article + FAQPage + Speakable JSON-LD → Kitchen Guide | ❌ **Outstanding** | Zero JSON-LD on page |
| FIX 2 | Organization + sameAs JSON-LD → `theme.liquid` | ❌ **Outstanding** | Zero Organization schema site-wide |
| FIX 3 | Named founder → About Us | ✅ **Done** | "Jonathan Yaraghi, Happimess founder" confirmed live |
| FIX 4 | EPA 32.1% verbatim stat → Dual Guide | ✅ **Done** | "32.1 percent recycling and composting rate" confirmed live |
| FIX 5 | Article + FAQPage JSON-LD → Dual Guide | ❌ **Outstanding** | Zero JSON-LD on page |
| FIX 6 | Article + FAQPage JSON-LD → Standard Size | ❌ **Outstanding** | Zero JSON-LD on page |
| FIX 7 | Household-size table (4 cols) → Standard Size | ✅ **Done** | All 4 rows × 4 columns confirmed live |
| FIX 8 content | 5 product-expertise Q&As → FAQ page | ✅ **Done** | "Product Questions" section + all 5 Q&As confirmed live (13 total) |
| FIX 8 schema | FAQPage JSON-LD → FAQ page | ❌ **Outstanding** | Zero JSON-LD on page |
| FIX 9 | Liner Bags section + 2,000+ words → Dual Guide | ✅ **Done** | "Liner Bags for Dual Trash Cans" section confirmed live; ~2,000 words |
| BONUS A | Homepage brand identity paragraph | ❌ **Outstanding** | No informational text on homepage |
| BONUS B | Homepage FAQPage JSON-LD | ❌ **Outstanding** | Zero schema on homepage |
| BONUS C | New article: "How to Stop Kitchen Trash from Smelling" | ❌ **Not started** | — |
| BONUS D | New article: "Kitchen Trash Can Placement Guide" | ❌ **Not started** | — |

**Done: 6 | Outstanding: 8**

---

## Section 2 — Page Scores (This Recheck)

| Page | Check 3 Score | Check 4 Score | Change | Evidence |
|------|--------------|--------------|--------|----------|
| Kitchen Trash Can Guide | 84/100 | **84/100** | — | No new changes; schema still missing |
| About Us | 90/100 | **90/100** | — | Stable; no schema yet |
| Dual Trash Can Guide | 77/100 | **80/100** | **+3** | ✅ Liner Bags section live; word count at ~2,000 |
| Standard Kitchen Trash Can Size | 70/100 | **70/100** | — | Stable; no schema yet |
| FAQ Page | 32/100 | **71/100** | **+39** | ✅ 5 product Q&As + "Product Questions" heading live |
| Homepage | 20/100 | **20/100** | — | No brand paragraph, no schema |

**5-page composite (excluding homepage): 79/100**

---

## Section 3 — Score Summary by Dimension

| Dimension | Weight | Score | Weighted | vs. Check 3 |
|-----------|--------|-------|----------|-------------|
| Answer Block Quality | 30% | 80/100 | 24.0 | +5 |
| Passage Self-Containment | 25% | 80/100 | 20.0 | +4 |
| Structural Readability | 20% | 80/100 | 16.0 | +2 |
| Statistical Density | 15% | 78/100 | 11.7 | +4 |
| Uniqueness & Original Data | 10% | 74/100 | 7.4 | +5 |
| **Overall** | | | **79.1/100** | **+8** |

---

## Section 4 — Per-Page Block Analysis

### Page 1: Kitchen Trash Can Guide — 84/100

| Section | Words | Answer | Self-Contain | Structure | Stats | Unique | Score |
|---------|-------|--------|-------------|-----------|-------|--------|-------|
| Intro paragraph | 62 | 88 | 85 | 80 | 72 | 70 | 82 |
| What Size? + sizing table | 180 | 95 | 92 | 98 | 92 | 65 | 91 |
| Lid Types + comparison table | 320 | 88 | 85 | 95 | 72 | 68 | 85 |
| Material Guide + table | 210 | 82 | 88 | 95 | 78 | 65 | 83 |
| Single vs Dual section | 150 | 75 | 78 | 72 | 65 | 60 | 72 |
| Features Worth Paying For | 280 | 78 | 80 | 78 | 75 | 68 | 77 |
| Features Not Worth Premium | 180 | 72 | 74 | 72 | 60 | 65 | 70 |
| How We Test (methodology) | 160 | 88 | 90 | 85 | 88 | 93 | 89 |
| FAQ — 5 Q&As | 220 | 92 | 95 | 85 | 82 | 62 | 87 |
| Recommendations by Type | 180 | 78 | 80 | 78 | 72 | 65 | 76 |

**Citability Coverage (blocks >70): 10/10 = 100%**
**Top passage:** Sizing table (91) | **Weakest:** Features Not Worth Premium (70)

---

### Page 2: About Us — Testing Methodology — 90/100

| Section | Words | Answer | Self-Contain | Structure | Stats | Unique | Score |
|---------|-------|--------|-------------|-----------|-------|--------|-------|
| Founder + testing methodology | 95 | 92 | 95 | 82 | 92 | 95 | **91** |
| Brand overview / mission | 80 | 70 | 72 | 68 | 45 | 65 | 67 |
| Product category descriptions | 120 | 65 | 68 | 70 | 40 | 60 | 63 |

**Citability Coverage: 1/3 = 33%**
**Top passage:** Founder + methodology (91/100) — site's highest-scoring passage
**Note:** The methodology paragraph alone is the strongest E-E-A-T signal on the entire site.

---

### Page 3: Dual Trash Can Guide — 80/100 *(was 77)*

| Section | Words | Answer | Self-Contain | Structure | Stats | Unique | Score |
|---------|-------|--------|-------------|-----------|-------|--------|-------|
| Intro paragraph | 65 | 88 | 85 | 82 | 78 | 68 | 83 |
| Why Worth It (EPA 32.1%) | 90 | 84 | 85 | 78 | 88 | 72 | **83** |
| Common Problems | 55 | 45 | 50 | 60 | 30 | 45 | 47 |
| What to Look For | 120 | 70 | 68 | 75 | 55 | 55 | 67 |
| Recommended Product | 80 | 62 | 60 | 65 | 45 | 55 | 60 |
| Real-Life Use Cases | 60 | 42 | 45 | 50 | 20 | 40 | 41 |
| Dual vs Single table | 70 | 65 | 72 | 88 | 42 | 55 | 65 |
| Not Recommended | 50 | 48 | 50 | 55 | 35 | 45 | 48 |
| Pro Tips | 55 | 52 | 55 | 60 | 28 | 42 | 50 |
| **Liner Bags (FIX 9 — new)** | 160 | 82 | 85 | 78 | 80 | 78 | **81** |
| FAQ — 5 Q&As | 100 | 78 | 80 | 78 | 68 | 60 | 75 |
| Summary | 60 | 55 | 58 | 60 | 30 | 45 | 52 |

**Citability Coverage (blocks >70): 4/12 = 33%**
**Top passages:** Intro (83), Why Worth It/EPA (83), Liner Bags (81)
**Weakest:** Real-Life Use Cases (41) — emoji headers, no data, 1 sentence per section

**Remaining weak blocks fix:** The "Real-Life Use Cases," "Not Recommended," and "Pro Tips" sections are thin (1-2 sentences, no data). These are low-priority but each could gain +10-15 pts with 2 added sentences and 1 specific metric.

---

### Page 4: Standard Kitchen Trash Can Size — 70/100

| Section | Words | Answer | Self-Contain | Structure | Stats | Unique | Score |
|---------|-------|--------|-------------|-----------|-------|--------|-------|
| Intro paragraph | 55 | 88 | 90 | 80 | 85 | 60 | 84 |
| **Household-size table (FIX 7)** | 80 | 92 | 95 | 98 | 92 | 68 | **91** |
| Why Size Matters | 120 | 55 | 58 | 68 | 30 | 40 | 53 |
| Standard Sizes table | 80 | 75 | 82 | 92 | 72 | 55 | 76 |
| Factors to Consider | 180 | 62 | 65 | 72 | 35 | 42 | 59 |
| How to Measure | 90 | 65 | 68 | 72 | 40 | 45 | 61 |
| Modern Features | 80 | 60 | 62 | 70 | 35 | 42 | 57 |
| Expert Tips | 280 | 58 | 60 | 68 | 32 | 38 | 54 |
| Tips for Efficiency | 80 | 55 | 58 | 65 | 30 | 38 | 52 |
| FAQ — 4 Q&As | 120 | 72 | 78 | 72 | 58 | 48 | 69 |
| Buying Guide | 110 | 60 | 62 | 70 | 32 | 40 | 57 |
| Conclusion | 90 | 68 | 70 | 65 | 45 | 42 | 63 |

**Citability Coverage (blocks >70): 3/12 = 25%**
**Top passages:** Household-size table (91), Standard Sizes table (76), Intro (84)
**Drag:** Most middle sections are generic advice with no specific metrics — "Place bin near prep areas" scores low on stats and uniqueness.

---

### Page 5: FAQ Page — 71/100 *(was 32)*

| Section | Words | Answer | Self-Contain | Structure | Stats | Unique | Score |
|---------|-------|--------|-------------|-----------|-------|--------|-------|
| Logistics Q&As (8) | 280 | 55 | 75 | 70 | 45 | 30 | 57 |
| **Product Questions (5) — FIX 8** | 420 | 88 | 85 | 80 | 82 | 75 | **84** |

**Citability Coverage (blocks >70): 1/2 = 50%**
**Top passage:** Product Questions block (84/100) — now the 3rd highest-scoring page block on the site
**Gap:** FAQPage JSON-LD schema not yet added (+3-5 pts when done)

---

### Page 6: Homepage — 20/100

| Section | Words | Answer | Self-Contain | Structure | Stats | Unique | Score |
|---------|-------|--------|-------------|-----------|-------|--------|-------|
| Brand Identity (H1 only) | 5 | 5 | 5 | 15 | 0 | 10 | 7 |
| Trending Products (grid) | 80 | 10 | 25 | 40 | 25 | 30 | 24 |
| Scented Liners promo | 10 | 12 | 18 | 25 | 0 | 25 | 16 |
| Trays category | 5 | 5 | 5 | 20 | 0 | 10 | 8 |
| Newsletter | 10 | 0 | 5 | 15 | 0 | 5 | 5 |
| Contact Us | 30 | 50 | 85 | 55 | 45 | 75 | 62 |

**Citability Coverage: 0/6 = 0%**

---

## Section 5 — Strongest Passages Across Site (Live-Verified)

| # | Passage | Page | Score | Status |
|---|---------|------|-------|--------|
| 1 | About Us: founder + testing methodology | About Us | **91/100** | ✅ Live |
| 2 | Household-size table (4 cols × 4 rows) | Standard Size | **91/100** | ✅ Live |
| 3 | Sizing table with emptying frequency | Kitchen Guide | **91/100** | ✅ Live |
| 4 | FAQ Product Questions block (5 Q&As) | FAQ Page | **84/100** | ✅ Live (new) |
| 5 | Kitchen Guide FAQ — 5 Q&As | Kitchen Guide | **87/100** | ✅ Live |
| 6 | How We Test methodology | Kitchen Guide | **89/100** | ✅ Live |
| 7 | Lid type comparison table | Kitchen Guide | **85/100** | ✅ Live |
| 8 | Intro direct-answer paragraph | Dual Guide | **83/100** | ✅ Live |
| 9 | EPA 32.1% source-separation paragraph | Dual Guide | **83/100** | ✅ Live (fixed) |
| 10 | Liner Bags section | Dual Guide | **81/100** | ✅ Live (new) |
| 11 | Material comparison table | Kitchen Guide | **83/100** | ✅ Live |
| 12 | Dual vs Single comparison table | Dual Guide | 65/100 | ✅ Live (qualitative only) |

---

## Section 6 — All Remaining Fixes (Schema Only — Ready to Paste)

All content fixes are complete. Everything remaining is JSON-LD schema.

---

### FIX 1 — JSON-LD: Kitchen Guide *(highest priority)*
**Where:** Shopify Admin → Content → Blog Posts → Kitchen Trash Can Guide → HTML editor → paste before `</body>`
**Gain: +6 pts on page (84 → 90)**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "The Complete Guide to Choosing the Perfect Kitchen Trash Can",
      "description": "Choosing the right kitchen trash can comes down to four decisions: size (10–13 gallons for most households), lid type, material, and compartments.",
      "author": {"@type": "Organization", "name": "Happimess Editorial Team", "url": "https://happimess.com/pages/about-us"},
      "publisher": {"@type": "Organization", "name": "Happimess", "url": "https://happimess.com"},
      "datePublished": "2025-04-24",
      "dateModified": "2026-05-14",
      "mainEntityOfPage": {"@type": "WebPage", "@id": "https://happimess.com/blogs/news/the-guide-to-choosing-the-perfect-kitchen-trash-can"},
      "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["h2", "h3", "table"]}
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {"@type": "Question", "name": "What is the most common kitchen trash can size?", "acceptedAnswer": {"@type": "Answer", "text": "The most common kitchen trash can size in US households is 13 gallons. This size fits standard 13-gallon kitchen trash bags sold at all major retailers (Glad, Hefty, Great Value) and accommodates daily waste volume for 2–4 person households without requiring daily emptying."}},
        {"@type": "Question", "name": "How often should a kitchen trash can be emptied?", "acceptedAnswer": {"@type": "Answer", "text": "A 13-gallon can in a 2–4 person household cooking most meals at home should be emptied every 1–3 days. Wet food waste should be emptied within 24–48 hours regardless of fill level."}},
        {"@type": "Question", "name": "What is the best trash can for a small kitchen?", "acceptedAnswer": {"@type": "Answer", "text": "For small kitchens under 100 square feet, a 7–10 gallon step-open can with a slim profile (under 10 inches wide) provides adequate capacity without dominating floor space."}},
        {"@type": "Question", "name": "Is stainless steel worth the extra cost for a kitchen trash can?", "acceptedAnswer": {"@type": "Answer", "text": "For a primary kitchen can with daily family use, yes. Stainless steel does not absorb odors the way plastic does over 12–24 months. The additional cost ($40–$100 more) is recovered in a longer service life (5–10 years vs 2–5 years for plastic)."}},
        {"@type": "Question", "name": "What size trash bag fits a 13-gallon can?", "acceptedAnswer": {"@type": "Answer", "text": "Standard 13-gallon kitchen trash bags fit all 13-gallon trash cans — sold as 'kitchen' or 'tall kitchen' bags at any grocery, warehouse, or hardware store."}}
      ]
    }
  ]
}
</script>
```

---

### FIX 2 — JSON-LD: Organization + sameAs *(site-wide, one paste)*
**Where:** Shopify Admin → Online Store → Themes → Edit Code → `layout/theme.liquid` → inside `<head>`
**Gain: +3 pts composite across all pages**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Happimess",
  "url": "https://happimess.com",
  "description": "Happimess sells home organization, storage, and kitchen trash management products. Founded in New York City. Every product undergoes a minimum 30-day evaluation — pedal and sensor mechanisms tested for 500+ open/close cycles, liner compatibility verified with Glad, Hefty, and Simplehuman brands.",
  "foundingLocation": {"@type": "Place", "name": "New York City, NY, USA"},
  "sameAs": [
    "https://www.instagram.com/happimess_official/",
    "https://www.facebook.com/happimessofficial/",
    "https://www.linkedin.com/company/happimesshome/",
    "https://www.pinterest.com/happimess_/",
    "https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g",
    "https://www.tiktok.com/@happimess_official"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer support",
    "hoursAvailable": "Mo-Fr 09:00-17:00",
    "url": "https://happimess.com/pages/faqs",
    "email": "hello@happimess.com",
    "telephone": "+19172614961"
  }
}
</script>
```

---

### FIX 5 — JSON-LD: Dual Guide
**Where:** Blog Posts → Dual Guide → HTML editor → paste before `</body>`
**Gain: +3 pts on page (80 → 83)**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Best Dual Trash Can for Kitchen 2026: Guide to What Actually Works",
      "description": "The best dual-compartment trash can for most kitchens is a 50–60 liter model with a manual step-open pedal, soft-close lid, and removable inner buckets.",
      "author": {"@type": "Organization", "name": "Happimess Editorial Team", "url": "https://happimess.com/pages/about-us"},
      "publisher": {"@type": "Organization", "name": "Happimess", "url": "https://happimess.com"},
      "datePublished": "2026-04-22",
      "dateModified": "2026-05-28",
      "mainEntityOfPage": {"@type": "WebPage", "@id": "https://happimess.com/blogs/news/best-dual-trash-can-for-kitchen-2026-guide-what-actually-works"}
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {"@type": "Question", "name": "What size dual trash can is best for most homes?", "acceptedAnswer": {"@type": "Answer", "text": "Most homes benefit from a 50–60L dual trash can. Small kitchens: 30–40L. Most households: 40–60L. Large households: 60L+."}},
        {"@type": "Question", "name": "Are dual trash cans worth it?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, for households with mandatory recycling separation or those generating significant weekly recycling. A dual can eliminates a second standalone bin and reduces floor space use."}},
        {"@type": "Question", "name": "Do dual trash cans use standard bags?", "acceptedAnswer": {"@type": "Answer", "text": "Each compartment in a standard 50L dual can is approximately 25L (6.5 gallons). Standard 13-gallon bags are too large — use 4–8 gallon bags per compartment for proper fit."}},
        {"@type": "Question", "name": "Is pedal better than sensor for a dual trash can?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Pedal bins require no batteries, have no electronic components to fail, and last 5–10 years with daily use. Sensor mechanisms on dual cans are less reliable due to the two-compartment format."}},
        {"@type": "Question", "name": "How long should a dual trash can last?", "acceptedAnswer": {"@type": "Answer", "text": "A quality dual trash can with a well-engineered pedal mechanism lasts 3–5+ years. Happimess evaluates pedal mechanisms for 500+ open/close cycles per week during a 30-day evaluation before catalog inclusion."}}
      ]
    }
  ]
}
</script>
```

---

### FIX 6 — JSON-LD: Standard Kitchen Trash Can Size
**Where:** Blog Posts → Standard Kitchen Trash Can Size → HTML editor → paste before `</body>`
**Gain: +3 pts on page (70 → 73)**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Standard Kitchen Trash Can Size: Complete Sizing Guide",
      "description": "The standard kitchen trash can size in the US is 13 gallons. A 3–4 person household needs 10–13 gallons emptied every 1–3 days. Sizes range from 4 gallons to 21+ gallons.",
      "author": {"@type": "Organization", "name": "Happimess Editorial Team", "url": "https://happimess.com/pages/about-us"},
      "publisher": {"@type": "Organization", "name": "Happimess", "url": "https://happimess.com"},
      "datePublished": "2025-09-22",
      "dateModified": "2026-05-28",
      "mainEntityOfPage": {"@type": "WebPage", "@id": "https://happimess.com/blogs/news/standard-kitchen-trash-can-size"}
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {"@type": "Question", "name": "What is the best trash can size for a family of four?", "acceptedAnswer": {"@type": "Answer", "text": "A 10–13 gallon trash can works best for a family of four, emptied every 1–3 days. This size fits standard tall kitchen bags from all major US retailers."}},
        {"@type": "Question", "name": "How often should I empty a 10-gallon trash can?", "acceptedAnswer": {"@type": "Answer", "text": "For a family of four, empty every 2–3 days. Wet food waste (fish, meat scraps, cooked food) should be emptied within 24–48 hours regardless of fill level."}},
        {"@type": "Question", "name": "How high should a standard kitchen trash can be?", "acceptedAnswer": {"@type": "Answer", "text": "Most standard 13-gallon kitchen trash cans are 20–25 inches tall. Under-sink and compact models range from 12–18 inches. Large household cans (15–20+ gallons) stand 24–30 inches."}},
        {"@type": "Question", "name": "Are stainless steel bins better than plastic?", "acceptedAnswer": {"@type": "Answer", "text": "For primary kitchen use, yes. Stainless steel does not absorb odors over time the way plastic does after 12–18 months. Plastic is lighter and costs less, making it suitable for secondary rooms and lower-traffic spaces."}}
      ]
    }
  ]
}
</script>
```

---

### FIX 8 schema — FAQPage JSON-LD: FAQ Page
**Where:** Shopify Admin → Online Store → Pages → FAQs → HTML editor → paste at end of content
**Gain: +3 pts on page (71 → 74)**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What size kitchen trash can is right for a 3–4 person household?", "acceptedAnswer": {"@type": "Answer", "text": "A 10–13 gallon trash can is right for most 3–4 person households cooking at home 4–7 times per week. This size is emptied every 1–3 days and fits standard 13-gallon kitchen bags from any major retailer."}},
    {"@type": "Question", "name": "What is the difference between a step-open and a sensor trash can?", "acceptedAnswer": {"@type": "Answer", "text": "Step-open pedal cans require no batteries, have no electronic components to fail, and work in all lighting conditions. Sensor cans close after 3–5 seconds and suit users with mobility limitations. Pedal cans outperform sensor on reliability and long-term cost for most households."}},
    {"@type": "Question", "name": "How do I stop my kitchen trash can from smelling?", "acceptedAnswer": {"@type": "Answer", "text": "Use a can with a full-perimeter lid seal, empty wet food waste within 24–48 hours regardless of fill level, and ensure the liner bag is anchored at the rim. Stainless steel outlasts plastic on odor resistance because the non-porous surface does not absorb odors after 12–18 months of use."}},
    {"@type": "Question", "name": "Is stainless steel worth the extra cost for a kitchen trash can?", "acceptedAnswer": {"@type": "Answer", "text": "For a primary kitchen can with daily family use, yes. Stainless steel does not absorb odors like plastic does over 12–24 months. The $40–$100 upfront premium is recovered in a 5–10 year service life vs 2–5 years for plastic."}},
    {"@type": "Question", "name": "What trash bags fit Happimess trash cans?", "acceptedAnswer": {"@type": "Answer", "text": "Happimess 8-gallon step-open cans use standard 13-gallon kitchen bags. Glad ForceFlex 13-gallon, Hefty Ultra Strong 13-gallon, and Great Value 13-gallon all fit. Happimess scented drawstring liners are specifically sized and tested for these models."}},
    {"@type": "Question", "name": "When will my order ship?", "acceptedAnswer": {"@type": "Answer", "text": "In-stock orders ship within 1–2 business days (Monday–Friday). You will receive an email confirmation with tracking information when your order ships."}},
    {"@type": "Question", "name": "What is your return policy?", "acceptedAnswer": {"@type": "Answer", "text": "Returns accepted within 30 days. Pre-paid labels provided for 48 contiguous US states. A $10 return fee per item is deducted. Original packaging required. FINAL SALE and MADE TO ORDER items are not eligible."}},
    {"@type": "Question", "name": "Does Happimess ship internationally?", "acceptedAnswer": {"@type": "Answer", "text": "Happimess ships to the 48 contiguous United States only. Hawaii, Alaska, and international shipping are not currently available."}}
  ]
}
</script>
```

---

### BONUS A — Homepage Brand Identity Paragraph
**Where:** Shopify Admin → Online Store → Themes → Customize → Homepage → add Rich Text section near top
**Gain: +28 pts on homepage (20 → 48)**

```html
<p>Happimess is a New York-based home organization brand specializing in kitchen trash cans, storage furniture, and home organization accessories. Every product in the Happimess catalog is evaluated over a minimum 30-day period under real household conditions — including pedal and sensor mechanism testing (500+ open/close cycles), lid seal testing with food waste over 15 days, and liner compatibility testing with Glad, Hefty, and Simplehuman brands. Ships to the 48 contiguous US states.</p>
```

---

### BONUS B — Homepage FAQPage JSON-LD
**Where:** `layout/theme.liquid` → inside `<head>` with homepage conditional
**Gain: +5 pts on homepage**

```html
{% if request.page_type == 'index' %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What is Happimess?", "acceptedAnswer": {"@type": "Answer", "text": "Happimess is a New York-based home organization brand specializing in kitchen trash cans, storage furniture, and home organization accessories. Every product undergoes a minimum 30-day evaluation including pedal mechanism testing (500+ open/close cycles) and liner compatibility testing with Glad, Hefty, and Simplehuman brands."}},
    {"@type": "Question", "name": "What trash cans does Happimess sell?", "acceptedAnswer": {"@type": "Answer", "text": "Happimess sells step-open pedal trash cans, touchless sensor trash cans, and dual-compartment recycling trash cans. Sizes range from 4-gallon compact models to 13-gallon full-size kitchen cans. All step-open models include a soft-close lid and removable inner bucket."}},
    {"@type": "Question", "name": "Does Happimess ship internationally?", "acceptedAnswer": {"@type": "Answer", "text": "Happimess ships to the 48 contiguous United States only. Orders ship within 1–2 business days Monday–Friday. Hawaii, Alaska, and international shipping are not currently available."}}
  ]
}
</script>
{% endif %}
```

---

## Section 7 — Implementation Checklist (8 Remaining)

| # | Fix | Where | Time | Score Gain |
|---|-----|-------|------|-----------|
| 1 | **FIX 2** — Organization + sameAs → `theme.liquid` | theme.liquid `<head>` | 5 min | +3 composite |
| 2 | **FIX 1** — Article + FAQPage + Speakable → Kitchen Guide | Blog post HTML | 10 min | +6 on page |
| 3 | **FIX 8 schema** — FAQPage JSON-LD → FAQ page | Page HTML | 5 min | +3 on page |
| 4 | **FIX 5** — Article + FAQPage → Dual Guide | Blog post HTML | 5 min | +3 on page |
| 5 | **FIX 6** — Article + FAQPage → Standard Size | Blog post HTML | 5 min | +3 on page |
| 6 | **BONUS A** — Brand paragraph → Homepage | Theme Customize | 10 min | +28 on homepage |
| 7 | **BONUS B** — FAQPage JSON-LD → Homepage | theme.liquid conditional | 10 min | +5 on homepage |
| 8 | **BONUS C** — New "How to Stop Kitchen Trash from Smelling" article | New blog post | 2 hrs | +4 composite |

**All remaining fixes are schema or one new article — zero content rewrites needed.**

---

## Section 8 — Projected Final Scores

| Page | Current | After Schema Fixes | After New Articles |
|------|---------|-------------------|-------------------|
| Kitchen Trash Can Guide | 84/100 | **90/100** | 90/100 |
| About Us | 90/100 | **93/100** | 93/100 |
| Dual Trash Can Guide | 80/100 | **83/100** | 83/100 |
| Standard Size | 70/100 | **73/100** | 73/100 |
| FAQ Page | 71/100 | **74/100** | 74/100 |
| Homepage | 20/100 | **53/100** | 53/100 |
| **5-page composite** | **79/100** | **~84/100** | **~88/100** |

---

*Full 6-page live crawl completed: May 28, 2026 — Check 4*
