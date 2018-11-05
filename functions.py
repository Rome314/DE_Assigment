from math import exp


# Original function and it's exact solution:
def f(x, y):
    return (1 - 2 * y) * exp(x) + y * y + exp(2 * x)


# assypmtot = (5 - 9 * exp(5)) / (2 * exp(5) - 1)


def exact(x):
    return (-exp(x) * (x + 5) + exp(x + 5) * (2 * x + 9) - (2 * exp(5)) + 1) / (-x + exp(5) * (2 * x + 9) - 5)


# Helping functions for Runge-Kutta method:

def k1(x, y):
    return f(x, y)


def k2(x, y, h):
    return f(x + h / 2, y + h * k1(x, y) / 2)


def k3(x, y, h):
    return f(x + h / 2, y + h * k2(x, y, h) / 2)


def k4(x, y, h):
    return f(x + h, y + h * k3(x, y, h))


def rk_delta(x, y, h):
    return h / 6 * (k1(x, y) + 2 * k2(x, y, h) + 2 * k3(x, y, h) + k4(x, y, h))


# Helping function for improved Euler method:

def imp_Euler_delta(x, y, h):
    return h * f(x + h / 2, y + h / 2 * f(x, y))


