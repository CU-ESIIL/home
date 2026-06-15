#!/usr/bin/env python3
"""Build the static homepage stats band from local OASIS metadata.

The stats band intentionally combines manual program metrics with conservative
generated counts. Compute hours remain a manual external-infrastructure metric.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "data" / "oasis_stats_config.yml"
ORG_REPOS_PATH = ROOT / "data" / "org_repos.json"
PROJECT_REGISTRY = ROOT / "registry" / "projects"
OUTPUT_JSON = ROOT / "docs" / "assets" / "data" / "oasis_stats.json"
OUTPUT_PARTIAL = ROOT / "docs" / "overrides" / "partials" / "stats_bar.html"


class OasisStatsError(Exception):
    """Raised when the stats config cannot be converted into homepage output."""


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise OasisStatsError(f"Missing stats config: {path}")

    with path.open("r", encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle) or {}

    if not isinstance(loaded, dict):
        raise OasisStatsError(f"Expected a mapping in {path}")

    return loaded


def load_org_repos(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)

    if not isinstance(loaded, list):
        raise OasisStatsError(f"Expected a list in {path}")

    return [repo for repo in loaded if isinstance(repo, dict)]


def parse_threshold(value: str | None) -> int | None:
    if not value:
        return None

    match = re.search(r"\d+", value)
    if not match:
        return None

    return int(match.group(0))


def format_count(count: int) -> str:
    return f"{count:,}"


def active_org_repos(repos: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [repo for repo in repos if not repo.get("isArchived", False)]


def collect_registry_websites(projects_dir: Path) -> set[str]:
    websites: set[str] = set()

    if not projects_dir.exists():
        return websites

    for path in sorted(projects_dir.glob("*.y*ml")):
        with path.open("r", encoding="utf-8") as handle:
            project = yaml.safe_load(handle) or {}

        if not isinstance(project, dict):
            continue

        website = str(project.get("website") or "").strip()
        if website and website != "#":
            websites.add(website)

    return websites


def generated_repository_value(config: dict[str, Any], repos: list[dict[str, Any]]) -> tuple[str, bool]:
    fallback = str(config.get("fallback_value") or "")
    active_repos = active_org_repos(repos)

    if active_repos:
        return format_count(len(active_repos)), True

    return fallback, False


def generated_website_value(
    config: dict[str, Any],
    repos: list[dict[str, Any]],
    registry_websites: set[str],
) -> tuple[str, bool]:
    fallback = str(config.get("fallback_value") or "")
    reliable_threshold = parse_threshold(fallback)
    websites = set(registry_websites)

    for repo in active_org_repos(repos):
        homepage = str(repo.get("homepageUrl") or "").strip()
        if homepage and homepage != "#":
            websites.add(homepage)

    # Registry-only counts are useful internally but incomplete as a public
    # program metric. Use them only once they meet the configured fallback scale.
    if websites and (reliable_threshold is None or len(websites) >= reliable_threshold):
        return format_count(len(websites)), True

    return fallback, False


def build_stats(config: dict[str, Any]) -> list[dict[str, Any]]:
    manual_stats = config.get("manual_stats")
    if not isinstance(manual_stats, dict):
        raise OasisStatsError("Expected manual_stats mapping in stats config")

    repos = load_org_repos(ORG_REPOS_PATH)
    registry_websites = collect_registry_websites(PROJECT_REGISTRY)

    ordered_ids = [
        "working_groups",
        "events",
        "dois",
        "websites",
        "repositories",
        "compute_hours",
    ]
    stats: list[dict[str, Any]] = []

    for stat_id in ordered_ids:
        stat_config = manual_stats.get(stat_id)
        if not isinstance(stat_config, dict):
            raise OasisStatsError(f"Missing config for stat: {stat_id}")

        generated = False
        if stat_id == "repositories":
            value, generated = generated_repository_value(stat_config, repos)
        elif stat_id == "websites":
            value, generated = generated_website_value(stat_config, repos, registry_websites)
        else:
            value = str(stat_config.get("value") or "")

        if not value:
            raise OasisStatsError(f"Missing value for stat: {stat_id}")

        stats.append(
            {
                "id": stat_id.replace("_", "-"),
                "value": value,
                "label": str(stat_config.get("label") or ""),
                "href": str(stat_config.get("href") or ""),
                "source_note": str(stat_config.get("source_note") or ""),
                "generated": generated,
            }
        )

    return stats


def write_json(stats: list[dict[str, Any]]) -> None:
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_by": "scripts/build_oasis_stats.py",
        "stats": stats,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_stat(stat: dict[str, Any]) -> str:
    value = html.escape(stat["value"])
    label = html.escape(stat["label"])
    href = stat.get("href", "")
    content = (
        f'      <span class="oasis-stat__value">{value}</span>\n'
        f'      <span class="oasis-stat__label">{label}</span>'
    )

    if href and href != "#":
        escaped_href = html.escape(href, quote=True)
        external = href.startswith(("http://", "https://"))
        attrs = ' target="_blank" rel="noopener"' if external else ""
        return f'    <a class="oasis-stat" href="{escaped_href}"{attrs}>\n{content}\n    </a>'

    return f'    <div class="oasis-stat" role="group" aria-label="{label}">\n{content}\n    </div>'


def write_partial(stats: list[dict[str, Any]]) -> None:
    rendered_stats = "\n".join(render_stat(stat) for stat in stats)
    partial = f"""<section class="oasis-stats-band" aria-labelledby="oasis-stats-heading">
  <div class="oasis-shell">
    <div class="oasis-stats-band__panel" data-reveal>
      <div class="oasis-stats-band__intro">
        <h2 id="oasis-stats-heading">ESIIL science at scale</h2>
        <p>A living gallery of projects, events, open outputs, and shared infrastructure.</p>
      </div>
      <div class="oasis-stats-band__grid" aria-label="OASIS program metrics">
{rendered_stats}
      </div>
    </div>
  </div>
</section>
"""
    OUTPUT_PARTIAL.write_text(partial, encoding="utf-8")


def build_oasis_stats() -> list[dict[str, Any]]:
    config = load_yaml(CONFIG_PATH)
    stats = build_stats(config)
    write_json(stats)
    write_partial(stats)
    return stats


if __name__ == "__main__":
    build_oasis_stats()
    print(f"Wrote {OUTPUT_JSON.relative_to(ROOT)}")
    print(f"Wrote {OUTPUT_PARTIAL.relative_to(ROOT)}")
