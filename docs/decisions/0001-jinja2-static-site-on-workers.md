# 0001. Jinja2 static site served by Cloudflare Workers static assets

- Status: accepted
- Date: 2026-10-30
- ClickUp task: <link>

## Context

The personal page is a single page with an intro, social links and a short
portfolio list. It needs no runtime logic and should be cheap to host on the
existing Cloudflare account.

## Decision

Generate HTML with a small Python script using Jinja2 (content in TOML) and
deploy the output as a static-assets-only Worker (`assets.directory`, no
`main` script).

## Alternatives considered

- Off-the-shelf SSG (Pelican, Hugo, Astro): more features than one page needs,
  adds a framework to learn and upgrade.
- Cloudflare Pages: Workers static assets is Cloudflare's recommended path for
  new projects and matches the rest of the stack.
- Worker script rendering at request time: unnecessary for static content.

## Consequences

- No JavaScript or runtime cost; content changes require rebuild + redeploy.
- Adding pages means adding a template; anything beyond that (Markdown posts,
  RSS) has to be written by hand or prompts a revisit of this decision.
