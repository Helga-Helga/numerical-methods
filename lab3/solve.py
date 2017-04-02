from numpy import array, zeros_like

def iteration(matrix, result, accuracy):
    matrix = array(matrix, dtype='f8', copy=True)
    result = array(result, dtype='f8', copy=True)
    assert matrix.ndim == 2 and matrix.shape[0] == matrix.shape[1]
    assert result.ndim == 1 and result.size == matrix.shape[0]

    solution = zeros_like(result)

    iteration = 1
    while True:
        solution_prev, solution = solution, matrix.dot(solution) + result
        print 'Iteration: {}'.format(iteration)
        print 'Solution:', ' '.join(['{:> .016f}'.format(r) for r in solution])
        vector = residuals(solution)
        print 'Vector of residuals:', ' '.join(str(v) for v in vector)
        print 'Error: {}'.format(max(abs(solution - solution_prev))/(1 - max(abs(matrix).sum(axis=1))))
        if max(abs(solution - solution_prev))/(1 - max(abs(matrix).sum(axis=1))) < accuracy:
            break
        iteration += 1

    return solution.tolist()

def residuals(solution):
    A = [[10.39, 2.45, 3.35, 2.28],
         [1.5, 7.03, -0.3, -0.71],
         [2.25, 1.32, 5.58, 0.49],
         [3.11, 14.35, -0.08, -18.51]]
    b = [11.48, -1.83, 7.47, 3.43]
    return (b - array(A).dot(solution)).tolist()
