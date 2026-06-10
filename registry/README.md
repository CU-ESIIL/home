# ESIIL Registry

This directory is the source of truth for the static ESIIL metadata graph used
by the OASIS MkDocs site.

## What lives here

- `projects/`: project, event, library, and hub metadata
- `people/`: individual or group contributor records
- `themes/`: cross-cutting topical categories
- `datasets/`: named datasets or data collections
- `schema/`: human-readable schema documentation

## How to add a new project

1. Create a new YAML file in `registry/projects/`.
2. Follow the schema in `registry/schema/project-schema.md`.
3. Use a stable lowercase kebab-case `id`.
4. Reference existing `people`, `themes`, `datasets`, and
   `related_projects` by id.
5. Keep `methods` and `outputs` as short descriptive strings.
6. Run:

```bash
python scripts/build_graph.py
pytest tests/test_build_graph.py
```

7. Verify:
   - `docs/assets/data/esiil_graph.json` updated cleanly
   - `docs/explore/themes/` pages render as expected
   - `mkdocs build --strict` succeeds

## Notes

- This system is intentionally static-site friendly.
- No database or hosted graph service is used.
- Generated pages under `docs/explore/themes/` should be rebuilt from registry
  content rather than hand-edited.
