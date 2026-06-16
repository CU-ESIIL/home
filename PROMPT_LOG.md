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

## 2026-05-28

- Goal: Fix narrow-window homepage overlap by making the hero responsive at
  phone widths and add an automated regression check for horizontal overflow.
- Context reviewed: `docs/assets/css/custom.css`, `tests/homepage.spec.ts`,
  the homepage hero structure in `docs/overrides/partials/hero.html`, and a
  live narrow-width browser render of the built site.
- Files changed: `PROMPT_LOG.md`, `docs/assets/css/custom.css`,
  `tests/homepage.spec.ts`.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission; browser spot check at `320px`
  width confirmed the hero stays within the viewport without horizontal
  clipping.
- Follow-up / unresolved: If other sections show narrow-width crowding later,
  the new small-screen overflow test can be extended to the gallery pages too.

## 2026-05-28

- Goal: Replace the homepage’s lower footer area with the institutional footer
  pattern from the `Project_group_OASIS` reference page, including the CU
  Boulder, CIRES, ESIIL, and NSF logos.
- Context reviewed: `docs/overrides/partials/footer_cta.html`,
  `docs/assets/css/custom.css`, the live footer structure at
  `https://cu-esiil.github.io/Project_group_OASIS/#cite-reuse`, and the logo
  asset paths used by that reference page.
- Files changed: `PROMPT_LOG.md`, `docs/overrides/partials/footer_cta.html`,
  `docs/assets/css/custom.css`, plus new local footer logo assets in
  `docs/assets/branding/footer-cu-logo.png`,
  `docs/assets/branding/footer-cires-logo.png`,
  `docs/assets/branding/footer-esiil-logo.png`, and
  `docs/assets/branding/footer-nsf-logo.png`.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission; browser spot check confirmed
  the institutional footer copy and four logos render together at the bottom of
  the homepage.
- Follow-up / unresolved: The homepage keeps its existing top CTA footer band,
  with the reference-style institutional footer replacing the previous
  supporters/nav block beneath it.

## 2026-05-28

- Goal: Tighten the homepage footer after the first institutional-footer pass
  landed too large, especially the overall band height and the four partner
  logos.
- Context reviewed: `docs/assets/css/custom.css`, the homepage footer partial,
  the user screenshot of the oversized footer, and a live local browser render
  of the homepage footer after rebuild.
- Files changed: `PROMPT_LOG.md`, `docs/assets/css/custom.css`.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission; browser spot check confirmed a
  shorter footer band and smaller logo row.
- Follow-up / unresolved: If you want it even quieter, the next easy pass would
  be shrinking the top CTA band typography rather than the institutional block.

## 2026-05-28

- Goal: Replace the checkerboard-backed header logo with a real white-backed,
  tightly cropped lockup so the header can be thinner while the logo occupies
  more of the header height.
- Context reviewed: `docs/assets/branding/esiil-oasis-lockup.png`,
  `docs/assets/css/style.css`, the header rendering on the homepage, and the
  user screenshot showing the faux transparency pattern in the logo asset.
- Files changed: `PROMPT_LOG.md`, `docs/assets/css/style.css`,
  `docs/assets/branding/esiil-oasis-lockup.png`, and archived copy
  `docs/assets/archive/branding/esiil-oasis-lockup-checkerboard-legacy.png`.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission; browser spot check confirmed the
  tighter white-backed logo inside a thinner header.
- Follow-up / unresolved: If desired, the next refinement would be adjusting
  the overall header controls spacing so the search box and repo metadata align
  even more tightly with the new logo scale.

## 2026-05-28

- Goal: Repair dark mode so the palette toggle actually repaints the custom
  homepage and gallery pages, and remove the GitHub repository badge from the
  header.
- Context reviewed: `mkdocs.yml`, `docs/styles/brand.css`,
  `docs/assets/css/custom.css`, `docs/dev/oasis-site-dev-guide.md`, and the
  homepage Playwright coverage in `tests/homepage.spec.ts`.
