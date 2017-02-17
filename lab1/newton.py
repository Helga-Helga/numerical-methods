from utils import *

def derivativeF(x):
    return 10 * x**4 + 6 * x - 2

def newton(x0, accuracy):
    iteration = 1
    while abs(f(x0)) >= accuracy:
        output(iteration, x0, abs(f(x0)))
        x0 = x0 - f(x0) / derivativeF(x0)
        iteration += 1
    return x0

newton(b, accuracy)
