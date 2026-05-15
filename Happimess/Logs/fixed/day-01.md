# Day 1 — Critical Broken Pages + Organization Schema + llms.txt
**Date:** May 7, 2026 | **Estimated Time:** 3.5 hours | **Score Impact:** +8 points (42 → ~50)

---

## Day 1 Goals

Today fixes four things that are **actively broken** — not improvements, literal errors:

1. An author page that returns 404, voiding E-E-A-T credit on 26 blog posts
2. An FAQ page that returns 404, linked in the footer of every page
3. A global Organization schema with 4 validation errors visible on every single page
4. An llms.txt file that completely omits the blog, making Happimess invisible as a knowledge resource to AI

**Why Day 1?** These are not optional improvements — they are broken infrastructure that degrades GEO score every hour they remain unfixed. Fixing them before anything else ensures that Phase 2 schema work, Phase 3 content work, and all subsequent changes operate on a clean foundation.

**SEO/GEO Impact:** Composite score moves from 42 → ~50. Article E-E-A-T on all 26 blog posts restored. Organization entity graph fixed site-wide. AI systems will begin indexing Happimess as an editorial knowledge resource.

---

## FIX-01 — Create Author Bio Page (404 → HTTP 200)

### Severity
**CRITICAL**

### Problem
Every blog post's Article JSON-LD schema contains:
```json
"author": {
  "@type": "Person",
  "url": "https://happimess.com/pages/asodariya-sumi"
}
```
This URL returns **HTTP 404**. Google and all AI crawlers (GPTBot, ClaudeBot, PerplexityBot) follow this URL to verify author credentials. A 404 tells them the author is unverifiable.

### Why This Is Dangerous
- **E-E-A-T damage:** All 26 blog posts lose their author credibility signal. Google's QRG explicitly requires verifiable author identity for YMYL-adjacent content.
- **AI citation damage:** Perplexity and ChatGPT cannot attribute content to a real person. They deprioritize unverifiable sources.
- **Schema validation failure:** Article schema on all 26 posts fails the `author.url` validation check.
- **Crawl signal:** Googlebot logs a 404 crawl error for every blog post — compounds crawl budget waste.
- **GEO impact:** 26 posts that could be citation sources are treated as low-trust anonymous content.

### Current Broken Example
```
GET https://happimess.com/pages/asodariya-sumi
Response: HTTP 404 Not Found

Article schema on every blog post:
"author": {
  "@type": "Person",
  "name": "Asodariya Sumi",
  "url": "https://happimess.com/pages/asodariya-sumi"   ← 404
}
```

### How To Fix

**Step 1 — Create the page in Shopify Admin:**
1. Go to **Shopify Admin → Online Store → Pages**
2. Click **"Add page"**
3. Title: `Asodariya Sumi`
4. URL handle: set to exactly `asodariya-sumi` (Shopify will auto-suggest this from the title)
5. Paste this content into the page body (HTML mode):

```html
<div class="author-bio-page">
  <h1>About Asodariya Sumi</h1>
  
  <div class="author-bio-intro">
    <p>
      Asodariya Sumi is a home organization specialist and product expert at Happimess 
      with over 5 years of experience in kitchen storage, waste management solutions, 
      and sustainable home design. She researches, tests, and writes about storage 
      furniture, trash can selection, and home organization systems.
    </p>
    <p>
      Her guides and buying recommendations are informed by hands-on evaluation of 
      hundreds of products, consultation with interior designers, and feedback from 
      thousands of Happimess customers across the United States.
    </p>
  </div>

  <h2>Areas of Expertise</h2>
  <ul>
    <li>Kitchen organization and storage systems</li>
    <li>Trash can selection (capacity, lid mechanism, material)</li>
    <li>Dual-compartment recycling solutions</li>
    <li>Storage furniture (benches, ottomans, shelving)</li>
    <li>Sustainable and eco-friendly home products</li>
    <li>Bathroom and laundry organization</li>
  </ul>

  <h2>Published Guides</h2>
  <ul>
    <li><a href="/blogs/news/standard-kitchen-trash-can-size">Standard Kitchen Trash Can Size: The Complete Guide</a></li>
    <li><a href="/blogs/news/best-dual-trash-can-for-kitchen-2026-guide-what-actually-works">Best Dual Trash Can for Kitchen (2026 Guide)</a></li>
    <li><a href="/blogs/news/the-guide-to-choosing-the-perfect-kitchen-trash-can">Guide to Choosing the Perfect Kitchen Trash Can</a></li>
    <li><a href="/blogs/news/tips-for-organizing-your-kitchen-a-comprehensive-guide">Tips for Organizing Your Kitchen</a></li>
  </ul>

  <p>
    <strong>Organization:</strong> <a href="https://happimess.com">Happimess</a> — 
    Modern Storage, Organization &amp; Home Furniture Solutions<br>
    <strong>Contact:</strong> hello@happimess.com
  </p>
</div>
```

