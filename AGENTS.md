# SEO Machine for Codex

This repository now supports Codex-first workflows in addition to the existing Claude setup.

The preferred publishing path is now:

`drafts/` -> `site/content/` (Obsidian vault or Quartz content root) -> Quartz -> Cloudflare Pages

## Start Here

1. Read `.agents/skills/seo-machine/SKILL.md`.
2. Run `python scripts/codex_seo_machine.py context-audit` before content work.
3. Use the Codex workflow below instead of relying on `.claude/commands`.

## Codex Workflow

## Non-Negotiable Publishing Rules

- Every publishable article must be created as a Korean and English pair.
- Korean and English versions must live at matching relative paths under `site/content/ko/...` and `site/content/en/...`.
- Korean and English versions of the same article must share the same `translationKey`.
- Public pages must support language switching with the site toggle. A reader should be able to click the toggle and move between the paired Korean and English pages.
- Do not leave a public article as one-language-only unless the user explicitly asks for a temporary exception.
- Do not dump public notes directly into `site/content/blog/`. Always place them inside a category path such as `blog/ai-video/`, `blog/ai-video/camera-techniques/`, or `blog/ai-video/seedance/`.
- For AI video content, prefer the category folders already established in the site:
  - `blog/ai-video/prompt-terms/subject-action`
  - `blog/ai-video/prompt-terms/shot-composition`
  - `blog/ai-video/prompt-terms/lens-depth`
  - `blog/ai-video/prompt-terms/camera-movement`
  - `blog/ai-video/prompt-terms/lighting`
  - `blog/ai-video/prompt-terms/mood-texture`
  - `blog/ai-video/prompt-terms/environment`
  - `blog/ai-video/prompt-terms/speed-physics`
  - `blog/ai-video/prompt-terms/editing-cuts`
  - `blog/ai-video/prompt-terms/technical-output`
  - `blog/ai-video/seedance`

## Korean Writing Tone Rules

- Korean public-facing copy must read like natural editorial Korean, not like translated AI marketing copy.
- Avoid lazy comparison jargon when plain Korean is available. Be especially careful with words and phrases such as `공격적`, `포지션`, `ceiling`, `워크플로 의존성`, and `커뮤니티 체감` when they are used as vague labels instead of concrete meaning.
- Prefer concrete rewrites that describe what the reader can actually verify. Example:
  - Avoid: `기능 스펙만 보면 제일 공격적`
  - Prefer: `공개된 지원 기능 범위가 가장 넓다`
- If an English industry term is unavoidable, explain it once and then keep the Korean sentence readable.
- Before finalizing a Korean article, quickly reread standout lines and remove any phrase that sounds like model-generated summary prose rather than a human editor's sentence.

## YouTube And Shorts Embed Rule

- If the user provides a specific YouTube video or Shorts URL for a public article, embed it in the article unless the user explicitly wants a plain link only.
- For Korean and English article pairs, keep the embed in both versions at the same relative position.
- Default placement is immediately below the H1.
- In Quartz markdown, use a raw HTML `iframe`, not a plain pasted URL, when the goal is an inline playable embed.
- Reuse the site class `external-embed youtube` so the existing responsive styling applies automatically.
- Convert Shorts URLs from `https://www.youtube.com/shorts/VIDEO_ID` to `https://www.youtube.com/embed/VIDEO_ID`.
- Standard snippet:

```html
<iframe
  class="external-embed youtube"
  src="https://www.youtube.com/embed/VIDEO_ID"
  title="Descriptive video title"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>
```

- Only replace `VIDEO_ID` and `title` unless the user asks for a custom layout.

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
- Draft both the Korean and English versions for any publishable article.
- Keep metadata in markdown using fields like `**Meta Title**:`, `**Meta Description**:`, and `**Primary Keyword**:`.
- Prefer Obsidian-style links such as `[[other-note]]` or `[[other-note|Anchor Text]]` for cross-post references when the target note exists.

### Korean Prompt Archive Preference

- For Korean-only explanatory sections that unpack English prompt phrases, keep the English phrase and add a direct Korean translation immediately below it before the explanation.
- Preferred pattern for Korean pages:
  - `` `transitions from running on cars to sprinting along the vertical wall` ``
  - `한국어 번역: 자동차 위를 달리던 흐름에서 수직 벽 질주로 전환한다`
  - Then explain why that phrase matters.
- Apply this preference only to Korean pages unless the user explicitly asks to mirror it in English pages.

### 5. Optimize the Draft

Run:

```powershell
python scripts/codex_seo_machine.py optimize drafts/your-article.md
```

This scrubs the draft in place and writes an optimization report next to it.

### 6. Export to Obsidian/Quartz

Run:

```powershell
python scripts/codex_seo_machine.py quartz-export drafts/your-article-ko.md --locale ko --folder blog/ai-video/camera-techniques --translation-key your-article
python scripts/codex_seo_machine.py quartz-export drafts/your-article-en.md --locale en --folder blog/ai-video/camera-techniques --translation-key your-article
```

This writes Quartz-ready notes into matching Korean and English paths when you pass `--locale`, a nested `--folder`, and the same `--translation-key` for both exports. The shared `translationKey` is what makes the site toggle switch between languages. You can also point `--content-dir` to an external Obsidian vault root or an existing Quartz `content/` directory.

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
- Obsidian/Quartz notes: `site/content/[locale]/blog/ai-video/[category]/[topic-slug].md`
- Quartz project: `site/quartz-site/`
- Rewrites: `rewrites/[topic-slug]-rewrite-[YYYY-MM-DD].md`
- Published references: `published/`

## Notes

- `.claude/` remains in the repo for Claude users. Codex should ignore it unless the user asks for parity work.
- `optimize` requires Python dependencies from `data_sources/requirements.txt`.
- The deterministic parts of the workflow live in `scripts/codex_seo_machine.py`; use that instead of manually recreating analysis steps.
- Quartz/Cloudflare deployment guidance lives in `site/DEPLOY-QUARTZ-CLOUDFLARE.md`.
- Language-toggle behavior depends on Korean and English pages both existing and sharing the same `translationKey`.
- Category management is mandatory. Put each article into the closest matching category folder instead of using a flat blog root.
