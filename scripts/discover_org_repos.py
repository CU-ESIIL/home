#!/usr/bin/env python3
"""Discover public CU-ESIIL repositories via GitHub CLI."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "data" / "org_repos.json"
GH_FIELDS = (
    "name,url,description,homepageUrl,repositoryTopics,isArchived,isFork"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Discover CU-ESIIL organization repositories."
    )
    parser.add_argument(
        "--include-archived",
        action="store_true",
        help="Include archived repositories in the exported JSON.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=OUTPUT_PATH,
        help="Path to write the discovered repository JSON.",
    )
    return parser.parse_args()


def discover_repositories(include_archived: bool = False) -> list[dict]:
    gh_path = shutil.which("gh")
    if not gh_path:
        print("GitHub CLI not found; writing empty repository list.", file=sys.stderr)
        return []

    command = [
        gh_path,
        "repo",
        "list",
        "CU-ESIIL",
        "--limit",
        "1000",
        "--json",
        GH_FIELDS,
    ]
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"gh repo list failed: {message}")

    repositories = json.loads(result.stdout)
    if include_archived:
        return repositories
    return [repo for repo in repositories if not repo.get("isArchived", False)]


def write_output(output_path: Path, repositories: list[dict]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(repositories, indent=2, sort_keys=True) + "\n")


def main() -> int:
    args = parse_args()
    repositories = discover_repositories(include_archived=args.include_archived)
    write_output(args.output, repositories)
    print(f"Wrote {len(repositories)} repositories to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
