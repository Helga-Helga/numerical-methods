a = 2/3
b = 1.2
accuracy = 10**(-5)

def f(x):
    return 2 * x**5 + 3 * x**2 - 2*x - 6

def output(iteration, x, accuracy):
    print 'Iteration # {}'.format(iteration)
    print 'Approximate value {}'.format(x)
    print 'Error: {}'.format(accuracy)
