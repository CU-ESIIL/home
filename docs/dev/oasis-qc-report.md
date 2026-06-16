---
title: OASIS Website QC Report
date: 2026-06-16
tags: [development, qc, architecture]
---

# OASIS Website QC Report

This report reviews the current OASIS homepage and supporting MkDocs site after
the May and June 2026 redesign, gallery, thumbnail, metadata graph, stats, and
event-group work. The review focused on user experience, architecture,
agent-readability, data/generated systems, and low-risk maintenance fixes.

## Executive Summary

The site is in a strong state overall. The custom homepage builds cleanly with
`mkdocs build --strict`, the stats and graph generators run successfully, the
first-row destination pages now use the shared gallery template, and the
homepage has a clear visual system rather than feeling like a raw repository
index.

No site-blocking critical issues were found during this pass. The most important
near-term risks are operational: `data/org_repos.json` is currently empty, local
test environments may not have the same Python packages as CI, Playwright could
not be executed in this local session because the app rejected the required
browser-test escalation, and a few placeholder or imported documentation areas
remain easy for future agents to misread as finished product.

Low-risk fixes completed during this review:

- Added a concrete linked example card for the `LLM Lesson Exemplar` in the
  `AI + Team Science` section.
- Added `.DS_Store` to `.gitignore`.
- Removed two tracked macOS metadata files: `.DS_Store` and `code/.DS_Store`.
- Regenerated tag pages with `scripts/generate_tags.py`, which added missing
  generated pages for `onboarding`, `training`, and `tutorials`.

## What Works Well

- The homepage now has a coherent editorial structure: hero, quicklinks, stats,
  working groups, event groups, research, events, interludes, infrastructure,
  AI/team-science framing, and footer.
- Directory pages for working groups, event groups, research, events, and
  infrastructure use `section-gallery.html`, which keeps the homepage journey
  visually continuous instead of dropping users into legacy Markdown lists.
- The thumbnail system has a clear source-of-truth structure with active,
  original, generated set, manifest, and documentation paths.
- The static metadata graph is lightweight and appropriate for a MkDocs site.
  It avoids databases and hosted services while still creating a path toward
  richer discovery.
- The stats bar is appropriately manual where it should be manual. Compute
  hours are not incorrectly derived from GitHub Actions.
- The homepage Playwright test file is meaningful. It checks the custom layout,
  dark-mode toggle, small-screen behavior, first-row links, back navigation,
  gallery pages, stats, interlude ordering, and image/link health.
- `docs/dev-schedule.md` now functions as real historical documentation, with
  recent May and June work plus a future roadmap section.

## Critical Issues

No critical runtime or build issues were found in the source review and strict
MkDocs build.

Residual critical-risk caveat: Playwright was not executed in this session
because the app rejected the escalation required to launch the local browser
suite. The existing test file should still be treated as required CI coverage.

## High-Priority Improvements

- Refresh or populate `data/org_repos.json`. It is currently `[]`, so generated
  repository and website metrics fall back to configured values. CI can discover
  repos with `GH_TOKEN`, but the checked-in cache does not currently represent
  the organization.
- Align local development environments with CI. `requirements.txt` includes
  `pytest>=8`, but the local `.venv` used in this review did not have `pytest`
  installed, so graph unit tests could not run locally.
- Keep event-group galleries moving from shell to content. The homepage and
  directory structure are present, but the confirmed event-group sets still need
  to stay complete and accurately linked as those group pages evolve.
- Continue reducing placeholder content. `docs/container-library.md`,
  `docs/container-library/example-container.md`, and placeholder cards in some
  directory partials are understandable, but future agents need to know which
  placeholders are intentional and which are stale.
- Stabilize interlude-banner tuning. The current partial is reusable, but the
  CSS relies on per-banner transform offsets and zero-height flow behavior,
  which has repeatedly required manual visual tuning.

## Medium-Priority Improvements

- Consider documenting the intended role of imported or mirrored resource
  folders, especially Quarto-like generated assets under `docs/resources/` and
  `docs/worksheets/`. They are valid content, but they are noisier than the rest
  of the repo and can confuse maintenance agents.
- Add a short note to the registry documentation explaining that
  `data/org_repos.json` may be empty locally and is refreshed by CI or by a
  maintainer with GitHub CLI access.
- Add a small `make` or script wrapper for common validation commands. The repo
  now has multiple independent checks: front matter, tags, stats, graph, MkDocs,
  pytest, and Playwright.
- Keep generated tag pages in sync when front matter changes. The generator
  updated tag outputs during this pass, which suggests tags can drift if the
  script is not part of a normal maintenance habit.
- Review external placeholder links with `href="#"` in data outputs before they
  become user-facing CTAs. The stats JSON correctly keeps DOI and compute-hours
  as non-clickable main-bar groups, but future templates should not accidentally
  expose placeholder anchors as primary links.

## Agent Readability Findings

- `AGENTS.md` is unusually strong and useful. It explains repository purpose,
  audiences, homepage safety rules, image guidelines, generated content, and
  prompt-log expectations.
