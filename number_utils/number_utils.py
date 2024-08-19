#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sy,Sang"
__version__ = ""

# 系统模块
import copy
import pickle
import json
import decimal
from typing import Union, Self, Any
import re
from datetime import datetime

# 项目模块

# 外部模块
import numpy


# 代码块

class EasyFloat(float):
    """
    常用数据清洗类
    """

    def __new__(cls, x: Any, e: float = 0, no_inf: Union[bool, float] = False):
        fx = e
        if isinstance(x, (float, int, decimal.Decimal)):
            if numpy.isnan(x):
                pass
            elif no_inf is not False and numpy.isinf(x):
                fx = no_inf
            else:
                fx = x
        elif isinstance(x, str):
            number_str = "".join([i for i in re.findall(r'\d+', x)])
            fx = float(number_str) if number_str else e
        elif isinstance(x, datetime):
            fx = x.timestamp()
        else:
            pass
        return super(EasyFloat, cls).__new__(cls, fx)

    def __init__(self, x: Any, e: float = 0, no_inf: Union[bool, float] = False, r: int = 10):
        self.str = str(round(self, r))
        self.e = e
        self.no_inf = no_inf

    def __str__(self):
        return self.str

    def __truediv__(self, other):
        if other == 0:
            return type(self)(self.e)
        else:
            return super().__truediv__(other)

    def __rtruediv__(self, other):
        if self == 0:
            if self.no_inf is True:
                return type(self)(self.e)
            else:
                return type(self)(numpy.inf)
        else:
            return super().__rtruediv__(other)

    def __divmod__(self, other):
        if other == 0:
            return type(self)(self.e)
        else:
            return super().__divmod__(other)

    def __rdivmod__(self, other):
        if self == 0:
            return type(self)(self.e)
        else:
            return super().__rdivmod__(other)

    def __floordiv__(self, other):
        if other == 0:
            return type(self)(self.e)
        else:
            return super().__floordiv__(other)

    def __rfloordiv__(self, other):
        if self == 0:
            return type(self)(self.e)
        else:
            return super().__rfloordiv__(other)

    @classmethod
    def frange(cls, *args, first: float = 0, end: float = 1, step: float = 0.1, closed_interval: bool = False) -> list:
        """
        生成保证浮点数位数的range list
        :param first:
        :param end:
        :param step:
        :param closed_interval:
        :param args:
        :return:
        """
        num_args = len(args)
        if num_args >= 1:
            end = args[0]
        if num_args >= 2:
            first = args[0]
            end = args[1]
        if num_args >= 3:
            step = args[2]
        if num_args >= 4:
            closed_interval = args[3]

        range_list = []
        decimal_first = decimal.Decimal(str(first))
        decimal_step = decimal.Decimal(str(step))
        decimal_end = decimal.Decimal(str(end))
        decimal_ranger = decimal_first
        while decimal_ranger <= decimal_end:
            range_list.append(float(decimal_ranger))
            decimal_ranger += decimal_step
        if not closed_interval and float(decimal_end) in range_list:
            range_list.remove(float(decimal_end))
        else:
            pass
        return range_list

    @classmethod
    def finterval(cls, *args, first: float = 0, end: float = 1, num: int = 10, closed_interval: bool = False) -> list:
        """
        生成均匀间隔序列
        :param args:
        :param first:
        :param end:
        :param num:
        :param closed_interval:
        :return:
        """
        num_args = len(args)
        if num_args >= 1:
            num = args[0]
        if num_args >= 2:
            end = args[0]
            num = args[1]
        if num_args >= 3:
            first = args[0]
            end = args[1]
            num = args[2]
        if num_args >= 4:
            closed_interval = args[3]

        step = (end - first) / num
        return cls.frange(first, end, step, closed_interval)


if __name__ == "__main__":
    f = EasyFloat(0)
    print(EasyFloat.frange(0.1, 0.5, 0.01, closed_interval=True))
    print(EasyFloat.finterval(0, 10, 2, closed_interval=True))
