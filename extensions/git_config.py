from __future__ import annotations

import subprocess
from typing import TYPE_CHECKING

from jinja2.ext import Extension

if TYPE_CHECKING:
    from jinja2 import Environment


def _git_config(key: str, default: str = "") -> str:
    """Return a git config value or default if missing/errors."""
    try:
        result = subprocess.run(  # noqa: S603
            ["git", "config", "--get", key],  # noqa: S607
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            value = result.stdout.strip()
            if value:
                return value
    except Exception:  # noqa: BLE001, S110
        pass
    return default


class GitConfigExtension(Extension):
    """Expose a git_config(key, default) helper to Jinja templates."""

    def __init__(self, environment: "Environment"):
        super().__init__(environment)
        environment.globals["git_config"] = _git_config  # pyright: ignore[reportArgumentType]
