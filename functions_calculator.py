from .functions import *

# Kere functions to find x's and y's for each function in range [X0:X]
# Where:
#   X0 = -5
#   X = final_x(You can change it in main function)

def exact_solution(steps_count, final_x):
    x = [-5.0]  # x0
    y = [2.0]  # y0

    h = (final_x - x[0]) / steps_count

    for i in range(steps_count):
        x.append(x[i] + h)
        y.append(exact(x[i]))
    y.append(exact(x[-1]))
    return x, y


def runge_kutta_solution(steps_count, final_x):
    x = [-5.0]  # x0
    y = [2.0]  # y0

    h = (final_x - x[0]) / steps_count

    for i in range(steps_count):
        x.append(x[i] + h)
        y.append(y[i] + rk_delta(x[i], y[i], h))
    return x, y


def improved_euler_solution(steps_count, final_x):
    x = [-5.0]  # x0
    y = [2.0]  # y0

    h = (final_x - x[0]) / steps_count

    for i in range(steps_count):
        x.append(x[i] + h)
        y.append(y[i] + imp_Euler_delta(x[i], y[i], h))
    return x, y
