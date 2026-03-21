from typing import List


class Task:
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed

    def mark_completed(self) -> None:
        self.completed = True

    def __str__(self) -> str:
        return f'[{self.id}] {self.title} {"✅" if self.completed else "❌"}'

    def to_dict(self) -> dict:
        return {'id': self.id, 'title': self.title, 'completed': self.completed}

    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        return cls(data['id'], data['title'], data['completed'])


class TaskManager:
    def __init__(self, tasks: List[Task] = None):
        self.tasks = tasks

    def _gen_next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def add_task(self, title: str) -> None:
        self.tasks.append(Task(id=self._gen_next_id(), title=title))

    def list_tasks(self) -> List[Task]:
        return self.tasks

    def complete_task(self, id: int) -> bool:
        for task in self.tasks:
            if task.id == id:
                task.mark_completed()
                return True
        return False

    def delete_task(self, id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == id:
                del self.tasks[i]
                return True
        return False

