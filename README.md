# OASIS Home

This repository powers the OASIS homepage and supporting documentation for the
Open Analysis and Synthesis Infrastructure for Science. It is a MkDocs site
with a dense single-page homepage, supporting quickstarts, resource hubs, and
tag-driven discovery pages.

## Local development

Create and activate a virtual environment if you want an isolated Python setup,
then install the site requirements and start the local server:

```bash
pip install -r requirements.txt
mkdocs serve
```

The local site is typically available at `http://127.0.0.1:8000/`.

## Build and deploy

Use a strict local build before opening a pull request:

```bash
mkdocs build --strict
```

GitHub Actions runs the same strict build before publishing with
`mkdocs gh-deploy`, so deploys cannot bypass build failures.

## Homepage/layout development guidance

For homepage architecture, hero/sidebar/header CSS rules, selector strategy,
and Codex-safe prompts, use the canonical dev guide:

- [`docs/dev/oasis-site-dev-guide.md`](docs/dev/oasis-site-dev-guide.md)
