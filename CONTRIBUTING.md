# Contributing

## Tagging content

Pages that should appear in the tag browser must begin with YAML front matter:

```yaml
---
title: Your Page Title
tags: [tag1, tag2]
date: 2024-01-01  # YYYY-MM-DD
weight: 0.0       # optional, higher ranks first
---
```

- **tags** – one or more keywords used to categorize the page.
- **date** – publication date used for recency sorting.
- **weight** – optional float to boost important pages.

Run `pre-commit run --files <file.md>` before committing to ensure the metadata
is present.
