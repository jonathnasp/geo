# Day 01 — Implementation Details

---

## Fix 1: Deploy spec-compliant llms.txt

### Files to deploy
- `geo(180526)/llms.txt` → serve at `https://happimess.com/llms.txt`
- `geo(180526)/llms-full.txt` → serve at `https://happimess.com/llms-full.txt`

### Deployment method (Shopify)

**Method A — Shopify Files (CDN path, not root path):**
1. Shopify Admin → Content → Files → Upload file
2. Upload `llms.txt`
3. Note the CDN URL (e.g., `https://cdn.shopify.com/s/files/...`)
4. This does NOT serve at `/llms.txt` — the CDN path is different

**Method B — Shopify Page redirect (serves at correct path):**
1. Create a new page with handle `llms-txt` in Shopify Admin
2. In Online Store → Navigation → URL Redirects, add:
   - From: `/llms.txt` → To: `/pages/llms-txt`
3. Set the page content to the full llms.txt text content

**Method C — Custom Liquid route (preferred, requires developer):**
Create `templates/page.llms-txt.liquid` with a plain-text content type that outputs the llms.txt content directly.

### Verification
```
curl -s https://happimess.com/llms.txt | head -5
# Expected first line: "# Happimess"
```

### Why this matters
AI models (ChatGPT, Claude, Perplexity, Gemini) fetch `/llms.txt` as their first step when encountering a new site. The current file is a commerce-agent API document. The spec requires: `# H1 title`, `> description blockquote`, `## Section headers`, `- [Title](URL): Description` link lists. None of these are present in the current file.

### Rollback
Re-upload the original `llms.txt` from the existing Shopify file. The file has no external dependencies — replacing it is instant.

---

## Fix 2: FAQ Page Title

### Change
- **Location:** Shopify Admin → Online Store → Pages → FAQs → SEO section
- **Field:** Page title
- **Before:** `Faqs`
- **After:** `Frequently Asked Questions | Happimess`

### Meta description (add if blank)
```
Find answers to common questions about Happimess orders, shipping, returns, and product policies. Ships to 48 contiguous US states.
```

### Why this matters
The page title `"Faqs"` contains zero search keywords and zero brand name. The page answers questions that AI models regularly extract for direct answers (shipping times, return policy, order modification). A weak title reduces the page's relevance score for every AI and search crawler. The fix is instantaneous and has no risk.

### Verification
```
curl -s https://happimess.com/pages/faqs | grep -o '<title>[^<]*'
# Expected: <title>Frequently Asked Questions | Happimess
```

### Rollback
Revert the Page title field in Shopify Admin to the original value. No theme files touched.

---

## Fix 3: Author Name Casing

### Change
- **Location:** Shopify Admin → Settings → Users and permissions
- **Account:** Sandip Hadiya (email: sandip@eyely.com)
- **Field:** Display name
- **Before:** `sandip hadiya`
- **After:** `Sandip Hadiya`

### Why this matters
The author name propagates to every blog article's JSON-LD `Person` schema:
```json
"author": {
  "@type": "Person",
  "@id": "https://happimess.com/pages/meet-our-authors#sandip-hadiya",
  "name": "sandip hadiya"  ← this is wrong
}
```
AI models performing entity resolution on author names attempt to match them to known entities (LinkedIn, Wikidata). Lowercase names fail name-matching algorithms. This fix propagates to all blog articles automatically on next page render.

### Verification
View source on any blog article authored by Sandip → search for `"name":` in the JSON-LD block → confirm `"Sandip Hadiya"` (capital S, capital H).

### Rollback
Revert display name in Shopify Admin. One-field change.

---

## Fix 4: Blog Listing Publication Dates

### File to edit
`sections/main-blog.liquid` (most themes) or `templates/blog.liquid`

Find the article loop — it will look like:
```liquid
{% for article in blog.articles %}
```

### Before (typical pattern)
```liquid
{% for article in blog.articles %}
  <div class="article-card">
    <h2><a href="{{ article.url }}">{{ article.title }}</a></h2>
    <p>{{ article.excerpt_or_content | strip_html | truncatewords: 30 }}</p>
  </div>
{% endfor %}
```

### After (add date line)
```liquid
{% for article in blog.articles %}
  <div class="article-card">
    <h2><a href="{{ article.url }}">{{ article.title }}</a></h2>
    <time class="article-date" datetime="{{ article.published_at | date: '%Y-%m-%dT%H:%M:%SZ' }}">
      {{ article.published_at | date: "%B %d, %Y" }}
    </time>
    <p>{{ article.excerpt_or_content | strip_html | truncatewords: 30 }}</p>
  </div>
{% endfor %}
```

### CSS note
If dates appear unstyled, add minimal CSS in the theme's `base.css` or `custom.css`:
```css
.article-date {
  display: block;
  font-size: 0.85em;
  color: #666;
  margin: 0.25rem 0;
}
```

### Why this matters
Perplexity AI heavily weights content freshness. The blog listing page is the first page Perplexity crawls for the blog. Without visible dates, Perplexity cannot assess how current the content catalog is. The `datetime` attribute in the `<time>` element provides machine-readable date data for crawlers even if users don't see it.

### Verification
Visit `https://happimess.com/blogs/news` → confirm dates like "April 22, 2026" appear under article titles.

### Rollback
Remove the `<time>...</time>` block from the template. The rest of the article card is unchanged.

---

## Fix 5: robots.txt Allow Override Ordering

### Current state (problematic)
```
Disallow: /policies/
Allow: /policies/refund-policy
Allow: /policies/privacy-policy
Allow: /policies/terms-of-service
```

### Fixed state (correct order)
```
Allow: /policies/refund-policy
Allow: /policies/privacy-policy
Allow: /policies/terms-of-service
Disallow: /policies/
```

### Per RFC 9309 specification
When multiple rules match a URL, crawlers should use the most specific rule. However, many crawlers (especially lesser-known bots) implement a first-match algorithm. With `Disallow` before `Allow`, first-match crawlers block all `/policies/` URLs including the three explicitly allowed ones.

### How to edit robots.txt in Shopify
Shopify stores with a custom `robots.txt.liquid` file:
1. Shopify Admin → Online Store → Themes → Edit Code
2. Find `templates/robots.txt.liquid`
3. Locate the `/policies/` section and reorder as shown above

Shopify stores using default robots.txt (no custom template):
1. You must create a `robots.txt.liquid` to override Shopify's default
2. Or use a Shopify SEO app (Plug In SEO, SEO Manager) that provides a robots.txt editor

### Default Shopify robots.txt structure
If no custom robots.txt.liquid exists, create it by duplicating from Shopify's default and applying the change.

### Verification
```
curl -s https://happimess.com/robots.txt | grep -A 5 "policies"
# Allow lines must appear before Disallow: /policies/
```

### Rollback
Revert to previous rule order in `robots.txt.liquid`. No downstream effects — this is a single file change.
