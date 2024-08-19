#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sy,Sang"
__version__ = ""

# 系统模块
import copy
import pickle
import json
from typing import Union, Self

# 项目模块

# 外部模块
import numpy
from scipy.interpolate import CubicSpline


# 代码块

def n_integrate_dim_wrapper(fun):
    """
    保证数据为二维的装饰器
    :param fun:
    :return:
    """

    def wrapper(*args, **kwargs):
        """wrapper"""
        xarray = numpy.array(args[0])
        if xarray.ndim == 1:
            axis_array = numpy.arange(len(xarray))
            xarray = numpy.column_stack((axis_array, xarray))
        elif xarray.ndim > 2:
            xarray = xarray[:, 0:2]
        else:
            pass
        return fun(xarray, *args, **kwargs)

    return wrapper


@n_integrate_dim_wrapper
def n_integrate(xlist, *args, **kwargs) -> float:
    """梯形积分"""
    h0 = xlist[:-1, 1]
    h1 = xlist[1:, 1]
    l = xlist[1:, 0] - xlist[:-1, 0]
    r = numpy.sum((h0 + h1) * l * 0.5)
    return float(r)


def n_integrate2(xlist, interpolate: int = 10, *args, **kwargs) -> float:
    """
    带三次样条差值的数值积分
    """
    array = numpy.array(xlist)
    cs = CubicSpline(array[:, 0], array[:, 1])
    x_new = numpy.linspace(array[:, 0][0], array[:, 0][-1], len(xlist) * interpolate)
    y_new = cs(x_new)
    return n_integrate(numpy.column_stack((x_new, y_new)))


def integrate(f: callable, first: float, end: float, num, *args, **kwargs) -> float:
    """梯形积分"""
    x = numpy.linspace(first, end, num)
    y = numpy.array([f(i) for i in x])
    return n_integrate(numpy.column_stack((x, y)))


def integrate2(f: callable, first: float, end: float, num, interpolate: int = 10, *args, **kwargs) -> float:
    """
    使用三次样条差值的梯形积分
    """
    x = numpy.linspace(first, end, num)
    y = numpy.array([f(i) for i in x])
    return n_integrate2(numpy.column_stack((x, y)), interpolate)


def simpsons_integrate(f: callable, first: float, end: float, num, *args, **kwargs) -> float:
    """
    辛普森法则积分
    :param f:
    :param first:
    :param end:
    :param num:
    :param args:
    :param kwargs:
    :return:
    """
    num = num if num % 2 == 0 else num + 1
    h = (end - first) / num
    x = numpy.linspace(first, end, num + 1)
    fx = numpy.array([f(i) for i in x])
    integral = h / 3 * (fx[0] + 2 * sum(fx[2:num:2]) + 4 * sum(fx[1:num:2]) + fx[num])
    return integral


if __name__ == "__main__":
    x = numpy.arange(0, 10, 0.01)
    y = numpy.sin(x)
    data = numpy.column_stack((x, y))
    print(n_integrate(data))
    print(n_integrate2(data))
    print(simpsons_integrate(numpy.sin, 0, 10, 100))
