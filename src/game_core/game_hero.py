from ..core.general import Any
from .experience_convertor import ExperienceConverter
from ..tasks.task import Task


class GameHero(Any):
    LEVELUP_STABLE = 1
    LEVELUP_DONE = 2

    def __init__(self,
                 name: str,
                 current_experience: float = 1.0,
                 current_level: int = 0):
        self.name = name
        self.current_experience = current_experience
        self.current_level = current_level
        self.experience_to_next_level = self.experience_to_next_level(current_level)
        self.levelup_status = self.LEVELUP_STABLE

    def up_level(self):
        self.current_level += 1
        self.experience_to_next_level = self.exp_for_lvl_formula(self.current_level)

    def is_ready_for_levelup(self) -> bool:
        return self.current_experience >= self.experience_to_next_level

    def increase_current_exp(self, experience: float):
        self.current_experience += experience

    def increase_exp_from_worked_time(self, worked_time):
        experience_convertor = ExperienceConverter()
        exp = experience_convertor.convert_worked_hours_to_experience(worked_time)
        self.increase_current_exp(exp)

    def increase_exp(self, source, count):
        sources_mapping = {
            Task: self.increase_exp_from_worked_time,
        }
        increaser_func = sources_mapping.get(source, self.increase_current_exp)
        increaser_func(count)
        self.levelup_status = self.LEVELUP_STABLE
        if self.is_ready_for_levelup():
            self.up_level()
            self.levelup_status = self.LEVELUP_DONE

    def exp_for_lvl_formula(self, level):
        return (level * self.LEVEL_MULTIPLIER) + (level + 1)