- Files changed: `PROMPT_LOG.md`, `mkdocs.yml`, `docs/styles/brand.css`,
  `docs/assets/css/custom.css`, and `tests/homepage.spec.ts`.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission; in-app browser snapshot check on
  the rebuilt homepage after the theme and header updates.
- Follow-up / unresolved: The repo metadata stays in `mkdocs.yml` so `edit_uri`
  remains valid, and the visible header source badge is suppressed in CSS
  instead of removing repository configuration entirely.

## 2026-05-28

- Goal: Build a durable thumbnail-management system with preserved originals, an
  active-set folder, a manifest, and a human-readable inventory for future
  image-generation work.
- Context reviewed: `mkdocs.yml`, homepage and gallery partials under
  `docs/overrides/partials/`, directory pages under `docs/directory/`, the
  current thumbnail tree under `docs/assets/homepage/`, and the existing
  Playwright link-and-image checks in `tests/homepage.spec.ts`.
- Files changed: `PROMPT_LOG.md`, homepage and directory partials now pointing
  to `docs/assets/thumbnails/active/`, new docs under
  `docs/thumbnail-system/project-thumbnail-index.md`,
  `docs/assets/thumbnails/README.md`,
  `docs/assets/thumbnails/thumbnail-manifest.yml`,
  `docs/assets/thumbnails/style-guides/README.md`, and copied thumbnail trees
  under `docs/assets/thumbnails/active/`, `originals/`, and
  `sets/set-001-originals/`.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission.
- Follow-up / unresolved: Several entries are marked `needs review` in the
  inventory and manifest because local card text was enough to place them in
  the system, but not enough to support a high-confidence replacement image
  without deeper page review.

## 2026-05-29

- Goal: Split the combined ESIIL/OASIS header-footer lockup into separate
  marks, add the new standalone OASIS hero illustration, make the dark-mode
  toggle easy to find again, and introduce light-touch biology flourishes
  across the curated homepage and gallery templates.
- Context reviewed: `mkdocs.yml`, `docs/overrides/partials/hero.html`,
  `docs/overrides/partials/footer_cta.html`,
  `docs/overrides/section-gallery.html`, `docs/styles/brand.css`,
  `docs/styles/extra.css`, `docs/assets/css/custom.css`, and the Material
  header partial structure inside the local `.venv` theme package.
- Files changed: `PROMPT_LOG.md`, `mkdocs.yml`, new
  `docs/overrides/partials/header.html`, homepage/gallery partials, and the
  branding assets `docs/assets/branding/esiil-wordmark-color.png`,
  `docs/assets/branding/oasis-wordmark-mark.png`,
  `docs/assets/branding/oasis-hero-illustration.png`, and
  `docs/assets/branding/biology-flourishes-panel.png`.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission; in-app browser snapshot check on
  the rebuilt homepage header and hero.
- Follow-up / unresolved: The centered OASIS header logo is intentionally
  hidden below `900px` so the palette toggle, search, and mobile navigation
  stay discoverable and uncluttered on narrow screens.

## 2026-05-29

- Goal: Convert user-provided thumbnail panels into a managed alternate set,
  preserve the legacy screen-print set, and switch the live site to the new
  panel-derived thumbnails.
- Context reviewed: `docs/assets/thumbnails/README.md`,
  `docs/assets/thumbnails/thumbnail-manifest.yml`,
  `docs/thumbnail-system/project-thumbnail-index.md`, and the live active-tree
  filenames under `docs/assets/thumbnails/active/`.
- Files changed: `docs/assets/thumbnails/active/` for the newly promoted live
  alternate thumbnails, populated `docs/assets/thumbnails/sets/set-002-generated/`,
  copied reference panels into `docs/assets/thumbnails/style-guides/`, and
  updated thumbnail-system documentation.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission.
