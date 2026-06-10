from __future__ import annotations

import json
from pathlib import Path

import yaml

from scripts.build_graph import GraphValidationError, build_graph


def write_yaml(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False))


def make_registry(root: Path) -> tuple[Path, Path, Path]:
    registry_root = root / "registry"
    data_path = root / "data" / "org_repos.json"
    output_path = root / "docs" / "assets" / "data" / "esiil_graph.json"
    explore_root = root / "docs" / "explore"

    write_yaml(
        registry_root / "people" / "staff.yaml",
        {"id": "staff", "name": "Staff", "role": "Team", "website": ""},
    )
    write_yaml(
        registry_root / "themes" / "theme.yaml",
        {"id": "theme", "title": "Theme", "description": "Theme description"},
    )
    write_yaml(
        registry_root / "datasets" / "dataset.yaml",
        {
            "id": "dataset",
            "title": "Dataset",
            "description": "Dataset description",
            "website": "",
        },
    )
    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text("[]\n")
    return registry_root, data_path, output_path, explore_root


def test_build_graph_generates_json_and_theme_pages(tmp_path: Path) -> None:
    registry_root, data_path, output_path, explore_root = make_registry(tmp_path)
    write_yaml(
        registry_root / "projects" / "project.yaml",
        {
            "id": "project",
            "title": "Project",
            "description": "Project description",
            "type": "working-group",
            "status": "active",
            "website": "https://example.org/project",
            "repository": "https://github.com/CU-ESIIL/project",
            "people": ["staff"],
            "themes": ["theme"],
            "datasets": ["dataset"],
            "methods": ["analysis"],
            "outputs": ["documentation"],
            "related_projects": [],
        },
    )

    graph = build_graph(
        registry_root=registry_root,
        data_path=data_path,
        output_path=output_path,
        explore_root=explore_root,
    )

    assert output_path.exists()
    payload = json.loads(output_path.read_text())
    assert payload["meta"]["project_count"] == 1
    assert any(node["id"] == "project:project" for node in payload["nodes"])
    assert (explore_root / "themes" / "theme.md").exists()
    assert graph["meta"]["theme_count"] == 1


def test_duplicate_id_detection(tmp_path: Path) -> None:
    registry_root, data_path, output_path, explore_root = make_registry(tmp_path)
    write_yaml(
        registry_root / "projects" / "project-a.yaml",
        {
            "id": "duplicate",
            "title": "Project A",
            "description": "Project A description",
            "type": "working-group",
            "status": "active",
            "website": "",
            "repository": "",
            "people": ["staff"],
            "themes": ["theme"],
            "datasets": ["dataset"],
            "methods": [],
            "outputs": [],
            "related_projects": [],
        },
    )
    write_yaml(
        registry_root / "projects" / "project-b.yaml",
        {
            "id": "duplicate",
            "title": "Project B",
            "description": "Project B description",
            "type": "working-group",
            "status": "active",
            "website": "",
            "repository": "",
            "people": ["staff"],
            "themes": ["theme"],
            "datasets": ["dataset"],
            "methods": [],
            "outputs": [],
            "related_projects": [],
        },
    )

    try:
        build_graph(
            registry_root=registry_root,
            data_path=data_path,
            output_path=output_path,
            explore_root=explore_root,
        )
    except GraphValidationError as exc:
        assert "Duplicate id 'duplicate'" in str(exc)
    else:
        raise AssertionError("Expected duplicate id validation error.")


def test_missing_reference_detection(tmp_path: Path) -> None:
    registry_root, data_path, output_path, explore_root = make_registry(tmp_path)
    write_yaml(
        registry_root / "projects" / "project.yaml",
        {
            "id": "project",
            "title": "Project",
            "description": "Project description",
            "type": "working-group",
            "status": "active",
            "website": "",
            "repository": "",
            "people": ["missing-person"],
            "themes": ["theme"],
            "datasets": ["dataset"],
            "methods": [],
            "outputs": [],
            "related_projects": [],
        },
    )

    try:
        build_graph(
            registry_root=registry_root,
            data_path=data_path,
            output_path=output_path,
            explore_root=explore_root,
        )
    except GraphValidationError as exc:
        assert "missing person 'missing-person'" in str(exc)
    else:
        raise AssertionError("Expected missing reference validation error.")
