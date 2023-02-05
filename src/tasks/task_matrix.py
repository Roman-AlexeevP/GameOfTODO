from .task import PriorityTypes
from .task_list import TaskList
from core.general import Any


class TaskMatrix(Any):

    def __init__(self,
                 important_urgent_tasks: TaskList = None,
                 not_important_urgent_tasks: TaskList = None,
                 important_not_urgent_tasks: TaskList = None,
                 not_important_not_urgent_tasks: TaskList = None):
        self.important_urgent_tasks = important_urgent_tasks
        self.not_important_urgent_tasks = not_important_urgent_tasks
        self.important_not_urgent_tasks = important_not_urgent_tasks
        self.not_important_not_urgent_tasks = not_important_not_urgent_tasks

    def init_from_task_list(self, task_list: TaskList):
        self.important_urgent_tasks = task_list.get_tasks_by_type(PriorityTypes.IMPORTANT_URGENT.value)
        self.not_important_urgent_tasks = task_list.get_tasks_by_type(PriorityTypes.NOT_IMPORTANT_URGENT.value)
        self.important_not_urgent_tasks = task_list.get_tasks_by_type(PriorityTypes.IMPORTANT_NOT_URGENT.value)
        self.not_important_not_urgent_tasks = task_list.get_tasks_by_type(PriorityTypes.NOT_IMPORTANT_NOT_URGENT.value)

    def get_str_repr_of_count(self) -> str:
        return f"Текущее кол-во задач: {self.get_summary_tasks_count()}"

    def get_summary_tasks_count(self):
        return sum([
            len(self.important_urgent_tasks),
            len(self.important_not_urgent_tasks),
            len(self.not_important_urgent_tasks),
            len(self.not_important_not_urgent_tasks)
        ])

    def __str__(self):
        return f"Важные и срочные\n{self.important_urgent_tasks}\n" \
               f"Важные и несрочные\n{self.important_not_urgent_tasks}\n" \
               f"Неважные и срочные\n{self.not_important_urgent_tasks}\n" \
               f"Неважные и несрочные\n{self.not_important_not_urgent_tasks}"