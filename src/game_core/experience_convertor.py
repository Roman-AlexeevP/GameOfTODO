from ..core.general import Any
from . import consts


class ExperienceConverter(Any):

    def __init__(self, time_multiplier: float = consts.DEFAULT_TIME_TO_EXP_MULTIPLIER):
        self.time_multiplier = time_multiplier

    def convert_worked_hours_to_experience(self, worked_hours: float):
        return self.time_multiplier * worked_hours
