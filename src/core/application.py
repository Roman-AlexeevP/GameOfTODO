
from pathlib import Path
from typing import List, Optional


from .general import Any
from db.init_manager import InitManager
from db import consts
from .user import User
from db.game_hero_manager import GameHeroManager
from db.task_manager import TaskManager


class Application(Any):
    DEFAULT_SQL_SCRIPTS_PATH = "src/db/sql_scripts"

    def __init__(self, path_to_sql_scripts: str = DEFAULT_SQL_SCRIPTS_PATH, db_name=consts.DB_NAME):
        self.path_to_sql_scripts = path_to_sql_scripts
        self.db_name = db_name
        self.user: Optional[User] = None

    def run(self):
        self.launch_db()
        self.init_user()

    def launch_db(self):
        sql_files = self.get_files_from_folder(self.path_to_sql_scripts)
        db_init_manager = InitManager(init_files=sql_files, db_name=self.db_name)
        db_init_manager.init_database()

    def init_user(self):
        self.user = User()
        game_hero_manager = GameHeroManager(db_name=self.db_name)
        tasks_manager = TaskManager(db_name=self.db_name)
        self.user.set_game_hero_manager(game_hero_manager)
        self.user.set_task_manager(tasks_manager)
        self.user.init_tasks()
        self.user.init_tasks()


    def get_files_from_folder(self, folder_name: str) -> List[Path]:
        folder_path = Path(folder_name)
        files = [file for file in folder_path.iterdir()]
        return files
