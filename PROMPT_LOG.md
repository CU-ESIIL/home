# Prompt Log

This file records substantial AI/agent prompts and outcomes for the OASIS home
repository.

Use it as lightweight working memory for future maintenance, especially when a
task establishes new conventions, updates repo process, or changes multiple
homepage sections.

## Entry template

```md
## YYYY-MM-DD

- Goal:
- Context reviewed:
- Files changed:
- Validation:
- Follow-up / unresolved:
```

## 2026-04-21

- Goal: Create a repository-specific `AGENTS.md` and establish a reusable prompt
  log format grounded in the actual OASIS repo rather than generic agent rules.
- Context reviewed: `README.md`, `CONTRIBUTING.md`, `mkdocs.yml`,
  `docs/dev/oasis-site-dev-guide.md`, `docs/index.md`, representative
  quickstart/resource/container docs, generated-content scripts
  (`scripts/check_front_matter.py`, `scripts/generate_tags.py`,
  `scripts/update_dev_schedule.py`), Playwright tests, GitHub workflows,
  schedule docs, style/override files, and submodule configuration.
- Files changed: `AGENTS.md`, `PROMPT_LOG.md`.
- Validation: Cross-checked the new guidance against repo workflows, build/test
  config, homepage layout constraints, generated tag behavior, schedule update
  process, and existing contributor docs.
- Follow-up / unresolved: `AGENTS.md` recommends substantial-work logging in
  this file going forward; future agents should append entries rather than
  rewriting prior ones.

## 2026-04-21

- Goal: Refine the repository mission statement in `AGENTS.md` to reflect that
  this is the central repository for ESIIL activities, paired with a network
  portal for deploying resources and a data store for large data.
- Context reviewed: Existing `AGENTS.md` mission/role language and the user’s
  clarification about the broader ESIIL platform model.
- Files changed: `AGENTS.md`, `PROMPT_LOG.md`.
- Validation: Confirmed the updated wording still aligns with the rest of the
  repo-specific guidance and strengthens the explanation of how this repo fits
  into the larger ESIIL ecosystem.
- Follow-up / unresolved: If desired, the same ecosystem framing could also be
  added to `README.md` for human contributors.

## 2026-04-21

- Goal: Establish a durable button-image guideline system and explicitly direct
  all agents, including Codex, to use it for homepage button imagery.
- Context reviewed: Existing homepage image references in `docs/index.md`,
  current asset storage under `docs/assets/thumbnails/`, the repo instruction
  structure in `AGENTS.md`, and the required visual constraints for future
  button-image generation.
- Files changed: `docs/button-image-guidelines.md`, `AGENTS.md`,
  `PROMPT_LOG.md`.
- Validation: Confirmed that `docs/assets/thumbnails/` is the active existing
  repository pattern for homepage button imagery, so the new guideline aligns
  with that path rather than creating a parallel asset tree.
- Follow-up / unresolved: Existing images were not modified. The new guidance
  standardizes future generated assets and future replacements only.

## 2026-05-28

- Goal: Restore the redesigned homepage after the custom template stopped
  rendering, clean up stale repo structure and asset organization, remove the
  lingering analytics-library submodule metadata, and add stronger Playwright
  link-health coverage to CI/deploy workflows.
- Context reviewed: `mkdocs.yml`, `docs/index.md`, homepage override templates
  and partials, homepage CSS/JS, existing Playwright config and tests, GitHub
  workflows, asset references across `docs/`, `.gitmodules`, `AGENTS.md`, and
  the current analytics-library nested repo state.
- Files changed: `.github/workflows/gh-pages.yml`,
  `.github/workflows/playwright.yml`, `.gitmodules`, `AGENTS.md`,
  `PROMPT_LOG.md`, `playwright.config.ts`, `tests/homepage.spec.ts`,
  `docs/file_structure.md`, plus cleanup/removal of the unused root
  `overrides/` folder and stale `.DS_Store` files.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npm ci`; `npx
  playwright test` with elevated local-server permission; in-app browser
  snapshot confirmed the custom homepage sections and CTAs render again.
- Follow-up / unresolved: The curated homepage and ecosystem directory links
  are now covered in Playwright. If future work expands the directory or adds
  new homepage sections, the link-health expectations should be reviewed
  alongside those content changes.

## 2026-05-28

- Goal: Split the old all-in-one ecosystem directory into dedicated gallery
  subpages for working groups, research, events, and infrastructure, and fix
  blank/failed browser back behavior across the custom homepage experience.
- Context reviewed: `mkdocs.yml`, `docs/assets/css/custom.css`,
  `docs/assets/js/homepage.js`, homepage partials, the new custom page
  templates under `docs/overrides/`, the directory markdown pages, and the
  existing Playwright coverage for homepage rendering and link health.
- Files changed: `PROMPT_LOG.md`, `docs/assets/css/custom.css`,
  `docs/assets/js/homepage.js`, `docs/directory/index.md`,
  `docs/directory/working-groups.md`, `docs/directory/research.md`,
  `docs/directory/events.md`, `docs/directory/infrastructure.md`,
  `docs/overrides/home.html`, `docs/overrides/section-gallery.html`,
  `docs/overrides/partials/working_groups.html`,
  `docs/overrides/partials/staff_projects.html`,
  `docs/overrides/partials/events.html`,
  `docs/overrides/partials/infrastructure.html`,
  `docs/overrides/partials/directory/hub.html`,
  `docs/overrides/partials/directory/working_groups_page.html`,
  `docs/overrides/partials/directory/research_page.html`,
  `docs/overrides/partials/directory/events_page.html`,
  `docs/overrides/partials/directory/infrastructure_page.html`, and
  `tests/homepage.spec.ts`.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission; in-app browser spot checks on
  the homepage and working-groups gallery after fixing section-page asset
  paths.
- Follow-up / unresolved: The new gallery pages intentionally stay linked from
  the homepage and ecosystem hub rather than expanding the top-level nav. If
  the user wants them added to global navigation later, that can be done as a
  small follow-up.
