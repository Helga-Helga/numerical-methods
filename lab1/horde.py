a = 1
b = 1.5
accuracy = 10**(-5)

def f(x):
    return 2 * x**5 + 3 * x**2 - 2*x - 6

def horde(a, b, accuracy):
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    iteration = 1
    while abs(f(c)) >= accuracy:
        print 'Iteration # {}'.format(iteration)
        print 'Approximate value {}'.format(c)
        print 'Error: {}'.format(abs(f(c)))
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        elif f(b) * f(c) < 0:
            a = c
        c = (a + b) / 2
        iteration += 1
    return c

horde(a, b, accuracy)
