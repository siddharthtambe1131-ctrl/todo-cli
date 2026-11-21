import json
from pathlib import Path

DEFAULT_FILE = Path.home() / ".todo_cli.json"


def load_tasks(path=DEFAULT_FILE):
    path = Path(path)
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return []


def save_tasks(tasks, path=DEFAULT_FILE):
    Path(path).write_text(json.dumps(tasks, indent=2))
