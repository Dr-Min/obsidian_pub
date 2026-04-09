# Site Content

`site/content/` is the default publishing root for the free Obsidian + Quartz workflow.
It now uses a bilingual structure:

- `site/content/ko/` for Korean pages
- `site/content/en/` for English pages
- `site/content/index.md` as the language hub

Important publishing rule:

- Public articles should be created in both Korean and English.
- Keep both versions at matching relative paths.
- Reuse the same `translationKey` for both pages so the site language toggle can switch between them.
- Keep public notes inside category folders such as `blog/ai-video/`, `blog/ai-video/camera-techniques/`, and `blog/ai-video/seedance/`.

## How to Use It

1. Draft articles in `drafts/`.
2. Run:

```powershell
python scripts/codex_seo_machine.py quartz-export drafts/your-article-ko.md --locale ko --folder blog/ai-video/seedance --translation-key your-article
python scripts/codex_seo_machine.py quartz-export drafts/your-article-en.md --locale en --folder blog/ai-video/seedance --translation-key your-article
```

3. The exported note appears in `site/content/ko/blog/ai-video/...` or `site/content/en/blog/ai-video/...` depending on the `--folder` you choose.
4. Open `site/content/` as an Obsidian vault if you want to edit or link notes there directly.
5. Use the bundled Quartz project in `site/quartz-site/` to preview and build the site.

## Wikilinks and Backlinks

- Write links as `[[other-note]]` or `[[other-note|Custom Label]]`.
- `quartz-export` also converts matching internal Markdown links into Obsidian wikilinks where possible.
- Quartz supports wikilinks and shows backlinks, so readers can move between related notes and see inbound references.
- If Korean and English versions share the same `translationKey`, the site adds language switch links and `hreflang` metadata automatically.
