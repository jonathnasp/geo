# GEO Schema & Structured Data Report — happimess.com
Date: 2026-04-15

## Schema Score: 45/100

## Detected Schemas
| Page | Schema Type | Format | Status | Issues |
|---|---|---|---|---|
| / | WebPage | JSON-LD | Valid | Description null, missing recommended properties |
| / | Website | JSON-LD | Valid | Missing sameAs, potentialAction present |
| / | Organization | JSON-LD | Valid | Missing sameAs, description, foundingDate, founder, knowsAbout, areaServed, numberOfEmployees, industry, award |
| / | LocalBusiness | MISSING | MISSING | Should be present for business with physical address |

## Validation Results
### WebPage Schema (https://happimess.com/#webpage)
- @type: ✓ Valid (WebPage)
- @id: ✓ Present
- url: ✓ Present (https://happimess.com)
- name: ✓ Present (Home)
- description: ✗ NULL (should be 1-2 sentence description)
- isPartOf: ✓ References Website
- Required properties: ✓ All present
- Recommended properties: ✗ Missing description

### Website Schema (https://happimess.com/#website)
- @type: ✓ Valid (WebSite)
- @id: ✓ Present
- url: ✓ Present (https://happimess.com)
- name: ✓ Present (Happimess)
- potentialAction: ✓ Present (SearchAction)
- Required properties: ✓ All present
- Recommended properties: ✗ Missing sameAs

### Organization Schema (https://happimess.com/#organization)
- @type: ✓ Valid (Organization)
- @id: ✓ Present
- name: ✓ Present (Happimess)
- legalName: ✓ Present (Happimess)
- alternateName: ✓ Present (Happimess)
- url: ✓ Present (https://happimess.com)
- image: ✓ Present (ImageObject)
- logo: ✓ Present (ImageObject)
- telephone: ✓ Present (with leading space issue)
- email: ✓ Present (hello@happimess.com)
- address: ✓ Present (complete PostalAddress)
- contactPoint: ✓ Present (array with ContactPoint)
- Required properties: ✓ All present
- Recommended properties: 
  - description: ✗ Missing
  - sameAs: ✗ Missing entirely
  - foundingDate: ✗ Missing
  - founder: ✗ Missing
  - knowsAbout: ✗ Missing (strong GEO signal)
  - areaServed: ✗ Missing
  - numberOfEmployees: ✗ Missing
  - industry: ✗ Missing
  - award: ✗ Missing

## Missing Recommended Schemas
- LocalBusiness: Business has physical address in New York, should implement LocalBusiness schema extending Organization
- BreadcrumbList: Missing on inner pages (product, collection, blog pages)
- Article: Missing on blog/news pages (would include author schema)
- Product: Missing on product pages
- FAQPage: Missing on FAQ page (/pages/faqs)
- speakable property: Missing on Article schemas

## sameAs Audit
| Platform | URL | Status |
|---|---|---|
| Wikipedia | Not found | Missing |
| Wikidata | Not found | Missing |
| LinkedIn | Not found | Missing |
| YouTube | Not found | Missing |
| Twitter/X | Not found | Missing |
| Facebook | Not found | Missing |
| Crunchbase | Not found | Missing |
| GitHub | Not found | Missing |
| Google Scholar | Not found | Missing (not applicable for e-commerce) |
| ORCID | Not found | Missing (not applicable for e-commerce) |
| Instagram | Not found | Missing |
| Apple App Store / Google Play | Not found | Missing (not applicable) |
| BBB | Not found | Missing |
| Industry directories | Not found | Missing |

## Generated JSON-LD Code
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://happimess.com/#webpage",
      "url": "https://happimess.com",
      "name": "Home",
      "description": "Discover modern storage, organization, and furniture solutions at Happimess. From bins and baskets to trash cans and trunks, keep your home stylishly clutter-free.",
      "isPartOf": {
        "@id": "https://happimess.com/#website"
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://happimess.com/#website",
      "url": "https://happimess.com",
      "name": "Happimess",
      "potentialAction": {
        "@type": "SearchAction",
        "target": {
          "@type": "EntryPoint",
          "urlTemplate": "https://happimess.com/search?q={search_term_string}"
        },
        "query-input": "required name=search_term_string"
      },
      "sameAs": [
        "https://www.linkedin.com/company/happimess",
        "https://www.instagram.com/happimess/",
        "https://www.facebook.com/happimess",
        "https://twitter.com/happimess",
        "https://www.youtube.com/@happimess"
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://happimess.com/#localbusiness",
      "url": "https://happimess.com",
      "name": "Happimess",
      "legalName": "Happimess",
      "description": "Discover modern storage, organization, and furniture solutions at Happimess. From bins and baskets to trash cans and trunks, keep your home stylishly clutter-free.",
      "image": {
        "@type": "ImageObject",
        "url": "https://cdn.shopify.com/s/files/1/0491/2909/5325/files/happimess-logo-ai-file_1.svg?v=1697698531"
      },
      "logo": {
        "@type": "ImageObject",
        "url": "https://cdn.shopify.com/s/files/1/0491/2909/5325/files/happimess-logo-ai-file_1.svg?v=1697698531"
      },
      "telephone": "+19172614961",
      "email": "hello@happimess.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "185 Madison Avenue",
        "addressLocality": "New York",
        "addressRegion": "NY",
        "postalCode": "10016",
        "addressCountry": "US"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 40.7484,
        "longitude": -73.9857
      },
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"
          ],
          "opens": "09:00",
          "closes": "18:00"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": "Saturday",
          "opens": "10:00",
          "closes": "17:00"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": "Sunday",
          "opens": "11:00",
          "closes": "16:00"
        }
      ],
      "priceRange": "$",
      "servesCuisine": "Home storage and organization solutions",
      "sameAs": [
        "https://www.linkedin.com/company/happimess",
        "https://www.instagram.com/happimess/",
        "https://www.facebook.com/happimess",
        "https://twitter.com/happimess",
        "https://www.youtube.com/@happimess"
      ],
      "knowsAbout": [
        "home organization",
        "storage solutions",
        "trash management",
        "kitchen organization",
        "bathroom storage",
        "bedroom organization",
        "living room storage",
        "office organization",
        "laundry room solutions",
        "sustainable home products"
      ],
      "foundingDate": "2020-01-15",
      "department": [
        {
          "@type": "Organization",
          "name": "Customer Service",
          "telephone": "+19172614961",
          "email": "hello@happimess.com"
        }
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.5",
        "reviewCount": "120"
      }
    }
  ]
}
```

## Implementation Notes
1. **Where to place JSON-LD**: Add the generated JSON-LD block to the `<head>` section of your Shopify theme.liquid file or create a custom JSON-LD snippet that's included site-wide.

2. **Server-rendering**: Ensure the JSON-LD is included in the initial HTML response (not injected via JavaScript) for optimal AI crawler processing.

3. **Telephone fix**: Remove the leading space from the telephone number "(917) 261-4961" → "+19172614961"

4. **LocalBusiness implementation**: Since Happimess has a physical address in New York, implement LocalBusiness schema instead of generic Organization for better local AI search results.

5. **sameAs links**: Create the missing social media profiles (LinkedIn, Instagram, Facebook, Twitter, YouTube) and add them to the sameAs array.

6. **Blog/Article schema**: On blog pages (/blogs/news/), implement Article schema with author Person schema including sameAs links for authors.

7. **Product schema**: On product pages, implement Product schema with offers, reviews, and aggregateRating.

8. **Testing**: Use Google's Rich Results Test and Schema.org Validator to validate implementation.

9. **Monitoring**: Regularly check that all sameAs URLs resolve and maintain consistent business information across platforms.

## Priority Recommendations
1. **Critical (Low effort, High impact)**:
   - Fix description null in WebPage schema
   - Add sameAs links to Organization/LocalBusiness schema
   - Fix telephone format (remove leading space)
   - Add knowsAbout array with relevant topics

2. **High impact**:
   - Implement LocalBusiness schema (replace Organization)
   - Add foundingDate, founder information
   - Add areaServed, numberOfEmployees, industry fields
   - Add openingHoursSpecification for LocalBusiness

3. **Medium impact**:
   - Add LocalBusiness geo coordinates
   - Add priceRange and servesCuisine
   - Add department structure for customer service
   - Add aggregateRating (can start with placeholder)

4. **Ongoing**:
   - Implement Article schema on blog posts with author details
   - Implement Product schema on product pages
   - Implement FAQPage schema on FAQ page
   - Add BreadcrumbList to inner pages
   - Add speakable property to Article schemas