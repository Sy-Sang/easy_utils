#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sy,Sang"
__version__ = ""
__license__ = ""
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
import decimal
from typing import Union, Self, Any
import re
from datetime import datetime

# 项目模块

# 外部模块
import numpy


# 代码块
def infectious_wrapper(f: callable):
    """
    将涉及除0的计算结果改变为easyfloat类
    """

    def wrapper(instance, *args, **kwargs):
        param_dic = {
            "error_value": instance.error_value,
            "fix_nan": instance.fix_nan,
            "fix_inf": instance.fix_inf,
            "r": instance.r
        }
        return type(instance)(f(instance, *args, **kwargs), **param_dic)

    return wrapper


class EasyFloat(float):
    """
    常用数据清洗类
    """

    def __new__(cls, x: Any, error_value: float = 0, fix_nan: Union[bool, float] = False,
                fix_inf: Union[bool, float] = False, *args, **kwargs):
        if isinstance(x, (float, int, decimal.Decimal)):
            if fix_nan is not False and numpy.isnan(x):
                fx = fix_nan
            elif fix_inf is not False and numpy.isinf(x):
                fx = fix_inf
            else:
                fx = x
        elif isinstance(x, str):
            number_str = "".join([i for i in re.findall(r'\d+', x)])
            fx = float(number_str) if number_str else error_value
        elif isinstance(x, datetime):
            fx = x.timestamp()
        else:
            fx = error_value
        return super(EasyFloat, cls).__new__(cls, fx)

    def __init__(self, x: Any, error_value: float = 0, fix_nan: Union[bool, float] = False,
                 fix_inf: Union[bool, float] = False, r: int = 10):
        self.str = str(round(self, r))
        self.error_value = error_value
        self.fix_nan = fix_nan
        self.fix_inf = fix_inf
        self.r = r

    def __str__(self):
        return self.str

    @infectious_wrapper
    def __truediv__(self, other):
        if other == 0:
            if self.fix_nan is not False:
                return self.fix_nan
            else:
                return numpy.nan
        else:
            return super().__truediv__(other)

    @infectious_wrapper
    def __rtruediv__(self, other):
        if self == 0:
            if self.fix_inf is not False:
                return self.fix_inf
            else:
                return numpy.inf
        else:
            return super().__rtruediv__(other)

    @infectious_wrapper
    def __divmod__(self, other):
        if other == 0:
            if self.fix_nan is not False:
                return self.fix_nan
            else:
                return numpy.nan
        else:
            return super().__divmod__(other)

    @infectious_wrapper
    def __rdivmod__(self, other):
        if self == 0:
            if self.fix_inf is not False:
                return self.fix_inf
            else:
                return numpy.inf
        else:
            return super().__rdivmod__(other)

    @infectious_wrapper
    def __floordiv__(self, other):
        if other == 0:
            if self.fix_nan is not False:
                return self.fix_nan
            else:
                return numpy.nan
        else:
            return super().__floordiv__(other)

    @infectious_wrapper
    def __rfloordiv__(self, other):
        if self == 0:
            if self.fix_inf is not False:
                return self.fix_inf
            else:
                return numpy.inf
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
    f = EasyFloat(0, fix_nan=False, fix_inf=numpy.nan)
    # print(EasyFloat.frange(0.1, 0.5, 0.01, closed_interval=True))
    # print(EasyFloat.finterval(0, 10, 2, closed_interval=True))
    print(1 / f)