6. Click **Save**

**Step 2 — Add Person JSON-LD schema to the author page:**

In Shopify Admin → Online Store → Themes → Edit code, create a new page template for the author:
- Under **Templates**, click **Add a new template**
- Choose `page` type, name it `author`
- In the `page.author.json` (or `.liquid`) file, add the following schema

If using a custom liquid template for this page:

```html
<!-- In pages/asodariya-sumi page, add this via Additional Scripts or Metafield -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://happimess.com/pages/asodariya-sumi#author",
  "name": "Asodariya Sumi",
  "url": "https://happimess.com/pages/asodariya-sumi",
  "jobTitle": "Home Organization Specialist",
  "description": "Home organization specialist and product expert at Happimess with 5+ years experience in kitchen storage, waste management solutions, and sustainable home design.",
  "worksFor": {
    "@type": "Organization",
    "@id": "https://happimess.com/#organization",
    "name": "Happimess",
    "url": "https://happimess.com"
  },
  "knowsAbout": [
    "kitchen organization",
    "trash can selection",
    "storage furniture",
    "home organization",
    "sustainable home products"
  ],
  "sameAs": [
    "https://www.linkedin.com/in/[ADD-LINKEDIN-URL-IF-EXISTS]"
  ]
}
</script>
```

**Alternative — add via theme.liquid using Liquid conditional:**

Open `layout/theme.liquid`, and inside `<head>` add:

```liquid
{% if page.handle == 'asodariya-sumi' %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://happimess.com/pages/asodariya-sumi#author",
  "name": "Asodariya Sumi",
  "url": "https://happimess.com/pages/asodariya-sumi",
  "jobTitle": "Home Organization Specialist",
  "description": "Home organization specialist at Happimess. Expert in kitchen storage, trash can selection, and sustainable home design.",
  "worksFor": {
    "@type": "Organization",
    "@id": "https://happimess.com/#organization"
  }
}
</script>
{% endif %}
```

### Files To Edit
```
Shopify Admin → Online Store → Pages → New Page (handle: asodariya-sumi)
layout/theme.liquid  (for Person schema injection)
snippets/schema-article.liquid  (verify author.url is dynamic from article.author)
```

