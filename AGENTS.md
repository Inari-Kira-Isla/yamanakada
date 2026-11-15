# AGENTS.md - 靈動智境人工智能 SMART REALM AI website

Public static website for 靈動智境人工智能 SMART REALM AI (Macau AI consulting and knowledge platform), optimised for AI/search discovery (AEO/GEO).

## Facts
- **Canonical URL**: https://smartrealm.vercel.app
- **Deployment**: Vercel, auto-deployed from `main`. The old GitHub Pages address only redirects to the Vercel URL via a small script already present on each page; keep that script.
- **Structure**: static multi-page HTML, no build step.
  - `index.html`, `about.html`
  - `articles/` (language variants by filename suffix: `-cn`, `-en`, `-pt`)
  - `tutorials/`
  - `feed.xml`, `sitemap.xml`, `llms.txt`, `robots.txt`
  - Site-verification files (`google*.html`, `BingSiteAuth.xml`, key `*.txt`, `security.txt`) must stay untouched.
- **Security headers** are set in `vercel.json`, including a strict Content-Security-Policy. Check it before adding any external script or API call.

## Rules
- Keep `llms.txt` and the JSON-LD structured data; only edit their text values, never remove them. `robots.txt` must keep welcoming AI crawlers.
- **Every claim needs a source.** Do not invent people, numbers, customers, results or addresses.
- **Never commit secrets**: no API keys, tokens, passwords, webhook URLs, `.env` files, or hard-coded fallback values (`process.env.X || "key"`). Use environment variables only.
- Do not add backup or scratch files (`*.bak*`, `*.orig`, `*~`) to the repository.
- Work on a branch and open a pull request; do not push to `main` directly. Keep changes small and targeted.
- Do not change article body text or citations when doing brand or URL cleanups.

## Local preview
```
python3 -m http.server 3190    # then open http://localhost:3190
```
