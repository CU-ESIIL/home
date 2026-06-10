# Project Schema

Each YAML file in `registry/projects/` must contain the following fields:

```yaml
id: example-project
title: Example Project
description: Short human-readable summary.
type: working-group
status: active
website: https://example.org/
repository: https://github.com/CU-ESIIL/example-project
people:
  - esiil-staff
themes:
  - data-infrastructure
datasets:
  - example-dataset
methods:
  - data cubes
outputs:
  - training materials
related_projects:
  - another-project
```

## Field notes

- `id`: stable lowercase kebab-case identifier
- `title`: public display title
- `description`: concise summary of the project or resource
- `type`: category such as `working-group`, `research-project`, `event`,
  `library`, `training`, or `hub`
- `status`: `active`, `planned`, `archived`, or another short lifecycle label
- `website`: canonical public website URL, or empty string if none
- `repository`: canonical GitHub repository URL, or empty string if none
- `people`: list of ids from `registry/people/`
- `themes`: list of ids from `registry/themes/`
- `datasets`: list of ids from `registry/datasets/`
- `methods`: plain-language method labels; these become graph nodes
- `outputs`: plain-language output labels; these become graph nodes
- `related_projects`: list of ids from `registry/projects/`