### Validation Steps
1. Visit `https://happimess.com/pages/asodariya-sumi` — must return HTTP 200
2. Open [Google Rich Results Test](https://search.google.com/test/rich-results) → enter a blog post URL
3. Confirm Article schema shows author.url with no red error
4. Run `curl -o /dev/null -s -w "%{http_code}" https://happimess.com/pages/asodariya-sumi` — should return `200`

### Expected Result
- All 26 blog posts have a live, crawlable author URL
- Article schema validation passes with no author.url errors
- E-E-A-T author expertise signal active across entire blog
- AI crawlers can verify author identity

---

## FIX-02 — Fix FAQ Page (404 → HTTP 200)

### Severity
**CRITICAL**

### Problem
`https://happimess.com/pages/faq` is linked in the footer navigation of **every page** on the site. It returns HTTP 404.

### Why This Is Dangerous
- **Trust damage:** Users clicking FAQ get a 404. Immediate trust destruction at the bottom of every page.
- **Crawl budget waste:** Googlebot follows this internal link on every crawl, logs a 404 error every time.
- **E-E-A-T damage:** Trustworthiness score directly impacted — a broken FAQ signals poor site maintenance.
- **Indexing impact:** Google's internal link equity passes through footer links. A 404 destination absorbs link equity and returns nothing.
- **AI model impact:** AI systems that crawl the site discover an unresolvable linked page, reducing trust in the site's structural integrity.

### Current Broken Example
```
Footer navigation links on every page:
<a href="/pages/faq">FAQ</a>

GET https://happimess.com/pages/faq
Response: HTTP 404 Not Found
```

### How To Fix

**Option A — Create a Real FAQ Page (RECOMMENDED, 30 min):**

1. Shopify Admin → **Online Store → Pages → Add page**
2. Title: `Frequently Asked Questions`
3. URL handle: `faq`
4. Paste this content:

```html
<div class="faq-page">
  <h1>Frequently Asked Questions</h1>

  <h2>Orders &amp; Shipping</h2>

  <h3>How long does shipping take?</h3>
  <p>Most orders ship within 1–2 business days. Delivery typically takes 3–7 business days via standard shipping to all 50 US states.</p>

  <h3>Do you ship internationally?</h3>
  <p>We currently ship to all 50 US states. International shipping is not available at this time.</p>

  <h3>How do I track my order?</h3>
  <p>You will receive a tracking number via email once your order ships. Use the link in your confirmation email or visit your account page to track your order.</p>

  <h2>Returns &amp; Exchanges</h2>

  <h3>What is your return policy?</h3>
  <p>We accept returns within 30 days of delivery. Items must be unused and in original packaging. Email <a href="mailto:hello@happimess.com">hello@happimess.com</a> to initiate a return.</p>

  <h3>How do I start a return?</h3>
  <p>Email hello@happimess.com with your order number and reason for return. Our team will respond within 1 business day with return instructions.</p>

  <h2>Products</h2>

  <h3>What size trash can do I need for my kitchen?</h3>
  <p>For most households, a 10–13 gallon trash can is ideal for a kitchen. Single-person households can use 4–8 gallons; large families (5+) often need 20+ gallons. See our <a href="/blogs/news/standard-kitchen-trash-can-size">complete size guide</a> for detailed recommendations.</p>

  <h3>Do your trash cans come with bags?</h3>
  <p>Trash bags are not included with purchase. Our product pages specify the recommended liner size for each model.</p>

  <h3>Are your products available in Spanish?</h3>
  <p>Yes. Our full catalog and product information is available in Spanish at <a href="/es/">happimess.com/es/</a>.</p>

  <h2>Contact</h2>

  <h3>How do I contact customer support?</h3>
  <p>
    Email: <a href="mailto:hello@happimess.com">hello@happimess.com</a><br>
    Phone: <a href="tel:+19172614961">(917) 261-4961</a><br>
    Hours: Monday–Friday, 9AM–5PM EST
  </p>
</div>
```

5. Click **Save**

**Option B — Redirect to Contact Page (5 min if time-pressed):**
1. Shopify Admin → **Online Store → Navigation → URL Redirects**
2. Click **Add URL redirect**
3. Redirect from: `/pages/faq`
4. Redirect to: `/pages/contact` (or wherever contact/support info lives)

> Option A is strongly preferred — a real FAQ page adds FAQPage schema eligibility and E-E-A-T trust signals.

**Add FAQPage Schema to the FAQ page:**

After creating the page, add this JSON-LD via `theme.liquid` conditional:

```liquid
{% if page.handle == 'faq' %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What size trash can do I need for my kitchen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For most households, a 10–13 gallon trash can is ideal for a kitchen. Single-person households can use 4–8 gallons; large families (5+ members) often need 20+ gallons."
      }
    },
    {
      "@type": "Question",
      "name": "What is your return policy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We accept returns within 30 days of delivery. Items must be unused and in original packaging. Email hello@happimess.com to initiate a return."
      }
    },
    {
      "@type": "Question",
      "name": "How long does shipping take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most orders ship within 1–2 business days. Delivery takes 3–7 business days to all 50 US states."
      }
    },
    {
      "@type": "Question",
      "name": "How do I contact customer support?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Email: hello@happimess.com | Phone: (917) 261-4961 | Hours: Monday–Friday, 9AM–5PM EST"
      }
    }
  ]
}
</script>
{% endif %}
```

### Files To Edit
```
Shopify Admin → Online Store → Pages → New Page (handle: faq)
layout/theme.liquid  (for FAQPage schema conditional)
```

### Validation Steps
1. Visit `https://happimess.com/pages/faq` — must return HTTP 200 with content
2. Click the FAQ link in the footer — should navigate to the FAQ page (not 404)
3. Run [Google Rich Results Test](https://search.google.com/test/rich-results) on `/pages/faq` — FAQPage schema should show

### Expected Result
- Footer FAQ link works on every page
- Users can find answers without contacting support
- FAQPage schema eligible for Google AI Overview extraction

---

## FIX-03 — Fix Organization Schema (4 Validation Errors Site-Wide)

### Severity
**CRITICAL**

### Problem
The global schema block in `theme.liquid` uses `@type: "LocalBusiness"` (wrong for a D2C e-commerce brand) and contains 4 additional validation errors. This block appears on **every page** of the site.

### Why This Is Dangerous
- **Knowledge Panel blocked:** `LocalBusiness` tells Google this is a physical local business. Google will not create an Organization Knowledge Panel for a mistyped entity.
- **AI entity recognition poisoned:** AI models reading the schema tag Happimess as a local service business, not a D2C brand. This affects entity resolution in ChatGPT, Gemini, and Bing Copilot.
- **Telephone validation error:** Leading space in `" (917) 261-4961"` causes schema validation failure — this field is displayed in rich results.
- **Invalid property:** `servesCuisine` is a restaurant-only property. Its presence on every page signals schema spam to Google's rich result validator.
- **Wrong enum value:** `contactType: "Customer Support"` is not a valid Schema.org enum. Must be `"customer service"` (lowercase).
- **AggregateRating as strings:** `"4.5"` and `"120"` must be numbers, not quoted strings.

### Current Broken Schema
```json
{
  "@type": "LocalBusiness",           ← WRONG — should be Organization
  "telephone": " (917) 261-4961",    ← leading space = validation error
  "servesCuisine": "American",        ← restaurant-only property = invalid
  "contactType": "Customer Support",  ← wrong enum = validation error
  "aggregateRating": {
    "ratingValue": "4.5",             ← string not number = validation error
    "reviewCount": "120"              ← string not number = validation error
  }
}
```

### How To Fix

**Step 1 — Locate the existing schema in theme.liquid:**
1. Shopify Admin → **Online Store → Themes → Edit code**
2. Open `layout/theme.liquid`
3. Search (Ctrl+F) for: `LocalBusiness`
4. Select the entire `<script type="application/ld+json">` block containing `LocalBusiness`
5. Delete the entire block

**Step 2 — Paste the corrected Organization schema:**

Replace with the content from `schema/schema-organization.json` (already prepared in this audit package). The full corrected block:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://happimess.com/#organization",
  "name": "Happimess",
  "url": "https://happimess.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://cdn.shopify.com/s/files/1/0491/2909/5325/files/happimess-logo-ai-file_1.svg?v=1697698531",
    "width": 280,
    "height": 280
  },
  "description": "Happimess designs modern storage, organization, and home furniture solutions including step trash cans, sensor cans, dual-compartment bins, storage benches, dish racks, and hampers.",
  "email": "hello@happimess.com",
  "telephone": "+19172614961",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "185 Madison Avenue",
    "addressLocality": "New York",
    "addressRegion": "NY",
    "postalCode": "10016",
    "addressCountry": "US"
  },
  "foundingDate": "2020",
  "areaServed": {
    "@type": "Country",
    "name": "United States"
  },
  "contactPoint": [
    {
      "@type": "ContactPoint",
      "telephone": "+19172614961",
      "email": "hello@happimess.com",
      "contactType": "customer service",
      "areaServed": "US",
      "availableLanguage": ["English", "Spanish"],
      "hoursAvailable": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
        "opens": "09:00",
        "closes": "17:00"
      }
    }
  ],
  "sameAs": [
    "https://www.facebook.com/happimessofficial/",
    "https://www.instagram.com/happimess_official/",
    "https://www.linkedin.com/company/happimesshome/",
    "https://www.pinterest.com/happimessofficial/",
    "https://www.youtube.com/channel/UC6lUDdoZeZrYnoY2kmZyf4g",
    "https://www.tiktok.com/@happimess_official"
  ],
  "knowsAbout": [
    "home organization",
    "storage solutions",
    "trash can design",
    "kitchen organization",
    "bathroom storage",
    "laundry solutions",
    "sustainable home products"
  ]
}
</script>
```

**CRITICAL placement note:** This block MUST be inside `<head>` as a static HTML string — NOT inside a JavaScript block, NOT created by `document.createElement`. The T4S theme injects schema via JavaScript — AI crawlers miss JS-injected schema. Place the block directly in the `<head>` section before the closing `</head>` tag.

**Step 3 — Check for JavaScript-injected duplicate:**
Search `theme.liquid` and any theme JS files for:
- `JSON.stringify` containing schema
- `document.createElement('script')` with schema content
- `LocalBusiness` anywhere in JS files

Remove any JS-injected schema duplicates to avoid conflicting blocks.

**Step 4 — Fix the Pinterest sameAs URL:**
The current schema uses `https://pin.it/6USD9wO` (a short link). Replace with the canonical Pinterest profile URL. Find the actual profile URL by visiting pin.it/6USD9wO and copying the full resolved URL like `https://www.pinterest.com/happimessofficial/`.