- `docs/dev/oasis-site-dev-guide.md` remains important for homepage layout work.
  Future agents should read it before touching hero, band, or section CSS.
- The registry system is readable and boring in the right way. YAML registry
  files, `registry/README.md`, `scripts/build_graph.py`, and generated JSON are
  understandable without specialized infrastructure.
- The homepage is partialized enough to support safe edits, but visual behavior
  is distributed across several CSS files. Agents should inspect
  `docs/assets/css/custom.css`, `docs/styles/extra.css`, and the relevant
  partial before changing layout.
- The strongest agent-readability gap is still source-of-truth completeness.
  Some homepage/gallery card data lives inline in Jinja partials, while registry
  data and thumbnail manifests live elsewhere. This is acceptable for now, but
  future large content changes should avoid creating a third source of truth.

## AI + Team Science Findings

- The homepage now explicitly frames OASIS as infrastructure for collaborative
  science and AI-assisted work, not only as a project directory.
- The existing `AI + Team Science` section was conceptually sound but abstract.
  This pass added `LLM Lesson Exemplar` as a concrete linked example of an
  AI-ready project with lesson materials, repository structure, website content,
  and reusable project memory.
- Recommended next step: add one or two more concrete examples only after they
  have durable pages and clear metadata. Avoid turning this section into another
  dense gallery.

## Interlude Banner Findings

- Interludes are implemented through a reusable partial at
  `docs/overrides/partials/interlude_banner.html`.
- The current placement is source-order based, which is good. The banners are
  not injected with JavaScript or tied to external services.
- The CSS uses `height: 0`, visible overflow, and per-class `translateY(...)`
  values. This creates the desired seam-breaking visual effect, but it is
  fragile because small content, viewport, or image changes can make banners
  cover cards or float too far from a transition.
- Mobile behavior is simplified, but the same zero-height model means mobile
  QA should remain part of any banner edit.
- Recommended next step: keep the current look, but define each interlude with
  explicit CSS custom properties for visual height, overlap-up, overlap-down,
  and safe content buffer. That would preserve the aesthetic while making future
  tuning less guessy.

## Repo Cleanliness Findings

- Removed tracked macOS metadata files from `.DS_Store` and `code/.DS_Store`.
- Added `.DS_Store` to `.gitignore`.
- Local generated/build folders are present but ignored: `site/`, `node_modules/`,
  and `test-results/`.
- Python caches are ignored, but local `scripts/__pycache__/` exists and should
  be cleaned before packaging or release if it ever appears in status.
- `data/org_repos.json` is intentionally tracked as a data cache, but it is
  currently empty. That is a data freshness issue, not repo clutter.
- The repo contains substantial generated or imported documentation assets.
  They are not necessarily wrong, but future cleanup should distinguish
  imported content from OASIS-authored source content.

## Test Results

Commands run successfully:

```bash
./.venv/bin/python scripts/check_front_matter.py
./.venv/bin/python scripts/build_oasis_stats.py
./.venv/bin/python scripts/build_graph.py
./.venv/bin/python scripts/generate_tags.py
./.venv/bin/python -m mkdocs build --strict
```

Generated outputs updated:

- `docs/assets/data/oasis_stats.json`
- `docs/overrides/partials/stats_bar.html`
- `docs/assets/data/esiil_graph.json`
- `docs/tags/index.md`
- `docs/tags/development.md`
- `docs/tags/schedule.md`
- `docs/tags/onboarding.md`
- `docs/tags/training.md`
- `docs/tags/tutorials.md`

Command attempted but not runnable in the local `.venv`:

```bash
./.venv/bin/python -m pytest tests/test_build_graph.py
```

Result:

```text
No module named pytest
```

This is a local environment issue. `requirements.txt` already includes
`pytest>=8`, and the GitHub Action installs requirements before running graph
tests.

Command not run because the app rejected the browser-test escalation:

```bash
npx playwright test
```

The rejection came from the app usage-limit gate, not from Playwright or the
site. Playwright should still be run in CI or in a local environment where the
browser suite can launch.

## Recommended Next Actions

1. Run `pip install -r requirements.txt` in the active local `.venv`, then rerun
   `./.venv/bin/python -m pytest tests/test_build_graph.py`.
2. Run `npx playwright test` in CI or a local environment with browser-test
   permissions.
3. Refresh `data/org_repos.json` with `scripts/discover_org_repos.py` using
   GitHub CLI access, then rebuild stats and graph outputs.
4. Replace or clearly label remaining intentional placeholders in container and
   directory content.
5. Refactor interlude-banner spacing into named CSS variables before the next
   major visual tuning pass.
6. Keep adding meaningful project metadata to `registry/projects/` whenever
   new homepage cards, directories, or external project pages are added.

## Files Changed

- `.gitignore`
- `.DS_Store`
- `code/.DS_Store`
- `docs/assets/css/custom.css`
- `docs/overrides/partials/ai_team_science.html`
- `docs/tags/development.md`
- `docs/tags/index.md`
- `docs/tags/schedule.md`
- `docs/tags/onboarding.md`
- `docs/tags/training.md`
- `docs/tags/tutorials.md`
- `docs/dev/oasis-qc-report.md`

