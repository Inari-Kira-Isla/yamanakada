# 教學頁（tutorials）維護說明

教學分類 SSOT：`tutorials/categories.json`。4 類：film 短片製作、ai-tools AI 工具、games 遊戲設計、code 程式設計。
Hub 頁（`/tutorials/<slug>/`）同首頁「教學分類」卡片由 `tools/build_tutorial_hubs.py` 從 JSON 生成，**唔好手改**。

## 加一篇新教學

1. 揀分類（上面 4 個 slug 其中一個）。舊 URL 永不改。
2. 新頁放 `tutorials/<新頁名>/index.html`，head / nav / JSON-LD 抄 `tutorials/ai-assistant/index.html`。
3. 頁內標題前加分類標籤（抄現有頁嘅 `<a class="cat-tag" ...>`，href 指 `../<slug>/`，顏色用該分類色）。
4. 喺 `categories.json` 對應分類嘅 `tutorials` 加 `{title, url, date}`。
5. 跑 `python3 tools/build_tutorial_hubs.py` 重生 hub 頁同首頁分類卡（空分類有內容後會自動由 noindex 變 index）。
6. 首頁「最新文章」加一行 `<li class="article-item">`，用 `title-wrap` 包住標題同分類 chip（抄現有四行）。
7. `sitemap.xml` 加新頁；如該分類 hub 第一次有內容（games / code），hub 亦要加入 sitemap。`llms.txt` 同樣加 URL。
8. 本機 `python3 -m http.server` 逐頁 curl 200，手機闊度（375px）確認無橫向捲動，才 commit / push。

## 分類顏色（白字對比 ≥ 4.5:1）

film `#C2410C`、ai-tools `#4338CA`、games `#7E22CE`、code `#15803D`。

## 注意

- `articles/` 係自動生成，唔好碰。
- games / code 暫時空，hub 頁 `noindex` 且未入 sitemap；有第一篇教學後先加入。