- Follow-up / unresolved: The provided panels covered working groups, research,
  events, and four major infrastructure cards. Template thumbnails and several
  secondary infrastructure assets were intentionally inherited from the prior
  active set inside `set-002-generated` because no alternate panel art was
  provided for them.

## 2026-05-29

- Goal: Repair the panel-derived alternate thumbnail set so the thumbnails use
  real transparency, stay centered inside cards across sections, render at
  higher effective quality, and remove any embedded title text from the source
  panels.
- Context reviewed: `docs/assets/css/custom.css`, the active and
  `set-002-generated` thumbnail trees, the three panel source sheets in
  `docs/assets/thumbnails/style-guides/`, and the homepage/gallery partials
  that reference active thumbnails.
- Files changed: `docs/assets/css/custom.css`, the panel-derived PNG assets
  under `docs/assets/thumbnails/active/` and
  `docs/assets/thumbnails/sets/set-002-generated/`, the directory/homepage
  partials referencing panel-derived thumbnails, and
  `docs/assets/thumbnails/thumbnail-manifest.yml`.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission.
- Follow-up / unresolved: The repaired extraction path now uses transparent PNG
  assets derived directly from the source panels rather than relying on the
  earlier cropped intermediates. Panel coverage still does not include every
  template or secondary infrastructure tile, so inherited non-panel thumbnails
  remain in place for those items.

## 2026-05-29

- Goal: Refine the homepage opening view by removing the small green OASIS
  kicker, tightening the gap beneath the header, giving the hero illustration a
  larger overlapping presence, adding more horizontal breathing room to the
  header edges, and making the dark-mode toggle visible in slate mode.
- Context reviewed: `docs/overrides/partials/hero.html`,
  `docs/styles/brand.css`, and the hero/header sections of
  `docs/assets/css/custom.css`.
- Files changed: `docs/overrides/partials/hero.html`,
  `docs/styles/brand.css`, `docs/assets/css/custom.css`.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission.
- Follow-up / unresolved: The hero art now intentionally pushes further into
  the text column on desktop while collapsing back to a centered stacked layout
  on tablet and mobile breakpoints.

## 2026-05-29

- Goal: Add user-provided full-width interlude banners between major homepage
  sections so the long front page has stronger visual pacing.
- Context reviewed: `docs/overrides/home.html`, the homepage partial ordering,
  and the shared homepage section styles in `docs/assets/css/custom.css`.
- Files changed: `docs/overrides/home.html`,
  `docs/overrides/partials/interlude_banner.html`,
  `docs/assets/css/custom.css`, plus new banner assets at
  `docs/assets/branding/oasis-interlude-banner.png` and
  `docs/assets/branding/animal-interlude-banner.png`.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission.
- Follow-up / unresolved: The first banner currently sits between working
  groups and staff research, and the second sits between events and
  infrastructure. If the pacing feels off in practice, these placements can be
  swapped without changing the banner component itself.

## 2026-05-29

- Goal: Rework the new interlude banners so they behave like floating overlay
  artwork instead of boxed dark strips, and make the hero illustration itself
  substantially larger by trimming excess transparent canvas and pushing the art
  farther into the headline area from the right.
- Context reviewed: `docs/assets/css/custom.css`, the interlude partial, and
  the alpha bounds of the current hero and banner assets in
  `docs/assets/branding/`.
- Files changed: `docs/assets/css/custom.css`,
  `docs/assets/branding/oasis-hero-illustration.png`.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission.
- Follow-up / unresolved: The interlude banners now rely on blend/overlay
  presentation rather than a solid container background, so if future banner
  art uses very different tonal ranges it may need per-banner tuning.

## 2026-05-29

- Goal: Improve the blurry oversized staff/postdoc research tiles by replacing
  the cube and WUI-related thumbnail assets with tighter, higher-resolution
  panel-derived crops and making the larger research-card image variants fill
  their frames more aggressively.
