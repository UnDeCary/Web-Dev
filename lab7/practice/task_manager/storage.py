import json
import os.path

from models import Task


def load_tasks(filename: str) -> list:
    if not os.path.exists(filename):
        return []

    with open(filename, 'r') as f:
        tasks = json.load(f)
    return [Task.from_dict(item) for item in tasks]

def save_tasks(filename: str, tasks: list) -> None:
    data = [task.to_dict() for task in tasks]

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)