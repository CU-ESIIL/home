import yaml
from datetime import datetime, timedelta
import argparse
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TASKS_PATH = ROOT / 'docs' / 'upcoming_tasks.yaml'


def load_tasks(path=TASKS_PATH):
    with open(path) as f:
        data = yaml.safe_load(f) or {}
    return data.get('upcoming_tasks', [])


def save_tasks(tasks, path=TASKS_PATH):
    with open(path, 'w') as f:
        yaml.dump({'upcoming_tasks': tasks}, f, sort_keys=False)


def next_start_date(tasks):
    if not tasks:
        return datetime.today().date()
    last_end = max(datetime.strptime(str(t['end']), '%Y-%m-%d').date() for t in tasks)
    return last_end + timedelta(days=1)


def add_task(title, issue, duration):
    tasks = load_tasks()
    start = next_start_date(tasks)
    end = start + timedelta(days=duration - 1)
    tasks.append({
        'title': title,
        'issue': issue,
        'start': start.strftime('%Y-%m-%d'),
        'end': end.strftime('%Y-%m-%d'),
    })
    save_tasks(tasks)
    # Update development schedule to include the new task
    try:
        from update_dev_schedule import update_dev_schedule
        update_dev_schedule()
    except Exception as e:
        print(f"Warning: failed to update dev schedule: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Append a task to upcoming_tasks.yaml')
    parser.add_argument('title', help='Task title')
    parser.add_argument('issue', type=int, help='GitHub issue number')
    parser.add_argument('--duration', type=int, default=1, help='Task length in days')
    args = parser.parse_args()
    add_task(args.title, args.issue, args.duration)
