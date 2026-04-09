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
- Korean content lives in `../content/ko`
- English content lives in `../content/en`
- Public articles should be exported as Korean/English pairs with matching relative paths and the same `translationKey`
- Export blog posts there with:

```powershell
python ..\..\scripts\codex_seo_machine.py quartz-export ..\..\drafts\your-article-ko.md --locale ko --folder blog/ai-video/camera-techniques --translation-key your-article
python ..\..\scripts\codex_seo_machine.py quartz-export ..\..\drafts\your-article-en.md --locale en --folder blog/ai-video/camera-techniques --translation-key your-article
```

Quartz supports Obsidian wikilinks and backlinks, so links like `[[another-post]]` will work in the published site.
Paired `ko/en` pages also get language-switch links and SEO-safe `hreflang` tags.
