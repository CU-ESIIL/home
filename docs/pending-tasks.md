---
tags: [development]
date: 2025-08-29
---

# Pending Development Tasks

Some items from the development schedule remain outstanding. The notes below outline recommended steps for completing them.

## Interactive Cloud Triangle lesson

1. Design interactive plots using libraries such as Plotly or Altair to illustrate the Cloud Triangle concept.
2. Host the interactive components as standalone HTML or within Jupyter notebooks and integrate them into the documentation with `mkdocs-jupyter` or embedded iframes.
3. Provide explanatory text and data sources alongside the interactive elements.
4. Link the lesson to the existing Cloud Triangle overview and examples pages.

## Further automation

- Enhance `scripts/update_dev_schedule.py` to fetch issue titles and status directly from the GitHub API.
- Extend the script to update the timeline table in `docs/dev-schedule.md` for a fully automated roadmap.

Running `python scripts/update_dev_schedule.py` will rebuild the upcoming task list and planned Gantt section from `docs/upcoming_tasks.yaml`.
