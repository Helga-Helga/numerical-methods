import scipy


from runge_kutta import runge_kutta
from adams_bashford import adams_bashford

def runge_kutta_theoretical_error(h, left, right, result):
    new_result = runge_kutta(0.5 * h, left, right)[0]
    new_result = new_result[::2]
    result = scipy.array(result)
    new_result = scipy.array(new_result)
    error = abs(result - new_result) / 15.0
    return max(error)

def error(result, solution):
    result = scipy.array(result)
    solution = scipy.array(solution)
    return abs(result - solution)
