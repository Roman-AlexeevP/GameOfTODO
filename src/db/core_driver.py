import sqlite3
import logging

from core.general import Any

logger = logging.getLogger(__name__)


class DbDriver(Any):

    RETURN_ONE = 1
    RETURN_MANY = 2
    RETURN_ID = 3

    def __init__(self, db_name):
        self.db_name = db_name

    def _create_connection(self) -> sqlite3.Connection:
        connection = sqlite3.connect(
            database=self.db_name,
            detect_types=sqlite3.PARSE_DECLTYPES |
                         sqlite3.PARSE_COLNAMES
        )
        return connection

    def _create_cursor(self, connection: sqlite3.Connection) -> sqlite3.Cursor:
        return connection.cursor()

    def query(self, sql_query: str, return_result_type=None, *args, **kwargs):
        connection = self._create_connection()
        cursor = self._create_cursor(connection)
        try:
            result = cursor.execute(sql_query, *args, **kwargs)
        except sqlite3.Error as exception:
            logger.exception(exception)
        else:
            mapping_results = {
                self.RETURN_MANY: result.fetchall,
                self.RETURN_ONE: result.fetchone
            }
            return mapping_results.get(return_result_type, result.fetchone)()
        finally:
            connection.commit()
            connection.close()
