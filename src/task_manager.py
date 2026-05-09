# src/task_manager.py

import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Task:
    def __init__(self, task_id, title, description="", due_date=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "pending"
        self.created_at = datetime.now().isoformat()
        self.completed_at = None

    def complete(self):
        self.status = "completed"
        self.completed_at = datetime.now().isoformat()

    def is_overdue(self):
        if self.due_date and self.status == "pending":
            return datetime.now() > datetime.fromisoformat(self.due_date)
        return False

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
            "created_at": self.created_at,
            "completed_at": self.completed_at,
        }

    def __repr__(self):
        return f"Task(id={self.task_id}, title='{self.title}', status='{self.status}')"


class TaskManager:
    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add_task(self, title, description="", due_date=None):
        # Input validation 1: title must not be empty
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")
        # Input validation 2: due_date must be valid ISO format if provided
        if due_date:
            try:
                datetime.fromisoformat(due_date)
            except ValueError:
                raise ValueError("due_date must be a valid ISO format date string (YYYY-MM-DD).")
        task = Task(self._next_id, title.strip(), description, due_date)
        self._tasks[self._next_id] = task
        self._next_id += 1
        logger.info(f"Task created: ID={task.task_id}, title='{task.title}'")
        return task

    def get_task(self, task_id):
        return self._tasks.get(task_id)

    def get_all_tasks(self):
        return list(self._tasks.values())

    def get_tasks_by_status(self, status):
        return [t for t in self._tasks.values() if t.status == status]

    def complete_task(self, task_id):
        task = self._tasks.get(task_id)
        if not task:
            raise KeyError(f"Task with ID {task_id} not found.")
        task.complete()
        logger.info(f"Task completed: ID={task_id}")
        return task

    def delete_task(self, task_id):
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} not found.")
        logger.info(f"Task deleted: ID={task_id}")
        return self._tasks.pop(task_id)

    def search_tasks(self, keyword):
        keyword = keyword.lower()
        return [
            t for t in self._tasks.values()
            if keyword in t.title.lower() or keyword in t.description.lower()
        ]

    def task_count(self):
        return len(self._tasks)
