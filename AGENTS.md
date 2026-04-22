# AGENTS.md

This file is the operating manual for AI/code agents working in the OASIS home
repository.

## 1. What This Repository Is

OASIS is the public-facing documentation and homepage for the **Open Analysis
and Synthesis Infrastructure for Science**. It is also the central repository
for ESIIL activities, even though the broader ESIIL ecosystem extends beyond
this repo into companion platforms. In practice, this repository serves several
roles at once:

- The main OASIS landing page and discovery surface.
- The central coordination and documentation repo for ESIIL activities.
- A curated onboarding hub for environmental data science tools and workflows.
- A documentation site for quickstarts, CyVerse/cloud collaboration patterns,
  containers, and support resources.
- A visibility layer for ESIIL working groups, postdocs, students, events, and
  related project hubs.

This repository is paired with:

- a network portal where users can deploy resources and computational
  environments
- a persistent data store where users can keep large datasets and outputs

Agents should understand the repo as the documentation, navigation, and
coordination layer across that larger system, not as the entire system itself.

This is not just a generic marketing site. It is an operational knowledge hub
for a research community that values:

- Open science and reproducibility.
- Durable links to project hubs and external companion sites.
- Low-friction onboarding for new users.
- Clear, approachable documentation.
- Stable homepage behavior despite frequent content curation.

## 2. Primary Audiences

When making changes, optimize for these users:

- Newcomers who need a clear first path into OASIS, CyVerse, GitHub, data, and
  analytics workflows.
- ESIIL staff and collaborators maintaining project links, event buttons, and
  support documentation.
- Working groups, postdocs, students, and partner teams who rely on OASIS to
  surface their public-facing project sites.
- Contributors who need predictable structure, tagging, and site behavior.

## 3. Repo-wide Operating Principles

### Preserve the homepage as a curated front door

`docs/index.md` is the highest-visibility file in the repo. Changes there should
prioritize:

- Clear scanning and discoverability.
- Consistent button/card patterns.
- Stable layout across desktop and mobile.
- Safe integration of many external project links.

### Prefer consistency over novelty

This repo already has strong visual and structural patterns. Reuse the existing
button/card/grid conventions unless the user explicitly asks for a redesign.

### Make documentation durable

Favor edits that improve clarity, navigation, and maintainability. Avoid adding
one-off structures that future maintainers will have to reverse-engineer.

### Keep generated content and source-of-truth files straight

Some files are generated or partially generated. Agents should edit the source
of truth whenever possible and avoid hand-editing generated outputs unless
needed to finish the task.

## 4. Important File Boundaries

### Core site configuration

- `mkdocs.yml`: site navigation, theme, plugins, assets, and build behavior.
- `.github/workflows/gh-pages.yml`: strict build + deploy.
- `.github/workflows/playwright.yml`: homepage/browser smoke testing.

### Homepage and layout

- `docs/index.md`: homepage content and many inline layout/card sections.
- `docs/dev/oasis-site-dev-guide.md`: canonical homepage layout safety guide.
- `docs/styles/extra.css`: final-authority brand/visual styling layer.
- `docs/assets/css/style.css`: structural compatibility glue only.
- `docs/overrides/main.html` and `overrides/main.html`: MkDocs Material
  overrides; edit carefully and minimally.

### Content sections

- `docs/quickstart/`: onboarding guides and structured quickstarts.
- `docs/resources/`: reference and support material.
- `docs/container-library/`: container documentation.
- `docs/tags/`: generated tag pages; do not hand-curate unless absolutely
  necessary.

### Development/schedule tracking

- `docs/dev-schedule.md`: archived/historical schedule page.
- `docs/pending-tasks.md`: living follow-up list for unfinished work.
- `docs/upcoming_tasks.yaml`: schedule source for automated schedule refreshes.
- `scripts/update_dev_schedule.py`: updates the upcoming-task block and mermaid
  gantt block in `docs/dev-schedule.md`.

### Repo structure and submodules

- `docs/analytics-library/` is a Git submodule pointing at another repository.
  Do not edit it unless the user explicitly wants submodule work.

## 5. Homepage Safety Rules

Before editing homepage structure or layout CSS, read:

- [`docs/dev/oasis-site-dev-guide.md`](docs/dev/oasis-site-dev-guide.md)

That guide is the canonical source for homepage layout rules. The most
important constraints are:

- Keep the homepage hero inside `.oasis-layout > .oasis-main`.
- Scope homepage-only layout changes with `.oasis-layout`.
- Do **not** use `:has()` for homepage scoping.
- Do **not** reintroduce `100vw` full-bleed hero tricks or
  `calc(50% - 50vw)`-style layout hacks.