- Context reviewed: `docs/overrides/partials/staff_projects.html`,
  `docs/overrides/partials/directory/research_page.html`,
  `docs/assets/css/custom.css`, and the source panel at
  `docs/assets/thumbnails/style-guides/staff-postdoc-thumbnails-panel.png`.
- Files changed: `docs/assets/css/custom.css`,
  `docs/assets/thumbnails/active/research/cubedynamics-button.png`,
  `docs/assets/thumbnails/active/research/wui-boundary-button.png`,
  `docs/assets/thumbnails/active/research/datacube-sandbox-button.png`, plus
  matching files under
  `docs/assets/thumbnails/sets/set-002-generated/research/`.
- Validation: `.venv/bin/python -m mkdocs build --strict`; `npx playwright
  test` with elevated local-server permission after clearing a stale local
  server on port 8000.
- Follow-up / unresolved: The larger `feature` and `wide` research cards now
  use `object-fit: cover` with minimal padding by design, so if future assets
  for those slots need exact full-art preservation they may need dedicated
  layout-specific crops.
## 2026-05-29 - Hero spill, interlude refresh, and tighter thumbnail crops

- Goal: push the hero illustration farther off the right edge, replace both
  interlude banners with newer artwork, and remove the remaining baked-in white
  margins from the most prominent alternate-set thumbnails.
- Repo context reviewed:
  [docs/assets/css/custom.css](/Users/tuff/Library/CloudStorage/OneDrive-UCB-O365/Documents/github/home/docs/assets/css/custom.css),
  [docs/overrides/home.html](/Users/tuff/Library/CloudStorage/OneDrive-UCB-O365/Documents/github/home/docs/overrides/home.html),
  active and `set-002-generated` thumbnail paths under
  `docs/assets/thumbnails/`.
- Major files changed:
  [docs/assets/css/custom.css](/Users/tuff/Library/CloudStorage/OneDrive-UCB-O365/Documents/github/home/docs/assets/css/custom.css),
  [docs/assets/branding/oasis-interlude-banner.png](/Users/tuff/Library/CloudStorage/OneDrive-UCB-O365/Documents/github/home/docs/assets/branding/oasis-interlude-banner.png),
  [docs/assets/branding/animal-interlude-banner.png](/Users/tuff/Library/CloudStorage/OneDrive-UCB-O365/Documents/github/home/docs/assets/branding/animal-interlude-banner.png),
  [docs/assets/thumbnails/active/events/innovation-summit-2026-button.png](/Users/tuff/Library/CloudStorage/OneDrive-UCB-O365/Documents/github/home/docs/assets/thumbnails/active/events/innovation-summit-2026-button.png),
  [docs/assets/thumbnails/active/events/forest-carbon-codefest-button.png](/Users/tuff/Library/CloudStorage/OneDrive-UCB-O365/Documents/github/home/docs/assets/thumbnails/active/events/forest-carbon-codefest-button.png),
  [docs/assets/thumbnails/active/research/datacube-sandbox-button.png](/Users/tuff/Library/CloudStorage/OneDrive-UCB-O365/Documents/github/home/docs/assets/thumbnails/active/research/datacube-sandbox-button.png),
  [docs/assets/thumbnails/active/research/wui-boundary-button.png](/Users/tuff/Library/CloudStorage/OneDrive-UCB-O365/Documents/github/home/docs/assets/thumbnails/active/research/wui-boundary-button.png),
  plus their preserved copies in `docs/assets/thumbnails/sets/set-002-generated/`.
- Validation performed:
  `./.venv/bin/python -m mkdocs build --strict`
  Playwright passed once earlier in the same edit pass after the CSS/banner
  changes, then a final rerun after the last crop-tightening step was declined
  by the app permission prompt.
- Follow-ups / assumptions:
  The remaining most noticeable whitespace issue was image-intrinsic, not CSS
  layout padding, so the final pass focused on tighter asset crops rather than
  further shrinking card gutters.

