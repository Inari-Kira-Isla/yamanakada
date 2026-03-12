# 山中田 (Yamanakada)

## Overview
Macau AI information sharing platform. An AEO-optimized single-page website hosted on GitHub Pages, featuring Schema.org structured data and llms.txt for AI discovery.

## Tech Stack
- **Hosting**: GitHub Pages
- **Type**: Static HTML (Single Page)
- **AEO Tools**: Schema.org (Organization, LocalBusiness, FAQPage), llms.txt, robots.txt

## Architecture
- **Root**: `index.html`, `llms.txt`, `robots.txt`
- **Focus**: Flat single-page structure with heavy emphasis on semantic structure and JSON-LD for search engines and AI agents.

## Commands
- **Local Dev**: Use any static server (e.g., `python3 -m http.server` or VS Code Live Server).
- **Deploy**: Push to `main` branch. GitHub Pages auto-deploys the site.

## Coding Style
- Semantic HTML5.
- Clean, minimal CSS.
- Valid external links.

## Important Rules
- **AEO**: Maintain `llms.txt` and JSON-LD schemas. Do not remove structured data.
- **Robots**: Ensure `robots.txt` allows AI crawlers.
- **License**: Content is CC BY 4.0.