from solve import frobenius


if __name__ == '__main__':
    matrix_size = 4
    A = [[5.26, 0.10, 0.55, 1.28],
         [1.10, 4.44, 1.30, 0.16],
         [0.55, 1.30, 6.44, 2.10],
         [1.28, 0.16, 2.10, 8.10]]
    result = frobenius(A)
    #polynomial = danilevsky(result)
