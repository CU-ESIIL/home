---
title: Button Image Guidelines
tags: [development]
date: 2026-04-21
---

# Button Image Guidelines

## Purpose

This document is the authoritative standard for homepage button images in the
OASIS repository. It exists to keep button imagery visually durable, content
specific, and consistent with the existing OASIS homepage image family.

Use these rules for any newly generated button image and for any replacement of
an existing button image.

## Design intent

OASIS button images should look like minimal scientific screen-print panels,
not generic software icons, not centered badges, and not small illustrations.
The visual language should feel abstract, legible, research-oriented, and
slightly imperfect.

The intended family is:

- minimal scientific screen-print panel
- mid-century scientific infographic plus logo hybrid
- bold geometric symbolic composition distributed across a square tile

The intended family is not:

- glossy interface art
- corporate SaaS illustration
- generic AI icon generation
- scenic illustration
- miniature poster art
- centered logo or badge layouts

## Core visual style

Required style characteristics:

- square format
- one clear concept per image
- completely flat composition with no perspective
- symbolic designed panel, not an illustrated scene
- subtle texture and slight imperfection
- restrained 3 to 4 color palette
- strong readability at homepage thumbnail size
- visual weight distributed across the square

Default style shorthand:

`minimal scientific screen-print panel, square image, completely flat, highly abstract and symbolic, 2 to 4 connected elements, edge-filled composition, strong negative space, cream paper, navy or teal structure, muted red or orange or blue accents, slight print texture, no text`

## Composition rules

- Use a square canvas.
- Show one dominant element and at most one or two supporting elements.
- Build around a readable focal structure with strong negative space.
- Prioritize recognition at small scale.
- Keep supporting details subordinate to the main idea.
- Distribute visual weight across the whole square.
- Anchor at least one element to an edge.
- Extend shapes toward edges or corners.
- Connect or overlap elements into one composition.
- Use directional flow when helpful, such as left to right, bottom to top, or diagonal.
- Use only 2 to 4 large elements.
- Reduce complexity aggressively.
- Avoid centered icon layouts, empty margins, and collage-like layouts.

## Color palette guidance

Primary palette:

- dark structure: navy, dark teal, or deep blue-green
- light ground: cream, warm ivory, parchment
- accent 1: muted red, rust, or orange
- accent 2: muted teal, blue, or cyan
- optional accent 3: muted gold or ochre

Palette rule:

- Most new images should use 3 to 4 colors maximum including the dark
  structural ink.
- Prefer navy or teal structure with restrained red, orange, or blue accents.
- Avoid brown-heavy palettes.
- Use contrast intentionally so the image reads at small size.

Avoid:

- monochrome treatments unless replacing a legacy asset that already depends on it
- brown-heavy palettes
- neon greens
- bright tech blues and purples
- glossy gradients
- rainbow palettes
- white-on-brand-color icon treatment

## Texture and linework

- Texture should suggest ink on paper.
- Linework should feel carved, printed, hatched, or block-pressed.
- Slight irregularity is desirable.
- Perfectly smooth vector edges are undesirable.
- Use print grain, hatch, contour, or stipple where helpful.
- Texture must support legibility, not overwhelm it.

## Subject selection rules

- Derive the subject from the actual content of the button.
- Inspect the linked page or repository README when available before deciding
  what the image depicts.
- First represent the core process or question.
- Second represent the key method or data structure.
- Include biology only if it is central and scientifically accurate.
- Prefer symbols over scenes.
- Prefer dots, grids, lines, blocks, arrows, boundaries, networks, and simple
  glyphs.
- Avoid generic symbols when a content-specific symbolic encoding is available.

## What the image should communicate

Each image should communicate:

- what this content is about
- what kind of scientific or technical work it represents
- the domain or theme behind the destination
- the core process first
- the key method or data structure second
- a connected designed surface rather than a floating icon

The image should not merely communicate:

- “button”
- “technology”
- “project”

It should communicate intent, not category alone.

## Do not do this

Do not use:

- text inside images
- photorealism
- glossy UI icon style
- corporate SaaS icon look
- generic AI defaults
- scenic layouts
- perspective or angled views
- 3D or isometric forms
- circular or badge-like layouts
- large empty borders
- disconnected icons sitting apart from each other
- sterile flat vector icon packs
- random symbol collages
- fields of tiny floating icons without one dominant symbol
- multi-panel dashboards
- overly detailed drawings
- decorative nature scenes
- generic plants or animals
- meme aesthetics
- mascot or emoji style

## Prompt template for image generation

```text
Create a square homepage button image for OASIS.
Subject: [one sentence science summary].
Primary symbol: [core process].
Supporting symbol: [key method or data structure].
Optional biology: [only if central and accurate].
Style: minimal scientific screen-print panel, mid-century scientific infographic plus logo hybrid.
Composition: completely flat, highly abstract and symbolic, readable instantly at small size, 2 to 4 large connected elements, edge-filled square tile, strong negative space, no centered badge layout.
Texture: cream paper, subtle paper grain, light ink texture or halftone, slightly imperfect edges, no gradients.
Palette: 3 to 4 colors maximum including navy or teal structure and muted red or orange or blue accents.
Constraints: no text, no logos, no perspective, no 3D, no scenes, no circular layout, no empty margins, no illustrative layout, no photorealism, no glossy UI icon style, no corporate SaaS look.
```

## Negative prompt template

```text
text, letters, logo, photorealism, glossy icon, app icon, SaaS illustration, shiny 3D render, perspective, isometric, scene, landscape, dashboard, centered logo, circular badge, large empty margin, disconnected icons, clutter, decorative plants, decorative animals, unrelated symbols, infographic panel, stock icon set, muddy brown palette, smooth gradients
```

