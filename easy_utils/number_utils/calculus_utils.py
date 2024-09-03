#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sy,Sang"
__license__ = "GPLv3"
__version__ = ""

# 系统模块
import copy
import decimal
import pickle
import json
from typing import Union, Self

# 项目模块
from easy_datetime.timestamp import timer

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
    y = numpy.array([f(i, *args, **kwargs) for i in x])
    return n_integrate(numpy.column_stack((x, y)))


def integrate2(f: callable, first: float, end: float, num, interpolate: int = 10, *args, **kwargs) -> float:
    """
    使用三次样条差值的梯形积分
    """
    x = numpy.linspace(first, end, num)
    y = numpy.array([f(i, *args, **kwargs) for i in x])
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
    fx = numpy.array([f(i, *args, **kwargs) for i in x])
    integral = h / 3 * (fx[0] + 2 * sum(fx[2:num:2]) + 4 * sum(fx[1:num:2]) + fx[num])
    return integral


def romberg_integration(f: callable, a, b, tol=1e-6, max_iter=10, *args, **kwargs) -> float:
    """
    龙伯格积分
    """
    R = numpy.zeros((max_iter, max_iter))
    h = b - a

    R[0, 0] = 0.5 * h * (f(a, *args, **kwargs) + f(b, *args, **kwargs))

    for i in range(1, max_iter):
        h /= 2.0
        sum_f = sum(
            f(a + (k + 0.5) * h * 2, *args, **kwargs)
            for k in range(2 ** (i - 1))
        )
        R[i, 0] = 0.5 * R[i - 1, 0] + sum_f * h

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4 ** j - 1)

        if abs(R[i, i] - R[i - 1, i - 1]) < tol:
            return R[i, i]

    return R[max_iter - 1, max_iter - 1]


def gaussian_numerical_integration(f: callable, a, b, num=100, *args, **kwargs):
    """
    高斯数值积分
    """
    r = 0
    nodes, weights = numpy.polynomial.legendre.leggauss(num)

    for i, x in enumerate(nodes):
        w = weights[i]
        t = (b - a) / 2 * x + (b + a) / 2
        r += w * f(t, *args, **kwargs)
    r *= (b - a) / 2
    return r


def newton_method(f: callable, x0: Union[float, int, decimal.Decimal, numpy.floating],
                  tol=1e-6, max_iter=100, dx=1e-6, *args, **kwargs) -> tuple[float, float]:
    """
    牛顿法
    :param f:
    :param x0:
    :param tol:
    :param max_iter:
    :param dx:
    :return:
    """
    x = x0
    iter_count = 0
    while abs(f(x, *args, **kwargs)) > tol and iter_count < max_iter:
        f_prime = (f(x + dx, *args, **kwargs) - f(x, *args, **kwargs)) / dx
        if f_prime == 0:
            break
        else:
            x = x - f(x, *args, **kwargs) / f_prime
            iter_count += 1
    return x, abs(f(x, *args, **kwargs)) - tol


def adam_method(
        f: callable,
        x: Union[list, tuple, numpy.ndarray],
        y: Union[list, tuple, numpy.ndarray],
        diff: float = 1e-5,
        lr: float = 0.1,
        epoch: int = 200,
        loss: str = None,
        *args,
        **kwargs
):
    """
    简单的adam梯度下降
    """

    def mse(_x, _y):
        """
        MES损失函数, 默认
        """
        return numpy.mean((_y - f(_x, *args, **kwargs)) ** 2)

    if loss is None:
        loss = mse
    else:
        pass

    grad = [0] * len(x)
    beta1 = 0.9
    beta2 = 0.999
    epsilon = 1e-8
    m = numpy.zeros_like(x)  # 初始化一阶矩估计
    v = numpy.zeros_like(x)  # 初始化二阶矩估计
    t = 0  # 时间步长

    x = numpy.array(x)
    y = numpy.array(y)

    for ep in range(epoch):
        for i, xi in enumerate(x):
            dx_plus = xi + diff
            dx_minus = xi - diff

            x_plus = [
                xj if j != i else dx_plus for j, xj in enumerate(x)
            ]

            x_minus = [
                xj if j != i else dx_minus for j, xj in enumerate(x)
            ]

            loss_plus = loss(x_plus, y)
            loss_minus = loss(x_minus, y)

            grad[i] = (loss_plus - loss_minus) / (2 * lr)

        t += 1
        m = beta1 * m + (1 - beta1) * numpy.array(grad)
        v = beta2 * v + (1 - beta2) * (numpy.array(grad) ** 2)
        m_hat = m / (1 - beta1 ** t)
        v_hat = v / (1 - beta2 ** t)

        x -= lr * m_hat / (numpy.sqrt(v_hat) + epsilon)

    return x


if __name__ == "__main__":
    x = numpy.arange(-10, 10, 0.01)
    y = numpy.sin(x)
    data = numpy.column_stack((x, y))
    print(n_integrate(data))
    print(n_integrate2(data))
    print(simpsons_integrate(numpy.sin, 0, 10, 100))
    print(romberg_integration(numpy.sin, 0, 10))
    print(gaussian_numerical_integration(numpy.sin, 0, 10, 100))
