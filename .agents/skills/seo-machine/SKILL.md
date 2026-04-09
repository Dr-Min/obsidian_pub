---
name: seo-machine
description: Use this skill when working on SEO Machine content workflows in Codex, including auditing context files, scaffolding research briefs, generating article plans, optimizing markdown drafts, exporting Obsidian/Quartz notes, and optionally publishing to WordPress.
---

# SEO Machine

Use this skill for repository-local content operations in this workspace.

## Workflow

1. Run `python scripts/codex_seo_machine.py context-audit`.
2. Scaffold a brief with `python scripts/codex_seo_machine.py brief "<topic>"`.
3. Complete the brief with verified research.
4. Generate a plan with `python scripts/codex_seo_machine.py plan "<topic>" --brief <brief-path>`.
5. Draft the article into `drafts/`.
6. Optimize with `python scripts/codex_seo_machine.py optimize <draft-path>`.
7. Export with `python scripts/codex_seo_machine.py quartz-export <draft-path>`.
8. Publish with `python scripts/codex_seo_machine.py publish <draft-path>` only when the user specifically wants WordPress.

## Working Rules

- Treat `context/*.md` as the source of truth for voice, style, SEO rules, features, and internal links.
- Do not skip context auditing if files still contain template placeholders.
- Every publishable article must exist in both Korean and English.
- Keep Korean and English versions in matching relative paths and reuse the same `translationKey` so the Quartz language toggle can switch between them.
- Do not leave a public article as Korean-only or English-only unless the user explicitly approves that exception.
- Organize publishable notes into category folders, not a flat blog root. Example paths: `blog/ai-video/`, `blog/ai-video/camera-techniques/`, `blog/ai-video/seedance/`.
- Use markdown metadata fields in article drafts:
  - `**Meta Title**:`
  - `**Meta Description**:`
  - `**Primary Keyword**:`
  - `**Secondary Keywords**:`
  - `**URL Slug**:`
- Keep research briefs in `research/` and drafts in `drafts/`.
- Use `site/content/` as the default Obsidian vault or Quartz content root.
- Prefer Obsidian wikilinks `[[note]]` or `[[note|Label]]` for internal note-to-note linking.
- When exporting for publication, run `quartz-export` for both locales and keep the folder path identical on both sides.
- Use the CLI for deterministic work instead of redoing analysis manually.

## Command Reference

- `context-audit`: checks whether context files are still templates.
- `brief`: creates a Codex-ready research brief scaffold.
- `plan`: creates an article plan with section prompts.
- `optimize`: scrubs and analyzes a draft, then writes an optimization report.
- `quartz-export`: converts a draft into a Quartz-ready Obsidian note with frontmatter and wikilinks.
- `publish`: sends a draft to WordPress using the existing REST integration.

## Dependency Notes

- `plan` and `brief` work with the standard library plus repo modules.
- `optimize` requires `pip install -r data_sources/requirements.txt`.
- `publish` requires valid WordPress credentials in the configured environment variables.