## Example prompts

### 1. Working group wildfire theme

```text
Create a square homepage button image for OASIS.
Subject: wildfire boundary analysis across landscapes.
Primary symbol: a bold irregular boundary edge.
Supporting symbol: a grid and one directional analysis mark.
Optional biology: none.
Style: minimal scientific screen-print emblem, mid-century scientific infographic plus logo hybrid.
Composition: completely flat, highly abstract and symbolic, 2 to 4 connected elements, edge-filled square tile, strong negative space.
Texture: cream paper, light ink texture, slightly imperfect edges.
Palette: navy structure with muted rust and teal accents.
Constraints: no text, no perspective, no scenery, no photorealism.
```

### 2. Analytics resource

```text
Create a square homepage button image for OASIS.
Subject: environmental data analysis.
Primary symbol: a simple plot line crossing a gridded map block.
Supporting symbol: a small node cluster or data dots.
Optional biology: none.
Style: minimal scientific screen-print emblem, mid-century scientific infographic plus logo hybrid.
Composition: flat, edge-filled, 2 to 4 connected elements, strong negative space.
Texture: cream paper, light ink texture.
Palette: dark teal structure with muted blue and orange accents.
Constraints: no text, no dashboard layout, no photorealism.
```

### 3. Working-group collaboration

```text
Create a square homepage button image for OASIS.
Subject: collaborative synthesis around environmental data.
Primary symbol: a central circular meeting or synthesis mark.
Supporting symbol: one network arc and one plot or grid.
Optional biology: none.
Style: minimal scientific screen-print emblem, mid-century scientific infographic plus logo hybrid.
Composition: flat, symbolic, 2 to 4 connected elements, edge-filled square tile, strong negative space.
Texture: imperfect ink and paper grain.
Palette: navy structure with muted red and teal accents.
Constraints: no text, no scenic figures, no corporate illustration style.
```

### 4. Education or quickstart

```text
Create a square homepage button image for OASIS.
Subject: learning environmental data science methods.
Primary symbol: an open book or lesson block.
Supporting symbol: a grid, plot line, or branching method arrow.
Optional biology: none.
Style: minimal scientific screen-print emblem, mid-century scientific infographic plus logo hybrid.
Composition: flat, symbolic, 2 to 4 connected elements, edge-filled square tile, strong negative space.
Palette: dark teal structure with muted orange and blue accents.
Constraints: no text, no scenes, no photorealism.
```

### 5. Container or compute infrastructure

```text
Create a square homepage button image for OASIS.
Subject: environmental computing infrastructure.
Primary symbol: one container or modular block.
Supporting symbol: a simple data-flow arrow and one grid or plot.
Optional biology: none.
Style: minimal scientific screen-print emblem, mid-century scientific infographic plus logo hybrid.
Composition: flat, symbolic, 2 to 4 connected elements, edge-filled square tile, strong negative space.
Texture: subtle print grain, imperfect ink.
Palette: navy or teal structure with muted orange and blue accents.
Constraints: no text, no logos, no scenic layouts, no glossy UI icon style.
```

## Filename and asset conventions

Detected existing repository pattern:

- homepage button imagery is already stored in `docs/assets/thumbnails/`
- existing filenames are mixed legacy names and formats

Authoritative rule for new button-image assets:

- place new assets in `docs/assets/thumbnails/`
- do not rename legacy assets solely to enforce the new convention
- for new generated assets, use lowercase kebab-case
- prefer `.png` for newly generated button images
- for new generated assets, use the suffix `-button.png` unless intentionally
  replacing an established legacy filename already referenced in the site

Examples:

- `wildfire-boundary-button.png`
- `analytics-library-button.png`
- `graduate-student-button.png`

## Review checklist before committing

- Is the image square?
- Is there one clear concept?
- Does the image match the OASIS emblem-like scientific print family?
- Does the image communicate the real content intent?
- Is the composition completely flat with no perspective?
- Is the image built from only 2 to 4 large elements?
- Does the image encode process first and method second?
- Does the composition fill the square instead of behaving like a centered logo?
- Are the elements connected or interacting rather than floating independently?
- Does at least one element reach toward an edge or corner?
- Is the palette limited, balanced, and not brown-heavy?
- Is there visible texture and slight imperfection?
- Is the image readable at homepage thumbnail size?
- Is there no text inside the image?
- Does it avoid scenes, photorealism, glossy UI icon style, and corporate SaaS look?
- Is the asset saved in the correct directory?
- Does the filename follow the new-asset convention?

## Codex instructions for generating images

Before generating or replacing any button image, Codex must:

1. Read this file in full.
2. Inspect existing button images in `docs/assets/thumbnails/`.
3. Write a one-sentence subject summary.
4. Define the primary symbol, supporting symbol, and optional biology.
5. Derive the image from the actual content.
6. Use the prompt template from this document.
5. Use the negative prompt template when supported.
7. Prefer the simpler composition if multiple ideas compete.
8. Save the asset using the correct path and naming convention.
9. Verify consistency before committing.

## Notes on consistency with homepage

The homepage currently contains many legacy images, but the most coherent
visual thread is:

- square scientific scenes
- muted palettes
- print-like texture
- concept-specific subject matter

New assets should strengthen that thread. Do not introduce a parallel style
system.

## Codex operating rule

This file is authoritative for button-image generation in this repository.
Codex and all other agents must follow it when creating, replacing, or revising
homepage button images.
