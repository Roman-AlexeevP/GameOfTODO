from typing import Dict

from .core_driver import DbDriver
from . import consts
from ..game_core.game_hero import GameHero

import logging

logger = logging.getLogger(__name__)


class GameHeroManager(DbDriver):

    def __init__(self, db_name: str, table_name: str = consts.GAMEHERO_TABLE_NAME):
        super().__init__(db_name)
        self.table_name = table_name

    def get_saved_hero_state(self) -> GameHero:
        fields_for_select = [
            "current_level",
            "current_experience",
            "name"
        ]
        query_string = f"""
        SELECT {", ".join(fields_for_select)}
        FROM {self.table_name};
        """
        logger.debug(query_string)
        result = self.query(query_string)
        mapped_values = dict(zip(fields_for_select, result.fetchone()))
        hero = GameHero(
            current_experience=mapped_values.get("current_experience", 0),
            current_level=mapped_values.get("current_level", 0),
            name=mapped_values.get("name", "")
        )
        return hero

    def save_hero_state(self, hero: GameHero):
        column_names_repr = "current_level=?, current_experience=? "
        params = (hero.current_level, hero.current_experience,)
        query_string = f"""
                UPDATE {self.table_name}
                SET {column_names_repr}
                WHERE name=?
                """
        logger.debug(query_string)
        result = self.query(query_string, params)
        return hero