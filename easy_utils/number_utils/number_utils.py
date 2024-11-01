#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sy,Sang"
__version__ = ""
__license__ = "GPLv3"
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
Eps = numpy.finfo(float).eps


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

    def __repr__(self):
        return self.__str__()

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
    def frange(cls, *args) -> list:
        """
        生成保证浮点数位数的range list
        :param first:
        :param end:
        :param step:
        :param closed_interval:
        :param args:
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

    @classmethod
    def finterval(cls, *args) -> list:
        """
        生成均匀间隔序列
        :param args:
        :param first:
        :param end:
        :param num:
        :param closed_interval:
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
        return cls.frange(decimal_first, decimal_end, decimal_step, False) if closed_interval is False \
            else numpy.linspace(first, end, num).tolist()

    @classmethod
    def np_frange(cls, *args) -> numpy.array:
        return numpy.array(cls.frange(*args))

    @classmethod
    def np_finterval(cls, *args) -> numpy.array:
        return numpy.array(cls.finterval(*args))

    @classmethod
    def put_in_range(cls, domain_min, domain_max, *args):
        """将随机变量置于曲线可用范围内"""
        ylist = []
        for x in args:
            x = float(x)
            if domain_min and domain_max is None:
                # return x
                ylist.append(x)
            elif domain_min is None:
                ylist.append(min(domain_max, x))
            elif domain_max is None:
                ylist.append(max(domain_min, x))
            else:
                ylist.append(min(max(domain_min, x), domain_max))
        if len(args) == 1:
            return ylist[0]
        else:
            return ylist


if __name__ == "__main__":
    # print(EasyFloat.frange(11))
    # f = EasyFloat(0, fix_nan=False, fix_inf=numpy.nan)
    # # print(EasyFloat.frange(0.1, 0.5, 0.01, closed_interval=True))
    # # print(EasyFloat.finterval(0, 10, 2, closed_interval=True))
    # print(1 / f)
    print(len(EasyFloat.finterval(0.01, 0.99, 100, False)))
    # print(len(EasyFloat.frange(0.01, 1, 0.0099, False)))
    # print(EasyFloat.np_frange(0, -1, -0.1, True))
