from utils import *

def horde(a, b, accuracy):
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    iteration = 1
    while abs(f(c)) >= accuracy:
        output(iteration, c, abs(f(c)))
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        elif f(b) * f(c) < 0:
            a = c
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        iteration += 1
    return c

horde(a, b, accuracy)