## 2026-06-09

- Goal: add a static organization-wide metadata graph system for the CU-ESIIL
  ecosystem inside the OASIS home repo, generate initial Explore theme pages,
  add graph CI/test scaffolding, and restore the interlude banners to true
  full-width presentation.
- Context reviewed: `AGENTS.md`, `mkdocs.yml`, current homepage section
  partials, `.github/workflows/`, `requirements.txt`, existing docs directory
  structure, interlude banner CSS in `docs/assets/css/custom.css`, and current
  homepage-linked projects/libraries/events used as seed registry content.
- Files changed: `mkdocs.yml`, `requirements.txt`, `PROMPT_LOG.md`,
  `.github/workflows/build-graph.yml`, `scripts/__init__.py`,
  `scripts/discover_org_repos.py`, `scripts/build_graph.py`,
  `tests/test_build_graph.py`, `docs/explore/index.md`,
  `docs/assets/css/custom.css`, `docs/assets/data/esiil_graph.json`,
  generated theme pages under `docs/explore/themes/`, `data/org_repos.json`,
  and new registry content under `registry/projects/`, `registry/people/`,
  `registry/themes/`, `registry/datasets/`, and `registry/schema/`.
- Validation: `./.venv/bin/python scripts/build_graph.py`;
  `./.venv/bin/python -m py_compile scripts/build_graph.py scripts/discover_org_repos.py`;
  `./.venv/bin/python -m mkdocs build --strict`.
- Follow-up / unresolved: local `pytest` execution could not be completed on
  this machine because `pytest` is not installed in the repo virtualenv and
  package installation was blocked by network restrictions/approval limits, but
  the new CI workflow installs dependencies and runs `pytest
  tests/test_build_graph.py` automatically. The first graph registry is a
  starter slice of the ecosystem and should be extended over time rather than
  treated as complete coverage.

## 2026-06-09

- Goal: add a dedicated `Event Groups` homepage band directly below `Events &
  Summits` so event-linked repositories have a clear place on the front page.
- Context reviewed: `docs/overrides/home.html`,
  `docs/overrides/partials/events.html`,
  `docs/overrides/partials/working_groups.html`,
  `docs/overrides/partials/staff_projects.html`,
  `docs/overrides/partials/directory/events_page.html`, and the homepage card
  rail/grid patterns in `docs/assets/css/custom.css`.
- Files changed: `docs/overrides/home.html`,
  `docs/overrides/partials/event_groups.html`, `PROMPT_LOG.md`.
- Validation: Pending strict MkDocs build after wiring the new partial into the
  homepage template.
- Follow-up / unresolved: This first pass uses the existing event archive URLs
  and thumbnails so the section is immediately usable. If desired later, the
  event-group band can get its own dedicated directory page instead of sharing
  the current events archive destination.

## 2026-06-10

- Goal: correct the new homepage `Event Groups` band so it stops duplicating
  the public event archive and instead points at actual event-group pages in a
  single-row shelf.
- Context reviewed: `docs/overrides/partials/event_groups.html`,
  `docs/overrides/partials/events.html`, the placeholder card pattern in
  `docs/assets/css/custom.css`, and the user-provided summit-group URL.
- Files changed: `docs/overrides/partials/event_groups.html`,
  `PROMPT_LOG.md`.
- Validation: Pending strict MkDocs build after converting the section from
  duplicate event cards to one real event-group card plus placeholders.
- Follow-up / unresolved: Only one event-group URL was provided in this pass,
  so the remaining slots are placeholders ready to be replaced with real group
  repos as they are shared.

## 2026-06-10

- Goal: finish the `Event Groups` section by giving it its own directory page
  and forcing the homepage version into a four-card single-row strip instead of
  another event-archive shelf.
- Context reviewed: `docs/overrides/partials/event_groups.html`,
  `docs/overrides/section-gallery.html`,
  `docs/overrides/partials/directory/events_page.html`,
  sibling `docs/directory/*.md` pages, and the shared rail/grid rules in
  `docs/assets/css/custom.css`.
