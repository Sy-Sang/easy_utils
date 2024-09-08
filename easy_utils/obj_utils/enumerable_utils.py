#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sy,Sang"
__version__ = ""
__license__ = "GUN"
__maintainer__ = "Sy, Sang"
__email__ = "martin9le@163.com"
__status__ = "Development"
__credits__ = []
__date__ = ""
__copyright__ = ""

# 系统模块
import copy
import pickle
import json
from typing import Union, Self, Type
from collections import namedtuple
import decimal

# 项目模块

# 外部模块
import numpy


# 代码块

def frange(*args) -> list:
    """
    生成保证浮点数位数的range list
    :param args: <first, end, step, closed_interval=False>
    :return:
    """
    first = 0
    end = 1
    step = 0.1
    closed_interval = False
    l = len(args)

    if l <= 0:
        first = 0
        end = 1
        step = 0.1
        closed_interval = False
    elif l == 1:
        first = 0
        end = args[0]
        step = 1
        closed_interval = False
    elif l == 2:
        first = args[0]
        end = args[1]
        step = 1
        closed_interval = False
    elif l == 3:
        first = args[0]
        end = args[1]
        step = args[2]
        closed_interval = False
    elif l >= 4:
        first = args[0]
        end = args[1]
        step = args[2]
        closed_interval = args[3]

    range_list = []
    decimal_first = decimal.Decimal(str(first))
    decimal_step = decimal.Decimal(str(step))
    decimal_end = decimal.Decimal(str(end))
    decimal_ranger = decimal_first

    if end >= first:
        while True:
            if decimal_ranger < decimal_end:
                range_list.append(float(decimal_ranger))
            elif decimal_ranger == decimal_end and closed_interval is True:
                range_list.append(float(decimal_ranger))
            else:
                break
            decimal_ranger += decimal_step
    else:
        while True:
            if decimal_ranger > decimal_end:
                range_list.append(float(decimal_ranger))
            elif decimal_ranger == decimal_end and closed_interval is True:
                range_list.append(float(decimal_ranger))
            else:
                break
            decimal_ranger += decimal_step
    return range_list


def finterval(*args) -> list:
    """
    生成均匀间隔序列
    :param args: <first, end, step, closed_interval=False>
    :return:
    """
    l = len(args)
    first = 0
    end = 1
    num = 10
    closed_interval = False

    if l <= 0:
        first = 0
        end = 1
        num = 10
        closed_interval = False
    elif l == 1:
        first = 0
        end = args[0]
        num = 10
        closed_interval = False
    elif l == 2:
        first = args[0]
        end = args[1]
        num = 10
        closed_interval = False
    elif l == 3:
        first = args[0]
        end = args[1]
        num = args[2]
        closed_interval = False
    elif l >= 4:
        first = args[0]
        end = args[1]
        num = args[2]
        closed_interval = args[3]

    decimal_first = decimal.Decimal(str(first))
    decimal_num = decimal.Decimal(str(num))
    decimal_end = decimal.Decimal(str(end))

    decimal_step = (decimal_end - decimal_first) / decimal_num
    return frange(decimal_first, decimal_end, decimal_step, False) if closed_interval is False \
        else numpy.linspace(first, end, num).tolist()


def np_frange(*args) -> numpy.array:
    """
    numpy.ndarray格式的range列表
    """
    return numpy.array(frange(*args))


def np_finterval(*args) -> numpy.array:
    """
    numpy.ndarray格式的interval列表
    """
    return numpy.array(finterval(*args))


def flatten(seq: Union[list, tuple, numpy.ndarray]) -> list:
    """
    彻底压平
    """
    while True:
        nested = []
        flatten_list = []
        for i, item in enumerate(seq):
            if isinstance(item, (list, tuple, range, numpy.ndarray)):
                for subitem in item:
                    flatten_list.append(subitem)
                nested.append(True)
            elif isinstance(item, dict):
                for subitem in item.values():
                    flatten_list.append(subitem)
                nested.append(True)
            else:
                flatten_list.append(item)
        if not nested:
            return flatten_list
        else:
            seq = flatten_list


def dict_flatten(dic: dict, fill_type=None) -> list:
    """
    压平字典
    """
    if fill_type is None:
        fill_type = (dict, list, tuple)

    d = copy.deepcopy(dic).values()

    count = []
    while True:
        nested = []
        tree = []
        temp_count = []
        counter = 0
        for v in d:
            if isinstance(v, dict):
                temp_count.append([])
                for vv in v.values():
                    tree.append(vv)
                    temp_count[-1].append(counter)
                    counter += 1
                nested.append(True)
            elif isinstance(v, fill_type):
                temp_count.append([])
                for vv in v:
                    tree.append(vv)
                    temp_count[-1].append(counter)
                    counter += 1
                nested.append(True)
            else:
                tree.append(v)
                temp_count.append(counter)
                counter += 1
        count.append(temp_count)
        if not nested:
            return tree
        else:
            d = tree


if __name__ == "__main__":
    d = {
        "a": 10,
        "b": {"2": [2, 3, 4]},
        "d": [5, [6, {"e": [7, 8]}, 9]],
        "f": 10
    }
    print(dict_flatten(d))
    # v = [i * 10 for i in dict_flatten(d)]
    # print(v)

    # print(dict_displace(d, v))

    # l = [
    #     [1, 2, 3],
    #     [[4, 5], 6, {"a": 61, "b": [62, 63]}],
    #     7,
    #     (8, [9], 10),
    #     range(100, 110)
    # ]
    # print(flatten([[l]]))
    # print(flatten([1]))
