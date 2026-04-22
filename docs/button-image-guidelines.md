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

OASIS button images should look like scientific print artifacts, not generic
software icons. The visual language should feel handcrafted, ecological,
research-oriented, and slightly imperfect.

The intended family is:

- screen print
- linocut
- woodblock-inspired scientific illustration

The intended family is not:

- glossy interface art
- corporate SaaS illustration
- generic AI icon generation
- clean flat vector symbol sets

## Core visual style

Required style characteristics:

- square format
- one clear concept per image
- print-inspired scientific illustration
- subtle texture and slight imperfection
- muted palette built from cream, green, and dark ink tones
- strong readability at homepage thumbnail size

Default style shorthand:

`screen print / linocut / woodblock inspired scientific illustration, square image, cream paper, muted greens, dark ink, slight print texture, one clear subject, no text`

## Composition rules

- Use a square canvas.
- Show one dominant subject or one tightly unified concept.
- Build around a readable focal structure.
- Prioritize recognition at small scale.
- Use negative space intentionally.
- Keep supporting details subordinate to the main idea.
- Use one primary scene plus at most one or two subordinate analytic elements.
- Prefer a central subject with a small number of contextual elements.
- Avoid multi-panel or collage-like layouts unless the content truly requires a
  synthesis scene.

## Color palette guidance

Primary palette:

- dark ink: charcoal, deep green-black, forest ink
- light ground: cream, warm ivory, parchment
- secondary tones: muted sage, moss, olive, subdued eucalyptus

Optional accent use:

- restrained earthy rust
- restrained dusty blue-green

Avoid:

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
- Represent the real domain, workflow, or scientific theme.
- Prefer concrete environmental data science subjects over abstract symbols.
- For collaboration-oriented buttons, show collaboration in the context of
  science, fieldwork, maps, data, or synthesis.
- For data or compute buttons, combine computing with the domain subject when
  possible.
- Avoid generic symbols when a content-specific subject is available.

## What the image should communicate

Each image should communicate:

- what this content is about
- what kind of scientific or technical work it represents
- the domain or theme behind the destination

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
- shiny 3D render style
- sterile flat vector icon packs
- random symbol collages
- fields of tiny floating icons without one dominant scene
- unrelated scientific icons mashed together
- meme aesthetics
- mascot or emoji style

## Prompt template for image generation

```text
Create a square homepage button image for OASIS.
Subject: [specific content-derived subject].
Style: screen print / linocut / woodblock inspired scientific illustration.
Composition: one clear concept, strong focal structure, readable at thumbnail size.
Texture: subtle paper grain, imperfect ink, carved or printed linework, not clean vector.
Palette: cream background, muted greens, dark ink tones, restrained earthy accent only if needed.
Mood: thoughtful, research-oriented, ecological, content-specific.
Constraints: no text, no logos, no photorealism, no glossy UI icon style, no corporate SaaS look.
```

## Negative prompt template

```text
text, letters, logo, photorealism, glossy icon, app icon, clean flat vector, SaaS illustration, shiny 3D render, neon colors, futuristic dashboard, corporate tech branding, emoji style, mascot, clutter, unrelated symbols, infographic, stock icon set
```

## Example prompts

### 1. Working group wildfire theme

```text
Create a square homepage button image for OASIS.
Subject: a wildfire boundary research scene showing ecological burn patterns, landscape edges, and analysis structure.
Style: screen print / linocut / woodblock inspired scientific illustration.
Composition: one clear focal concept, readable at thumbnail size.
Texture: subtle paper grain, imperfect ink, carved linework.
Palette: cream paper, muted greens, dark ink, restrained earthy rust.
Constraints: no text, no logos, no photorealism, no glossy UI icon style, no corporate SaaS look.
```

### 2. Analytics resource

```text
Create a square homepage button image for OASIS.
Subject: environmental data analysis combining a map surface, ecological forms, and a simple plot in one coherent printed scene.
Style: screen print / linocut / woodblock inspired scientific illustration.
Composition: one integrated concept, not a symbol collage.
Texture: printed ink texture and carved contours.
Palette: cream, sage, moss, dark ink.
Constraints: no text, no logos, no photorealism, no glossy interface icon style.
```

### 3. Working-group collaboration

```text
Create a square homepage button image for OASIS.
Subject: a small group of researchers gathered around environmental data, field observations, and synthesis materials.
Style: screen print / woodblock scientific illustration.
Composition: one central collaboration scene with a small number of supporting scientific details.
Texture: imperfect ink and paper grain.
Palette: cream, muted greens, dark ink.
Constraints: no text, no generic network iconography, no corporate illustration style.
```

### 4. Education or quickstart

```text
Create a square homepage button image for OASIS.
Subject: a learner-oriented environmental data science scene with notebook, map, and analysis marks arranged as one coherent printed composition.
Style: linocut / woodblock inspired scientific illustration.
Composition: one clear concept, readable at small scale.
Palette: cream paper, muted greens, dark ink.
Constraints: no text, no photorealism, no glossy UI icon style.
```

### 5. Container or compute infrastructure

```text
Create a square homepage button image for OASIS.
Subject: environmental computing infrastructure represented through containers, data flow, and scientific analysis tools as one coherent ecological-computation scene.
Style: screen print / linocut / woodblock inspired scientific illustration.
Composition: one clear infrastructure concept, readable at thumbnail size.
Texture: subtle print grain, imperfect ink.
Palette: cream, muted green family, dark ink.
Constraints: no text, no logos, no generic cloud icon cluster, no glossy UI icon style.
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
- Does the image match the OASIS print-inspired family?
- Does the image communicate the real content intent?
- Is the palette limited and muted?
- Is there visible texture and slight imperfection?
- Is the image readable at homepage thumbnail size?
- Is there no text inside the image?
- Does it avoid photorealism, glossy UI icon style, and corporate SaaS look?
- Is the asset saved in the correct directory?
- Does the filename follow the new-asset convention?

## Codex instructions for generating images

Before generating or replacing any button image, Codex must:

1. Read this file in full.
2. Inspect existing button images in `docs/assets/thumbnails/`.
3. Derive the subject from the actual content.
4. Use the prompt template from this document.
5. Use the negative prompt template when supported.
6. Prefer the simpler composition if multiple ideas compete.
7. Save the asset using the correct path and naming convention.
8. Verify consistency before committing.

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
