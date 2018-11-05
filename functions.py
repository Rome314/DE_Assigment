from math import exp, sin, cos


# Original function and it's exact solution:
def f(x, y):
    return exp(-sin(x)) - y * cos(x)


def exact(x):
    return exp(-sin(x)) + x * exp(-sin(x))


# Helping fxunctions for Runge-Kutta method:

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
