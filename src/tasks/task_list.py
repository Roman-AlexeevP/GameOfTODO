from typing import Iterable, List

from .task import Task, PriorityTypes
from core.general import Any


class TaskList(Any):

    def __init__(self, tasks_iterable: Iterable[Task] = None):

        self.tasks: List[Task] = list(tasks_iterable) if tasks_iterable is not None else []

    def insert(self, task: Task):
        self.tasks.append(task)

    def get_sorted_by_time(self) -> List[Task]:
        return self.tasks.copy().sort(key=lambda x: x.hours_to_compete)

    def get_sorted_by_creation_time(self) -> List[Task]:
        return self.tasks.copy().sort(key=lambda x: x.created_at)

    def get_longest_task(self) -> Task:
        return self.get_sorted_by_time().pop()

    def get_shortest_task(self) -> Task:
        return self.get_sorted_by_time().pop(0)

    def get_first_created_task(self) -> Task:
        return self.get_sorted_by_creation_time().pop()

    def get_last_created_task(self) -> Task:
        return self.get_sorted_by_creation_time().pop(0)

    def get_tasks_by_type(self, task_type: PriorityTypes):
        new_task_list = TaskList()
        for task in self.tasks:
            if task.priority_type == task_type:
                new_task_list.insert(task)
        return new_task_list