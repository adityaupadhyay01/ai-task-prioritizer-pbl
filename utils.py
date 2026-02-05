from datetime import datetime

def importance_weight(level):
    level = level.lower()
    if level == "high":
        return 3
    elif level == "medium":
        return 2
    elif level == "low":
        return 1
    else:
        return 0


def urgency_score(deadline_str):
    today = datetime.today().date()
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
    days_left = (deadline - today).days

    if days_left <= 2:
        return 3
    elif days_left <= 5:
        return 2
    else:
        return 1


def priority_score(importance, urgency):
    return importance + urgency