- Files changed: `docs/overrides/partials/event_groups.html`,
  `docs/directory/event-groups.md`,
  `docs/overrides/partials/directory/event_groups_page.html`,
  `PROMPT_LOG.md`.
- Validation: Pending strict MkDocs build after wiring the new event-group
  directory page.
- Follow-up / unresolved: The user has only supplied one true event-group URL
  so far, so the dedicated page and homepage strip still contain placeholders
  until the remaining links are provided.

## 2026-06-10

- Goal: repair CI graph tests after GitHub Actions reported
  `ModuleNotFoundError: No module named 'scripts'` during pytest collection.
- Context reviewed: `.github/workflows/build-graph.yml`,
  `tests/test_build_graph.py`, `scripts/__init__.py`, and the import behavior
  of the local Python environment relative to repo-root path handling.
- Files changed: `tests/conftest.py`, `PROMPT_LOG.md`.
- Validation: Local sanity check confirmed the repository root was not being
  inserted into `sys.path` by default in this environment, so the new
  `tests/conftest.py` now establishes that path explicitly for pytest.
- Follow-up / unresolved: This fix is intentionally narrow and only affects the
  test harness. It does not change runtime graph-building behavior.

## 2026-06-15

- Goal: update `AGENTS.md` so future agents are explicitly instructed to add
  metadata-graph registry entries when they introduce new discoverable
  ecosystem entities.
- Context reviewed: `AGENTS.md` file-boundary guidance, recent graph-system
  additions (`registry/`, `scripts/build_graph.py`), and the current agent
  workflow expectations for source-of-truth updates.
- Files changed: `AGENTS.md`, `PROMPT_LOG.md`.
- Validation: Editorial/rules update only; cross-checked the new guidance
  against the existing static graph architecture and registry structure.
- Follow-up / unresolved: The guidance is intentionally scoped so agents do not
  over-register purely procedural docs or small utility pages.

## 2026-06-15

- Goal: rebuild the `Event Group Galleries` homepage section so it points to
  event-level gallery pages instead of duplicating event cards or linking to a
  single placeholder event-group repository.
- Context reviewed: attached event-group prompt, `mkdocs.yml`,
  `docs/overrides/partials/event_groups.html`, event-group gallery partials,
  `docs/assets/css/custom.css`, existing registry schema, and public CU-ESIIL
  GitHub repository names discovered through a read-only GitHub API query.
- Files changed: `docs/overrides/partials/event_groups.html`,
  `docs/overrides/partials/event_groups/index_page.html`,
  `docs/overrides/partials/event_groups/gallery_page.html`,
  `docs/event-groups/*.md`, `mkdocs.yml`, new
  `registry/projects/*-group-sites.yaml`, generated graph/theme outputs, and
  `PROMPT_LOG.md`.
- Validation: Ran `./.venv/bin/python scripts/build_graph.py` and
  `./.venv/bin/python -m mkdocs build --strict`; both passed.
- Follow-up / unresolved: The event group lists use public repository names
  discoverable from GitHub. If any event group should have a more formal title
  than its repository-derived topic label, update the matching
  `docs/event-groups/*.md` front matter entry.

## 2026-06-15

- Goal: update the archived development schedule page so it reflects major
  post-April homepage, CI, visual-system, metadata graph, and Event Groups
  work recorded in `PROMPT_LOG.md`.
- Context reviewed: `docs/dev-schedule.md` and the prompt-log entries covering
  the May 28 homepage restoration/directory split, May 29 hero and thumbnail
  work, June 9 metadata graph system, June 9-10 Event Groups iterations, June
  10 graph test harness fix, and June 15 Event Group gallery completion.
