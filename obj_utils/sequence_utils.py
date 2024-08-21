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
from typing import Union, Self
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
            else:
                flatten_list.append(item)
        if not nested:
            return flatten_list
        else:
            seq = flatten_list


if __name__ == "__main__":
    l = [
        [1, 2, 3],
        [[4, 5], 6],
        7,
        (8, [9], 10),
        range(100, 110)
    ]
    print(flatten([[l]]))
    print(flatten([1]))
