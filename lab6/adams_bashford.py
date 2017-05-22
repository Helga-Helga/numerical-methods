from runge_kutta import runge_kutta
from function import f

def adams_bashford(h, left, right):
    tmp = runge_kutta(h, left, right)[0]
    result = tmp[0:4]
    x = left
    i = 3
    x_axis = []
    while right > x:
        result.append(result[i] + h *
                  (55*f(x + 3 * h, result[i]) -
                   59*f(x + 2 * h, result[i-1]) +
                   37*f(x + h, result[i-2]) -
                   9*f(x, result[i-3])) / 24)
        x_axis.append(x)
        x += h
        i += 1
    result = result[4:len(result)]
    return x_axis, result
