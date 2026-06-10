---
title: Explore the ESIIL Network
---

# Explore the ESIIL Network

This section is the first static metadata-graph layer for the CU-ESIIL
organization. It connects projects, events, libraries, people, datasets,
methods, and outputs without introducing a hosted service or database.

Use it to move laterally across the ecosystem rather than navigating one
repository at a time.

## What this is

- A static graph built from YAML registry files in this repository
- A lightweight way to describe how projects, datasets, themes, and outputs fit
  together
- A foundation for future browse, search, and visualization features

## Start with themes

- [Theme Network](themes/index.md)
- [Data Infrastructure](themes/data-infrastructure.md)
- [Environmental AI](themes/environmental-ai.md)
- [Events & Summits](themes/events.md)
- [Synthesis & Collaboration](themes/synthesis-collaboration.md)
- [Wildfire](themes/wildfire.md)

## How it is built

- Source metadata lives under `registry/`
- Repository discovery can be refreshed with `scripts/discover_org_repos.py`
- The graph and generated pages are rebuilt with `scripts/build_graph.py`

This first version is intentionally boring, reliable, and easy to extend.
