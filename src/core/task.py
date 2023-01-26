from datetime import datetime
from enum import Enum

from .general import Any


class PriorityTypes(Enum):

    # Срочные и важные задачи
    IMPORTANT_URGENT = 1

    # Срочные и неважные задачи
    NOT_IMPORTANT_URGENT = 2

    # Несрочные и важные задачи
    IMPORTANT_NOT_URGENT = 3

    # Несрочные и неважные задачи
    NOT_IMPORTANT_NOT_URGENT = 4





class Task(Any):

    FULL_COMPLETE_INIT = 1
    FULL_COMPLETE_OK = 2
    FULL_COMPLETE_ERROR = 3

    def finish(self):
        self.is_complete = True

    def __init__(self,
                 hours_to_complete: float,
                 priority_type: PriorityTypes,
                 ended_at: datetime,
                 name: str = "-",
                 description: str = "-",
                 is_active: bool = False,
                 is_complete: bool = False,
                 created_at: datetime = datetime.now(),
                 worked_hours: float = 0,
                 ):
        super().__init__()
        self.name = name
        self.description = description
        self.hours_to_complete = hours_to_complete
        self.is_active = is_active
        self.is_complete = is_complete
        self.created_at = created_at
        self.ended_at = ended_at
        self.worked_hours = worked_hours
        self.priority_type = priority_type
        self.full_complete_status = self.FULL_COMPLETE_INIT
    # команды

    def deactivate(self):
        self.is_active = False

    def enable_focus(self):
        self.is_active = True

    def add_worked_time(self, worked_hours: float):
        self.worked_hours += worked_hours

    def complete(self):
        self.is_complete = True

    def full_complete(self):
        if self.can_complete():
            self.deactivate()
            self.complete()
            self.ended_at = datetime.now()
            self.full_complete_status = self.FULL_COMPLETE_OK
        else:
            self.full_complete_status = self.FULL_COMPLETE_ERROR


    # запросы
    def is_activated(self):
        return self.is_active

    def is_completed(self):
        return self.is_complete

    def get_current_hours_to_complete(self):
        return self.hours_to_complete - self.worked_hours

    def can_complete(self):
        return not(self.get_current_hours_to_complete() > 0)

    def get_full_complete_status(self):
        return self.full_complete_status

    def __str__(self):
        return f"{self.name} {self.hours_to_complete} ч."

