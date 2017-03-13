from sys import argv

from numpy.random import rand
from numpy import array

from solve import solve_gauss, residuals


if __name__ == '__main__':
    matrix_size = 4
    A = [[3.81, 0.25, 1.28, 1.75],
         [2.25, 1.32, 5.58, 0.49],
         [5.31, 7.28, 0.98, 1.04],
         [10.39, 2.45, 3.35, 2.28]]
    b = [4.21, 7.47, 2.38, 11.48]
    result = solve_gauss(A, b)
    vector = residuals(b, A, result)
    print 'Solution:', ' '.join(['{:> .06f}'.format(r) for r in result])
    print 'Vector of residuals:', ' '.join(str(v) for v in vector)
