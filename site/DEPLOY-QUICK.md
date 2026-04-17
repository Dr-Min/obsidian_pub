# Quick Deploy

This is the fastest day-to-day deploy flow for the live blog at `minventory.org`.

## Current Production Target

- Remote: `userrepo`
- Production branch: `main`
- Quartz root: `site/quartz-site`
- Build command: `npm run build:seomachine`
- Live domain: `https://minventory.org`

## Fastest Daily Flow

1. Edit the content pair.
   - Public posts should exist in both `site/content/ko/...` and `site/content/en/...`
   - Keep the same relative path and the same `translationKey`
2. Build locally before pushing.

```powershell
cd C:\ccode\_inspect_seomachine\site\quartz-site
npm run build:seomachine
```

3. Commit the changes on your working branch.

```powershell
cd C:\ccode\_inspect_seomachine
git status --short
git add site/content site/README.md site/DEPLOY-QUICK.md site/DEPLOY-QUARTZ-CLOUDFLARE.md
git commit -m "Update blog content"
```

4. Push the working branch for backup and review.

```powershell
git push userrepo HEAD
```

5. Push the same tip to production.

```powershell
git push userrepo HEAD:main
```

6. Verify the live page.
   - Open the exact `https://minventory.org/ko/...` URL
   - Open the exact `https://minventory.org/en/...` URL
   - Confirm the new headline, copy, or links are live

## Optional Release Branch Flow

If you want to keep your working branch separate from the release branch, use the local deploy branch and push that branch to remote `main`.

Current local deploy branch:

- `deploy/noir-western`

Example flow:

```powershell
cd C:\ccode\_inspect_seomachine
git checkout deploy/noir-western
git cherry-pick <feature-commit>
git push userrepo HEAD:main
git checkout <your-working-branch>
```

## Do Not Accidentally Commit

- `site/content/.obsidian/`
- `site/content/en/.obsidian/`
- scratch folders such as `site/content/*/blog/ai-video/test/`

## Troubleshooting

If `git` fails in the sandbox with a dubious ownership warning, mark the repo as safe:

```powershell
git config --global --add safe.directory C:/ccode/_inspect_seomachine
```

For Cloudflare Pages setup details, monorepo settings, and domain notes, see [DEPLOY-QUARTZ-CLOUDFLARE.md](./DEPLOY-QUARTZ-CLOUDFLARE.md).
