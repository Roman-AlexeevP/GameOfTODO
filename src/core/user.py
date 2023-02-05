from typing import Optional

from .general import Any
from db.task_manager import TaskManager
from game_core.game_hero import GameHero

from db.game_hero_manager import GameHeroManager
from tasks.task_matrix import TaskMatrix


class User(Any):

    def __init__(self):
        self.game_hero_manager: Optional[GameHeroManager] = None
        self.game_hero: Optional[GameHero] = None
        self.task_manager: Optional[TaskManager] = None
        self.task_matrix: Optional[TaskMatrix] = None

    def init_game_hero(self):
        self.game_hero_manager.load_test_data()
        self.game_hero = self.game_hero_manager.get_saved_hero_state()
        print(self.game_hero)

    def set_game_hero_manager(self, game_hero_manager: GameHeroManager):
        self.game_hero_manager = game_hero_manager

    def set_task_manager(self, task_manager: TaskManager):
        self.task_manager = task_manager

    def init_tasks(self):
        self.task_manager.load_test_data()
        all_tasks = self.task_manager.get_all()
        self.task_matrix = TaskMatrix()
        self.task_matrix.init_from_task_list(all_tasks)
        print(self.task_matrix.get_str_repr_of_count())
        print(self.task_matrix)

    def create_new_task(self):
        pass

    def complete_task(self):
        pass

    def add_worked_hours_to_task(self):
        pass