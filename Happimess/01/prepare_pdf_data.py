import json
import os

# Extract data from the existing GEO-AUDIT-REPORT.md
audit_data = {
    "url": "https://happimess.com",
    "brand_name": "Happimess",
    "date": "2026-04-14",
    "geo_score": 38,
    "scores": {
        "ai_citability": 37,
        "brand_authority": 18,
        "content_eeat": 37,
        "technical": 67,
        "schema": 42,
        "platform_optimization": 37
    },
    "platforms": {
        "Google AI Overviews": 44,
        "ChatGPT Web Search": 31,
        "Perplexity AI": 38,
        "Google Gemini": 36,
        "Bing Copilot": 35
    },
    "executive_summary": "Happimess is a well-merchandised Shopify e-commerce store with clean technical infrastructure but zero deliberate GEO infrastructure. The GEO Readiness Score is 38/100 (Poor). Primary barriers: missing llms.txt, missing sameAs entity links, brand name artifact ('Happimess Dev') in product schema, zero brand presence on Wikipedia/LinkedIn/Reddit/YouTube. Top 3 priorities: (1) Fix brand name (30 min), (2) Deploy llms.txt (1 hr), (3) Add sameAs links (30 min). Quick Wins alone could improve score by 15-20 points within 30 days.",
    "findings": [
        {
            "severity": "critical",
            "title": "Brand Name Artifact in Production",
            "description": "'Happimess Dev' in Product schema instead of 'Happimess', poisoning entity recognition across Google, Gemini, Bing."
        },
        {
            "severity": "critical",
            "title": "No llms.txt File",
            "description": "Missing AI crawler guide (404). Blocks AI platforms from understanding site structure."
        },
        {
            "severity": "critical",
            "title": "Organization Schema Missing sameAs",
            "description": "Zero social profile links. AI systems cannot verify brand across platforms."
        },
        {
            "severity": "critical",
            "title": "Author Identity Leak",
            "description": "Admin usernames visible in blog schema ('jonathany 2123', 'Asodariya Sumi')."
        },
        {
            "severity": "critical",
            "title": "No Named Blog Authors",
            "description": "24+ posts attributed to generic 'From The Mess Experts' with zero E-E-A-T value."
        },
        {
            "severity": "critical",
            "title": "Blog Posts Have No Publication Dates",
            "description": "No visible dates on blog content. AI cannot assess recency."
        },
        {
            "severity": "critical",
            "title": "Hreflang Not Implemented",
            "description": "Bilingual store lacks hreflang tags, creating duplicate content risk."
        },
        {
            "severity": "high",
            "title": "No Product Reviews or AggregateRating",
            "description": "Missing star ratings blocks rich results on Google, Perplexity, ChatGPT."
        },
        {
            "severity": "high",
            "title": "No Bing Webmaster Tools Verification",
            "description": "Missing msvalidate.01 and IndexNow protocol."
        },
        {
            "severity": "high",
            "title": "Policies Blocked from AI Crawlers",
            "description": "robots.txt blocks /policies/, preventing AI answers to purchase queries."
        },
        {
            "severity": "high",
            "title": "No LinkedIn Company Page",
            "description": "Entity disambiguation at risk due to unrelated Lithuanian nonprofit."
        },
        {
            "severity": "high",
            "title": "About Us Page Too Thin",
            "description": "~200 words generic copy. No founding story, team, or milestones."
        },
        {
            "severity": "medium",
            "title": "Zero External Citations on Blog",
            "description": "No outbound links to authoritative sources. AI-generated content indicator."
        },
        {
            "severity": "medium",
            "title": "FAQPage Schema Missing",
            "description": "FAQ content exists but lacks FAQPage JSON-LD markup."
        }
    ],
    "quick_wins": [
        "Fix 'Happimess Dev' → 'Happimess' in Product schema (30 min)",
        "Create and deploy llms.txt file (1 hr)",
        "Add sameAs array to Organization schema (30 min)",
        "Unblock /policies/ for AI crawlers in robots.txt (30 min)",
        "Fix description: null in WebPage schema (15 min)",
        "Verify in Bing Webmaster Tools (30 min)",
        "Fix admin usernames in Shopify blog (30 min)"
    ],
    "medium_term": [
        "Enable publication dates on all blog posts (2 hr)",
        "Rebuild About Us page with founder story (3 hr)",
        "Add FAQPage schema to /pages/faqs (2 hr)",
        "Set up review app + aggregateRating schema (3 hr)",
        "Create LinkedIn company page (1 hr)",
        "Implement hreflang for EN/ES (2 hr)",
        "Fix ItemList absolute URLs (1 hr)"
    ],
    "strategic": [
        "Add external citations to all blog posts (4 hr)",
        "Create buying guide / comparison articles (6 hr)",
        "Add speakable property to Article schema (2 hr)",
        "Create author bio pages (3 hr)",
        "Set up Trustpilot + Google Business Profile (2 hr)",
        "Build Reddit community strategy (ongoing)",
        "Implement content cluster architecture (8 hr)",
        "Pursue Wikipedia presence (6+ weeks)"
    ],
    "crawler_access": {
        "Googlebot": {"platform": "Google Search + AIO", "status": "Allowed"},
        "GPTBot": {"platform": "ChatGPT", "status": "Allowed"},
        "Bingbot": {"platform": "Bing Copilot", "status": "Allowed"},
        "PerplexityBot": {"platform": "Perplexity AI", "status": "Allowed"},
        "Google-Extended": {"platform": "Gemini", "status": "Allowed"},
        "ClaudeBot": {"platform": "Claude", "status": "Allowed"},
        "Applebot-Extended": {"platform": "Apple Intelligence", "status": "Allowed"}
    }
}

# Write to temp JSON file
temp_file = "/tmp/geo-audit-happimess.json"
with open(temp_file, 'w') as f:
    json.dump(audit_data, f, indent=2)

print(f"[OK] Audit data prepared: {temp_file}")
print(f"[OK] GEO Score: {audit_data['geo_score']}/100")
print(f"[OK] Platforms: {len(audit_data['platforms'])}")
print(f"[OK] Findings: {len(audit_data['findings'])}")