- Files changed: `docs/dev-schedule.md`, `PROMPT_LOG.md`.
- Validation: Added a `Recent Updates Since April 2026` section, appended
  checked historical tasks, extended the timeline table, appended May/June
  sections to the Mermaid Gantt block, and ran
  `./.venv/bin/python -m mkdocs build --strict` successfully.
- Follow-up / unresolved: The page remains archived historical documentation;
  active prioritization should still happen in GitHub issues and pull
  requests.

## 2026-06-15

- Goal: add a polished homepage stats band using manual program metrics plus
  conservative generated repository/website fallbacks.
- Context reviewed: homepage template ordering, hero quicklinks, existing
  interlude placement, custom homepage CSS, Playwright homepage/link-health
  tests, registry project metadata, and the empty `data/org_repos.json` cache.
- Files changed: `data/oasis_stats_config.yml`,
  `scripts/build_oasis_stats.py`, `docs/assets/data/oasis_stats.json`,
  `docs/overrides/partials/stats_bar.html`, `docs/overrides/home.html`,
  `docs/assets/css/custom.css`, `tests/homepage.spec.ts`, and
  `PROMPT_LOG.md`.
- Validation: Ran `./.venv/bin/python scripts/build_oasis_stats.py`,
  `./.venv/bin/python -m mkdocs build --strict`, and
  `npx playwright test`; all passed after rerunning Playwright with permission
  to start its local web server.
- Follow-up / unresolved: Repository and website counts currently use fallback
  values because `data/org_repos.json` is empty. Compute hours remain a manual
  external-infrastructure metric and are not calculated from in-repository
  automation.

## 2026-06-15

- Goal: evolve the homepage narrative from an inventory/gallery framing toward
  an ecosystem story centered on environmental science beyond the laptop,
  collaborative teams, AI, reusable infrastructure, and durable project
  outputs.
- Context reviewed: attached narrative prompt, homepage wrapper ordering,
  section partials, stats-band placement, custom homepage CSS, and existing
  Playwright homepage structure/link-health tests.
- Files changed: `docs/overrides/home.html`,
  `docs/overrides/partials/hero.html`,
  `docs/overrides/partials/working_groups.html`,
  `docs/overrides/partials/event_groups.html`,
  `docs/overrides/partials/staff_projects.html`,
  `docs/overrides/partials/events.html`,
  `docs/overrides/partials/infrastructure.html`,
  `docs/overrides/partials/footer_cta.html`,
  `docs/overrides/partials/ai_team_science.html`,
  `docs/assets/css/custom.css`, `tests/homepage.spec.ts`, and
  `PROMPT_LOG.md`.
- Validation: Ran `./.venv/bin/python scripts/build_oasis_stats.py`,
  `./.venv/bin/python -m mkdocs build --strict`, and
  `npx playwright test`; all passed after rerunning Playwright with permission
  to start its local web server.
- Follow-up / unresolved: The new `AI + Team Science` section is intentionally
  lightweight and text-led. It can gain linked cards or visual assets later if
  the team wants that section to become a deeper gateway.

## 2026-06-15

- Goal: add a future-facing Years 5-10 roadmap to the archived development
  schedule page without replacing the historical schedule.
- Context reviewed: attached future-roadmap prompt and the current
  `docs/dev-schedule.md` archive structure, including the existing historical
  Gantt chart and inline table styling.
- Files changed: `docs/dev-schedule.md`, `PROMPT_LOG.md`.
- Validation: Added a clearly separated `Future Roadmap (Years 5-10)` section
  with introductory narrative, a Mermaid Gantt chart, a phase explanation
  table, and a closing collective-intelligence narrative. Mermaid task labels
  were kept on single lines for safer MkDocs Material rendering.
- Follow-up / unresolved: The roadmap is strategic documentation only and does
  not create active scheduled tasks in `docs/upcoming_tasks.yaml`.

## 2026-06-15

- Goal: modernize the subpages linked from the homepage's first-row section
  buttons so the journey from the redesigned homepage continues into gallery
  pages rather than legacy Markdown-style link lists.
