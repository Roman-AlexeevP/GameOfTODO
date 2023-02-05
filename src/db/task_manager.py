from typing import Dict

from .core_driver import DbDriver
from . import consts
from tasks.task import Task
from tasks.task_list import TaskList

import logging

logger = logging.getLogger(__name__)


class TaskManager(DbDriver):

    def __init__(self, db_name: str, table_name: str = consts.TASKS_TABLE_NAME):
        super().__init__(db_name)
        self.table_name = table_name

    def get_all(self) -> TaskList:
        task_fields_for_select = [
            "uid",
            "name",
            "description",
            "hours_to_complete",
            "is_active",
            "is_complete",
            "created_at",
            "ended_at",
            "worked_hours",
            "priority_type",
        ]
        query_string = f"""
        SELECT {",".join(task_fields_for_select)}
        FROM {self.table_name};
        """
        logger.debug(query_string)
        result = self.query(query_string, return_result_type=self.RETURN_MANY)

        task_list = TaskList()
        for raw_task in result:
            mapped_values_from_query = dict(zip(task_fields_for_select, raw_task))
            task = Task(**mapped_values_from_query)
            task_list.insert(task)
        return task_list

    def get_by_uid(self, uid: int) -> Task:
        task_fields_for_select = [
            "uid",
            "name",
            "description",
            "hours_to_complete",
            "is_active",
            "is_complete",
            "created_at",
            "ended_at",
            "worked_hours",
            "priority_type",
        ]
        query_string = f"""
                SELECT {",".join(task_fields_for_select)}
                FROM {self.table_name}
                WHERE uid=?;
                """
        logger.debug(query_string)
        params = (uid,)
        result = self.query(query_string, params, return_result_type=self.RETURN_ONE)
        mapped_values_from_query = dict(zip(task_fields_for_select, result))
        task = Task(**mapped_values_from_query)
        return task

    def delete_by_uid(self, uid: int) -> bool:
        query_string = f"""
        DELETE FROM {self.table_name}
        WHERE uid = ?
        """
        logger.debug(query_string)
        params = (uid,)
        result = self.query(query_string, params)
        return True

    def update_by_id(self, uid: int, fields_to_update: Dict) -> Task:
        column_names_repr = f"=?, ".join(fields_to_update.keys())
        params = tuple([*fields_to_update.values(), uid])
        query_string = f"""
        UPDATE {self.table_name}
        SET {column_names_repr}
        WHERE uid=?
        """
        logger.debug(query_string)
        result = self.query(query_string, params)
        return self.get_by_uid(result.lastrowid)


    def create_one(self, task: Task) -> Task:
        task_fields_for_create = [
            "name",
            "description",
            "hours_to_complete",
            "is_active",
            "is_complete",
            "created_at",
            "ended_at",
            "worked_hours",
            "priority_type",
        ]
        column_names = ",".join(task_fields_for_create)
        column_placeholders = ",".join(['?' for _ in task_fields_for_create])
        query_string = f"""
        INSERT INTO {self.table_name} ({column_names}) 
        VALUES ({column_placeholders});
        """
        logger.debug(query_string)
        data = (
            task.name,
            task.description,
            task.hours_to_complete,
            task.is_active,
            task.is_complete,
            task.created_at,
            task.ended_at,
            task.worked_hours,
            task.priority_type,
        )
        result = self.query(query_string, data)
        task.uid = result.lastrowid
        return task

    def create_multiple(self, tasks_list: TaskList) -> TaskList:
        pass
