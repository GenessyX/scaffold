This repository is a [Copier](https://copier.readthedocs.io/) template for new Python libraries. It bootstraps a `uv`-managed project with dependency groups for local tooling, linting, and typing.

## What gets generated
- `uv` project with `pyproject.toml` configured for `uv_build`
- Dependency groups: `local` (prek), `lint` (ruff), `types` (mypy), `tests` (pytest)
- Basic Ruff and MyPy configuration
- `.pre-commit-config.yaml` with:
   - [`pre-commit-hooks`](https://github.com/pre-commit/pre-commit-hooks).
   - [`taplo-pre-commit`](https://github.com/ComPWA/taplo-pre-commit) - toml formatting.
   - [`ruff`](https://github.com/astral-sh/ruff-pre-commit).
   - [`mypy`](https://github.com/pre-commit/mirrors-mypy).
   - [`commitlint`](https://github.com/alessandrojcm/commitlint-pre-commit-hook)
- Minimal package layout under `src/` plus a smoke test

## Usage
1) Install Copier (and uv) locally if you do not have them:
   ```bash
   uv tool install copier
   ```
2) Scaffold a new project by running:
   ```bash
   copier copy --trust https://github.com/GenessyX/scaffold /path/to/new-project
   ```


## Notes
- The template defaults to Python 3.12; adjust via the Copier prompt.
