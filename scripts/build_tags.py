import os, re, json, yaml
from datetime import datetime, date as date_cls
from mkdocs_gen_files import open as gen_open, set_edit_path

DOCS_DIR = "docs"

def parse_front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    meta = yaml.safe_load(m.group(1)) or {}
    return meta if isinstance(meta, dict) else {}

def norm_date(d):
    """Return a datetime for sorting or None if invalid. Accepts datetime/date/str (YYYY-MM-DD)."""
    if isinstance(d, (datetime, date_cls)):
        # If it's a date (but not datetime), combine with midnight for consistency
        return datetime.combine(d, datetime.min.time()) if isinstance(d, date_cls) and not isinstance(d, datetime) else d
    try:
        return datetime.strptime(str(d), "%Y-%m-%d")
    except Exception:
        return None

pages = []
for root, _, files in os.walk(DOCS_DIR):
    for f in files:
        if f.endswith(".md"):
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8") as fh:
                txt = fh.read()
            meta = parse_front_matter(txt)
            tags = meta.get("tags") or []
            if isinstance(tags, str):
                tags = [tags]
            if tags:
                rel = os.path.relpath(p, DOCS_DIR).replace("\\", "/")
                title = meta.get("title") or os.path.splitext(os.path.basename(p))[0]
                date_val = meta.get("date", "")
                dt = norm_date(date_val)
                date_s = dt.strftime("%Y-%m-%d") if dt else (str(date_val) if date_val else "")
                weight = meta.get("weight", 0)
                try:
                    weight = float(weight)
                except Exception:
                    weight = 0.0
                pages.append({
                    "path": rel,
                    "title": title,
                    "tags": tags,
                    "date": date_s if date_s else "",
                    "weight": weight,
                    "_dt": dt.timestamp() if dt else 0.0
                })

# Build tag map
tagmap = {}
for pg in pages:
    for t in pg["tags"]:
        tagmap.setdefault(t, []).append(pg)

# Write tags.json for client-side UI
tags_sorted = sorted(tagmap.keys(), key=lambda x: x.lower())
json_payload = {
    "pages": [{k: v for k, v in p.items() if k != "_dt"} for p in pages],
    "tags": tags_sorted
}
with gen_open("assets/tags.json", "w") as f:
    json.dump(json_payload, f, indent=2, ensure_ascii=False)

# Generate per-tag markdown pages ranked by date desc then weight desc
for tag, items in tagmap.items():
    items_sorted = sorted(items, key=lambda x: (x["_dt"], x["weight"]), reverse=True)
    out_lines = [f"---\ntitle: {tag}\nhide:\n  - toc\n---\n", f"# {tag}\n"]
    for it in items_sorted:
        date_str = it["date"] if it["date"] else ""
        out_lines.append(f"- [{it['title']}](/{it['path']})  \n  <small>{date_str}</small>")
    out_path = f"tags/{tag}.md"
    with gen_open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))
    set_edit_path(out_path, out_path)
