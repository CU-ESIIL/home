---
tags: [development]
date: 2026-04-21
---

# Pending Development Tasks

The original 2025 launch roadmap is largely complete. The remaining follow-up work is mostly automation and a small amount of homepage polish.

## Schedule automation follow-ups

- Enhance `scripts/update_dev_schedule.py` to fetch issue titles and status directly from the GitHub API instead of relying only on `docs/upcoming_tasks.yaml`.
- Extend the script to update the timeline table in `docs/dev-schedule.md` for a fully automated roadmap.

## Homepage follow-up polish

- Replace placeholder thumbnails and placeholder descriptions on newly added homepage cards as project teams publish final artwork and summaries.
- If the homepage development schedule tile should mirror the current roadmap exactly, regenerate or replace `docs/gantt_chart.png`, because the live schedule page is updated separately from that static image.

Running `python scripts/update_dev_schedule.py` will rebuild the upcoming task list and planned Gantt section from `docs/upcoming_tasks.yaml`, but it still does not update the historical task list, the timeline table, or the homepage thumbnail image.
