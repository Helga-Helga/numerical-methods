from sympy import *


x, y, z, t = symbols('x y z t')
p = []

p.append(x**4 + 3*x**3 - 21*x**2 - 43*x + 60)
p.append(4*x**3 + 9*x**2 - 42*x - 43)

for i in range(3):
    q, r = div(p[i], p[i + 1])
    p.append(-r)

for i, P in enumerate(p):
    print('P{} = {}'.format(i, P))
