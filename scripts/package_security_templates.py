#!/usr/bin/env python3
"""Rebuild the downloadable OASIS security pack from its checked-in sources."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main():
    directory = Path(__file__).resolve().parents[1] / 'docs/assets/security-templates'
    templates = sorted(directory.glob('*.md'))
    if len(templates) != 10:
        raise SystemExit('Expected exactly ten Markdown security templates')
    sources = templates + [directory / 'synthetic-envelope.py']
    destination = directory / 'oasis-security-templates.zip'
    with ZipFile(destination, 'w', ZIP_DEFLATED) as archive:
        for source in sources:
            # Stable timestamps and permissions keep unchanged builds identical.
            info = ZipInfo(source.name, (2026, 10, 9, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())
    print(f'Packaged {len(sources)} files: {destination}')


if __name__ == '__main__':
    main()
