from DE_Assigment.functions_calculator import *
from matplotlib import pyplot as plt
from math import fabs

#Plotting usual graphs for each ,ethod:
#   @steps_count - accuracy value
#   @x_final - end of plotting interval
def plot_methods(steps_count, x_final):
    x_euler, y_euler = euler_solution(steps_count, x_final)
    x_exact, y_exact = exact_solution(steps_count, x_final)
    x_euler_improved, y_euler_improved = improved_euler_solution(steps_count, x_final)
    x_runge_kutta, y_runge_kutta = runge_kutta_solution(steps_count, x_final)

    plt.title("All methods result")
    plt.plot(x_euler, y_euler, label="Euler method")
    plt.plot(x_exact, y_exact, label="Exact solution")
    plt.plot(x_euler_improved, y_euler_improved, label="Improved Euler method")
    plt.plot(x_runge_kutta, y_runge_kutta, label="Runge-Kutta's method")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.legend()
    plt.show()

# Plotting local errors graphs for each method:
#   @steps_count - accuracy value
#   @x_final - end of plotting interval
def plot_local_error(steps_count, x_final):
    x_exact, y_exact = exact_solution(steps_count, x_final)
    x_euler_improved, y_euler_improved = improved_euler_solution(steps_count, x_final)
    x_euler, y_euler = euler_solution(steps_count, x_final)
    x_runge_kutta, y_runge_kutta = runge_kutta_solution(steps_count, x_final)

    runge_kutta_error = [0.0]
    euler_imp_error = [0.0]
    euler_error = [0.0]

    for i in range(steps_count):
        runge_kutta_error.append(fabs(y_exact[i] - y_runge_kutta[i]))
        euler_imp_error.append(fabs(y_exact[i] - y_euler_improved[i]))
        euler_error.append(fabs(y_exact[i] - y_euler[i]))

    plt.title("Local errors graph")
    plt.plot(x_euler, euler_error, label="Euler method")
    plt.plot(x_euler_improved, euler_imp_error, label="Improved Euler method")
    plt.plot(x_runge_kutta, runge_kutta_error, label="Runge-Kutta's method")
    plt.ylabel("Error")
    plt.xlabel("X")
    plt.legend()
    plt.show()

# Plotting global errors graphs for each method:
#   @start,end - accuracy values
#   @X - end of plotting interval

def plot_global_error(start, end, X):
    arr = [i for i in range(start, end)]
    euler_glob_err = []
    euler_imp_glob_err = []
    runge_kutta_glob_err = []
    for i in arr:
        x_euler, y_euler = euler_solution(i, X)
        x_exact, y_exact = exact_solution(i, X)
        x_euler_improved, y_euler_improved = improved_euler_solution(i, X)
        x_runge_kutta, y_runge_kutta = runge_kutta_solution(i, X)

        runge_kutta_error = 0
        euler_imp_error = 0
        euler_error = 0
        for k in range(i):
            runge_kutta_error = max((fabs(y_exact[k] - y_runge_kutta[k])), runge_kutta_error)
            euler_imp_error = max((fabs(y_exact[k] - y_euler_improved[k])), euler_imp_error)
            euler_error = max((y_exact[k] - y_euler[k]), euler_error)

        euler_glob_err.append(euler_error)
        euler_imp_glob_err.append(euler_imp_error)
        runge_kutta_glob_err.append(runge_kutta_error)

    plt.title("Global errors graph")
    plt.plot(arr, euler_glob_err, label="Euler method")
    plt.plot(arr, euler_imp_glob_err, label="Improved Euler method")
    plt.plot(arr, runge_kutta_glob_err, label="Runge-Kutta's method")
    plt.ylabel("Error")
    plt.xlabel("N")
    plt.legend()
    plt.show()
