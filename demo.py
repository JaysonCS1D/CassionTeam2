# demo.py — Capstone Demo Script
# Run with: python demo.py

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from task_manager import TaskManager

def separator(title):
    print(f"\n{'='*50}")
    print(f"  {title}")
    print('='*50)

def main():
    print("\n Python Task Manager App - Capstone Demo")
    print("   Version: v1.0  |  Author: Development Team")

    manager = TaskManager()

    separator("1. Creating Tasks")
    t1 = manager.add_task("Buy groceries", "Milk, eggs, bread", due_date="2026-05-10")
    t2 = manager.add_task("Write report", "Q1 summary for manager")
    t3 = manager.add_task("Fix login bug", "Auth module issue", due_date="2026-05-08")
    t4 = manager.add_task("Team standup", "Daily 9AM meeting")
    t5 = manager.add_task("Deploy app", "Push to Render.com", due_date="2026-05-09")
    print(f"  Created {manager.task_count()} tasks")

    separator("2. All Tasks")
    for t in manager.get_all_tasks():
        due = f" | due: {t.due_date}" if t.due_date else ""
        print(f"  [{t.task_id}] {t.title} - {t.status}{due}")

    separator("3. Completing Task #1")
    manager.complete_task(1)
    t = manager.get_task(1)
    print(f"  Task '{t.title}' marked as: {t.status}")

    separator("4. Filter: Pending Tasks")
    pending = manager.get_tasks_by_status("pending")
    for t in pending:
        print(f"  PENDING [{t.task_id}] {t.title}")

    separator("4b. Filter: Completed Tasks")
    completed = manager.get_tasks_by_status("completed")
    for t in completed:
        print(f"  DONE [{t.task_id}] {t.title}")

    separator("5. Search: 'bug'")
    results = manager.search_tasks("bug")
    for t in results:
        print(f"  Found: [{t.task_id}] {t.title}")

    separator("6. Input Validation Demo")
    try:
        manager.add_task("")
    except ValueError as e:
        print(f"  Empty title blocked: {e}")
    try:
        manager.add_task("Test task", due_date="not-a-date")
    except ValueError as e:
        print(f"  Bad date blocked: {e}")

    separator("7. Deleting Task #2")
    manager.delete_task(2)
    print(f"  Task #2 deleted. Remaining tasks: {manager.task_count()}")

    separator("8. Final Summary")
    print(f"  Total tasks:   {manager.task_count()}")
    print(f"  Pending:       {len(manager.get_tasks_by_status('pending'))}")
    print(f"  Completed:     {len(manager.get_tasks_by_status('completed'))}")
    print("\n  Demo complete - all features working!\n")

if __name__ == "__main__":
    main()
