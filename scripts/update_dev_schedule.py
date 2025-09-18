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
        data = yaml.safe_load(f) or {}
    upcoming = data.get('upcoming_tasks', [])
    completed = data.get('completed_tasks', [])
    return upcoming, completed

def format_upcoming(tasks):
    lines = []
    for t in tasks:
        link = f"https://github.com/CU-ESIIL/home/issues/{t['issue']}"
        lines.append(f"- [ ] [{t['title']}]({link})")
    return "\n".join(lines)

def _task_status(task, default_status):
    if 'status' in task:
        return f":{task['status']},"
    if task.get('active'):
        return ':active,'
    return default_status

def _format_gantt_tasks(tasks, start_index, default_status):
    lines = []
    for offset, t in enumerate(tasks):
        start = datetime.strptime(str(t['start']), '%Y-%m-%d')
        end = datetime.strptime(str(t['end']), '%Y-%m-%d')
        duration = (end - start).days + 1
        status = _task_status(t, default_status)
        lines.append(
            f"    {t['title']}  {status} plan{start_index + offset}, {t['start']}, {duration}d"
        )
    return lines

def format_gantt(upcoming, completed):
    lines = []
    counter = 1
    if completed:
        lines.append('    section Completed')
        completed_lines = _format_gantt_tasks(completed, counter, ':done,')
        lines.extend(completed_lines)
        counter += len(completed_lines)
    if upcoming:
        lines.append('    section Upcoming')
        upcoming_lines = _format_gantt_tasks(upcoming, counter, ':')
        lines.extend(upcoming_lines)
    return "\n".join(lines)

def replace_section(content, start_marker, end_marker, replacement):
    pattern = re.compile(
        rf"({re.escape(start_marker)}\n)(.*?)(\n{re.escape(end_marker)})",
        re.DOTALL,
    )
    return pattern.sub(rf"\1{replacement}\3", content)

def update_dev_schedule(dev_path=DEV_SCHEDULE_PATH, tasks_path=TASKS_PATH):
    upcoming, completed = load_tasks(tasks_path)
    content = dev_path.read_text()
    content = replace_section(
        content,
        '<!-- upcoming-start -->',
        '<!-- upcoming-end -->',
        format_upcoming(upcoming),
    )
    content = replace_section(
        content,
        '%% gantt-start',
        '%% gantt-end',
        format_gantt(upcoming, completed),
    )
    dev_path.write_text(content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update dev-schedule.md from YAML')
    parser.add_argument('--tasks', default=TASKS_PATH, help='Path to tasks YAML')
    parser.add_argument('--doc', default=DEV_SCHEDULE_PATH, help='Path to dev-schedule.md')
    args = parser.parse_args()
    update_dev_schedule(pathlib.Path(args.doc), pathlib.Path(args.tasks))