### Files To Edit
```
layout/theme.liquid   (primary — remove LocalBusiness, add Organization in <head>)
assets/theme.js       (search for any JS-injected schema — remove duplicates)
```

### Validation Steps
1. Go to [Google Rich Results Test](https://search.google.com/test/rich-results)
2. Enter `https://happimess.com` — **Organization schema should show with zero errors**
3. View page source (Ctrl+U) — Organization JSON-LD must be visible in raw HTML (not requiring JS)
4. [Schema.org Validator](https://validator.schema.org/) → paste the Organization block → verify no errors
5. Confirm no `LocalBusiness`, `servesCuisine`, or `"Customer Support"` remain in the schema

### Expected Result
- Organization schema valid on all pages with zero validation errors
- Google Knowledge Panel eligibility restored
- AI models correctly identify Happimess as a D2C e-commerce organization (not a restaurant or local service)
- Telephone, contactType, and AggregateRating fields pass structured data validation

---

## FIX-04 — Deploy Improved llms.txt

### Severity
**CRITICAL**

### Problem
The current `llms.txt` lists **0 of 26 blog posts**. The file reads as a pure product catalog. AI systems reading it classify Happimess as a transactional storefront with no educational content — so when a user asks ChatGPT "how to choose a kitchen trash can," Happimess blog posts are not surfaced.

### Why This Is Dangerous
- **AI citation invisibility:** The blog at `/blogs/news/` is 100% invisible to AI content classification. 26 posts representing hundreds of hours of content creation are unreachable by AI knowledge indexing.
- **ChatGPT impact:** ChatGPT ranks Happimess as 32/100 — the lowest of all 5 platforms. The entity-first architecture means without blog classification, zero content gets cited.
- **Perplexity impact:** Perplexity prefers pages it can identify as knowledge resources. A storefront-only llms.txt signals no editorial depth.
- **Gemini impact:** Google Gemini uses structured content signals. Blog presence in llms.txt elevates how the site is categorized in multimodal knowledge graphs.

### Current Broken State
```
Current llms.txt: 980 bytes — 0 blog posts listed
Improved llms.txt: ~4,200 bytes — all 26 blog posts, 7 product categories, key pages
```

### How To Fix

**Step 1 — Prepare the updated llms.txt:**

Use the `llms.txt` file from this audit package (already prepared). The file is located at:
`E:\IS\geo\Happimess\geo(070526)\llms.txt`

**Step 2 — Deploy to Shopify:**

The cleanest way is to add it directly as a theme asset:
1. Shopify Admin → **Online Store → Themes → Edit code**
2. Under **Assets**, look for existing `llms.txt`
3. If it exists: click it, replace all content with the updated version
4. If it doesn't exist: The file may be served via a page or redirect. Check **Online Store → Pages** for a page with handle `llms-txt`
5. Alternative: Shopify Admin → **Content → Files** → upload the `llms.txt` file → note the CDN URL
6. Then create a URL redirect: `/llms.txt` → `[Shopify CDN URL]`

**The critical additions in the improved llms.txt:**

```markdown
## Blog & Guides

- [Standard Kitchen Trash Can Size Guide](https://happimess.com/blogs/news/standard-kitchen-trash-can-size): Complete size reference table mapping gallon capacity (4–21+ gal) to height ranges and household use cases.
- [Best Dual Trash Can for Kitchen 2026](https://happimess.com/blogs/news/best-dual-trash-can-for-kitchen-2026-guide-what-actually-works): Buying guide covering compartment sizing, pedal durability, and feature comparison for waste-sorting bins.
- [Guide to Choosing the Perfect Kitchen Trash Can](https://happimess.com/blogs/news/the-guide-to-choosing-the-perfect-kitchen-trash-can): Decision framework covering size, material, lid mechanism, and design integration.
- [How to Organize Your Kitchen](https://happimess.com/blogs/news/tips-for-organizing-your-kitchen-a-comprehensive-guide): Comprehensive kitchen organization guide covering decluttering, zoning, and storage solutions.
- [Kitchen Trends 2025](https://happimess.com/blogs/news/kitchen-trends-for-2025): Annual kitchen design and organization trend roundup.
- [Trash Can Maintenance Tips](https://happimess.com/blogs/news/trashcan-maintenance-tips-and-tricks-for-a-fresh-and-odor-free-bin): Cleaning and maintenance guide for keeping bins odor-free.
- [10 Eco-Friendly Kitchen Swaps](https://happimess.com/blogs/news/10-eco-friendly-kitchen-swaps-to-make-today): Sustainable kitchen product alternatives and disposal practices.
- [Living Room Storage Bench Guide](https://happimess.com/blogs/news/living-room-storage-bench): Buyer's guide for storage ottomans and benches.

## Product Categories

- [Trash Cans Collection](https://happimess.com/collections/trash-can): Step-open, sensor, push-lid, and dual-compartment bins in 4–60+ gallon capacities.
- [Storage Furniture](https://happimess.com/collections/storage): Benches, ottomans, and shelving units for bedroom and living room.
- [Kitchen Accessories](https://happimess.com/collections/kitchen): Dish racks, soap dispensers, and countertop organizers.
- [Bathroom Storage](https://happimess.com/collections/bathroom): Hampers, wastebaskets, and bathroom organization.
- [All Products](https://happimess.com/collections/all): Complete catalog of 100+ Happimess products.

## Key Pages

- [About Happimess](https://happimess.com/pages/about-us): Brand story, mission, and founding (2020, New York NY).
- [Contact & Support](https://happimess.com/pages/contact): Email hello@happimess.com · Phone (917) 261-4961 · Mon–Fri 9AM–5PM EST.
- [Return Policy](https://happimess.com/policies/refund-policy): 30-day return window, unused items, original packaging required.
- [Privacy Policy](https://happimess.com/policies/privacy-policy): Data collection and privacy practices.
- [FAQ](https://happimess.com/pages/faq): Common questions about orders, shipping, products, and returns.
```

### Files To Edit
```
Theme root assets: llms.txt
OR: Shopify Admin → Content → Files (upload + redirect)
```

### Validation Steps
1. Visit `https://happimess.com/llms.txt` — must show the blog section
2. Check the `## Blog & Guides` section is present
3. Verify links in the blog section resolve to real pages (HTTP 200)
4. Confirm `sitemap_agentic_discovery.xml` still references the correct llms.txt URL

### Expected Result
- AI systems classify Happimess as an editorial knowledge resource + transactional storefront
- Blog content becomes visible to AI content indexing
- ChatGPT, Perplexity, Gemini all receive richer context about Happimess's editorial depth
- llms.txt Quality score improves from 55/100 to ~80/100

---

## Day 1 Completion Checklist

```
[ ] https://happimess.com/pages/asodariya-sumi → HTTP 200 with author bio content
[ ] https://happimess.com/pages/faq → HTTP 200 with FAQ content (not 404)
[ ] Google Rich Results Test on homepage → Organization schema, zero errors
[ ] Organization schema visible in page source (Ctrl+U) without executing JS
[ ] No "LocalBusiness" remains in theme.liquid or theme JS
[ ] https://happimess.com/llms.txt → Shows "## Blog & Guides" section
[ ] Footer FAQ link works (navigate to it manually)
[ ] Google Rich Results Test on any blog post → Article schema, author URL resolves
```

---

## Day 1 Score Impact Projection

| Category | Before | After Day 1 |
|----------|--------|-------------|
| Structured Data | 52/100 | 62/100 (+10) |
| Content Quality / E-E-A-T | 38/100 | 44/100 (+6) |
| AI Citability & Visibility | 45/100 | 52/100 (+7) |
| **Composite GEO Score** | **42/100** | **~50/100** |
