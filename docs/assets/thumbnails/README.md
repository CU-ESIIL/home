# Thumbnail System

This directory stores the thumbnail-management system for the OASIS homepage and gallery pages.

## Purpose

The goal is to keep thumbnail work durable and reversible. The live site can point at a single active thumbnail set while older sets remain preserved for comparison, rollback, or regeneration.

## Key files

- `docs/thumbnail-system/project-thumbnail-index.md`: human-readable inventory of major thumbnail-backed links, what each destination is about, and what a future replacement image should communicate.
- `docs/assets/thumbnails/thumbnail-manifest.yml`: machine-readable manifest of stable thumbnail IDs, current active paths, original paths, and set locations.
- `docs/assets/thumbnails/originals/`: preserved copy of the original homepage thumbnail collection.
- `docs/assets/thumbnails/sets/set-001-originals/`: first tracked set, matching the original thumbnails.
- `docs/assets/thumbnails/sets/set-002-generated/`: placeholder for the next generated set.
- `docs/assets/thumbnails/active/`: files currently referenced by the site.
- `docs/assets/thumbnails/style-guides/`: reference panels or visual guide images for future thumbnail-generation prompts.

## Current layout

The current active set is a copied version of the original homepage thumbnails. The legacy source files under `docs/assets/homepage/` are still preserved and were not deleted.

## How to switch the active thumbnail set

1. Choose a set directory under `docs/assets/thumbnails/sets/`.
2. Copy that set into `docs/assets/thumbnails/active/` while preserving the same relative subfolders and filenames.
3. Update `docs/assets/thumbnails/thumbnail-manifest.yml` so `active_thumbnail` and the set metadata match the live set.
4. Run a strict build and visually inspect the homepage and directory pages.

## How to add a new thumbnail set

1. Read `docs/thumbnail-system/project-thumbnail-index.md`.
2. Generate a complete new thumbnail set using the descriptions and the current visual guidance.
3. Save the generated thumbnails into `docs/assets/thumbnails/sets/set-00X-name/`.
4. Copy that set into `docs/assets/thumbnails/active/`.
5. Update `docs/assets/thumbnails/thumbnail-manifest.yml`.
6. Run `mkdocs build --strict`.
7. Visually inspect the homepage and directory pages.

## Validation checklist

- Run `mkdocs build --strict`.
- Run `npx playwright test` if the link-and-image smoke tests are available locally.
- Spot-check the homepage plus `/directory/working-groups/`, `/directory/research/`, `/directory/events/`, and `/directory/infrastructure/`.
- Confirm there are no broken image paths by searching rendered HTML or using the existing Playwright image-resolution check.

## Notes on style guides

Store future reference panels in `docs/assets/thumbnails/style-guides/`. If a future thumbnail set intentionally changes visual direction, such as moving toward pure-white backgrounds and layered 3D relief forms, document that change in the relevant prompt materials before replacing the active set.
