# personal-page

Static personal page: intro, GitHub/LinkedIn links and a portfolio section.
Rendered with Jinja2 and served as a static-assets-only Cloudflare Worker.

## Edit content

All text, links and projects live in `content/site.toml`. Add a portfolio
entry by appending another `[[projects]]` table (`demo`, `source` and `tags`
are optional).

## Commands

Requires [uv](https://docs.astral.sh/uv/) and Node.js (for `npx wrangler`).

```sh
uv sync                              # install dependencies (first time)
uv run deploy.py                     # build, then preview at http://localhost:8787 (same as --local)
uv run deploy.py --build-only        # build into deploy/public/ only
uv run deploy.py --live              # build, then deploy to Cloudflare
```

Every mode rebuilds `deploy/public/` first. Unrecognised arguments are passed
through to Wrangler, e.g. `uv run deploy.py --live --dry-run` or
`uv run deploy.py --port 8000`.

Before the first `--live` deploy, log in once: `cd deploy && npx wrangler login`.

## Layout

```text
content/site.toml       page content (edit this)
templates/              Jinja2 templates; files starting with "_" are layouts, not pages
static/                 copied verbatim into the output (CSS, images)
deploy.py               build script and CLI (local preview / live deploy / build only)
deploy/wrangler.jsonc   Cloudflare Workers config; deploy/public/ is build output (gitignored)
docs/decisions/         ADRs, NNNN-title.md
```
