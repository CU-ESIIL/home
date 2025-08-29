import yaml
from datetime import datetime
import argparse
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEV_SCHEDULE_PATH = ROOT / 'docs' / 'dev-schedule.md'
TASKS_PATH = ROOT / 'docs' / 'upcoming_tasks.yaml'

def load_tasks(path=TASKS_PATH):
    with open(path) as f:
        data = yaml.safe_load(f)
    return data.get('upcoming_tasks', [])

def format_upcoming(tasks):
    lines = []
    for t in tasks:
        link = f"https://github.com/CU-ESIIL/home/issues/{t['issue']}"
        lines.append(f"- [ ] [{t['title']}]({link})")
    return "\n".join(lines)

def format_gantt(tasks):
    lines = []
    for i, t in enumerate(tasks, 1):
        start = datetime.strptime(str(t['start']), '%Y-%m-%d')
        end = datetime.strptime(str(t['end']), '%Y-%m-%d')
        duration = (end - start).days + 1
        status = ':active,' if t.get('active') else ':'
        lines.append(f"    {t['title']}  {status} plan{i}, {t['start']}, {duration}d")
    return "\n".join(lines)

def replace_section(content, start_marker, end_marker, replacement):
    pattern = re.compile(
        rf"({re.escape(start_marker)}\n)(.*?)(\n{re.escape(end_marker)})",
        re.DOTALL,
    )
    return pattern.sub(rf"\1{replacement}\3", content)

def update_dev_schedule(dev_path=DEV_SCHEDULE_PATH, tasks_path=TASKS_PATH):
    tasks = load_tasks(tasks_path)
    content = dev_path.read_text()
    content = replace_section(
        content,
        '<!-- upcoming-start -->',
        '<!-- upcoming-end -->',
        format_upcoming(tasks),
    )
    content = replace_section(
        content,
        '<!-- gantt-start -->',
        '<!-- gantt-end -->',
        format_gantt(tasks),
    )
    dev_path.write_text(content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update dev-schedule.md from YAML')
    parser.add_argument('--tasks', default=TASKS_PATH, help='Path to tasks YAML')
    parser.add_argument('--doc', default=DEV_SCHEDULE_PATH, help='Path to dev-schedule.md')
    args = parser.parse_args()
    update_dev_schedule(pathlib.Path(args.doc), pathlib.Path(args.tasks))
