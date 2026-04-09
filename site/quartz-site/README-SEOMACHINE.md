# Quartz Site

This bundled Quartz project is configured to read content from `../content`.

## Commands

Install dependencies:

```powershell
python ..\..\scripts\codex_seo_machine.py quartz-install
```

Preview locally:

```powershell
python ..\..\scripts\codex_seo_machine.py quartz-build --serve --watch
```

Build static files:

```powershell
python ..\..\scripts\codex_seo_machine.py quartz-build
```

You can also run the npm scripts directly from this folder:

```powershell
npm run serve:seomachine
npm run build:seomachine
```

## Content Source

- Source notes live in `../content`
- Export blog posts there with:

```powershell
python ..\..\scripts\codex_seo_machine.py quartz-export ..\..\drafts\your-article.md
```

Quartz supports Obsidian wikilinks and backlinks, so links like `[[another-post]]` will work in the published site.
