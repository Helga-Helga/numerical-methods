import math, scipy, numpy
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.interpolate import CubicSpline

from lagrange import f, lagrange
from newton import newton_interpolation
from spline import spline_system


if __name__ == '__main__':
    x = []
    x.append(math.pi/6)
    while x[-1] <= math.pi/2:
        x.append(x[-1] + math.pi/30)
    x = scipy.array(x)
    y = [];
    for element in x:
        y.append(f(element))
    y = scipy.array(y)

    differences = spline_system(y)

    lagrange_polynom = lagrange(x, y)

    newton = []
    for element in x:
        newton.append(newton_interpolation(x, y, element))

    cs = CubicSpline(x, y)

    plt.plot(x, lagrange_polynom(x), 'g', x, newton, 'r', x, cs(x), 'b')
    plt.legend(['Lagrange', 'Newton', 'Cubic Spline'])
    plt.title('Interpolation')
    plt.show()

    xnew = []
    xnew.append(math.pi/6)
    while xnew[-1] <= math.pi/2:
        xnew.append(xnew[-1] + math.pi/150)
    xnew = scipy.array(xnew)
    ynew = [];
    for element in xnew:
        ynew.append(f(element))
    ynew = scipy.array(ynew)

    difference_lagrange = []
    new_lagrange_polynom = lagrange(xnew, ynew)

    difference_newton = []

    difference_spline = []
    new_cs = CubicSpline(xnew, ynew)

    for element in xnew:
        difference_lagrange.append(abs(f(element) - new_lagrange_polynom(element)))
        difference_newton.append(abs(f(element) - newton_interpolation(xnew, ynew, element)))
        difference_spline.append(abs(f(element) - new_cs(element)))

    difference_lagrange = scipy.array(difference_lagrange)
    difference_newton = scipy.array(difference_newton)
    difference_spline = scipy.array(difference_spline)

    plt.plot(xnew, difference_lagrange, 'g', xnew, difference_newton, 'r', xnew, difference_spline, 'b')
    plt.legend(['Lagrange', 'Newton', 'Cubic Spline'])
    plt.title('Error')
    plt.show()
