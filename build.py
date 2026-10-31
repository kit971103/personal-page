import shutil
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
OUTPUT = ROOT / "deploy" / "public"

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


if __name__ == "__main__":
    build()
