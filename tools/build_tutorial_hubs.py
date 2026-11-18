#!/usr/bin/env python3
"""Regenerate tutorial hub pages (tutorials/<slug>/index.html) and the home
page 教學分類 section from tutorials/categories.json.  Usage: python3 tools/build_tutorial_hubs.py"""
import json, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "tutorials" / "categories.json").read_text(encoding="utf-8"))
SITE = DATA["site"]
E = html.escape

HUB = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <script>/* smartrealm-move */if(/github\\.io$/.test(location.hostname)){{location.replace('https://smartrealm.vercel.app'+location.pathname.replace(/^\\/yamanakada/,'')+location.search+location.hash)}}</script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name}教學 | 靈動智境</title>
  <meta name="description" content="{desc_attr}">
  <meta name="robots" content="{robots}">
  <meta name="author" content="Joe｜建築AI男">
  <link rel="canonical" href="{site}/tutorials/{slug}/">
  <link rel="llms-txt" href="{site}/llms.txt">
  <meta property="og:title" content="{name}教學 | 靈動智境">
  <meta property="og:description" content="{desc_attr}">
  <meta property="og:image" content="{site}/images/og-image.jpg">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{site}/tutorials/{slug}/">
  <meta property="og:locale" content="zh_TW">
  <meta property="og:site_name" content="靈動智境人工智能 SMART REALM AI">
  <script type="application/ld+json">
  {jsonld}
  </script>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700;900&display=swap" rel="stylesheet">
  <style>
    :root {{ --cat: {color}; --cat-soft: {soft}; --bg: #fafafa; --text: #1e293b; --text-light: #475569; --card-bg: #ffffff; --border: #e2e8f0; --accent: #6366f1; }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'Noto Sans TC', system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.8; overflow-wrap: anywhere; overflow-x: hidden; }}
    a {{ color: var(--cat); }}
    nav {{ background: #fff; border-bottom: 1px solid var(--border); }}
    nav .container {{ max-width: 1080px; margin: 0 auto; padding: 0 16px; display: flex; justify-content: space-between; align-items: center; height: 56px; }}
    nav .logo {{ font-weight: 700; font-size: 1.1rem; color: var(--text); text-decoration: none; }}
    nav .logo span {{ color: var(--accent); }}
    nav .back {{ font-size: 0.9rem; color: var(--text-light); }}
    .hero {{ background: var(--cat); color: #fff; padding: 48px 16px 40px; }}
    .hero .inner {{ max-width: 1080px; margin: 0 auto; }}
    .kicker {{ display: inline-block; border: 1px solid rgba(255,255,255,0.85); border-radius: 4px; padding: 2px 10px; font-size: 0.8rem; letter-spacing: 0.08em; margin-bottom: 18px; }}
    .hero h1 {{ font-size: 1.9rem; font-weight: 900; line-height: 1.35; margin-bottom: 12px; }}
    .hero .lead {{ font-size: 1.05rem; max-width: 640px; }}
    .wrap {{ max-width: 1080px; margin: 0 auto; padding: 40px 16px 64px; }}
    .wrap h2 {{ font-size: 1.3rem; margin-bottom: 20px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }}
    .tcard {{ display: block; background: var(--card-bg); border: 1px solid var(--border); border-top: 4px solid var(--cat); border-radius: 12px; padding: 22px; text-decoration: none; color: var(--text); transition: transform .2s, box-shadow .2s; }}
    .tcard:hover {{ transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.08); }}
    .tcard .tag {{ display: inline-block; background: var(--cat); color: #fff; font-size: 0.75rem; border-radius: 4px; padding: 0 8px; margin-bottom: 10px; }}
    .tcard h3 {{ font-size: 1.05rem; line-height: 1.5; margin-bottom: 8px; }}
    .tcard .date {{ font-size: 0.85rem; color: var(--text-light); }}
    .btn {{ display: inline-block; background: var(--cat); color: #fff; text-decoration: none; border-radius: 8px; padding: 10px 20px; font-weight: 700; margin-top: 8px; }}
    .btn:hover {{ text-decoration: underline; }}
    .empty {{ background: var(--cat-soft); border: 1px dashed var(--cat); border-radius: 12px; padding: 40px 20px; text-align: center; }}
    .empty p {{ font-size: 1.1rem; margin-bottom: 12px; }}
    .others {{ margin-top: 48px; }}
    .others a {{ display: inline-block; margin: 0 8px 8px 0; padding: 4px 14px; border-radius: 999px; border: 1px solid var(--border); background: #fff; text-decoration: none; font-size: 0.9rem; }}
    footer {{ text-align: center; padding: 24px 16px; font-size: 0.85rem; color: var(--text-light); border-top: 1px solid var(--border); }}
    @media (max-width: 600px) {{ .hero h1 {{ font-size: 1.5rem; }} .grid {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>

<nav>
  <div class="container">
    <a class="logo" href="../../">靈動智<span>境</span> AI</a>
    <a class="back" href="../../#tutorial-categories">&larr; 返回教學分類</a>
  </div>
</nav>

<header class="hero">
  <div class="inner">
    <span class="kicker">{icon} 教學分類</span>
    <h1>{name}教學</h1>
    <p class="lead">{desc}</p>
  </div>
</header>

<main class="wrap">
  <h2>{name}　共 {count} 篇</h2>
{body}
  <div class="others">
    <p style="margin-bottom:8px;color:var(--text-light)">其他分類</p>
{others}
  </div>
</main>

<footer>
  <p>靈動智境人工智能 SMART REALM AI · <a href="/llms.txt">llms.txt</a> · <a href="/sitemap.xml">Sitemap</a></p>
</footer>
<img src="https://client-ai-tracker.inariglobal.workers.dev/yamanakada/pixel.gif?p=/tutorials/{slug}/" width="1" height="1" alt="" loading="eager" style="position:absolute;left:-9999px">
</body>
</html>
"""

def hub(c):
    ts = sorted(c["tutorials"], key=lambda t: t["date"], reverse=True)
    if ts:
        cards = "\n".join(
            f'    <a class="tcard" href="{E(t["url"])}"><span class="tag">{E(c["name"])}</span><h3>{E(t["title"])}</h3><span class="date">{E(t["date"])}</span></a>'
            for t in ts)
        body = f'  <div class="grid">\n{cards}\n  </div>'
    else:
        body = '  <div class="empty"><p>準備中，陸續上架</p><a class="btn" href="../../#tutorial-categories">睇其他分類</a></div>'
    others = "\n".join(f'    <a href="../{o["slug"]}/" style="color:{o["color"]}">{o["icon"]} {E(o["name"])}</a>'
                       for o in DATA["categories"] if o["slug"] != c["slug"])
    url = f'{SITE}/tutorials/{c["slug"]}/'
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": f'{c["name"]}教學',
          "description": c["description"], "inLanguage": "zh-Hant", "url": url,
          "isPartOf": {"@type": "WebSite", "name": "靈動智境人工智能 SMART REALM AI", "url": SITE + "/"},
          "mainEntity": {"@type": "ItemList", "itemListElement": [
              {"@type": "ListItem", "position": i + 1, "name": t["title"], "url": SITE + t["url"]} for i, t in enumerate(ts)]}}
    return HUB.format(name=c["name"], desc=E(c["description"]), desc_attr=E(c["description"], quote=True), slug=c["slug"],
                      site=SITE, color=c["color"], soft=c["color_soft"], icon=c["icon"], count=len(ts), body=body,
                      others=others, robots="index, follow" if ts else "noindex, follow",
                      jsonld=json.dumps(ld, ensure_ascii=False, indent=2).replace("\n", "\n  "))

def home_cards():
    out = []
    for c in DATA["categories"]:
        n = len(c["tutorials"])
        status = f"{n} 篇教學" if n else "準備中，陸續上架"
        out.append(f'''      <a class="cat-card" href="tutorials/{c["slug"]}/" style="--cat:{c["color"]};--cat-soft:{c["color_soft"]}">
        <div class="icon">{c["icon"]}</div>
        <h3>{E(c["name"])}</h3>
        <p>{E(c["description"])}</p>
        <span class="cat-count">{status}</span>
      </a>''')
    return "\n".join(out)

def main():
    for c in DATA["categories"]:
        d = ROOT / "tutorials" / c["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(hub(c), encoding="utf-8")
        print("wrote", d / "index.html")
    idx = ROOT / "index.html"
    s = idx.read_text(encoding="utf-8")
    a, b = "<!-- TUTORIAL-CATEGORIES-START -->", "<!-- TUTORIAL-CATEGORIES-END -->"
    if a in s and b in s:
        pre, rest = s.split(a, 1)
        _, post = rest.split(b, 1)
        s = pre + a + "\n" + home_cards() + "\n      " + b + post
        idx.write_text(s, encoding="utf-8")
        print("updated home cards")
    else:
        print("home markers not found; home not touched")

if __name__ == "__main__":
    main()