- Put visual/brand changes in `docs/styles/extra.css`.
- Put structural compatibility glue only in `docs/assets/css/style.css`.

If you touch homepage sections, prefer existing classes:

- `.library-item`
- `.gallery-item`
- `.template-item`
- `.template-gallery`

When adding new cards or buttons, match the surrounding section’s established
pattern instead of inventing a new component.

## 6. Content Standards

### Front matter and tags

For curated content pages, especially under:

- `docs/quickstart/`
- `docs/container-library/`

include YAML front matter with at least:

```yaml
---
title: Your Page Title
tags: [tag1, tag2]
date: 2026-04-21
---
```

`scripts/check_front_matter.py` and pre-commit enforce `tags` and `date` for
those areas.

For other documentation, add front matter when the page should participate in
tag-based discovery or date-driven sorting.

### Generated tag pages

`scripts/generate_tags.py` rebuilds `docs/tags/index.md` and per-tag pages from
front matter. Treat `docs/tags/` as generated output. Prefer editing source
pages and rerunning the generator rather than hand-editing tag pages.

### Writing tone

The repository’s user-facing documentation tends to be:

- welcoming and instructional
- concrete and procedural
- open-science oriented
- friendly to beginners without being shallow

Match that tone in new docs and edits.

### External links

This repo intentionally links out to many external project hubs. When updating
homepage cards or docs:

- use the canonical live URL when known
- prefer consistency in card text
- remove “site unavailable” notes once a live site exists
- note placeholder images/descriptions when final assets are not available yet

## Button Image Generation Rules

All agents, including Codex, MUST read
[`docs/button-image-guidelines.md`](docs/button-image-guidelines.md) before
generating, replacing, or modifying any button image.

The guideline is authoritative over default image generation behavior. Agents
must match the existing visual family before creating new assets.

Do not generate button images using generic AI defaults. Always follow the
repository image guidelines. If there is a conflict, the guidelines take
precedence.

If uncertain, agents should:

- inspect existing button images
- inspect the linked destination page or repository README when available
- choose simpler compositions
- avoid introducing new styles

When:

- a new homepage section is added
- a new library or feature needs a button
- an existing button is replaced

the agent must:

1. Read the guideline file.
2. Inspect the linked page or repository README when available, then derive an
   appropriate subject from the content.
3. Use the prompt template defined in the guideline.
4. Save the image using the correct path and naming convention.
5. Verify visual consistency before committing.

## 7. Build, Test, and Validation Expectations

### Preferred validation

Run the narrowest useful validation for the change:

- Full site sanity check:
  - `mkdocs build --strict`
- Homepage interaction/layout smoke test:
  - `npm install`
  - `npx playwright test`
- Front matter validation for changed curated docs:
  - `pre-commit run --files <changed-files>`

### Schedule-specific validation

For schedule changes:

- update `docs/upcoming_tasks.yaml` first when appropriate
- then run:
  - `python scripts/update_dev_schedule.py`

Important caveat:

- the script updates the upcoming-task block and mermaid gantt block in
  `docs/dev-schedule.md`
- it does **not** update the historical task list, the timeline table, or the
  static homepage image `docs/gantt_chart.png`

If the local environment is missing `PyYAML`, note that explicitly in your
handoff.

## 8. Known Repo Constraints and Pitfalls

- `docs/index.md` is large and mixes Markdown, inline HTML, and inline CSS.
  Read locally around the section you are editing before patching.
- The homepage contains repeated card-grid patterns with subtle differences;
  use the local section’s existing structure, not a nearby section by default.
- `docs/gantt_chart.png` is a static asset and can drift from
  `docs/dev-schedule.md`.
- `docs/analytics-library/` may appear modified independently because it is a
  submodule; do not “clean it up” unless asked.
- GitHub Pages deploys under `/home/`, but `mkdocs serve` runs locally at `/`.

## 9. Agent Workflow Expectations

When working in this repository:

1. Read the relevant surrounding files before editing.
2. Prefer source-of-truth updates over superficial output edits.
3. Preserve established homepage patterns unless a redesign is requested.
4. Validate proportionally to the risk of the change.
5. Record substantial agent work in `PROMPT_LOG.md`.

“Substantial” usually means:

- architectural or layout changes
- new process/contributor docs
- schedule/automation updates
- changes affecting multiple homepage sections
- changes that introduce new repo conventions

## 10. Prompt Log Policy

`PROMPT_LOG.md` is a lightweight repository memory for agent-led work. Append an
entry when you do substantial work. Each entry should include:

- date
- agent/user goal
- repo context reviewed
- major files changed
- validation performed
- unresolved follow-ups or assumptions

Keep entries concise and practical. The goal is continuity for future agents,
not exhaustive transcripts.
