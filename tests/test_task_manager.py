# tests/test_task_manager.py

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from task_manager import Task, TaskManager


# ──────────────────────────────────────────────
# Fixtures
# ──────────────────────────────────────────────

@pytest.fixture
def manager():
    return TaskManager()


@pytest.fixture
def manager_with_tasks():
    m = TaskManager()
    m.add_task("Buy groceries", "Milk and eggs")
    m.add_task("Write report", "Q1 summary")
    m.add_task("Fix login bug", "Auth module issue")
    return m


# ──────────────────────────────────────────────
# Tests: Task Creation
# ──────────────────────────────────────────────

def test_add_task_basic(manager):
    task = manager.add_task("Test task")
    assert task.title == "Test task"
    assert task.status == "pending"
    assert task.task_id == 1


def test_add_task_with_description(manager):
    task = manager.add_task("Task A", description="Details here")
    assert task.description == "Details here"


def test_add_task_empty_title_raises(manager):
    with pytest.raises(ValueError):
        manager.add_task("")


def test_add_task_whitespace_title_raises(manager):
    with pytest.raises(ValueError):
        manager.add_task("   ")


def test_add_multiple_tasks_increments_id(manager):
    t1 = manager.add_task("First")
    t2 = manager.add_task("Second")
    assert t2.task_id == t1.task_id + 1


# ──────────────────────────────────────────────
# Tests: Completing Tasks
# ──────────────────────────────────────────────

def test_complete_task(manager_with_tasks):
    task = manager_with_tasks.complete_task(1)
    assert task.status == "completed"
    assert task.completed_at is not None


def test_complete_nonexistent_task_raises(manager):
    with pytest.raises(KeyError):
        manager.complete_task(999)


# ──────────────────────────────────────────────
# Tests: Deleting Tasks
# ──────────────────────────────────────────────

def test_delete_task(manager_with_tasks):
    manager_with_tasks.delete_task(1)
    assert manager_with_tasks.get_task(1) is None


def test_delete_nonexistent_task_raises(manager):
    with pytest.raises(KeyError):
        manager.delete_task(999)


def test_task_count_after_delete(manager_with_tasks):
    before = manager_with_tasks.task_count()
    manager_with_tasks.delete_task(1)
    assert manager_with_tasks.task_count() == before - 1


# ──────────────────────────────────────────────
# Tests: Filtering & Searching
# ──────────────────────────────────────────────

def test_get_tasks_by_status_pending(manager_with_tasks):
    pending = manager_with_tasks.get_tasks_by_status("pending")
    assert len(pending) == 3


def test_get_tasks_by_status_completed(manager_with_tasks):
    manager_with_tasks.complete_task(1)
    completed = manager_with_tasks.get_tasks_by_status("completed")
    assert len(completed) == 1


def test_search_tasks_by_title(manager_with_tasks):
    results = manager_with_tasks.search_tasks("report")
    assert len(results) == 1
    assert results[0].title == "Write report"


def test_search_tasks_by_description(manager_with_tasks):
    results = manager_with_tasks.search_tasks("Auth module")
    assert len(results) == 1


def test_search_tasks_no_results(manager_with_tasks):
    results = manager_with_tasks.search_tasks("nonexistent")
    assert results == []
