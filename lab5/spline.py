import math


def spline_system(y):
    h = math.pi/30
    differences = []
    for y1, y0 in zip(y[1:], y[:-1]):
        differences.append((y1 - y0) / h)
    b = []
    for d1, d0 in zip(differences[1:], differences[:-1]):
        b.append(d1 - d0)
    print('Vector b:')
    print(b)
    return b
