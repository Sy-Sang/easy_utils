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

# 项目模块

# 外部模块
import numpy


# 代码块

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


def dict_flatten(dic: dict, fill_type=None):
    """
    压平字典中的值
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
