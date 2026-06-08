from datetime import datetime
from .validation import validate_task_title, validate_task_description, validate_due_date

# Store tasks as a list of dictionaries
tasks = []


def add_task(title, description, due_date):
    valid, msg = validate_task_title(title)
    if not valid:
        return False, msg
    valid, msg = validate_task_description(description)
    if not valid:
        return False, msg
    valid, msg = validate_due_date(due_date)
    if not valid:
        return False, msg

    task = {
        "title": title.strip(),
        "description": (description or "").strip(),
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.now().isoformat(),
    }
    tasks.append(task)
    return True, "Task added successfully."


def mark_task_as_complete(index, tasks_list=None):
    if tasks_list is None:
        tasks_list = tasks
    if not isinstance(index, int):
        return False, "Index must be an integer."
    if index < 1 or index > len(tasks_list):
        return False, "Index out of range."
    tasks_list[index - 1]["completed"] = True
    return True, "Task marked as complete."


def view_pending_tasks(tasks_list=None):
    if tasks_list is None:
        tasks_list = tasks
    pending = [t for t in tasks_list if not t.get("completed")]
    return pending


def calculate_progress(tasks_list=None):
    if tasks_list is None:
        tasks_list = tasks
    total = len(tasks_list)
    if total == 0:
        return 0.0
    completed = sum(1 for t in tasks_list if t.get("completed"))
    progress = (completed / total) * 100.0
    return round(progress, 2)
