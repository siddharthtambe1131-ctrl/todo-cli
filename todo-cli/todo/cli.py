import argparse
import sys

from . import __version__
from .core import add_task, clear_done, complete_task, delete_task
from .storage import load_tasks, save_tasks


def build_parser():
    parser = argparse.ArgumentParser(prog="todo", description="A simple CLI to-do manager.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("title", nargs="+", help="Task description")

    sub.add_parser("list", help="List all tasks")

    p_done = sub.add_parser("done", help="Mark a task as completed")
    p_done.add_argument("id", type=int)

    p_del = sub.add_parser("delete", help="Delete a task")
    p_del.add_argument("id", type=int)

    sub.add_parser("clear", help="Remove all completed tasks")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    tasks = load_tasks()

    try:
        if args.command == "add":
            task = add_task(tasks, " ".join(args.title))
            print(f"Added #{task['id']}: {task['title']}")
        elif args.command == "list":
            if not tasks:
                print("No tasks yet. Add one with: todo add \"Buy milk\"")
            for t in tasks:
                mark = "x" if t["done"] else " "
                print(f"[{mark}] #{t['id']}  {t['title']}  ({t['created']})")
        elif args.command == "done":
            task = complete_task(tasks, args.id)
            print(f"Completed #{task['id']}: {task['title']}")
        elif args.command == "delete":
            task = delete_task(tasks, args.id)
            print(f"Deleted #{task['id']}: {task['title']}")
        elif args.command == "clear":
            print(f"Removed {clear_done(tasks)} completed task(s).")
    except (ValueError, KeyError) as exc:
        print(f"Error: {exc.args[0]}", file=sys.stderr)
        return 1

    save_tasks(tasks)
    return 0


if __name__ == "__main__":
    sys.exit(main())
