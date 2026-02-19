# OASIS MkDocs Site Dev Guide (Homepage + Layout Safety)

This is the canonical guide for homepage layout behavior, homepage CSS scoping, and Codex-safe editing patterns.

Use this before touching:

- `docs/index.md`
- `docs/styles/extra.css`
- `docs/assets/css/style.css`
- `docs/overrides/main.html`
- `mkdocs.yml`

## Homepage layout architecture (current state)

- The homepage uses a persistent two-column wrapper: `.oasis-layout` containing `.oasis-sidebar` (tags) + `.oasis-main` (main content).
- The hero block (banner) **MUST** live inside `.oasis-layout > .oasis-main` to prevent overlap.
- Sidebar width is controlled by `--oasis-sidebar-w` (currently `300px`) and is enforced at desktop widths via flex sizing.
- Sidebar expansion is prevented via `overflow: hidden` and `max-width: 100%` on descendants.

### Required structure in `docs/index.md`

Keep the homepage shell in this form:

```html
<div class="oasis-layout" markdown="1">
  <aside class="oasis-sidebar" markdown="1">...</aside>
  <main class="oasis-main" markdown="1">
    <div class="esiil-banner oasis-hero" markdown="1">...</div>
    ...main homepage content...
  </main>
</div>
```

## Hero / header behavior rules (current working solution)

- The hero is “flush to header” using this scoped rule:

```css
.oasis-layout .oasis-main .oasis-hero {
  margin-top: calc(var(--md-header-height, 3rem) * -1);
  padding-top: var(--md-header-height, 3rem);
}
```

- We removed/avoided `100vw` full-bleed hero sizing and any `margin-left: calc(50% - 50vw)` tricks, because those caused hero underlap with the sidebar.
- If a pseudo-element is used for hero backgrounds, it must be confined to `.oasis-main` (not viewport width).

## Selector strategy (what to do / what NOT to do)

- Do **NOT** use `:has()` for homepage scoping (brittle + can silently fail in tooling and cause no-ops).
- Prefer scoping homepage-only rules using `.oasis-layout` as the homepage hook, since it only exists on `index.md`.
- For the white strip issue, do not target Material ancestor containers from inside `.oasis-layout`; those selectors cannot match.

### White-gap root cause (documented incident)

The visible white strip above the hero comes from MkDocs Material top padding on ancestor containers (for example, `.md-content__inner`). Since those containers are ancestors of homepage content, they cannot be reliably and safely overridden with descendant selectors from `.oasis-layout` without introducing brittle approaches.

Our chosen fix is to cancel that inherited top gap at the first homepage wrapper we control:

```css
.oasis-layout {
  margin-top: calc(var(--oasis-home-top-gap) * -1);
  padding-top: var(--oasis-home-top-gap);
}
```

This keeps homepage behavior explicit, structural, and maintainable while preserving internal layout flow.

## File responsibility boundaries

- `docs/styles/extra.css` is the final-authority **brand skin** layer.
- `docs/assets/css/style.css` should only contain legacy structural quirks (layout scaffolding), not aesthetic styling.
- Rule of thumb:
  - Visual/brand rule (color, surface, typography, polish, hero visual treatment) ➜ `extra.css`
  - Structural compatibility glue (legacy selectors needed for behavior/layout compatibility) ➜ `style.css`

Rationale: separating aesthetic intent from compatibility glue lowers regression risk when updating homepage visuals.

## Debug checklist / playbook

### If hero no longer touches header

1. Confirm hero negative margin/padding rule still exists on `.oasis-layout .oasis-main .oasis-hero`.
2. Confirm `.oasis-layout` top-gap cancellation is present (`margin-top` negative + matching `padding-top`).

### If hero overlaps sidebar

1. Confirm hero remains inside `.oasis-main` in `docs/index.md`.
2. Confirm no `100vw` or `calc(50% - 50vw)` hero sizing rules were introduced.
3. Confirm pseudo-element backgrounds are restricted to `.oasis-main` bounds.

### If white strip returns above hero

1. Check the value of `--oasis-home-top-gap` in `docs/styles/extra.css`.
2. Confirm it matches current Material top padding at the active breakpoint.
3. If needed, adjust the variable value or add a breakpoint override for `--oasis-home-top-gap`.

Do **not** reintroduce `:has()` or dead descendant selectors that try to target ancestor containers.

### If sidebar width changes unexpectedly

1. Check `--oasis-sidebar-w` in `docs/styles/extra.css`.
2. Check desktop flex-basis rule on `.oasis-sidebar`.
3. Check `overflow: hidden` and descendant `max-width: 100%` rules.

## Codex prompts we use

### 1) Change hero without reintroducing gap

```text
Update the homepage hero styling in docs/styles/extra.css.
Constraints:
- Homepage-only changes (scope via .oasis-layout)
- Do not use :has()
- Keep hero inside .oasis-layout > .oasis-main
- Preserve flush-header rule on .oasis-layout .oasis-main .oasis-hero
- Do not use 100vw or calc(50% - 50vw)
Validation:
- Run mkdocs build and mkdocs serve commands
- Report exactly which container padding resets were touched
```

### 2) Adjust sidebar width safely

```text
Change homepage sidebar width by editing --oasis-sidebar-w in docs/styles/extra.css.
Constraints:
- Homepage-only changes (scope via .oasis-layout)
- Do not use :has()
- Keep .oasis-sidebar flex-basis and width in sync with --oasis-sidebar-w
- Keep overflow: hidden and descendant max-width: 100%
Validation:
- Run mkdocs build and mkdocs serve commands
- Confirm hero does not overlap sidebar at desktop widths
```

### 3) Update hero background image/overlay

```text
Update the homepage hero background image/overlay in docs/styles/extra.css.
Constraints:
- Homepage-only changes (scope via .oasis-layout)
- Do not use :has()
- Keep .oasis-layout/.oasis-main structure unchanged
- Do not introduce 100vw full-bleed or calc(50% - 50vw) rules
- If using pseudo-elements, keep them confined to .oasis-main
Validation:
- Run mkdocs build and mkdocs serve commands
- Verify no white strip above hero
```

### 4) Header/safari tint experiments (notes only)

```text
Propose (do not apply) experiments for header + Safari theme tint behavior.
Constraints:
- Notes only; no functional CSS layout refactor
- Keep homepage rules scoped via .oasis-layout
- Avoid :has()
- Respect existing .oasis-layout/.oasis-main hero placement and flush-header rule
Output:
- 2-3 safe options with rollback notes
- Include mkdocs build/serve validation plan
```

## What changed and why

We iterated through homepage regressions (white top gap, hero/sidebar overlap, redundant sidebar layers, brittle selector scope) and stabilized on a layout-anchored approach:

- homepage hook = `.oasis-layout`
- hero constrained to `.oasis-main`
- white-gap cancellation handled at `.oasis-layout` using `--oasis-home-top-gap` (negative margin + matching padding)
- explicit split between brand skin (`extra.css`) and legacy structure glue (`style.css`)

This guide exists to preserve those decisions and prevent repeating the same regressions.

## Local testing note

- GitHub Pages deploys this site under `/home/`, but `mkdocs serve` runs the homepage at `/` locally.
- Do not test local homepage behavior at `/home/`; use `/` when validating layout fixes.
