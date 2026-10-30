# python-template-uv

Python project template managed by [uv](https://docs.astral.sh/uv/).

## Using this template

1. Rename the package directory `src/project_name/` to your package name.
2. Update `name` and `description` in `pyproject.toml`; `name` must match
   the package directory (hyphens become underscores).

## Setup

```sh
uv sync                    # create .venv and install the project + dev dependencies
uv sync --group notebook   # also install JupyterLab (optional)
uv run jupyter lab         # start JupyterLab (after the line above)
```

## Common commands

```sh
uvx ruff check .           # lint
uvx ruff format .          # format
uv run mypy src            # type check (mypy)
uv run ty check            # type check (ty, preview)
uv add <package>           # add a runtime dependency
uv add --dev <package>     # add a dev dependency
```

## Layout

```text
src/project_name/   package source (installed in editable mode by uv sync)
docs/decisions/     architecture decision records (ADRs), NNNN-title.md
```
