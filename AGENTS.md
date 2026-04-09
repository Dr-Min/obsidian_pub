# SEO Machine for Codex

This repository now supports Codex-first workflows in addition to the existing Claude setup.

The preferred publishing path is now:

`drafts/` -> `site/content/` (Obsidian vault or Quartz content root) -> Quartz -> Cloudflare Pages

## Start Here

1. Read `.agents/skills/seo-machine/SKILL.md`.
2. Run `python scripts/codex_seo_machine.py context-audit` before content work.
3. Use the Codex workflow below instead of relying on `.claude/commands`.

## Codex Workflow

### 1. Audit Context

Run:

```powershell
python scripts/codex_seo_machine.py context-audit
```

If the context files are still templates, fill them before writing production content.

### 2. Create a Research Brief Scaffold

Run:

```powershell
python scripts/codex_seo_machine.py brief "your topic"
```

This creates a structured research brief in `research/`. Codex should then complete the `TBD` sections with verified research.

### 3. Build the Article Plan

Run:

```powershell
python scripts/codex_seo_machine.py plan "your topic" --brief research/brief-your-topic-YYYY-MM-DD.md
```

This creates a section-by-section article plan with writing prompts in `research/`.

### 4. Draft the Article

When drafting:

- Read `context/brand-voice.md`, `context/style-guide.md`, `context/seo-guidelines.md`, `context/features.md`, and `context/internal-links-map.md`.
- Save the article to `drafts/[topic-slug]-[YYYY-MM-DD].md`.
- Keep metadata in markdown using fields like `**Meta Title**:`, `**Meta Description**:`, and `**Primary Keyword**:`.
- Prefer Obsidian-style links such as `[[other-note]]` or `[[other-note|Anchor Text]]` for cross-post references when the target note exists.

### 5. Optimize the Draft

Run:

```powershell
python scripts/codex_seo_machine.py optimize drafts/your-article.md
```

This scrubs the draft in place and writes an optimization report next to it.

### 6. Export to Obsidian/Quartz

Run:

```powershell
python scripts/codex_seo_machine.py quartz-export drafts/your-article.md
```

This writes a Quartz-ready note into `site/content/blog/` by default. You can also point `--content-dir` to an external Obsidian vault root or an existing Quartz `content/` directory.

### 7. Install Quartz Dependencies

Run:

```powershell
python scripts/codex_seo_machine.py quartz-install
```

### 8. Preview or Build the Public Site

Local preview:

```powershell
python scripts/codex_seo_machine.py quartz-build --serve --watch
```

Static build:

```powershell
python scripts/codex_seo_machine.py quartz-build
```

### 9. Optional: Publish to WordPress

Run:

```powershell
python scripts/codex_seo_machine.py publish drafts/your-article.md
```

This uses the existing WordPress REST integration if you still want it.

## File Conventions

- Research briefs: `research/brief-[topic-slug]-[YYYY-MM-DD].md`
- Article plans: `research/article-plan-[topic-slug]-[YYYY-MM-DD].md`
- Drafts: `drafts/[topic-slug]-[YYYY-MM-DD].md`
- Obsidian/Quartz notes: `site/content/blog/[topic-slug].md`
- Quartz project: `site/quartz-site/`
- Rewrites: `rewrites/[topic-slug]-rewrite-[YYYY-MM-DD].md`
- Published references: `published/`

## Notes

- `.claude/` remains in the repo for Claude users. Codex should ignore it unless the user asks for parity work.
- `optimize` requires Python dependencies from `data_sources/requirements.txt`.
- The deterministic parts of the workflow live in `scripts/codex_seo_machine.py`; use that instead of manually recreating analysis steps.
- Quartz/Cloudflare deployment guidance lives in `site/DEPLOY-QUARTZ-CLOUDFLARE.md`.