- Context reviewed: homepage partials, `section-gallery.html`, directory
  Markdown entry points, event-group gallery partials, homepage link tests, and
  existing section-card patterns.
- Files changed: `docs/directory/working-groups.md`,
  `docs/directory/event-groups.md`, `docs/directory/research.md`,
  `docs/directory/events.md`, `docs/directory/infrastructure.md`,
  `docs/event-groups/index.md`,
  `docs/overrides/partials/directory/event_groups_page.html`,
  `docs/overrides/section-gallery.html`, `tests/homepage.spec.ts`, and
  `PROMPT_LOG.md`.
- Validation: Ran `./.venv/bin/python -m mkdocs build --strict` and
  `npx playwright test`; all six Playwright tests passed after updating the
  gallery journey checks to assert the shared section-gallery layout and
  browser-back behavior.
- Follow-up / unresolved: The destination pages now share the OASIS visual
  system. Future content additions should continue to use section-gallery
  front matter and card/grid partials instead of plain link lists.

## 2026-06-16

- Goal: complete a comprehensive QC, UX, agent-readability, and architecture
  review of the OASIS website and document the findings for future maintainers.
- Context reviewed: attached QC prompt, homepage partial ordering, gallery
  destination pages, AI + Team Science partial, interlude banner partial/CSS,
  registry and thumbnail documentation, graph/stats generators, workflows,
  tag generation, and existing Playwright homepage tests.
- Files changed: `docs/dev/oasis-qc-report.md`, `.gitignore`,
  `docs/overrides/partials/ai_team_science.html`,
  `docs/assets/css/custom.css`, generated tag pages under `docs/tags/`, and
  removal of tracked `.DS_Store` metadata files.
- Validation: Ran front-matter validation, stats generation, graph generation,
  tag generation, and `./.venv/bin/python -m mkdocs build --strict`
  successfully. Local graph pytest could not run because the active `.venv`
  lacks `pytest`, even though `requirements.txt` declares it. Playwright was
  not run because the app rejected the required browser-test escalation.
- Follow-up / unresolved: Refresh the empty `data/org_repos.json` cache with
  GitHub CLI access, rerun graph pytest after installing requirements into the
  active `.venv`, and run Playwright in CI or a local session with browser-test
  permission.

## 2026-06-16

- Goal: add confirmed Cohort 3 working group repositories and update the AI +
  Team Science homepage section to foreground concrete OASIS AI infrastructure
  examples.
- Context reviewed: attached Cohort 3 prompt, Working Groups gallery partial,
  AI + Team Science partial, homepage CSS/card styles, project registry schema,
  graph builder, and Playwright homepage tests.
- Files changed: `docs/overrides/partials/directory/working_groups_page.html`,
  `docs/overrides/partials/ai_team_science.html`,
  `docs/assets/css/custom.css`, `scripts/build_graph.py`,
  `tests/homepage.spec.ts`, new Cohort 3 project registry files,
  `registry/projects/openclaw-container.yaml`,
  `registry/projects/hermes-container.yaml`, generated graph/explore outputs,
  and `PROMPT_LOG.md`.
- Validation: Ran `./.venv/bin/python scripts/build_graph.py`,
  `./.venv/bin/python scripts/check_front_matter.py`,
  `./.venv/bin/python scripts/build_oasis_stats.py`,
  `./.venv/bin/python -m mkdocs build --strict`, and `npx playwright test`.
  Playwright passed all 6 tests after rerunning with permission to bind its
  local web server.
- Follow-up / unresolved: Cohort 3 cards currently reuse the working-group
  OASIS template thumbnail as a placeholder. Excluded `byandell-esiil`,
  `Wyatt_ESIIL_proj`, `hermes_container`, `openclaw_container`,
  `ty_test_trainer`, and `Summit_group_2026_*` from Cohort 3 working groups as
  directed; Hermes and OpenClaw were added as AI infrastructure registry entries
  instead.
