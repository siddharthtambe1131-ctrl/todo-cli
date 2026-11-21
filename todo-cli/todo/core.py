from datetime import datetime


def add_task(tasks, title):
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty.")
    next_id = max((t["id"] for t in tasks), default=0) + 1
    task = {
        "id": next_id,
        "title": title,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    return task


def _find(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise KeyError(f"No task with id {task_id}.")


def complete_task(tasks, task_id):
    task = _find(tasks, task_id)
    task["done"] = True
    return task


def delete_task(tasks, task_id):
    task = _find(tasks, task_id)
    tasks.remove(task)
    return task


def clear_done(tasks):
    remaining = [t for t in tasks if not t["done"]]
    removed = len(tasks) - len(remaining)
    tasks[:] = remaining
    return removed
