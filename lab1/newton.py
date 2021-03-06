from utils import *

def derivativeF(x):
    return 10 * x**4 + 6 * x - 2

def derivative2F(x):
    return 40 * x**3 + 6

def newton(x0, accuracy):
    iteration = 1
    while True:
        output(iteration, x0, abs(f(x0)))
        x0_prev, x0 = x0, x0 - f(x0) / derivativeF(x0)
        if abs(x0_prev - x0) < accuracy or abs(f(x0)) < accuracy:
            break
        iteration += 1
    return x0

if f(a) * derivative2F(a) > 0:
    newton(a, accuracy)
elif f(b) * derivative2F(b) > 0:
    newton(b, accuracy)
