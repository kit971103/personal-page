import argparse
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

from jinja2 import (
    Environment,
    FileSystemLoader,
    StrictUndefined,
    select_autoescape,
)

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content" / "site.toml"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
DEPLOY_DIR = ROOT / "deploy"
OUTPUT = DEPLOY_DIR / "public"

# Templates starting with "_" are layouts/partials and are not rendered as pages.
PAGE_PREFIX_SKIP = "_"


def build(output: Path = OUTPUT) -> None:
    """Render the Jinja2 templates into a static site for Cloudflare Workers."""
    site = tomllib.loads(CONTENT.read_text(encoding="utf-8"))
    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(STATIC, output)

    for template in TEMPLATES.glob("*.html"):
        if template.name.startswith(PAGE_PREFIX_SKIP):
            continue
        html = env.get_template(template.name).render(site=site)
        (output / template.name).write_text(html, encoding="utf-8")
        print(f"rendered {template.name}")

    print(f"site written to {output}")


def wrangler(command: str, extra_args: list[str]) -> None:
    """Run a Wrangler command in the deploy folder and exit with its code."""
    # On Windows npx is npx.cmd, so resolve it instead of hard-coding the name.
    npx = shutil.which("npx")
    if npx is None:
        sys.exit("npx not found: install Node.js to run Wrangler")

    result = subprocess.run(  # noqa: S603
        [npx, "wrangler", command, *extra_args],
        cwd=DEPLOY_DIR,
        check=False,
    )
    sys.exit(result.returncode)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build the site, then preview it or deploy it.",
        epilog="Unknown args are passed to Wrangler, e.g. --live --dry-run.",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--local",
        action="store_const",
        dest="mode",
        const="local",
        help="build, then serve with `wrangler dev` (default)",
    )
    mode.add_argument(
        "--live",
        action="store_const",
        dest="mode",
        const="live",
        help="build, then deploy to Cloudflare with `wrangler deploy`",
    )
    mode.add_argument(
        "--build-only",
        action="store_const",
        dest="mode",
        const="build",
        help="build into deploy/public/ and stop",
    )
    parser.set_defaults(mode="local")
    args, extra_args = parser.parse_known_args()

    build()
    if args.mode == "local":
        wrangler("dev", extra_args)
    elif args.mode == "live":
        wrangler("deploy", extra_args)


if __name__ == "__main__":
    main()
