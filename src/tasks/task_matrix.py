from .task_list import TaskList
from src.core.general import Any


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
        self.all_tasks_matrix = (
            self.important_urgent_tasks,
            self.not_important_urgent_tasks,
            self.important_not_urgent_tasks,
            self.not_important_not_urgent_tasks,
        )

    def get_summary_tasks_count(self):
        return sum((len(task_list) for task_list in self.all_tasks_matrix))
