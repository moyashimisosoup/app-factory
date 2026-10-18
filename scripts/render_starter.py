#!/usr/bin/env python3
"""Render optional, non-destructive web starter files. No GitHub API or tokens."""
from __future__ import annotations

import argparse
import html
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "templates" / "web-minimal"
TEMPLATE_PATHS = (
    "README.md",
    "AGENTS.md",
    "index.html",
    "docs/ROADMAP.md",
)
REPO_NAME = re.compile(r"^[a-z][a-z0-9-]{2,48}[a-z0-9]$")
PLACEHOLDER = re.compile(r"%%[A-Z_]+%%")


def markdown_text(value: str) -> str:
    """Avoid interpreting user-provided metadata as Markdown/HTML markup."""
    result = html.escape(value, quote=False)
    for char in ("\\", "`", "|", "*", "_", "[", "]"):
        result = result.replace(char, "\\" + char)
    return result


def validate(app_name: str, repo_name: str, description: str, visibility: str) -> None:
    if not REPO_NAME.fullmatch(repo_name):
        raise ValueError("Invalid repository slug.")
    if visibility not in ("private", "public"):
        raise ValueError("Visibility must be private or public.")
    if not 1 <= len(app_name.strip()) <= 80 or not 1 <= len(description.strip()) <= 200:
        raise ValueError("App name or description length is invalid.")
    for value in (app_name, description):
        if any(ord(char) < 32 or ord(char) == 127 for char in value):
            raise ValueError("Control characters are not allowed.")


def render(app_name: str, repo_name: str, description: str, visibility: str) -> dict[str, str]:
    """Render in memory. Caller is responsible for choosing a safe destination."""
    validate(app_name, repo_name, description, visibility)
    mapping = {
        "%%APP_NAME_MD%%": markdown_text(app_name.strip()),
        "%%DESCRIPTION_MD%%": markdown_text(description.strip()),
        "%%APP_NAME_HTML%%": html.escape(app_name.strip(), quote=True),
        "%%DESCRIPTION_HTML%%": html.escape(description.strip(), quote=True),
        "%%REPO_NAME%%": repo_name,
        "%%VISIBILITY%%": visibility,
    }
    rendered = {}
    for destination in TEMPLATE_PATHS:
        source = TEMPLATE_ROOT / (destination + ".tpl")
        content = source.read_text(encoding="utf-8")
        for key, value in mapping.items():
            content = content.replace(key, value)
        if PLACEHOLDER.search(content):
            raise ValueError(f"Unresolved template placeholder: {destination}")
        rendered[destination] = content
    return rendered


def write_new_directory(destination: Path, files: dict[str, str]) -> None:
    """Refuse to overwrite an existing directory (including a real repository)."""
    if destination.exists() or destination.is_symlink():
        raise FileExistsError("Output directory already exists; refusing to overwrite.")
    destination.mkdir(parents=True, exist_ok=False)
    for path, content in files.items():
        target = destination / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app-name", required=True)
    parser.add_argument("--repo-name", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--visibility", choices=("private", "public"), default="private")
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    try:
        files = render(args.app_name, args.repo_name, args.description, args.visibility)
        write_new_directory(args.out_dir, files)
    except (ValueError, FileExistsError, OSError) as exc:
        parser.error(str(exc))
    print(f"Generated {len(files)} starter files; no remote repositories were modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
