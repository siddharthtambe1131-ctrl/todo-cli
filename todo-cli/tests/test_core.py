import pytest

from todo.core import add_task, clear_done, complete_task, delete_task


def test_add_task_assigns_incrementing_ids():
    tasks = []
    a = add_task(tasks, "First")
    b = add_task(tasks, "Second")
    assert (a["id"], b["id"]) == (1, 2)


def test_add_empty_title_fails():
    with pytest.raises(ValueError):
        add_task([], "   ")


def test_complete_and_delete():
    tasks = []
    add_task(tasks, "Write code")
    complete_task(tasks, 1)
    assert tasks[0]["done"] is True
    delete_task(tasks, 1)
    assert tasks == []


def test_missing_task_raises():
    with pytest.raises(KeyError):
        complete_task([], 99)


def test_clear_done():
    tasks = []
    add_task(tasks, "A")
    add_task(tasks, "B")
    complete_task(tasks, 1)
    assert clear_done(tasks) == 1
    assert len(tasks) == 1
