from pathlib import Path
from typing import List

from .core_driver import DbDriver

import logging

logger = logging.getLogger(__name__)


class InitManager(DbDriver):
    OPEN_SCRIPT_OK = 1
    OPEN_SCRIPT_ERROR = 2
    OPEN_SCRIPT_INIT = 3

    def __init__(self, init_files: List[Path], db_name):
        super().__init__(db_name)
        self.init_scripts = init_files
        self.open_script_status = self.OPEN_SCRIPT_INIT

    def get_script_from_file(self, filename: Path) -> str:
        if not filename.exists():
            logger.error(f"{filename.name} not exists!")
            self.open_script_status = self.OPEN_SCRIPT_ERROR
            return
        with filename.open(mode="r") as sql_script:
            query = sql_script.read()
        self.open_script_status = self.OPEN_SCRIPT_OK
        return query

    def init_database(self):
        logger.info("Starting DB initialization")
        failed_scripts = []
        for file in self.init_scripts:
            query = self.get_script_from_file(file)
            if self.open_script_status == self.OPEN_SCRIPT_ERROR:
                failed_scripts.append(file.name)
                continue
            self.query(query)
            logger.info(f"{file.name} successfully initiate")
        if failed_scripts:
            self.describe_failed_files(failed_scripts)

    def describe_failed_files(self, failed_filenames: List[str]):
        logger.error(
            f"Failed files count: {failed_filenames.count()}\n" + \
            "\n".join(failed_filenames)
        )
