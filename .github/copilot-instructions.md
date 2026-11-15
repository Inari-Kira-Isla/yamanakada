# 靈動智境人工智能 SMART REALM AI (website repo)

Public static multi-page website (AEO/GEO optimised). Same facts and rules are mirrored in `AGENTS.md` and `GEMINI.md` - keep the three consistent.

## Facts (verified against the repository)
- **Brand**: 靈動智境人工智能 SMART REALM AI (renamed from 山中田 Yamanakada on 2026-03-22). Use the new name for all display text. The old name appears only as `alternateName` in JSON-LD, in historical article titles ("山中田最新資訊"), and in tracker/repo paths; do not "fix" those without asking.
- **Canonical URL**: https://smartrealm.vercel.app (every page's `<link rel="canonical">` points here).
- **Deployment**: Vercel project `smartrealm`, auto-deployed from `main` of Inari-Kira-Isla/yamanakada. The old GitHub Pages address (inari-kira-isla.github.io/yamanakada) is redirect-only: each page carries a small `smartrealm-move` script that forwards github.io visitors to the Vercel URL. Keep that script.
- **Structure**: static multi-page HTML, no build step, no framework.
  - `index.html`, `about.html`
  - `articles/` - articles, with language variants by filename suffix (`-cn`, `-en`, `-pt`)
  - `tutorials/` - currently `tutorials/claude-codex/`
  - `feed.xml`, `sitemap.xml`, `llms.txt`, `robots.txt`
  - Verification files (`google*.html`, `BingSiteAuth.xml`, IndexNow key `*.txt`, `security.txt`) must stay untouched.
- **Vercel config**: `vercel.json` sets security headers (incl. a strict Content-Security-Policy: scripts only from self/inline, `connect-src 'self'`) - check CSP before adding any external script or API call. `.vercelignore` excludes `*.bak*`, `.github`, `AGENTS.md`, `GEMINI.md`, `.env*`.
- **License**: pages state content is CC BY 4.0 (footer links and `llms.txt`). There is no LICENSE file in the repo; whether code/other files share that license is unconfirmed (pending owner).

## Rules
- Keep `llms.txt` and the JSON-LD structured data (Organization / ProfessionalService / FAQPage etc.). Never remove them; only edit their text values.
- `robots.txt` must keep welcoming AI crawlers.
- **Every claim needs a source. Do not invent people, numbers, customers, results or addresses.** (The fabricated founder persona and unsourced superlatives were removed in July 2026 - do not reintroduce them.)
- Do not edit article body text, data or citations when doing brand/URL cleanups; only change brand names or URLs mechanically.
- Work on a branch and open a PR; do not push to `main` directly. Ask the owner (Joe) before changing public URLs, domains, or shared scripts/trackers.
- Several machines and a daily automated job commit to this repo at the same time. Keep changes small and targeted, do not reformat untouched files, and `git pull`/fetch before starting.
- If you regenerate `sitemap.xml`: each `<loc>` must equal that page's own canonical. The generator script is not in this repo (`llms.txt` header says "Generated"), so an automated run may overwrite manual edits.

## Local preview
```
cd /path/to/yamanakada
python3 -m http.server 3190    # open http://localhost:3190 ; stop with Ctrl+C
```

## Do Not
- Do not add backend code, frameworks (React, Vue, etc.) or a build step - keep it static HTML.
- Do not remove the github.io redirect snippet or the Vercel-based canonical URLs.
