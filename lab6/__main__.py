import matplotlib.pyplot as plt
import numpy as np
import math


from function import f
from runge_kutta import runge_kutta
from adams_bashford import adams_bashford
from error import runge_kutta_theoretical_error, error

if __name__ == '__main__':
    h = 0.1
    left = 0
    right = 3
    x, runge_kutta_result = runge_kutta(h, left, right)
    x_adams_bashford, adams_bashford_result = adams_bashford(h, left, right)
    y = []
    for element in x:
        y.append(math.exp(element))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, 'g--', label = 'True solution')
    plt.plot(x, runge_kutta_result, 'r--', label = 'Runge-Kutta method')
    plt.plot(x_adams_bashford, adams_bashford_result, 'b--', label = 'Adams-Bashford method')
    plt.legend()
    plt.grid(True)
    plt.show()

    theoretical_error = runge_kutta_theoretical_error(h, left, right, runge_kutta_result)
    print(theoretical_error)

    new_y = []
    for element in x_adams_bashford:
        new_y.append(math.exp(element))
    runge_kutta_error = error(runge_kutta_result, y)
    adams_bashford_error = error(adams_bashford_result, new_y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, runge_kutta_error, 'r--', label = 'Runge-Kutta error')
    plt.plot(x_adams_bashford, adams_bashford_error, 'b--', label = 'Adams-Bashford error')
    plt.legend()
    plt.grid(True)
    plt.show()
