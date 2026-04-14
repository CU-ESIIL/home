import re, sys, yaml
from pathlib import Path

ENFORCED_PREFIXES = ("docs/quickstart/", "docs/container-library/")

def check_file(path: Path):
    posix_path = path.as_posix()
    if not posix_path.startswith(ENFORCED_PREFIXES):
        return None
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return f"{path}: missing front matter"
    data = yaml.safe_load(m.group(1)) or {}
    errs = []
    if not data.get("tags"):
        errs.append("tags missing")
    if not data.get("date"):
        errs.append("date missing")
    if errs:
        return f"{path}: {'; '.join(errs)}"
    return None

def main(argv=None):
    paths = [Path(p) for p in (argv or sys.argv[1:])]
    errors = []
    for p in paths:
        if p.suffix != ".md" or not p.exists():
            continue
        err = check_file(p)
        if err:
            errors.append(err)
    if errors:
        print("\n".join(errors))
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
