from numpy import array, zeros_like, delete, unravel_index, nonzero, round


def solve_gauss(matrix, result):
    """
    >>> solve_gauss([[1]], [1])
    [1.0]
    >>> solve_gauss([[1, 2], [4, 1]], [5, 6])
    [1.0, 2.0]
    >>> solve_gauss([
    ...     [0, 1],
    ...     [1, 1]
    ... ], [2, 3])
    [1.0, 2.0]
    >>> solve_gauss([
    ...     [1, 0, 0],
    ...     [0, 1, 0],
    ...     [0, 0, 1],
    ... ], [1, 2, 3])
    [1.0, 2.0, 3.0]
    >>> solve_gauss([
    ...     [1, 0, 0, 0],
    ...     [0, 1, 0, 0],
    ...     [0, 0, 1, 0],
    ...     [0, 0, 0, 1],
    ... ], [1, 2, 3, 4])
    [1.0, 2.0, 3.0, 4.0]
    >>> solve_gauss([
    ...     [1, 0, 0, 0, 0],
    ...     [0, 1, 0, 0, 0],
    ...     [0, 0, 1, 0, 0],
    ...     [0, 0, 0, 1, 0],
    ...     [0, 0, 0, 0, 1],
    ... ], [1, 2, 3, 4, 5])
    [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> solve_gauss([
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [0, 0, 1],
    ... ], [6, 5, 3])
    [1.0, 2.0, 3.0]
    """
    matrix = array(matrix, dtype='f8', copy=True)
    result = array(result, dtype='f8', copy=True)
    assert matrix.ndim == 2 and matrix.shape[0] == matrix.shape[1]
    assert result.ndim == 1 and result.size == matrix.shape[0]

    n = result.size

    path = []

    while n > 0:
        i, j = argmax(abs(matrix), path)
        m = matrix[i, j]
        for k in range(matrix.shape[0]):
            if i != k and i not in path:
                el = matrix[k][j] / m
                matrix[k] -= el * matrix[i]
                result[k] -= el * result[i]
        path.append(i)
        n -= 1
        print('A:')
        print(round(matrix, 6))

    assert len(path) == result.size

    solutions = zeros_like(result)
    solved = set()

    matrix = round(matrix, 6)

    for i in path[::-1]:
        k = list(set(int(t) for t in nonzero(matrix[i])[0]) - solved)
        assert len(k) == 1, 'Found {} non-zero coefficients in {}:{}'.format(len(k), matrix[i], list(solved))
        k = k[0]
        solved.add(k)
        result[i] -= matrix[i].dot(solutions)
        result[i] /= matrix[i, k]
        solutions[k] = result[i]

    return solutions.tolist()

def argmax(matrix, ignored=()):
    result = ((0, 0), float('-inf'))
    for i in range(matrix.shape[0]):
        if i in ignored:
            continue
        for j in range(matrix.shape[1]):
            if matrix[i, j] > result[1]:
                result = ((i, j), matrix[i, j])
    return result[0]

def residuals(result, matrix, solution):
    return (result - array(matrix).dot(solution)).tolist()
