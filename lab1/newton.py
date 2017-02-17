a = 1
b = 1.5
accuracy = 10**(-5)

def f(x):
    return 2 * x**5 + 3 * x**2 - 2*x - 6

def derivativeF(x):
    return 10 * x**4 + 6 * x - 2

def newton(x0, accuracy):
    iteration = 1
    while abs(f(x0)) >= accuracy:
        print 'Iteration # {}'.format(iteration)
        print 'Approximate value {}'.format(x0)
        print 'Error: {}'.format(abs(f(x0)))
        x0 = x0 - f(x0) / derivativeF(x0)
        iteration += 1
    return x0

newton(b, accuracy)
