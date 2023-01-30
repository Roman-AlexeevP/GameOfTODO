import sys

from pathlib import Path
from typing import List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

from .general import Any
from src.db.init_manager import InitManager
from src.db import consts


class Application(Any):
    DEFAULT_SQL_SCRIPTS_PATH = "src/db/sql_scripts"

    def __init__(self, path_to_sql_scripts: str = DEFAULT_SQL_SCRIPTS_PATH, db_name=consts.DB_NAME):
        self.path_to_sql_scripts = path_to_sql_scripts
        self.db_name = db_name

    def run(self):
        self.launch_db()
        self.launch_gui()

    def launch_db(self):
        sql_files = self.get_files_from_folder(self.path_to_sql_scripts)
        db_init_manager = InitManager(init_files=sql_files, db_name=self.db_name)
        db_init_manager.init_database()

    def launch_gui(self):
        app = QApplication(sys.argv)
        label = QLabel("Менеджер задач", alignment=Qt.AlignCenter)
        label.show()
        sys.exit(app.exec_())

    def get_files_from_folder(self, folder_name: str) -> List[Path]:
        folder_path = Path(folder_name)
        files = [file for file in folder_path.iterdir()]
        return files
