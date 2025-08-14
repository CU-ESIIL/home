#!/usr/bin/env python3
import os, re, yaml
from datetime import datetime, date as date_cls

DOCS_DIR = "docs"
TAGS_DIR = os.path.join(DOCS_DIR, "tags")

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)

def parse_front_matter(text):
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return {}
    meta = yaml.safe_load(m.group(1)) or {}
    return meta if isinstance(meta, dict) else {}

def norm_date(d):
    if isinstance(d, (datetime, date_cls)):
        return datetime.combine(d, datetime.min.time()) if isinstance(d, date_cls) and not isinstance(d, datetime) else d
    try:
        return datetime.strptime(str(d), "%Y-%m-%d")
    except Exception:
        return None

pages = []
for root, _, files in os.walk(DOCS_DIR):
    for f in files:
        if not f.endswith(".md"):
            continue
        p = os.path.join(root, f)
        if p.startswith(TAGS_DIR):
            continue
        with open(p, "r", encoding="utf-8") as fh:
            txt = fh.read()
        meta = parse_front_matter(txt)
        tags = meta.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]
        if not tags:
            continue
        rel = os.path.relpath(p, DOCS_DIR).replace("\\", "/")
        title = meta.get("title") or os.path.splitext(os.path.basename(p))[0]
        date_val = meta.get("date", "")
        dt = norm_date(date_val)
        date_str = dt.strftime("%Y-%m-%d") if dt else (str(date_val) if date_val else "")
        weight = meta.get("weight", 0)
        try:
            weight = float(weight)
        except Exception:
            weight = 0.0
        pages.append({
            "path": rel,
            "title": title,
            "tags": tags,
            "date": date_str,
            "weight": weight,
            "_dt": dt.timestamp() if dt else 0.0
        })

# Build tag map
tagmap = {}
for pg in pages:
    for t in pg["tags"]:
        tagmap.setdefault(t, []).append(pg)

os.makedirs(TAGS_DIR, exist_ok=True)

# Write index page
index_lines = ["---", "title: Tags", "hide:", "  - toc", "---", "", "# Tags", ""]
for tag in sorted(tagmap.keys(), key=lambda x: x.lower()):
    index_lines.append(f"- [{tag}]({tag}.md)")
with open(os.path.join(TAGS_DIR, "index.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(index_lines))

# Write per-tag pages
for tag, items in tagmap.items():
    items_sorted = sorted(items, key=lambda x: (x["_dt"], x["weight"]), reverse=True)
    lines = ["---", f"title: {tag}", "hide:", "  - toc", "---", "", f"# {tag}", ""]
    for it in items_sorted:
        date_str = it["date"] if it["date"] else ""
        lines.append(f"- [{it['title']}](/{it['path']})  \n  <small>{date_str}</small>")
    with open(os.path.join(TAGS_DIR, f"{tag}.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
