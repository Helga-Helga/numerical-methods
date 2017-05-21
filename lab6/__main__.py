import matplotlib.pyplot as plt
import numpy as np


from function import f
from runge_kutta import runge_kutta

if __name__ == '__main__':
    h = 0.1
    left = 0
    right = 3
    runge_kutta_result = []
    x, runge_kutta_result = runge_kutta(h, left, right)
    print(x)
    print(runge_kutta_result)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, runge_kutta_result, 'r--', label = 'Runge-Kutta method')
    plt.legend()
    plt.grid(True)
    plt.show()
