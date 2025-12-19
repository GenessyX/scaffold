This repository is a [Copier](https://copier.readthedocs.io/) template for new Python libraries. It bootstraps a `uv`-managed project with dependency groups for local tooling, linting, and typing.

## What gets generated
- `uv` project with `pyproject.toml` configured for `hatchling`
- Dependency groups: `local` (prek), `lint` (ruff), `types` (mypy)
- Basic Ruff and MyPy configuration
- `.pre-commit-config.yaml` populated from Copier input (or a TODO placeholder)
- Minimal package layout under `src/` plus a smoke test

## Usage
1) Install Copier (and uv) locally if you do not have them:
   ```bash
   uv tool install copier
   ```
2) Scaffold a new project by running:
   ```bash
   copier copy --trust . /path/to/new-project
   ```
   - You will be prompted for project metadata and asked to paste your `.pre-commit-config.yaml` content. If you skip it, a TODO placeholder is written so you can edit it later.
3) Inside the generated project:
   ```bash
   uv sync --group local --group lint --group types
   uv run pre-commit install  # once your config is in place
   uv run ruff check
   uv run mypy
   ```

## Notes
- The template defaults to Python 3.12; adjust via the Copier prompt.
- `uv` writes `uv.lock` when you run `uv sync`; it is ignored by default.
- Update the `Homepage`/`Issues` URLs in `pyproject.toml` after creation.
