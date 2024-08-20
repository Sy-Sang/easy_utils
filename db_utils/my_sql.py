#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sy,Sang"
__version__ = ""
__license__ = "GUN"
__maintainer__ = "Sy, Sang"
__email__ = "martin9le@163.com"
__status__ = "Development"
__credits__ = []
__date__ = "2024-8-20"
__copyright__ = ""

# 系统模块
import copy
import pickle
import json
from typing import Union, Self
from abc import ABC, abstractmethod

# 项目模块

# 外部模块
import numpy
import pymysql


# 代码块

class Link(ABC):
    def __init__(self, url: str, port: int, user: str, pwd: str, db: str, max_try=50, *args, **kwargs):
        self.url = url
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db
        self.max_try = max_try

    @abstractmethod
    def new_conn(self, *args, **kwargs):
        pass

    @abstractmethod
    def close_cursor(self, *args, **kwargs):
        pass

    @abstractmethod
    def close_conn(self, *args, **kwargs):
        pass


def try_wrapper(f: callable):
    """

    :param f:
    :param args:
    :param kwargs:
    :return:
    """

    def wrapper(instance: Link, *args, **kwargs):
        counter = 0
        error = []
        while counter < instance.max_try:
            try:
                res = f(instance, *args, **kwargs)
            except Exception as e:
                counter += 1
                error.append([counter, str(e)])
            else:
                return res
        raise Exception(str(error))

    return wrapper


def query_wrapper(f: callable):
    """

    :param f:
    :param args:
    :param kwargs:
    :return:
    """

    def wrapper(instance: Link, *args, **kwargs):
        succeeded = False
        try:
            instance.new_conn(*args, **kwargs)
            res = f(instance, *args, **kwargs)
            succeeded = True
        except Exception as e:
            print(str(e))
            res = ()
        instance.close_cursor()
        instance.close_conn()
        return res, succeeded

    return wrapper


class MySQLLink(Link):
    """
    MYSQL Link
    """

    def __init__(self, url: str, port: int, user: str, pwd: str, db: str, max_try=50):
        """

        :param url:
        :param port:
        :param user:
        :param pwd:
        :param db:
        :param max_try:
        """
        super().__init__(url, port, user, pwd, db, max_try)

        self.conn = None
        self.cursor = None

    @try_wrapper
    def new_conn(self, *args, **kwargs):
        """
        新建连接
        :return:
        """
        self.close_conn()
        self.close_cursor()
        self.conn = pymysql.connect(
            host=self.url,
            port=self.port,
            user=self.user,
            passwd=self.pwd,
            db=self.db,
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def close_conn(self, *args, **kwargs):
        """
        关闭连接
        :param e:
        :return:
        """
        if isinstance(self.conn, pymysql.connections.Connection):
            self.conn.close()
            self.conn = None
            return 1
        else:
            return 0

    def close_cursor(self, *args, **kwargs):
        """

        :return:
        """
        if isinstance(self.cursor, pymysql.cursors.Cursor):
            self.cursor.close()
            self.cursor = None
            return 1
        else:
            return 0

    @query_wrapper
    def select(self, sql: str, *args, **kwargs):
        """
        查询
        """
        self.cursor.execute(sql)
        query_result = self.cursor.fetchall()
        return query_result

    @query_wrapper
    def insert(self, sql: str, *args, **kwargs):
        """
        简单插入数据
        """
        executer = self.cursor.execute(sql)
        self.conn.commit()
        return executer

    @query_wrapper
    def insert_many(self, sql: str, data: Union[list, tuple]):
        """
        批量插入数据
        """
        executer = self.cursor.executemany(sql, data)
        self.conn.commit()
        return executer

    def long_to_wide(
            self,
            table: str,
            case_column: str,
            value_column: str,
            seq_column: str,
            where: str = "",
            case_key: list[str] = None,
            if_null: Union[float, str] = None
    ) -> tuple:
        where_piece = "" if where == "" else f"WHERE {where}"
        where_sql = f"SELECT DISTINCT {case_column} FROM {table} {where_piece} ORDER BY {case_column}"
        print(where_sql)
        if case_key is None:
            key_query = self.select(
                where_sql
            )
            case_key_list = [i[0] for i in key_query]
        else:
            case_key_list = copy.deepcopy(case_key)

        case_sql = ""
        for i, k in enumerate(case_key_list):
            if if_null is None:
                case_sql += f"MAX(CASE WHEN {case_column} = '{k}' THEN {value_column} END) AS '{k}'"
            else:
                case_sql += f"COALESCE(MAX(CASE WHEN {case_column} = '{k}' THEN {value_column} END), {if_null}) AS '{k}'"
            if i != len(case_key_list) - 1:
                case_sql += ","
            else:
                pass

        sql = (f"SELECT {seq_column}, {case_sql} "
               f"FROM {table} "
               f"{where_piece} "
               f"GROUP BY {seq_column} ORDER BY {seq_column}")

        return self.select(sql), case_key_list, sql


if __name__ == "__main__":
    test_link = MySQLLink(
        "bj-cynosdbmysql-grp-94j6daxc.sql.tencentcdb.com",
        22681,
        "sangsiyuan",
        "!Sakula131313",
        "test_db",
        50
    )
    print(test_link.insert("insert into test (id, name, value) values (3,'b',10)"))
