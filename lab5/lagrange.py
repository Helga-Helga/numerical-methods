import scipy, numpy, math
import matplotlib.pyplot as plt


def f(x):
    return 1 / math.sin(x)

def lagrange(x, y):
    result = scipy.poly1d([0.0]) #setting result = 0

    for i in range(0,len(x)): #number of polynomials L_k(x).
        temp_numerator = scipy.poly1d([1.0]) # resets temp_numerator such that a new numerator can be created for each i.
        denumerator = 1.0 #resets denumerator such that a new denumerator can be created for each i.
        for j in range(0,len(x)):
            if i != j:
                temp_numerator *= scipy.poly1d([1.0,-x[j]]) #finds numerator for L_i
                denumerator *= x[i]-x[j] #finds denumerator for L_i
        result += (temp_numerator/denumerator) * y[i] #linear combination
    return result
