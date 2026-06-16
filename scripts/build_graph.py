#!/usr/bin/env python3
"""Build a static ESIIL metadata graph and theme exploration pages."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_ROOT = REPO_ROOT / "registry"
DATA_PATH = REPO_ROOT / "data" / "org_repos.json"
GRAPH_OUTPUT_PATH = REPO_ROOT / "docs" / "assets" / "data" / "esiil_graph.json"
EXPLORE_ROOT = REPO_ROOT / "docs" / "explore"
THEMES_ROOT = EXPLORE_ROOT / "themes"

PROJECT_REQUIRED_FIELDS = {
    "id",
    "title",
    "description",
    "type",
    "status",
    "website",
    "repository",
    "people",
    "themes",
    "datasets",
    "methods",
    "outputs",
    "related_projects",
}


class GraphValidationError(Exception):
    """Raised when registry content fails validation."""


@dataclass(frozen=True)
class Entity:
    kind: str
    data: dict[str, Any]
    source_path: Path

    @property
    def id(self) -> str:
        return str(self.data["id"])


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def load_yaml_documents(directory: Path, kind: str) -> list[Entity]:
    if not directory.exists():
        return []
    entities: list[Entity] = []
    for path in sorted(list(directory.glob("*.yaml")) + list(directory.glob("*.yml"))):
        raw = yaml.safe_load(path.read_text()) or {}
        if not isinstance(raw, dict):
            raise GraphValidationError(f"{path} must contain a YAML mapping.")
        entities.append(Entity(kind=kind, data=raw, source_path=path))
    return entities


def validate_project(entity: Entity) -> None:
    missing = sorted(PROJECT_REQUIRED_FIELDS - set(entity.data))
    if missing:
        raise GraphValidationError(
            f"{entity.source_path} is missing required fields: {', '.join(missing)}"
        )
    for field in ("people", "themes", "datasets", "methods", "outputs", "related_projects"):
        if not isinstance(entity.data.get(field), list):
            raise GraphValidationError(f"{entity.source_path} field '{field}' must be a list.")


def validate_support_entity(entity: Entity, label_field: str) -> None:
    for field in ("id", label_field):
        if field not in entity.data:
            raise GraphValidationError(
                f"{entity.source_path} is missing required field '{field}'."
            )


def load_registry(registry_root: Path) -> dict[str, list[Entity]]:
    registry = {
        "project": load_yaml_documents(registry_root / "projects", "project"),
        "person": load_yaml_documents(registry_root / "people", "person"),
        "theme": load_yaml_documents(registry_root / "themes", "theme"),
        "dataset": load_yaml_documents(registry_root / "datasets", "dataset"),
    }

    for project in registry["project"]:
        validate_project(project)
    for person in registry["person"]:
        validate_support_entity(person, "name")
    for theme in registry["theme"]:
        validate_support_entity(theme, "title")
    for dataset in registry["dataset"]:
        validate_support_entity(dataset, "title")

    seen_ids: dict[str, Path] = {}
    for entities in registry.values():
        for entity in entities:
            if entity.id in seen_ids:
                raise GraphValidationError(
                    f"Duplicate id '{entity.id}' in {entity.source_path} and {seen_ids[entity.id]}"
                )
            seen_ids[entity.id] = entity.source_path

    return registry


def load_org_repos(data_path: Path) -> list[dict[str, Any]]:
    if not data_path.exists():
        return []
    payload = json.loads(data_path.read_text() or "[]")
    if not isinstance(payload, list):
        raise GraphValidationError(f"{data_path} must contain a JSON array.")
    return payload


def ensure_references(registry: dict[str, list[Entity]]) -> None:
    project_ids = {entity.id for entity in registry["project"]}
    person_ids = {entity.id for entity in registry["person"]}
    theme_ids = {entity.id for entity in registry["theme"]}
    dataset_ids = {entity.id for entity in registry["dataset"]}

    for project in registry["project"]:
        for ref in project.data["people"]:
            if ref not in person_ids:
                raise GraphValidationError(
                    f"{project.source_path} references missing person '{ref}'."
                )
        for ref in project.data["themes"]:
            if ref not in theme_ids:
                raise GraphValidationError(
                    f"{project.source_path} references missing theme '{ref}'."
                )
        for ref in project.data["datasets"]:
            if ref not in dataset_ids:
                raise GraphValidationError(
                    f"{project.source_path} references missing dataset '{ref}'."
                )
        for ref in project.data["related_projects"]:
            if ref not in project_ids:
                raise GraphValidationError(
                    f"{project.source_path} references missing project '{ref}'."
                )


def make_node(kind: str, entity_id: str, label: str, **attributes: Any) -> dict[str, Any]:
    payload = {"id": f"{kind}:{entity_id}", "type": kind, "label": label}
    payload.update(attributes)
    return payload


def add_edge(edges: list[dict[str, str]], source: str, target: str, edge_type: str) -> None:
    edges.append({"source": source, "target": target, "type": edge_type})


def repo_key_from_url(url: str) -> str:
    return slugify(url.rstrip("/").split("/")[-1] or url)


def build_graph(
    registry_root: Path = REGISTRY_ROOT,
    data_path: Path = DATA_PATH,
    output_path: Path = GRAPH_OUTPUT_PATH,
    explore_root: Path = EXPLORE_ROOT,
) -> dict[str, Any]:
    registry = load_registry(registry_root)
    ensure_references(registry)
    org_repos = load_org_repos(data_path)

    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, str]] = []
    nodes_by_id: set[str] = set()

    def upsert_node(node: dict[str, Any]) -> None:
        if node["id"] in nodes_by_id:
            return
        nodes.append(node)
        nodes_by_id.add(node["id"])

    project_lookup = {entity.id: entity for entity in registry["project"]}
    people_lookup = {entity.id: entity for entity in registry["person"]}
    theme_lookup = {entity.id: entity for entity in registry["theme"]}
    dataset_lookup = {entity.id: entity for entity in registry["dataset"]}

    for person in registry["person"]:
        upsert_node(
            make_node(
                "person",
                person.id,
                person.data["name"],
                role=person.data.get("role", ""),
                website=person.data.get("website", ""),
            )
        )

    for theme in registry["theme"]:
        upsert_node(
            make_node(
                "theme",
                theme.id,
                theme.data["title"],
                description=theme.data.get("description", ""),
            )
        )

    for dataset in registry["dataset"]:
        upsert_node(
            make_node(
                "dataset",
                dataset.id,
                dataset.data["title"],
                description=dataset.data.get("description", ""),
                website=dataset.data.get("website", ""),
            )
        )

    repo_nodes_by_url: dict[str, str] = {}
    for repo in org_repos:
        repo_url = repo.get("url", "")
        repo_name = repo.get("name", "")
        if not repo_url or not repo_name:
            continue
        repo_id = repo_key_from_url(repo_name)
        node_id = f"repo:{repo_id}"
        upsert_node(
            make_node(
                "repo",
                repo_id,
                repo_name,
                url=repo_url,
                description=repo.get("description") or "",
                homepage=repo.get("homepageUrl") or "",
                topics=repo.get("repositoryTopics") or [],
                is_archived=repo.get("isArchived", False),
                is_fork=repo.get("isFork", False),
            )
        )
        repo_nodes_by_url[repo_url.rstrip("/")] = node_id

    for project in registry["project"]:
        project_node_id = f"project:{project.id}"
        upsert_node(
            make_node(
                "project",
                project.id,
                project.data["title"],
                description=project.data["description"],
                project_type=project.data["type"],
                status=project.data["status"],
                cohort=project.data.get("cohort", ""),
                website=project.data["website"],
                repository=project.data["repository"],
            )
        )

        if project.data["repository"]:
            repo_url = project.data["repository"].rstrip("/")
            repo_node_id = repo_nodes_by_url.get(repo_url)
            if not repo_node_id:
                repo_id = repo_key_from_url(repo_url)
                repo_node_id = f"repo:{repo_id}"
                upsert_node(
                    make_node(
                        "repo",
                        repo_id,
                        repo_url.split("/")[-1],
                        url=repo_url,
                    )
                )
            add_edge(edges, project_node_id, repo_node_id, "HAS_REPO")

        if project.data["website"]:
            website_id = slugify(project.data["website"])
            website_node_id = f"website:{website_id}"
            upsert_node(
                make_node(
                    "website",
                    website_id,
                    project.data["title"],
                    url=project.data["website"],
                )
            )
            add_edge(edges, project_node_id, website_node_id, "HAS_WEBSITE")

        for person_id in project.data["people"]:
            add_edge(edges, project_node_id, f"person:{person_id}", "HAS_PERSON")
            add_edge(edges, f"person:{person_id}", project_node_id, "CONTRIBUTED_TO")

        for theme_id in project.data["themes"]:
            add_edge(edges, project_node_id, f"theme:{theme_id}", "HAS_THEME")

        for dataset_id in project.data["datasets"]:
            add_edge(edges, project_node_id, f"dataset:{dataset_id}", "USES_DATASET")

        for method in project.data["methods"]:
            method_id = slugify(method)
            upsert_node(make_node("method", method_id, method))
            add_edge(edges, project_node_id, f"method:{method_id}", "USES_METHOD")

        for output in project.data["outputs"]:
            output_id = slugify(output)
            upsert_node(make_node("output", output_id, output))
            add_edge(edges, project_node_id, f"output:{output_id}", "HAS_OUTPUT")

        for related_id in project.data["related_projects"]:
            add_edge(edges, project_node_id, f"project:{related_id}", "RELATED_TO")

    graph = {
        "nodes": sorted(nodes, key=lambda item: item["id"]),
        "edges": sorted(
            edges, key=lambda item: (item["source"], item["type"], item["target"])
        ),
        "meta": {
            "project_count": len(registry["project"]),
            "person_count": len(registry["person"]),
            "theme_count": len(registry["theme"]),
            "dataset_count": len(registry["dataset"]),
            "repo_count": len([node for node in nodes if node["type"] == "repo"]),
        },
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(graph, indent=2, sort_keys=True) + "\n")
    generate_theme_pages(
        registry=registry,
        graph=graph,
        project_lookup=project_lookup,
        people_lookup=people_lookup,
        theme_lookup=theme_lookup,
        dataset_lookup=dataset_lookup,
        explore_root=explore_root,
    )
    return graph


def generate_theme_pages(
    registry: dict[str, list[Entity]],
    graph: dict[str, Any],
    project_lookup: dict[str, Entity],
    people_lookup: dict[str, Entity],
    theme_lookup: dict[str, Entity],
    dataset_lookup: dict[str, Entity],
    explore_root: Path,
) -> None:
    themes_root = explore_root / "themes"
    themes_root.mkdir(parents=True, exist_ok=True)

    for theme in registry["theme"]:
        projects = [
            project
            for project in registry["project"]
            if theme.id in project.data["themes"]
        ]
        people = sorted(
            {
                people_lookup[person_id].data["name"]
                for project in projects
                for person_id in project.data["people"]
            }
        )
        datasets = sorted(
            {
                dataset_lookup[dataset_id].data["title"]
                for project in projects
                for dataset_id in project.data["datasets"]
            }
        )
        outputs = sorted(
            {
                output
                for project in projects
                for output in project.data["outputs"]
            }
        )
        repos = sorted(
            {
                project.data["repository"]
                for project in projects
                if project.data["repository"]
            }
        )
        websites = sorted(
            {
                project.data["website"]
                for project in projects
                if project.data["website"]
            }
        )

        lines = [
            "---",
            f"title: {theme.data['title']}",
            "---",
            "",
            f"# {theme.data['title']}",
            "",
            theme.data.get("description", ""),
            "",
            "## Connected Projects",
            "",
        ]
        if projects:
            for project in projects:
                destination = project.data["website"] or project.data["repository"] or "#"
                lines.extend(
                    [
                        f"- [{project.data['title']}]({destination}): {project.data['description']}",
                    ]
                )
        else:
            lines.append("- None currently registered.")

        lines.extend(["", "## Repositories", ""])
        lines.extend([f"- [{repo}]({repo})" for repo in repos] or ["- None currently registered."])

        lines.extend(["", "## Websites", ""])
        lines.extend(
            [f"- [{website}]({website})" for website in websites]
            or ["- None currently registered."]
        )

        lines.extend(["", "## People", ""])
        lines.extend([f"- {person}" for person in people] or ["- None currently registered."])

        lines.extend(["", "## Datasets", ""])
        lines.extend(
            [f"- {dataset}" for dataset in datasets] or ["- None currently registered."]
        )

        lines.extend(["", "## Outputs", ""])
        lines.extend([f"- {output}" for output in outputs] or ["- None currently registered."])

        theme_path = themes_root / f"{theme.id}.md"
        theme_path.write_text("\n".join(lines) + "\n")

    index_lines = [
        "---",
        "title: Theme Network",
        "---",
        "",
        "# Theme Network",
        "",
        "Browse cross-cutting ESIIL themes generated from the registry.",
        "",
    ]
    for theme in registry["theme"]:
        index_lines.append(f"- [{theme.data['title']}]({theme.id}.md)")
    (themes_root / "index.md").write_text("\n".join(index_lines) + "\n")


def main() -> int:
    try:
        build_graph()
    except GraphValidationError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(f"Wrote graph to {GRAPH_OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
