"""Simple non-interactive demo to validate task manager behavior."""
from task_manager.task_utils import tasks, add_task, mark_task_as_complete, view_pending_tasks, calculate_progress


def run_demo():
    print("Running demo tests...")
    # Clear tasks
    tasks.clear()

    # Valid add
    ok, msg = add_task("Buy groceries", "Milk, eggs, bread", "2026-06-30")
    print("Add valid:", ok, msg)

    # Invalid due date
    ok, msg = add_task("Old task", "Should fail", "2020-01-01")
    print("Add invalid due date:", ok, msg)

    # Invalid title
    ok, msg = add_task("", "No title", "2026-06-30")
    print("Add invalid title:", ok, msg)

    # Add another valid
    ok, msg = add_task("Write report", "Weekly status report", "2026-06-10")
    print("Add valid 2:", ok, msg)

    print("Current tasks:")
    for i, t in enumerate(tasks, 1):
        print(i, t)

    # Mark first as complete
    ok, msg = mark_task_as_complete(1)
    print("Mark complete:", ok, msg)

    # View pending
    pending = view_pending_tasks()
    print("Pending tasks:", pending)

    # Progress
    print("Progress:", calculate_progress(), "%")


if __name__ == "__main__":
    run_demo()
