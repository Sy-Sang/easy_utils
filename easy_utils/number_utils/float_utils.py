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
from typing import Union, Self, Any, Type
from collections import namedtuple
import decimal
from datetime import datetime
import re

# 项目模块

# 外部模块
import numpy

# 代码块
Eps = float(numpy.finfo(float).eps)


def eps_rational_wrapper(f: callable):
    """
    将涉及除0的计算结果改变为easyfloat类
    """

    def wrapper(instance, *args, **kwargs):
        param_dic = {
            "nan_value": instance.nan_value,
            "r": instance.r
        }
        return type(instance)(f(instance, *args, **kwargs), **param_dic)

    return wrapper


class EpsRational(float):
    """
    使用float(numpy.finfo(float).eps)处理除零的有理数
    """

    def __new__(
            cls,
            x: Any,
            nan_value: Union[float, int, numpy.floating] = 0,
            *args, **kwargs):

        if x is None or numpy.isnan(x):
            y = nan_value
        elif isinstance(x, (float, int, decimal.Decimal)):
            y = float(x)
        elif isinstance(x, str):
            number_str = "".join([i for i in re.findall(r'\d+', x)])
            y = float(number_str) if number_str else nan_value
        elif isinstance(x, datetime):
            y = x.timestamp()
        else:
            y = nan_value

        return super(EpsRational, cls).__new__(cls, y)

    def __init__(self, x: Any, nan_value: Union[float, int, numpy.floating] = 0, r: int = 10):
        self.str = str(round(self, r))
        self.nan_value = nan_value
        self.r = r

    def __str__(self):
        return self.str

    def __repr__(self):
        return self.__str__()

    @eps_rational_wrapper
    def __truediv__(self, other):
        if other == 0:
            b = Eps
        else:
            b = float(other)
        return super().__truediv__(b)

    @eps_rational_wrapper
    def __rtruediv__(self, other):
        if self == 0:
            return float(other) / Eps
        else:
            return super().__rtruediv__(other)

    @eps_rational_wrapper
    def __divmod__(self, other):
        if other == 0:
            b = Eps
        else:
            b = float(other)
        return super().__divmod__(b)

    @eps_rational_wrapper
    def __rdivmod__(self, other):
        if self == 0:
            return float(other) % Eps
        else:
            return super().__rdivmod__(other)

    @eps_rational_wrapper
    def __floordiv__(self, other):
        if other == 0:
            b = Eps
        else:
            b = float(other)
        return super().__floordiv__(b)

    @eps_rational_wrapper
    def __rfloordiv__(self, other):
        if self == 0:
            return float(other) // Eps
        else:
            return super().__rfloordiv__(other)


if __name__ == "__main__":
    lr = EpsRational(numpy.nan, numpy.nan)
    print(lr / 0)

    z = EpsRational(numpy.inf)
    print(1 / z)
    print(z / 0)
