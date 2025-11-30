from datetime import date, datetime

def calculate_task_score(task):
    score = 0
    today = date.today()

    importance = int(task.get("importance", 5))
    hours = int(task.get("estimated_hours", 1))
    dependencies = task.get("dependencies", [])

    # Urgency
    due_raw = task.get("due_date")
    if due_raw:
        if isinstance(due_raw, str):
            due = datetime.strptime(due_raw, "%Y-%m-%d").date()
        else:
            due = due_raw

        days_left = (due - today).days

        if days_left < 0:
            score += 100
        elif days_left <= 3:
            score += 60
        elif days_left <= 7:
            score += 40
        else:
            score += 20
    else:
        score += 10

    # Importance
    score += importance * 5

    # Effort bonus
    if hours <= 2:
        score += 15
    elif hours <= 5:
        score += 5

    # Dependency penalty
    score -= len(dependencies) * 10

    return score
