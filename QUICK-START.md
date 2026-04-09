# Quick Start Guide

Get SEO Machine running in Codex or Claude Code in 10 minutes.

## Step 1: Install Dependencies

```powershell
pip install -r data_sources/requirements.txt
```

`brief` and `plan` mostly use repo code and the standard library. `optimize` and `publish` need the Python dependencies above.

## Step 2: Configure Context Files

Fill out these files before writing production content:

- `context/brand-voice.md`
- `context/features.md`
- `context/writing-examples.md`
- `context/internal-links-map.md`
- `context/target-keywords.md`
- `context/style-guide.md`
- `context/seo-guidelines.md`

Check `examples/castos/` for a complete real-world example.

## Step 3: Start the Codex Workflow

```powershell
python scripts/codex_seo_machine.py context-audit
python scripts/codex_seo_machine.py brief "your topic"
python scripts/codex_seo_machine.py plan "your topic" --brief research/brief-your-topic-YYYY-MM-DD.md
```

Then:

1. Complete the brief with verified research.
2. Draft the article in both Korean and English into `drafts/`.
3. Run `python scripts/codex_seo_machine.py optimize drafts/your-article-ko.md` and `python scripts/codex_seo_machine.py optimize drafts/your-article-en.md`.
4. Export both versions with the same `translationKey`.
5. Run `python scripts/codex_seo_machine.py quartz-install`.
6. Run `python scripts/codex_seo_machine.py quartz-build --serve --watch`.
7. Use `site/DEPLOY-QUARTZ-CLOUDFLARE.md` to publish the site for free with your custom domain.

## Core Commands

```powershell
python scripts/codex_seo_machine.py context-audit
python scripts/codex_seo_machine.py brief "topic"
python scripts/codex_seo_machine.py plan "topic" --brief research/brief-topic-YYYY-MM-DD.md
python scripts/codex_seo_machine.py optimize drafts/topic-ko-YYYY-MM-DD.md
python scripts/codex_seo_machine.py optimize drafts/topic-en-YYYY-MM-DD.md
python scripts/codex_seo_machine.py quartz-export drafts/topic-ko-YYYY-MM-DD.md --locale ko --folder blog/ai-video/camera-techniques --translation-key topic
python scripts/codex_seo_machine.py quartz-export drafts/topic-en-YYYY-MM-DD.md --locale en --folder blog/ai-video/camera-techniques --translation-key topic
python scripts/codex_seo_machine.py quartz-install
python scripts/codex_seo_machine.py quartz-build --serve --watch
```

## Notes

- Codex instructions live in `AGENTS.md`.
- The legacy Claude slash commands still exist in `.claude/`.
- Output quality still depends heavily on how well the context files are filled out.
- WordPress publishing is optional and no longer the recommended default.
- The Quartz site is now bilingual by default. Keep Korean and English versions under matching category paths in `site/content/ko/blog/ai-video/...` and `site/content/en/blog/ai-video/...`.
- The language toggle between Korean and English only works when both versions exist and share the same `translationKey`.
- Keep public notes inside category folders like `blog/ai-video/`, `blog/ai-video/camera-techniques/`, and `blog/ai-video/seedance/` instead of using a flat blog root.
