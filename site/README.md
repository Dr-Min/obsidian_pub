# Site Content

`site/content/` is the default publishing root for the free Obsidian + Quartz workflow.

## How to Use It

1. Draft articles in `drafts/`.
2. Run:

```powershell
python scripts/codex_seo_machine.py quartz-export drafts/your-article.md
```

3. The exported note appears in `site/content/blog/`.
4. Open `site/content/` as an Obsidian vault if you want to edit or link notes there directly.
5. Use the bundled Quartz project in `site/quartz-site/` to preview and build the site.

## Wikilinks and Backlinks

- Write links as `[[other-note]]` or `[[other-note|Custom Label]]`.
- `quartz-export` also converts matching internal Markdown links into Obsidian wikilinks where possible.
- Quartz supports wikilinks and shows backlinks, so readers can move between related notes and see inbound references.
