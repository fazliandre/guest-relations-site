# The Guest Relations System — Site

The public search site for The Guest Relations System. Six pages: a home page
and five articles. Each page is self-contained, so you can open any of them in
a browser directly.

Live at https://fazliandre.github.io/guest-relations-site

## Building

```
python3 scripts/build-site.py
```

This regenerates all six pages plus `sitemap.xml` and `robots.txt` from one
place. **Edit the script, not the HTML** — the design stays consistent across
every page that way, and the deploy workflow rejects hand-edited output.

Two settings live at the top of `scripts/build-site.py`:

- `SITE` — the public base URL, used for canonical tags, `og:url`, schema,
  the sitemap, and robots.txt.
- `BUY` — the Gumroad product link. While it is `"#"` the seven
  "Get the full pack" buttons are dead. Setting it to the real URL feeds all
  seven at once. This is the one thing still outstanding.

## Hosting

Deploys to GitHub Pages from `main` via `.github/workflows/pages.yml`.

**One-time setup:** repo **Settings → Pages → Source → GitHub Actions**.
Until that is set the workflow fails at `configure-pages` with
`Get Pages site failed ... Not Found`. It cannot be automated — creating a
Pages site needs admin rights the workflow's `GITHUB_TOKEN` does not have.

The workflow also rebuilds the site and fails if the committed `site/` is out
of date, so always commit the regenerated HTML alongside a change to
`build-site.py`.

## The split

This repository is public because GitHub Pages does not serve private
repositories on the free plan.

It holds **only** the site. The paid product and the script that generates it
stay in a separate private repository and must never be added here.
