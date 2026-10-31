# personal-page

Static personal page positioning Kit as a technical analyst: hero, proof
stats, a featured case study, side projects and skills. Rendered with Jinja2
and served as a static-assets-only Cloudflare Worker.

## Edit content

All text, links and projects live in `content/site.toml`. Add a portfolio
entry by appending another `[[projects]]` table (`proves` is required; `demo`,
`source`, `tags` and `featured` are optional). Before changing copy or styling,
read `docs/0001-design-navy-technical-analyst.md`.

## Commands

Requires [uv](https://docs.astral.sh/uv/) and Node.js (for `npx wrangler`).

```sh
uv sync                              # install dependencies (first time)
uv run build.py                      # build into deploy/public/
cd deploy && npx wrangler dev        # preview at http://localhost:8787
cd deploy && npx wrangler deploy     # deploy to Cloudflare
```

Before the first deploy, log in once: `cd deploy && npx wrangler login`.

## Layout

```text
content/site.toml       page content (edit this)
templates/              Jinja2 templates; files starting with "_" are layouts, not pages
static/                 copied verbatim into the output (CSS, images)
build.py                build script
deploy/wrangler.jsonc   Cloudflare Workers config; deploy/public/ is build output (gitignored)
docs/                   design records, 0001-design-title.md
docs/decisions/         ADRs, NNNN-title.md
```
