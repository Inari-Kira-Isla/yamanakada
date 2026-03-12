# 山中田 (Yamanakada)

## Project
Single-page AEO-optimized website for Macau AI information sharing, deployed on GitHub Pages.

## Conventions
- Keep all content in single HTML file
- Use semantic HTML5 elements
- Include Schema.org JSON-LD structured data
- Generate llms.txt at site root
- Place FAQ in structured format for AEO

## Naming
- Use lowercase for file names: `index.html`, `llms.txt`, `robots.txt`
- Maintain consistent Japanese/Chinese naming for headings

## Architecture
- Static HTML with embedded CSS/JS
- Schema.org: Organization, LocalBusiness, FAQPage
- Single-page design with anchor navigation
- AEO-first approach: prioritize AI crawler accessibility

## Commands
- Push to `main` branch to trigger auto-deploy
- No build process required

## Do Not
- Do not add backend code or server-side rendering
- Do not use frameworks (React, Vue, etc.) — keep it static HTML
- Do not modify deployment workflow — GitHub Pages auto-deploys from main