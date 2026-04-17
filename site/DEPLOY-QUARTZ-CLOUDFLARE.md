# Quartz + Cloudflare Pages

This is the recommended free publishing setup for this repository.

For the current day-to-day release flow used for `minventory.org`, start with [DEPLOY-QUICK.md](./DEPLOY-QUICK.md).

## Target Stack

- Content authoring: Obsidian-compatible Markdown
- Static site generator: Quartz
- Hosting: Cloudflare Pages
- Domain: your own custom domain

## Workflow

1. Export notes into `site/content/` with `quartz-export`.
2. Use the bundled Quartz site in `site/quartz-site/`.
3. Install dependencies with `python scripts/codex_seo_machine.py quartz-install`.
4. Test a local build with `python scripts/codex_seo_machine.py quartz-build`.
5. Push this repo or the `site/quartz-site/` project to GitHub.
6. Connect the GitHub repo to Cloudflare Pages.
7. Add your custom domain in Cloudflare Pages.

## Cloudflare Pages Values

If you connect this repository directly as a monorepo, use these values:

- Production branch: `main`
- Framework preset: `None`
- Root directory (advanced): `site/quartz-site`
- Build command: `npm run build:seomachine`
- Build output directory: `public`
- Environment variable:
  - `QUARTZ_BASE_URL=your-domain.com` for an apex domain
  - `QUARTZ_BASE_URL=notes.your-domain.com` for a subdomain

## Domain Recommendation

The easiest setup is a subdomain such as `notes.your-domain.com`.

- You do not need to move the entire domain to Cloudflare for a subdomain setup.
- Add the custom domain in the Pages dashboard first.
- Then add a CNAME record at your DNS provider pointing `notes.your-domain.com` to your Pages hostname such as `your-project.pages.dev`.

If you want the apex domain itself, such as `your-domain.com`, Cloudflare requires that the domain be added as a Cloudflare zone and its nameservers be changed to Cloudflare.

## Recommended Repo Layout

Default:
- Keep this SEO Machine repo for content operations.
- Treat `site/content/` as your Obsidian vault.
- The bundled `site/quartz-site/` project builds directly from `site/content/`.

## Internal Linking

- Prefer Obsidian wikilinks: `[[another-post]]`
- Use labeled links when needed: `[[another-post|Read the comparison]]`
- Quartz resolves wikilinks and can show backlinks on the published site.

## Cloudflare Pages Notes

- Start on the free Pages plan.
- Use the Pages UI to connect your GitHub repo.
- Add your custom domain after the first successful deploy.
- Cloudflare manages TLS automatically for the connected domain.

## WordPress

WordPress remains optional in this repository, but it is no longer the recommended default publishing path.
