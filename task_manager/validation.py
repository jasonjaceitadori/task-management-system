from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str):
        return False, "Title must be a string."
    title = title.strip()
    if not title:
        return False, "Title cannot be empty."
    if len(title) > 100:
        return False, "Title must be 100 characters or fewer."
    return True, ""


def validate_task_description(description):
    if description is None:
        return True, ""
    if not isinstance(description, str):
        return False, "Description must be a string."
    if len(description) > 500:
        return False, "Description must be 500 characters or fewer."
    return True, ""


def validate_due_date(due_date):
    if not isinstance(due_date, str):
        return False, "Due date must be a string in YYYY-MM-DD format."
    try:
        dt = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        return False, "Due date must be in YYYY-MM-DD format."
    return True, ""
